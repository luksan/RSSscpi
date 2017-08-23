# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import pytest
from .conftest import VISA  # noqa: F401

from RSSscpi.SCPI_response import format_SCPI_block_data, SCPIResponse  # noqa: F401


@pytest.mark.parametrize('expected, txt', [
    (True,  ("1", "ON", "on", "On")),
    (False, ("0", "OFF", "off", "Off")),
    (None,  ("OF", "O", "1.0", "0.0"))
    ])
def test_bool(expected, txt):
    for x in txt:
        if expected is None:
            assert pytest.raises(ValueError, "bool(SCPIResponse(x))")
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
    n = ",".join(s)
    assert SCPIResponse(n).comma_list_pairs() == list(zip(s[0::2], s[1::2]))


def test_split_comma():
    n = "'1, ASD, 2, K,3,t,4,f'"
    assert SCPIResponse(n).split_comma() == list(map(lambda x: x.strip(" '"), n.split(",")))
    n = ",".join(map(str, range(10)))
    assert SCPIResponse(n).split_comma(convert=int) == list(range(10))


def test_block_data():
    with pytest.raises(ValueError):
        SCPIResponse("1").block_data()
    assert SCPIResponse("#11A").block_data() == "A"
    assert SCPIResponse("#210" + "A" * 10).block_data() == "A" * 10

    assert format_SCPI_block_data("A"*10) == "#210" + "A" * 10


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
