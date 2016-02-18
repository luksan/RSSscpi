# -*- coding: utf-8 -*-
"""
Created on 16 feb. 2016

@author: Lukas Sandström
"""

from gen.ZNB_gen import ZNB_gen


class ZNB(ZNB_gen):
    def __init__(self, visa_res):
        super(ZNB, self).__init__(visa_res)

    def set_source_power_offset(self, channel=None, src=0, power=-300, relative=True):
        """
        :type relative: bool
        """
        if relative:
            x = 'CPAD'
        else:
            x = 'ONLY'
        self.SOURce(channel).POWer(src).LEVel.IMMediate.OFFSet().w(power, x)

    @property
    def active_channel(self):
        """
        Get the active channel, INSTrument:NSELect?
        :return: int
        """
        return int(self.INSTrument.NSELect().q())

    @active_channel.setter
    def active_channel(self, n):
        """
        Set the active channel, INSTrument:NSELect n
        :param n: (int, str)
        :return: None
        """
        self.INSTrument.NSELect().w(n)

if __name__ == '__main__':
    from RSSscpi.gen.SCPI_gen_support import DummyVisa
    znb = ZNB(DummyVisa("Visa1"))

    znb.ABORt.w()
