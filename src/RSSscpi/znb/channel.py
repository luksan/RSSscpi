from typing import List, Union

from .. import znb
from ..scpi.class_property import SCPIProperty, SCPIPropertyMinMax, SCPIPropertyMapping
from ..gen import ZNB_gen

from .trace import MeasParamBase, Trace


class Channel:
    def __init__(self, n: int, instrument: "znb.ZNB"):
        """
        :param n: Channel number
        :param instrument: A SCPINode instance, linked to the instrument
        """
        self.n = n
        self._instr = instrument  # type: znb.ZNB

    @property
    def instrument(self) -> "znb.ZNB":
        return self._instr

    @property
    def CALC(self) -> ZNB_gen.CALCulate:
        return self.instrument.CALCulate[self.n]

    @property
    def CONFch(self) -> ZNB_gen.CONFigure.CHANnel:
        return self.instrument.CONFigure.CHANnel[self.n]

    @property
    def SENSe(self) -> ZNB_gen.SENSe:
        return self.instrument.SENSe[self.n]

    @property
    def SOURce(self) -> ZNB_gen.SOURce:
        return self.instrument.SOURce[self.n]

    @property
    def TRIGger(self) -> ZNB_gen.TRIGger:
        return self.instrument.TRIGger[self.n]

    name = SCPIProperty(ZNB_gen.CONFigure.CHANnel.NAME, str, get_root_node=lambda self: self.CONFch)
    """
    The channel name, CONFigure:CHANnel<Ch>:NAME
    """

    def get_trace(self, name: str) -> Trace:
        """
        :param name: The name of the trace
        :return: A Trace object
        """
        return Trace(name=name, channel=self)

    @property
    def sweep(self) -> "Sweep":
        return Sweep(self)

    @property
    def calibration(self):
        # type () -> RSSscpi.znb.ChannelCal
        return ChannelCal(self)

    def get_vna_port(self, port_no):
        return ChannelVNAPort(self, port_no)

    state = SCPIProperty(ZNB_gen.CONFigure.CHANnel.STATe, bool, get_root_node=lambda self: self.CONFch)
    """
    Returns True if the channel is activated. Set to True to create the channel, and to False to delete it.
    """

    def create_trace(self, name, parameter: Union[str, MeasParamBase], diagram=None) -> Trace:
        """
        Create a new trace with a measurement parameter according to CALCulate<Ch>:PARameter:SDEFine

        :param name: The trace name
        :param parameter: A string defining the measured quantity.
        :param Diagram diagram: An optional Diagram, which the trace will be assigned to.
                        The trace will not be visible unless a Diagram is specified.
        :return: A reference to the new trace
        :rtype: Trace
        """
        self.CALC.PARameter.SDEFine.w(name, parameter)
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
        name = str(self.CALC.PARameter.SELect.q())
        # n = self.instrument.CONFigure.TRACe.CHANnel.NAME.ID.q(name)
        return self.get_trace(name)

    @active_trace.setter
    def active_trace(self, trace):
        name = trace.name if hasattr(trace, "name") else str(trace)
        self.CALC.PARameter.SELect.w(name)

    def query_trace_list(self) -> List[Trace]:
        """
        Returns a list of all the traces defined in the channel.
        """
        traces = self.CONFch.TRACe.CATalog.q()
        return [self.get_trace(tr_name) for _tr_no, tr_name in traces.comma_list_pairs()]

    power_level = SCPIProperty(ZNB_gen.SOURce.POWer.LEVel.IMMediate.AMPLitude, float,
                               get_root_node=lambda self: self.SOURce)  # type: float
    """
    The channel power level, in dBm.
    """

    _FRQ = ZNB_gen.SENSe.FREQuency
    freq_cw = SCPIProperty(_FRQ.CW, float, get_root_node=lambda x: x.SENSe)
    freq_cw_minmax = SCPIPropertyMinMax(freq_cw)
    freq_start = SCPIProperty(_FRQ.STARt, float, get_root_node=lambda x: x.SENSe)
    freq_start_minmax = SCPIPropertyMinMax(freq_start)
    freq_stop = SCPIProperty(_FRQ.STOP, float, get_root_node=lambda x: x.SENSe)
    freq_stop_minmax = SCPIPropertyMinMax(freq_stop)
    freq_center = SCPIProperty(_FRQ.CENTer, float, get_root_node=lambda x: x.SENSe)
    freq_center_minmax = SCPIPropertyMinMax(freq_center)
    freq_span = SCPIProperty(_FRQ.SPAN, float, get_root_node=lambda x: x.SENSe)
    freq_span_minmax = SCPIPropertyMinMax(freq_span)

    ifbw = SCPIProperty(ZNB_gen.SENSe.BANDwidth, int, get_root_node=lambda x: x.SENSe)
    ifbw_minmax = SCPIPropertyMinMax(ifbw)
    if_selectivity = SCPIProperty(ZNB_gen.SENSe.BANDwidth.RESolution.SELect, str, get_root_node=lambda x: x.SENSe)

    def cal_auto(self, vna_ports, cal_unit_ports=None, cal_type="FNPort", cal_unit_characterization=""):
        if cal_unit_ports:
            cmd_fmt = "{:s}, {:q}, {:d**}"
            self.SENSe.CORRection.COLLect.AUTO.PORTs.TYPE.w(
                cal_type, cal_unit_characterization, zip(vna_ports, cal_unit_ports), fmt=cmd_fmt)
        else:
            cmd_fmt = "{:s}, {:q}, {:d*}"
            self.SENSe.CORRection.COLLect.AUTO.TYPE.w(cal_type, cal_unit_characterization, vna_ports, fmt=cmd_fmt)

    def configure_freq_sweep(self, start_freq, stop_freq, *, points=None, ifbw=None, power=None, log_sweep=False):
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
            self.sweep.type = Sweep.LIN
        else:
            self.sweep.type = Sweep.LOG

        self.freq_start = start_freq
        self.freq_stop = stop_freq
        if points is not None:
            self.sweep.points = points
        if ifbw is not None:
            self.ifbw = ifbw
        if power is not None:
            self.power_level = power

    def configure_power_sweep(self, freq, start_power, stop_power, *, points=None, ifbw=None):
        """
        Configure the channel for a power sweep. Unspecified parameters are not modified.

        :param float freq: The CW frequency for the channel
        :param float start_power: Start power level in dBm
        :param float stop_power: Stop power level in dBm
        :param int points: Number of sweep points
        :param ifbw: IF bandwidth
        """
        self.sweep.type = Sweep.POWER
        self.freq_cw = freq
        self.SOURce.POWer[1].STARt.w(start_power)  # The port number suffix on POWer is ignored by the instrument
        self.SOURce.POWer[1].STOP.w(stop_power)
        if points:
            self.sweep.points = points
        if ifbw:
            self.ifbw = ifbw

    def init_sweep(self):  # FIXME: rename to start_sweep() or similar??
        """
        INITiate:IMMediate

        This is valid in single sweep mode only.
        """
        self.instrument.INITiate[self.n].IMMediate.w()

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
        self.instrument.MMEMory.STORe.TRACe.PORTs.w(self.n, filename, fmt, mode_impedance, ports, fmt=cmd_fmt)
        return self.instrument.filesystem.file(filename)


class ChannelVNAPort(ZNB_gen.SOURce.POWer):
    def __init__(self, channel, port_no):
        super(ChannelVNAPort, self).__init__(parent=channel.SOURce)
        self.channel = channel
        self.n = port_no

    _POW = ZNB_gen.SOURce.POWer

    cal_power_offset = SCPIProperty(_POW.CORRection.LEVel.OFFSet, float)
    """This offset only changes the displayed port power, the source level is not affected"""

    power_enabled = SCPIProperty(_POW.STATe, bool)
    """Turn the source power on or off"""

    power_gen = SCPIProperty(_POW.PERManent.STATe, bool)
    """If power_gen is set to True the port power is on for all partial measurements."""

    power_slope = SCPIProperty(_POW.LEVel.IMMediate.SLOPe, float)
    """Set a slope for the port power in dB/GHz"""

    def get_source_power_offset(self):
        """
        The method returs a 2-tuple. The first element is the power offset in dB, the second element is True
        if the offset is relative to the channel base power. If false the first element is the port power in dBm.
        """
        (power, rel) = self.LEVel.IMMediate.OFFSet.q().split_comma()
        return float(power), rel == "CPAD"

    def set_source_power_offset(self, power, relative=True):
        """
        Set the port power effset. If relative is true `power` is an offset to the channel base power. If `relative`
        is False then power is the port power in dBm.

        :param power: Port power offset in dB, or port power in dBm.
        :param bool relative: Determines whether `power` is relative to the channel base power, or an absolute power.
        """
        if relative:
            x = 'CPAD'
        else:
            x = 'ONLY'
        self.LEVel.IMMediate.OFFSet.w(power, x)


class ChannelCal:
    def __init__(self, channel):
        """

        :param RSSscpi.znb.Channel channel:
        """
        self.channel = channel

    def query_calpool_list(self):
        return self.channel.instrument.cal_manager.query_calpool_list()

    def query_calgroup(self):
        x = str(self.channel.instrument.MMEMory.LOAD.CORRection.q(self.channel.n))
        if not x:
            return None
        return x

    def resolve_calgroup_link(self):
        """
        Break the link between the channel calibration and the calpool file.
        """
        self.channel.instrument.MMEMory.LOAD.CORRection.RESolve.w(self.channel.n)

    def load_calibration(self, filename):
        """

        :param str filename:
        :return:
        """
        if filename[-4:] != ".cal":
            filename += ".cal"
        self.channel.instrument.MMEMory.LOAD.CORRection.w(self.channel.n, filename, fmt="{:d}, {:q}")

    def store_calibration(self, filename):
        """
        Store the channel calibration data to disk at ..\\Calibration\\Data

        :param str filename: The target filename
        """
        if filename[-4:] != ".cal":
            filename += ".cal"
        self.channel.instrument.MMEMory.STORe.CORRection.w(self.channel.n, filename, fmt="{:d}, {:q}")


class SweepSegment(ZNB_gen.SENSe.SEGMent):
    def __init__(self, n, channel):
        """
        :param n: The sweep segment number
        :param Channel channel:
        """
        super(SweepSegment, self).__init__(parent=channel.SENSe)
        self.channel = channel
        self.n = n

    def delete(self):
        self.DELete.w()

    _SEG = ZNB_gen.SENSe.SEGMent
    dwell_time = SCPIProperty(_SEG.SWEep.DWELl, float)
    is_enabled = SCPIProperty(_SEG.STATe, bool)
    freq_start = SCPIProperty(_SEG.FREQuency.STARt, float)
    freq_stop = SCPIProperty(_SEG.FREQuency.STOP, float)
    if_bandwidth = SCPIProperty(_SEG.BWIDth.RESolution, int)
    # if_gain = SCPIProperty(_SEG.POWer.GAINcontrol, str)  # TODO: this behaves differently from the other per segment settings...
    if_selectivity = SCPIProperty(_SEG.BWIDth.RESolution.SELect, str)
    number_of_points = SCPIProperty(_SEG.SWEep.POINts, int)
    power_level = SCPIProperty(_SEG.POWer, float)
    sweep_time = SCPIProperty(_SEG.SWEep.TIME, float)  # type: float
    analog_sweep_is_enabled = SCPIPropertyMapping(_SEG.SWEep.GENeration, str, {"ANALog": True, "STEPped": False})


class SweepSegments:
    def __init__(self, sweep):
        """
        :param Sweep sweep: The Sweep which the sweep segments belong to
        """
        self._sweep = sweep
        self._SEG = sweep.channel.SENSe.SEGMent

    def __len__(self):
        return int(self._SEG.COUNt.q())

    def __getitem__(self, item):
        if isinstance(item, slice):
            return [self.get_segment(x + 1) for x in range(*item.indices(len(self)))]
        return self.get_segment(item + 1)

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

    def get_segment(self, n):
        # type: (int) -> SweepSegment
        return self._sweep.get_segment(n)

    def insert_segment(self, start_freq, stop_freq, *, points, ifbw, power, time="AUTO",
                       lo_sideband="AUTO", if_selectivity="NORMal", analog_sweep=False, position=1):
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
        :param int position: The position in the segment list which the created segment will be inserted at. Default is 1 (top).
        :return: The newly created segment
        :rtype: SweepSegment
        """
        if analog_sweep:
            sweep_mode = "ANALog"
        else:
            sweep_mode = "STEPped"
        self._SEG[position].INSert.w(start_freq, stop_freq, points, power, time, "0", ifbw, lo_sideband, if_selectivity,
                                     sweep_mode)
        return self.get_segment(position)

    def delete_segment(self, n):
        """
        Delete segment number `n` from the segment list.

        :param int n: Segment index
        """
        self.get_segment(n).delete()

    def delete_all_segments(self):
        self._SEG.DELete.ALL.w()

    def disable_per_segment_dwell_time(self):
        self._SEG.SWEep.DWELl.CONTrol.w(False)

    def disable_per_segment_ifbw(self):
        self._SEG.BWIDth.RESolution.CONTrol.w(False)

    def disable_per_segment_if_selectivity(self):
        self._SEG.BWIDth.RESolution.SELect.CONTrol.w(False)

    def disable_per_segment_power(self):
        self._SEG.POWer.LEVel.CONTrol.w(False)

    def disable_per_segment_sweep_time(self):
        self._SEG.SWEep.TIME.CONTrol.w(False)

    def query_total_sweep_time(self):
        return float(self._SEG.SWEep.TIME.SUM.q())


class Sweep(ZNB_gen.SENSe.SWEep):
    # Using an Enum for the variuos sweep types only causes complications, with no clear benefit
    LIN = "LIN"
    LOG = "LOG"
    POWER = "POW"
    CW = "CW"
    POINT = "POIN"
    SEGMENT = "SEGM"

    def __init__(self, channel):
        """

        :param Channel channel:
        """
        super(Sweep, self).__init__(parent=channel.SENSe)
        self.channel = channel
        self.segments = SweepSegments(self)

    def get_segment(self, n):
        # type: (int) -> SweepSegment
        return SweepSegment(n, self.channel)

    continuous_sweep = SCPIProperty(ZNB_gen.INITiate.CONTinuous,
                                    bool,
                                    get_root_node=lambda sweep: sweep.channel.instrument.scpi)
    _SWE = ZNB_gen.SENSe.SWEep

    analog_sweep_is_enabled = SCPIPropertyMapping(_SWE.GENeration, str, {"ANALog": True, "STEPped": False})
    count = SCPIProperty(_SWE.COUNt, int)
    dwell_time = SCPIProperty(_SWE.DWELl, float)
    dwell_on_each_partial_measurement = SCPIPropertyMapping(_SWE.DWELl.IPOint, str, {"ALL": True, "FIRSt": False})
    points = SCPIProperty(_SWE.POINts, int)
    points_minmax = SCPIPropertyMinMax(points)
    time = SCPIProperty(_SWE.TIME, float)
    time_minmax = SCPIPropertyMinMax(time)
    type = SCPIProperty(_SWE.TYPE, str)
    use_auto_time = SCPIProperty(_SWE.TIME.AUTO, bool)
    step_size = SCPIProperty(_SWE.STEP, float)
    step_size_minmax = SCPIPropertyMinMax(step_size)
