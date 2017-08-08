# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import division, print_function

from generate_class_defs import *

from bs4 import BeautifulSoup
import re


class RohdeZNBWebhelp(ModernRohdeWebhelp):
    _base_url = "http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en{0}"
    toc_file = "ZNB_webhelp_toc.xml"
    cmd_list_file = "ZNB_webhelp_command_list.htm"

    def parse_toc(self):
        super(RohdeZNBWebhelp, self).parse_toc()

        common = self._toc_soup.find(title="Command Reference").find(title="Common Commands")["link"]
        self._common_commands = self._base_url.format(common)

        if_msg = self._toc_soup.find(title="VXI-11 Interface Messages")["link"]
        self._interface_messages = self._base_url.format(if_msg)


class ZNBTreePatcher(TreePatcher):
    def __init__(self):
        super(ZNBTreePatcher, self).__init__()

        self.fixit[("MMEMory:STORe:TRACe:PORTs", "args")] = \
            ["1", "'string'", "COMPlex", "LINPhase", "LOGPhase", "CIMPedance", "PIMPedance"]

        self.fixit[("SENSe:CORRection:COLLect:METHod:DEFine", "args")] = \
            ["1", "'string'", "ETOM", "ETSM", "FOPort1", "FOPort12", "FOPort2", "FOPTport", "FRTRans",
             "FTRans", "REFL1", "REFL12", "REFL2",
             "ROPTport", "RTRans", "TNA", "TOM", "TOSM", "TPORt", "TRL", "TRM", "TSM", "UOSM"]

        self.fixit[("SENSe:CORRection:CDATa", "args")] = ["1", "'string'"]


def generate():
    generate_SCPI_class(CmdListParser("ZNB_commands.inp"), "ZNB_gen", RohdeZNBWebhelp(download_webhelp=download),
                        tree_patcher=ZNBTreePatcher())

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    download = True
    generate()
