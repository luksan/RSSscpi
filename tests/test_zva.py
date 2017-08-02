# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function

import pytest
from .conftest import VISA  # noqa: F401

from RSSscpi.zva import ZVA  # noqa: F401


def test_vna_port(zva, visa):
    # type: (ZVA, VISA) -> None
    ch = zva.get_channel(1)
    p2 = ch.get_vna_port(2)

    p2.src_attenuator = 20
    x = p2.src_attenuator
    assert isinstance(x, int) and x == 1
    assert ["SOURce1:POWer2:ATTenuation 20",
            "SOURce1:POWer2:ATTenuation:AUTO:VALue?",
            ] == visa.cmd

    visa.ret = "MAN"
    p2.src_attenuator_mode = "AUTO"
    assert p2.src_attenuator_mode == "MAN"
    assert ["SOURce1:POWer2:ATTenuation:MODE AUTO",
            "SOURce1:POWer2:ATTenuation:MODE?",
            ] == visa.cmd
