# -*- coding: utf-8 -*-
"""
Created on 16 feb. 2016

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import RSSscpi
from RSSscpi.gen import ZNB_gen
from RSSscpi.SCPI_property import SCPIProperty, SCPIPropertyMinMax, SCPIPropertyMapping
from RSSscpi.SCPI_response import format_SCPI_block_data
import RSSscpi.network as net

import ntpath
import os.path

import logging
import re

from memoized_property import memoized_property


def connect_ethernet(ip_address):
    # type: ([str, unicode]) -> ZNB
    """
    Helper to connect to a ZNB VNA via Ethernet / TCPIP / VISA.
    Creates an ZNB instance and calls init() on it before returning.

    :param ip_address: The ip address in string format
    :return: An initialized ZNB instance.
    :rtype: ZNB
    """
    return net.connect_ethernet(ZNB, ip_address, "hislip0")


class ZNBZeroconf(net.ZeroconfInfo):
    def __init__(self, zeroconf_info):
        self.fw = ""
        self.serial = ""
        super(ZNBZeroconf, self).__init__(zeroconf_info)

    def parse_zc_info(self, i):
        self.name = i.properties['fqdn'].split(".")[0]
        self.fw = i.properties['FirmwareVersion']
        self.serial = i.properties['SerialNumber']

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.fw, self.ip_address)


class ZCListener(net.ZeroconfListener):
    info_class = ZNBZeroconf
    service_name = "_vxi-11._tcp.local."

    def filter_zc_info(self, zc_info):
        return "ZNB" in zc_info.name


def find_znb(max_time=2, max_devices=None):
    """
    Use zeroconf to scan the local network for ZNB VNAs

    :param float max_time: The maximum time we will wait, in seconds
    :param int max_devices: Stop the search after this many devices have been found
    :return: A list of ZNBZeroconf objects describing the found devices.
    :rtype: list[ZNBZeroconf]
    """

    return net.zeroconf_scan(ZCListener(), max_time, max_devices)


class ZNB(ZNB_gen):
    def __init__(self, visa_res):
        super(ZNB, self).__init__(visa_res)
        self.logger = logging.getLogger(__name__)
        self.visa_logger = self.logger.getChild("VISA")
        self._port_count = None

    @memoized_property
    def filesystem(self):
        """
        A Filsystem instance which enables filesystem operations on the instrument.

        :rtype: RSSscpi.znb.Filesystem
        """
        return Filesystem(self)

    def init(self):
        super(ZNB, self).init()

        self._set_codec()
        self.reset_remote_emulation()

    def _set_codec(self):
        self.SYSTem.COMMunicate.CODec().w("UTF8")  # Set the character encoding

    def reset_remote_emulation(self):
        # type: () -> str
        """
        Restores the SYSTem:LANGuage setting to SCPI, disabling emulation of other VNA types.

        :return: The original SYSTem:LANGuage setting
        """
        orig_lang = str(self.SYSTem.LANGuage().q())
        if orig_lang != "SCPI":
            self.visa_logger.warning("Changing remote language from '%s' to 'SCPI' (default)", orig_lang)
            self.SYSTem.LANGuage().w("SCPI")
        return orig_lang

    @property
    def active_channel(self):
        """
        Get/set the active channel, INSTrument:NSELect?
        """
        return self.get_channel(int(self.INSTrument.NSELect().q()))

    @active_channel.setter
    def active_channel(self, n):
        if hasattr(n, "n"):
            n = n.n
        self.INSTrument.NSELect().w(n)

    def get_channel(self, n):
        # type: (int) -> Channel
        """
        :param n: The number of the channel
        :return: A Channel object
        """
        return Channel(n, self)

    def query_channel_list(self):
        """
        Returns a list of tuples representing all the channels in the active recall set.
        CONFigure:CHANnel:CATalog?

        The first element of each tuple is a :class:`Channel` instance,
        the second element is the name of the channel as a string.
        """
        x = self.CONFigure.CHANnel.CATalog.q().comma_list_pairs()
        return [(self.get_channel(int(n)), str(name)) for n, name in x]

    def get_diagram(self, n):
        """
        Returns a :class:`RSSscpi.znb.Diagram` instance, linked to the instrument.

        :param int n: The diagram id, Wnd
        :rtype: RSSscpi.znb.Diagram
        """
        return Diagram(n, self)

    def query_number_of_ports(self):
        # type: () -> int
        """
        Query the instrument about how many physical ports there are on the instrument.
        This can be different from the number of test ports, i.e if a switch matrix is connected
        to the instrument.

        :return: The number of physical ports on the instrument
        """
        if self._port_count:
            return self._port_count
        x = int(self.INSTrument.PORT.COUNt().q())
        self._port_count = x
        return x

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

    @property
    def CALC(self):
        # type: () -> ZNB_gen.CALCulate
        return self.instrument.CALCulate(self.n)

    @property
    def CONFch(self):
        # type: () -> ZNB_gen.CONFigure.CHANnel
        return self.instrument.CONFigure.CHANnel(self.n)

    @property
    def SENSe(self):
        # type: () -> ZNB_gen.SENSe
        return self.instrument.SENSe(self.n)

    @property
    def SOURce(self):
        # type: () -> ZNB_gen.SOURce
        return self.instrument.SOURce(self.n)

    @property
    def TRIGger(self):
        # type: () -> ZNB_gen.TRIGger
        return self.instrument.TRIGger(self.n)

    name = SCPIProperty(ZNB_gen.CONFigure.CHANnel.NAME, str, get_root_node=lambda self: self.CONFch)
    """
    The channel name, CONFigure:CHANnel<Ch>:NAME
    """

    def get_trace(self, name):
        # type: ([unicode, str]) -> Trace
        """
        :param name: The name of the trace
        :return: A Trace object
        """
        return Trace(name=name, channel=self)

    @property
    def sweep(self):
        # type: () -> RSSscpi.znb.Sweep
        return Sweep(self)

    def get_vna_port(self, port_no):
        return ChannelVNAPort(self, port_no)

    state = SCPIProperty(ZNB_gen.CONFigure.CHANnel.STATe, bool, get_root_node=lambda self: self.CONFch)
    """
    Returns True if the channel is activated. Set to True to create the channel, and to False to delete it.
    """

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
        name = trace.name if hasattr(trace, "name") else str(trace)
        self.CALC.PARameter.SELect().w(name)

    power_level = SCPIProperty(ZNB_gen.SOURce.POWer.LEVel.IMMediate.AMPLitude, float, get_root_node=lambda self: self.SOURce)  # type: float
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
            self.SENSe.CORRection.COLLect.AUTO.PORTs.TYPE().w(
                cal_type, cal_unit_characterization, zip(vna_ports, cal_unit_ports), fmt=cmd_fmt)
        else:
            cmd_fmt = "{:s}, {:q}, {:d*}"
            self.SENSe.CORRection.COLLect.AUTO.TYPE().w(cal_type, cal_unit_characterization, vna_ports, fmt=cmd_fmt)

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

    def configure_power_sweep(self, freq, start_power, stop_power, points=None, ifbw=None):
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
        self.SOURce.POWer(1).STARt().w(start_power)  # The port number suffix on POWer is ignored by the instrument
        self.SOURce.POWer(1).STOP().w(stop_power)
        if points:
            self.sweep.points = points
        if ifbw:
            self.ifbw = ifbw

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
        (power, rel) = self.LEVel.IMMediate.OFFSet().q().split_comma()
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
        self.LEVel.IMMediate.OFFSet().w(power, x)


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
        self.DELete().w()

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


class SweepSegments(object):
    def __init__(self, sweep):
        """
        :param Sweep sweep: The Sweep which the sweep segments belong to
        """
        self._sweep = sweep
        self._SEG = sweep.channel.SENSe.SEGMent

    def __len__(self):
        return int(self._SEG.COUNt().q())

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

    def insert_segment(self, start_freq, stop_freq, points, ifbw, power, time="AUTO",
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
        self._SEG(position).INSert().w(start_freq, stop_freq, points, power, time, "0", ifbw, lo_sideband, if_selectivity, sweep_mode)
        return self.get_segment(position)

    def delete_segment(self, n):
        """
        Delete segment number `n` from the segment list.

        :param int n: Segment index
        """
        self.get_segment(n).delete()

    def delete_all_segments(self):
        self._SEG.DELete.ALL().w()

    def disable_per_segment_dwell_time(self):
        self._SEG.SWEep.DWELl.CONTrol().w(False)

    def disable_per_segment_ifbw(self):
        self._SEG.BWIDth.RESolution.CONTrol.w(False)

    def disable_per_segment_if_selectivity(self):
        self._SEG.BWIDth.RESolution.SELect.CONTrol().w(False)

    def disable_per_segment_power(self):
        self._SEG.POWer.LEVel.CONTrol().w(False)

    def disable_per_segment_sweep_time(self):
        self._SEG.SWEep.TIME.CONTrol().w(False)

    def query_total_sweep_time(self):
        return float(self._SEG.SWEep.TIME.SUM().q())


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


class MeasParamBase(object):
    def __init__(self, dst_port, src_port, detector=""):
        self.dst_port = int(dst_port)
        self.src_port = int(src_port)
        self.detector = str(detector).upper()


class Trace(object):
    """
    A class representing a trace on the VNA. Instances are obtained via Channel.create_trace() and Channel.get_trace()
    """

    class MeasParam(object):
        class S(MeasParamBase):
            def __str__(self):
                return "S{:02d}{:02d}{!s}".format(self.dst_port, self.src_port, self.detector)

        class Wave(MeasParamBase):
            def __init__(self, receiver, dst_port, src_port, detector=""):
                super(Trace.MeasParam.Wave, self).__init__(dst_port, src_port, detector)
                self.receiver = str(receiver).upper()

            def __str__(self):
                return "{!s}{:02d}D{:02d}{!s}".format(self.receiver, self.dst_port, self.src_port, self.detector)

    def __init__(self, name, channel):
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
        self.channel.instrument.DISPlay.WINDow.TRACe.Y.SCALe.AUTO().w("ONCE", self.name, fmt="{:s}, {:q}")

    def copy_data_to_mem(self, target_trace_name):
        self.check_if_name_is_valid(target_trace_name, raise_err=True)
        self.channel.instrument.TRACe.COPY().w(target_trace_name, self.name)
        return self.__class__(target_trace_name, self.channel)

    def copy_math_to_mem(self, target_trace_name):
        self.check_if_name_is_valid(target_trace_name, raise_err=True)
        self.channel.instrument.TRACe.COPY.MATH().w(target_trace_name, self.name)
        return self.__class__(target_trace_name, self.channel)

    def copy(self, new_name, diagram=None):
        # type: ([str, unicode], Diagram) -> Trace
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
        self.channel.CALC.PARameter.DELete().w(self.name)

    @property
    def measurement(self):
        """
        A string describing the measurement associated with the trace.
        See CALCulate<Ch>:PARameter:SDEFine for all possible options.

        Use the Trace.MeasParam... helpers for easier use.

        Example: tr1.measurement = tr1.MeasParam.Wave("b", 1, src_port=1, detector="sam")
        """
        return str(self.channel.CALC.PARameter.MEASure().q(self.name))

    @measurement.setter
    def measurement(self, param):
        self.channel.CALC.PARameter.MEASure().w(self.name, str(param))

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
        self.check_if_name_is_valid(name, raise_err=True)
        self.channel.instrument.CONFigure.TRACe.REName().w(self.name, name)
        self._name = name

    @staticmethod
    def check_if_name_is_valid(name, raise_err=False):
        # type: (str) -> bool
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
            self._n = int(self.channel.instrument.CONFigure.TRACe.NAME.ID().q(self.name))
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


class Diagram(ZNB_gen.DISPlay.WINDow):
    def __init__(self, n, instrument):
        """
        :param n: Number of the diagram area
        :param instrument: Reference to the Instrument
        :type instrument: ZNB
        """
        super(Diagram, self).__init__(parent=instrument.DISPlay)
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

    state = SCPIProperty(_WIN.STATe, bool)
    """
    Enable/disable the diagram.
    Note that disabling the diagram will renumber all the remaining diagrams on the instrument,
    and delete all traces that are assigned to the diagram.
    """

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
            ch_no = self.instrument.CONFigure.TRACe.CHANnel.NAME.ID.q(name)
            ch = self.instrument.get_channel(ch_no)
            yield ch.get_trace(name=name)


class Filesystem(ZNB_gen.MMEMory):
    def __init__(self, instrument):
        super(Filesystem, self).__init__(parent=instrument)
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

    @memoized_property
    def default_dir(self):
        cdir = self.getcwd()
        self.CDIRectory.w("DEFault")
        def_dir = self.getcwd()
        self.chdir(cdir)
        return def_dir

    @memoized_property
    def calpool_dir(self):
        return ntpath.join(self.default_dir, 'Calibration', 'Data')

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
        return File(filename=filename, path=path, instrument=self.instrument)

    def listdir(self, path=None):
        if path is None:
            path = self.getcwd()
        return Directory(path=path, instrument=self.instrument).listdir()


class Path(object):
    def __init__(self, path, filename):
        if filename and ntpath.isabs(filename):
            self.path, self.filename = ntpath.split(filename)
        else:
            self.filename = filename
            self.path = path

    def __str__(self):
        return ntpath.join(self.path, self.filename)

    def __repr__(self):
        return str(self)


class Directory(Path):
    def __init__(self, path, instrument):
        super(Directory, self).__init__(path=path, filename=None)
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
                return self.instrument.filesystem.file(filename=match.group(1), path=self.path)

        import re
        x = self.instrument.MMEMory.CATalog.q(self.path)
        # <used_size>,<free_disk_space> {,<file_name>,,<file_size>}
        try:
            used_size, free_disk, files = str(x).split(",", 2)
        except ValueError:
            raise RuntimeError("Bad instrument response from MMEM:CAT? %s -> %s" % (self.path, str(x)))
        # We can't split files on comma alone, since a comma might be contained in a filename
        r = re.finditer(' (.*?),(?:( <DIR>),|, (\d+)),', files)
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
        super(File, self).__init__(filename=filename, path=path)
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
        self.instrument.MMEMory.DATA().w(self.full_path, format_SCPI_block_data(data))

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


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    devices = find_znb(max_devices=10, max_time=1)
    print([str(_dev) for _dev in devices])
    znb = connect_ethernet(devices[0].ip_address)
    print(znb.IDN.q())
