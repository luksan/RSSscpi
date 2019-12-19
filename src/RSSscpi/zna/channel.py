from .. import zna
from .. import znb
from . import ZNA_gen
from .trace import Trace


class Channel(znb.Channel):
    def __init__(self, n: int, instrument: "zna.ZNA"):
        super().__init__(n, instrument)

    @property
    def instrument(self) -> "zna.ZNA":
        assert isinstance(self._instr, zna.ZNA)
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

    def set_analog_IF_path(self, *, ifbw: float = None, path: str = None):
        """
        Sets the analog IF path. If ifbw is given then a suitable path is selected,
        otherwise the path_name can be given as one of WIDeband, NORMal, NARRowband.
        """
        if ifbw and ifbw > 1.5e6:
            if path and path not in ("WID", "WIDeband"):
                raise ValueError("IF bandwidth higher than 1.5 MHz require the wide IF path")
            self.SENSe.IFPath.w("WIDeband")
            return
        if path:
            if path not in ("WIDeband", "WID", "NORMal", "NORM", "NARRowband", "NARR"):
                raise ValueError("Invalid analog IF path: {:}".format(path))
            self.SENSe.IFPath.w(path)
        else:
            self.SENSe.IFPath.w("NORMal")

    def configure_freq_sweep(self, start_freq, stop_freq, *, points=None, ifbw=None, power=None, log_sweep=False):
        if ifbw:
            self.set_analog_IF_path(ifbw=ifbw)
        super().configure_freq_sweep(start_freq, stop_freq, points=points, ifbw=ifbw, power=power, log_sweep=log_sweep)

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


class Sweep(znb.Sweep):
    @property
    def INITiate(self) -> ZNA_gen.INITiate:
        return super().INITiate

    @property
    def SWEep(self) -> ZNA_gen.SENSe.SWEep:
        return super().SWEep

    def get_segment(self, n):
        return SweepSegment(n, channel=self.channel)


class SweepSegment(ZNA_gen.SENSe.SEGMent, znb.SweepSegment):
    pass


class ChannelCal(znb.ChannelCal):
    pass


class ChannelVNAPort(znb.ChannelVNAPort):
    @property
    def SOURcePOWer(self) -> ZNA_gen.SOURce.POWer:
        return super().SOURcePOWer
