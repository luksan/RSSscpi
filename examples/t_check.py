# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import logging
from connect_instrument import connect_znb

logging.basicConfig()

znb_ip = "localhost"
znb = connect_znb(znb_ip)

znb.preset()
znb.INITiate.CONTinuous.ALL.w("OFF")

ch = znb.get_channel(1)
ch.name = "SP_ch_1"
dia1 = znb.get_diagram(1)

ch.configure_freq_sweep(start_freq=100e6, stop_freq=3e9, points=801, power=0)

# Add traces
ch.active_trace.delete()  # remove the predefined trace
tr_s11 = ch.create_trace("S11", "S11", dia1)
tr_s21 = ch.create_trace("S21", "S21", dia1)
tr_s12 = ch.create_trace("S12", "S12", dia1)
tr_s22 = ch.create_trace("S22", "S22", dia1)

# Create a diagram with the T-check equation trace
dia2 = znb.get_diagram(2)
dia2.state = True
dia2.name = "Tcheck"
tr_Tcheck = ch.create_trace("T_check", "S11", dia2)
tr_Tcheck.math_equation = "linMag(S11*(Re(S21)-Im(S21)) + S12*(Re(S22)-Im(S22))) / ((1-linMag(S11)^2-linMag(S12)^2)*(1-linMag(S21)^2-linMag(S22)^2))^0.5"
tr_Tcheck.math_is_enabled = True
tr_Tcheck.trace_format = "REAL"
tr_Tcheck.scale_top = 1.25
tr_Tcheck.scale_bottom = 0.75
tr_Tcheck.ref_level = 1
tr_Tcheck.ref_pos = 50

# Add limit lines

# Make a measurement sweep
ch.init_sweep()
znb.query_OPC()
