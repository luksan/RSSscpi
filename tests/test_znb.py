# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from .common import *
from RSSscpi import ZNB, ZVA


def test_channel(dummy_vna, visa):
    """

    :param ZNB dummy_vna:
    :return:
    """
    ch = dummy_vna.get_channel(3)
    x = ch.sweep.points.query_default()
    assert isinstance(x, int)
    ch.sweep.points.value = 301
    x = ch.sweep.points.value
    assert isinstance(x, int)
    ch.sweep.points = 301
    ch.sweep.TYPE.w("LIN")
    ch.configure_freq_sweep(10, 10e6, points=101, ifbw=1e3, power=-10, log_sweep=True)
    ch.init_sweep()
    assert ["SENSe3:SWEep:POINts? DEF",
            "SENSe3:SWEep:POINts 301",
            "SENSe3:SWEep:POINts?",
            "SENSe3:SWEep:POINts 301",
            "SENSe3:SWEep:TYPE LIN",
            "SENSe3:SWEep:TYPE LOG",
            "SENSe3:FREQuency:STARt 10",
            "SENSe3:FREQuency:STOP 10000000.0",
            "SENSe3:SWEep:POINts 101",
            "SENSe3:BANDwidth 1000.0",
            "SOURce3:POWer:LEVel:IMMediate:AMPLitude -10",
            "INITiate3:IMMediate",
            ] == visa.cmd


def test_diagram(dummy_vna, visa):
    """
    :param ZNB dummy_vna:
    :param VISA visa:
    """
    dia = dummy_vna.get_diagram(1)
    f = dia.save_screenshot("hej.png")
    assert str(f) == "1\hej.png"
    assert ["MMEMory:NAME 'hej.png'",
            "HCOPy:DESTination 'MMEM'",
            "HCOPy:DEVice:LANGuage PNG",
            "DISPlay:WINDow1:MAXimize?",
            "DISPlay:WINDow1:MAXimize ON",
            "HCOPy:PAGE:WINDow ACTive",
            "HCOPy:IMMediate",
            "MMEMory:CDIRectory?",
            ] == visa.cmd
    assert dia.is_maximized
    dia.is_maximized = False
    dia.select_diagram()
    assert dia.n == 1
    dia.delete()
    assert dia.name == "1"
    dia.name = "Name2"
    assert dia.title == "1"
    dia.title = "Title2"
    assert dia.title_is_visible is True
    assert ["DISPlay:WINDow1:MAXimize?",
            "DISPlay:WINDow1:MAXimize OFF",
            "DISPlay:WINDow1:MAXimize?",
            "DISPlay:WINDow1:MAXimize ON",
            "DISPlay:WINDow1:STATe OFF",
            "DISPlay:WINDow1:NAME?",
            "DISPlay:WINDow1:NAME 'Name2'",
            "DISPlay:WINDow1:TITLe:DATA?",
            "DISPlay:WINDow1:TITLe:DATA 'Title2'",
            "DISPlay:WINDow1:TITLe:STATe?",
            ] == visa.cmd


def test_marker(dummy_vna, visa):
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

    with pytest.raises(AttributeError, message="Assignment to marker y value is not possible."):
        m1.y = 2


def test_trace(dummy_vna, visa):
    """

    :param ZNB dummy_vna:
    :return:
    """
    ch = dummy_vna.get_channel(2)
    tr = ch.get_trace("Tr7")
    tr.ref_level = 8
    x = tr.trace_format
    tr.trace_format = 2
    assert ["DISPlay:WINDow:TRACe:Y:SCALe:RLEVel 8, 'Tr7'",
            "CALCulate2:PARameter:SELect 'Tr7'",
            "CALCulate2:FORMat?",
            "CALCulate2:FORMat 2",
            ] == visa.cmd
