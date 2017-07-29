# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import division, print_function

from generate_class_defs import *

from bs4 import BeautifulSoup
import re


class RohdeZNBWebhelp(Webhelp):
    def __init__(self, download_webhelp=False):

        self._base_url = "http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en{0}"

        self.toc_file = os.path.join(cmd_list_dir, "ZNB_webhelp_toc.xml")
        self.cmd_list_file = os.path.join(cmd_list_dir, "ZNB_webhelp_command_list.htm")

        self._urls = dict()
        self._common_commands = None  # *CLS, *OPC, etc.
        self._interface_messages = None  # VXI-11 Interface messages, @LOC, @DCL, etc.

        if download_webhelp:
            self.download_cmd_list()
        self.load_urls()

    def download_cmd_list(self):
        toc_url = self._base_url.format("/Data/Toc.xml")
        toc = BeautifulSoup(urlopen(toc_url), "html.parser")
        with open(self.toc_file, "w") as f:
            f.write(toc.prettify("utf-8"))

        cmd_list_url = toc.find(title="List of Commands")["link"]
        cmd_list = BeautifulSoup(urlopen(self._base_url.format(cmd_list_url)), "html.parser")
        with open(self.cmd_list_file, "w") as f:
            f.write(cmd_list.prettify("utf-8"))

        logging.info("ZNB commandlist downloaded.")

    def load_urls(self):
        """
        Load help URLs from the SCPI command list.
        """
        toc_soup = BeautifulSoup(open(self.toc_file), "html.parser")

        common = toc_soup.find(title="Command Reference").find(title="Common Commands")["link"]
        self._common_commands = self._base_url.format(common)

        if_msg = toc_soup.find(title="VXI-11 Interface Messages")["link"]
        self._interface_messages = self._base_url.format(if_msg)

        cmd_soup = BeautifulSoup(open(self.cmd_list_file), "html.parser")
        d = cmd_soup.find("div", class_="block")
        for u in d("a"):
            cmd = u.string.strip()
            url = u['href']
            cmd_key = str(cmd).translate(None, "[]?")  # Remove all brackets and question marks
            cmd_key = re.sub(r"([^:])<\w+?>", r"\1", cmd_key)  # Convert "SENSE<Ch>" to "SENSE"
            self._urls[cmd_key] = (cmd, url)

    def get_help_url(self, cmd):
        if cmd[0][0] == "*":
            return self._common_commands
        if cmd[0][0] == "@":
            return self._interface_messages
        try:
            return self._base_url.format("/Content/" + self._urls[":".join(cmd)][1])
        except KeyError:
            return None


class ZNBTreePatcher(object):
    def __init__(self):
        self.fixit = dict()

        self.fixit[("MMEMory:STORe:TRACe:PORTs", "args")] = \
            ["1", "'string'", "COMPlex", "LINPhase", "LOGPhase", "CIMPedance", "PIMPedance"]

        self.fixit[("SENSe:CORRection:COLLect:METHod:DEFine", "args")] = \
            ["1", "'string'", "ETOM", "ETSM", "FOPort1", "FOPort12", "FOPort2", "FOPTport", "FRTRans",
             "FTRans", "REFL1", "REFL12", "REFL2",
             "ROPTport", "RTRans", "TNA", "TOM", "TOSM", "TPORt", "TRL", "TRM", "TSM", "UOSM"]

        self.fixit[("SENSe:CORRection:CDATa", "args")] = ["1", "'string'"]

    def __call__(self, cmd_tree):
        for cmd, prop in self.fixit.keys():
            x = cmd_tree
            for c in cmd.split(":"):
                x = x[c]
            setattr(x, prop, self.fixit[(cmd, prop)])

        return cmd_tree


def generate():
    generate_SCPI_class(CmdListParser("ZNB_commands_2_70.inp"), "ZNB_gen", RohdeZNBWebhelp(download_webhelp=download),
                        tree_patcher=ZNBTreePatcher())

if __name__ == "__main__":
    generate()
