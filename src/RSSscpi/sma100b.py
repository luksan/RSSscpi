# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from RSSscpi.gen.SMA100B_gen import SMA100B_gen
from RSSscpi.SCPI_property import SCPIProperty, SCPIPropertyMinMax

import visa
import socket
import threading


def connect_ethernet(ip_address):
    # type: ([str, unicode]) -> SMA100B
    """
    Helper to connect to a SMA100B signal generator via Ethernet / TCPIP / VISA.
    Creates an SMA100B instance and calls init() on it before returning.

    :param ip_address: The ip address in string format
    :return: An initialized SMA100B instance.
    :rtype: SMA100B
    """
    rm = visa.ResourceManager()
    visa_str = 'TCPIP::' + ip_address + '::hislip0'
    visa_res = rm.open_resource(visa_str)
    nrp = SMA100B(visa_res)
    nrp.visa_logger.info("Connected to " + visa_str)
    nrp.init()
    return nrp


class SMA100BZeroconf(object):
    def __init__(self, zeroconf_info):
        i = zeroconf_info
        (sma, fw, sn) = i.name.split()
        self.name = sma + "-" + sn[:6]  # SMA100B-xxxxxx
        self.fw = fw.strip("()")
        self.ip_address = socket.inet_ntoa(i.address)

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.fw, self.ip_address)


def find_sma100b(max_time=2, max_devices=None):
    """
    Use zeroconf to scan the local network for SMA100B generators.

    :param float max_time: The maximum time we will wait, in seconds
    :param int max_devices: Stop the search after this many devices have been found
    :return: A list of SMA100BZeroconf objects describing the found devices.
    :rtype: list[SMA100BZeroconf]
    """
    from zeroconf import Zeroconf, ServiceBrowser
    found_devices = []
    stop_search = threading.Condition()

    class Listener(object):
        @staticmethod
        def add_service(zc, type_, name):
            stop_search.acquire()
            info = zc.get_service_info(type_, name)
            if not info.name.startswith("SMA100B"):
                return
            found_devices.append(SMA100BZeroconf(info))
            if max_devices is not None and len(found_devices) >= max_devices:
                stop_search.notify_all()
            stop_search.release()

    z = Zeroconf()
    listener = Listener()
    stop_search.acquire()
    try:
        ServiceBrowser(z, "_hislip._tcp.local.", listener)
        stop_search.wait(max_time)
    finally:
        z.close()

    return found_devices


class SMA100B(SMA100B_gen):
    pass

if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    devices = find_sma100b(max_devices=1)
    print("Found %s" % devices[0])
    sma = connect_ethernet(devices[0].ip_address)
    print(sma.IDN.q())
