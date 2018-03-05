# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import RSSscpi
from RSSscpi.gen import ZVA_gen
from RSSscpi.SCPI_property import SCPIProperty
from RSSscpi import znb
import RSSscpi.network as net

import logging

from memoized_property import memoized_property


def connect_ethernet(ip_address):
    # type: ([str, unicode]) -> ZVA
    """
    Helper to connect to a ZVA VNA via Ethernet / TCPIP / VISA.
    Creates an ZVA instance and calls init() on it before returning.

    :param ip_address: The ip address in string format
    :return: An initialized ZVA instance.
    :rtype: ZVA
    """
    return net.connect_ethernet(ZVA, ip_address)


class ZVAZeroconf(znb.ZNBZeroconf):
    pass


class ZCListener(net.ZeroconfListener):
    info_class = ZVAZeroconf
    service_name = "_vxi-11._tcp.local."

    def filter_zc_info(self, zc_info):
        return "ZVA" in zc_info.name


def find_zva(max_time=2, max_devices=None):
    """
    Use zeroconf to scan the local network for ZVA VNAs

    :param float max_time: The maximum time we will wait, in seconds
    :param int max_devices: Stop the search after this many devices have been found
    :return: A list of ZVAZeroconf objects describing the found devices.
    :rtype: list[ZVAZeroconf]
    """

    return net.zeroconf_scan(ZCListener(), max_time, max_devices)


class ZVA(ZVA_gen, znb.ZNB):
    def __init__(self, visa_res):
        super(ZVA, self).__init__(visa_res=visa_res)
        self.logger = logging.getLogger(__name__)
        self.visa_logger = self.logger.getChild("VISA")

    #def init(self):
        # SYSTem:DATA:SIZE ALL | AUTO

    @memoized_property
    def filesystem(self):
        """
        A Filsystem instance which enables filesystem operations on the instrument.

        :rtype: RSSscpi.zva.Filesystem
        """
        return Filesystem(self)

    def _set_codec(self):
        # There is no functionality for this on the ZVA
        assert not hasattr(self.SYSTem.COMMunicate, "CODec")

    def get_channel(self, n):
        # type: (int) -> Channel
        return Channel(n, self)

    def get_diagram(self, n):
        """
        Returns a :class:`RSSscpi.zva.Diagram` instance, linked to the instrument.

        :param int n: The diagram id, Wnd
        :rtype: RSSscpi.zva.Diagram
        """
        return Diagram(n, self)


class Channel(znb.Channel):

    @property
    def sweep(self):
        # type: () -> RSSscpi.zva.Sweep
        return Sweep(self)

    def get_trace(self, name):
        # type: ([str, unicode]) -> Trace
        return Trace(name=name, channel=self)

    def get_vna_port(self, port_no):
        return ChannelVNAPort(self, port_no)


class Diagram(ZVA_gen.DISPlay.WINDow, znb.Diagram):
    pass


class Filesystem(ZVA_gen.MMEMory, znb.Filesystem):
    pass


class Limit(ZVA_gen.CALCulate.LIMit, znb.Limit):
    pass


class Marker(ZVA_gen.CALCulate.MARKer, znb.Marker):
    pass


class ChannelVNAPort(ZVA_gen.SOURce.POWer, znb.ChannelVNAPort):
    @property
    def src_attenuator(self):
        """
        Sets/queries the source attenuator value. If the attenuator setting is in auto mode,
        the current value of the attenuator will be returned.

        SOURce:POWer:ATTenuation / SOURce:POWer:ATTenuation:AUTO:VALue?
        """
        return int(self.ATTenuation.AUTO.VALue().q())

    @src_attenuator.setter
    def src_attenuator(self, att):
        # TODO: check that the att parameter is within the range of the instrument
        self.ATTenuation().w(int(att))

    src_attenuator_mode = SCPIProperty(ZVA_gen.SOURce.POWer.ATTenuation.MODE, str)
    """AUTO | MANual | LNOise"""


class Sweep(ZVA_gen.SENSe.SWEep, znb.Sweep):
    def __init__(self, channel):
        super(Sweep, self).__init__(channel=channel)
        self.segments = SweepSegments(self)

    @property
    def dwell_on_each_partial_measurement(self):
        """
        The ZVA does not support setting dwell time on only the first partial measurement.
        """
        return True

    def get_segment(self, n):
        # type: (int) -> SweepSegment
        return SweepSegment(n, self.channel)


class SweepSegment(ZVA_gen.SENSe.SEGMent, znb.SweepSegment):

    @property
    def analog_sweep_is_enabled(self):
        """The ZVA does not support ANALog sweeps"""
        return False


class SweepSegments(znb.SweepSegments):
    def insert_segment(self, start_freq, stop_freq, points, ifbw, power, time="AUTO", lo_sideband="AUTO",
                       if_selectivity="NORMal", analog_sweep=False, position=1):
        """
        :param float start_freq: Segment start frequency in Hz
        :param float stop_freq: Segment stop frequency in Hz
        :param int points: Number of sweep points in the segment
        :param float ifbw: IF bandwidth
        :param float power: Segment source power in dBm
        :param float time: Segment sweep time or segment dwell time in seconds
        :param str lo_sideband: "POSitive" | "NEGative" | "AUTO" (default)
        :param str if_selectivity: "NORMal" (default) | "MEDium" | "HIGH"
        :param bool analog_sweep: For code compatibility with ZNB. Must be set to False.
        :param int position: The position in the segment list which the created segment will be inserted at. Default is 1 (top).
        :return: The newly created segment
        :rtype: SweepSegment
        """
        if analog_sweep:
            raise ValueError("The ZVA does not support analog sweeps.")
        self._SEG(position).INSert().w(start_freq, stop_freq, points, power, time, "0", ifbw, lo_sideband, if_selectivity)
        return self.get_segment(position)


class Trace(znb.Trace):
    def get_marker(self, n):
        return Marker(n, self)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print([str(x) for x in find_zva(max_devices=10, max_time=1)])
