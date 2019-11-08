# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
import socket

from . import network as net
from .gen.SMA100B_gen import SMA100B_gen


def connect_ethernet(ip_address: str) -> "SMA100B":
    """
    Helper to connect to a SMA100B signal generator via Ethernet / TCPIP / VISA.
    Creates an SMA100B instance and calls init() on it before returning.

    :param ip_address: The ip address in string format
    :return: An initialized SMA100B instance.
    :rtype: SMA100B
    """
    return net.connect_ethernet(SMA100B, ip_address)


class SMA100BZeroconf(net.ZeroconfInfo):
    def __init__(self, zeroconf_info):
        self.fw = ""
        super(SMA100BZeroconf, self).__init__(zeroconf_info)

    def parse_zc_info(self, zeroconf_info):
        i = zeroconf_info
        (sma_type, fw, sn) = i.name.split()
        self.name = sma_type + "-" + sn[:6]  # SMA100B-xxxxxx
        self.fw = fw.strip("()")
        self.ip_address = socket.inet_ntoa(i.address)

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.fw, self.ip_address)


class ZCListener(net.ZeroconfListener):
    info_class = SMA100BZeroconf
    service_name = "_hislip._tcp.local."

    def filter_zc_info(self, zc_info):
        return zc_info.name.startswith("SMA100B")


def find_sma100b(max_time=2, max_devices=None):
    """
    Use zeroconf to scan the local network for SMA100B generators.

    :param float max_time: The maximum time we will wait, in seconds
    :param int max_devices: Stop the search after this many devices have been found
    :return: A list of SMA100BZeroconf objects describing the found devices.
    :rtype: list[SMA100BZeroconf]
    """

    return net.zeroconf_scan(ZCListener(), max_time, max_devices)


class SMA100B(SMA100B_gen):
    pass


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    devices = find_sma100b(max_devices=1)
    print("Found %s" % devices[0])
    sma = connect_ethernet(devices[0].ip_address)
    print(sma.IDN.q())
