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


class SCPINodeBase(object):
    _cmd = "SCPINodeBase"

    def __init__(self, parent=None):
        """
        :param parent: The command node level above this node.
        :type parent: SCPINodeBase or None
        """
        self._parent = parent

    def __str__(self):
        return self.__class__._cmd

    def __getattribute__(self, name):
        x = object.__getattribute__(self, name)
        if inspect.isclass(x) and issubclass(x, SCPINodeBase):
            # Automatic instantiation of SCPINodeBase class accesses
            return x(self)
        return x

    def build_cmd(self):
        x = self._build_cmd_r()
        return x[1:]  # remove leading colon

    def _build_cmd_r(self):
        if not self._parent:
            return str(self)
        return self._parent._build_cmd_r() + ":" + str(self)

    def _get_root(self):
        """
        :return: Returns the root node of the command tree, an Instrument.
        :rtype: Instrument
        """
        if not self._parent:
            return self
        return self._parent._get_root()


class SCPINode(SCPINodeBase):
    _cmd = "SCPINode"

    def __call__(self, *args):
        if len(args):
            raise TypeError(self.build_cmd() + "(XX) <- invalid index operation, command node does not support indexing.")
        return self


class Instrument(SCPINodeBase):
    _cmd = ""

    def __init__(self, visa_res):
        super(Instrument, self).__init__(None)
        self._visa_res = visa_res

    @staticmethod
    def _build_arg_str(args):
        return ", ".join([str(x) for x in args])

    def write(self, cmd, *args):
        """
        Send a string to the instrument, without reading a respone.\n
        :param cmd: The SCPI command
        :type cmd: SCPINodeBase
        :param args: Any number of arguments for the command, will be converted with str()
        :rtype: None
        """
        self._visa_res.write(cmd.build_cmd() + " " + self._build_arg_str(args))

    def opc(self, cmd, *args):
        """Send command followed by *OPC? query in the same command string.\n
        :param cmd: The SCPI command
        :type cmd: SCPINodeBase
        :param args: A list of arguments for the command, will be converted with str()
        :rtype: None
        """
        self._visa_res.query(cmd.build_cmd() + " " + self._build_arg_str(args) + ";*OPC?")

    def query(self, cmd, *args):
        """
        Execute a SCPI query.\n
        :param cmd: The SCPI command
        :type cmd: SCPINodeBase
        :param args: A list of arguments for the command, will be converted with str()
        :return: The response from the pyvisa query
        """
        # TODO: parse return values?
        # TODO: add function to read back result later
        return self._visa_res.query(cmd.build_cmd() + "? " + self._build_arg_str(args))

    def preset(self):
        self.RST.w()


class SCPINodeN(SCPINodeBase):
    _cmd = "SPCINodeN"

    def __init__(self, parent=None):
        super(SCPINodeN, self).__init__(parent)
        self.N = ""

    def __call__(self, N=None):
        """
        :param N: Integer index to be appended to the command node string.
        :return: *self*
        """
        if N is not None:
            N = str(N)
            if not N.isdigit():
                raise TypeError(self.build_cmd() + "(XX) <- Node index must be integer, or None.")
            self.N = N
        else:
            self.N = ""
        return self

    def __str__(self):
        return self.__class__._cmd + self.N


class SCPICmd(SCPINodeBase):
    pass


class SCPIQuery(SCPICmd):
    def q(self, *args):
        """
        Execeute a SCPI query.
        """
        return self._get_root().query(self, *args)


class SCPISet(SCPICmd):
    def w(self, *args):
        """
        Send a string to the VISA resorce, without reading the respone.
        :rtype: None
        """
        return self._get_root().write(self, *args)

    def opc(self, *args):
        """
        Send command followed by *OPC? query in the same command string
        """
        return self._get_root().opc(self, *args)
