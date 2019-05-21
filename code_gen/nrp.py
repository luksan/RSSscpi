# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import division, print_function

from generate_class_defs import *

from RSSscpi import nrp

syntax_file = "NRPxxSN_syntax.txt"


class NRPCmdListParser(CmdListParser):
    def _add_cmd(self, cmd, arg=None):  # The NRP command list does not contain units
        has_query = cmd[-1] == '?' or cmd[-3:] == "[?]"
        has_write = cmd[-1] != '?'

        # GPIB explorer indicates an indexed node by appending "1" to the name
        cmd = str(cmd).translate(str.maketrans("", "", "[]")).rstrip("?").lstrip(":").replace("{1..*}", "1")

        cmd = self._filter_cmd(cmd)
        if cmd is None:
            return

        if has_query:
            self.cmd_tree.add_cmd(cmd.split(":"), arg, None, True)
        if has_write:
            self.cmd_tree.add_cmd(cmd.split(":"), arg, None, False)

    def _filter_cmd(self, cmd):
        """
        Return cmd, optionally modified, if the command should be included in the command tree.
        Return None if the command should be ignored.
        """
        return cmd


class NRPTreePatcher(SystHelpTreePatcher):
    def __init__(self):
        super(NRPTreePatcher, self).__init__()
        self.fixit[("CALibration:ZERO:AUTO", "args")] = ["ONCE"]
        self.fixit[("FETCh", "has_query")] = True
        self.fixit[("FORMat:DATA", "args")] = ["ASCii", "REAL"]
        self.fixit[("SENSe:RANGe", "args")] = ["0", "1", "2"]
        self.fixit[("SYSTem:HELP:HEADers", "args")] = []
        self.fixit[("SYSTem:PRESet", "args")] = []


def upate_syntax_definition(sensor):
    """
    Updates the command syntax definition file with data from the power sensor.

    :param nrp.NRPxxSN sensor:
    """
    x = sensor.SYSTem.HELP.SYNTax.ALL.q().block_data()
    info = sensor.query_system_info()
    with open(os.path.join(cmd_list_dir, syntax_file), "w", newline="\n", encoding="utf-8") as fd:
        fd.write("// Generated from %s, fw: %s\n" % (info["Type"], info["SW Build"]))
        fd.write(x.lstrip())


def generate(download_webhelp=False):
    generate_SCPI_class(NRPCmdListParser(syntax_file), "NRPxxSN_gen", tree_patcher=NRPTreePatcher())


if __name__ == "__main__":
    upate_syntax_definition(nrp.connect_ethernet(nrp.find_sensors(max_sensors=1)[0].ip_address))
    generate(False)
