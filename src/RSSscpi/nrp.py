# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
import socket
from typing import List, Dict

from . import network as net
from .gen.NRPxxSN_gen import NRPxxSN_gen
from .instrument import Instrument
from .scpi.class_property import SCPIProperty, SCPIPropertyMinMax


def connect_ethernet(ip_address: str) -> "NRPxxSN":
    """
    Helper to connect to a power sensor via Ethernet / TCPIP / VISA.
    Creates an NRPxxSN instance and calls init() on it before returning.

    :param ip_address: The ip address in string format
    :return: An initialized NRPxxSN instance.
    :rtype: NRPxxSN
    """
    return net.connect_ethernet(NRPxxSN, ip_address)


class NRPZeroconf(net.ZeroconfInfo):

    def parse_zc_info(self, zeroconf_info):
        i = zeroconf_info
        self.name = i.name.split()[0]  # nrp33sn-100927
        self.mac = i.name.split()[1][1:len("00:90:b8:1f:7c:29") + 1]
        self.ip_address = socket.inet_ntoa(i.address)


class ZCListener(net.ZeroconfListener):
    info_class = NRPZeroconf
    service_name = "_workstation._tcp.local."

    def filter_zc_info(self, zc_info):
        return zc_info.name.startswith("nrp")


def find_sensors(max_time=2, max_sensors=None):
    """
    Use zeroconf to scan the local network for NRP sensors.

    :param float max_time: The maximum time we will wait, in seconds
    :param int max_sensors: Stop the search after this many sensors have been found
    :return: A list of NRPZeroconf objects describing the found sensors.
    :rtype: list[NRPZeroconf]
    """
    return net.zeroconf_scan(ZCListener(), max_time, max_sensors)


class NRPxxSN(Instrument):
    _scpi = NRPxxSN_gen()

    @property
    def scpi(self) -> NRPxxSN_gen:
        return self._scpi

    def init(self):
        super(NRPxxSN, self).init()
        self._visa_res.timeout = 6000  # Zeroing the sensor takes ca 5 seconds
        self.scpi.ABORt.w()
        idn = self.scpi.IDN.q()
        self.visa_logger.info("NRP sensor initialized: %s", idn)

    def query_system_info(self) -> Dict[str, str]:
        """
        Queries SYSTem:INFO? and returns the respons parsed in to a dict()
        """
        # SYST:INFO? => "A:B\nC:D\n....\n"
        info_list = str(self.scpi.SYSTem.INFO.q()).strip('" \n').split("\n")
        return dict([x.split(":", 1) for x in info_list])  # type: ignore

    def init_immediate(self):
        """
        Sends INITiate:IMMediate to the sensor to begin a measurement cycle.
        """
        self.scpi.INITiate.IMMediate.w()  # TODO: this should be in Instrument

    def cal_zero(self):
        """
        Run the zero level adjustment routine. Disconnect power from the sensor before running.
        """
        self.scpi.CALibration.ZERO.AUTO.w("ONCE")

    def fetch_data(self) -> List[float]:
        """
        Get the data from the measurement buffer using FETCh?

        :return: A list of floats
        """
        return self.scpi.FETCh.q().split_comma(convert=float)

    def fetch_numpy(self):
        """
        Get the data from the measurement buffer using FETCh?

        :return: The data from the measurement buffer, stored in a numpy array.
        """
        return self.scpi.FETCh.q().numpy_array()

    frequency = SCPIProperty(NRPxxSN_gen.SENSe.FREQuency, float, parent_prop=scpi)
    frequency_minmax = SCPIPropertyMinMax(frequency)
    init_cont = SCPIProperty(NRPxxSN_gen.INITiate.CONTinuous, bool, parent_prop=scpi)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    sensors = find_sensors(max_sensors=1)
    print("Found %s" % sensors[0])
    sensor = connect_ethernet(sensors[0].ip_address)
