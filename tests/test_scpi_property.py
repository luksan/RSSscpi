# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function

import math
import pytest
from .conftest import VISA  # noqa: F401

from RSSscpi.SCPI_property import SCPIProperty, SCPIPropertyMinMax, SCPIPropertyMapping, MinMaxFloat
from RSSscpi.gen import ZNB_gen
from RSSscpi.gen import ZVA_gen


class VNAProp(ZNB_gen):
    def __init__(self, *args, **kwargs):
        super(VNAProp, self).__init__(*args, **kwargs)
        self.cb_value = None

    def get_root(self):
        return self

    def cb(self, *args, **kwargs):
        assert "get" in kwargs
        last_cb = self.cb_value
        if not kwargs["get"]:
            assert "value" in kwargs
            v = kwargs["value"]
            self.cb_value = v
            if isinstance(v, dict):
                return v  # dict passed to Instrument.write()
        else:
            self.cb_value = None
            if isinstance(last_cb, dict):
                return last_cb

    _SWE = ZNB_gen.SENSe.SWEep
    str_prop = SCPIProperty(_SWE.TYPE, str)
    int_prop = SCPIPropertyMinMax(_SWE.POINts, int)
    float_prop = SCPIProperty(_SWE.TIME, float)
    float_minmax = SCPIPropertyMinMax(_SWE.DWELl, float)
    znb_only = SCPIPropertyMapping(_SWE.DWELl.IPOint, str, {"ALL": True, "FIRSt": False})
    map_prop = SCPIPropertyMapping(_SWE.GENeration, str, mapping={"ANALog": True, "STEPped": False})

    cb_prop = SCPIProperty(_SWE.TYPE, str, callback=cb, get_root_node=get_root)


class BadPropInheritance(ZVA_gen, VNAProp):
    pass


def test_inheritance(visa):
    znb = VNAProp(visa)
    znb.znb_only = True
    assert ["SENSe:SWEep:DWELl:IPOint ALL"] == visa.cmd
    zva = BadPropInheritance(visa)
    with pytest.raises(AttributeError):
        zva.znb_only = True
    assert [] == visa.cmd


def test_cb_prop(visa):
    """
    :param VISA visa:
    """
    vna = VNAProp(visa)
    vna.cb_prop = ""
    assert vna.cb_value == ""
    vna.cb_prop = "A"
    assert vna.cb_value == "A"
    x = vna.cb_prop
    assert x == "1"
    assert vna.cb_value is None
    vna.cb_prop = {"value": 123.4, "fmt": "{value:.2f}"}
    x = vna.cb_prop
    assert x == "1"
    assert ["SENSe:SWEep:TYPE",
            "SENSe:SWEep:TYPE A",
            "SENSe:SWEep:TYPE?",
            "SENSe:SWEep:TYPE 123.40",
            'SENSe:SWEep:TYPE? 123.40',
            ] == visa.cmd


def test_prop(visa):
    """
    :param VISA visa:
    """
    vna = VNAProp(visa)

    vna.str_prop = "abc123"
    x = vna.str_prop
    assert isinstance(x, str)
    assert ["SENSe:SWEep:TYPE abc123",
            "SENSe:SWEep:TYPE?",
            ] == visa.cmd

    vna.int_prop = 2
    vna.int_prop.value = 3
    x = vna.int_prop.value
    assert isinstance(x, int)
    vna.int_prop.query_max()
    vna.int_prop.query_min()
    vna.int_prop.query_default()
    vna.int_prop.set_max()
    vna.int_prop.set_min()
    vna.int_prop.set_default()
    assert ["SENSe:SWEep:POINts 2",
            "SENSe:SWEep:POINts 3",
            "SENSe:SWEep:POINts?",
            "SENSe:SWEep:POINts? MAX",
            "SENSe:SWEep:POINts? MIN",
            "SENSe:SWEep:POINts? DEF",
            "SENSe:SWEep:POINts MAX",
            "SENSe:SWEep:POINts MIN",
            "SENSe:SWEep:POINts DEF",
            ] == visa.cmd

    vna.map_prop = True
    vna.map_prop = False
    pytest.raises(KeyError, "vna.map_prop = 9")
    vna.map_prop = 0  # This works beacuse 0 and False hashes to same value
    pytest.raises(KeyError, 'vna.map_prop = "OFF"')
    pytest.raises(KeyError, 'vna.map_prop = "ON"')
    pytest.raises(KeyError, 'vna.map_prop = "oops"')
    pytest.raises(TypeError, 'vna.map_prop = [123, True, "asd"]')  # list() is not hashable, hence TypeError
    pytest.raises(KeyError, 'x = vna.map_prop')
    visa.ret = "ANALog"
    x = vna.map_prop
    assert x is True
    visa.ret = "STEPped"
    x = vna.map_prop
    assert x is False
    assert ["SENSe:SWEep:GENeration ANALog",
            "SENSe:SWEep:GENeration STEPped",
            "SENSe:SWEep:GENeration STEPped",
            "SENSe:SWEep:GENeration?",
            "SENSe:SWEep:GENeration?",
            "SENSe:SWEep:GENeration?",
            ] == visa.cmd


@pytest.mark.parametrize("ref", [-1e9, -1.23456789, -1, -1e-9, 0, 1e-9, 1, 1.23456789, 1e9])
def test_minmaxfloat(visa, ref):
    vna = VNAProp(visa)
    visa.ret = str(ref)
    f = vna.float_minmax
    assert [] == visa.cmd
    assert isinstance(f, MinMaxFloat)

    assert complex(f) == complex(ref)
    assert bool(f) == bool(ref)

    assert f.real == complex(ref).real
    assert f.imag == complex(ref).imag

    assert f == ref
    assert f >= ref
    assert f <= ref
    assert f < ref + 1
    assert f > ref - 1

    assert +f == +ref
    assert -f == -ref
    assert f + 1 == 1 + f
    assert -f - 1 == -1 - f
    assert f + 1 == ref + 1
    assert f - 1 == ref - 1
    assert f * 2 == ref * 2
    assert f / 2 == ref / 2
    assert f ** 2 == ref ** 2
    try:
        assert 2 ** f == 2 ** ref
    except OverflowError:
        pass

    assert abs(f) == abs(ref)
    assert round(f) == round(ref)
    assert math.trunc(f) == math.trunc(ref)
