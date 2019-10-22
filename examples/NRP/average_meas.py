# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from RSSscpi import nrp

import csv
import tkinter
from tkinter import messagebox
import logging
import numpy
import time
from RSSscpi.Instrument import Queue


def wait_on_queue_progress_bar(queue, expected_duration, tick_interval=1):
    max_tick = 200  # limited by the console width
    prog_len = int(expected_duration / tick_interval)
    if prog_len > max_tick:
        tick_interval = expected_duration / max_tick
        prog_len = max_tick
    dots = 0
    time_start = time.time()

    while True:
        try:
            queue.get(timeout=tick_interval)
            break
        except Queue.Empty:
            dots += 1
            if dots > prog_len:
                prog_len = dots
            elapsed = time.time() - time_start
            print("\r|" + ("." * dots) + (" " * (prog_len - dots)) + "|  elapsed time: %.1f seconds" % elapsed, end="")
    print("\r|" + "."*prog_len + "| elapsed time: %.2f seconds" % (time.time() - time_start))


class VISAFilter(logging.Filter):
    def filter(self, record):
        """
        :param logging.LogRecord record:
        :return: bool
        """
        if record.name.endswith(".VISA") and record.levelno <= logging.INFO:
            return False
        return True


def zero_cal():
    ok = messagebox.askyesno("Zero power sensor", "Perform zero level adjust? (Disconnect sensor from the signal source)")
    if ok:
        sensor.cal_zero()
        sensor.send_OPC()
        print("Zeroing sensor. Please wait.")
        wait_on_queue_progress_bar(sensor.event_queue, 6)
        messagebox.showinfo("Zero power sensor", "Zero cal complete. Reconnect the power sensor to the signal source.")


def init_sensor(frequency):
    sensor.preset()
    sensor.query_OPC()

    if ask_zero_cal:
        zero_cal()

    # sensor.UNIT.POWer.w("DBM")
    sensor.UNIT.POWer.w("W")
    sensor.frequency = frequency
    sensor.init_cont = "OFF"


def prepare_avg_meas(buffer_size, avg_aperture, avg_count):
    sensor.ABORt.w()  # Stop any active measurement

    sensor.SENSe.RANGe.AUTO.w("OFF")
    sensor.SENSe.RANGe.w(0)  # Select the lowest measurement range

    sensor.SENSe.POWer.AVG.BUFFer.CLEar.w()
    sensor.SENSe.POWer.AVG.APERture.w(avg_aperture)  # Set the measurement aperture time

    sensor.SENSe.AVERage.COUNt.AUTO.w("OFF")  # Disable automatic averaging
    sensor.SENSe.AVERage.COUNt.w(avg_count)
    sensor.SENSe.AVERage.RESet.w()

    sensor.SENSe.POWer.AVG.BUFFer.SIZE.w(buffer_size)  # Set the measurement buffer size, and auto triggering
    sensor.SENSe.POWer.AVG.BUFFer.STATe.w("ON")
    sensor.TRIGger.COUNt.w(buffer_size)


def dBm(x):
    # return x
    return 10*numpy.log10(x) + 30


def main():
    init_sensor(frequency=20e9)

    data = []
    avg_count = 64
    buffer_size = 10
    target_duraton = 40
    avg_aperture = 20e-3
    # for avg_aperture in numpy.linspace(20e-3, 0.05, num=4):
    # for avg_count in numpy.logspace(0, 3, 4):
    for n in range(1):
        avg_count = max([int(target_duraton / (avg_aperture * 2)), 1])

        prepare_avg_meas(buffer_size, avg_aperture, avg_count)

        expected_duration = (avg_aperture * avg_count * buffer_size * 2)
        print("Expected meas duration: %g seconds" % expected_duration)

        sensor.init_immediate()
        sensor.send_OPC()
        wait_on_queue_progress_bar(sensor.event_queue, expected_duration, 1)

        result = sensor.fetch_numpy()
        data.append((avg_aperture, avg_count, dBm(result.mean()), dBm(numpy.median(result)), dBm(result.max()), dBm(result.min()), result.ptp(), result.std()))
        print("Avg aperture: {:g} s, Avg count {:g}, Mean: {:g} dBm, Median: {:g} dBm, max: {:g} dBm, min: {:g} dBm, peak-to-peak: {:g} W, std dev: {:g} W".format(*data[-1]))

    with open("avg_data.csv", "wb") as fd:
        csv_writer = csv.writer(fd)
        csv_writer.writerow(["Aperture", "Average count", "Mean", "Max", "Min", "Peak-to-peak", "Std. dev."])
        csv_writer.writerows(data)

ask_zero_cal = True

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()

    sensor = nrp.connect_ethernet(nrp.find_sensors(max_sensors=1)[0].ip_address)
    sensor.visa_logger.setLevel(logging.DEBUG)
    sensor.visa_logger.addHandler(logging.FileHandler(filename=__file__[:-3] + "_visa_log.txt", mode="wb"))
    logger.handlers[0].addFilter(VISAFilter())  # don't print VISA INFO logging to the console

    tkRoot = tkinter.Tk()
    tkRoot.withdraw()
    main()
    print("All good.")
