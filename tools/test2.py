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


def test_diagram():
    print "*  test_diagram()"
    dia = znb.get_diagram(1)
    dia.save_screenshot("hej.png")


def test_sweep():
    pass

test_diagram()

