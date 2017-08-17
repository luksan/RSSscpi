# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import RSSscpi.znb

import logging


class VISAFilter(logging.Filter):
    def filter(self, record):
        """
        :param logging.LogRecord record:
        :return: bool
        """
        if record.name.endswith(".VISA") and record.levelno <= logging.INFO:
            return False
        return True

# logging.basicConfig(level=logging.WARN, filename=__file__[:-3]+"_log.txt", filemode="w")
logging.basicConfig()
logger = logging.getLogger()
logger.handlers[0].addFilter(VISAFilter())  # don't print VISA INFO logging to the console

znb_ip = "192.168.56.101"

# VISA command logging
# Error checking / handling

znb = RSSscpi.znb.connect_ethernet(znb_ip)

znb.visa_logger.setLevel(logging.DEBUG)
znb.visa_logger.addHandler(logging.FileHandler(filename=__file__[:-3]+"_visa_log.txt", mode="wb"))
znb.init()

# Instrument setup
# Number of points
# Start and stop frequency
# Source power
# IF bandwidth

znb.RST.w()
znb.INITiate.CONTinuous.ALL().w("OFF")

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
ch.init_sweep()
znb.query_OPC()
