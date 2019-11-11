# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import inspect
import logging

import RSSscpi.zva
import RSSscpi.znb


class VISAFilter(logging.Filter):
    def filter(self, record):
        """
        :param logging.LogRecord record:
        :return: bool
        """
        if record.name.endswith(".VISA") and record.levelno <= logging.INFO:
            return False
        return True


def connect_zva(zva_ip):
    zva = RSSscpi.zva.connect_ethernet(zva_ip)
    logging_setup(zva)
    return zva


def connect_znb(znb_ip):
    znb = RSSscpi.znb.connect_ethernet(znb_ip)
    logging_setup(znb)
    return znb


def logging_setup(instrument):
    instrument.visa_logger.setLevel(logging.DEBUG)
    # Get the name of the top level script from the stack, use that to name the log file
    logfile = inspect.getmodule(inspect.stack()[-1][0]).__file__[:-3] + "_visa_log.txt"
    instrument.visa_logger.addHandler(logging.FileHandler(filename=logfile, mode="w"))
    logger = logging.getLogger()
    logger.handlers[0].addFilter(VISAFilter())  # don't print VISA INFO logging to the console
