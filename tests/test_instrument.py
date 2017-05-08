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


