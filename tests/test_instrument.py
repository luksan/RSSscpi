# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
import logging

import pytest
from .conftest import VISA  # noqa: F401

from RSSscpi.zva import ZVA  # noqa: F401
from RSSscpi.znb import ZNB  # noqa: F401
from RSSscpi.Instrument import InstrumentError


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
            "*CLS;*ESE 127;*SRE 36",
            "*OPC?",
            "*OPC",
            "*TRG",
            ] == visa.cmd


def test_query_write(dummy_znb, visa):
    """
    :param ZNB znb:
    :param VISA visa:
    """
    vna = dummy_znb
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


def test_error_handling(dummy_zva, visa):
    # type: (ZVA, VISA) -> None
    zva = dummy_zva
    zva.init()
    zva.SOURce(1).POWer(1).ATTenuation().w(80)
    visa.ret_dict["SYSTem:ERRor:ALL?"] = '-222,"Data out of range;SOURce1:POWer1:ATTenuation 80\n"'
    visa.raise_error()
    with pytest.raises(InstrumentError) as excinfo:
        zva.query_OPC()  # The exception won't be raised until the next SCPI operation
    assert excinfo.value.stack is not None
    visa.ret_dict["SYSTem:ERRor:ALL?"] = '''-151,"Invalid string data;CALCulate1:PARameter:SDEFine '...",-114,"Header suffix out of range;DISPlay:WINDow1:TRACe:EFEed 'A..."'''
    zva.CALCulate(1).PARameter.SDEFine().w('AVG', 'BASD01D01AVG')
    visa.raise_error()
    with pytest.raises(InstrumentError) as excinfo:
        zva.query_OPC()
    assert excinfo.value.stack is not None


def test_logging(dummy_zva, visa, caplog):
    zva = dummy_zva
    caplog.set_level(logging.INFO)

    def check_log(msg):
        if isinstance(msg, str):
            msg = (msg, )
        for m, rec in zip(msg, caplog.records):
            time, _, data = rec.getMessage().partition("\t")
            assert data == m
        caplog.clear()

    zva.OPC.w()
    check_log("*OPC")
    zva.OPC.q()
    check_log("*OPC? -> '1'")
    zva.OPC.q(fmt="x"*200)
    check_log("*OPC? " + "x" * zva.MAX_RESPONSE_LOG_LENGTH + " -> '1'")
