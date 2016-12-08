# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from SCPI_gen_support import SCPINodeBase, SCPIQuery, SCPISet


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
        return self._leaf_node.relink_to_ancestor(root)

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
