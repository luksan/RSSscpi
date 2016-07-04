# -*- coding: utf-8 -*-
"""
Created on 16 feb. 2016

@author: Lukas Sandström
"""

from gen import ZNB_gen, SCPINodeBase, SCPIProperty, SCPIPropertyMinMax
from VNA import VNA


class ZNB(ZNB_gen):
    def __init__(self, visa_res):
        super(ZNB, self).__init__(visa_res)

    def set_source_power_offset(self, channel=None, src=0, power=-300, relative=True):
        """
        :type relative: bool
        """
        if relative:
            x = 'CPAD'
        else:
            x = 'ONLY'
        self.SOURce(channel).POWer(src).LEVel.IMMediate.OFFSet().w(power, x)

    @property
    def active_channel(self):
        """
        Get the active channel, INSTrument:NSELect? \n
        :return: int
        """
        return int(self.INSTrument.NSELect().q())

    @active_channel.setter
    def active_channel(self, n):
        """
        Set the active channel, INSTrument:NSELect n \n
        :param n: (int, str)
        :return: None
        """
        self.INSTrument.NSELect().w(n)

    def get_channel(self, n):
        """

        :param n: Channel number
        :rtype: Channel
        """
        return Channel(n, self)


class Channel(object):
    def __init__(self, n, instrument):
        """
        :param n: Channel number
        :param instrument: A SCPINode instance, linked to the instrument
        :type instrument: ZNB_gen
        """
        self.n = n
        self.instrument = instrument
        self.CALC = instrument.CALCulate(n)
        self.CONFch = instrument.CONFigure.CHANnel(n)
        self.SWEep = instrument.SENSe(n).SWEep

    def get_trace(self, name, n=None):
        """

        :param name: The name of the trace
        :param n: The trace id, if known
        :rtype: Trace
        """
        return Trace(name, self)

    @property
    def active_trace(self):
        """
        Query or set the active trace in the channel

        :rtype: Trace
        """
        name = str(self.CALC.PARameter.SELect.q())
        #n = self.instrument.CONFigure.TRACe.CHANnel.NAME.ID.q(name)
        return Trace(name, self)

    @active_trace.setter
    def active_trace(self, trace):
        name = trace.name if isinstance(trace, Trace) else str(trace)
        self.CALC.PARameter.SELect.w(name)

    sweep_points = SCPIPropertyMinMax(["POINts"], None, lambda self: self.SWEep)
    """
    The number of points in the sweep. SENSe<Ch>:SWEep:POINts
    """


class Sweep(ZNB_gen.SENSe.SWEep):
    def __init__(self, channel):
        super(Sweep, self).__init__(parent=channel.SWEep)


class Trace(object):
    def __init__(self, name, channel):
        """
        :param n: The trace ID, CONF:TRAC:CHAN:NAME:ID? '<trace name>'
        :param name: The trace name
        :param channel: The channel the trace belongs to
        :type channel: Channel
        """
        self._name = name
        self.channel = channel

    def _root_node(self):
        return self.channel.instrument

    def _make_active_cb(self, *args, **kwargs):
        self.make_active()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        name = str(name)
        self.channel.instrument.CONFigure.TRACe.REName.w(self.name, name)
        self._name = name

    @property
    def n(self):
        return int(self.channel.instrument.CONFigure.TRACe.NAME.ID.q(self.name))

    # TODO: argument checking?
    format = SCPIProperty(["CALCulate", "FORMat"], _make_active_cb, _root_node)

    def is_active(self):
        return self.channel.active_trace.name == self.name

    def make_active(self):
        """
        Makes the trace the active trace in the channel.
        """
        self.channel.CALC.PARameter.SELect.w(self.name)

    def get_marker(self, n):
        """

        :param n: Marker number
        :rtype: Marker
        """
        return Marker(n, self)


class Marker(ZNB_gen.CALCulate.MARKer):  # Add direct inheritance from object to un-confuse PyCharm
    """
    Represents a trace marker in the VNA.
    Property access will make the trace associated with the marker the active trace in the channel.
    """

    def __init__(self, n, trace):
        """
        :param n: Marker number
        :param trace: The trace which the marker belongs to
        :type trace: Trace
        """
        super(Marker, self).__init__(parent=trace.channel.CALC)
        self.n = n
        self.trace = trace
        self._cmd_cnt = None

    def _prop_callback(self, *args, **kwargs):
        if not self._cmd_cnt or self._cmd_cnt != self.trace.channel.instrument.command_cnt:
            self.trace.make_active()
        self._cmd_cnt = self.trace.channel.instrument.command_cnt + 1

    tracking = SCPIProperty(["SEARch", "TRACking"], _prop_callback) #: Marker tracking enabled
    state = SCPIProperty(["STATe"], _prop_callback)
    """Enable/disable the marker"""
    #: Marker position
    x = SCPIProperty(["X"], _prop_callback)
    #: Marker value
    y = SCPIProperty(["Y"], _prop_callback)


if __name__ == '__main__':
    from RSSscpi.gen.SCPI_gen_support import DummyVisa
    znb = ZNB(DummyVisa("Visa1"))

    znb.ABORt.w()
