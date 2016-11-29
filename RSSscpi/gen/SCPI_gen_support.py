# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:30:33 2016

@author: Lukas Sandström
"""

import inspect
from SCPIResponse import SCPIResponse

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


class SCPIProperty(object):
    """
    Getter/setter class for turning SCPINodes to class properties
    """
    def __init__(self, node, conv, callback=None, get_root_node=lambda x: x, docstr=None):
        """

        :param SCPINodeBase node: A __class__ derived from SCPINodeBase, which q() and w() will be invoked on an instance of.
        :param conv: A function which converts a SCPIResponse object to the desired type of the property.
        :param callback: A function called before each write and query, if the return is not None it will be passed as the argument to q()/w()
        :param get_root_node: A function returning a SCPINodeBase instance, nodes between root and <node> will be instantiated an linked to root
        :type get_root_node: (T, ) -> SCPINodeBase
        :param str docstr: The property doctring
        """
        self._leaf_node = node
        self._conv = conv
        self._callback = callback  # type: (*args, **kwargs) -> T
        self._get_root_node = get_root_node  # type: (T, ) -> SCPINodeBase
        if docstr:  # FIXME: remove the argument and assign self.__doc__ =  node.__doc__ unconditionally
            self.__doc__ = docstr

    def _get_leaf(self, instance):
        # type: (T) -> SCPINodeBase
        root = self._get_root_node(instance)  # type: SCPINodeBase
        x = [self._leaf_node]
        while not issubclass(root.__class__, x[-1]._parent_class):
            x.append(x[-1]._parent_class)
        for c in reversed(x):
            root = c(parent=root)
        return root  # Return the instantiated leaf node, properly linked to the root node

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        leaf = self._get_leaf(instance)  # type: SCPIQuery
        if not hasattr(leaf, "q"):
            raise AttributeError("SCPI node doesn't support query")
        args = ""  # FIXME: the callback argument mangling needs improvement
        if self._callback:
            cb = self._callback(self=instance, get=True)
            if cb is not None:
                args = cb
        return self._conv(leaf.q(args))

    def __set__(self, instance, value):
        leaf = self._get_leaf(instance)  # type: SCPISet
        if not hasattr(leaf, "w"):
            raise AttributeError("SCPI node doesn't support write")
        if self._callback:
            cb = self._callback(self=instance, get=False, value=value)
            if cb is not None:
                value = cb
        leaf.w(value)


class SCPIPropertyMapping(SCPIProperty):
    """
    A property which maps SCPI responses to different values. Can be used to create a boolean property
    from a SCPI command which returns two diffrent strings.
    """
    def __init__(self, node, conv, mapping, rev_mapping=None, *args, **kwargs):
        """
        Also see SCPIProperty

        :param node: The SCPI node which will be set/queried
        :param conv:
        :param mapping: A dict mapping SCPI responses to property values. The SCPIResponse object will be passed to conv before being used as dict index.
        :param rev_mapping: The reverse mapping, used for setting the property. Generated automatically if not provided.
        :param args: Parameters for SCPIProperty
        :param kwargs: Parameters for SCPIProperty
        """
        super(SCPIPropertyMapping, self).__init__(node, conv, *args, **kwargs)
        self._map = mapping
        self._rev_map = rev_mapping
        if rev_mapping is None:
            self._rev_map = {v: k for k, v in self._map.items()}

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        x = super(SCPIPropertyMapping, self).__get__(instance, owner)
        return self._map[self._conv(x)]

    def __set__(self, instance, value):
        v = self._rev_map[value]
        super(SCPIPropertyMapping, self).__set__(instance, v)


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
