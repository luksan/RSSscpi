# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from RSSscpi import ZNB

import Queue
import time, timeit

from RSSscpi.gen.SCPI_gen_support import DummyVisa
from RSSscpi import SocketInterface

import logging
# logging.basicConfig(level=logging.WARN, filename=__file__[:-3]+"_log.txt", filemode="w")
logging.basicConfig(level=logging.WARN)

import visa
rm = visa.ResourceManager()

#znb_ip = "10.188.178.47"
znb_ip = "192.168.56.101"
#znb_ip = "10.188.178.63"

visa_res = rm.open_resource('TCPIP::' + znb_ip + '::INSTR')
#visa_res = SocketInterface(znb_ip)
#visa_res = DummyVisa("hej")

# VISA command logging
# Error checking / handling

znb = ZNB(visa_res)

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

ch_no = 1
ch = znb.get_channel(1)
ch.name = "SP_ch_1"
dia1 = znb.get_diagram(1)

sense = znb.SENSe(ch_no)

sense.FREQuency.STARt().w(100e6)
sense.FREQuency.STOP().w(3e9)

sense.SWEep.POINts().w(10001)
znb.SOURce(ch_no).POWer.LEVel().w("0 dBm")


# Add traces
ch.active_trace.delete()  # remove the predefined trace
tr_s11 = ch.create_trace("S11", "S11", dia1)
tr_s21 = ch.create_trace("S21", "S21", dia1)
tr_s12 = ch.create_trace("S12", "S12", dia1)
tr_s22 = ch.create_trace("S22", "S22", dia1)


# Calibrate

#ch.cal_auto((1, 2))
ch.init_sweep()
znb.send_OPC()


def wait_for_event():
    for x in range(100):  # wait for at most 10 seconds for completion
        try:
            return znb.event_queue.get(timeout=0.1)
        except Queue.Empty:
            print ".",
            continue
    return None

print "Calibrating",
opc = wait_for_event()
print "done"
#print opc

# Make the measurement
ch.init_sweep()
znb.send_OPC()

print "Measuring",
wait_for_event()
print "done"

# Save the S-parameter data
print ch.save_touchstone("test.s2p", ports=(1,2))
# Final OPC before the program terminates
znb.query_OPC()
