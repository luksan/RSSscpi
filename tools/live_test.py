# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:57:01 2016

@author: SANDSTRO
"""

import visa
rm = visa.ResourceManager()

from RSSscpi.gen.ZVA_gen import ZVA_gen
#zva_res = rm.open_resource('TCPIP::10.188.179.15::INSTR')
#x = ZVA_gen(zva_res)

from RSSscpi.gen.ZNB_gen import ZNB_gen
znb_res = rm.open_resource('TCPIP::10.188.179.12::INSTR')
x = ZNB_gen(znb_res)


print x.IDN.q()
x.OPC.q()

znb_res.close()