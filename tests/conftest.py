# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
import os
import collections

import pytest

from RSSscpi import ZVA, ZNB
import RSSscpi.nrp

logging.basicConfig(stream=open(os.devnull, "w"))
logging.captureWarnings(True)


class VISA(object):
    def __init__(self):
        self._cmd = []
        self._def_ret = "1"
        self._def_set = False  # Indicates if the default was changed since the last query
        self.ret_dict = collections.defaultdict(lambda: self._def_ret)
        self.srq_callback = None
        self.stb = 0

    def install_handler(self, event_type, func, user_handle):
        self.srq_callback = func

    def raise_error(self):
        self.stb = 0x04
        self.srq_callback(None, None, None, None)
        self.stb = 0

    def enable_event(*args):
        pass

    def read_stb(self):
        return self.stb

    @property
    def ret(self):
        """
        The value returned from query()
        """
        return self._def_ret

    @ret.setter
    def ret(self, val):
        self._def_ret = val
        self._def_set = True

    def write(self, w):
        assert isinstance(w, str) or isinstance(w, type(u""))
        self._cmd.append(w)

    def query(self, q):
        assert isinstance(q, str) or isinstance(q, type(u""))
        self._cmd.append(q)
        if self._def_set:  # If the default was changed we overwrite any existing value for the following query
            self.ret_dict[q] = self._def_ret
            self._def_set = False
        return self.ret_dict[q]

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
        yield ZVA(visa_res=visa)
    if request.param == "ZNB":
        yield ZNB(visa_res=visa)


@pytest.fixture
def dummy_zva(visa):
    return ZVA(visa_res=visa)


@pytest.fixture
def dummy_znb(visa):
    return ZNB(visa_res=visa)


@pytest.fixture
def nrpxxsn(visa):
    return RSSscpi.nrp.NRPxxSN(visa_res=visa)


@pytest.fixture(params=[0, 1, 1e9])
def scpi_float(request):
    x = request.param
    return x, str(x)


def pytest_exception_interact(node, call, report):
    # print the VISA command log on exception
    if hasattr(node, 'funcargs') and 'visa' in node.funcargs:
        node.funcargs['visa'].print_cmd()
