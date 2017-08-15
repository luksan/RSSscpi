# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import pytest

import inspect

from .conftest import VISA  # noqa: F401

from RSSscpi import ZNB
from RSSscpi.SCPI_gen_support import SCPINodeBase


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

    # Verify that assignment to the SPCINodes is prevented
    assert hasattr(dummy_znb, "OPC")
    with pytest.raises(AttributeError):
        dummy_znb.OPC = ""
