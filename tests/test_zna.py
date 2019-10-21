from .conftest import VISA

from RSSscpi.zna import ZNA


class TestZNA:
    def test_init(self, dummy_zna: ZNA, visa: VISA):
        dummy_zna.init()
        assert ["*CLS;*ESE 127;*SRE 36",
                "SYSTem:COMMunicate:CODec UTF8",
                "SYSTem:LANGuage?",
                "SYSTem:LANGuage 'SCPI'",
                ] == visa.cmd
