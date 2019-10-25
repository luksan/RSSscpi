from .. import zna
from .. import znb
from . import ZNA_gen
from .trace import Trace


class Channel(znb.Channel):
    def __init__(self, n: int, instrument: "zna.ZNA"):
        super().__init__(n, instrument)

    @property
    def instrument(self) -> "zna.ZNA":
        return self._instr

    @property
    def CALC(self) -> ZNA_gen.CALCulate:
        return self.instrument.scpi.CALCulate[self.n]

    @property
    def CONFch(self) -> ZNA_gen.CONFigure.CHANnel:
        return self.instrument.scpi.CONFigure.CHANnel[self.n]

    @property
    def SENSe(self) -> ZNA_gen.SENSe:
        return self.instrument.scpi.SENSe[self.n]

    @property
    def SOURce(self) -> ZNA_gen.SOURce:
        return self.instrument.scpi.SOURce[self.n]

    @property
    def TRIGger(self) -> ZNA_gen.TRIGger:
        return self.instrument.scpi.TRIGger[self.n]

    def get_trace(self, name: str) -> "Trace":
        """
        :param name: The name of the trace
        :return: A Trace object
        """
        return Trace(name=name, channel=self)

    @property
    def sweep(self) -> "Sweep":
        return Sweep(self)

    @property
    def calibration(self) -> "ChannelCal":
        return ChannelCal(self)

    def get_vna_port(self, port_no) -> "ChannelVNAPort":
        return ChannelVNAPort(self, port_no)


class Sweep(ZNA_gen.SENSe.SWEep, znb.Sweep):
    def get_segment(self, n):
        return SweepSegment(n, channel=self.channel)


class SweepSegment(ZNA_gen.SENSe.SEGMent, znb.SweepSegment):
    pass


class ChannelCal(znb.ChannelCal):
    pass


class ChannelVNAPort(ZNA_gen.SOURce.POWer, znb.ChannelVNAPort):
    pass
