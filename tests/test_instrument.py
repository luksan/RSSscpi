# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import pytest
from .conftest import VISA  # noqa: F401

from RSSscpi import ZNB  # noqa: F401


def test_generic_commands(dummy_vna, visa):
    """
    :param ZNB dummy_vna:
    :param VISA visa:
    """
    vna = dummy_vna
    vna.update_display(once=True)
    vna.update_display(once=False)
    vna.update_display(False)
    vna.update_display(True)
    vna.update_display(True, once=True)
    vna.update_display(True, once=False)
    vna.update_display(False, once=True)
    vna.update_display(False, once=False)
    vna.preset()
    vna.query_OPC()
    vna.send_OPC()
    vna.send_TRG()
    assert ["SYSTem:DISPlay:UPDate ONCE",
            "SYSTem:DISPlay:UPDate ON",
            "SYSTem:DISPlay:UPDate OFF",
            "SYSTem:DISPlay:UPDate ON",
            "SYSTem:DISPlay:UPDate ONCE",
            "SYSTem:DISPlay:UPDate ON",
            "SYSTem:DISPlay:UPDate OFF",
            "SYSTem:DISPlay:UPDate OFF",
            "*RST",
            "*OPC?",
            "*OPC",
            "*TRG",
            ] == visa.cmd


def test_query_write(znb, visa):
    """
    :param ZNB znb:
    :param VISA visa:
    """
    vna = znb
    vna.OPC.q("ABC", quote=True)
    vna.OPC.q("'ABC'", quote=True)
    vna.OPC.q("ABC", quote=False)
    vna.OPC.w("ABC", quote=True)
    vna.OPC.w("'ABC'", quote=True)
    vna.OPC.w("ABC", quote=False)
    vna.OPC.w("ABC")
    assert ["*OPC? 'ABC'",
            "*OPC? 'ABC'",
            "*OPC? ABC",
            "*OPC 'ABC'",
            "*OPC 'ABC'",
            "*OPC ABC",
            "*OPC ABC",
            ] == visa.cmd
    vna.OPC.w("A", "B", "C", "", "E")
    vna.OPC.w("A", "B", "C", "", "E", quote=True)
    vna.OPC.w(("A", "B", "C", "", "E"), quote=True, fmt="{:s*}")
    assert ["*OPC A, B, C, , E",
            "*OPC 'A', 'B', 'C', '', 'E'",
            "*OPC A, B, C, , E",
            ] == visa.cmd
