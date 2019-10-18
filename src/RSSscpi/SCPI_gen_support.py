# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:30:33 2016

@author: Lukas Sandström
"""

from itertools import zip_longest
from typing import Generator, NoReturn, Optional, Type, TypeVar, Union

from RSSscpi.SCPI_response import SCPIResponse

N = TypeVar("N", bound="SCPINodeBase")


class SCPINodeBase(object):
    _cmd = "SCPINodeBase"
    _parent_class = None  # The class of the parent of the command node
    _SCPI_class = None  # Identifies the original class type in cases of subclassing
    args = []  # type: List[str]
    """
    The arguments available for the SCPI node, as reported by GPIB Explorer.
    """

    __slots__ = ("_parent", )

    def __init__(self, parent: "SCPINodeBase" = None):
        """
        :param parent: The command node level above this node.
        """
        self._parent = parent
        if self.__class__._SCPI_class is None:
            self.__class__._SCPI_class = self.__class__

    def __str__(self) -> str:
        return self._cmd

    def __get__(self, instance: "SCPINodeBase", owner: Type["SCPINodeBase"]) -> Union["SCPINodeBase", Type["SCPINodeBase"]]:
        # Since the class definitions are nested we have to resolve the parent class at runtime
        if self.__class__._parent_class is None:
            assert owner._SCPI_class is not None
            self.__class__._parent_class = owner._SCPI_class
        if not instance:
            return self.__class__
        return self.__class__(parent=instance)

    def __set__(self, instance, value) -> NoReturn:
        raise AttributeError("You probably don't want to do this assignment. Use .w() instead.")

    def __getattribute__(self, name: str):
        try:
            x = object.__getattribute__(self, name)
        except AttributeError:
            raise AttributeError("'%s' has no attribute '%s'" % (self.build_cmd(), name))
        cls = x.__class__
        if issubclass(cls, SCPINodeBase) and cls._SCPI_class.__module__ != self._SCPI_class.__module__:
            raise AttributeError("Refusing access to a SCPINode from another module. %s !-> %s" % (self._SCPI_class, cls))
        return x

    @classmethod
    def _parent_class_iter(cls) -> Generator[Type["SCPINodeBase"], None, None]:
        while cls:
            yield cls
            cls = cls._parent_class

    def _parent_instance_iter(self) -> Generator["SCPINodeBase", None, None]:
        while self:
            yield self
            self = self._parent

    def build_cmd(self) -> str:
        return ":".join(reversed([str(x) for x in self._parent_instance_iter() if str(x)]))

    def _get_instrument(self):
        """
        :return: Returns the root node of the command tree, an Instrument.
        :rtype: RSSscpi.Instrument.Instrument
        """
        if not self._parent:
            from RSSscpi.Instrument import Instrument  # FIXME: restructure the code to avoid circular import
            assert isinstance(self, Instrument)
            return self
        return self._parent._get_instrument()

    @classmethod
    def relink_to_ancestor(cls, ancestor: "SCPINodeBase") -> "SCPINodeBase":
        """
        Create a new instance with the parent chain linking to ancestor.

        :param SCPINodeBase ancestor: The SCPINodeBase instance to link to
        :rtype: SCPINodeBase
        """
        assert isinstance(ancestor, SCPINodeBase)
        intermediates = []
        for i in cls._parent_class_iter():
            # Stop adding parents to the list when we find `ancestor`
            # We can't use isinstance(), since ZVA is subclassed from ZNB, instead we compare
            # the _cmd attribute and check that the trees have the same length and command nodes
            for a, b in zip_longest(ancestor._parent_class_iter(), i._parent_class_iter()):  # type: (Type["SCPINodeBase"], Type["SCPINodeBase"])
                if a is None or b is None or a._cmd != b._cmd:
                    break
            else:
                break
            intermediates.append(i.__name__)
        else:
            raise AttributeError("The given ancestor was not found in the command tree.")

        leaf = ancestor
        for c in reversed(intermediates):
            try:
                # We use getattr(..) instead of direct instantiation, since ZVA is subclassed from ZNB
                leaf = getattr(leaf, c)
            except AttributeError as e:  # Apparently the subclassing was incorrect
                raise AttributeError(str(e) + " -- " + ancestor.build_cmd() + ":" + ":".join(reversed(intermediates)))
        return leaf  # Return the instantiated leaf node, properly linked to the root node


class SCPINode(SCPINodeBase):
    _cmd = "SCPINode"

    __slots__ = ()

    def __getitem__(self, item: int) -> NoReturn:
        raise TypeError(self.build_cmd() + "(XX) <- invalid index operation, SCPI node does not support indexing.")


class SCPINodeN(SCPINodeBase):
    _cmd = "SPCINodeN"

    __slots__ = ("_n", )

    def __init__(self, parent=None):
        super(SCPINodeN, self).__init__(parent=parent)
        self._n = ""

    def __str__(self):
        return self._cmd + self._n

    @property
    def n(self):
        """
        The index of the node, ie. channel or marker number.

        :rtype: int
        """
        return int(self._n)

    @n.setter
    def n(self, n: Optional[int]):
        if n is None or n == 0:
            self._n = ""
            return

        self._n = str(n)
        if not self._n.isdigit():
            raise ValueError(self.build_cmd() + "[%s] <- Node index must be integer, or None." % n)

    def __getitem__(self: N, n: int = None) -> N:
        """
        Returns a copy of self, with the node index set to n.
        :param int n: Integer index to be appended to the command node string. If n is None or 0 the index is removed.
        """
        cpy = self.__class__(parent=self._parent)
        cpy.n = n
        return cpy


class SCPICmd(SCPINodeBase):
    __slots__ = ()


class SCPIQuery(SCPICmd):
    __slots__ = ()

    def q(self, *args, **kwargs) -> SCPIResponse:
        """
        Execeute a SCPI query.

        :returns: a SCPIResponse instance
        """
        return self._get_instrument().query(self, *args, **kwargs)


class SCPISet(SCPICmd):
    __slots__ = ()

    def w(self, *args, **kwargs) -> None:
        """
        Send a string to the VISA resource, without reading the response.

        :rtype: None
        """
        return self._get_instrument().write(self, *args, **kwargs)


class SCPIBool(SCPIQuery, SCPISet):
    __slots__ = ()

    def _mk_arg(self, x):
        if str(x) in self.args:  # Allow extensions, such as ONCE to SYSTem:DISPlay:UPDate
            return str(x)
        return "OFF" if not x or x == "0" or str(x).upper() == "OFF" else "ON"

    def q(self, *args, **kwargs) -> bool:
        """
        Execute a query and convert the response to a bool, (0, OFF) -> False, etc.
        """
        return bool(super(SCPIBool, self).q(*args, **kwargs))

    def w(self, x):
        super(SCPIBool, self).w(self._mk_arg(x))

    def on(self):
        self.w("ON")

    def off(self):
        self.w("OFF")
