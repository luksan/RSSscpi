# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:57:01 2016

@author: Lukas Sandström
"""

from RSSscpi.gen.ZNB_gen import ZNB_gen
from RSSscpi.gen.SCPI_gen_support import DummyVisa

def test():
    znb = ZNB_gen(DummyVisa("K1"))
    
    znb.CALCulate.MARKer(3).FUNCtion().BWIDth.q("asd")
    
    znb.CALCulate.MARKer()
    z = znb.CALCulate(2).MARKer("3").FUNCtion.BWIDth
    
    z.MODE.opc(123, 123,123333)

    ass = znb.SENSe.CORRection.COLLect.AUTO.ASSignment
    ass(2).DEFine.w(5,4,3,2,1)
    ass(3).DEFine.w(5,4,3,2,1)
    x = [5,4,3]
    ass(1).DEFine.w(*x)
    znb.OPC.q()

    z1 = znb.CALCulate(1)
    z = z1.MARKer(1)
    z.q()
    y = z1(2).MARKer(3)
    z.q()
    y.q()

test()
