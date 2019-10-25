from .. import znb
from . import ZNA_gen


class Trace(znb.Trace):
    def get_marker(self, n):
        return Marker(n, trace=self)


class Marker(ZNA_gen.CALCulate.MARKer, znb.Marker):
    pass
