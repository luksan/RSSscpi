# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import division, print_function

from .vna1 import VNA1, Bsub1, SCPINodeN


def node(name, *args):
    d = {"_cmd": name}
    for x in args:
        d[x._cmd] = x
    return type(name, (SCPINodeN, ), d)()


class VNA2(VNA1):

    def __init__(self, visa_res):
        super(VNA2, self).__init__(visa_res)
        print (self.A.__class__)
        self.bsub = Bsub2(parent=self.A)

    A = node("A", node("B", node("Ca", node("D"))))
    Aa = node("Aa", node("B"), node("Ca", node("D")))

VNA2._SCPI_class = VNA2


class Bsub2(VNA2.A.B, Bsub1):
    pass
