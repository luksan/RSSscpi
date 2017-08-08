# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import visa
import socket
import threading
import logging


def connect_ethernet(instr_class, ip_address, proto="INSTR"):
    """
    Helper to connect to an Instrument via Ethernet / TCPIP / VISA.
    Creates an `instr_class` instance and calls init() on it before returning.

    :param instr_class: The type of instrument we are connecting to, a subclass of Instrument.
    :param ip_address: The ip address in string format
    :param proto: The last part of the VISA resource string. Default is "INSTR", "hislip0" could be an alternative.
    :return: An initialized Instrument instance.
    """
    rm = visa.ResourceManager()
    visa_str = 'TCPIP::' + ip_address + '::' + proto
    visa_res = rm.open_resource(visa_str)
    dev = instr_class(visa_res)
    dev.visa_logger.info("Connected to " + visa_str)
    dev.init()
    return dev


class ZeroconfInfo(object):
    def __init__(self, zeroconf_info):
        self.name = ""
        self.ip_address = ""
        self.mac = ""

        self.parse_zc_info(zeroconf_info)

    def parse_zc_info(self, zeroconf_info):
        i = zeroconf_info
        self.name = i.name.split()[0]  # nrp33sn-100927
        self.mac = i.name.split()[1][1:len("00:90:b8:1f:7c:29")+1]
        self.ip_address = socket.inet_ntoa(i.address)

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.mac, self.ip_address)


class ZeroconfListener(object):
    info_class = ZeroconfInfo
    service_name = "_hislip._tcp.local."

    def __init__(self):
        self.max_devices = None
        self.found_sensors = []
        self.stop_search = threading.Event()

    def add_service(self, zc, type_, name):
        logging.debug("Service added, %s, %s", type_, name)
        info = zc.get_service_info(type_, name)
        if not self.filter_zc_info(info):
            return
        self.found_sensors.append(self.info_class(info))
        logging.debug("Found device %s", self.found_sensors[-1])
        if self.max_devices is not None and len(self.found_sensors) >= self.max_devices:
            self.stop_search.set()

    def filter_zc_info(self, zc_info):
        """
        Return True if this zc_info describes a relevant device
        """
        return True


def zeroconf_scan(listener, max_time=2, max_devices=None):
    """
    Use zeroconf to scan the local network for NRP sensors.

    :param ZeroconfListener listener: This object will be invoked for every Zeroconf device discovered
    :param float max_time: The maximum time we will wait, in seconds
    :param int max_devices: Stop the search after this many devices have been found
    :return: A list of ZeroconfInfo objects describing the found devices.
    """
    from zeroconf import Zeroconf, ServiceBrowser

    z = Zeroconf()
    listener.max_devices = max_devices
    try:
        ServiceBrowser(z, listener.service_name, listener)
        listener.stop_search.wait(max_time)
    finally:
        z.close()

    return listener.found_sensors


if __name__ == "__main__":
    pass
