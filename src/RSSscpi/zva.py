# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from .gen import ZVA_gen
import znb

import logging


class ZVA(ZVA_gen, znb.ZNB):
    def __init__(self, visa_res):
        super(ZVA, self).__init__(visa_res=visa_res)
        self.filesystem = Filesystem(self)
        self.logger = logging.getLogger(__name__)
        self.visa_logger = self.logger.getChild("VISA")

    #def init(self):
        # SYSTem:DATA:SIZE ALL | AUTO

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


class Diagram(ZVA_gen.DISPlay.WINDow, znb.Diagram):
    pass


class Filesystem(ZVA_gen.MMEMory, znb.Filesystem):
    pass


class Limit(ZVA_gen.CALCulate.LIMit, znb.Limit):
    pass


class Marker(ZVA_gen.CALCulate.MARKer, znb.Marker):
    pass


class Sweep(ZVA_gen.SENSe.SWEep, znb.Sweep):
    pass


class SweepSegment(ZVA_gen.SENSe.SEGMent, znb.SweepSegment):
    pass


class Trace(znb.Trace):
    def get_marker(self, n):
        return Marker(n, self)
