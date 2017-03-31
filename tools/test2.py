# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:57:01 2016

@author: Lukas Sandström
"""

from RSSscpi.gen.ZNB_gen import ZNB_gen
from RSSscpi.gen.SCPI_gen_support import DummyVisa, SCPINodeBase
from RSSscpi import ZNB
import inspect

znb = ZNB(DummyVisa("K1"))


def test():
    print "*  test()"
    znb.CALCulate.MARKer(3).FUNCtion().BWIDth.q("asd")

    znb.CALCulate.MARKer()
    z = znb.CALCulate(2).MARKer("3").FUNCtion.BWIDth

    z.MODE.w(123, 123,123333)

    ass = znb.SENSe.CORRection.COLLect.AUTO.ASSignment
    ass(2).DEFine.w(5,4,3,2,1)
    ass(3).DEFine.w(5,4,3,2,1)
    x = [5,4,3]
    ass(1).DEFine.w(*x)
    znb.OPC.q()
    znb.query_OPC()

    z1 = znb.CALCulate(1)
    z = z1.MARKer(1)
    z.q()
    y = z1(2).MARKer(3)
    z.q()
    y.q()


def test2():
    assert inspect.isclass(znb.ABORt.__class__)
    assert isinstance(znb.ABORt, SCPINodeBase)

def test_marker():
    print "*  test_marker()"
    ch = znb.get_channel(1)
    tr = ch.get_trace("Tr1")
    m1 = tr.get_marker(1)
    x = m1.tracking
    m1.tracking = False
    m1.is_enabled = True
    m1.is_enabled = "OFF"
    m1.y
    try:
        m1.y = 2
    except AttributeError as a:
        print a

def test_trace():
    print "*  test_trace()"
    ch = znb.get_channel(2)
    tr = ch.get_trace("Tr2")
    x = tr.trace_format
    tr.trace_format = 2


def test_channel():
    print "*  test_channel()"
    ch = znb.get_channel(3)
    ch.sweep.points.query_default()
    ch.sweep.points.value = 301
    ch.sweep.points = 301
    ch.sweep.TYPE.w("LIN")
    ch.configure_freq_sweep(10, 10e6, points=101, ifbw=1e3, power=-10, log_sweep=True)


def test_diagram():
    print "*  test_diagram()"
    dia = znb.get_diagram(1)
    dia.save_screenshot("hej.png")

def test_sweep():
    pass

test_channel()
test_trace()
test_marker()
test_diagram()

test2()
test()
