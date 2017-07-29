# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from RSSscpi.gen.NRPxxSN_gen import NRPxxSN_gen
from RSSscpi.SCPI_property import SCPIProperty, SCPIPropertyMinMax

import visa
import socket
import threading


def connect_ethernet(ip_address):
    # type: ([str, unicode]) -> NRPxxSN
    """
    Helper to connect to a power sensor via Ethernet / TCPIP / VISA.
    Creates an NRPxxSN instance and calls init() on it before returning.

    :param ip_address: The ip address in string format
    :return: An initialized NRPxxSN instance.
    :rtype: NRPxxSN
    """
    rm = visa.ResourceManager()
    visa_str = 'TCPIP::' + ip_address + '::INSTR'
    visa_res = rm.open_resource(visa_str)
    nrp = NRPxxSN(visa_res)
    nrp.visa_logger.info("Connected to " + visa_str)
    nrp.init()
    return nrp


class NRPZeroconf(object):
    def __init__(self, zeroconf_info):
        i = zeroconf_info
        self.name = i.name.split()[0]  # nrp33sn-100927
        self.mac = i.name.split()[1][1:len("00:90:b8:1f:7c:29")+1]
        self.ip_address = socket.inet_ntoa(i.address)

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.mac, self.ip_address)


def find_sensors(max_time=2, max_sensors=None):
    """
    Use zeroconf to scan the local network for NRP sensors.

    :param float max_time: The maximum time we will wait, in seconds
    :param int max_sensors: Stop the search after this many sensors have been found
    :return: A list of NRPZeroconf objects describing the found sensors.
    :rtype: list[NRPZeroconf]
    """
    from zeroconf import Zeroconf, ServiceBrowser
    found_sensors = []
    stop_search = threading.Condition()

    class Listener(object):
        @staticmethod
        def add_service(zc, type_, name):
            stop_search.acquire()
            info = zc.get_service_info(type_, name)
            if info.name[:3] != "nrp":
                return
            found_sensors.append(NRPZeroconf(info))
            if max_sensors is not None and len(found_sensors) >= max_sensors:
                stop_search.notify_all()
            stop_search.release()

    z = Zeroconf()
    listener = Listener()
    stop_search.acquire()
    try:
        ServiceBrowser(z, "_workstation._tcp.local.", listener)
        stop_search.wait(max_time)
    finally:
        z.close()

    return found_sensors


class NRPxxSN(NRPxxSN_gen):
    def __init__(self, visa_res):
        super(NRPxxSN, self).__init__(visa_res)

    def init(self):
        super(NRPxxSN, self).init()
        self._visa_res.timeout = 6000  # Zeroing the sensor takes ca 5 seconds
        self.ABORt.w()
        idn = self.IDN.q()
        self.visa_logger.info("NRP sensor initialized: %s", idn)

    def query_system_info(self):
        """
        Queries SYSTem:INFO? and returns the respons parsed in to a dict()
        """
        # SYST:INFO? => "A:B\nC:D\n....\n"
        info_list = str(self.SYSTem.INFO.q()).strip('" \n').split("\n")
        return dict([x.split(":", 1) for x in info_list])

    def init_immediate(self):
        """
        Sends INITiate:IMMediate to the sensor to begin a measurement cycle.
        """
        self.INITiate.IMMediate.w()  # TODO: this should be in Instrument

    def cal_zero(self):
        """
        Run the zero level adjustment routine. Disconnect power from the sensor before running.
        """
        self.CALibration.ZERO.AUTO().w("ONCE")

    def fetch_data(self):
        # type: () -> [float]
        """
        Get the data from the measurement buffer using FETCh?

        :return: A list of floats
        """
        x = self.FETCh.q()
        return list(map(float, x.split_comma()))  # TODO: add this as a method to SCPIResponse

    def fetch_numpy(self):
        """
        Get the data from the measurement buffer using FETCh?

        :return: The data from the measurement buffer, stored in a numpy array.
        """
        return self.FETCh.q().numpy_array()

    frequency = SCPIPropertyMinMax(NRPxxSN_gen.SENSe.FREQuency, float)
    init_cont = SCPIProperty(NRPxxSN_gen.INITiate.CONTinuous, bool)  # FIXME: This node should be a SCPIBool


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    sensors = find_sensors(max_sensors=1)
    print("Found %s" % sensors[0])
    sensor = connect_ethernet(sensors[0].ip_address)
