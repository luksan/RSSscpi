# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from RSSscpi import ZNB
import visa

rm = visa.ResourceManager()

znb_ip = "192.168.56.101"

visa_res = rm.open_resource('TCPIP::' + znb_ip + '::INSTR')

# VISA command logging
# Error checking / handling

znb = ZNB(visa_res)

znb.logger = open("t_check_visa_log.txt", "wb")
znb.init()

# Instrument setup
# Number of points
# Start and stop frequency
# Source power
# IF bandwidth

znb.RST.w()
znb.INITiate.CONTinuous.ALL().w("OFF")

ch_no = 1
ch = znb.get_channel(1)
ch.name = "SP_ch_1"
dia1 = znb.get_diagram(1)

sense = znb.SENSe(ch_no)

sense.FREQuency.STARt().w(100e6)
sense.FREQuency.STOP().w(3e9)

sense.SWEep.POINts().w(801)
znb.SOURce(ch_no).POWer.LEVel().w("0 dBm")


# Add traces
ch.active_trace.delete()  # remove the predefined trace
tr_s11 = ch.create_trace("S11", "S11", dia1)
tr_s21 = ch.create_trace("S21", "S21", dia1)
tr_s12 = ch.create_trace("S12", "S12", dia1)
tr_s22 = ch.create_trace("S22", "S22", dia1)

# Create a diagram with the T-check equation trace
dia2 = znb.get_diagram(2)
dia2.STATe().w("ON")
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
znb.INITiate.IMMediate.ALL.w()
znb.OPC.q()
