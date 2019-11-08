# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from . import network as net
from .gen.SMB100A_gen import SMB100A_gen


def connect_ethernet(ip_address: str) -> "SMB100A":
    """
    Helper to connect to a SMB100A signal generator via Ethernet / TCPIP / VISA.
    Creates an SMB100A instance and calls init() on it before returning.

    :param ip_address: The ip address in string format
    :return: An initialized SMB100A instance.
    :rtype: SMB100A
    """
    return net.connect_ethernet(SMB100A, ip_address)


class SMB100AZeroconf(net.ZeroconfInfo):
    """Zeroconf result parser"""


class ZCListener(net.ZeroconfListener):
    info_class = SMB100AZeroconf
    service_name = "_workstation._tcp.local."

    def filter_zc_info(self, zc_info):
        return zc_info.name.startswith("rssmb100a")


def find_smb100a(max_time=2, max_devices=None):
    """
    Use zeroconf to scan the local network for SMB100A generators.

    :param float max_time: The maximum time we will wait, in seconds
    :param int max_devices: Stop the search after this many devices have been found
    :return: A list of SMB100AZeroconf objects describing the found devices.
    :rtype: list[SMB100AZeroconf]
    """

    return net.zeroconf_scan(ZCListener(), max_time, max_devices)


class SMB100A(SMB100A_gen):
    pass


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    devices = find_smb100a(max_devices=1)
    print("Found %s" % devices[0])
    smb = connect_ethernet(devices[0].ip_address)
    print(smb.IDN.q())
