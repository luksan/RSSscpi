# -*- coding: utf-8 -*-
"""
This example shows how to configure the ZVA or ZNB for a per point triggered measurement.

@author: Lukas Sandström
"""
from __future__ import print_function

import RSSscpi.zva
import time

import logging
# logging.basicConfig(level=logging.WARN, filename=__file__[:-3]+"_log.txt", filemode="w")

#vna_ip = "10.188.178.48"
vna_ip = "192.168.56.101"


zva = RSSscpi.zva.connect_ethernet(vna_ip)
zva.visa_logger.setLevel(logging.DEBUG)
zva.visa_logger.addHandler(logging.FileHandler(filename=__file__[:-3] + "_visa_log.txt", mode="wb"))
zva.init()

##

sweep_points = 11
meas_bw = 10  # Hz
##

zva.preset()
zva.INITiate.CONTinuous.off()

ch1 = zva.get_channel(1)

ch1.sweep.points = sweep_points
ch1.SENSe.BANDwidth.w(meas_bw)

ch1.TRIGger.SEQuence.LINK.w("POINt")
ch1.TRIGger.SEQuence.SOURce.w("MAN")

ch1.init_sweep()

sweep_time = float(zva.SENSe.SWEep.TIME.q())
print("Total sweep time:", sweep_time, "seconds")

print("Starting sweep")
for n in range(sweep_points):
    zva.send_TRG()
    time.sleep(sweep_time/sweep_points)

print("Final OPC")
time.sleep(2)
print(zva.query_OPC())
