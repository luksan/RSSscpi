# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from .gen import ZVA_gen
from . import ZNB

import logging


class ZVA(ZVA_gen, ZNB):
    def __init__(self, visa_res):
        super(ZVA, self).__init__(visa_res=visa_res)
        self.logger = logging.getLogger(__name__)
        self.visa_logger = self.logger.getChild("VISA")

    #def init(self):
        # SYSTem:DATA:SIZE ALL | AUTO
