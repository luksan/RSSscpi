# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:30:33 2016

@author: Lukas Sandström
"""

import inspect

class DummyVisa(object):
    def __init__(self, name):
        self.name = name
    def query(self, q):
        print "Visa query,", self.name, q
        return "1 A"
        
    def write(self, w):
        print "Visa write,", self.name, w
        
        
class SCPINode(object):
    _cmd = "SPCINode"
    def __init__(self, parent):
        self._parent = parent
    
    def __str__(self):
        return type(self)._cmd
        
    def __getattribute__(self, name):
        x = object.__getattribute__(self, name)
        if inspect.isclass(x) and issubclass(x, SCPINode):
            # Automatic instantiation of SCPINode class accesses
            return x(self)
        return x
    
    def __call__(self, *args):
        if len(args):
            raise TypeError(self.build_cmd() + "(XX) <- invalid index operation, command node does not support indexing.")
        return self
    
    def build_cmd(self):
        x = self._build_cmd_r()
        return x[1:] # remove leading colon

    def _build_cmd_r(self):
        if not self._parent:
            return str(self)
        return self._parent._build_cmd_r() + ":" + str(self)

    def _get_root(self):
        if not self._parent:
            return self
        return self._parent._get_root()

    def _get_visa_res(self):
        return self._get_root()._visa_res
        
class Instrument(SCPINode):
    _cmd = ""
    def __init__(self, visa_res):
        self._parent = None
        self._visa_res = visa_res
    
    def preset(self):
        self.RST.w()

class SCPINodeN(SCPINode):
    _cmd = "SPCINodeN"
    def __init__(self, parent):
        super(SCPINodeN, self).__init__(parent)
        self.N = ""
    
    def __call__(self, N = None):
        if not N is None:
            N = str(N)
            if not N.isdigit():
                raise TypeError(self.build_cmd() + "(XX) <- Node index must be integer, or None.")
            self.N = N
        else:
            self.N = ""
        return self

    def __str__(self):
        return type(self)._cmd + self.N

class SCPICmd(object):
    def _build_arg_str(self, args):
        return ", ".join([str(x) for x in args])

class SCPIQuery(SCPICmd):
    # TODO: parse return values?
    # TODO: add function to read back result later
    def q(self, *args):
        v = self._get_visa_res()
        return v.query(self.build_cmd() + "? " + self._build_arg_str(args))
    
class SCPISet(SCPICmd):
    def w(self, *args):
        v = self._get_visa_res()
        v.write(self.build_cmd() + " " + self._build_arg_str(args))

    def opc(self, *args):
        """Send command followed by *OPC? query in the same command string"""
        v = self._get_visa_res()
        v.query(self.build_cmd() + " " + self._build_arg_str(args) + ";*OPC?")