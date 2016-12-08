# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:30:33 2016

@author: Lukas Sandström
"""

import inspect
from SCPI_response import SCPIResponse

# TODO
# Implement the cmd structure with properties returning a Cmd object
# znb.SENSe -> SENSe(znb)
# class ZNB_gen(object):
#   SENSe = SCPICmdProp_SENSe("SENSe")
# class SCPICmdProp_SENSe(object):
#    FREQuency = SCPICmdProp_SENSe_FREQuency("FREQuency")


class DummyVisa(object):

    def __init__(self, name):
        self.name = name

    def query(self, q):
        print "Visa query,", self.name, q
        return "1 A"

    def write(self, w):
        print "Visa write,", self.name, w

    def install_handler(*args):
        print "Install handler not implemented"

    def enable_event(*args):
        print "Not implemented"


class SCPINodeBase(object):
    _cmd = "SCPINodeBase"
    _parent_class = None  # The class of the parent of the command node
    _SCPI_class = None  # Identifies the original class type in cases of subclassing

    def __init__(self, parent=None):
        """
        :param parent: The command node level above this node.
        :type parent: SCPINodeBase or None
        """
        self._parent = parent

    def __str__(self):
        return self._cmd

    def __get__(self, instance, owner):
        # type: (SCPINodeBase, SCPINodeBase) -> SCPINodeBase
        # Since the class definitions are nested we have to resolve the parent at runtime
        if self._SCPI_class is None:
            self.__class__._SCPI_class = self.__class__
            self.__class__._parent_class = owner._SCPI_class  # TODO: introspection to check for subclassing?
        if not instance:
            return self.__class__
        return self.__class__(parent=instance)

    # def __getattribute__(self, name):
    #     x = object.__getattribute__(self, name)
    #     if inspect.isclass(x) and issubclass(x, SCPINodeBase) and name == x.__name__:
    #         # Automatic instantiation of SCPINodeBase class accesses
    #         return x(parent=self)
    #     return x

    def build_cmd(self):
        x = self._build_cmd_r()
        return x[1:]  # remove leading colon

    def _build_cmd_r(self):
        if not self._parent:
            return self._cmd
        return self._parent._build_cmd_r() + ":" + self._cmd

    def _get_root(self):
        """
        :return: Returns the root node of the command tree, an Instrument.
        :rtype: RSSscpi.gen.Instrument.Instrument
        """
        if not self._parent:
            return self
        return self._parent._get_root()

    @classmethod
    def relink_to_ancestor(cls, ancestor):
        """
        Create a new instance with the parent chain linking to ancestor.

        :param ancestor: The SCPINodeBase instance to link to
        :type ancestor: SCPINodeBase
        :rtype: SCPINodeBase
        """
        assert isinstance(ancestor, SCPINodeBase)
        x = [cls]
        while not issubclass(ancestor._SCPI_class, x[-1]._parent_class):
            x.append(x[-1]._parent_class)
        leaf = ancestor
        for c in reversed(x):
            leaf = c(parent=leaf)
        return leaf  # Return the instantiated leaf node, properly linked to the root node


class SCPINode(SCPINodeBase):
    _cmd = "SCPINode"

    def __call__(self, *args):
        if len(args):
            raise TypeError(self.build_cmd() + "(XX) <- invalid index operation, SCPI node does not support indexing.")
        return self


class SCPINodeN(SCPINodeBase):
    _cmd = "SPCINodeN"

    def __init__(self, parent=None):
        super(SCPINodeN, self).__init__(parent=parent)
        self._n = None

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, n):
        if n is not None:
            n = str(n)
            if not n.isdigit():
                raise ValueError(self.build_cmd() + "(%s) <- Node index must be integer, or None." % n)
            self._n = int(n)
            self._cmd = self.__class__._cmd + str(n)
        else:
            self._n = None
            self._cmd = self.__class__._cmd

    def __call__(self, n=None):
        """
        Returns a copy of self, with the node index set to n.
        :param n: Integer index to be appended to the command node string.
        :return: *self*
        """
        cpy = self.__class__(parent=self._parent)
        cpy.n = n
        return cpy


class SCPICmd(SCPINodeBase):
    pass


class SCPIQuery(SCPICmd):
    def q(self, *args, **kwargs):
        """
        Execeute a SCPI query.

        :returns: a SCPIResponse instance
        :rtype: SCPIResponse
        """
        return self._get_root().query(self, *args, **kwargs)


class SCPISet(SCPICmd):
    def w(self, *args, **kwargs):
        """
        Send a string to the VISA resource, without reading the response.

        :rtype: None
        """
        return self._get_root().write(self, *args, **kwargs)


class SCPIBool(SCPIQuery, SCPISet):
    @staticmethod
    def _mk_arg(x):
        return "OFF" if not x or x == "0" or str(x).upper() == "OFF" else "ON"

    def w(self, x):
        super(SCPIBool, self).w(self._mk_arg(x))

