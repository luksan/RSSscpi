# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from collections import OrderedDict
import logging

# FIXME: There sould be some top-level management in RSSsscpi of the loggers
from typing import Any, Type

logger = logging.getLogger(__name__)


def scpi_bit(bit_number):
    """
    This functions returns a decorator for use in ScpiRegister subclasses in order to define
    individual bits in the register.

    The name of the decorated method and the bit number is appended as a tuple to the BITS list
    in the class.

    :param int bit_number: The number of the bit in the register. LSB is zero.
    """
    def fget(reg):
        return reg.value & (1 << bit_number)

    def fset(reg, value):
        if value:
            reg.value |= 1 << bit_number
        else:
            reg.value &= ~(1 << bit_number)

    class decorator(property):
        def __init__(self, bit_func):
            super().__init__(fget=fget, fset=fset, fdel=None, doc=bit_func.__doc__)
            self.__doc__ = super().__doc__
            self.bit_number = bit_number

    return decorator


class MetaRegister(type):
    @classmethod
    def __prepare__(mcs, name, bases):
        namespace = OrderedDict()
        namespace["BITS"] = []  # Create a new empty bit list for each subclass
        return namespace

    def __new__(mcs, name, bases, dict_: dict) -> Any:
        # noinspection PyTypeChecker
        register_cls = super().__new__(mcs, name, bases, dict_)  # type: Type[SCPIRegister]
        for name, val in dict_.items():
            if not hasattr(val, "bit_number"):
                continue
            assert not any(map(lambda bit: bit[1] == val.bit_number, register_cls.BITS)), \
                "A bit with number " + str(val.bit_number) + " is already defined in the register."
            register_cls.BITS.append((name, val.bit_number))
        return register_cls


class SCPIRegister(metaclass=MetaRegister):
    """
    Base class for defining a SCPI type register. Each bit in the register should be an empty method
    with a descriptive docstring, decorated with scpi_bit(<bit number>).

    The metaclass ensures that the BITS list is not inherited from the parent class.
    """

    BITS = None  # This is a list of tuples in the subclasses, set to None here to detect programming errors

    def __init__(self, value=0):
        self._bitmask = 0
        for _, bit in self.BITS:
            self._bitmask |= 1 << bit
        self._value = 0

        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if val & ~self._bitmask:
            logger.warning("Register value has set bits outside of the bits in the register definition. 0b{:08b}".format(val))
        self._value = val

    def __int__(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def pprint(self):
        print("0b{:08b}, {:}".format(self.value, self.value))
        for name, bit_no in self.BITS:
            print("{:>25} (bit {:}) {:}".format(name, bit_no, getattr(self, name)))

    def short_status(self):
        status = []
        for name, bit_no in self.BITS:
            if getattr(self, name):
                short_name = getattr(type(self), name).__doc__.lstrip()[:4]
                if not short_name[-1].isupper():
                    short_name = short_name[:-1]
                status.append(short_name)
        return ",".join(status)


class StatusByteRegister(SCPIRegister):
    """
    The STatus Byte (STB) provides a rough overview of the instrument status by collecting the pieces of information
    of the lower registers. The STB represents the highest level within the SCPI hierarchy. A special feature is that
    bit 6 acts as the summary bit of the remaining bits of the status byte.

    The STatus Byte (STB) is linked to the Service Request Enable (SRE) register on a bit-by-bit basis.

    The STB is read out using the command *STB? or a "Serial Poll".
    The SRE can be set using command *SRE and read using *SRE? .
    """
    @scpi_bit(2)
    def error_queue_not_empty(self):
        """
        ERRor queue not empty. Bit 2
        If this bit is enabled by the SRE, each entry of the error queue generates a "Service Request" (SRQ).
        Thus an error can be recognized and further pinned down by polling the error queue. The poll provides an
        informative error message.
        """
        pass

    @scpi_bit(3)
    def questionable_status(self):
        """
        QUEStionable status summary bit. Bit 3
        This bit is set if an EVENt bit is set in the "STATus:QUEStionable" register and the associated ENABle bit is set to 1.
        The bit indicates a questionable instrument status, which can be further pinned down by polling the QUEStionable register.
        """
        pass

    @scpi_bit(4)
    def message_available(self):
        """
        MAV bit (message available). Bit 4
        This bit is set if a message is available and can be read from the output buffer.
        This bit can be used to automatically transfer data from the instrument to the controller.
        """
        pass

    @scpi_bit(5)
    def event_status_summary(self):
        """
        ESB bit. Bit 5
        Sum bit of the event status register. It is set if one of the bits in the event status register is set and enabled
        in the event status enable register. Setting of this bit implies an error or an event which can be further pinned
        down by polling the event status register.
        """
        pass

    @scpi_bit(6)
    def master_status_summary(self):
        """
        MSS bit (master status summary bit). Bit 6
        This bit is set if the instrument triggers a service request. This is the case if one of the other bits of this
        register is set together with its mask bit in the service request enable register SRE.
        """
        pass

    @scpi_bit(7)
    def operation_status_summary(self):
        """
        OPERation status register summary. Bit 7
        This bit is set if an EVENt bit is set in the OPERation-Status register and the associated ENABle bit is set to 1.
        The bit indicates that the instrument is currently performing an action. The type of action can be determined by
        polling the "STATus:OPERation" register.
        """
        pass


class EventStatusRegister(SCPIRegister):
    """
    The Event Status Register (ESR) indicates general instrument states. It is linked to the Event Status Enable (ESE)
    register on a bit-by-bit basis.

    The ESR corresponds to the CONDition part of an SCPI register indicating the current instrument state
    (although reading is destructive).

    The Event Status Register (ESR) can be queried using ESR?. The Event Status Enable (ESE) register can be set
    using the command *ESE and read using *ESE?.
    """
    @scpi_bit(0)
    def operation_complete(self):
        """
        OPC. Operation Complete. This bit is set on receipt of the command *OPC after all previous commands have been executed.
        """
        pass

    @scpi_bit(2)
    def query_error(self):
        """
        QERR Query Error. This bit is set if either the controller wants to read data from the instrument without having
        sent a query, or if it does not fetch requested data and sends new instructions to the instrument instead. The cause
        is often a query which is faulty and hence cannot be executed.
        """
        pass

    @scpi_bit(3)
    def device_dependent_error(self):
        """
        DDE Device-Dependent Error
        This bit is set if a device-dependent error occurs. An error message with a number between –300 and –399 or a positive
        error number, which describes the error in greater detail, is entered into the error queue
        """
        pass

    @scpi_bit(4)
    def exceution_error(self):
        """
        EXE Execution Error
        This bit is set if a received command is syntactically correct, but cannot be performed for other reasons. An error
        message with a number between –200 and –300, which describes the error in greater detail, is entered into the error queue.
        """
        pass

    @scpi_bit(5)
    def command_error(self):
        """
        CMD Command Error
        This bit is set if a command which is undefined or syntactically incorrect is received. An error message with a
        number between -100 and -200, which describes the error in greater detail, is entered into the error queue.
        """
        pass

    @scpi_bit(6)
    def user_request(self):
        """
        USR User Request
        This bit is set when the instrument is switched over to manual control or when a user-defined softkey is used
        (see SYSTem:​USER:​KEY).
        """
        pass

    @scpi_bit(7)
    def power_on(self):
        """
        PWR Power On (supply voltage on)
        This bit is set when the instrument is switched on.
        """
        pass
