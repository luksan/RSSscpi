# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:30:33 2016

@author: Lukas Sandström
"""

import inspect

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


class SCPINodeBase(object):
    _cmd = "SCPINodeBase"

    def __init__(self, parent=None):
        """
        :param parent: The command node level above this node.
        :type parent: SCPINodeBase or None
        """
        self._parent = parent

    def __str__(self):
        return self._cmd

    # def __get__(self, instance, owner):
    #     if not instance:
    #         return self
    #     return self.__class__(parent=instance)

    def __getattribute__(self, name):
        x = object.__getattribute__(self, name)
        if inspect.isclass(x) and issubclass(x, SCPINodeBase) and name == x.__name__:
            # Automatic instantiation of SCPINodeBase class accesses
            return x(parent=self)
        return x

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
        :rtype: RSSscpi.gen.Instrument
        """
        if not self._parent:
            return self
        return self._parent._get_root()


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


class SCPIResponse(object):
    """
    Class used for containing and parsing responses from SCPI queries.
    """
    def __init__(self, res):
        self.raw = res

    def __nonzero__(self):
        """
        Converts the instrument response to a boolean value

        :return: bool
        """
        return str(self) in ["1", "ON"]

    def __str__(self):
        x = self.raw.replace("\r", "\n")
        return x.strip().strip("'")

    def __int__(self):
        return int(str(self))

    def comma_list_pairs(self):
        """
        Split the comma separated response into a list of tuples,
        with each tuple containing two consecutive response elements.

        :return: [ (str1, str2), ..]
        """
        x = self.split_comma()
        return zip(x[0::2], x[1::2])

    def split_comma(self):
        """
        Split the response into a list, separated by commas.
        Each list element is stripped of leading and trailing whitespace.

        :return: a string list
        :rtype: list of str
        """
        return [x.strip() for x in self.raw.split(",")]

    def block_data(self):
        """
        Interpret the response as a SCPI block data transfer

        :return: the data from the block transfer
        """
        return SCPIBlockData.parse(self.raw)


class SCPIBlockData(object):
    def __init__(self, data=None):
        self.data = data

    @staticmethod
    def parse(blk):
        if blk[0] != "#":
            print "WARN: invalid block data header"
        n = int(blk[1])  # The number of digits in the data length specifier
        l = int(blk[2:n + 2])  # data length
        return blk[n + 2:l + n + 2]

    @staticmethod
    def format(data):
        l = str(len(data))
        return "#" + str(len(l)) + l + data

    def __str__(self):
        return self.format(self.data)


class SCPICmd(SCPINodeBase):
    pass


class SCPIQuery(SCPICmd):
    def q(self, *args, **kwargs):
        """
        Execeute a SCPI query.
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


class SCPIProperty(object):
    """
    Getter/setter class for turning SCPINodes to class properties
    """
    def __init__(self, nodes, callback=None, get_root_node=None, docstr=None):
        """

        :param nodes: A list of strings representing the nodes under the root node
        :type nodes: list of str
        :param callback: A function called before each write and query
        :param get_root_node: A function returning a SCPINodeBase, the root of nodes
        :param docstr: The property doctring
        """
        self._nodes = nodes
        self._callback = callback
        self._get_root_node = get_root_node  # Function which returns a SCPINodeBase instance
        if docstr:
            self.__doc__ = docstr

    def _leaf(self, x):
        for n in self._nodes:
            x = getattr(x, n)
        return x

    def _get_leaf(self, instance):
        return self._leaf(self._get_root_node(instance)) if self._get_root_node else self._leaf(instance)

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        leaf = self._get_leaf(instance)
        if not hasattr(leaf, "q"):
            raise AttributeError("SCPI node doesn't support query")
        if self._callback:
            self._callback(self=instance, get=True)
        return leaf.q()

    def __set__(self, instance, value):
        leaf = self._get_leaf(instance)
        if not hasattr(leaf, "w"):
            raise AttributeError("SCPI node doesn't support write")
        if self._callback:
            self._callback(self=instance, get=False)
        leaf.w(value)


class MinMax(object):
    def __init__(self, instance, leaf, callback):
        self._instance = instance
        self._leaf = leaf
        self._cb = callback

    def _q(self, *args):
        if self._cb:
            self._cb(self=self._instance, get=True)
        self._leaf.q(*args)

    def _w(self, *args):
        if self._cb:
            self._cb(self=self._instance, get=False)
        self._leaf.w(*args)

    @property
    def value(self):
        return self._q()

    @value.setter
    def value(self, value):
        self._w(value)

    def query_min(self):
        return self._q("MIN")

    def set_min(self):
        self._w("MIN")

    def query_max(self):
        return self._q("MAX")

    def set_max(self):
        self._w("MAX")

    def query_default(self):
        return self._q("DEF")

    def set_default(self):
        self._w("DEF")


class SCPIPropertyMinMax(SCPIProperty):
    def __init__(self, *args, **kwargs):
        """
        :rtype: MinMax
        """
        super(SCPIPropertyMinMax, self).__init__(*args, **kwargs)

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return MinMax(instance, self._get_leaf(instance), self._callback)
