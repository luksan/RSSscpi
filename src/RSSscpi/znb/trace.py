from math import floor, log10
import re
from typing import List

from ..gen import ZNB_gen
from ..scpi.class_property import SCPIProperty
from .diagram import Diagram

from .. import znb


class MeasParam:
    """
    Helper functions for creating the strings that define a measurement parameter.
    """

    @classmethod
    def S(cls, dst_port: int, src_port: int, detector="") -> str:
        """
        S-parameter measurement.

        :param int dst_port: Receiving port index, S21 -> 2
        :param int src_port: Transmitting port index, S21 -> 1
        :param str detector: SAM (sample/normal) or AVG (complex averaging)
        """
        port_digits = cls._port_digit_count(dst_port, src_port)
        detector = detector.upper()
        if detector and detector not in ("SAM", "AVG"):
            raise ValueError("The S-parameter detector must be SAM or AVG")
        return "S{0:0{pad}d}{1:0{pad}d}{2!s}".format(
            dst_port, src_port, detector, pad=port_digits
        )

    @classmethod
    def Ratio(
        cls,
        numerator_rec: str,
        numerator_port: int,
        denominator_rec: str,
        denominator_port: int,
        src_port: int,
        detector: str = "",
    ) -> str:
        """
        A measurement of the ratio between two receivers.

        :param str numerator_rec: A, B, AP or BP, the P means primed detector, available in ZVA and ZNA.
        :param int numerator_port: port index
        :param str denominator_rec: see above
        :param int denominator_port: port index
        :param int src_port: Port index of the port generating the stimuli signal.
        :param str detector: SAM, AVG, AMP or RMS
        """

        port_digits = cls._port_digit_count(numerator_port, denominator_port, src_port)
        num = cls.Wave(
            numerator_rec, numerator_port, src_port, port_digit_count=port_digits
        )
        denom = cls.Wave(
            denominator_rec,
            denominator_port,
            src_port,
            detector=detector,
            port_digit_count=port_digits,
        )
        return "/".join((num, denom))

    @classmethod
    def Wave(
        cls,
        receiver: str,
        dst_port: int,
        src_port: int,
        detector: str = "",
        *,
        port_digit_count: int = None
    ) -> str:
        """
        A wave quantity

        :param str receiver: A, B, AP, BP
        :param int dst_port: Index of receiving port
        :param int src_port: Index of port generating the stimuli
        :param str detector: Detector type, SAM, AVG, AMP, RMS
        :param port_digit_count: internal use only
        """
        receiver = receiver.upper()
        detector = detector.upper()
        if detector and detector not in ("SAM", "AVG", "AMP", "RMS"):
            raise ValueError("'{:}' is not a valid detector".format(detector))
        if not port_digit_count:
            port_digit_count = cls._port_digit_count(dst_port, src_port)
        return "{0!s}{1:0{pad}d}D{2:0{pad}d}{3!s}".format(
            receiver, dst_port, src_port, detector, pad=port_digit_count
        )

    @staticmethod
    def _port_digit_count(*ports: int) -> int:
        return floor(log10(max(ports))) + 1


class Trace:
    """
    A class representing a trace on the VNA. Instances are obtained via Channel.create_trace() and Channel.get_trace()
    """

    MeasParam = MeasParam

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

    def copy(self, new_name: str, diagram: Diagram = None) -> "Trace":
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

    def set_scaling(self, *,
                    scale_div: float = None,
                    top: float = None,
                    bottom: float = None,
                    ref_level: float = None,
                    ref_pos: float = None):
        """
        Parameter coupling:

        * top -> scaling, reference level
        * bottom -> scaling, reference level
        * scaling -> top, bottom
        * reference level -> top, bottom
        * reference position -> top, bottom

        :param scale_div:
        :param top:
        :param bottom:
        :param ref_level:
        :param ref_pos:
        :return:
        """
        scale_check = 0

        def check_scaling(new_scale):
            nonlocal scale_check
            if new_scale <= 0:
                raise ValueError("Scaling must be larger than 0.")
            if scale_check:
                if new_scale != scale_check:
                    raise ValueError("Settings conflic results in different y axis ranges")
            scale_check = new_scale

        if ref_pos is not None:
            if not 0 <= ref_pos <= 100:
                raise ValueError("ref_pos must be in range [0-100]")

        if scale_div is not None:
            check_scaling(scale_div)

        set_top_before_bottom = False
        if None not in (top, bottom):
            if top <= bottom:
                raise ValueError("top must be greater than bottom")
            check_scaling((top - bottom) / 10.0)

            if ref_level is not None:
                if not bottom <= ref_level <= top:
                    raise ValueError("ref_level is outside specified bottom-top range")
            else:
                # When setting both top and bottom
                # check that we don't try to set a new bottom value higher than the current top
                if self.scale_top <= bottom:
                    set_top_before_bottom = True

        if scale_check and None not in (ref_level, ref_pos):
            # check that the ref level doesn't conflict with other settings
            rp = ref_pos / 10.0
            if (top is not None and top - (10 - rp) * scale_check != ref_level) or (
                    bottom is not None and bottom + rp * scale_check != ref_level):
                raise ValueError("Y axis scaling parameters conflict")

        if ref_pos is not None:
            self.ref_pos = ref_pos
        if ref_level is not None:
            self.ref_level = ref_level
        if scale_div is not None:
            self.scale_per_div = scale_div
        if set_top_before_bottom:
            if top is not None:
                self.scale_top = top
            if bottom is not None:
                self.scale_bottom = bottom
        else:
            if bottom is not None:
                self.scale_bottom = bottom
            if top is not None:
                self.scale_top = top

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
        diagram.WINDow.TRACe.EFEed.w(self.name)

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
    state = SCPIProperty(_MKR.STATe, bool, callback=_prop_callback)
    """Enable/disable the marker"""
    #: Marker position
    x = SCPIProperty(_MKR.X, float, callback=_prop_callback)
    #: Marker value
    y = SCPIProperty(_MKR.Y, float, callback=_prop_callback)

    format = SCPIProperty(_MKR.FORMat, str, callback=_prop_callback)
    """Get/set the y-value display format for the marker"""


class Limit(ZNB_gen.CALCulate.LIMit):
    def __init__(self, trace):
        """
        :param Trace trace: The trace which the limit applies to
        """
        super(Limit, self).__init__(parent=trace.channel.CALC)
        self.trace = trace
