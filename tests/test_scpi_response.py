# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import pytest

import struct

from RSSscpi.scpi.response import make_ieee_data_block, SCPIResponse  # noqa: F401


@pytest.mark.parametrize('expected, txt', [
    (True,  ("1", "ON", "on", "On")),
    (False, ("0", "OFF", "off", "Off")),
    (None,  ("OF", "O", "1.0", "0.0"))
    ])
def test_bool(expected, txt):
    for x in txt:
        if expected is None:
            with pytest.raises(ValueError):
                bool(SCPIResponse(x))
        else:
            assert expected == bool(SCPIResponse(x))


@pytest.mark.parametrize('param,expect', [
    ("1", 1),
    ("-2", -2),
    ("-3 dBm", -3)])
def test_int(param, expect):
    assert int(SCPIResponse(param + "\r\n")) == expect


@pytest.mark.parametrize('param,expect', [
    ("1E-9", 1e-9),
    ("-2.5", -2.5),
    ("-3.33 dBm", -3.33),
    ("1.5E+9", 1.5e9),
    ("9.9E37", 9.9e37),  # +Infinity
    ("-9.9E37", -9.9e37),  # -Infinity
    ("9.91E37", 9.91e37),  # NaN
])
def test_float(param, expect):
    assert float(SCPIResponse(param + "\r\n")) == expect


def test_comma_list_pairs():
    s = list(map(str, range(10)))
    resp = SCPIResponse(",".join(s))
    assert resp.comma_list_pairs() == list(zip(s[0::2], s[1::2]))
    conv = resp.comma_list_pairs(convert=lambda x: (int(x[0]), int(x[1]+"0")))
    assert all((a+1)*10 == b and isinstance(a, int) for a, b in conv)


def test_split_comma():
    n = "'1, ASD, 2, K,3,t,4,f'"
    assert SCPIResponse(n).split_comma() == list(map(lambda x: x.strip(" '"), n.split(",")))
    n = ",".join(map(str, range(10)))
    assert SCPIResponse(n).split_comma(convert=int) == list(range(10))


def test_complex_list():
    def cplx2bin(cplx: complex):
        return struct.pack("f", cplx.real) + struct.pack("f", cplx.imag)

    def cplx2str(cplx: complex):
        return str(cplx.real) + "," + str(cplx.imag)

    expect = list(map(complex, range(0, 100, 2), range(1, 101, 2)))
    bin_data = make_ieee_data_block(b"".join(map(cplx2bin, expect)))
    assert SCPIResponse(bin_data).complex_list(float_size=4) == expect
    assert SCPIResponse(",".join(map(cplx2str, expect))).complex_list() == expect
    assert SCPIResponse(b'\r\n').complex_list() == []


def test_block_data_reponse():
    with pytest.raises(ValueError):  # Incorrect data
        SCPIResponse(b"1").block_data()
    with pytest.raises(ValueError):  # Missing '#' at start of header
        SCPIResponse(b"11A").block_data()
    with pytest.raises(ValueError):  # '-' instead of '#' at start of header
        SCPIResponse(b"-11A").block_data()
    with pytest.raises(ValueError):  # Not enugh data
        SCPIResponse(b"#19" + b"A"*8).block_data()
    assert SCPIResponse(b"#11\x01").block_data() == b"\x01"
    assert SCPIResponse(b"#210" + b"A" * 10).block_data() == b"A" * 10


def test_block_data_formatting():
    with pytest.raises(ValueError):
        # noinspection PyTypeChecker
        make_ieee_data_block("string")

    assert make_ieee_data_block(b"A" * 10) == b"#210" + b"A" * 10


@pytest.mark.parametrize("data, expect", [
    ("", ""),
    ("A", "A"),
    ("  1234\r\n", "1234"),
    ("-2.2 dBm ", "-2.2 dBm"),
    ("LIN\r\n", "LIN"),
    ("'LIN'\r\n", "LIN"),
])
def test_str_equals(data, expect):
    assert SCPIResponse(data) == expect
    assert not SCPIResponse(data) != expect
    assert hash(SCPIResponse(data)) == hash(expect)


@pytest.mark.parametrize("data, expect", [
    ('"LIN"\r\n', "LIN"),
    ("LINear", "LIN"),
])
def test_str_not_equals(data, expect):
    assert SCPIResponse(data) != expect
    assert not SCPIResponse(data) == expect
    assert hash(SCPIResponse(data)) != hash(expect)
