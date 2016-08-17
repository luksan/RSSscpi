# -*- coding: utf-8 -*-
"""


@author: Lukas Sandström
"""

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, HTTPError
    from urllib import urlretrieve

from bs4 import BeautifulSoup
import re


class CmdNode(dict):
    leaf = "_leaf"  # Constant indicating that the current node is a leaf node
    
    def __init__(self, is_countable=False):
        super(CmdNode, self).__init__()
        self.units = []
        self.args = []
        self.has_query = False  # query command supported
        self.has_set = False  # set command supported
        self.is_countable = is_countable  # An integer can be appended to the node name

    def add_cmd(self, node_list, arg, unit, query):
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
        with open(self.filename) as fd:
            for line in fd:
                if not line or line[0] == '/' or line.isspace():
                    continue
                try:
                    self._add_cmd(*line.split())
                except:
                    print "Error on line: '" + line + "'"
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


class RohdeZVAWebhelp(Webhelp):
    def __init__(self, download_webhelp=False):
        self._base_url = "http://www.rohde-schwarz.com/webhelp/webhelp_zva_{1}{0}"
        self._help_rev = 6

        self.cmd_list_file = "SCPI_cmd_lists/ZVA_help_index.htm"

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
            print "ZVA webhelp is at revision", rev, ", started search at rev", self._help_rev
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
            soup = BeautifulSoup(f)
        with open(self.cmd_list_file, "w") as f:
            f.write(soup.prettify())

        for u in soup("key"):
            # TODO: The second item in the list can contain "(deprecated)". Use this info?
            cmd = u['name'].split()[0].translate(None, '"\\')
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

        self._base_url = "http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_{1}{0}"
        self._help_rev = 7

        self.toc_file = "SCPI_cmd_lists/ZNB_webhelp_toc.xml"
        self.cmd_list_file = "SCPI_cmd_lists/ZNB_webhelp_command_list.htm"

        self._urls = dict()
        self._common_commands = None  # *CLS, *OPC, etc.
        self._interface_messages = None  # VXI-11 Interface messages, @LOC, @DCL, etc.

        if download_webhelp:
            self.download_cmd_list()
        self.load_urls()

    def download_cmd_list(self):
        for rev in range(self._help_rev, self._help_rev + 10):  # Search after newer revisions of the manual
            try:
                url = self._base_url.format("/Data/Toc.xml", rev)
                toc = urlopen(url)
            except HTTPError:
                continue
            print "ZNB webhelp is at revision", rev, ", started search at rev", self._help_rev
            self._help_rev = rev
            break
        else:
            raise RuntimeError("No valid ZNB web help URL found")

        toc = BeautifulSoup(toc)
        with open(self.toc_file, "w") as f:
            f.write(toc.prettify("utf-8"))

        cmd_list_url = toc.find(title="List of Commands")["link"]
        url = self._base_url.format(cmd_list_url, self._help_rev)
        urlretrieve(url, "SCPI_cmd_lists/ZNB_webhelp_command_list.htm")

        with open("SCPI_cmd_lists/ZNB_webhelp_rev.txt", "w") as u:
            u.write("%i" % self._help_rev)

    def load_urls(self):
        """
        Load help URLs from the SCPI command list.
        https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c0e6efab4c3f4280.htm
        :return:
        """
        toc_soup = BeautifulSoup(open(self.toc_file))

        common = toc_soup.find(title="Command Reference").find(title="Common Commands")["link"]
        self._common_commands = self._base_url.format(common, self._help_rev)

        if_msg = toc_soup.find(title="VXI-11 Interface Messages")["link"]
        self._interface_messages = self._base_url.format(if_msg, self._help_rev)

        cmd_soup = BeautifulSoup(open(self.cmd_list_file))
        d = cmd_soup.find("div", class_="block")
        for u in d("a"):
            cmd = u.string
            url = u['href']
            cmd_key = str(cmd).translate(None, "[]?")
            cmd_key = re.sub(r"([^:])<\w+?>", r"\1", cmd_key)
            self._urls[cmd_key] = (cmd, url)

    def get_help_url(self, cmd):
        if cmd[0][0] == "*":
            return self._common_commands
        if cmd[0][0] == "@":
            return self._interface_messages
        try:
            return self._base_url.format("/Content/" + self._urls[":".join(cmd)][1], self._help_rev)
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
        self._out("from SCPI_gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool")
        self._out("from . import Instrument")
        self._out("class " + self.class_name + "(Instrument):")
        self._indent += 1
        
    def gen(self):
        self._preamble()
        self._gen(self.cmd_tree, [])
        self._out("# END OF " + self.class_name)
        c1 = self._cmd_cnt
        c2 = self._cmd_help_cnt
        c3 = str(int(float(c2)/c1 * 100))
        print self.class_name + ":", c1, "commands,", c2, "have a help URL (" + c3 + "%)."

    def _out(self, str_):
        if not str_:
            self._output.write("\n")  # don't print lines with only indentation
        else:
            self._output.write(" "*(self._indent*4) + str_ + "\n")

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

            if "ON" in cmd.args:
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
            self._out('args = ["' + '", "'.join(cmd.args) + '"]')
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

def generate_SCPI_class(input_file, module_name, webhelp=Webhelp(), tree_patcher=None):
    """

    :param input_file: filename of the command list from GPIB Explorer
    :param module_name: Name of the module to be generated
    :param webhelp: Webhelp subclass instance, generating help URLs
    :param tree_patcher: Function used to fix errors in the command tree before the code generation
    :return: None
    """
    parser = CmdListParser('SCPI_cmd_lists/' + input_file)

    if tree_patcher:
        cmd_tree = tree_patcher(parser.cmd_tree)
    else:
        cmd_tree = parser.cmd_tree
    path = "RSSscpi/gen/" + module_name + ".py"
    with open(path, 'wb') as fd:
        g = ClassCodeGen(module_name, cmd_tree, fd, source=input_file, webhelp=webhelp)
        g.gen()

    import importlib
    importlib.import_module("RSSscpi.gen." + module_name)  # Test that the module can be loaded
    print "Generated " + path


if __name__ == '__main__':
    import os
    os.chdir("..")
    download = False
    generate_SCPI_class("ZVA_commands_3_70.inp", "ZVA_gen", RohdeZVAWebhelp(download_webhelp=download))
    generate_SCPI_class("ZNB_commands_2_70.inp", "ZNB_gen", RohdeZNBWebhelp(download_webhelp=download), tree_patcher=ZNBTreePatcher())
    print "All good :)"
