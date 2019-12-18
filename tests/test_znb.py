# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import math

import pytest
from .conftest import VISA  # noqa: F401

import struct

from RSSscpi import znb  # noqa: F401
from RSSscpi.znb import ZNB  # noqa: F401
from RSSscpi.scpi.class_property import SCPIPropertyMinMax
from RSSscpi.scpi.response import make_ieee_data_block


class PropertyTester:
    def pytest_generate_tests(self, metafunc):
        if metafunc.function.__name__ == "test_bool_properties":
            props = self.bool_properties
        elif metafunc.function.__name__ == "test_float_properties":
            props = self.float_properties
        elif metafunc.function.__name__ == "test_int_properties":
            props = self.int_properties
        else:
            return
        if not props:
            metafunc.parametrize('prop_name, scpi_cmd, scpi_write, scpi_query', ([None] * 4,))
            return
        metafunc.parametrize('prop_name, scpi_cmd, scpi_write, scpi_query',
                             props, ids=[x[0] for x in props])

    @pytest.fixture
    def prop_owner(self):
        """
        This fixture should be overridden in subclasses. It should return an object on which the attributes to be
        tested can be found.
        """
        raise NotImplementedError

    @staticmethod
    def prop_parametrize(props):
        return pytest.mark.parametrize('prop_name, scpi_cmd, scpi_write, scpi_query', props, ids=[x[0] for x in props])

    bool_properties = []

    def test_bool_properties(self, prop_name, scpi_cmd, scpi_write, scpi_query, scpi_bool, prop_owner, visa):
        self.prop_test(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_bool, prop_owner, visa, bool)

    float_properties = []

    def test_float_properties(self, prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, prop_owner, visa):
        self.prop_test(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, prop_owner, visa, float)

    int_properties = []

    def test_int_properties(self, prop_name, scpi_cmd, scpi_write, scpi_query, scpi_int, prop_owner, visa):
        self.prop_test(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_int, prop_owner, visa, int)

    @staticmethod
    def prop_test(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_values, instance, visa, type_):
        """

        :param prop_name: the name of the class attribute
        :param scpi_cmd: the expected SCPI command
        :param scpi_write: expected write
        :param scpi_query: expected query
        :param scpi_values: values to test with write
        :param instance: The instance to which prop_name is attached
        :param visa: the VISA mock
        :param type_: the expected type of the value of the attribute
        :return:
        """
        if prop_name is None:
            return
        visa.ret = scpi_values[1]  # the string representation of the value
        x = getattr(instance, prop_name)
        assert isinstance(x, type_) and x == scpi_values[0]
        setattr(instance, prop_name, scpi_values[0])
        assert visa.cmd == [scpi_query.format(scpi_cmd), scpi_write.format(scpi_cmd, scpi_values[1])]
        minmax = prop_name + "_minmax"
        if hasattr(instance, minmax):
            assert isinstance(getattr(instance, minmax), SCPIPropertyMinMax)
            setattr(instance, minmax, scpi_values[0])
            assert visa.cmd == [scpi_write.format(scpi_cmd, scpi_values[1])]


class TestZNB:
    def test_scpi_getattr(self, dummy_znb):
        vna = dummy_znb
        assert type(vna.IDN) == type(vna.scpi.IDN)
        with pytest.raises(AttributeError, match="'ZNB' object has no attribute 'no_such_attr'"):
            getattr(vna, "no_such_attr")
        with pytest.raises(AttributeError, match="'' has no attribute 'NOTreallyanode'"):
            getattr(vna, "NOTreallyanode")

    def test_init(self, dummy_znb, visa):
        # type: (ZNB, VISA) -> None
        dummy_znb.init()
        assert visa.cmd == [
            "*CLS;*ESE 125;*SRE 36",
            "SYSTem:COMMunicate:CODec UTF8",
            "SYSTem:LANGuage?",
            "SYSTem:LANGuage 'SCPI'",
        ]

    def test_preset(self, dummy_znb: ZNB, visa: VISA):
        dummy_znb.preset()
        assert visa.cmd == [
            "*RST",
            "*OPC?",
            "*CLS;*ESE 125;*SRE 36",
            "SYSTem:COMMunicate:CODec UTF8",
            "SYSTem:LANGuage?",
            "SYSTem:LANGuage 'SCPI'",
        ]

    def test_info(self, dummy_znb: ZNB, visa: VISA):
        info = dummy_znb.info
        assert info.manufacturer == "Rohde-Schwarz"
        assert info.model == "ZNB8-4Port"
        assert info.serial_number == "1311601044100005"
        assert info.firmware == "2.90.1.125"
        assert visa.cmd == ["*IDN?", ]

    def test_reset_remote_emulation(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        visa.ret = "SCPI"
        assert dummy_vna.reset_remote_emulation() == "SCPI"
        assert ["SYSTem:LANGuage?"] == visa.cmd
        visa.ret = "ZVR"
        assert dummy_vna.reset_remote_emulation() == "ZVR"
        assert ["SYSTem:LANGuage?",
                "SYSTem:LANGuage 'SCPI'",
                ] == visa.cmd

    def test_use_binary_transfer(self, dummy_vna: ZNB, visa: VISA):
        vna = dummy_vna
        visa.ret = "ASCii"
        assert vna.use_binary_data_transfer is False
        visa.ret = "REAL"
        assert vna.use_binary_data_transfer is True
        vna.use_binary_data_transfer = True
        vna.use_binary_data_transfer = False
        assert visa.cmd == [
            "FORMat:DATA?",
            "FORMat:DATA?",
            "FORMat:DATA REAL",
            "FORMat:DATA ASCii",
        ]

    def test_active_channel(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        vna = dummy_vna
        x = vna.active_channel
        assert x.n == 1
        vna.active_channel = 3
        vna.active_channel = "2"
        vna.active_channel = x
        assert ["INSTrument:NSELect?",
                "INSTrument:NSELect 3",
                "INSTrument:NSELect 2",
                "INSTrument:NSELect 1",
                ] == visa.cmd

    def test_query_channel_list(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        visa.ret = "1,Ch1,3,Test_channel"
        x = dummy_vna.query_channel_list()
        assert len(x) == 2
        assert isinstance(x[0][0], dummy_vna.get_channel(1).__class__)
        assert x[0][0].n == 1 and x[0][1] == "Ch1"
        assert x[1][0].n == 3 and x[1][1] == "Test_channel"
        assert ["CONFigure:CHANnel:CATalog?",
                ] == visa.cmd

    def test_query_port_count(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        vna = dummy_vna
        visa.ret = "4"
        x = vna.query_number_of_ports()
        assert x == 4
        assert ["INSTrument:PORT:COUNt?",
                ] == visa.cmd
        visa.ret = "1"
        x = vna.query_number_of_ports()  # The number of ports on the instrument should be cached
        assert x == 4
        assert [] == visa.cmd

    def test_save_and_load_state(self, dummy_vna: ZNB, visa: VISA):
        znb = dummy_vna
        state1 = znb.save_recall_set("state1.znx")
        assert str(state1) == r"C:\Rohde & Schwarz\Nwa\state1.znx"
        state2 = znb.filesystem.file(r"c:\state2.znx")
        assert str(state2) == r"c:\state2.znx"
        state2_out = znb.save_recall_set(state2)
        assert str(state2_out) == str(state2)

        assert visa.cmd == [
            "MMEMory:STORe:STATe 1,'state1.znx'",
            "MMEMory:CDIRectory?",
            "MMEMory:CDIRectory?",
            "MMEMory:STORe:STATe 1,'c:\\state2.znx'",
            "MMEMory:CDIRectory?",
        ]

        znb.load_recall_set("state1.znx")
        znb.load_recall_set(state2_out)
        assert visa.cmd == [
            "MMEMory:LOAD:STATe 1,'state1.znx'",
            "MMEMory:LOAD:STATe 1,'c:\\state2.znx'",
        ]

    def test_znb_screenshot(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        vna = dummy_vna
        scr = vna.save_screenshot("scr.png")
        assert scr.filename == "scr.png"
        assert ["MMEMory:NAME 'scr.png'",
                "HCOPy:DESTination 'MMEM'",
                "HCOPy:DEVice:LANGuage PNG",
                "HCOPy:PAGE:WINDow HARDcopy",
                "HCOPy:IMMediate",
                "MMEMory:CDIRectory?",
                ] == visa.cmd
        with pytest.raises(ValueError):
            vna.save_screenshot("scr.docx")
        assert visa.cmd == []


class TestCalibrationManager:
    def test_calpool_ops(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        c = dummy_vna.cal_manager
        visa.ret = '77668, 125731287040, cal1.cal,, 38834, cal2.cal,, 38834,'
        visa._def_set = False
        x = c.query_calpool_list()
        assert ["cal1.cal", "cal2.cal"] == x
        c.delete_calgroup("test1.cal")
        assert [r"MMEMory:CDIRectory?",
                r"MMEMory:CDIRectory DEFault",
                r"MMEMory:CDIRectory?",
                r"MMEMory:CDIRectory 'C:\Rohde & Schwarz\Nwa'",
                r"MMEMory:CATalog? 'C:\Rohde & Schwarz\Nwa\Calibration\Data'",
                r"MMEMory:DELete:CORRection 'test1.cal'",
                ] == visa.cmd


class TestChannel(PropertyTester):
    @pytest.fixture
    def ch(self, dummy_vna):
        return dummy_vna.get_channel(2)

    @pytest.fixture
    def prop_owner(self, ch):
        return ch

    def test_channel(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        ch = dummy_vna.get_channel(3)
        assert ch.name == "1"
        ch.name = "Ch2"
        assert ["CONFigure:CHANnel3:NAME?",
                "CONFigure:CHANnel3:NAME 'Ch2'",
                ] == visa.cmd

        tr = ch.create_trace("Tr1", "S11")
        assert tr.name == "Tr1"
        tr = ch.create_trace("Tr2", tr.MeasParam.S(dst_port=2, src_port=2), dummy_vna.get_diagram(1))
        assert tr.name == "Tr2"
        assert ["CALCulate3:PARameter:SDEFine 'Tr1', 'S11'",
                "CALCulate3:PARameter:SDEFine 'Tr2', 'S22'",
                "DISPlay:WINDow1:STATe ON",
                "DISPlay:WINDow1:TRACe:EFEed 'Tr2'",
                ] == visa.cmd

        visa.ret = "Tr1"
        tr = ch.active_trace
        visa.ret = "1"
        assert tr.name == "Tr1"
        ch.active_trace = "Tr3"
        ch.active_trace = ch.get_trace("Tr2")
        assert ["CALCulate3:PARameter:SELect?",
                "CALCulate3:PARameter:SELect 'Tr3'",
                "CALCulate3:PARameter:SELect 'Tr2'",
                ] == visa.cmd

        ch.power_level = -10.33
        assert ch.power_level == 1.
        assert ["SOURce3:POWer:LEVel:IMMediate:AMPLitude -10.33",
                "SOURce3:POWer:LEVel:IMMediate:AMPLitude?",
                ] == visa.cmd

    def test_query_trace_list(self, dummy_vna, visa):
        if type(dummy_vna).__name__ == "ZVA":
            pytest.xfail("Not implemented on ZVA")
        ch = dummy_vna.get_channel(2)
        visa.ret = ""
        assert ch.query_trace_list() == []
        visa.ret = "1,Trc1,2,Ch2Trc"
        traces = ch.query_trace_list()
        assert len(traces) == 2
        assert traces[0].name == "Trc1"
        assert traces[1].name == "Ch2Trc"
        assert visa.cmd == [
            "CONFigure:CHANnel2:TRACe:CATalog?",
            "CONFigure:CHANnel2:TRACe:CATalog?",
        ]

    def test_channel_sweep(self, dummy_znb: ZNB, visa: VISA):
        ch = dummy_znb.get_channel(3)
        assert isinstance(ch.sweep.points_minmax.query_default(), int)
        ch.sweep.points = 301
        assert isinstance(ch.sweep.points, int)
        ch.sweep.points_minmax = 301
        ch.sweep.TYPE.w("LIN")
        assert ["SENSe3:SWEep:POINts? DEF",
                "SENSe3:SWEep:POINts 301",
                "SENSe3:SWEep:POINts?",
                "SENSe3:SWEep:POINts 301",
                "SENSe3:SWEep:TYPE LIN",
                ] == visa.cmd

        visa.ret = "LIN"
        assert ch.sweep.type == "LIN"
        ch.sweep.type = "POW"
        assert ["SENSe3:SWEep:TYPE?",
                "SENSe3:SWEep:TYPE POW",
                ] == visa.cmd

        ch.configure_freq_sweep(10e6, 9e9)
        assert ["SENSe3:SWEep:TYPE LIN",
                "SENSe3:FREQuency:STARt 10000000.0",
                "SENSe3:FREQuency:STOP 9000000000.0",
                ] == visa.cmd

        ch.configure_freq_sweep(10, 10e6, points=101, ifbw=1e3, power=-10, log_sweep=True)
        ch.init_sweep()
        assert ["SENSe3:SWEep:TYPE LOG",
                "SENSe3:FREQuency:STARt 10",
                "SENSe3:FREQuency:STOP 10000000.0",
                "SENSe3:SWEep:POINts 101",
                "SENSe3:BANDwidth 1000.0",
                "SOURce3:POWer:LEVel:IMMediate:AMPLitude -10",
                "INITiate3:IMMediate",
                ] == visa.cmd

        ch.configure_power_sweep(freq=40e9, start_power=-40, stop_power=10, points=41, ifbw=1e3)
        assert ["SENSe3:SWEep:TYPE POW",
                "SENSe3:FREQuency:CW 40000000000.0",
                "SOURce3:POWer1:STARt -40",
                "SOURce3:POWer1:STOP 10",
                "SENSe3:SWEep:POINts 41",
                "SENSe3:BANDwidth 1000.0",
                ] == visa.cmd

    bool_properties = [
        ("state", "CONFigure:CHANnel2:STATe", "{:s} {:s}", "{:s}?"),
    ]

    float_properties = [
        ("freq_cw", "SENSe2:FREQuency:CW", "{:s} {:s}", "{:s}?"),
        ("freq_start", "SENSe2:FREQuency:STARt", "{:s} {:s}", "{:s}?"),
        ("freq_stop", "SENSe2:FREQuency:STOP", "{:s} {:s}", "{:s}?"),
        ("freq_center", "SENSe2:FREQuency:CENTer", "{:s} {:s}", "{:s}?"),
        ("freq_span", "SENSe2:FREQuency:SPAN", "{:s} {:s}", "{:s}?"),
        ("power_level", "SOURce2:POWer:LEVel:IMMediate:AMPLitude", "{:s} {:s}", "{:s}?"),
    ]

    int_properties = [
        ("ifbw", "SENSe2:BANDwidth", "{:s} {:s}", "{:s}?"),
    ]

    def test_channel_properties(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        ch = dummy_vna.get_channel(1)
        visa.ret = "'Ch1'"
        assert ch.name == "Ch1"
        ch.name = "Ch2"
        assert ["CONFigure:CHANnel1:NAME?",
                "CONFigure:CHANnel1:NAME 'Ch2'",
                ] == visa.cmd

        visa.ret = "HIGH"
        ch.if_selectivity = "NORM"
        assert ch.if_selectivity == "HIGH"
        assert ["SENSe1:BANDwidth:RESolution:SELect NORM",
                "SENSe1:BANDwidth:RESolution:SELect?",
                ] == visa.cmd

    def test_channel_cal(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        ch = dummy_vna.get_channel(2)
        ch.cal_auto((1, 2, 3, 4))
        assert ["SENSe2:CORRection:COLLect:AUTO:TYPE FNPort, '', 1, 2, 3, 4",
                ] == visa.cmd
        ch.cal_auto((1, 2, 3, 4), (3, 4, 1, 2), cal_type="FOPort")
        assert ["SENSe2:CORRection:COLLect:AUTO:PORTs:TYPE FOPort, '', 1, 3, 2, 4, 3, 1, 4, 2",
                ] == visa.cmd
        ch.cal_auto((1, 2, 3, 4), cal_unit_characterization="user2.calkit")
        assert ["SENSe2:CORRection:COLLect:AUTO:TYPE FNPort, 'user2.calkit', 1, 2, 3, 4",
                ] == visa.cmd

    def test_channel_save_touchstone(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        ch = dummy_vna.get_channel(2)
        f = ch.save_touchstone("file.s3p", (1, 2, 3))
        assert f.filename == "file.s3p"
        assert ["MMEMory:STORe:TRACe:PORTs 2, 'file.s3p', LOGPhase, CIMPedance, 1, 2, 3",
                "MMEMory:CDIRectory?",
                ] == visa.cmd


class TestChannelCal:
    def test_calgroup(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        cal = dummy_vna.get_channel(1).calibration
        visa.ret = '77668, 125731287040, cal1.cal,, 38834, cal2.cal,, 38834,'
        visa._def_set = False
        assert cal.query_calpool_list() == ['cal1.cal', 'cal2.cal']

        visa.ret = ""
        assert cal.query_calgroup() is None
        visa.ret = "cal4.cal"
        assert cal.query_calgroup() == "cal4.cal"

        cal.resolve_calgroup_link()
        assert [r"MMEMory:CDIRectory?",
                r"MMEMory:CDIRectory DEFault",
                r"MMEMory:CDIRectory?",
                r"MMEMory:CDIRectory 'C:\Rohde & Schwarz\Nwa'",
                r"MMEMory:CATalog? 'C:\Rohde & Schwarz\Nwa\Calibration\Data'",
                r"MMEMory:LOAD:CORRection? 1",
                r"MMEMory:LOAD:CORRection? 1",
                r"MMEMory:LOAD:CORRection:RESolve 1",
                ] == visa.cmd

        cal.load_calibration("cal3.cal")
        cal.store_calibration("cal2.cal")
        assert ["MMEMory:LOAD:CORRection 1, 'cal3.cal'",
                "MMEMory:STORe:CORRection 1, 'cal2.cal'",
                ] == visa.cmd


class TestChannelVNAPort(PropertyTester):
    @pytest.fixture()
    def prop_owner(self, dummy_vna):
        return dummy_vna.get_channel(3).get_vna_port(2)

    SOURcePOWer = "SOURce3:POWer2:"

    bool_properties = [
        ("power_enabled", SOURcePOWer + "STATe", "{:s} {:s}", "{:s}?"),
        ("power_gen", SOURcePOWer + "PERManent:STATe", "{:s} {:s}", "{:s}?"),
    ]

    float_properties = [
        ("cal_power_offset", SOURcePOWer + "CORRection:LEVel:OFFSet", "{:s} {!s}", "{:s}?"),
        ("power_slope", SOURcePOWer + "LEVel:IMMediate:SLOPe", "{:s} {!s}", "{:s}?"),
    ]

    int_properties = [
        ("receiver_attenuator", "SENSe3:POWer:ATTenuation", "{:s} 2, {:s}", "{:s}? 2"),
    ]

    def test_source_power_offset(self, dummy_vna: ZNB, visa: VISA):
        ch = dummy_vna.get_channel(1)
        p2 = ch.get_vna_port(2)

        visa.ret = "-2,CPAD"
        (power, rel) = p2.get_source_power_offset()
        assert power == -2 and rel is True
        visa.ret = "5.5, ONLY"
        (power, rel) = p2.get_source_power_offset()
        assert power == 5.5 and rel is False
        visa.ret = "5.5, ON"
        with pytest.raises(AssertionError):
            p2.get_source_power_offset()
        assert visa.cmd == [
            "SOURce1:POWer2:LEVel:IMMediate:OFFSet?"
        ] * 3

        p2.set_source_power_offset(0)
        p2.set_source_power_offset(12.3, relative=False)
        p2.set_source_power_offset(3.45, relative=True)
        assert visa.cmd == [
            "SOURce1:POWer2:LEVel:IMMediate:OFFSet 0, CPAD",
            "SOURce1:POWer2:LEVel:IMMediate:OFFSet 12.3, ONLY",
            "SOURce1:POWer2:LEVel:IMMediate:OFFSet 3.45, CPAD",
        ]


class TestFilesystem:
    import ntpath

    def test_basic_ops(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        fs = dummy_vna.filesystem
        assert fs == dummy_vna.filesystem  # Test that Filesystem instance is memoized
        visa.ret = r"'C:\Users\Public\Documents\Rohde-Schwarz\'"

        fs.getcwd()
        fs.chdir(r"C:\Users\Public")
        assert [r"MMEMory:CDIRectory?",
                r"MMEMory:CDIRectory 'C:\Users\Public'",
                ] == visa.cmd

    def test_directory_defs(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        fs = dummy_vna.filesystem
        visa.ret = self.ntpath.join("C:\\", "Rohde & Schwarz", "Nwa")
        assert fs.default_dir == fs.default_dir
        assert ["MMEMory:CDIRectory?",
                "MMEMory:CDIRectory DEFault",
                "MMEMory:CDIRectory?",
                "MMEMory:CDIRectory 'C:\\Rohde & Schwarz\\Nwa'",
                ] == visa.cmd

        assert fs.calpool_dir == self.ntpath.join(fs.default_dir, "Calibration", "Data")
        assert [] == visa.cmd

    @pytest.mark.parametrize('dir_list',
                             [('77668, 125731287040, cal1.cal,, 38834, cal2.cal,, 38834,',
                               ("cal1.cal", "cal2.cal")),
                              ('0, 125731287040, calibration, <DIR>,, colorschemes, <DIR>,, doc, <DIR>,,',
                               ("calibration", "colorschemes", "doc")),
                              ])
    def test_listdir(self, dir_list, dummy_vna, visa):
        # type: (str, ZNB, VISA) -> None
        visa.ret = r"C:\R&S"
        response, result = dir_list
        visa.ret_dict[r"MMEMory:CATalog? 'C:\R&S'"] = response
        x = dummy_vna.filesystem.listdir()
        assert len(result) == len(x)
        for a, b in zip(x, result):
            assert a.filename == b
        assert [r"MMEMory:CDIRectory?",
                r"MMEMory:CATalog? 'C:\R&S'",
                ] == visa.cmd


class TestSweep(PropertyTester):
    @pytest.fixture
    def sw(self, dummy_vna):
        return dummy_vna.get_channel(2).sweep

    @pytest.fixture
    def seg(self, sw):
        return sw.segments[5]

    @pytest.fixture
    def prop_owner(self, sw):
        return sw

    def test_sweep_dwell(self, dummy_znb, visa):
        # type: (ZNB, VISA) -> None
        """
        This setting is not available on the ZVA
        """
        sw = dummy_znb.get_channel(2).sweep
        sw.dwell_on_each_partial_measurement = True
        sw.dwell_on_each_partial_measurement = False
        visa.ret = "FIRSt"
        assert sw.dwell_on_each_partial_measurement is False
        visa.ret = "ALL"
        assert sw.dwell_on_each_partial_measurement is True
        assert ["SENSe2:SWEep:DWELl:IPOint ALL",
                "SENSe2:SWEep:DWELl:IPOint FIRSt",
                "SENSe2:SWEep:DWELl:IPOint?",
                "SENSe2:SWEep:DWELl:IPOint?",
                ] == visa.cmd

    bool_properties = [
        ("continuous_sweep", "INITiate:CONTinuous", "{:s} {:s}", "{:s}?"),
    ]

    float_properties = [
        ("dwell_time", "SENSe2:SWEep:DWELl", "{:s} {:s}", "{:s}?"),
        ("time",       "SENSe2:SWEep:TIME",  "{:s} {:s}", "{:s}?"),
        ("step_size",  "SENSe2:SWEep:STEP",  "{:s} {:s}", "{:s}?"),
    ]

    int_properties = [
        ("points", "SENSe2:SWEep:POINts", "{:s} {:s}", "{:s}?"),
        ("count", "SENSe2:SWEep:COUNt",   "{:s} {:s}", "{:s}?"),
    ]


class TestSweepSegments:
    @pytest.fixture
    def sw(self, dummy_vna):
        return dummy_vna.get_channel(2).sweep

    @pytest.fixture
    def seg(self, sw):
        return sw.segments[5]

    def test_segments_properties(self, sw, visa):
        # type: (znb.Sweep, VISA) -> None
        sw.TYPE.w(sw.SEGMENT)

        sw.analog_sweep_is_enabled = True
        sw.analog_sweep_is_enabled = False
        sw.use_auto_time = True
        assert ["SENSe2:SWEep:TYPE SEGM",
                "SENSe2:SWEep:GENeration ANALog",
                "SENSe2:SWEep:GENeration STEPped",
                "SENSe2:SWEep:TIME:AUTO ON",
                ] == visa.cmd

    def test_segmented_sweep(self, sw, visa):
        # type: (znb.Sweep, VISA) -> None
        visa.ret = "5"
        assert len(sw.segments) == 5
        assert sw.segments[0].n == 1
        assert len(sw.segments[1:5]) == 4
        assert ["SENSe2:SEGMent:COUNt?",
                "SENSe2:SEGMent:COUNt?",
                ] == visa.cmd

        sw.segments.query_total_sweep_time()
        assert ["SENSe2:SEGMent:SWEep:TIME:SUM?"] == visa.cmd

        for (seg, n) in zip(iter(sw.segments), range(5)):
            assert seg.n == n + 1
        visa.clear_cmd()

    def test_delete(self, sw, visa):
        # type: (znb.Sweep, VISA) -> None
        visa.ret = "5"
        del sw.segments[2]
        del sw.segments[0:5:2]
        assert ["SENSe2:SEGMent3:DELete",
                "SENSe2:SEGMent:COUNt?",
                "SENSe2:SEGMent5:DELete",
                "SENSe2:SEGMent3:DELete",
                "SENSe2:SEGMent1:DELete",
                ] == visa.cmd

        sw.segments.delete_all_segments()
        sw.segments.delete_segment(3)
        assert ["SENSe2:SEGMent:DELete:ALL",
                "SENSe2:SEGMent3:DELete",
                ] == visa.cmd

        seg = sw.segments[5]
        seg.delete()
        assert ["SENSe2:SEGMent6:DELete"] == visa.cmd

    def test_disable_methods(self, sw, visa):
        sw.segments.disable_per_segment_dwell_time()
        sw.segments.disable_per_segment_ifbw()
        sw.segments.disable_per_segment_if_selectivity()
        sw.segments.disable_per_segment_power()
        sw.segments.disable_per_segment_sweep_time()
        assert ["SENSe2:SEGMent:SWEep:DWELl:CONTrol OFF",
                "SENSe2:SEGMent:BWIDth:RESolution:CONTrol OFF",
                "SENSe2:SEGMent:BWIDth:RESolution:SELect:CONTrol OFF",
                "SENSe2:SEGMent:POWer:LEVel:CONTrol OFF",
                "SENSe2:SEGMent:SWEep:TIME:CONTrol OFF",
                ] == visa.cmd

    def test_insert_segment(self, dummy_znb, visa):
        # type: (ZNB, VISA) -> None
        """ANALog sweeps are only supported on the ZNB"""
        sw = dummy_znb.get_channel(2).sweep
        x = sw.segments.insert_segment(1e6, 1e9, points=11, ifbw=1e3, power=-10, position=3)
        assert x.n == 3
        sw.segments.insert_segment(1e6, 1e9, points=11, ifbw=1e3, power=-10, position=3, analog_sweep=True)
        assert ["SENSe2:SEGMent3:INSert 1000000.0, 1000000000.0, 11, -10, AUTO, 0, 1000.0, AUTO, NORMal, STEPped",
                "SENSe2:SEGMent3:INSert 1000000.0, 1000000000.0, 11, -10, AUTO, 0, 1000.0, AUTO, NORMal, ANALog",
                ] == visa.cmd


class TestSweepSegment(PropertyTester):
    @pytest.fixture
    def sw(self, dummy_vna):
        return dummy_vna.get_channel(2).sweep

    @pytest.fixture
    def seg(self, sw):
        return sw.segments[5]

    @pytest.fixture
    def prop_owner(self, seg):
        return seg

    def test_segment_analog_sweep(self, dummy_znb, visa):
        # type: (ZNB, VISA) -> None
        """ANALog sweeps are only supported on the ZNB"""
        seg = dummy_znb.get_channel(2).sweep.segments[5]
        seg.analog_sweep_is_enabled = True
        seg.analog_sweep_is_enabled = False
        assert ["SENSe2:SEGMent6:SWEep:GENeration ANALog",
                "SENSe2:SEGMent6:SWEep:GENeration STEPped",
                ] == visa.cmd

    float_properties = [
        ("dwell_time",  "SENSe2:SEGMent6:SWEep:DWELl",     "{:s} {:s}", "{:s}?"),
        ("freq_start",  "SENSe2:SEGMent6:FREQuency:STARt", "{:s} {:s}", "{:s}?"),
        ("freq_stop",   "SENSe2:SEGMent6:FREQuency:STOP",  "{:s} {:s}", "{:s}?"),
        ("power_level", "SENSe2:SEGMent6:POWer",           "{:s} {:s}", "{:s}?"),
        ("sweep_time",  "SENSe2:SEGMent6:SWEep:TIME",      "{:s} {:s}", "{:s}?"),
    ]

    int_properties = [
        ("if_bandwidth",     "SENSe2:SEGMent6:BWIDth:RESolution", "{:s} {:s}", "{:s}?"),
        ("number_of_points", "SENSe2:SEGMent6:SWEep:POINts",      "{:s} {:s}", "{:s}?"),
    ]

    def test_properties(self, seg, visa):
        visa.ret = "0"
        assert seg.is_enabled is False
        assert seg.if_selectivity == "0"
        assert ["SENSe2:SEGMent6:STATe?",
                "SENSe2:SEGMent6:BWIDth:RESolution:SELect?",
                ] == visa.cmd


def test_diagram(dummy_vna, visa):
    """
    :param ZNB dummy_vna:
    :param VISA visa:
    """
    dia = dummy_vna.get_diagram(1)
    f = dia.save_screenshot("hej.png")
    assert str(f) == "C:\\Rohde & Schwarz\\Nwa\\hej.png"
    assert ["MMEMory:NAME 'hej.png'",
            "HCOPy:DESTination 'MMEM'",
            "HCOPy:DEVice:LANGuage PNG",
            "DISPlay:WINDow1:MAXimize?",
            "DISPlay:WINDow1:MAXimize ON",
            "HCOPy:PAGE:WINDow ACTive",
            "HCOPy:IMMediate",
            "MMEMory:CDIRectory?",
            ] == visa.cmd
    assert dia.is_maximized
    dia.is_maximized = False
    dia.select_diagram()
    assert dia.n == 1
    dia.delete()
    assert dia.name == "1"
    dia.name = "Name2"
    assert dia.title == "1"
    dia.title = "Title2"
    assert dia.title_is_visible is True
    assert ["DISPlay:WINDow1:MAXimize?",
            "DISPlay:WINDow1:MAXimize OFF",
            "DISPlay:WINDow1:MAXimize?",
            "DISPlay:WINDow1:MAXimize ON",
            "DISPlay:WINDow1:STATe OFF",
            "DISPlay:WINDow1:NAME?",
            "DISPlay:WINDow1:NAME 'Name2'",
            "DISPlay:WINDow1:TITLe:DATA?",
            "DISPlay:WINDow1:TITLe:DATA 'Title2'",
            "DISPlay:WINDow1:TITLe:STATe?",
            ] == visa.cmd
    dia.state = True
    dia.state = False
    assert dia.state is True
    assert ["DISPlay:WINDow1:STATe ON",
            "DISPlay:WINDow1:STATe OFF",
            "DISPlay:WINDow1:STATe?",
            ] == visa.cmd


def test_diagram_assigned_traces(dummy_vna, visa):
    """
    :param ZNB dummy_vna:
    :param VISA visa:
    """
    dia = dummy_vna.get_diagram(2)
    traces = []
    for a in range(1, 3):
        for b in range(1, 3):
            n = (a - 1) * 2 + b
            traces.append((n, "S%i%i" % (b, a)))

    visa.ret_dict["DISPlay:WINDow2:TRACe:CATalog?"] = "'1,S11,2,S21,3,S12,4,S22'"
    cnt = 0
    for (tr, (n, name)) in zip(dia.query_assigned_traces(), traces):
        assert tr.name == name
        cnt += 1
    assert cnt == 4
    assert ["DISPlay:WINDow2:TRACe:CATalog?",
            "CONFigure:TRACe:CHANnel:NAME:ID? 'S11'",
            "CONFigure:TRACe:CHANnel:NAME:ID? 'S21'",
            "CONFigure:TRACe:CHANnel:NAME:ID? 'S12'",
            "CONFigure:TRACe:CHANnel:NAME:ID? 'S22'",
            ] == visa.cmd


def test_marker(dummy_vna, visa):
    """
    Test that the Marker class works as expected.

    :param ZNB dummy_vna: This can be either a ZVA or ZNB instance with visa_res = visa dummy.
    :param VISA visa:
    """
    ch = dummy_vna.get_channel(2)
    tr = ch.get_trace("Tr1")
    m1 = tr.get_marker(3)
    assert [] == visa.cmd

    x = m1.tracking
    m1.tracking = False
    assert ["CALCulate2:PARameter:SELect 'Tr1'",
            "CALCulate2:MARKer3:SEARch:TRACking?",
            "CALCulate2:MARKer3:SEARch:TRACking OFF"] == visa.cmd
    assert isinstance(x, bool)

    tr.name = "Tr2"  # Change the trace name to force an "active trace" select
    visa.clear_cmd()
    m1.state = True
    m1.state = False
    assert m1.state is True
    m1.state = "OFF"
    assert visa.cmd == [
        "CALCulate2:PARameter:SELect 'Tr2'",
        "CALCulate2:MARKer3:STATe ON",
        "CALCulate2:MARKer3:STATe OFF",
        "CALCulate2:MARKer3:STATe?",
        "CALCulate2:MARKer3:STATe OFF"]

    m1.x = 3.3
    assert isinstance(m1.x, float)
    assert m1.x == 1.0
    assert visa.cmd == [
        "CALCulate2:MARKer3:X 3.3",
        "CALCulate2:MARKer3:X?",
        "CALCulate2:MARKer3:X?"]

    assert isinstance(m1.y, float)
    assert visa.cmd == ["CALCulate2:MARKer3:Y?"]

    m1.format = "ADM"
    visa.ret = "ADM"
    assert m1.format == "ADM"
    assert visa.cmd == [
        "CALCulate2:MARKer3:FORMat ADM",
        "CALCulate2:MARKer3:FORMat?",
    ]


def test_marker_y_set(dummy_znb, visa):
    # type: (ZNB, VISA) -> None
    m1 = dummy_znb.get_channel(2).get_trace("Tr2").get_marker(3)
    m1.TYPE.w("ARB")
    m1.y = 2
    assert m1.y == 1
    assert ["CALCulate2:MARKer3:TYPE ARB",
            "CALCulate2:PARameter:SELect 'Tr2'",
            "CALCulate2:MARKer3:Y 2",
            "CALCulate2:MARKer3:Y?",
            ] == visa.cmd


class TestTrace(PropertyTester):
    @pytest.fixture
    def tr(self, dummy_vna):
        return dummy_vna.get_channel(2).get_trace("Tr3")

    @pytest.fixture
    def prop_owner(self, tr):
        tr._cmd_cnt = tr.channel.instrument.command_cnt
        return tr

    float_properties = [
        ("scale_per_div",   "DISPlay:WINDow:TRACe:Y:SCALe:PDIVision",   "{:s} {!s}, 'Tr3'", "{:s}?"),
        ("scale_top",       "DISPlay:WINDow:TRACe:Y:SCALe:TOP",         "{:s} {!s}, 'Tr3'", "{:s}?"),
        ("scale_bottom",    "DISPlay:WINDow:TRACe:Y:SCALe:BOTTom",      "{:s} {!s}, 'Tr3'", "{:s}?"),
        ("ref_level",       "DISPlay:WINDow:TRACe:Y:SCALe:RLEVel",      "{:s} {!s}, 'Tr3'", "{:s}?"),
        ("ref_pos",         "DISPlay:WINDow:TRACe:Y:SCALe:RPOSition",   "{:s} {!s}, 'Tr3'", "{:s}?"),
    ]

    class ScaleModel:
        def __init__(self, cmds):
            self.top = 10
            self.bottom = -90
            self._ref_pos = 0.9
            self.parse_scpi_cmds(cmds)

        @property
        def ref_pos(self):
            return self._ref_pos * 100

        @ref_pos.setter
        def ref_pos(self, value):
            scale = self.scale_div
            ref_level = self.ref_level
            self._ref_pos = value / 100
            self.bottom = ref_level - scale * 10 * self._ref_pos
            self.top = self.bottom + scale * 10

        @property
        def scale_div(self):
            return (self.top - self.bottom) / 10

        @scale_div.setter
        def scale_div(self, scale):
            ref_value = self.ref_level
            self.bottom = ref_value - scale * 10 * self._ref_pos
            self.top = self.bottom + scale * 10

        @property
        def ref_level(self):
            return self.bottom + self.scale_div * 10 * self._ref_pos

        @ref_level.setter
        def ref_level(self, value):
            scale = self.scale_div
            self.bottom = value - scale * 10 * self._ref_pos
            self.top = self.bottom + scale * 10

        def assert_params(self, scale_params):
            for attr, expected in scale_params.items():
                actual = getattr(self, attr)
                assert math.isclose(actual, expected), \
                    "Incorrect value for {}, {} (actual) != {} (expected)".format(attr, actual, expected)

        def parse_scpi_cmds(self, cmd_list):
            for cmd in cmd_list:
                if cmd[-1] == "?":
                    continue
                node, args = cmd.split(" ", maxsplit=1)
                leaf = node.split(":")[-1]
                value = float(args.split(",")[0])
                if leaf == "RPOSition":
                    self.ref_pos = value
                elif leaf == "RLEVel":
                    self.ref_level = value
                elif leaf == "PDIVision":
                    self.scale_div = value
                elif leaf == "BOTTom":
                    self.bottom = value
                elif leaf == "TOP":
                    self.top = value
                else:
                    assert False, "Unknown command " + cmd


    def test_trace_format(self, tr, visa):
        # type: (ZNB, VISA) -> None
        visa.ret = "REAL"
        assert tr.trace_format == "REAL"
        tr.trace_format = 2
        assert ["CALCulate2:PARameter:SELect 'Tr3'",
                "CALCulate2:FORMat?",
                "CALCulate2:FORMat 2",
                ] == visa.cmd

    def test_assign_diagram(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        dia = tr.channel.instrument.get_diagram(2)
        tr.assign_diagram(dia)
        assert ["DISPlay:WINDow2:STATe ON",
                "DISPlay:WINDow2:TRACe:EFEed 'Tr3'",
                ] == visa.cmd

    def test_trace_copy(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        tr.copy_data_to_mem("Mem1")
        tr.copy_math_to_mem("MathMem1")
        assert ["TRACe:COPY 'Mem1', 'Tr3'",
                "TRACe:COPY:MATH 'MathMem1', 'Tr3'",
                ] == visa.cmd

        visa.ret = "S11"
        tr_new = tr.copy("NEW_TRACE")
        assert isinstance(tr_new, type(tr))
        assert ["CALCulate2:PARameter:MEASure? 'Tr3'",
                "CALCulate2:PARameter:SDEFine 'NEW_TRACE', 'S11'",
                ] == visa.cmd

        dia = tr.channel.instrument.get_diagram(2)
        tr.copy("Tr2", dia)
        assert ["CALCulate2:PARameter:MEASure? 'Tr3'",
                "CALCulate2:PARameter:SDEFine 'Tr2', 'S11'",
                "DISPlay:WINDow2:STATe ON",
                "DISPlay:WINDow2:TRACe:EFEed 'Tr2'",
                ] == visa.cmd

        tr.copy_assign_math("Math1", "Tr1/Tr2")
        tr.copy_assign_math("Math1", "Tr3/Tr2", dia)
        assert ["CALCulate2:PARameter:MEASure? 'Tr3'",
                "CALCulate2:PARameter:SDEFine 'Math1', 'S11'",
                "CALCulate2:PARameter:SELect 'Math1'",
                "CALCulate2:MATH:EXPRession:SDEFine 'Tr1/Tr2'",
                "CALCulate2:MATH:STATe ON",
                "CALCulate2:PARameter:MEASure? 'Tr3'",
                "CALCulate2:PARameter:SDEFine 'Math1', 'S11'",
                "DISPlay:WINDow2:STATe ON",
                "DISPlay:WINDow2:TRACe:EFEed 'Math1'",
                "CALCulate2:PARameter:SELect 'Math1'",
                "CALCulate2:MATH:EXPRession:SDEFine 'Tr3/Tr2'",
                "CALCulate2:MATH:STATe ON",
                ] == visa.cmd

    def test_trace_id(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        """Test that the trace id is cached, and can't be assigned"""
        visa.ret = "1"
        assert tr.n == 1
        assert tr.n == 1
        with pytest.raises(AttributeError):
            # noinspection PyPropertyAccess
            tr.n = 2
        assert ["CONFigure:TRACe:NAME:ID? 'Tr3'"] == visa.cmd

    def test_cal_state_label(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        """"Test fetching the cal state label"""
        visa.ret = "Cal"
        x = tr.query_cal_state_label()
        assert isinstance(x, str) and x == "Cal"
        assert ["CALCulate2:PARameter:SELect 'Tr3'",
                "SENSe2:CORRection:SSTate?",
                ] == visa.cmd

    def test_is_active(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        visa.ret = "Tr3\r\n"
        assert tr.is_active() is True
        visa.ret = "Tr6\r\n"
        assert not tr.is_active()
        assert ["CALCulate2:PARameter:SELect?",
                "CALCulate2:PARameter:SELect?",
                ] == visa.cmd

    def test_trace_removal(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        tr.delete()
        assert ["CALCulate2:PARameter:DELete 'Tr3'"] == visa.cmd

    def test_trace_name(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        """Test that the trace name attribute works and is cached"""
        assert tr.name == "Tr3"
        tr.name = "Abc[12]"
        tr.name = "[MEM]a"
        assert ["CONFigure:TRACe:REName 'Tr3', 'Abc[12]'",
                "CONFigure:TRACe:REName 'Abc[12]', '[MEM]a'",
                ] == visa.cmd

    @pytest.mark.parametrize("name", [
        "0"  # Leading integer
        "ASD.a",  # "." in name
        "...",  # "." in name
        "09a",  # Leading integer
    ])
    def test_trace_name_validation(self, name, tr, visa):
        with pytest.raises(ValueError):
            tr.channel.get_trace(name)
        with pytest.raises(ValueError):
            tr.name = name
        with pytest.raises(ValueError):
            tr.copy(name)
        with pytest.raises(ValueError):
            tr.copy_data_to_mem(name)
        with pytest.raises(ValueError):
            tr.copy_math_to_mem(name)
        assert [] == visa.cmd

    def test_autoscale(self, tr: znb.Trace, visa: VISA):
        tr.autoscale()
        assert ["DISPlay:WINDow:TRACe:Y:SCALe:AUTO ONCE, 'Tr3'"] == visa.cmd

    @pytest.mark.parametrize("scale_params,expected", [
        ({"scale_div": 1}, ["DISPlay:WINDow:TRACe:Y:SCALe:PDIVision 1, 'Tr3'"]),
        ({"scale_div": 0}, (ValueError, [])),
        ({"top": -30}, ["DISPlay:WINDow:TRACe:Y:SCALe:TOP -30, 'Tr3'"]),
        ({"bottom": -100}, ["DISPlay:WINDow:TRACe:Y:SCALe:BOTTom -100, 'Tr3'"]),
        ({"ref_level": 0.3}, ["DISPlay:WINDow:TRACe:Y:SCALe:RLEVel 0.3, 'Tr3'"]),
        ({"ref_pos": 10}, ["DISPlay:WINDow:TRACe:Y:SCALe:RPOSition 10, 'Tr3'"]),
        ({"ref_pos": 103}, (ValueError, [])),
        ({"top": 10, "bottom": 0}, [
            "DISPlay:WINDow:TRACe:Y:SCALe:TOP?",
            "DISPlay:WINDow:TRACe:Y:SCALe:BOTTom 0, 'Tr3'",
            "DISPlay:WINDow:TRACe:Y:SCALe:TOP 10, 'Tr3'",
        ]),
        ({"top": 20, "bottom": 10}, [  # Reversed top/bottom setting, since bottom > old_top (1)
            "DISPlay:WINDow:TRACe:Y:SCALe:TOP?",
            "DISPlay:WINDow:TRACe:Y:SCALe:TOP 20, 'Tr3'",
            "DISPlay:WINDow:TRACe:Y:SCALe:BOTTom 10, 'Tr3'",
        ]),
        pytest.param({"top": -20, "scale_div": 20}, [
            "DISPlay:WINDow:TRACe:Y:SCALe:TOP -20, 'Tr3'",
            "DISPlay:WINDow:TRACe:Y:SCALe:PDIVision 20, 'Tr3'",
        ], marks=pytest.mark.xfail),  # This case will have to be considered
        ({"top": 0, "bottom": 10}, (ValueError, [])),
        ({"top": 10, "bottom": 0, "scale_div": 5}, (ValueError, [])),
        ({"top": 10, "bottom": 0, "ref_level": -5}, (ValueError, [])),
        ({"top": 10, "bottom": -10, "scale_div": 2, "ref_level": -2, "ref_pos": 40}, [
            "DISPlay:WINDow:TRACe:Y:SCALe:RPOSition 40, 'Tr3'",
            "DISPlay:WINDow:TRACe:Y:SCALe:RLEVel -2, 'Tr3'",
            "DISPlay:WINDow:TRACe:Y:SCALe:PDIVision 2, 'Tr3'",
            "DISPlay:WINDow:TRACe:Y:SCALe:BOTTom -10, 'Tr3'",
            "DISPlay:WINDow:TRACe:Y:SCALe:TOP 10, 'Tr3'",
        ]),
    ])
    def test_set_scaling(self, scale_params, expected, tr: znb.Trace, visa: VISA):
        tr._cmd_cnt = tr.channel.instrument.command_cnt  # don't test trace select all the time
        if not isinstance(expected, tuple):
            tr.set_scaling(**scale_params)
            cmds = visa.cmd
            self.ScaleModel(cmds).assert_params(scale_params)
            assert cmds == expected
        else:
            with pytest.raises(expected[0]):
                tr.set_scaling(**scale_params)
            assert visa.cmd == expected[1]

    def test_trace_measurement(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        meas = tr.measurement
        assert isinstance(meas, str)
        tr.measurement = "S21AVG"
        assert visa.cmd == [
            "CALCulate2:PARameter:MEASure? 'Tr3'",
            "CALCulate2:PARameter:MEASure 'Tr3', 'S21AVG'",
            ]
        tr.measurement = tr.MeasParam.Wave("b", 1, src_port=1, detector="sam")
        assert visa.cmd == ["CALCulate2:PARameter:MEASure 'Tr3', 'B1D1SAM'"]

    def test_meas_param(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        assert str(tr.MeasParam.S(2, 1)) == "S21"
        assert tr.MeasParam.S(2, 1, detector="avg") == "S21AVG"
        with pytest.raises(ValueError, match="The S-parameter detector must be SAM or AVG"):
            tr.MeasParam.S(2, 1, "RMS")
        assert str(tr.MeasParam.Wave("Ap", 2, 2)) == "AP2D2"
        assert str(tr.MeasParam.Wave("B", 2, 1)) == "B2D1"
        assert str(tr.MeasParam.Wave("B", 2, 2, detector="AVG")) == "B2D2AVG"
        assert str(tr.MeasParam.S(dst_port=2, src_port=1)) == "S21"
        assert str(tr.MeasParam.S(dst_port=20, src_port=1)) == "S2001"
        assert str(tr.MeasParam.S(dst_port=20, src_port=1, detector="Avg")) == "S2001AVG"

        assert str(tr.MeasParam.Wave(receiver="a", src_port=300, dst_port=25)) == "A025D300"
        assert str(tr.MeasParam.Wave(receiver="B", src_port=3, dst_port=5, detector="rms")) == "B5D3RMS"

    def test_query_multiple_sweep_data(self, tr: znb.Trace, visa: VISA):

        def expect_complex(stop):
            return map(complex, range(0, stop, 2), range(1, stop + 1, 2))

        # Test ascii response
        visa.ret = ",".join(map(str, range(24)))
        data = tr.query_multiple_sweep_data(1, 3)
        assert len(data) == 3
        assert len(data[0]) == 4
        assert isinstance(data[0][0], complex)
        assert all(map(lambda a, b: a == b, data[0], expect_complex(8)))
        assert visa.cmd == [
            "CALCulate2:PARameter:SELect 'Tr3'",
            "CALCulate2:DATA:NSWeep:FIRSt? SDATa, 1, 3",
        ]

        # Default last_trace
        data = tr.query_multiple_sweep_data(2)
        assert len(data) == 1
        assert len(data[0]) == 12
        assert visa.cmd == [
            "CALCulate2:DATA:NSWeep:FIRSt? SDATa, 2, 2",
        ]

        # Test binary response
        visa.ret = make_ieee_data_block(b"".join(map(lambda x: struct.pack("<f", float(x)), range(48))))
        data = tr.query_multiple_sweep_data(3, 6)
        assert len(data) == 4
        assert len(data[3]) == 6
        assert isinstance(data[0][0], complex)
        assert all(map(lambda a, b: a == b, data[0], expect_complex(4)))
        assert data[3][-1] == complex(46, 47)
        assert visa.cmd == [
            "CALCulate2:DATA:NSWeep:FIRSt? SDATa, 3, 6",
        ]
