from math import floor, log10
import re
from typing import List

from ..SCPI_property import SCPIProperty
from ..gen import ZNB_gen
from .diagram import Diagram

from .. import znb


class MeasParamBase(object):
    def __init__(self, dst_port, src_port, detector=""):
        self.dst_port = int(dst_port)
        self.src_port = int(src_port)
        self.detector = str(detector).upper()
        self.port_digits = floor(log10(max(self.src_port, self.dst_port))) + 1


class Trace(object):
    """
    A class representing a trace on the VNA. Instances are obtained via Channel.create_trace() and Channel.get_trace()
    """

    class MeasParam(object):
        class S(MeasParamBase):
            def __str__(self):
                return "S{0.dst_port:0{pad}d}{0.src_port:0{pad}d}{0.detector!s}".format(self, pad=self.port_digits)

        class Wave(MeasParamBase):
            def __init__(self, receiver, dst_port, src_port, detector=""):
                super(Trace.MeasParam.Wave, self).__init__(dst_port, src_port, detector)
                self.receiver = str(receiver).upper()

            def __str__(self):
                return "{0.receiver!s}{0.dst_port:0{pad}d}D{0.src_port:0{pad}d}{0.detector!s}".format(self, pad=self.port_digits)

    def __init__(self, name: str, channel: "znb.Channel"):
        """
        :param name: The trace name
        :param Channel channel: The channel the trace belongs to
        """
        self._n = None
        self._name = str(name)
        self.check_if_name_is_valid(self._name, raise_err=True)
        self.channel = channel
        self._cmd_cnt = None

    def _calc_node(self):
        return self.channel.CALC

    def _corr_node(self):
        return self.channel.SENSe.CORRection

    def _sweep_node(self):
        return self.channel.SENSe.SWEep

    def _disp_node(self):
        return self.channel.instrument.DISPlay

    # noinspection PyUnusedLocal
    def _make_active_cb(self, *args, **kwargs):
        if self._cmd_cnt != self.channel.instrument.command_cnt:
            self.select_trace()
        self._cmd_cnt = self.channel.instrument.command_cnt + 1

    def autoscale(self):
        """
        Activate the autoscaling function for the trace
        """
        self.channel.instrument.DISPlay.WINDow.TRACe.Y.SCALe.AUTO.w("ONCE", self.name, fmt="{:s}, {:q}")

    def copy_data_to_mem(self, target_trace_name):
        self.check_if_name_is_valid(target_trace_name, raise_err=True)
        self.channel.instrument.TRACe.COPY.w(target_trace_name, self.name)
        return self.__class__(target_trace_name, self.channel)

    def copy_math_to_mem(self, target_trace_name):
        self.check_if_name_is_valid(target_trace_name, raise_err=True)
        self.channel.instrument.TRACe.COPY.MATH.w(target_trace_name, self.name)
        return self.__class__(target_trace_name, self.channel)

    def copy(self, new_name: str, diagram: "Diagram" = None) -> "Trace":
        """
        Create a copy of the trace. If the diagram parameter is provided the new trace will be assigned to
        that diagram.

        :param str new_name: The name of the new trace
        :param diagram: (optional)
        :return: A new Trace instance
        """
        self.check_if_name_is_valid(new_name, raise_err=True)
        meas = self.measurement
        tr = self.channel.create_trace(new_name, meas)
        if diagram:
            tr.assign_diagram(diagram)
        return tr

    def copy_assign_math(self, new_name, equation, diagram=None):
        tr = self.copy(new_name, diagram)
        tr.math_equation = equation
        tr.math_is_enabled = True
        return tr

    def delete(self):
        """
        Deletes the trace. CALCulate<Ch>:​PARameter:​DELete
        """
        self.channel.CALC.PARameter.DELete.w(self.name)

    @property
    def measurement(self):
        """
        A string describing the measurement associated with the trace.
        See CALCulate<Ch>:PARameter:SDEFine for all possible options.

        Use the Trace.MeasParam... helpers for easier use.

        Example: tr1.measurement = tr1.MeasParam.Wave("b", 1, src_port=1, detector="sam")
        """
        return str(self.channel.CALC.PARameter.MEASure.q(self.name))

    @measurement.setter
    def measurement(self, param):
        self.channel.CALC.PARameter.MEASure.w(self.name, str(param))

    @property
    def name(self) -> str:
        """
        The trace name, must be unique in the recall set.
        """
        return self._name

    @name.setter
    def name(self, name):
        name = str(name)
        self.check_if_name_is_valid(name, raise_err=True)
        self.channel.instrument.CONFigure.TRACe.REName.w(self.name, name)
        self._name = name

    @staticmethod
    def check_if_name_is_valid(name: str, raise_err: bool = False) -> bool:
        """
        The first character of a trace name can be either one of the upper case letters A to Z, one of the lower case letters a to z, an underscore _ or a square bracket [ or ].
        For all other characters of a trace name, the numbers 0 to 9 can be used in addition.

        :param name: A string which will be checked to see if it is a valid trace name
        :param raise_err: Raise a ValueError if the name is invalid
        """
        ret = re.match(r"^[A-Za-z\[\]_][A-Za-z\[\]_0-9]*$", name) is not None
        if not ret and raise_err:
            raise ValueError("Invalid trace name '%s'" % name)
        return ret

    @property
    def n(self):
        """
        :return: CONFigure.TRACe.NAME.ID?
        """
        if not self._n:  # The trace number doesn't change with trace add/delete, so it's ok to cache it.
            self._n = int(self.channel.instrument.CONFigure.TRACe.NAME.ID.q(self.name))
        return self._n

    def query_cal_state_label(self):
        """
        Returns the system error correction state label for the trace as a string.
        """
        self._make_active_cb()
        return str(self._corr_node().SSTate.q())

    # TODO: argument checking?
    trace_format = SCPIProperty(ZNB_gen.CALCulate.FORMat, str, callback=_make_active_cb, get_root_node=_calc_node)

    # noinspection PyUnusedLocal
    def _add_trace_name_arg_cb(self, value=None, **kwargs):
        ret = {"name": self.name}
        if value is None:  # The command form with trace name only works for setting the value, not querying it
            self._make_active_cb()
            ret = {}
        else:
            ret["value"] = value
            ret["fmt"] = "{value:s}, {name:q}"
        return ret

    _SCALE = ZNB_gen.DISPlay.WINDow.TRACe.Y.SCALe
    scale_per_div = SCPIProperty(_SCALE.PDIVision, float, callback=_add_trace_name_arg_cb, get_root_node=_disp_node)
    scale_top = SCPIProperty(_SCALE.TOP, float, callback=_add_trace_name_arg_cb, get_root_node=_disp_node)
    scale_bottom = SCPIProperty(_SCALE.BOTTom, float, callback=_add_trace_name_arg_cb, get_root_node=_disp_node)
    ref_level = SCPIProperty(_SCALE.RLEVel, float, callback=_add_trace_name_arg_cb, get_root_node=_disp_node)
    ref_pos = SCPIProperty(_SCALE.RPOSition, float, callback=_add_trace_name_arg_cb, get_root_node=_disp_node)
    """
    The reference position of the trace on the screen specified in percent,
    where 0 is the bottom and 100 is the top of the screen.
    """

    source_port = SCPIProperty(ZNB_gen.SENSe.SWEep.SRCPort, int, callback=_make_active_cb,
                               get_root_node=_sweep_node)  # Logical port number of the simulus port

    math_equation = SCPIProperty(ZNB_gen.CALCulate.MATH.EXPRession.SDEFine, str, callback=_make_active_cb,
                                 get_root_node=_calc_node)
    math_is_enabled = SCPIProperty(ZNB_gen.CALCulate.MATH.STATe, bool, callback=_make_active_cb,
                                   get_root_node=_calc_node)
    math_is_wave_quantity = SCPIProperty(ZNB_gen.CALCulate.MATH.WUNit.STATe, bool, callback=_make_active_cb,
                                         get_root_node=_calc_node)

    def is_active(self):
        return self.channel.active_trace.name == self.name

    def select_trace(self):
        """
        Makes the trace the active trace in the channel.
        """
        self.channel.CALC.PARameter.SELect.w(self.name)

    def get_marker(self, n):
        """

        :param n: Marker number
        :rtype: Marker
        """
        return Marker(n, self)

    def assign_diagram(self, diagram):
        """
        Assigns the trace to a diagram.

        :param diagram: An existing Diagram area
        :type diagram: Diagram
        """
        diagram.state = True
        diagram.TRACe.EFEed.w(self.name)

    def query_multiple_sweep_data(self, first_sweep: int, last_sweep: int = None) -> List[List[complex]]:
        """
        This function is used to read back trace data when the instrument is setup to perform multiple
        sweeps in single sweep mode.

        It does not work if the instrument is in continiuous sweep mode, or if the sweep count is 1.

        :param int first_sweep: The number of the first sweep to return, starting from 1
        :param int last_sweep: The number of the last sweep, or None. If None, only one sweep is returned.
        :return: A list of lists of complex trace data
        """
        assert first_sweep >= 1
        if last_sweep is None:
            last_sweep = first_sweep
        sweep_cnt = last_sweep - first_sweep + 1
        assert sweep_cnt >= 1

        self._make_active_cb()
        response = self.channel.CALC.DATA.NSWeep.FIRSt.q("SDATa", first_sweep, last_sweep)
        # The response is a list of (real, imag) values, with all requested traces concatenated
        cplx_list = response.complex_list(float_size=4)  # Assuming 32 bit float
        sweep_pts = len(cplx_list) // sweep_cnt
        if sweep_cnt * sweep_pts != len(cplx_list):
            raise ValueError("Invalid number of sweep points from instrument")
        return [cplx_list[n * sweep_pts:(n + 1) * sweep_pts] for n in range(sweep_cnt)]


class Marker(ZNB_gen.CALCulate.MARKer):
    """
    Represents a trace marker in the VNA.
    Property access will make the trace associated with the marker the active trace in the channel.
    """

    def __init__(self, n, trace):
        """
        :param n: Marker number
        :param trace: The trace which the marker belongs to
        :type trace: Trace
        """
        super(Marker, self).__init__(parent=trace.channel.CALC)
        self.n = n
        self.trace = trace
        self._cmd_cnt = None

    # noinspection PyUnusedLocal
    def _prop_callback(self, *args, **kwargs):
        if not self._cmd_cnt or self._cmd_cnt != self.trace.channel.instrument.command_cnt:
            self.trace.select_trace()
        self._cmd_cnt = self.trace.channel.instrument.command_cnt + 1

    _MKR = ZNB_gen.CALCulate.MARKer
    tracking = SCPIProperty(_MKR.SEARch.TRACking, bool, callback=_prop_callback)  #: Marker tracking enabled
    is_enabled = SCPIProperty(_MKR.STATe, bool, callback=_prop_callback)
    """Enable/disable the marker"""
    #: Marker position
    x = SCPIProperty(_MKR.X, float, callback=_prop_callback)
    #: Marker value
    y = SCPIProperty(_MKR.Y, float, callback=_prop_callback)


class Limit(ZNB_gen.CALCulate.LIMit):
    def __init__(self, trace):
        """
        :param Trace trace: The trace which the limit applies to
        """
        super(Limit, self).__init__(parent=trace.channel.CALC)
        self.trace = trace
