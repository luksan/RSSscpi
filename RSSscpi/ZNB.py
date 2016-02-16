# -*- coding: utf-8 -*-
'''
Created on 16 feb. 2016

@author: Lukas Sandström
'''

from gen.ZNB_gen import ZNB_gen

class ZNB(ZNB_gen):
    def __init__(self, visa_res):
        super(ZNB, self).__init__(visa_res)

if __name__ == '__main__':
    from RSSscpi.gen.SCPI_gen_support import DummyVisa
    x = ZNB(DummyVisa("Visa1"))
    
    x.ABORt.w()