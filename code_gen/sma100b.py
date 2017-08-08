# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import division, print_function

from generate_class_defs import *
from nrp import NRPCmdListParser
from RSSscpi import sma100b

syntax_file = "SMA100B_syntax.txt"


class SMB100AWebhelp(ModernRohdeWebhelp):
    _base_url = "http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en{0}"
    toc_file = "SMA100B_webhelp_toc.xml"
    cmd_list_file = "SMA100B_webhelp_command_list.htm"

    def parse_toc(self):
        super(SMB100AWebhelp, self).parse_toc()


class SMA100BTreePatcher(SystHelpTreePatcher):
    pass


def upate_syntax_definition(sma):
    """
    Updates the command syntax definition file with data from the power sensor.

    :param sma100b.SMA100B sma:
    """
    x = sma.SYSTem.HELP.SYNTax.ALL.q().block_data()
    info = sma.IDN.q().split_comma()
    with open(os.path.join(cmd_list_dir, syntax_file), "wb") as fd:
        fd.write("// Generated from %s, fw: %s\n" % (info[1], info[3]))
        fd.write(x.lstrip())


def generate():
    generate_SCPI_class(NRPCmdListParser(syntax_file), "SMA100B_gen",
                        tree_patcher=SMA100BTreePatcher(),
                        webhelp=SMB100AWebhelp(download))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    upate_syntax_definition(sma100b.connect_ethernet(sma100b.find_sma100b(max_devices=1)[0].ip_address))
    download = True
    generate()
