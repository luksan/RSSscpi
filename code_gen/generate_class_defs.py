# -*- coding: utf-8 -*-
"""


@author: Lukas Sandström
"""

import os
import sys

try:
    # For Python 3.0 and later
    # noinspection PyCompatibility
    from urllib.request import urlopen, urlretrieve
    # noinspection PyCompatibility
    from urllib.error import HTTPError
except ImportError:
    # Fall back to Python 2's urllib2
    # noinspection PyCompatibility
    from urllib2 import urlopen, HTTPError
    from urllib import urlretrieve

from bs4 import BeautifulSoup
import re

import logging

_module_dir = os.path.abspath(os.path.dirname(__file__))
_cmd_list_dir = os.path.join(_module_dir, "SCPI_cmd_lists")
_output_dir = os.path.join(_module_dir, '..', 'src', 'RSSscpi', 'gen')


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
        with open(os.path.join(_cmd_list_dir, self.filename)) as fd:
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


class Webhelp(object):
    def get_help_url(self, cmd):
        """
        :param cmd: A SCPI command, ex. CALCULATE:MARKER, in the form of a string list with one element per node.
        :type cmd: list of str
        :return: A string URL for the relevant page in the online manual, or None if not found.
        :rtype: str or None
        """
        return None


class RohdeZVAWebhelp(Webhelp):
    def __init__(self, download_webhelp=False):
        self._base_url = "http://www.rohde-schwarz.com/webhelp/webhelp_zva_{1}{0}"
        self._help_rev = 8

        self.cmd_list_file = os.path.join(_cmd_list_dir, "ZVA_help_index.xml")

        if download_webhelp:
            self.download_cmd_list()

        self._urls = dict()
        self._common_commands = None
        self._interface_messages = None

        self.load_urls()

    def download_cmd_list(self):
        for rev in range(self._help_rev, self._help_rev + 10):  # Search after newer revisions of the manual
            try:
                url = self._base_url.format("/whxdata/whidata0_xml.js", rev)
                index = urlopen(url)
            except HTTPError:
                continue
            logging.info("ZVA webhelp is at revision %d, started search at rev %d.", rev, self._help_rev)
            self._help_rev = rev
            break
        else:
            raise RuntimeError("No valid ZVA web help URL found")

        with open(self.cmd_list_file, "w") as cmd_list:
            data_cnt = 1
            while True:
                x = index.read()
                cmd_list.write(x[x.find('"')+1:x.rfind('"')])
                try:
                    index = urlopen(self._base_url.format("/whxdata/whidata%i_xml.js" % data_cnt, self._help_rev))
                except HTTPError:
                    break
                data_cnt += 1

    def load_urls(self):
        """
        Load help URLs from the Index page of the online manual, saved locally.
        :return:
        """
        self._common_commands = self._base_url.format("/scpi_reference/common_commands.htm", self._help_rev)
        self._interface_messages = self._base_url.format(
            "/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages", self._help_rev)

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
            return self._base_url.format(self._urls[":".join(cmd)][1], self._help_rev)
        except KeyError:
            return None


class RohdeZNBWebhelp(Webhelp):
    def __init__(self, download_webhelp=False):

        self._base_url = "http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en{0}"

        self.toc_file = os.path.join(_cmd_list_dir, "ZNB_webhelp_toc.xml")
        self.cmd_list_file = os.path.join(_cmd_list_dir, "ZNB_webhelp_command_list.htm")

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
        self._out("from RSSscpi.SCPI_gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool")
        self._out("from RSSscpi.Instrument import Instrument")
        self._out("")
        self._out("")
        self._out("class " + self.class_name + "(Instrument):")
        self._indent += 1
        
    def gen(self):
        self._preamble()
        self._gen(self.cmd_tree, [])
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
            if name[0] == '*' or name[0] == '@':
                name = name[1:]            
            self._out("class " + name + "(" + base_class + "):")
            self._indent += 1
            self._make_docstr(cmd, parents + [cmd_str])
            self._out('_cmd = "' + cmd_str + '"')
            if cmd.args:
                self._out('args = ["' + '", "'.join(cmd.args) + '"]')
            else:
                self._out('args = []')  # Don't emit the empty string if we don't have any arguments
            self._out("")
            self._gen(cmd, parents + [cmd_str])
            self._indent -= 1
            # Uncomment below to generate attributes
            self._out(name + " = " + name + "()")
            self._make_docstr(cmd, parents + [cmd_str])
            self._out("")


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


def generate_SCPI_class(parser, module_name, webhelp=Webhelp(), tree_patcher=None):
    """

    :param CmdListParser parser: A CmdListParser instance
    :param module_name: Name of the module to be generated
    :param webhelp: Webhelp subclass instance, generating help URLs
    :param tree_patcher: Function used to fix errors in the command tree before the code generation
    :return: None
    """

    if tree_patcher:
        cmd_tree = tree_patcher(parser.cmd_tree)
    else:
        cmd_tree = parser.cmd_tree
    path = os.path.join(_output_dir, module_name + ".py")
    with open(path, 'wb') as fd:
        g = ClassCodeGen(module_name, cmd_tree, fd, source=parser.filename, webhelp=webhelp)
        g.gen()

    import importlib
    sys.path.insert(0, _output_dir)
    importlib.import_module("RSSscpi.gen." + module_name)  # Test that the module can be loaded
    sys.path.pop(0)

    logging.info("Generated %s", path)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    download = False

    generate_SCPI_class(CmdListParser("ZVA_commands_3_70.inp"), "ZVA_gen", RohdeZVAWebhelp(download_webhelp=download))
    generate_SCPI_class(CmdListParser("ZNB_commands_2_70.inp"), "ZNB_gen", RohdeZNBWebhelp(download_webhelp=download),
                        tree_patcher=ZNBTreePatcher())
    generate_SCPI_class(NRPCmdListParser("NRPxxSN_rev07.txt"), "NRPxxSN_gen")

    logging.info("All good :)")
