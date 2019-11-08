# -*- coding: utf-8 -*-
"""


@author: Lukas Sandström
"""

from typing import Optional

import os
import sys

from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError

import logging
from bs4 import BeautifulSoup
import re

module_dir = os.path.abspath(os.path.dirname(__file__))
cmd_list_dir = os.path.join(module_dir, "SCPI_cmd_lists")
output_dir = os.path.join(module_dir, '..', 'src', 'RSSscpi', 'gen')


class CmdNode(dict):
    """
    CmdNode instances are used to represent the SCPI command tree.
    """
    def __init__(self, is_countable=False):
        super(CmdNode, self).__init__()
        self.units = []
        self.args = []
        self.has_query = False  # query command supported
        self.has_set = False  # set command supported
        self.is_countable = is_countable  # An integer can be appended to the node name

    def add_cmd(self, node_list, arg, unit, query):
        """

        :param node_list: A list of strings, from "SENSE1:CAL...".split(":")
        :type node_list: list of str
        :param arg:
        :param unit:
        :param bool query: True if this is the query form of the command
        :rtype: None
        """
        cmd = node_list.pop(0)
        is_countable = False
        if cmd[-1].isdigit():
            cmd = cmd[:-1]
            is_countable = True
        node = self.setdefault(cmd, CmdNode(is_countable))

        if len(node_list):
            return node.add_cmd(node_list, arg, unit, query)

        if arg and arg not in node.args:
            node.args.append(str(arg))
        unit and node.units.append(unit)
        node.has_query |= query
        node.has_set |= not query
   

class CmdListParser(object):
    """Parses a command set file obtained from RS GPIB Explorer (ICEWIN32)"""
    def __init__(self, filename):
        self.filename = filename   
        self.cmd_tree = CmdNode()
        self._parse()

    def _parse(self):
        with open(os.path.join(cmd_list_dir, self.filename)) as fd:
            for line in fd:
                if not line or line[0] == '/' or line.isspace():
                    continue
                try:
                    self._add_cmd(*line.split())
                except:
                    logging.exception("Error on line: '%s'", line)
                    raise
            
    def _add_cmd(self, cmd, arg=None, unit=None):
        query = False
        if cmd[-1] == '?':
            query = True
            cmd = cmd[:-1]

        c = cmd.split(':')
        self.cmd_tree.add_cmd(c, arg, unit, query)


class Webhelp(object):
    instrument_name = None  # type: str

    def get_help_url(self, cmd) -> Optional[str]:
        """
        :param cmd: A SCPI command, ex. CALCULATE:MARKER, in the form of a string list with one element per node.
        :type cmd: list of str
        :return: A string URL for the relevant page in the online manual, or None if not found.
        :rtype: str or None
        """
        return None

    def find_online_manual(self):
        """
        This function attempts to find the URL for the landing page of the
        online version of the user manual for the instrument specified by the
        instrument_name attribute.

        :return: An URL or None
        """
        search_url = "http://www.rohde-schwarz.com/manual/%s/" % self.instrument_name
        try:
            bs = BeautifulSoup(urlopen(search_url), "html.parser")
        except HTTPError:
            logging.error("Failed to open manual search URL %s" % search_url)
            return None

        tag = bs.find("a", class_="file_link", href=re.compile(r"webhelp.*%s.*\.html?$" % self.instrument_name, re.IGNORECASE))
        if tag:
            logging.debug("Found user manual for %s: %s" % (self.instrument_name, tag["href"]))
            return tag["href"]
        logging.debug("No user manual for %s found" % self.instrument_name)

    def find_base_url(self):
        """
        Returns the part to the left of the last / in the URL for the online manual.
        Links in the manual are relative to this base URL.

        :return: Base URL string or None.
        """
        url = self.find_online_manual()
        if url:
            return url.rpartition("/")[0]
        else:
            logging.warning("Couldn't find online user manual for instrument %s" % self.instrument_name)


class ModernRohdeWebhelp(Webhelp):
    _base_url = None  # type: str
    """The root of the online help URLs, without trailing slash.

    example: http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en{0}
    """

    toc_file = None  # type: str
    """The filename for caching the table of contents."""

    cmd_list_file = None  # type: str
    """The filename for caching the command list."""

    def __init__(self, download_webhelp=False):
        self.toc_file = os.path.join(cmd_list_dir, self.toc_file)
        self.cmd_list_file = os.path.join(cmd_list_dir, self.cmd_list_file)

        self._urls = dict()
        self._common_commands = None  # *CLS, *OPC, etc.
        self._interface_messages = None  # VXI-11 Interface messages, @LOC, @DCL, etc.

        if download_webhelp:
            base_url = self.find_base_url()
            if base_url:
                self._base_url = base_url + "{0}"
            self.download_cmd_list()

        self._toc_soup = None
        self._cmd_list_soup = None

        self.parse_toc()
        self.parse_cmd_list()

    def download_cmd_list(self):
        toc_url = self._base_url.format("/Data/Toc.xml")
        try:
            toc = BeautifulSoup(urlopen(toc_url), "html.parser")
        except HTTPError:
            logging.error("Download of TOC from %s failed." % toc_url)
            return
        with open(self.toc_file, "w", encoding="utf-8") as f:
            f.write(toc.prettify())
        logging.debug("TOC downloaded from %s" % toc_url)

        cmd_list_rel_url = toc.find(title="List of Commands")["link"]
        cmd_list_url = self._base_url.format(cmd_list_rel_url)
        try:
            cmd_list = BeautifulSoup(urlopen(cmd_list_url), "html.parser")
        except HTTPError:
            logging.error("Download of command list from %s failed." % cmd_list_url)
            return
        with open(self.cmd_list_file, "w", encoding="utf-8") as f:
            f.write(cmd_list.prettify())
        logging.debug("Command list downloaded from %s" % cmd_list_url)

    def parse_toc(self):
        """
        Load help URLs from the SCPI command list.
        """
        self._toc_soup = BeautifulSoup(open(self.toc_file), "html.parser")

    def parse_cmd_list(self):
        self._cmd_list_soup = BeautifulSoup(open(self.cmd_list_file), "html.parser")
        d = self._cmd_list_soup.find("div", class_="block")
        for u in d("a"):
            cmd = u.string.strip()
            url = u['href']
            cmd_key = str(cmd).translate(str.maketrans("", "", "[]?"))  # Remove all brackets and question marks
            cmd_key = re.sub(r"([^:])<\w+?>", r"\1", cmd_key)  # Convert "SENSE<Ch>" to "SENSE"
            cmd_key = cmd_key.lstrip(":")  # Remove leading colon from key
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


class TreePatcher(object):
    def __init__(self):
        self.fixit = dict()

    def __call__(self, cmd_tree):
        for cmd, prop in self.fixit.keys():
            x = cmd_tree
            for c in cmd.split(":"):
                x = x[c]
            setattr(x, prop, self.fixit[(cmd, prop)])

        return cmd_tree


class SystHelpTreePatcher(TreePatcher):
    def fix_args(self, cmd_tree):
        for node_name in cmd_tree:
            self.fix_args(cmd_tree[node_name])

            args = cmd_tree[node_name].args
            if not args:
                continue
            if not len(args) == 1:
                logging.error("More than one element in args %s, %s", node_name, args)
            arg = args[0]
            # :TRIGger:HYSTeresis[?] <numeric_value>[dB|PCT]
            u = arg.rfind("[")
            if u != -1:
                cmd_tree[node_name].units = arg[u+1:-1].split("|")
                arg = arg[:u]

            if arg == "<numeric_value>" or arg == "<integer>":
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
        super(SystHelpTreePatcher, self).__call__(cmd_tree)


class ClassCodeGen(object):
    """
    Generates a Python module with a SCPI command class structure for the instrument.
    """
    def __init__(self, class_name, cmd_tree, io_obj, source, webhelp=Webhelp()):
        """

        :param class_name: The name of the Python module to be generated.
        :param cmd_tree: A SCPI command tree structure, obtained from a CmdListParser.
        :type cmd_tree: CmdNode
        :param io_obj: An IO object to output the module to.
        :param source: String comment indicating the source file of the SCPI command structure.
        """
        self.cmd_tree = cmd_tree
        self._output = io_obj
        self._indent = 0
        self.class_name = class_name
        self.source = source
        self.hlp = webhelp

        self._cmd_cnt = 0
        self._cmd_help_cnt = 0
    
    def _preamble(self):
        import time
        self._out("# -*- coding: utf-8 -*-")
        self._out("# Generated from " + self.source + " on " + time.strftime("%Y-%m-%d %H:%M"))
        self._out("from typing import List\n")
        self._out("from ..scpi.gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool")
        self._out("")
        self._out("")
        self._out("class " + self.class_name + "(SCPINode):")
        self._indent += 1
        self._out("_cmd = \"\"")
        self._indent -= 1
        self._out("")

    def gen(self):
        self._preamble()
        self._indent += 1
        self._gen(self.cmd_tree, [])
        self._indent -= 1
        self._out("\n%s._SCPI_class = %s" % (self.class_name, self.class_name))
        self._out("# END OF " + self.class_name)
        c1 = self._cmd_cnt
        c2 = self._cmd_help_cnt
        logging.info("%s: %d commands, %d have a help URL (%i%%).", self.class_name, c1, c2, 100*float(c2)/c1)

    def _out(self, str_):
        o = " "*(self._indent*4) + str_
        self._output.write(o.rstrip() + "\n")

    def _make_docstr(self, cmd, cmd_str_list):
        """
        Creates the docstring for the generated SCPI node

        :param cmd: The CmdNode being processed
        :type cmd: CmdNode
        :param cmd_str_list: A list of strings making up the SCPI command
        :type cmd_str_list: list of str
        :rtype: None
        """
        self._cmd_cnt += 1
        self._out('"""')
        cmd_str = ":".join(cmd_str_list)
        url = self.hlp.get_help_url(cmd_str_list)
        if url is not None:
            self._out("`"+cmd_str)
            self._out("<" + url + ">`_")
            self._cmd_help_cnt += 1
        else:
            self._out(cmd_str)
        self._out("")
        self._out("Arguments: " + ", ".join(cmd.args))
        self._out('"""')

    def _gen(self, cmd_tree, parents):
        """
        Generates the class definitions for the command tree.

        :param cmd_tree:
        :type cmd_tree: CmdNode
        :param parents:
        :type parents: list of str
        """
        for cmd_str in sorted(cmd_tree):
            cmd = cmd_tree[cmd_str]

            base_class = "SCPINodeN" if cmd.is_countable else "SCPINode"

            if {"ON", "OFF"}.issubset(cmd.args):
                base_class += ", SCPIBool"
            else:
                if cmd.has_query:
                    base_class += ", SCPIQuery"
                if cmd.has_set:
                    base_class += ", SCPISet"

            name = cmd_str
            if name[0] == '*' or name[0] == '@' or name[0] == '&':
                name = name[1:]
            self._out("class " + name + "(" + base_class + "):")
            self._indent += 1
            self._make_docstr(cmd, parents + [cmd_str])
            self._out("__slots__ = ()")
            self._out('_cmd = "' + cmd_str + '"')
            if cmd.args:
                self._out('args = ["' + '", "'.join(cmd.args) + '"]')
            else:
                self._out('args = []  # type: List[str]')  # Don't emit the empty string if we don't have any arguments
            self._out("")
            self._gen(cmd, parents + [cmd_str])
            self._indent -= 1
            # Uncomment below to generate attributes
            self._out(name + " = " + name + "()  # type: ignore")
            self._make_docstr(cmd, parents + [cmd_str])
            self._out("")


def generate_SCPI_class(parser, module_name, webhelp=Webhelp(), tree_patcher=None):
    """

    :param CmdListParser parser: A CmdListParser instance
    :param module_name: Name of the module to be generated
    :param webhelp: Webhelp subclass instance, generating help URLs
    :param tree_patcher: Function used to fix errors in the command tree before the code generation
    :return: None
    """

    if tree_patcher:
        tree_patcher(parser.cmd_tree)

    path = os.path.join(output_dir, module_name + ".py")
    with open(path, 'w', encoding='utf-8', newline='\n') as fd:
        g = ClassCodeGen(module_name, parser.cmd_tree, fd, source=parser.filename, webhelp=webhelp)
        g.gen()

    import importlib
    sys.path.insert(0, output_dir)
    importlib.import_module("RSSscpi.gen." + module_name)  # Test that the module can be loaded
    sys.path.pop(0)

    logging.info("Generated %s", path)

def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    download = False

    import zva
    zva.generate(download)

    import zna
    zna.generate(download)

    import znb
    znb.generate(download)

    import nrp
    nrp.generate(download)

    import sma100b
    sma100b.generate(download)

    import smb100a
    smb100a.generate(download)

    logging.info("All good :)")


if __name__ == '__main__':
    main()
