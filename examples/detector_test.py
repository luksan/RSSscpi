# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
import logging

from RSSscpi import zva

# logging.basicConfig(level=logging.WARN, filename=__file__[:-3]+"_log.txt", filemode="w")

vna_ip = "10.188.178.82"
# vna_ip = "192.168.56.101"

instr = zva.connect_ethernet(vna_ip)
instr.visa_logger.setLevel(logging.DEBUG)
instr.visa_logger.addHandler(logging.FileHandler(filename=__file__[:-3] + "_visa_log.txt", mode="w"))
instr.init()

instr.preset()
instr.INITiate.CONTinuous.off()
instr.update_display(True)

dia1 = instr.get_diagram(1)
ch1 = instr.get_channel(1)

tr1 = ch1.get_trace("Trc1")
tr1.name = "SAM"
tr1.measurement = tr1.MeasParam.Wave("b", 1, src_port=1, detector="sam")

tr2 = ch1.create_trace("RMS", zva.Trace.MeasParam.Wave(receiver="b", dst_port=1, src_port=1, detector="rms"), dia1)
tr3 = ch1.create_trace("AVG", zva.Trace.MeasParam.Wave(receiver="b", dst_port=1, src_port=1, detector="avg"), dia1)

ch1.sweep.DETector.TIME.w(0.01)
ch1.get_vna_port(1).src_attenuator = 0
ch1.configure_power_sweep(freq=4e9, start_power=-40, stop_power=0, points=41, ifbw=1e6)

tr4 = tr1.copy("RMS_AVG")
tr4.assign_diagram(dia1)
tr4.math_equation = "RMS / AVG"
tr4.math_is_enabled = True

ch1.init_sweep()
instr.query_OPC()

tr4.autoscale()

print("OPC", instr.query_OPC())
