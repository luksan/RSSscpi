# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function

import pytest
from .conftest import VISA  # noqa: F401

from RSSscpi.nrp import NRPxxSN  # noqa: F401


def test_nrp_init(nrpxxsn, visa):
    # type: (NRPxxSN, VISA) -> None
    nrpxxsn.init()
    assert ["*CLS;*ESE 127;*SRE 36",
            "ABORt",
            "*IDN?",
            ] == visa.cmd
    # FIXME: add typical IDN string as test vector


def test_basic_commands(nrpxxsn, visa):
    # type: (NRPxxSN, VISA) -> None
    nrpxxsn.init_immediate()
    nrpxxsn.cal_zero()
    assert ["INITiate:IMMediate",
            "CALibration:ZERO:AUTO ONCE",
            ] == visa.cmd

    visa.ret = "1,2,3,4,5"
    x = nrpxxsn.fetch_data()
    assert ["FETCh?"] == visa.cmd
    assert x == [1, 2, 3, 4, 5]


def test_numpy(nrpxxsn, visa):
    # type: (NRPxxSN, VISA) -> None
    numpy = pytest.importorskip("numpy")
    visa.ret = "1,2,3,4,5,6"
    x = nrpxxsn.fetch_numpy()
    assert ["FETCh?"] == visa.cmd
    assert isinstance(x, numpy.ndarray)
    assert numpy.array_equal(x, [1, 2, 3, 4, 5, 6])


def test_nrp_scpi_properties(nrpxxsn, visa):
    # type: (NRPxxSN, VISA) -> None

    nrpxxsn.frequency = 20e9
    assert nrpxxsn.frequency == 1
    nrpxxsn.frequency_minmax.query_default()
    assert ["SENSe:FREQuency 20000000000.0",
            "SENSe:FREQuency?",
            "SENSe:FREQuency? DEF",
            ] == visa.cmd

    nrpxxsn.init_cont = "OFF"
    nrpxxsn.init_cont = False
    visa.ret = "OFF"
    assert nrpxxsn.init_cont is False
    visa.ret = "ON"
    assert nrpxxsn.init_cont is True
    assert ["INITiate:CONTinuous OFF",
            "INITiate:CONTinuous OFF",
            "INITiate:CONTinuous?",
            "INITiate:CONTinuous?",
            ] == visa.cmd


def test_system_info(nrpxxsn, visa):
    # type: (NRPxxSN, VISA) -> None
    visa.ret = '"MAC:09:09:09\nX:9\nempty:\n"'  # FIXME: use a proper test vector
    x = nrpxxsn.query_system_info()
    assert ["SYSTem:INFO?"] == visa.cmd
    assert len(x) == 3
    assert x['MAC'] == "09:09:09"
    assert x['X'] == "9"
    assert x['empty'] == ""
