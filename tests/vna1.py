# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function

from RSSscpi.Instrument import Instrument
from RSSscpi.scpi.gen_support import SCPINodeN


def node(name, *args):
    d = {"_cmd": name}
    for x in args:
        d[x._cmd] = x
    return type(name, (SCPINodeN, ), d)()


class VNA1(Instrument):

    def __init__(self, visa_res):
        super(VNA1, self).__init__(visa_res)
        self.bsub = Bsub1(parent=self.A)

    A = node("A", node("B", node("Ca", node("D", node("E"))),
                            node("Cb", node("D"))))

VNA1._SCPI_class = VNA1


class Bsub1(VNA1.A.B):
    pass

