# -*- coding: utf-8 -*-
"""
Created on 16 feb. 2016

@author: Lukas Sandström
"""

from .gen import ZNB_gen
from .SCPI_property import SCPIProperty, SCPIPropertyMinMax, SCPIPropertyMapping

import ntpath
import os.path

import logging


class ZNB(ZNB_gen):
    def __init__(self, visa_res):
        super(ZNB, self).__init__(visa_res)
        self.filesystem = self.Filesystem(self)
        self.logger = logging.getLogger(__name__)
        self.visa_logger = self.logger.getChild("VISA")

    def init(self):
        super(ZNB, self).init()
        self.SYSTem.COMMunicate.GPIB.SELF.RTERminator().w("EOI")
        try:
            self.SYSTem.COMMunicate.CODec().w("UTF8")  # Set the character encoding
        except AttributeError:
            # FIXME: subclass this properly
            pass  # This command isn't available on ZVA
        orig_lang = str(self.SYSTem.LANGuage().q())
        if orig_lang != "SCPI":
            self.visa_logger.warning("Changing remote language from '%s' to 'SCPI' (default)", orig_lang)
            self.SYSTem.LANGuage().w("SCPI")

    def set_source_power_offset(self, channel=None, src=0, power=-300, relative=True):
        # FIXME: remove this method from ZNB(), put in Channel
        if relative:
            x = 'CPAD'
        else:
            x = 'ONLY'
        self.SOURce(channel).POWer(src).LEVel.IMMediate.OFFSet().w(power, x)

    @property
    def active_channel(self):
        """
        Get the active channel, INSTrument:NSELect? \n
        :return: ZNB.Channel
        """
        return self.get_channel(int(self.INSTrument.NSELect().q()))

    @active_channel.setter
    def active_channel(self, n):
        """
        Set the active channel, INSTrument:NSELect n \n
        :param n: (int, str, Channel)
        :return: None
        """
        if hasattr(n, "n"):
            n = n.n
        self.INSTrument.NSELect().w(n)

    def get_channel(self, n):
        """

        :param n: Channel number
        :rtype: ZNB.Channel
        """
        return self.Channel(n, self)

    def get_diagram(self, n):
        """

        :param n: The diagram id, Wnd
        :rtype: ZNB.Diagram
        """
        return self.Diagram(n, self)

    def save_screenshot(self, filename, diagram=None):
        """
        Take a screenshot containing only this diagram. The file type is inferred from the filename extension,
        valid options are BMP, EMF, EWMF, JPG, PDF, PNG, SVG, WMF.

        :param str filename: The filename under which the screenshot will be saved on the instrument.
        :param Diagram diagram: The diagram to be captured. The whole screen will be captured if None.
        :return: a File object representing the captured screenshot
        :rtype: File
        """
        _, filetype = ntpath.splitext(filename)
        filetype = filetype[1:].upper()
        if filetype not in self.HCOPy.DEVice.LANGuage.args:
            raise ValueError("Invalid file extension for screenshot: " + filetype)
        self.MMEMory.NAME().w(filename)  # Define the filename
        self.HCOPy.DESTination().w("MMEM")  # Print to mass storage
        self.HCOPy.DEVice.LANGuage().w(filetype)  # Define the file type
        if diagram is not None:
            diagram.select_diagram()
            self.HCOPy.PAGE.WINDow().w("ACTive")  # Print only the active diagram
        else:
            self.HCOPy.PAGE.WINDow().w("HARDcopy")
        self.HCOPy.IMMediate().w()  # Perform the screen capture
        return self.filesystem.file(filename)

    class Channel(object):
        def __init__(self, n, instrument):
            """
            :param n: Channel number
            :param instrument: A SCPINode instance, linked to the instrument
            :type instrument: ZNB
            """
            self.n = n
            self.instrument = instrument
            self.CALC = instrument.CALCulate(n)
            self.CONFch = instrument.CONFigure.CHANnel(n)
            self.SENSe = instrument.SENSe(n)
            self.CORRection = instrument.SENSe(n).CORRection
            self.SOURce = instrument.SOURce(n)
            self.TRIGger = instrument.TRIGger(n)  # type: ZNB_gen.TRIGger

            self.sweep = instrument.Sweep(self)  # type: ZNB.Sweep

        name = SCPIProperty(ZNB_gen.CONFigure.CHANnel.NAME, str, get_root_node=lambda self: self.CONFch)
        """
        The channel name, CONFigure:CHANnel<Ch>:NAME
        """

        def get_trace(self, name):
            """

            :param name: The name of the trace
            :rtype: ZNB.Trace
            """
            return self.instrument.Trace(name, self)

        def create_trace(self, name, parameter, diagram=None):
            """
            Create a new trace with a measurement parameter according to CALCulate<Ch>:PARameter:SDEFine

            :param name: The trace name
            :param parameter: A string defining the measured quantity
            :param diagram: An optional Diagram, which the trace will be assigned to
            :type diagram: Diagram
            :return: A reference to the new trace
            :rtype: Trace
            """
            self.CALC.PARameter.SDEFine().w(name, parameter)
            trace = self.get_trace(name)
            if diagram is not None:
                trace.assign_diagram(diagram)
            return trace

        @property
        def active_trace(self):
            """
            Query or set the active trace in the channel

            :rtype: Trace
            """
            name = str(self.CALC.PARameter.SELect().q())
            # n = self.instrument.CONFigure.TRACe.CHANnel.NAME.ID.q(name)
            return self.get_trace(name)

        @active_trace.setter
        def active_trace(self, trace):
            name = trace.name if isinstance(trace, self.instrument.Trace) else str(trace)
            self.CALC.PARameter.SELect().w(name)

        power_level = SCPIProperty(ZNB_gen.SOURce.POWer.LEVel.IMMediate.AMPLitude, float, get_root_node=lambda self: self.SOURce)  # type: float
        """
        The channel power level, in dBm.
        """

        def cal_auto(self, vna_ports, cal_unit_ports=None, cal_type="FNPort", cal_unit_characterization=""):
            if cal_unit_ports:
                cmd_fmt = "{:s}, {:q}, {:d**}"
                self.CORRection.COLLect.AUTO.PORTs.TYPE().w(
                    cal_type, cal_unit_characterization, zip(vna_ports, cal_unit_ports), fmt=cmd_fmt)
            else:
                cmd_fmt = "{:s}, {:q}, {:d*}"
                self.CORRection.COLLect.AUTO.TYPE().w(cal_type, cal_unit_characterization, vna_ports, fmt=cmd_fmt)

        def configure_freq_sweep(self, start_freq, stop_freq, points=None, ifbw=None, power=None, log_sweep=False):
            """
            Configure the instrument for a frequency sweep. Parameters which are not provided are left as is.

            :param float start_freq: Start frequency
            :param float stop_freq: Stop frequency
            :param int points: Number of sweep points
            :param float ifbw: Measurement IF bandwidth
            :param float power: Channel power setting, in dBm
            :param bool log_sweep: Sets the sweep type to LOGarithmic if True, LINear if False (default).
            """
            if not log_sweep:
                self.SENSe.SWEep.TYPE().w("LIN")
            else:
                self.SENSe.SWEep.TYPE().w("LOG")

            self.SENSe.FREQuency.STARt().w(start_freq)
            self.SENSe.FREQuency.STOP().w(stop_freq)
            if points is not None:
                self.sweep.points = points
            if ifbw is not None:
                self.SENSe.BANDwidth().w(ifbw)
            if power is not None:
                self.power_level = power

        def init_sweep(self):  # FIXME: rename to start_sweep() or similar??
            """
            INITiate:IMMediate

            This is valid in single sweep mode only.
            """
            self.instrument.INITiate(self.n).IMMediate().w()

        def save_touchstone(self, filename, ports, fmt="LOGPhase", mode_impedance="CIMPedance"):
            """
            Save the S-parameters for the selected ports to a Touchstone file on the instrument.
            MMEMory:STORe:TRACe:PORTs

            :param filename: Desired filename
            :type filename: str
            :param ports: List of integers designating the logical ports which shall be included in the file
            :param fmt: Data format of the Touchstone file, default is "LOGPhase". "COMPlex" and "LINPhase" are the alternatives.
            :param mode_impedance: "CIMPedance" (default) or "PIMPedance". Determines if port impedances are renormalized according to common target impedance (50 ohm) or the individual port impedances.
            :return: A File object representing the stored file
            :rtype: ZNB.File
            """
            cmd_fmt = "{:d}, {:q}, {:s}, {:s}, {:d*}"
            self.instrument.MMEMory.STORe.TRACe.PORTs().w(self.n, filename, fmt, mode_impedance, ports, fmt=cmd_fmt)
            return self.instrument.File(self.instrument, filename)

    class SweepSegment(ZNB_gen.SENSe.SEGMent):
        def __init__(self, n, channel):
            """
            :param n: The sweep segment number
            :param Channel channel:
            """
            super(ZNB.SweepSegment, self).__init__(parent=channel.SENSe)
            self.channel = channel
            self.n = n

        def delete(self):
            self.DELete().w()

        _SEG = ZNB_gen.SENSe.SEGMent
        dwell_time = SCPIProperty(_SEG.SWEep.DWELl, float)
        is_enabled = SCPIProperty(_SEG.STATe, bool)
        freq_start = SCPIProperty(_SEG.FREQuency.STARt, float)
        freq_stop = SCPIProperty(_SEG.FREQuency.STOP, float)
        if_bandwidth = SCPIProperty(_SEG.BWIDth.RESolution, float)
        # if_gain = SCPIProperty(_SEG.POWer.GAINcontrol, str)  # TODO: this behaves differently from the other per segment settings...
        if_selectivity = SCPIProperty(_SEG.BWIDth.RESolution.SELect, str)
        number_of_points = SCPIProperty(_SEG.SWEep.POINts, int)
        power_level = SCPIProperty(_SEG.POWer, float)
        sweep_time = SCPIProperty(_SEG.SWEep.TIME, float)  # type: float
        analog_sweep_is_enabled = SCPIPropertyMapping(_SEG.SWEep.GENeration, str, {"ANALog": True, "STEPped": False})

    class SweepSegments(object):
        def __init__(self, channel):
            """
            :param ZNB.Channel channel: The channel which the sweep segments belong to
            """
            self.channel = channel
            self._SEG = self.channel.SENSe.SEGMent
            self._seg_type = channel.instrument.SweepSegment

        def __len__(self):
            return int(self._SEG.COUNt().q())

        def __getitem__(self, item):
            if isinstance(item, slice):
                return [self._seg_type(x + 1, self.channel) for x in range(*item.indices(len(self)))]
            return self._seg_type(item + 1, self.channel)

        def __delitem__(self, key):
            if isinstance(key, slice):
                r = list(range(*key.indices(len(self))))
                r.sort(reverse=True)  # Make sure we delete the segments in descending order
                for x in r:
                    del self[x]
            else:
                self[key].delete()

        def __iter__(self):
            for x in range(len(self)):
                yield self[x]

        def insert_segment(self, start_freq, stop_freq, points, ifbw, power, time="AUTO",
                           lo_sideband="AUTO", if_selectivity="NORMal", analog_sweep=False, position=0):
            """

            :param float start_freq: Segment start frequency in Hz
            :param float stop_freq: Segment stop frequency in Hz
            :param int points: Number of sweep points in the segment
            :param float ifbw: IF bandwidth
            :param float power: Segment source power in dBm
            :param float time: Segment sweep time or segment dwell time in seconds
            :param str lo_sideband: "POSitive" | "NEGative" | "AUTO" (default)
            :param str if_selectivity: "NORMal" (default) | "MEDium" | "HIGH"
            :param bool analog_sweep: Sets the generator sweep type for the segment, "STEPped" (False) or "ANALog" (True)
            :param int position: The position in the segment list which the created segment will be inserted at. Default is 0 (top).
            :return:
            """
            if analog_sweep:
                sweep_mode = "ANALog"
            else:
                sweep_mode = "STEPped"
            self._SEG(position + 1).INSert().w(start_freq, stop_freq, points, power, time, "0", ifbw, lo_sideband, if_selectivity, sweep_mode)
            return self._seg_type(position, self.channel)

        def remove_segment(self, n):
            """
            Remove segment number <n> from the segment list. The same as del Segments[n]

            :param n: Segment index or slice, [0, len(segments))
            """
            del self[n]

        def remove_all_segments(self):
            self._SEG.DELete.ALL().w()

        def disable_per_segment_dwell_time(self):
            self._SEG.SWEep.DWELl.CONTrol().w(False)

        def disable_per_segment_if_selectivity(self):
            self._SEG.BWIDth.RESolution.SELect.CONTrol().w(False)

        def disable_per_segment_power(self):
            self._SEG.POWer.LEVel.CONTrol().w(False)

        def disable_per_segment_sweep_time(self):
            self._SEG.SWEep.TIME.CONTrol().w(False)

        def query_total_sweep_time(self):
            return float(self._SEG.SWEep.TIME.SUM().q())

    class Sweep(ZNB_gen.SENSe.SWEep):
        LIN = "LIN"  # FIXME: use enum instead
        LOG = "LOG"
        POWER = "POW"
        CW = "CW"
        POINT = "POIN"
        SEGMENT = "SEGM"

        def __init__(self, channel):
            """

            :param Channel channel:
            """
            super(ZNB.Sweep, self).__init__(parent=channel.SENSe)
            self.channel = channel
            self.segments = self.channel.instrument.SweepSegments(self.channel)  # type: ZNB.SweepSegments

        _SWE = ZNB_gen.SENSe.SWEep

        analog_sweep_is_enabled = SCPIPropertyMapping(_SWE.GENeration, str, {"ANALog": True, "STEPped": False})
        dwell_time = SCPIProperty(_SWE.DWELl, float)
        dwell_on_each_partial_measurement = SCPIPropertyMapping(_SWE.DWELl.IPOint, str, {"ALL": True, "FIRSt": False})
        points = SCPIPropertyMinMax(_SWE.POINts, int)
        count = SCPIProperty(_SWE.COUNt, int)
        time = SCPIPropertyMinMax(_SWE.TIME, float)
        use_auto_time = SCPIProperty(_SWE.TIME.AUTO, bool)
        step_size = SCPIPropertyMinMax(_SWE.STEP, float)

    class Trace(object):
        """
        A class representing a trace on the VNA. Instances are obtained via Channel.create_trace() and Channel.get_trace()
        """
        def __init__(self, name, channel):
            """
            :param name: The trace name
            :param channel: The channel the trace belongs to
            :type channel: ZNB.Channel
            """
            self._n = None
            self._name = str(name)
            self.channel = channel
            self._cmd_cnt = None

        def _calc_node(self):
            return self.channel.CALC

        def _corr_node(self):
            return self.channel.CORRection

        def _sweep_node(self):
            return self.channel.SENSe.SWEep

        def _disp_node(self):
            return self.channel.instrument.DISPlay

        # noinspection PyUnusedLocal
        def _make_active_cb(self, *args, **kwargs):
            if self._cmd_cnt != self.channel.instrument.command_cnt:
                self.select_trace()
            self._cmd_cnt = self.channel.instrument.command_cnt + 1

        def copy_data_to_mem(self, target_trace_name):
            self.channel.instrument.TRACe.COPY().w(target_trace_name, self.name)
            return self.__class__(target_trace_name, self.channel)

        def copy_math_to_mem(self, target_trace_name):
            self.channel.instrument.TRACe.COPY.MATH().w(target_trace_name, self.name)
            return self.__class__(target_trace_name, self.channel)

        def delete(self):
            """
            Deletes the trace. CALCulate<Ch>:​PARameter:​DELete
            """
            self.channel.CALC.PARameter.DELete().w(self.name)

        @property
        def name(self):
            """
            The trace name, must be unique in the recall set.

            :rtype: str
            """
            return self._name

        @name.setter
        def name(self, name):
            name = str(name)
            self.channel.instrument.CONFigure.TRACe.REName().w(self.name, name)
            self._name = name

        @property
        def n(self):
            """
            :return: CONFigure.TRACe.NAME.ID?
            """
            if not self._n:  # FIXME: check if the trace id changes when deleting a trace
                self._n = int(self.channel.instrument.CONFigure.TRACe.NAME.ID().q(self.name))
            return self._n

        # TODO: argument checking?
        trace_format = SCPIProperty(ZNB_gen.CALCulate.FORMat, str, callback=_make_active_cb, get_root_node=_calc_node)

        # noinspection PyUnusedLocal
        def _add_trace_name_arg_cb(self, value=None, **kwargs):
            ret = {"name": self.name, "fmt": "{name:q}"}
            if value is not None:
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

        cal_state_label = SCPIProperty(ZNB_gen.SENSe.CORRection.SSTate, str, callback=_make_active_cb, get_root_node=_corr_node)  # FIXME: read-only -> method
        source_port = SCPIProperty(ZNB_gen.SENSe.SWEep.SRCPort, int, callback=_make_active_cb, get_root_node=_sweep_node)  # Logical port number of the simulus port

        math_equation = SCPIProperty(ZNB_gen.CALCulate.MATH.EXPRession.SDEFine, str, callback=_make_active_cb, get_root_node=_calc_node)
        math_is_enabled = SCPIProperty(ZNB_gen.CALCulate.MATH.STATe, bool, callback=_make_active_cb, get_root_node=_calc_node)
        math_is_wave_quantity = SCPIProperty(ZNB_gen.CALCulate.MATH.WUNit.STATe, bool, callback=_make_active_cb, get_root_node=_calc_node)

        def is_active(self):
            return self.channel.active_trace.name == self.name

        def select_trace(self):
            """
            Makes the trace the active trace in the channel.
            """
            self.channel.CALC.PARameter.SELect().w(self.name)

        def get_marker(self, n):
            """

            :param n: Marker number
            :rtype: ZNB.Marker
            """
            return self.channel.instrument.Marker(n, self)

        def assign_diagram(self, diagram):
            """
            Assigns the trace to a diagram.

            :param diagram: An existing Diagram area
            :type diagram: Diagram
            """
            diagram.TRACe.EFEed().w(self.name)

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
            super(ZNB.Marker, self).__init__(parent=trace.channel.CALC)
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
        y = SCPIProperty(_MKR.Y, float, callback=_prop_callback)  # FIXME: query only -> query_y() method

    class Limit(ZNB_gen.CALCulate.LIMit):
        def __init__(self, trace):
            """
            :param Trace trace: The trace which the limit applies to
            """
            super(ZNB.Limit, self).__init__(parent=trace.channel.CALC)
            self.trace = trace

    class Diagram(ZNB_gen.DISPlay.WINDow):
        def __init__(self, n, instrument):
            """
            :param n: Number of the diagram area
            :param instrument: Reference to the Instrument
            :type instrument: ZNB
            """
            super(ZNB.Diagram, self).__init__(parent=instrument.DISPlay)
            self.instrument = instrument
            self.n = n

        def delete(self):
            # FIXME: make some kind of callback to update all remaining Diagram instances?? requires a weakref dict.
            """
            Remove the diagram area. Note that this will re-number all remaining diagrams, so use with care.
            Renumbering causes the diagram name to be reset to the diagram number, this is arguably a FW bug.
            Also deletes all traces assigned to the diagram.
            :return:
            """
            self.STATe().w("OFF")

        def select_diagram(self):
            """
            Make the diagram the active diagram.

            :return: None
            """
            self.is_maximized = self.is_maximized

        _WIN = ZNB_gen.DISPlay.WINDow

        is_maximized = SCPIProperty(_WIN.MAXimize, bool)
        """
        Displays the diagram on top of the other diagrams, filling the whole screen.
        """

        name = SCPIProperty(_WIN.NAME, str)
        """
        The diagram name, shown in upper right corner. Returned with DISPlay:CATalog?
        """

        title = SCPIProperty(_WIN.TITLe.DATA, str)
        """
        The diagram title, shown on screen.
        """

        title_is_visible = SCPIProperty(_WIN.TITLe.STATe, bool)
        """
        Determines whether the diagram title is shown or not.
        """

        def save_screenshot(self, filename):
            """
            Take a screenshot containing only this diagram.

            :param filename: The filname under which the screenshot will be saved on the instrument.
            :return: a File object representing the captured screenshot
            :rtype: File
            """
            return self.instrument.save_screenshot(filename=filename, diagram=self)

        def query_assigned_traces(self):
            """
            Get the traces assigned to the diagram

            :return: A generator returning Traces
            """
            l = self.TRACe.CATalog().q()
            for wnr, name in l.comma_list_pairs():
                ch = self.instrument.CONFigure.TRACe.CHANnel.NAME.ID.q(name)
                yield self.instrument.Trace(name=name, channel=self.instrument.Channel(int(ch), self.instrument))

    class Filesystem(ZNB_gen.MMEMory):
        def __init__(self, instrument):
            super(ZNB.Filesystem, self).__init__(parent=instrument)
            self.instrument = instrument

        def getcwd(self):
            """
            :return: a string representing the current working directory on the instrument.
            :rtype: str
            """
            return str(self.CDIRectory().q())

        def chdir(self, path):
            """
            Change the current working directory on the instrument to path.
            """
            self.CDIRectory.w(path)

        def file(self, filename, path=None):
            """
            Create a File instance

            :param filename:
            :param path: Set to getcwd() if None
            :return: File(filename, path)
            :rtype: File
            """
            if path is None:
                path = self.getcwd()
            return self.instrument.File(filename=filename, path=path, instrument=self._parent)

        def listdir(self, path=None):
            if path is None:
                path = self.getcwd()
            return self.instrument.Directory(path=path, instrument=self._parent).listdir()

    class Path(object):
        def __init__(self, path, filename):
            if filename and ntpath.isabs(filename):
                self.path, self.filename = ntpath.split(filename)
            else:
                self.filename = filename
                self.path = path

        def __str__(self):
            return ntpath.join(self.path, self.filename)

    class Directory(Path):
        def __init__(self, path, instrument):
            super(ZNB.Directory, self).__init__(path=path, filename=None)
            self.instrument = instrument

        def __str__(self):
            return self.path

        def file(self, filename):
            return self.instrument.File(filename=filename, instrument=self.instrument, path=self.path)

        def listdir(self):
            def mk_list(match):
                if match.group(2) == "<DIR>":
                    return self.__class__(path=match.group(1), instrument=self.instrument)
                else:
                    return self.instrument.File(filename=match.group(1), path=self.path, instrument=self.instrument)

            import re
            x = self.instrument.MMEMory.CATalog.q(self.path)
            used_size, free_disk, files = str(x).split(", ", 2)
            # We can't split files on comma alone, since a comma might be contained in a filename
            r = re.finditer('(.*?), (?:(<DIR>), |, (\d+)),', files)
            return list(map(mk_list, r))

        @staticmethod
        def isdir():
            return True

        @staticmethod
        def isfile():
            return False

    class File(Path):
        """
        An object representing a file on the instrument.
        """
        def __init__(self, instrument, filename, path=None):
            """

            :param instrument:
            :type instrument: ZNB
            :param filename:
            :param path:
            """
            ZNB.Path.__init__(self, filename=filename, path=path)
            self.instrument = instrument
            if self.path is None:
                self.path = instrument.filesystem.getcwd()

        @staticmethod
        def isdir():
            return False

        @staticmethod
        def isfile():
            return True

        @property
        def full_path(self):
            return ntpath.join(self.path, self.filename)

        def read(self):
            return self.instrument.MMEMory.DATA().q(self.full_path).block_data()

        def write(self, data):
            # FIXME: rename to reflect that the method overwrites the existing file
            self.instrument.MMEMory.DATA().w(self.full_path, SCPIBlockData(data))

        def get(self, local_target):
            """
            Retrieve a file from the VNA.

            :param local_target: The target file on the controller. If local_target is a directory the file will be stored with the same name as on the instrument.
            """
            if os.path.isdir(local_target):
                local_target = os.path.join(local_target, self.filename)
            with open(local_target, "wb") as fd:
                fd.write(self.read())

        def put(self, local_file):
            """
            Copy a file from the controller to the instrument.

            :param local_file:
            :return:
            """
            with open(local_file, "rb") as fd:
                self.write(fd.read())

        def copy(self, target):
            """
            Copy the file to a new location on the instrument

            :param target: The location of the copy
            """
            self.instrument.MMEMory.COPY().w(self.full_path, str(target))
