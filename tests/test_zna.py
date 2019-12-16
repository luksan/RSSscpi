import pytest

from .conftest import VISA

from RSSscpi.zna import ZNA


class TestZNA:
    def test_init(self, dummy_zna: ZNA, visa: VISA):
        dummy_zna.init()
        assert visa.cmd == [
            "*CLS;*ESE 61;*SRE 36",
            "SYSTem:COMMunicate:CODec UTF8",
            "SYSTem:LANGuage?",
            "SYSTem:LANGuage 'SCPI'",
        ]

    def test_info(self, dummy_zna: ZNA, visa: VISA):
        info = dummy_zna.info
        assert info.manufacturer == "Rohde-Schwarz"
        assert info.model == "ZNA26-4Port"
        assert info.serial_number == "1332450024101220"
        assert info.firmware == "1.91"
        assert visa.cmd == ["*IDN?", ]

        assert info.installed_options == tuple(visa.ret_dict["*OPT?"].split(","))
        assert info.has_option("B34")
        assert info.has_option("ZNA26-B34")
        assert not info.has_option("K2")
        assert not info.has_option("B1")
        assert visa.cmd == ["*OPT?", ]


class TestChannel:
    def test_IF_path(self, dummy_zna: ZNA, visa: VISA):
        ch = dummy_zna.get_channel(1)
        ch.set_analog_IF_path(ifbw=1e6)
        ch.set_analog_IF_path(ifbw=15e6)
        with pytest.raises(ValueError):
            ch.set_analog_IF_path(ifbw=15e6, path="NORM")
        ch.set_analog_IF_path(path="WIDeband")
        ch.set_analog_IF_path(path="NORM")
        ch.set_analog_IF_path(path="NARRowband")
        with pytest.raises(ValueError):
            ch.set_analog_IF_path(path="NAR")

        assert visa.cmd == [
            "SENSe1:IFPath NORMal",
            "SENSe1:IFPath WIDeband",
            "SENSe1:IFPath WIDeband",
            "SENSe1:IFPath NORM",
            "SENSe1:IFPath NARRowband",
        ]

    def test_conf_freq_sweep(self, dummy_zna: ZNA, visa: VISA):
        ch = dummy_zna.get_channel(1)
        ch.configure_freq_sweep(1e9, 2e9, ifbw=1e6)
        assert visa.cmd == [
            "SENSe1:IFPath NORMal",
            "SENSe1:SWEep:TYPE LIN",
            "SENSe1:FREQuency:STARt 1000000000.0",
            "SENSe1:FREQuency:STOP 2000000000.0",
            "SENSe1:BANDwidth 1000000.0",
        ]

        ch.configure_freq_sweep(1e9, 2e9, ifbw=30e6)
        assert visa.cmd == [
            "SENSe1:IFPath WIDeband",
            "SENSe1:SWEep:TYPE LIN",
            "SENSe1:FREQuency:STARt 1000000000.0",
            "SENSe1:FREQuency:STOP 2000000000.0",
            "SENSe1:BANDwidth 30000000.0",
        ]
