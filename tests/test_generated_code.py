# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import pytest

import inspect

from .conftest import VISA  # noqa: F401

from RSSscpi import ZNB
from RSSscpi.SCPI_gen_support import SCPINodeBase

from vna1 import VNA1
from vna2 import VNA2


def test_basic(dummy_vna, visa):
    """
    :param ZNB dummy_vna:
    :param VISA visa:
    """
    znb = dummy_vna

    assert inspect.isclass(znb.ABORt.__class__)
    assert inspect.isclass(ZNB.ABORt)
    assert isinstance(znb.ABORt, SCPINodeBase)

    znb.CALCulate.MARKer(3).FUNCtion().BWIDth.q("'asd'")
    znb.CALCulate.MARKer(3).FUNCtion().BWIDth.q("asd")

    znb.CALCulate.MARKer()
    z = znb.CALCulate(2).MARKer("3").FUNCtion.BWIDth

    z.MODE.w(123, 123, 123333)

    ass = znb.SENSe.CORRection.COLLect.AUTO.ASSignment
    ass(2).DEFine.w(5, 4, 3, 2, 1)
    ass(3).DEFine.w(5, 4, 3, 2, 1)
    x = [5, 4, 3]
    ass(1).DEFine.w(*x)
    znb.OPC.q()
    znb.query_OPC()

    z1 = znb.CALCulate(1)
    z = z1.MARKer(1)
    z.q()
    y = z1(2).MARKer(3)
    z.q()
    y.q()
    assert ["CALCulate:MARKer3:FUNCtion:BWIDth? 'asd'",
            "CALCulate:MARKer3:FUNCtion:BWIDth? asd",
            "CALCulate2:MARKer3:FUNCtion:BWIDth:MODE 123, 123, 123333",
            "SENSe:CORRection:COLLect:AUTO:ASSignment2:DEFine 5, 4, 3, 2, 1",
            "SENSe:CORRection:COLLect:AUTO:ASSignment3:DEFine 5, 4, 3, 2, 1",
            "SENSe:CORRection:COLLect:AUTO:ASSignment1:DEFine 5, 4, 3",
            "*OPC?",
            "*OPC?",
            "CALCulate1:MARKer1?",
            "CALCulate1:MARKer1?",
            "CALCulate2:MARKer3?"] == visa.cmd


def test_node_base(dummy_znb, visa):
    # type: (ZNB, VISA) -> None

    instr = dummy_znb

    # Verify that assignment to the SPCINodes is prevented
    assert hasattr(instr, "OPC")
    with pytest.raises(AttributeError):
        instr.OPC = ""

    # Check that Instrument has _SCPI_class set correctly
    assert instr._SCPI_class.__module__ == instr.OPC.__class__.__module__


def test_attributes(visa):
    v1 = VNA1(visa)
    v2 = VNA2(visa)

    assert v1.bsub._SCPI_class == VNA1.A.B
    assert v2.bsub._SCPI_class != v1.bsub._SCPI_class
    assert v2.A.__class__.__module__ == VNA2.__module__
    assert v2.A._SCPI_class == VNA2.A
    assert v2.bsub._SCPI_class == VNA2.A.B


def test_relink_to_ancestor(visa):
    instr = VNA2(visa)
    a = instr.A(2)
    d = VNA1.A.B.Ca.D.relink_to_ancestor(a)
    assert d.build_cmd() == "A2:B:Ca:D"

    aa = instr.Aa(1)
    with pytest.raises(AttributeError) as err:
        VNA1.A.B.Ca.D.relink_to_ancestor(aa)
    assert str(err).endswith("AttributeError: The given ancestor was not found in the command tree.")

    with pytest.raises(AttributeError) as err:
        VNA1.A.B.Cb.D.relink_to_ancestor(a)
    assert str(err).endswith("AttributeError: 'B' object has no attribute 'Cb' -- A2:B:Cb:D")

    with pytest.raises(AttributeError) as err:
        VNA1.A.B.Ca.D.E.relink_to_ancestor(d)
    assert str(err).endswith("AttributeError: 'D' object has no attribute 'E' -- A2:B:Ca:D:E")

    with pytest.raises(AttributeError) as err:
        VNA1.A.B.Cb.relink_to_ancestor(instr.bsub)
    assert str(err).endswith("AttributeError: Refusing access to a SCPINode from another module. "
                             "<class 'tests.vna2.B'> !-> <class 'tests.vna1.Cb'> -- A:B:Cb")
