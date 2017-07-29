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

import logging

module_dir = os.path.abspath(os.path.dirname(__file__))
cmd_list_dir = os.path.join(module_dir, "SCPI_cmd_lists")
output_dir = os.path.join(module_dir, '..', 'src', 'RSSscpi', 'gen')

download = False


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
    def get_help_url(self, cmd):
        """
        :param cmd: A SCPI command, ex. CALCULATE:MARKER, in the form of a string list with one element per node.
        :type cmd: list of str
        :return: A string URL for the relevant page in the online manual, or None if not found.
        :rtype: str or None
        """
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
    with open(path, 'wb') as fd:
        g = ClassCodeGen(module_name, parser.cmd_tree, fd, source=parser.filename, webhelp=webhelp)
        g.gen()

    import importlib
    sys.path.insert(0, output_dir)
    importlib.import_module("RSSscpi.gen." + module_name)  # Test that the module can be loaded
    sys.path.pop(0)

    logging.info("Generated %s", path)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    download = False

    import zva
    zva.generate()

    import znb
    znb.generate()

    import nrp
    nrp.generate()

    logging.info("All good :)")
