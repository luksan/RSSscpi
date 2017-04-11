# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:57:01 2016

@author: Lukas Sandström
"""

import inspect
import logging
import sys

from RSSscpi import ZNB
from RSSscpi.gen.SCPI_gen_support import DummyVisa, SCPINodeBase

logging.basicConfig(stream=sys.stdout)

znb = ZNB(DummyVisa("K1"))


def test_trace():
    print "*  test_trace()"
    ch = znb.get_channel(2)
    tr = ch.get_trace("Tr2")
    x = tr.trace_format
    tr.trace_format = 2


def test_channel():
    print "*  test_channel()"
    ch = znb.get_channel(3)
    ch.sweep.points.query_default()
    ch.sweep.points.value = 301
    ch.sweep.points = 301
    ch.sweep.TYPE.w("LIN")
    ch.configure_freq_sweep(10, 10e6, points=101, ifbw=1e3, power=-10, log_sweep=True)
    ch.init_sweep()


def test_diagram():
    print "*  test_diagram()"
    dia = znb.get_diagram(1)
    dia.save_screenshot("hej.png")


def test_sweep():
    pass

test_channel()
test_trace()
test_diagram()

