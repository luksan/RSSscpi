from RSSscpi.gen import ZNA_gen
import RSSscpi.znb as znb
from .. import network as net

from .channel import Channel
from .diagram import Diagram


def connect_ip(ip_address: str) -> "ZNA":
    """
    Helper to connect to a ZNA VNA via TCPIP / HiSLIP / VISA.
    Creates an ZNA instance and calls init() on it before returning.

    :param ip_address: The ip address in string format
    :return: An initialized ZNA instance.
    :rtype: ZNA
    """
    return net.connect_ethernet(ZNA, ip_address, "hislip0")


class ZNA(znb.ZNB):
    _scpi = ZNA_gen()

    @property
    def scpi(self) -> ZNA_gen:
        return self._scpi

    def get_channel(self, n: int):
        return Channel(n, instrument=self)

    def get_diagram(self, n):
        return Diagram(n, instrument=self)
