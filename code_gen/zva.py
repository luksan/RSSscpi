# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import division, print_function

from generate_class_defs import *

from bs4 import BeautifulSoup
import re


class RohdeZVAWebhelp(Webhelp):
    def __init__(self, download_webhelp=False):
        self._base_url = "http://www.rohde-schwarz.com/webhelp/webhelp_zva{0}"

        self.cmd_list_file = os.path.join(cmd_list_dir, "ZVA_help_index.xml")

        if download_webhelp:
            self.download_cmd_list()

        self._urls = dict()
        self._common_commands = None
        self._interface_messages = None

        self.load_urls()

    def download_cmd_list(self):
        with open(self.cmd_list_file, "w") as cmd_list:
            data_cnt = 0
            while True:
                try:
                    index = urlopen(self._base_url.format("/whxdata/whidata%i_xml.js" % data_cnt))
                except HTTPError:
                    break
                x = index.read()
                cmd_list.write(x[x.find('"') + 1:x.rfind('"')])
                data_cnt += 1
            logging.debug("Downloaded help index from %s",
                          self._base_url.format("/whxdata/whidata%i_xml.js" % (data_cnt - 1)))

    def load_urls(self):
        """
        Load help URLs from the Index page of the online manual, saved locally.
        :return:
        """
        self._common_commands = self._base_url.format("/scpi_reference/common_commands.htm")
        self._interface_messages = self._base_url.format(
            "/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages")

        with open(self.cmd_list_file) as f:
            soup = BeautifulSoup(f, "html.parser")
        with open(self.cmd_list_file, "w") as f:
            f.write(soup.prettify())

        for u in soup("key"):
            # TODO: The second item in the list can contain "(deprecated)". Use this info?
            cmd = str(u['name'].split()[0]).translate(None, '"\\')  # Remove " and \ from the command
            if not cmd[0:3].isupper():
                continue  # All SCPI commands start with at least three capital letters
            cmd_key = str(cmd).translate(None, '[]?')
            cmd_key = re.sub(r"([^:])<\w+?>", r"\1", cmd_key)
            url = "/" + u.topic['url'][2:-2]
            self._urls[cmd_key] = (cmd, url)

    def get_help_url(self, cmd):
        if cmd[0][0] == "*":
            return self._common_commands
        if cmd[0][0] == "@":
            return self._interface_messages
        try:
            return self._base_url.format(self._urls[":".join(cmd)][1])
        except KeyError:
            return None


def generate():
    generate_SCPI_class(CmdListParser("ZVA_commands_3_70.inp"), "ZVA_gen", RohdeZVAWebhelp(download_webhelp=download))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    download = True
    generate()
