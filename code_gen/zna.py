# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from generate_class_defs import *


class RohdeZNAWebhelp(ModernRohdeWebhelp):
    instrument_name = "ZNA"
    toc_file = "ZNA_webhelp_toc.xml"
    cmd_list_file = "ZNA_webhelp_command_list.htm"
    _base_url = "https://www.rohde-schwarz.com/webhelp/ZNA_HTML_UserManual_en{0}"

    def parse_toc(self):
        super().parse_toc()

        common = self._toc_soup.find(title="Command Reference").find(title="Common Commands")["link"]
        self._common_commands = self._base_url.format(common)

        if_msg = self._toc_soup.find(title="VXI-11 Interface Messages")["link"]
        self._interface_messages = self._base_url.format(if_msg)


def generate(download_webhelp=False):
    generate_SCPI_class(CmdListParser("ZNA_commands.inp"), "ZNA_gen",
                        RohdeZNAWebhelp(download_webhelp=download_webhelp))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    download = True
    generate(download)
