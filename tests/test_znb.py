# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import pytest
from pytest import raises
import inspect
import logging
import sys

from RSSscpi import ZNB, ZVA
from common import *

logging.basicConfig(stream=sys.stdout)


def test_marker(dummy_vna):
    """
    Test that the Marker class works as expected.

    :param ZNB dummy_vna: This can be either a ZVA or ZNB instance with visa_res = visa dummy.
    """
    ch = dummy_vna.get_channel(2)
    tr = ch.get_trace("Tr1")
    m1 = tr.get_marker(3)
    assert [] == visa.cmd

    x = m1.tracking
    m1.tracking = False
    assert ["CALCulate2:PARameter:SELect 'Tr1'",
            "CALCulate2:MARKer3:SEARch:TRACking?",
            "CALCulate2:MARKer3:SEARch:TRACking OFF"] == visa.cmd
    assert isinstance(x, bool)

    tr.name = "Tr2"  # Change the trace name to force an "active trace" select
    visa.clear_cmd()
    m1.is_enabled = True
    x = m1.is_enabled
    m1.is_enabled = "OFF"
    assert ["CALCulate2:PARameter:SELect 'Tr2'",
            "CALCulate2:MARKer3:STATe ON",
            "CALCulate2:MARKer3:STATe?",
            "CALCulate2:MARKer3:STATe OFF"] == visa.cmd
    assert isinstance(x, bool)

    m1.x = 3.3
    x = m1.x
    assert ["CALCulate2:MARKer3:X 3.3",
            "CALCulate2:MARKer3:X?"] == visa.cmd
    assert isinstance(x, float)

    x = m1.y
    assert ["CALCulate2:MARKer3:Y?"] == visa.cmd
    assert isinstance(x, float)

    with raises(AttributeError, message="Assignment to marker y value is not possible."):
        m1.y = 2
