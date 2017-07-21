# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from .SCPI_gen_support import SCPINodeBase, SCPIQuery, SCPISet
import functools
import numbers
import math


class SCPIProperty(object):
    """
    Getter/setter class for turning SCPINodes to class properties
    """
    def __init__(self, node, conv, callback=None, get_root_node=lambda x: x, docstr=None):
        """

        :param SCPINodeBase node: A __class__ derived from SCPINodeBase, which q() and w() will be invoked on an instance of.
        :param conv: A function which converts a SCPIResponse object to the desired type of the property.
        :param callback: A function called before each write and query, returning either a dict or None. The dict will be used as parameters for write()/query()
        :param get_root_node: A function returning a SCPINodeBase instance, called with instance as only parameter. Nodes between root and <node> will be instantiated an linked to root
        :type get_root_node: (T, ) -> SCPINodeBase
        :param str docstr: The property doctring
        """
        self._leaf_node = node
        self._conv = conv
        self._callback = callback  # type: (*args, **kwargs) -> T
        self._get_root_node = get_root_node  # type: (T, ) -> SCPINodeBase
        self._set_doc()
        if docstr:  # FIXME: remove the argument and assign self.__doc__ =  node.__doc__ unconditionally
            self.__doc__ = docstr

    def _set_doc(self):
        doc = [x.strip() for x in self._leaf_node.__doc__.splitlines()]
        doc.append("")
        doc.append("Conversion: `" + self._conv.__name__ + "`")
        self.__doc__ = "\n".join(doc)

    def _get_leaf(self, instance):
        # type: (T) -> SCPINodeBase
        root = self._get_root_node(instance)  # type: SCPINodeBase
        return self._leaf_node.relink_to_ancestor(root)

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.q(instance)

    def q(self, instance, **kwargs):
        """
        Executes a query on the SCPI node represented by the property.

        :param instance: The object which the SCPIProperty is an attribute of.
        :param kwargs: Any additional keyword parameters will be passed to query(), if the callback returns None.
        :return: The result of passing the SCPIResponse object to the conv function.
        """
        leaf = self._get_leaf(instance)  # type: SCPIQuery
        if not hasattr(leaf, "q"):
            raise AttributeError("SCPI node doesn't support query")
        if self._callback:
            cb = self._callback(self=instance, get=True)
            if cb is not None:
                return self._conv(leaf.q(**cb))
        return self._conv(leaf.q(**kwargs))

    def __set__(self, instance, value):
        self.w(instance, value)

    def w(self, instance, value, **kwargs):
        """
        Executes a write on the SCPI node represented by the property.

        :param instance: The object which the SCPIProperty is an attribute of.
        :param value: This will be passed as the first, and only, positional argument to write(), if callback returns None
        :param kwargs: Any additional keyword parameters will be passed to write(), if the callback returns None.
        """
        leaf = self._get_leaf(instance)  # type: SCPISet
        if not hasattr(leaf, "w"):
            raise AttributeError("SCPI node doesn't support write")

        if self._callback:
            cb = self._callback(self=instance, get=False, value=value)
            if cb is not None:
                return leaf.w(**cb)
        leaf.w(value, **kwargs)


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
        self._map = mapping
        self._rev_map = rev_mapping
        if rev_mapping is None:
            self._rev_map = {v: k for k, v in self._map.items()}
        super(SCPIPropertyMapping, self).__init__(node, conv, *args, **kwargs)

    def _set_doc(self):
        doc = [x.strip() for x in self._leaf_node.__doc__.splitlines() if not x.strip().startswith("Arguments")]
        doc.append("::\n")
        for a in self._map:
            doc.append("    " + str(a) + " : " + str(self._map[a]))
        self.__doc__ = "\n".join(doc)

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        x = super(SCPIPropertyMapping, self).__get__(instance, owner)
        try:
            return self._map[self._conv(x)]
        except KeyError as e:  # TODO: How should values missing from the mapping be handled? type coercion? Exception?
            raise KeyError("The response '{:s}' from the instrument was not found in the mapping dict.". format(str(x)))

    def __set__(self, instance, value):
        try:
            v = self._rev_map[value]
        except KeyError as e:
            raise KeyError("Value not found in the reverse mapping.")
        super(SCPIPropertyMapping, self).__set__(instance, v)


@functools.total_ordering
class MinMaxFloat(numbers.Real):
    """
    The MinMax class is used as return value from SCPIPropertyMinMax.__get__(..).
    """
    def __init__(self, prop, instance):
        """
        :param SCPIPropertyMinMax prop:
        :param instance:
        """
        self._instance = instance
        self._w = lambda x="": prop.w(instance, x)
        self._q = lambda x="": prop.q(instance, value=x, fmt="{value:s}")

    @property
    def value(self):
        """
        Attribute that queries/sets the value of the property.
        The return type is determined by the `conv` attribute of the SCPIProperty.
        """
        return self._q()

    @value.setter
    def value(self, value):
        self._w(value)

    def query_min(self):
        """ Returns the lowest value that the property can have. """
        return self._q("MIN")

    def set_min(self):
        """ Set the property to the lowest possible value. """
        self._w("MIN")

    def query_max(self):
        """ Returns the highest possible value that the property can have. """
        return self._q("MAX")

    def set_max(self):
        """ Set the property to the highest possible value. """
        self._w("MAX")

    def query_default(self):
        """ Returns the default value of the property. """
        return self._q("DEF")

    def set_default(self):
        """Set the property to the default value."""
        self._w("DEF")

    # Methods for numbers.Complex

    def __abs__(self):
        return abs(self.value)

    def __eq__(self, other):
        return self.value == other

    def __radd__(self, other):
        return other + self.value

    def __bool__(self):
        return bool(self.value)

    def __neg__(self):
        return -self.value

    def __pos__(self):
        return +self.value

    def __add__(self, other):
        return self.value + other

    def __mul__(self, other):
        return self.value * other

    def __rmul__(self, other):
        return other * self.value

    def __truediv__(self, other):
        return float(self) / other

    def __pow__(self, exponent):
        return self.value ** exponent

    def __rpow__(self, base):
        return base ** self.value

    # Methods for numbers.Real

    def __float__(self):
        return float(self.value)

    def __div__(self, other):
        return float(self) / other

    def __rdiv__(self, other):
        return other / float(self)

    def __rtruediv__(self, other):
        return other / float(self)

    def __floor__(self):
        return math.floor(float(self))

    def __ceil__(self):
        return math.ceil(float(self))

    def __round__(self, n=None):
        return round(float(self))

    def __floordiv__(self, other):
        return float(self).__floordiv__(other)

    def __rfloordiv__(self, other):
        return float(self).__rfloordiv__(other)

    def __mod__(self, other):
        return float(self) % other

    def __lt__(self, other):
        return float(self) < other

    def __le__(self, other):
        return float(self) <= other

    def __rmod__(self, other):
        return other % self.value

    def __trunc__(self):
        return math.trunc(self.value)


class SCPIPropertyMinMax(SCPIProperty):
    def __init__(self, *args, **kwargs):
        """
        :rtype: MinMax
        """
        super(SCPIPropertyMinMax, self).__init__(*args, **kwargs)

    def _set_doc(self):
        doc = [x.strip() for x in self._leaf_node.__doc__.splitlines() if not x.strip().startswith("Arguments")]
        doc.append(":class:`RSSscpi.SCPI_property.MinMax` instance, type conversion `" + self._conv.__name__ + "`")
        self.__doc__ = "\n".join(doc)

    def __get__(self, instance, owner=None):
        # type: (SCPINodeBase, object) -> MinMaxFloat
        if instance is None:
            return self
        return MinMaxFloat(self, instance)
