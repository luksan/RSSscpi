# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:57:01 2016

@author: SANDSTRO
"""

import visa
rm = visa.ResourceManager()
from RSSscpi import SocketInterface

znb_ip = "10.188.178.47"

#from RSSscpi.gen.ZVA_gen import ZVA_gen
#zva_res = rm.open_resource('TCPIP::10.188.179.15::INSTR')
#x = ZVA_gen(zva_res)

from RSSscpi import ZNB

#znb_res = rm.open_resource('TCPIP::10.188.178.47::INSTR')
znb_res = SocketInterface(znb_ip)

znb = ZNB(znb_res)
znb.init()

print znb.IDN.q()
znb.OPC.q()

cwd = znb.filesystem.getcwd()
#print cwd
d = znb.filesystem.listdir()

#f = znb.filesystem.file("touch.s1p")
#f.get(".")
#f.put("touch.s1p")

#dia = znb.get_diagram(2)
#scr = dia.save_screenshot("scr.png")
scr = znb.save_screenshot("scr.png")
scr.get(".")


znb_res.close()
