# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import print_function

import logging
import sys
import os
import pytest

from RSSscpi import ZVA, ZNB
from RSSscpi.gen.SCPI_gen_support import DummyVisa

logging.basicConfig(stream=open(os.devnull, "w"))
logging.captureWarnings(True)

class VISA(DummyVisa):
    def __init__(self):
        super(VISA, self).__init__("")
        self._cmd = []

    def write(self, w):
        assert isinstance(w, str)
        self._cmd.append(w.strip())  # read()/write() in Instrument appends a space to the command even without arguments

    def query(self, q):
        assert isinstance(q, str)
        self._cmd.append(q.strip())
        return "1"

    def clear_cmd(self):
        self._cmd = []

    @property
    def cmd(self):
        """
        Returns a list of the commands submitted since the last invocation, and clears the internal list.
        """
        r = self._cmd
        self._cmd = []
        return r

    def print_cmd(self):
        """
        Print the command list in a format suitable for copy-paste.
        """
        print("assert [", end="")
        for x in self._cmd:
            print('"%s",' % (x))
        print("] == visa.cmd")


@pytest.fixture
def visa():
    return VISA()


@pytest.fixture(params=["ZVA", "ZNB"])
def dummy_vna(request, visa):
    visa.clear_cmd()
    if request.param == "ZVA":
        yield ZNB(visa_res=visa)
    if request.param == "ZNB":
        yield ZVA(visa_res=visa)


@pytest.fixture
def znb(visa):
    return ZNB(visa_res=visa)
