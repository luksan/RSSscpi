# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from RSSscpi.gen import ZVA_gen
from RSSscpi.SCPI_property import SCPIProperty
from RSSscpi import znb
import RSSscpi.network as net

import logging


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
        self.filesystem = Filesystem(self)
        self.logger = logging.getLogger(__name__)
        self.visa_logger = self.logger.getChild("VISA")

    #def init(self):
        # SYSTem:DATA:SIZE ALL | AUTO

    def _set_codec(self):
        # There is no functionality for this on the ZVA
        assert not hasattr(self.SYSTem.COMMunicate, "CODec")

    def get_channel(self, n):
        # type: (int) -> Channel
        return Channel(n, self)

    def get_diagram(self, n):
        # type: (int) -> Diagram
        return Diagram(n, self)


class Channel(znb.Channel):

    def get_sweep(self):
        # type: () -> Sweep
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


class Trace(znb.Trace):
    def get_marker(self, n):
        return Marker(n, self)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print([str(x) for x in find_zva(max_devices=10, max_time=1)])
