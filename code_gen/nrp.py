# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import division, print_function

from generate_class_defs import *
import re


class NRPCmdListParser(CmdListParser):
    def _add_cmd(self, cmd):  # The NRP command list is copied from the PDF, so no arguments or units
        query_only = cmd[-1] == '?'
        if query_only:
            cmd = cmd[:-1]
        cmd = str(cmd).translate(None, "[]")
        cmd = re.sub(r'<.*?>', '1', cmd)  # GPIB explorer indicates an indexed node by appending "1" to the name
        self.cmd_tree.add_cmd(cmd.split(":"), None, None, True)
        if not query_only:
            self.cmd_tree.add_cmd(cmd.split(":"), 1, None, False)


def generate():
    generate_SCPI_class(NRPCmdListParser("NRPxxSN_rev07.txt"), "NRPxxSN_gen")

if __name__ == "__main__":
    generate()
