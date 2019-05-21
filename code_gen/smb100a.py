# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import division, print_function

from generate_class_defs import *
from nrp import NRPCmdListParser
from RSSscpi import smb100a

syntax_file = "SMB100A_syntax.txt"


class SMB100ACmdListParser(NRPCmdListParser):
    def _filter_cmd(self, cmd):
        if cmd[0].isalpha() and cmd[-1].isupper() or len(cmd) <= 3:
            return None
        cmd = re.sub(r"{\d\.\.\d}", "1", cmd)
        return cmd


class SMB100AWebhelp(ModernRohdeWebhelp):
    instrument_name = "SMB100A"
    _base_url = "http://www.rohde-schwarz.com/webhelp/smb100a_webhelp{0}"
    toc_file = "SMB100A_webhelp_toc.xml"
    cmd_list_file = "SMB100A_webhelp_command_list.htm"

    def parse_toc(self):
        super(SMB100AWebhelp, self).parse_toc()


class SMB100ATreePatcher(SystHelpTreePatcher):
    def __call__(self, cmd_tree):
        # type: (CmdNode) -> None
        # Remove all short, undocumented, commands from the command tree
        for cmd in list(cmd_tree.keys()):
            if cmd[0].isalpha() and cmd[-1].isupper() or len(cmd) <= 3:
                del cmd_tree[cmd]

        # The SYSTem.HELP.SYNTax.ALL command is not included in its own output.
        cmd_tree.add_cmd("SYSTem.HELP.SYNTax.ALL".split("."), arg=[], unit=[], query=True)

        # These are available both as *STB/@STB and &LLO/@LLO,
        # but one version will be masked due to class name restrictions
        del cmd_tree["&STB"]
        del cmd_tree["&LLO"]

        super(SMB100ATreePatcher, self).__call__(cmd_tree)


def upate_syntax_definition(smb):
    """
    Updates the command syntax definition file with data from a generator

    :param smb100a.SMB100A smb:
    """
    x = smb.SYSTem.HELP.SYNTax.ALL.q().block_data().decode(encoding="utf-8")
    info = smb.IDN.q().split_comma()
    with open(os.path.join(cmd_list_dir, syntax_file), "w", newline="\n", encoding="utf-8") as fd:
        fd.write("// Generated from %s, fw: %s\n" % (info[1], info[3]))
        fd.write(x.lstrip())


def generate(download_webhelp=False):
    generate_SCPI_class(SMB100ACmdListParser(syntax_file), "SMB100A_gen",
                        tree_patcher=SMB100ATreePatcher(),
                        webhelp=SMB100AWebhelp(download_webhelp=download_webhelp))


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    upate_syntax_definition(smb100a.connect_ethernet(smb100a.find_smb100a(max_devices=1)[0].ip_address))
    download = True
    generate(download)
