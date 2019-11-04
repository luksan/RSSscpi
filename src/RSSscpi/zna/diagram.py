from .. import znb
from . import ZNA_gen


class Diagram(znb.Diagram):
    @property
    def LAYout(self) -> ZNA_gen.DISPlay.LAYout:
        return super().LAYout

    @property
    def WINDow(self) -> ZNA_gen.DISPlay.WINDow:
        return super().WINDow
