from RSSscpi.gen import ZNA_gen
import RSSscpi.znb as znb

from .channel import Channel
from .diagram import Diagram


class ZNA(znb.ZNB):
    _scpi = ZNA_gen()

    @property
    def scpi(self) -> ZNA_gen:
        return self._scpi

    def get_channel(self, n: int):
        return Channel(n, instrument=self)

    def get_diagram(self, n):
        return Diagram(n, instrument=self)
