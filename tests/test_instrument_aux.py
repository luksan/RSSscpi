# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import pytest
from .conftest import VISA  # noqa: F401

from RSSscpi.instrument import LimitedCapacityDict
from RSSscpi.instrument import SCPICmdFormatter


def test_SCPICmdFormatter():
    f = SCPICmdFormatter
    arg = (1, 2, 3)
    assert f().vformat("{:q*}", (arg, ), {}) == "'1', '2', '3'"
    assert f().format("{:d*}", arg) == "1, 2, 3"
    assert f().format("{:s}", arg) == "(1, 2, 3)"
    assert f().format("{:q}", arg) == "'(1, 2, 3)'"
    assert f().format("{:q}", "'Q'") == "'Q'"
    assert f().format("{:s}", "'Q'") == "'Q'"
    assert f().format("{:q}", "Q") == "'Q'"
    assert f().format("{:s}", "Q") == "Q"
    arg_str_list = ("'Q'", "Q", "S", "'S'")
    assert f().format("{:q}, {:q}, {:s}, {:s}", *arg_str_list) == "'Q', 'Q', S, 'S'"
    assert f().format("{:q*}", arg_str_list) == "'Q', 'Q', 'S', 'S'"
    assert f().format("{:s*}", arg_str_list) == "'Q', Q, S, 'S'"
    assert f().format("{0:s}", "hej") == "hej"
    assert f().format("{0:q}", "HEJsan") == "'HEJsan'"
    assert f().format("{0:d*}", [1, 2, 3]) == "1, 2, 3"
    assert f().format("{:.2f*}", [1, 2, 3]) == "1.00, 2.00, 3.00"
    assert f().format("{} - {:q*}", "CMd", ["str", "list"]) == "CMd - 'str', 'list'"
    assert f().format("{:d**}", zip([1, 2, 3], [4, 5, 6])) == "1, 4, 2, 5, 3, 6"


def test_cmd_formatting(dummy_zva, visa):
    # type: (ZVA, VISA) -> None
    zva = dummy_zva
    zva.TRACe.COPY.MATH.w("MDATA8")  # This shouldn't be quoted
    zva.TRACe.COPY.MATH.w("sq")  # Quote
    zva.SENSe.SWEep.POINts.w(1e9)
    zva.SENSe.SWEep.POINts.w("1000000000")
    zva.SENSe.SWEep.POINts.w(1000000000)
    zva.TRIGger.SEQuence.LINK.w("POINt")  # This should be quoted
    zva.TRIGger.SEQuence.LINK.w("'POINT'")  # This should only have one pair of quotes
    with pytest.warns(UserWarning) as record:  # This should warn since ..:Y? has an empty argument list
        zva.CALCulate.MARKer.Y.q("")
        zva.CALCulate.MARKer.Y.q("asd", fmt="{:s}")
        zva.CALCulate.MARKer.Y.q("asd", fmt="")
    assert len(record) == 1
    assert ["TRACe:COPY:MATH MDATA8",
            "TRACe:COPY:MATH 'sq'",
            "SENSe:SWEep:POINts 1000000000.0",
            "SENSe:SWEep:POINts 1000000000",
            "SENSe:SWEep:POINts 1000000000",
            "TRIGger:SEQuence:LINK 'POINt'",
            "TRIGger:SEQuence:LINK 'POINT'",
            "CALCulate:MARKer:Y?",
            "CALCulate:MARKer:Y? asd",
            "CALCulate:MARKer:Y?",
            ] == visa.cmd


def test_cmd_formatting_with_param_enc(dummy_zva, visa):
    w = dummy_zva.OPC.w

    w(param_enc=())
    assert visa.cmd == ["*OPC"]
    w(b'ABC', param_enc="b")
    assert visa.cmd == ["*OPC ABC"]

    bin_data = b"\x00\x01\x10\xFF"
    w(bin_data, param_enc="b")
    w(bin_data, param_enc="ieee")
    w(bin_data, bin_data, param_enc=("ieee", "b"))
    w(bin_data, range(10), bin_data, param_enc=("ieee", "d*", "b"))
    assert visa.cmd == [
        b'*OPC \x00\x01\x10\xff',
        b'*OPC #14\x00\x01\x10\xff',
        b'*OPC #14\x00\x01\x10\xff, \x00\x01\x10\xff',
        b'*OPC #14\x00\x01\x10\xff, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \x00\x01\x10\xff',
    ]

    with pytest.raises(ValueError):  # Cannot use fmt and param_enc at the same time
        w(b'\x00\xff', fmt="{:s}", param_enc="b")
    with pytest.raises(AssertionError):  # Not enough elements in param_enc
        w(1, 2, 3, param_enc=("b", "b"))
    with pytest.raises(AssertionError):  # Too many elements in param_enc
        w(1, param_enc=("b", "b"))

def test_unicode_cmds(dummy_zva, visa, caplog):
    zva = dummy_zva
    visa.encoding = "utf8"
    visa.ret = "åäö"
    assert zva.OPC.q("åäö", fmt="{:s}") == "åäö"
    assert visa.cmd == ["*OPC? åäö" ]


def test_LimitedCapacityDict():
    d = LimitedCapacityDict()
    assert d.max_len is None
    for n in range(100):
        d[n] = str(n)
    assert len(d) == 100
    assert list(d.keys()) == list(range(100))
    d.max_len = 150
    assert len(d) == 100
    d.max_len = 100
    assert len(d) == 100
    d.max_len = 50
    assert len(d) == 50
    assert list(d.keys()) == list(range(50, 100))
    for n in range(20):
        d[n] = str(n)
    assert len(d) == 50
    assert list(d.keys()) == list(range(70, 100)) + list(range(20))

    # check that rewritten elements are moved to the end
    for n in range(70, 80):
        d[n] = str(n)
    assert list(d.keys()) == list(range(80, 100)) + list(range(20)) + list(range(70, 80))
