# -*- coding: utf-8 -*-
"""


@author: Lukas Sandström
"""
import RSSscpi

class CmdNode(dict):
    leaf = "_leaf"
    
    def __init__(self, is_countable=False):
        super(CmdNode, self).__init__()
        self.units = []
        self.args = []
        self.has_query = False # query command supported
        self.has_set = False # set command supported
        self.is_countable = is_countable # An integer can be appended to the node name

    def add_cmd(self, node_list, arg, unit, query):
        cmd = node_list.pop(0)
        is_countable = False
        if cmd[-1].isdigit():
            cmd = cmd[:-1]
            is_countable = True
        node = self.setdefault(cmd, CmdNode(is_countable))

        if len(node_list):
            return node.add_cmd(node_list, arg, unit, query)

        arg and arg not in node.args and node.args.append(arg)
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
                if not line or line[0] == '/':
                    continue
                self._add_cmd(*line.split())
            
    def _add_cmd(self, cmd, arg=None, unit=None):
        query = False
        if cmd[-1] == '?':
            query = True
            cmd = cmd[:-1]
        c = cmd.split(':')
        
        self.cmd_tree.add_cmd(c, arg, unit, query)

class ClassCodeGen(object):
    def __init__(self, class_name, cmd_tree, io_obj, source):
        self.cmd_tree = cmd_tree
        self._output = io_obj
        self._indent = 0
        self.class_name = class_name
        self.source = source
    
    def _preamble(self):
        import time
        self._out("# -*- coding: utf-8 -*-")
        self._out("# Generated from " + self.source + " on " + time.strftime("%Y-%m-%d %H:%M"))
        self._out("from SCPI_gen_support import Instrument, SCPINode, SCPINodeN, SCPIQuery, SCPISet")
        self._out("class "+ self.class_name + "(Instrument):")
        self._indent += 1
        
    def gen(self):
        self._preamble()
        self._gen(self.cmd_tree)
        self._out("# END OF FILE")

    def _out(self, str_):
        self._output.write(" "*(self._indent*4) + str_ + "\n")

    def _gen(self, cmd_tree):
        for cmd_str in sorted(cmd_tree):
            cmd = cmd_tree[cmd_str]

            base_class = "SCPINode"
            if cmd.is_countable:
                base_class = "SCPINodeN"
            if cmd.has_query:
                base_class += ", SCPIQuery"
            if cmd.has_set:
                base_class += ", SCPISet"

            name = cmd_str
            if name[0] == '*' or name[0] == '@':
                name = name[1:]            
            self._out("class " + name+"(" + base_class + "):")
            self._indent += 1
            #self._out('"""Docstring x http://www.google.se"""')
            self._out('_cmd = "' + cmd_str + '"')
            self._gen(cmd)
            self._indent -= 1

#import StringIO
#from pprint import pprint
if __name__ == '__main__':
    #filename = "ZNB_commands_2_56.inp" ; module_name = "ZNB_gen"
    filename = "ZVA_commands_3_60.inp" ; module_name = "ZVA_gen"

    parser = CmdListParser('../SCPI_cmd_lists/' + filename)
    #pprint(parser.cmd_tree['*OPC'])
    #fd = StringIO.StringIO()

    fd = open("../RSSscpi/gen/" + module_name + ".py", 'wb')
    g = ClassCodeGen(module_name, parser.cmd_tree, fd, source=filename)
    g.gen()
    fd.close()
    
    import importlib
    importlib.import_module("RSSscpi.gen." + module_name) # Test that the module can be loaded
    
    #print fd.getvalue()
    print "All good :)"
