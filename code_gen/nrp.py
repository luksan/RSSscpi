# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import division, print_function

from generate_class_defs import *
import re


class NRPCmdListParser(CmdListParser):
    def _add_cmd(self, cmd, arg=None):  # The NRP command list does not contain units
        has_query = cmd[-1] == '?' or cmd[-3:] == "[?]"
        has_write = cmd[-1] != '?'

        # GPIB explorer indicates an indexed node by appending "1" to the name
        cmd = str(cmd).translate(None, "[]").rstrip("?").lstrip(":").replace("{1..*}", "1")

        if has_query:
            self.cmd_tree.add_cmd(cmd.split(":"), arg, None, True)
        if has_write:
            self.cmd_tree.add_cmd(cmd.split(":"), arg, None, False)


class NRPTreePatcher(object):
    def __init__(self):
        self.fixit = dict()

        self.fixit[("CALibration:ZERO:AUTO", "args")] = ["ONCE"]
        self.fixit[("FETCh", "has_query")] = True
        self.fixit[("FORMat:DATA", "args")] = ["ASCii", "REAL"]
        self.fixit[("SENSe:RANGe", "args")] = ["0", "1", "2"]
        self.fixit[("SYSTem:HELP:HEADers", "args")] = []
        self.fixit[("SYSTem:PRESet", "args")] = []

    def fix_args(self, cmd_tree):
        for node_name in cmd_tree:
            self.fix_args(cmd_tree[node_name])

            args = cmd_tree[node_name].args
            if not args:
                continue
            assert len(args) == 1
            arg = args[0]
            # :TRIGger:HYSTeresis[?] <numeric_value>[dB|PCT]
            u = arg.rfind("[")
            if u != -1:
                cmd_tree[node_name].units = arg[u+1:-1].split("|")
                arg = arg[:u]

            if arg == "<numeric_value>":
                args[:] = ["1"]
            elif arg == "<boolean>":
                args[:] = ["1", "ON", "OFF"]
            elif arg == "<block_data>":
                pass  # TODO: this is useful, maybe do something similar for ZNB/ZVA
            elif arg == "<string>":
                args[:] = ["'string'"]
            else:
                args[:] = arg.split("|")

    def __call__(self, cmd_tree):
        self.fix_args(cmd_tree)

        for cmd, prop in self.fixit.keys():
            x = cmd_tree
            for c in cmd.split(":"):
                x = x[c]
            setattr(x, prop, self.fixit[(cmd, prop)])


def generate():
    generate_SCPI_class(NRPCmdListParser("NRPxxSN_syntax.txt"), "NRPxxSN_gen", tree_patcher=NRPTreePatcher())

if __name__ == "__main__":
    generate()
