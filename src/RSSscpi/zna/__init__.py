from .. import znb
from .. import network as net

from ..gen import ZNA_gen

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

    def init(self, ese=None, **kwargs):
        if ese is None:
            ese = self.default_ese
            # Disable user request events, since that effectivly disables the Go to local button
            ese.user_request = False
        super().init(ese=ese, **kwargs)

    @property
    def scpi(self) -> ZNA_gen:
        return self._scpi

    def get_channel(self, n: int) -> Channel:
        """
        Creates a channel instance for the ZNA.

        :param n: Channel number
        :return: A Channel instance
        """
        return Channel(n, instrument=self)

    def get_diagram(self, n: int) -> Diagram:
        """
        Create a Diagram instance linked to the ZNA.

        :param n: Diagram number
        :return: A Diagram instance
        """
        return Diagram(n, instrument=self)
