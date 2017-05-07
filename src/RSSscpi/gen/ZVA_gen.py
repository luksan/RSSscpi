# -*- coding: utf-8 -*-
# Generated from ZVA_commands_3_70.inp on 2017-05-07 17:36
from RSSscpi.SCPI_gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool
from RSSscpi.Instrument import Instrument


class ZVA_gen(Instrument):
    class CAL(SCPINode, SCPIQuery):
        """
        `*CAL
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments:
        """
        _cmd = "*CAL"
        args = []

    CAL = CAL()
    """
    `*CAL
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments:
    """

    class CLS(SCPINode, SCPISet):
        """
        `*CLS
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments:
        """
        _cmd = "*CLS"
        args = []

    CLS = CLS()
    """
    `*CLS
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments:
    """

    class ESE(SCPINode, SCPIQuery, SCPISet):
        """
        `*ESE
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments: 1
        """
        _cmd = "*ESE"
        args = ["1"]

    ESE = ESE()
    """
    `*ESE
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments: 1
    """

    class ESR(SCPINode, SCPIQuery, SCPISet):
        """
        `*ESR
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments: 1
        """
        _cmd = "*ESR"
        args = ["1"]

    ESR = ESR()
    """
    `*ESR
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments: 1
    """

    class IDN(SCPINode, SCPIQuery):
        """
        `*IDN
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments:
        """
        _cmd = "*IDN"
        args = []

    IDN = IDN()
    """
    `*IDN
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments:
    """

    class IST(SCPINode, SCPIQuery, SCPISet):
        """
        `*IST
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments: 1
        """
        _cmd = "*IST"
        args = ["1"]

    IST = IST()
    """
    `*IST
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments: 1
    """

    class OPC(SCPINode, SCPIQuery, SCPISet):
        """
        `*OPC
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments:
        """
        _cmd = "*OPC"
        args = []

    OPC = OPC()
    """
    `*OPC
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments:
    """

    class OPT(SCPINode, SCPIQuery):
        """
        `*OPT
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments:
        """
        _cmd = "*OPT"
        args = []

    OPT = OPT()
    """
    `*OPT
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments:
    """

    class PCB(SCPINode, SCPISet):
        """
        `*PCB
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments: 1
        """
        _cmd = "*PCB"
        args = ["1"]

    PCB = PCB()
    """
    `*PCB
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments: 1
    """

    class PRE(SCPINode, SCPIQuery, SCPISet):
        """
        `*PRE
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments: 1
        """
        _cmd = "*PRE"
        args = ["1"]

    PRE = PRE()
    """
    `*PRE
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments: 1
    """

    class PSC(SCPINode, SCPIBool):
        """
        `*PSC
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments: 1, OFF, ON
        """
        _cmd = "*PSC"
        args = ["1", "OFF", "ON"]

    PSC = PSC()
    """
    `*PSC
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments: 1, OFF, ON
    """

    class RST(SCPINode, SCPISet):
        """
        `*RST
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments:
        """
        _cmd = "*RST"
        args = []

    RST = RST()
    """
    `*RST
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments:
    """

    class SRE(SCPINode, SCPIQuery, SCPISet):
        """
        `*SRE
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments: 1
        """
        _cmd = "*SRE"
        args = ["1"]

    SRE = SRE()
    """
    `*SRE
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments: 1
    """

    class STB(SCPINode, SCPIQuery):
        """
        `*STB
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments:
        """
        _cmd = "*STB"
        args = []

    STB = STB()
    """
    `*STB
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments:
    """

    class TRG(SCPINode, SCPISet):
        """
        `*TRG
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments:
        """
        _cmd = "*TRG"
        args = []

    TRG = TRG()
    """
    `*TRG
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments:
    """

    class TST(SCPINode, SCPIQuery):
        """
        `*TST
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments:
        """
        _cmd = "*TST"
        args = []

    TST = TST()
    """
    `*TST
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments:
    """

    class WAI(SCPINode, SCPISet):
        """
        `*WAI
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

        Arguments:
        """
        _cmd = "*WAI"
        args = []

    WAI = WAI()
    """
    `*WAI
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/common_commands.htm>`_

    Arguments:
    """

    class DCL(SCPINode, SCPIQuery, SCPISet):
        """
        `@DCL
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_

        Arguments:
        """
        _cmd = "@DCL"
        args = []

    DCL = DCL()
    """
    `@DCL
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_

    Arguments:
    """

    class GET(SCPINode, SCPIQuery, SCPISet):
        """
        `@GET
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_

        Arguments:
        """
        _cmd = "@GET"
        args = []

    GET = GET()
    """
    `@GET
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_

    Arguments:
    """

    class LOC(SCPINode, SCPIQuery, SCPISet):
        """
        `@LOC
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_

        Arguments:
        """
        _cmd = "@LOC"
        args = []

    LOC = LOC()
    """
    `@LOC
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_

    Arguments:
    """

    class REM(SCPINode, SCPIQuery, SCPISet):
        """
        `@REM
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_

        Arguments:
        """
        _cmd = "@REM"
        args = []

    REM = REM()
    """
    `@REM
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_

    Arguments:
    """

    class ABORt(SCPINode, SCPISet):
        """
        `ABORt
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/abort/abort.htm#ABORt>`_

        Arguments:
        """
        _cmd = "ABORt"
        args = []

    ABORt = ABORt()
    """
    `ABORt
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/abort/abort.htm#ABORt>`_

    Arguments:
    """

    class CALCulate(SCPINodeN):
        """
        CALCulate

        Arguments:
        """
        _cmd = "CALCulate"
        args = []

        class CLIMits(SCPINode):
            """
            CALCulate:CLIMits

            Arguments:
            """
            _cmd = "CLIMits"
            args = []

            class FAIL(SCPINode, SCPIQuery):
                """
                `CALCulate:CLIMits:FAIL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_climits.htm#FAIL>`_

                Arguments:
                """
                _cmd = "FAIL"
                args = []

            FAIL = FAIL()
            """
            `CALCulate:CLIMits:FAIL
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_climits.htm#FAIL>`_

            Arguments:
            """

        CLIMits = CLIMits()
        """
        CALCulate:CLIMits

        Arguments:
        """

        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:DATA
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA>`_

            Arguments: FDATa, MDATa, SCORr1, SCORr10, SCORr11, SCORr12, SCORr13, SCORr14, SCORr15, SCORr16, SCORr17, SCORr18, SCORr19, SCORr2, SCORr20, SCORr21, SCORr22, SCORr23, SCORr24, SCORr25, SCORr26, SCORr27, SCORr3, SCORr4, SCORr5, SCORr6, SCORr7, SCORr8, SCORr9, SDATa, TSData
            """
            _cmd = "DATA"
            args = ["FDATa", "MDATa", "SCORr1", "SCORr10", "SCORr11", "SCORr12", "SCORr13", "SCORr14", "SCORr15", "SCORr16", "SCORr17", "SCORr18", "SCORr19", "SCORr2", "SCORr20", "SCORr21", "SCORr22", "SCORr23", "SCORr24", "SCORr25", "SCORr26", "SCORr27", "SCORr3", "SCORr4", "SCORr5", "SCORr6", "SCORr7", "SCORr8", "SCORr9", "SDATa", "TSData"]

            class ALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:ALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA_ALL>`_

                Arguments: FDATa, MDATa, SDATa
                """
                _cmd = "ALL"
                args = ["FDATa", "MDATa", "SDATa"]

            ALL = ALL()
            """
            `CALCulate:DATA:ALL
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA_ALL>`_

            Arguments: FDATa, MDATa, SDATa
            """

            class CALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:CALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA_CALL>`_

                Arguments: FDATa, MDATa, SDATa
                """
                _cmd = "CALL"
                args = ["FDATa", "MDATa", "SDATa"]

                class CATalog(SCPINode, SCPIQuery):
                    """
                    `CALCulate:DATA:CALL:CATalog
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA_CALL_CATalog>`_

                    Arguments:
                    """
                    _cmd = "CATalog"
                    args = []

                CATalog = CATalog()
                """
                `CALCulate:DATA:CALL:CATalog
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA_CALL_CATalog>`_

                Arguments:
                """

            CALL = CALL()
            """
            `CALCulate:DATA:CALL
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA_CALL>`_

            Arguments: FDATa, MDATa, SDATa
            """

            class DALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:DALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA_DALL>`_

                Arguments: FDATa, MDATa, SDATa
                """
                _cmd = "DALL"
                args = ["FDATa", "MDATa", "SDATa"]

            DALL = DALL()
            """
            `CALCulate:DATA:DALL
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA_DALL>`_

            Arguments: FDATa, MDATa, SDATa
            """

            class NSWeep(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:DATA:NSWeep

                Arguments: SDATa
                """
                _cmd = "NSWeep"
                args = ["SDATa"]

                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CALCulate:DATA:NSWeep:COUNt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#NSWeep_COUNt>`_

                    Arguments:
                    """
                    _cmd = "COUNt"
                    args = []

                COUNt = COUNt()
                """
                `CALCulate:DATA:NSWeep:COUNt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#NSWeep_COUNt>`_

                Arguments:
                """

                class FIRSt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:NSWeep:FIRSt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#NSWeep_FIRSt>`_

                    Arguments: SDATa
                    """
                    _cmd = "FIRSt"
                    args = ["SDATa"]

                FIRSt = FIRSt()
                """
                `CALCulate:DATA:NSWeep:FIRSt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#NSWeep_FIRSt>`_

                Arguments: SDATa
                """

                class LAST(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:NSWeep:LAST
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#NSWeep>`_

                    Arguments: SDATa
                    """
                    _cmd = "LAST"
                    args = ["SDATa"]

                LAST = LAST()
                """
                `CALCulate:DATA:NSWeep:LAST
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#NSWeep>`_

                Arguments: SDATa
                """

            NSWeep = NSWeep()
            """
            CALCulate:DATA:NSWeep

            Arguments: SDATa
            """

            class SGRoup(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:SGRoup
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA_SGRoup>`_

                Arguments: FDATa, MDATa, SDATa
                """
                _cmd = "SGRoup"
                args = ["FDATa", "MDATa", "SDATa"]

            SGRoup = SGRoup()
            """
            `CALCulate:DATA:SGRoup
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA_SGRoup>`_

            Arguments: FDATa, MDATa, SDATa
            """

            class STIMulus(SCPINode, SCPIQuery):
                """
                `CALCulate:DATA:STIMulus
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#STIMulus>`_

                Arguments:
                """
                _cmd = "STIMulus"
                args = []

            STIMulus = STIMulus()
            """
            `CALCulate:DATA:STIMulus
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#STIMulus>`_

            Arguments:
            """

        DATA = DATA()
        """
        `CALCulate:DATA
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_data.htm#DATA>`_

        Arguments: FDATa, MDATa, SCORr1, SCORr10, SCORr11, SCORr12, SCORr13, SCORr14, SCORr15, SCORr16, SCORr17, SCORr18, SCORr19, SCORr2, SCORr20, SCORr21, SCORr22, SCORr23, SCORr24, SCORr25, SCORr26, SCORr27, SCORr3, SCORr4, SCORr5, SCORr6, SCORr7, SCORr8, SCORr9, SDATa, TSData
        """

        class DLINe(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:DLINe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_dline.htm#DLINe>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "DLINe"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:DLINe:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_dline.htm#DLINe_STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `CALCulate:DLINe:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_dline.htm#DLINe_STATe>`_

            Arguments: 1, OFF, ON
            """

        DLINe = DLINe()
        """
        `CALCulate:DLINe
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_dline.htm#DLINe>`_

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class FILTer(SCPINode):
            """
            CALCulate:FILTer

            Arguments:
            """
            _cmd = "FILTer"
            args = []

            class GATE(SCPINode):
                """
                CALCulate:FILTer:GATE

                Arguments:
                """
                _cmd = "GATE"
                args = []

                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:FILTer:GATE:TIME

                    Arguments: BPASs, NOTCh
                    """
                    _cmd = "TIME"
                    args = ["BPASs", "NOTCh"]

                    class CENTer(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:CENTer
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#CENTer>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "CENTer"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    CENTer = CENTer()
                    """
                    `CALCulate:FILTer:GATE:TIME:CENTer
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#CENTer>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class DCHebyshev(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:DCHebyshev
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#DCHebyshev>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "DCHebyshev"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    DCHebyshev = DCHebyshev()
                    """
                    `CALCulate:FILTer:GATE:TIME:DCHebyshev
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#DCHebyshev>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:SHAPe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#SHAPe>`_

                        Arguments: MAXimum, MINimum, NORMal, WIDE
                        """
                        _cmd = "SHAPe"
                        args = ["MAXimum", "MINimum", "NORMal", "WIDE"]

                    SHAPe = SHAPe()
                    """
                    `CALCulate:FILTer:GATE:TIME:SHAPe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#SHAPe>`_

                    Arguments: MAXimum, MINimum, NORMal, WIDE
                    """

                    class SHOW(SCPINode, SCPIBool):
                        """
                        `CALCulate:FILTer:GATE:TIME:SHOW
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#SHOW>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "SHOW"
                        args = ["1", "OFF", "ON"]

                    SHOW = SHOW()
                    """
                    `CALCulate:FILTer:GATE:TIME:SHOW
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#SHOW>`_

                    Arguments: 1, OFF, ON
                    """

                    class SPAN(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:SPAN
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#SPAN>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "SPAN"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    SPAN = SPAN()
                    """
                    `CALCulate:FILTer:GATE:TIME:SPAN
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#SPAN>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:STARt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#STARt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STARt = STARt()
                    """
                    `CALCulate:FILTer:GATE:TIME:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#STARt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        `CALCulate:FILTer:GATE:TIME:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `CALCulate:FILTer:GATE:TIME:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#STATe>`_

                    Arguments: 1, OFF, ON
                    """

                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:STOP
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#STOP>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STOP = STOP()
                    """
                    `CALCulate:FILTer:GATE:TIME:STOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#STOP>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class TYPE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:TYPE
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#TYPE>`_

                        Arguments: BPASs, NOTCh
                        """
                        _cmd = "TYPE"
                        args = ["BPASs", "NOTCh"]

                    TYPE = TYPE()
                    """
                    `CALCulate:FILTer:GATE:TIME:TYPE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#TYPE>`_

                    Arguments: BPASs, NOTCh
                    """

                    class WINDow(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:WINDow
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#WINDow>`_

                        Arguments: BOHMan, DCHebyshev, HAMMing, HANNing, RECT
                        """
                        _cmd = "WINDow"
                        args = ["BOHMan", "DCHebyshev", "HAMMing", "HANNing", "RECT"]

                    WINDow = WINDow()
                    """
                    `CALCulate:FILTer:GATE:TIME:WINDow
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_filter.htm#WINDow>`_

                    Arguments: BOHMan, DCHebyshev, HAMMing, HANNing, RECT
                    """

                TIME = TIME()
                """
                CALCulate:FILTer:GATE:TIME

                Arguments: BPASs, NOTCh
                """

            GATE = GATE()
            """
            CALCulate:FILTer:GATE

            Arguments:
            """

        FILTer = FILTer()
        """
        CALCulate:FILTer

        Arguments:
        """

        class FORMat(SCPINode, SCPIQuery, SCPISet):
            """
            CALCulate:FORMat

            Arguments: COMPlex, GDELay, IMAGinary, ISMith, MAGNitude, MLINear, MLOGarithmic, PHASe, POLar, REAL, SMITh, SWR, UPHase
            """
            _cmd = "FORMat"
            args = ["COMPlex", "GDELay", "IMAGinary", "ISMith", "MAGNitude", "MLINear", "MLOGarithmic", "PHASe", "POLar", "REAL", "SMITh", "SWR", "UPHase"]

            class WQUType(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:FORMat:WQUType
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_format.htm#FORMat_WQUType>`_

                Arguments: POWer, VOLTage
                """
                _cmd = "WQUType"
                args = ["POWer", "VOLTage"]

            WQUType = WQUType()
            """
            `CALCulate:FORMat:WQUType
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_format.htm#FORMat_WQUType>`_

            Arguments: POWer, VOLTage
            """

        FORMat = FORMat()
        """
        CALCulate:FORMat

        Arguments: COMPlex, GDELay, IMAGinary, ISMith, MAGNitude, MLINear, MLOGarithmic, PHASe, POLar, REAL, SMITh, SWR, UPHase
        """

        class FSIMulator(SCPINode):
            """
            CALCulate:FSIMulator

            Arguments:
            """
            _cmd = "FSIMulator"
            args = []

            class BALun(SCPINode):
                """
                CALCulate:FSIMulator:BALun

                Arguments:
                """
                _cmd = "BALun"
                args = []

                class DEVice(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:FSIMulator:BALun:DEVice

                    Arguments: SBALanced
                    """
                    _cmd = "DEVice"
                    args = ["SBALanced"]

                DEVice = DEVice()
                """
                CALCulate:FSIMulator:BALun:DEVice

                Arguments: SBALanced
                """

                class DMCircuit(SCPINode):
                    """
                    CALCulate:FSIMulator:BALun:DMCircuit

                    Arguments:
                    """
                    _cmd = "DMCircuit"
                    args = []

                    class BPORt(SCPINodeN):
                        """
                        CALCulate:FSIMulator:BALun:DMCircuit:BPORt

                        Arguments:
                        """
                        _cmd = "BPORt"
                        args = []

                        class PARameters(SCPINode):
                            """
                            CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters

                            Arguments:
                            """
                            _cmd = "PARameters"
                            args = []

                            class C(SCPINode, SCPIQuery, SCPISet):
                                """
                                CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:C

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "C"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            C = C()
                            """
                            CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:C

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                            class L(SCPINode, SCPIQuery, SCPISet):
                                """
                                CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:L

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "L"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            L = L()
                            """
                            CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:L

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                        PARameters = PARameters()
                        """
                        CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters

                        Arguments:
                        """

                    BPORt = BPORt()
                    """
                    CALCulate:FSIMulator:BALun:DMCircuit:BPORt

                    Arguments:
                    """

                DMCircuit = DMCircuit()
                """
                CALCulate:FSIMulator:BALun:DMCircuit

                Arguments:
                """

                class DZConversion(SCPINode):
                    """
                    CALCulate:FSIMulator:BALun:DZConversion

                    Arguments:
                    """
                    _cmd = "DZConversion"
                    args = []

                    class BPORt(SCPINodeN):
                        """
                        CALCulate:FSIMulator:BALun:DZConversion:BPORt

                        Arguments:
                        """
                        _cmd = "BPORt"
                        args = []

                        class ZCOMmon(SCPINode, SCPIQuery, SCPISet):
                            """
                            CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZCOMmon

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "ZCOMmon"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZCOMmon:R

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "R"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            R = R()
                            """
                            CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZCOMmon:R

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                        ZCOMmon = ZCOMmon()
                        """
                        CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZCOMmon

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class ZDIFferent(SCPINode, SCPIQuery, SCPISet):
                            """
                            CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZDIFferent

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "ZDIFferent"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZDIFferent:R

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "R"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            R = R()
                            """
                            CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZDIFferent:R

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                        ZDIFferent = ZDIFferent()
                        """
                        CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZDIFferent

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                    BPORt = BPORt()
                    """
                    CALCulate:FSIMulator:BALun:DZConversion:BPORt

                    Arguments:
                    """

                DZConversion = DZConversion()
                """
                CALCulate:FSIMulator:BALun:DZConversion

                Arguments:
                """

            BALun = BALun()
            """
            CALCulate:FSIMulator:BALun

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                CALCulate:FSIMulator:STATe

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            CALCulate:FSIMulator:STATe

            Arguments: 1, OFF, ON
            """

        FSIMulator = FSIMulator()
        """
        CALCulate:FSIMulator

        Arguments:
        """

        class GDAPerture(SCPINode):
            """
            CALCulate:GDAPerture

            Arguments:
            """
            _cmd = "GDAPerture"
            args = []

            class SCOunt(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:GDAPerture:SCOunt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_gdaperture.htm#SCOunt>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SCOunt"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            SCOunt = SCOunt()
            """
            `CALCulate:GDAPerture:SCOunt
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_gdaperture.htm#SCOunt>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        GDAPerture = GDAPerture()
        """
        CALCulate:GDAPerture

        Arguments:
        """

        class LDEViation(SCPINode):
            """
            CALCulate:LDEViation

            Arguments:
            """
            _cmd = "LDEViation"
            args = []

            class AUTO(SCPINode, SCPISet):
                """
                `CALCulate:LDEViation:AUTO
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ldeviation.htm#AUTO>`_

                Arguments: ONCE
                """
                _cmd = "AUTO"
                args = ["ONCE"]

            AUTO = AUTO()
            """
            `CALCulate:LDEViation:AUTO
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ldeviation.htm#AUTO>`_

            Arguments: ONCE
            """

            class CONStant(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LDEViation:CONStant
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ldeviation.htm#CONStant>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CONStant"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            CONStant = CONStant()
            """
            `CALCulate:LDEViation:CONStant
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ldeviation.htm#CONStant>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class ELENgth(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LDEViation:ELENgth
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ldeviation.htm#ELENgth>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "ELENgth"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            ELENgth = ELENgth()
            """
            `CALCulate:LDEViation:ELENgth
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ldeviation.htm#ELENgth>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class MODE(SCPINode, SCPIBool):
                """
                `CALCulate:LDEViation:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ldeviation.htm#MODE>`_

                Arguments: OFF, ON, TRACking
                """
                _cmd = "MODE"
                args = ["OFF", "ON", "TRACking"]

            MODE = MODE()
            """
            `CALCulate:LDEViation:MODE
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ldeviation.htm#MODE>`_

            Arguments: OFF, ON, TRACking
            """

            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LDEViation:SLOPe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ldeviation.htm#SLOPe>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SLOPe"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            SLOPe = SLOPe()
            """
            `CALCulate:LDEViation:SLOPe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ldeviation.htm#SLOPe>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        LDEViation = LDEViation()
        """
        CALCulate:LDEViation

        Arguments:
        """

        class LIMit(SCPINodeN):
            """
            CALCulate:LIMit

            Arguments:
            """
            _cmd = "LIMit"
            args = []

            class CONTrol(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:CONTrol

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CONTrol"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#CONTrol_DATA>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                DATA = DATA()
                """
                `CALCulate:LIMit:CONTrol:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#CONTrol_DATA>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class DOMain(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:DOMain
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#CONTrol_Domain>`_

                    Arguments: FLIN, FLOG, FSEG, FSINgle, PLIN, PLOG, PSINgle, TLIN, TLOG
                    """
                    _cmd = "DOMain"
                    args = ["FLIN", "FLOG", "FSEG", "FSINgle", "PLIN", "PLOG", "PSINgle", "TLIN", "TLOG"]

                DOMain = DOMain()
                """
                `CALCulate:LIMit:CONTrol:DOMain
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#CONTrol_Domain>`_

                Arguments: FLIN, FLOG, FSEG, FSINgle, PLIN, PLOG, PSINgle, TLIN, TLOG
                """

                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:SHIFt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#CONTrol_SHIFt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SHIFt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                SHIFt = SHIFt()
                """
                `CALCulate:LIMit:CONTrol:SHIFt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#CONTrol_SHIFt>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            CONTrol = CONTrol()
            """
            CALCulate:LIMit:CONTrol

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LIMit:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#DATA>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "DATA"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            DATA = DATA()
            """
            `CALCulate:LIMit:DATA
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#DATA>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class DELete(SCPINode):
                """
                CALCulate:LIMit:DELete

                Arguments:
                """
                _cmd = "DELete"
                args = []

                class ALL(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#DELete_ALL>`_

                    Arguments:
                    """
                    _cmd = "ALL"
                    args = []

                ALL = ALL()
                """
                `CALCulate:LIMit:DELete:ALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#DELete_ALL>`_

                Arguments:
                """

            DELete = DELete()
            """
            CALCulate:LIMit:DELete

            Arguments:
            """

            class DISPlay(SCPINode, SCPIBool):
                """
                CALCulate:LIMit:DISPlay

                Arguments: 1, OFF, ON
                """
                _cmd = "DISPlay"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:DISPlay:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#DISPlay_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:LIMit:DISPlay:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#DISPlay_STATe>`_

                Arguments: 1, OFF, ON
                """

            DISPlay = DISPlay()
            """
            CALCulate:LIMit:DISPlay

            Arguments: 1, OFF, ON
            """

            class FAIL(SCPINode, SCPIQuery):
                """
                `CALCulate:LIMit:FAIL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#FAIL>`_

                Arguments:
                """
                _cmd = "FAIL"
                args = []

            FAIL = FAIL()
            """
            `CALCulate:LIMit:FAIL
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#FAIL>`_

            Arguments:
            """

            class LOWer(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:LOWer

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "LOWer"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#LOWer_DATA>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                DATA = DATA()
                """
                `CALCulate:LIMit:LOWer:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#LOWer_DATA>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class FEED(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:FEED
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#LOWer_FEED>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "FEED"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                FEED = FEED()
                """
                `CALCulate:LIMit:LOWer:FEED
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#LOWer_FEED>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:SHIFt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#LOWer_SHIFt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SHIFt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                SHIFt = SHIFt()
                """
                `CALCulate:LIMit:LOWer:SHIFt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#LOWer_SHIFt>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:LOWer:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#LOWer_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:LIMit:LOWer:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#LOWer_STATe>`_

                Arguments: 1, OFF, ON
                """

            LOWer = LOWer()
            """
            CALCulate:LIMit:LOWer

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class RDOMain(SCPINode):
                """
                CALCulate:LIMit:RDOMain

                Arguments:
                """
                _cmd = "RDOMain"
                args = []

                class COMPlex(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:RDOMain:COMPlex
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#RDOMain_COMPlex>`_

                    Arguments: S, SINV, Y, YREL, Z, ZREL
                    """
                    _cmd = "COMPlex"
                    args = ["S", "SINV", "Y", "YREL", "Z", "ZREL"]

                COMPlex = COMPlex()
                """
                `CALCulate:LIMit:RDOMain:COMPlex
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#RDOMain_COMPlex>`_

                Arguments: S, SINV, Y, YREL, Z, ZREL
                """

                class FORMat(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:RDOMain:FORMat
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#RDOMain_FORMat>`_

                    Arguments: C, COMPlex, GDELay, IMAGinary, L, MAGNitude, PHASe, REAL, SWR
                    """
                    _cmd = "FORMat"
                    args = ["C", "COMPlex", "GDELay", "IMAGinary", "L", "MAGNitude", "PHASe", "REAL", "SWR"]

                FORMat = FORMat()
                """
                `CALCulate:LIMit:RDOMain:FORMat
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#RDOMain_FORMat>`_

                Arguments: C, COMPlex, GDELay, IMAGinary, L, MAGNitude, PHASe, REAL, SWR
                """

                class SPACing(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:RDOMain:SPACing
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#RDOMain_SPACing>`_

                    Arguments: DB, LINear, LOGarithmic, SIC
                    """
                    _cmd = "SPACing"
                    args = ["DB", "LINear", "LOGarithmic", "SIC"]

                SPACing = SPACing()
                """
                `CALCulate:LIMit:RDOMain:SPACing
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#RDOMain_SPACing>`_

                Arguments: DB, LINear, LOGarithmic, SIC
                """

            RDOMain = RDOMain()
            """
            CALCulate:LIMit:RDOMain

            Arguments:
            """

            class SEGMent(SCPINodeN):
                """
                CALCulate:LIMit:SEGMent

                Arguments:
                """
                _cmd = "SEGMent"
                args = []

                class AMPLitude(SCPINode):
                    """
                    CALCulate:LIMit:SEGMent:AMPLitude

                    Arguments:
                    """
                    _cmd = "AMPLitude"
                    args = []

                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:AMPLitude:STARt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_AMPLITUDE_START>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STARt = STARt()
                    """
                    `CALCulate:LIMit:SEGMent:AMPLitude:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_AMPLITUDE_START>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:AMPLitude:STOP
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_AMPLitude_STOP>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STOP = STOP()
                    """
                    `CALCulate:LIMit:SEGMent:AMPLitude:STOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_AMPLitude_STOP>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                AMPLitude = AMPLitude()
                """
                CALCulate:LIMit:SEGMent:AMPLitude

                Arguments:
                """

                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CALCulate:LIMit:SEGMent:COUNt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_COUNt>`_

                    Arguments:
                    """
                    _cmd = "COUNt"
                    args = []

                COUNt = COUNt()
                """
                `CALCulate:LIMit:SEGMent:COUNt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_COUNt>`_

                Arguments:
                """

                class STIMulus(SCPINode):
                    """
                    CALCulate:LIMit:SEGMent:STIMulus

                    Arguments:
                    """
                    _cmd = "STIMulus"
                    args = []

                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:STIMulus:STARt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_STIMulus_STARt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STARt = STARt()
                    """
                    `CALCulate:LIMit:SEGMent:STIMulus:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_STIMulus_STARt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:STIMulus:STOP
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_STIMulus_STOP>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STOP = STOP()
                    """
                    `CALCulate:LIMit:SEGMent:STIMulus:STOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_STIMulus_STOP>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                STIMulus = STIMulus()
                """
                CALCulate:LIMit:SEGMent:STIMulus

                Arguments:
                """

                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:SEGMent:TYPE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_TYPE>`_

                    Arguments: LMAX, LMIN, OFF
                    """
                    _cmd = "TYPE"
                    args = ["LMAX", "LMIN", "OFF"]

                TYPE = TYPE()
                """
                `CALCulate:LIMit:SEGMent:TYPE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SEG_TYPE>`_

                Arguments: LMAX, LMIN, OFF
                """

            SEGMent = SEGMent()
            """
            CALCulate:LIMit:SEGMent

            Arguments:
            """

            class SOUNd(SCPINode, SCPIBool):
                """
                CALCulate:LIMit:SOUNd

                Arguments: 1, OFF, ON
                """
                _cmd = "SOUNd"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:SOUNd:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SOUNd_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:LIMit:SOUNd:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#SOUNd_STATe>`_

                Arguments: 1, OFF, ON
                """

            SOUNd = SOUNd()
            """
            CALCulate:LIMit:SOUNd

            Arguments: 1, OFF, ON
            """

            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:LIMit:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `CALCulate:LIMit:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#STATe>`_

            Arguments: 1, OFF, ON
            """

            class TTLout(SCPINodeN, SCPIBool):
                """
                CALCulate:LIMit:TTLout

                Arguments: 1, OFF, ON
                """
                _cmd = "TTLout"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:TTLout:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#TTLout>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:LIMit:TTLout:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#TTLout>`_

                Arguments: 1, OFF, ON
                """

            TTLout = TTLout()
            """
            CALCulate:LIMit:TTLout

            Arguments: 1, OFF, ON
            """

            class UPPer(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:UPPer

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "UPPer"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#UPPer_DATA>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                DATA = DATA()
                """
                `CALCulate:LIMit:UPPer:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#UPPer_DATA>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class FEED(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:FEED
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#UPPer_FEED>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "FEED"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                FEED = FEED()
                """
                `CALCulate:LIMit:UPPer:FEED
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#UPPer_FEED>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:SHIFt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#UPPer_SHIFt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SHIFt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                SHIFt = SHIFt()
                """
                `CALCulate:LIMit:UPPer:SHIFt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#UPPer_SHIFt>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:UPPer:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#UPPer_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:LIMit:UPPer:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_limit.htm#UPPer_STATe>`_

                Arguments: 1, OFF, ON
                """

            UPPer = UPPer()
            """
            CALCulate:LIMit:UPPer

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        LIMit = LIMit()
        """
        CALCulate:LIMit

        Arguments:
        """

        class MARKer(SCPINodeN, SCPIBool):
            """
            CALCulate:MARKer

            Arguments: 1, OFF, ON
            """
            _cmd = "MARKer"
            args = ["1", "OFF", "ON"]

            class AOFF(SCPINode, SCPISet):
                """
                `CALCulate:MARKer:AOFF
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#AOFF>`_

                Arguments:
                """
                _cmd = "AOFF"
                args = []

            AOFF = AOFF()
            """
            `CALCulate:MARKer:AOFF
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#AOFF>`_

            Arguments:
            """

            class BWIDth(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MARKer:BWIDth

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "BWIDth"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            BWIDth = BWIDth()
            """
            CALCulate:MARKer:BWIDth

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class COUPled(SCPINode, SCPIBool):
                """
                CALCulate:MARKer:COUPled

                Arguments: 1, OFF, ON
                """
                _cmd = "COUPled"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:MARKer:COUPled:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#COUPled_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:MARKer:COUPled:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#COUPled_STATe>`_

                Arguments: 1, OFF, ON
                """

            COUPled = COUPled()
            """
            CALCulate:MARKer:COUPled

            Arguments: 1, OFF, ON
            """

            class DELTa(SCPINode, SCPIBool):
                """
                CALCulate:MARKer:DELTa

                Arguments: 1, OFF, ON
                """
                _cmd = "DELTa"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:MARKer:DELTa:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DELTa_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:MARKer:DELTa:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DELTa_STATe>`_

                Arguments: 1, OFF, ON
                """

            DELTa = DELTa()
            """
            CALCulate:MARKer:DELTa

            Arguments: 1, OFF, ON
            """

            class FORMat(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:FORMat
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#FORMat>`_

                Arguments: ADMittance, COMPlex, DEFault, GDELay, IMAGinary, IMPedance, LINPhase, LOGPhase, MDB, MDPHase, MLINear, MLOGarithmic, MLPHase, PHASe, POLar, REAL, SWR
                """
                _cmd = "FORMat"
                args = ["ADMittance", "COMPlex", "DEFault", "GDELay", "IMAGinary", "IMPedance", "LINPhase", "LOGPhase", "MDB", "MDPHase", "MLINear", "MLOGarithmic", "MLPHase", "PHASe", "POLar", "REAL", "SWR"]

            FORMat = FORMat()
            """
            `CALCulate:MARKer:FORMat
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#FORMat>`_

            Arguments: ADMittance, COMPlex, DEFault, GDELay, IMAGinary, IMPedance, LINPhase, LOGPhase, MDB, MDPHase, MLINear, MLOGarithmic, MLPHase, PHASe, POLar, REAL, SWR
            """

            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MARKer:FUNCtion

                Arguments: BFILter, LPEak, LTARget, MAXimum, MINimum, NPEak, RPEak, RTARget, SPRogress, TARGet
                """
                _cmd = "FUNCtion"
                args = ["BFILter", "LPEak", "LTARget", "MAXimum", "MINimum", "NPEak", "RPEak", "RTARget", "SPRogress", "TARGet"]

                class APEak(SCPINode):
                    """
                    CALCulate:MARKer:FUNCtion:APEak

                    Arguments:
                    """
                    _cmd = "APEak"
                    args = []

                    class EXCursion(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:APEak:EXCursion
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#EXCursion>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "EXCursion"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    EXCursion = EXCursion()
                    """
                    `CALCulate:MARKer:FUNCtion:APEak:EXCursion
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#EXCursion>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class THReshold(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:APEak:THReshold
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#THReshold>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "THReshold"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    THReshold = THReshold()
                    """
                    `CALCulate:MARKer:FUNCtion:APEak:THReshold
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#THReshold>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                APEak = APEak()
                """
                CALCulate:MARKer:FUNCtion:APEak

                Arguments:
                """

                class BWIDth(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:BWIDth
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#BFILter_BWIDth>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "BWIDth"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    class GMCenter(SCPINode, SCPIBool):
                        """
                        `CALCulate:MARKer:FUNCtion:BWIDth:GMCenter
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#BFILTer_GMCenter>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "GMCenter"
                        args = ["1", "OFF", "ON"]

                    GMCenter = GMCenter()
                    """
                    `CALCulate:MARKer:FUNCtion:BWIDth:GMCenter
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#BFILTer_GMCenter>`_

                    Arguments: 1, OFF, ON
                    """

                    class MODE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:BWIDth:MODE
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#BFILTer_MODE>`_

                        Arguments: BPABsolute, BPASs, BPRMarker, BSABsolute, BSRMarker, BSTop
                        """
                        _cmd = "MODE"
                        args = ["BPABsolute", "BPASs", "BPRMarker", "BSABsolute", "BSRMarker", "BSTop"]

                    MODE = MODE()
                    """
                    `CALCulate:MARKer:FUNCtion:BWIDth:MODE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#BFILTer_MODE>`_

                    Arguments: BPABsolute, BPASs, BPRMarker, BSABsolute, BSRMarker, BSTop
                    """

                BWIDth = BWIDth()
                """
                `CALCulate:MARKer:FUNCtion:BWIDth
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#BFILter_BWIDth>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class CENTer(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:CENTer
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#FUNCtion_CENTer>`_

                    Arguments:
                    """
                    _cmd = "CENTer"
                    args = []

                CENTer = CENTer()
                """
                `CALCulate:MARKer:FUNCtion:CENTer
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#FUNCtion_CENTer>`_

                Arguments:
                """

                class DELTa(SCPINode):
                    """
                    CALCulate:MARKer:FUNCtion:DELTa

                    Arguments:
                    """
                    _cmd = "DELTa"
                    args = []

                    class STATe(SCPINode, SCPIBool):
                        """
                        `CALCulate:MARKer:FUNCtion:DELTa:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DELTa_STATe_ZVR>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `CALCulate:MARKer:FUNCtion:DELTa:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DELTa_STATe_ZVR>`_

                    Arguments: 1, OFF, ON
                    """

                DELTa = DELTa()
                """
                CALCulate:MARKer:FUNCtion:DELTa

                Arguments:
                """

                class DOMain(SCPINode):
                    """
                    CALCulate:MARKer:FUNCtion:DOMain

                    Arguments:
                    """
                    _cmd = "DOMain"
                    args = []

                    class USER(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:DOMain:USER
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DOMain_USER>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "USER"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        class SHOW(SCPINode, SCPIBool):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:SHOW
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DOMain_USER_SHOW>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "SHOW"
                            args = ["1", "OFF", "ON"]

                        SHOW = SHOW()
                        """
                        `CALCulate:MARKer:FUNCtion:DOMain:USER:SHOW
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DOMain_USER_SHOW>`_

                        Arguments: 1, OFF, ON
                        """

                        class STARt(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:STARt
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DOMain_USER_STARt>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "STARt"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        STARt = STARt()
                        """
                        `CALCulate:MARKer:FUNCtion:DOMain:USER:STARt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DOMain_USER_STARt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class STOP(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:STOP
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DOMain_USER_STOP>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "STOP"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        STOP = STOP()
                        """
                        `CALCulate:MARKer:FUNCtion:DOMain:USER:STOP
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DOMain_USER_STOP>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                    USER = USER()
                    """
                    `CALCulate:MARKer:FUNCtion:DOMain:USER
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#DOMain_USER>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                DOMain = DOMain()
                """
                CALCulate:MARKer:FUNCtion:DOMain

                Arguments:
                """

                class EXECute(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:EXECute
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#EXECute>`_

                    Arguments: BFILter, LPEak, LTARget, MAXimum, MINimum, NPEak, RPEak, RTARget, SPRogress, TARGet
                    """
                    _cmd = "EXECute"
                    args = ["BFILter", "LPEak", "LTARget", "MAXimum", "MINimum", "NPEak", "RPEak", "RTARget", "SPRogress", "TARGet"]

                EXECute = EXECute()
                """
                `CALCulate:MARKer:FUNCtion:EXECute
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#EXECute>`_

                Arguments: BFILter, LPEak, LTARget, MAXimum, MINimum, NPEak, RPEak, RTARget, SPRogress, TARGet
                """

                class RESult(SCPINode, SCPIQuery):
                    """
                    `CALCulate:MARKer:FUNCtion:RESult
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#RESult>`_

                    Arguments:
                    """
                    _cmd = "RESult"
                    args = []

                RESult = RESult()
                """
                `CALCulate:MARKer:FUNCtion:RESult
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#RESult>`_

                Arguments:
                """

                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:SELect
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SELect>`_

                    Arguments: BFILter, LPEak, LTARget, MAXimum, MINimum, NPEak, RPEak, RTARget, SPRogress, TARGet
                    """
                    _cmd = "SELect"
                    args = ["BFILter", "LPEak", "LTARget", "MAXimum", "MINimum", "NPEak", "RPEak", "RTARget", "SPRogress", "TARGet"]

                SELect = SELect()
                """
                `CALCulate:MARKer:FUNCtion:SELect
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SELect>`_

                Arguments: BFILter, LPEak, LTARget, MAXimum, MINimum, NPEak, RPEak, RTARget, SPRogress, TARGet
                """

                class STARt(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#FUNCTion_STARt>`_

                    Arguments:
                    """
                    _cmd = "STARt"
                    args = []

                STARt = STARt()
                """
                `CALCulate:MARKer:FUNCtion:STARt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#FUNCTion_STARt>`_

                Arguments:
                """

                class STOP(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:STOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#FUNCtion_STOP>`_

                    Arguments:
                    """
                    _cmd = "STOP"
                    args = []

                STOP = STOP()
                """
                `CALCulate:MARKer:FUNCtion:STOP
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#FUNCtion_STOP>`_

                Arguments:
                """

                class TARGet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:TARGet
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#TARGet_ZVR>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TARGet"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                TARGet = TARGet()
                """
                `CALCulate:MARKer:FUNCtion:TARGet
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#TARGet_ZVR>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            FUNCtion = FUNCtion()
            """
            CALCulate:MARKer:FUNCtion

            Arguments: BFILter, LPEak, LTARget, MAXimum, MINimum, NPEak, RPEak, RTARget, SPRogress, TARGet
            """

            class MAXimum(SCPINode, SCPISet):
                """
                `CALCulate:MARKer:MAXimum
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#MAXimum>`_

                Arguments:
                """
                _cmd = "MAXimum"
                args = []

            MAXimum = MAXimum()
            """
            `CALCulate:MARKer:MAXimum
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#MAXimum>`_

            Arguments:
            """

            class MINimum(SCPINode, SCPISet):
                """
                `CALCulate:MARKer:MINimum
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#MINimum>`_

                Arguments:
                """
                _cmd = "MINimum"
                args = []

            MINimum = MINimum()
            """
            `CALCulate:MARKer:MINimum
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#MINimum>`_

            Arguments:
            """

            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#MODE>`_

                Arguments: CONTinuous, DISCrete
                """
                _cmd = "MODE"
                args = ["CONTinuous", "DISCrete"]

            MODE = MODE()
            """
            `CALCulate:MARKer:MODE
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#MODE>`_

            Arguments: CONTinuous, DISCrete
            """

            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:NAME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#NAME>`_

                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]

            NAME = NAME()
            """
            `CALCulate:MARKer:NAME
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#NAME>`_

            Arguments: 'string'
            """

            class REFerence(SCPINode, SCPIBool):
                """
                CALCulate:MARKer:REFerence

                Arguments: 1, OFF, ON
                """
                _cmd = "REFerence"
                args = ["1", "OFF", "ON"]

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:MODE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence_MODE>`_

                    Arguments: CONTinuous, DISCrete
                    """
                    _cmd = "MODE"
                    args = ["CONTinuous", "DISCrete"]

                MODE = MODE()
                """
                `CALCulate:MARKer:REFerence:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence_MODE>`_

                Arguments: CONTinuous, DISCrete
                """

                class NAME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:NAME
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence_NAME>`_

                    Arguments: 'string'
                    """
                    _cmd = "NAME"
                    args = ["'string'"]

                NAME = NAME()
                """
                `CALCulate:MARKer:REFerence:NAME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence_NAME>`_

                Arguments: 'string'
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:MARKer:REFerence:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:MARKer:REFerence:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence>`_

                Arguments: 1, OFF, ON
                """

                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:TYPE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence_TYPE>`_

                    Arguments: FIXed, NORMal
                    """
                    _cmd = "TYPE"
                    args = ["FIXed", "NORMal"]

                TYPE = TYPE()
                """
                `CALCulate:MARKer:REFerence:TYPE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence_TYPE>`_

                Arguments: FIXed, NORMal
                """

                class X(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:X
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence_X>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "X"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                X = X()
                """
                `CALCulate:MARKer:REFerence:X
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence_X>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class Y(SCPINode, SCPIQuery):
                    """
                    `CALCulate:MARKer:REFerence:Y
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence_Y>`_

                    Arguments:
                    """
                    _cmd = "Y"
                    args = []

                Y = Y()
                """
                `CALCulate:MARKer:REFerence:Y
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#REFerence_Y>`_

                Arguments:
                """

            REFerence = REFerence()
            """
            CALCulate:MARKer:REFerence

            Arguments: 1, OFF, ON
            """

            class SEARch(SCPINode, SCPISet):
                """
                CALCulate:MARKer:SEARch

                Arguments:
                """
                _cmd = "SEARch"
                args = []

                class BFILter(SCPINode):
                    """
                    CALCulate:MARKer:SEARch:BFILter

                    Arguments:
                    """
                    _cmd = "BFILter"
                    args = []

                    class RESult(SCPINode, SCPIBool):
                        """
                        CALCulate:MARKer:SEARch:BFILter:RESult

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "RESult"
                        args = ["1", "OFF", "ON"]

                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:MARKer:SEARch:BFILter:RESult:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_BFILter_RESult_STATe>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `CALCulate:MARKer:SEARch:BFILter:RESult:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_BFILter_RESult_STATe>`_

                        Arguments: 1, OFF, ON
                        """

                    RESult = RESult()
                    """
                    CALCulate:MARKer:SEARch:BFILter:RESult

                    Arguments: 1, OFF, ON
                    """

                BFILter = BFILter()
                """
                CALCulate:MARKer:SEARch:BFILter

                Arguments:
                """

                class IMMediate(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:IMMediate
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_IMMediate>`_

                    Arguments:
                    """
                    _cmd = "IMMediate"
                    args = []

                IMMediate = IMMediate()
                """
                `CALCulate:MARKer:SEARch:IMMediate
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_IMMediate>`_

                Arguments:
                """

                class LEFT(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:LEFT
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_LEFT>`_

                    Arguments:
                    """
                    _cmd = "LEFT"
                    args = []

                LEFT = LEFT()
                """
                `CALCulate:MARKer:SEARch:LEFT
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_LEFT>`_

                Arguments:
                """

                class NEXT(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:NEXT
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_NEXT>`_

                    Arguments:
                    """
                    _cmd = "NEXT"
                    args = []

                NEXT = NEXT()
                """
                `CALCulate:MARKer:SEARch:NEXT
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_NEXT>`_

                Arguments:
                """

                class RIGHt(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:RIGHt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_RIGHt>`_

                    Arguments:
                    """
                    _cmd = "RIGHt"
                    args = []

                RIGHt = RIGHt()
                """
                `CALCulate:MARKer:SEARch:RIGHt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_RIGHt>`_

                Arguments:
                """

                class TRACking(SCPINode, SCPIBool):
                    """
                    `CALCulate:MARKer:SEARch:TRACking
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_TRACking>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "TRACking"
                    args = ["1", "OFF", "ON"]

                TRACking = TRACking()
                """
                `CALCulate:MARKer:SEARch:TRACking
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_TRACking>`_

                Arguments: 1, OFF, ON
                """

            SEARch = SEARch()
            """
            CALCulate:MARKer:SEARch

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:MARKer:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `CALCulate:MARKer:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#STATe>`_

            Arguments: 1, OFF, ON
            """

            class TARGet(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MARKer:TARGet

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "TARGet"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            TARGet = TARGet()
            """
            CALCulate:MARKer:TARGet

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:TYPE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#TYPE>`_

                Arguments: FIXed, NORMal
                """
                _cmd = "TYPE"
                args = ["FIXed", "NORMal"]

            TYPE = TYPE()
            """
            `CALCulate:MARKer:TYPE
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#TYPE>`_

            Arguments: FIXed, NORMal
            """

            class X(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:X
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#X>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "X"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            X = X()
            """
            `CALCulate:MARKer:X
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#X>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class Y(SCPINode, SCPIQuery):
                """
                `CALCulate:MARKer:Y
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#Y>`_

                Arguments:
                """
                _cmd = "Y"
                args = []

            Y = Y()
            """
            `CALCulate:MARKer:Y
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#Y>`_

            Arguments:
            """

        MARKer = MARKer()
        """
        CALCulate:MARKer

        Arguments: 1, OFF, ON
        """

        class MATH(SCPINode, SCPIQuery, SCPISet):
            """
            CALCulate:MATH

            Arguments: (expression)
            """
            _cmd = "MATH"
            args = ["(expression)"]

            class EXPRession(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MATH:EXPRession

                Arguments: (expression)
                """
                _cmd = "EXPRession"
                args = ["(expression)"]

                class DEFine(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MATH:EXPRession:DEFine
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#EXPRession_DEFine>`_

                    Arguments: (expression)
                    """
                    _cmd = "DEFine"
                    args = ["(expression)"]

                DEFine = DEFine()
                """
                `CALCulate:MATH:EXPRession:DEFine
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#EXPRession_DEFine>`_

                Arguments: (expression)
                """

                class SDEFine(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MATH:EXPRession:SDEFine
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#EXPRession_SDEFine>`_

                    Arguments: 'string'
                    """
                    _cmd = "SDEFine"
                    args = ["'string'"]

                SDEFine = SDEFine()
                """
                `CALCulate:MATH:EXPRession:SDEFine
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#EXPRession_SDEFine>`_

                Arguments: 'string'
                """

            EXPRession = EXPRession()
            """
            CALCulate:MATH:EXPRession

            Arguments: (expression)
            """

            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MATH:FUNCtion
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#FUNCtion>`_

                Arguments: ADD, DIVide, MULTiply, NORMal, SUBTract
                """
                _cmd = "FUNCtion"
                args = ["ADD", "DIVide", "MULTiply", "NORMal", "SUBTract"]

            FUNCtion = FUNCtion()
            """
            `CALCulate:MATH:FUNCtion
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#FUNCtion>`_

            Arguments: ADD, DIVide, MULTiply, NORMal, SUBTract
            """

            class MEMorize(SCPINode, SCPISet):
                """
                `CALCulate:MATH:MEMorize
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#MEMorize>`_

                Arguments:
                """
                _cmd = "MEMorize"
                args = []

            MEMorize = MEMorize()
            """
            `CALCulate:MATH:MEMorize
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#MEMorize>`_

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:MATH:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `CALCulate:MATH:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#STATe>`_

            Arguments: 1, OFF, ON
            """

            class WUNit(SCPINode, SCPIBool):
                """
                CALCulate:MATH:WUNit

                Arguments: 1, OFF, ON
                """
                _cmd = "WUNit"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:MATH:WUNit:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#WUNit_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:MATH:WUNit:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_math.htm#WUNit_STATe>`_

                Arguments: 1, OFF, ON
                """

            WUNit = WUNit()
            """
            CALCulate:MATH:WUNit

            Arguments: 1, OFF, ON
            """

        MATH = MATH()
        """
        CALCulate:MATH

        Arguments: (expression)
        """

        class PARameter(SCPINode):
            """
            CALCulate:PARameter

            Arguments:
            """
            _cmd = "PARameter"
            args = []

            class CATalog(SCPINode, SCPIQuery):
                """
                `CALCulate:PARameter:CATalog
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#CATalog>`_

                Arguments:
                """
                _cmd = "CATalog"
                args = []

            CATalog = CATalog()
            """
            `CALCulate:PARameter:CATalog
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#CATalog>`_

            Arguments:
            """

            class DEFine(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:DEFine
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DEFine>`_

                Arguments: 'string'
                """
                _cmd = "DEFine"
                args = ["'string'"]

                class SGRoup(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:PARameter:DEFine:SGRoup
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DEFine_SGRoup>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SGRoup"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                SGRoup = SGRoup()
                """
                `CALCulate:PARameter:DEFine:SGRoup
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DEFine_SGRoup>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            DEFine = DEFine()
            """
            `CALCulate:PARameter:DEFine
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DEFine>`_

            Arguments: 'string'
            """

            class DELete(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:DELete
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DELete>`_

                Arguments: 'string'
                """
                _cmd = "DELete"
                args = ["'string'"]

                class ALL(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DELete_ALL>`_

                    Arguments:
                    """
                    _cmd = "ALL"
                    args = []

                ALL = ALL()
                """
                `CALCulate:PARameter:DELete:ALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DELete_ALL>`_

                Arguments:
                """

                class CALL(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:CALL
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DELete_CALL>`_

                    Arguments:
                    """
                    _cmd = "CALL"
                    args = []

                CALL = CALL()
                """
                `CALCulate:PARameter:DELete:CALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DELete_CALL>`_

                Arguments:
                """

                class SGRoup(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:SGRoup
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DELete_SGRoup>`_

                    Arguments:
                    """
                    _cmd = "SGRoup"
                    args = []

                SGRoup = SGRoup()
                """
                `CALCulate:PARameter:DELete:SGRoup
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DELete_SGRoup>`_

                Arguments:
                """

            DELete = DELete()
            """
            `CALCulate:PARameter:DELete
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#DELete>`_

            Arguments: 'string'
            """

            class MEASure(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:PARameter:MEASure
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#MEASure>`_

                Arguments: 'string'
                """
                _cmd = "MEASure"
                args = ["'string'"]

            MEASure = MEASure()
            """
            `CALCulate:PARameter:MEASure
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#MEASure>`_

            Arguments: 'string'
            """

            class NFIGure(SCPINode):
                """
                CALCulate:PARameter:NFIGure

                Arguments:
                """
                _cmd = "NFIGure"
                args = []

                class CSETtings(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:NFIGure:CSETtings
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#NFIGure_CSETtings>`_

                    Arguments: 'string'
                    """
                    _cmd = "CSETtings"
                    args = ["'string'"]

                CSETtings = CSETtings()
                """
                `CALCulate:PARameter:NFIGure:CSETtings
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#NFIGure_CSETtings>`_

                Arguments: 'string'
                """

            NFIGure = NFIGure()
            """
            CALCulate:PARameter:NFIGure

            Arguments:
            """

            class SDEFine(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:SDEFine
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#SDEFine>`_

                Arguments: 'string'
                """
                _cmd = "SDEFine"
                args = ["'string'"]

            SDEFine = SDEFine()
            """
            `CALCulate:PARameter:SDEFine
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#SDEFine>`_

            Arguments: 'string'
            """

            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:PARameter:SELect
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#SELect>`_

                Arguments: 'string'
                """
                _cmd = "SELect"
                args = ["'string'"]

            SELect = SELect()
            """
            `CALCulate:PARameter:SELect
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_parameter.htm#SELect>`_

            Arguments: 'string'
            """

        PARameter = PARameter()
        """
        CALCulate:PARameter

        Arguments:
        """

        class PHOLd(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:PHOLd
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_phold.htm#PHOLd>`_

            Arguments: MAX, MIN, OFF
            """
            _cmd = "PHOLd"
            args = ["MAX", "MIN", "OFF"]

        PHOLd = PHOLd()
        """
        `CALCulate:PHOLd
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_phold.htm#PHOLd>`_

        Arguments: MAX, MIN, OFF
        """

        class RIPPle(SCPINode):
            """
            CALCulate:RIPPle

            Arguments:
            """
            _cmd = "RIPPle"
            args = []

            class CONTrol(SCPINode):
                """
                CALCulate:RIPPle:CONTrol

                Arguments:
                """
                _cmd = "CONTrol"
                args = []

                class DOMain(SCPINode, SCPISet):
                    """
                    `CALCulate:RIPPle:CONTrol:DOMain
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#CONTrol_Domain>`_

                    Arguments: FLIN, FLOG, FSEG, FSINgle, PLIN, PLOG, PSINgle, TLIN, TLOG
                    """
                    _cmd = "DOMain"
                    args = ["FLIN", "FLOG", "FSEG", "FSINgle", "PLIN", "PLOG", "PSINgle", "TLIN", "TLOG"]

                DOMain = DOMain()
                """
                `CALCulate:RIPPle:CONTrol:DOMain
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#CONTrol_Domain>`_

                Arguments: FLIN, FLOG, FSEG, FSINgle, PLIN, PLOG, PSINgle, TLIN, TLOG
                """

            CONTrol = CONTrol()
            """
            CALCulate:RIPPle:CONTrol

            Arguments:
            """

            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:RIPPle:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#DATA>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "DATA"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            DATA = DATA()
            """
            `CALCulate:RIPPle:DATA
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#DATA>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class DELete(SCPINode):
                """
                CALCulate:RIPPle:DELete

                Arguments:
                """
                _cmd = "DELete"
                args = []

                class ALL(SCPINode, SCPISet):
                    """
                    `CALCulate:RIPPle:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#DELete_ALL>`_

                    Arguments:
                    """
                    _cmd = "ALL"
                    args = []

                ALL = ALL()
                """
                `CALCulate:RIPPle:DELete:ALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#DELete_ALL>`_

                Arguments:
                """

            DELete = DELete()
            """
            CALCulate:RIPPle:DELete

            Arguments:
            """

            class DISPlay(SCPINode, SCPIBool):
                """
                CALCulate:RIPPle:DISPlay

                Arguments: 1, OFF, ON
                """
                _cmd = "DISPlay"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:RIPPle:DISPlay:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#DISPlay_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:RIPPle:DISPlay:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#DISPlay_STATe>`_

                Arguments: 1, OFF, ON
                """

            DISPlay = DISPlay()
            """
            CALCulate:RIPPle:DISPlay

            Arguments: 1, OFF, ON
            """

            class FAIL(SCPINode, SCPIQuery):
                """
                `CALCulate:RIPPle:FAIL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#FAIL>`_

                Arguments:
                """
                _cmd = "FAIL"
                args = []

            FAIL = FAIL()
            """
            `CALCulate:RIPPle:FAIL
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#FAIL>`_

            Arguments:
            """

            class RDOMain(SCPINode):
                """
                CALCulate:RIPPle:RDOMain

                Arguments:
                """
                _cmd = "RDOMain"
                args = []

                class FORMat(SCPINode, SCPISet):
                    """
                    `CALCulate:RIPPle:RDOMain:FORMat
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#RDOMain_FORMat>`_

                    Arguments: C, COMPlex, GDELay, IMAGinary, L, MAGNitude, PHASe, REAL, SWR
                    """
                    _cmd = "FORMat"
                    args = ["C", "COMPlex", "GDELay", "IMAGinary", "L", "MAGNitude", "PHASe", "REAL", "SWR"]

                FORMat = FORMat()
                """
                `CALCulate:RIPPle:RDOMain:FORMat
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#RDOMain_FORMat>`_

                Arguments: C, COMPlex, GDELay, IMAGinary, L, MAGNitude, PHASe, REAL, SWR
                """

            RDOMain = RDOMain()
            """
            CALCulate:RIPPle:RDOMain

            Arguments:
            """

            class SEGMent(SCPINodeN, SCPIBool):
                """
                CALCulate:RIPPle:SEGMent

                Arguments: 1, OFF, ON
                """
                _cmd = "SEGMent"
                args = ["1", "OFF", "ON"]

                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CALCulate:RIPPle:SEGMent:COUNt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_COUNt>`_

                    Arguments:
                    """
                    _cmd = "COUNt"
                    args = []

                COUNt = COUNt()
                """
                `CALCulate:RIPPle:SEGMent:COUNt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_COUNt>`_

                Arguments:
                """

                class LIMit(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:SEGMent:LIMit
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_LIMit>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "LIMit"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                LIMit = LIMit()
                """
                `CALCulate:RIPPle:SEGMent:LIMit
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_LIMit>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class RESult(SCPINode, SCPIQuery):
                    """
                    `CALCulate:RIPPle:SEGMent:RESult
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_RESult>`_

                    Arguments:
                    """
                    _cmd = "RESult"
                    args = []

                RESult = RESult()
                """
                `CALCulate:RIPPle:SEGMent:RESult
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_RESult>`_

                Arguments:
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:RIPPle:SEGMent:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:RIPPle:SEGMent:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_STATe>`_

                Arguments: 1, OFF, ON
                """

                class STIMulus(SCPINode):
                    """
                    CALCulate:RIPPle:SEGMent:STIMulus

                    Arguments:
                    """
                    _cmd = "STIMulus"
                    args = []

                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:RIPPle:SEGMent:STIMulus:STARt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_STIMulus_STARt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STARt = STARt()
                    """
                    `CALCulate:RIPPle:SEGMent:STIMulus:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_STIMulus_STARt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:RIPPle:SEGMent:STIMulus:STOP
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_STIMulus_STOP>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STOP = STOP()
                    """
                    `CALCulate:RIPPle:SEGMent:STIMulus:STOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SEG_STIMulus_STOP>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                STIMulus = STIMulus()
                """
                CALCulate:RIPPle:SEGMent:STIMulus

                Arguments:
                """

            SEGMent = SEGMent()
            """
            CALCulate:RIPPle:SEGMent

            Arguments: 1, OFF, ON
            """

            class SOUNd(SCPINode, SCPIBool):
                """
                CALCulate:RIPPle:SOUNd

                Arguments: 1, OFF, ON
                """
                _cmd = "SOUNd"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:RIPPle:SOUNd:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SOUNd_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:RIPPle:SOUNd:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#SOUNd_STATe>`_

                Arguments: 1, OFF, ON
                """

            SOUNd = SOUNd()
            """
            CALCulate:RIPPle:SOUNd

            Arguments: 1, OFF, ON
            """

            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:RIPPle:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `CALCulate:RIPPle:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_ripple.htm#STATe>`_

            Arguments: 1, OFF, ON
            """

        RIPPle = RIPPle()
        """
        CALCulate:RIPPle

        Arguments:
        """

        class SMOothing(SCPINode, SCPIBool):
            """
            CALCulate:SMOothing

            Arguments: 1, OFF, ON
            """
            _cmd = "SMOothing"
            args = ["1", "OFF", "ON"]

            class APERture(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:SMOothing:APERture
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_smoothing.htm#APERture>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "APERture"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            APERture = APERture()
            """
            `CALCulate:SMOothing:APERture
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_smoothing.htm#APERture>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:SMOothing:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_smoothing.htm#STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `CALCulate:SMOothing:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_smoothing.htm#STATe>`_

            Arguments: 1, OFF, ON
            """

        SMOothing = SMOothing()
        """
        CALCulate:SMOothing

        Arguments: 1, OFF, ON
        """

        class STATistics(SCPINode, SCPIBool):
            """
            CALCulate:STATistics

            Arguments: 1, OFF, ON
            """
            _cmd = "STATistics"
            args = ["1", "OFF", "ON"]

            class DOMain(SCPINode):
                """
                CALCulate:STATistics:DOMain

                Arguments:
                """
                _cmd = "DOMain"
                args = []

                class USER(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:STATistics:DOMain:USER
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#USER>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "USER"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    class SHOW(SCPINode, SCPIBool):
                        """
                        `CALCulate:STATistics:DOMain:USER:SHOW
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#USER_SHOW>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "SHOW"
                        args = ["1", "OFF", "ON"]

                    SHOW = SHOW()
                    """
                    `CALCulate:STATistics:DOMain:USER:SHOW
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#USER_SHOW>`_

                    Arguments: 1, OFF, ON
                    """

                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:DOMain:USER:STARt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#USER_STARt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STARt = STARt()
                    """
                    `CALCulate:STATistics:DOMain:USER:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#USER_STARt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:DOMain:USER:STOP
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#USER_STOP>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STOP = STOP()
                    """
                    `CALCulate:STATistics:DOMain:USER:STOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#USER_STOP>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                USER = USER()
                """
                `CALCulate:STATistics:DOMain:USER
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#USER>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            DOMain = DOMain()
            """
            CALCulate:STATistics:DOMain

            Arguments:
            """

            class EPDelay(SCPINode, SCPIBool):
                """
                CALCulate:STATistics:EPDelay

                Arguments: 1, OFF, ON
                """
                _cmd = "EPDelay"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:STATistics:EPDelay:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#EPDelay_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:STATistics:EPDelay:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#EPDelay_STATe>`_

                Arguments: 1, OFF, ON
                """

            EPDelay = EPDelay()
            """
            CALCulate:STATistics:EPDelay

            Arguments: 1, OFF, ON
            """

            class MMPTpeak(SCPINode, SCPIBool):
                """
                CALCulate:STATistics:MMPTpeak

                Arguments: 1, OFF, ON
                """
                _cmd = "MMPTpeak"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:STATistics:MMPTpeak:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#MMPTpeak_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:STATistics:MMPTpeak:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#MMPTpeak_STATe>`_

                Arguments: 1, OFF, ON
                """

            MMPTpeak = MMPTpeak()
            """
            CALCulate:STATistics:MMPTpeak

            Arguments: 1, OFF, ON
            """

            class MSTDdev(SCPINode, SCPIBool):
                """
                CALCulate:STATistics:MSTDdev

                Arguments: 1, OFF, ON
                """
                _cmd = "MSTDdev"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    CALCulate:STATistics:MSTDdev:STATe

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                CALCulate:STATistics:MSTDdev:STATe

                Arguments: 1, OFF, ON
                """

            MSTDdev = MSTDdev()
            """
            CALCulate:STATistics:MSTDdev

            Arguments: 1, OFF, ON
            """

            class NLINear(SCPINode):
                """
                CALCulate:STATistics:NLINear

                Arguments:
                """
                _cmd = "NLINear"
                args = []

                class COMP(SCPINode, SCPIBool):
                    """
                    CALCulate:STATistics:NLINear:COMP

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "COMP"
                    args = ["1", "OFF", "ON"]

                    class LEVel(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:NLINear:COMP:LEVel
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#COMP_LEVel>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "LEVel"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    LEVel = LEVel()
                    """
                    `CALCulate:STATistics:NLINear:COMP:LEVel
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#COMP_LEVel>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class RESult(SCPINode, SCPIQuery):
                        """
                        `CALCulate:STATistics:NLINear:COMP:RESult
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#COMP_RESult>`_

                        Arguments:
                        """
                        _cmd = "RESult"
                        args = []

                    RESult = RESult()
                    """
                    `CALCulate:STATistics:NLINear:COMP:RESult
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#COMP_RESult>`_

                    Arguments:
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        `CALCulate:STATistics:NLINear:COMP:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#COMP_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `CALCulate:STATistics:NLINear:COMP:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#COMP_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                COMP = COMP()
                """
                CALCulate:STATistics:NLINear:COMP

                Arguments: 1, OFF, ON
                """

            NLINear = NLINear()
            """
            CALCulate:STATistics:NLINear

            Arguments:
            """

            class RESult(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:STATistics:RESult
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#RESult>`_

                Arguments: ALL, ELENgth, FLATness, GAIN, MAX, MEAN, MIN, PDELay, PEAK2p, PTPeak, RMS, SLOPe, STDDev
                """
                _cmd = "RESult"
                args = ["ALL", "ELENgth", "FLATness", "GAIN", "MAX", "MEAN", "MIN", "PDELay", "PEAK2p", "PTPeak", "RMS", "SLOPe", "STDDev"]

            RESult = RESult()
            """
            `CALCulate:STATistics:RESult
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#RESult>`_

            Arguments: ALL, ELENgth, FLATness, GAIN, MAX, MEAN, MIN, PDELay, PEAK2p, PTPeak, RMS, SLOPe, STDDev
            """

            class RMS(SCPINode, SCPIBool):
                """
                CALCulate:STATistics:RMS

                Arguments: 1, OFF, ON
                """
                _cmd = "RMS"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:STATistics:RMS:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#RMS_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:STATistics:RMS:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#RMS_STATe>`_

                Arguments: 1, OFF, ON
                """

            RMS = RMS()
            """
            CALCulate:STATistics:RMS

            Arguments: 1, OFF, ON
            """

            class SFLatness(SCPINode, SCPIBool):
                """
                CALCulate:STATistics:SFLatness

                Arguments: 1, OFF, ON
                """
                _cmd = "SFLatness"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:STATistics:SFLatness:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#SFLatness_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:STATistics:SFLatness:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#SFLatness_STATe>`_

                Arguments: 1, OFF, ON
                """

            SFLatness = SFLatness()
            """
            CALCulate:STATistics:SFLatness

            Arguments: 1, OFF, ON
            """

            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:STATistics:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `CALCulate:STATistics:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_statistics.htm#STATe>`_

            Arguments: 1, OFF, ON
            """

        STATistics = STATistics()
        """
        CALCulate:STATistics

        Arguments: 1, OFF, ON
        """

        class TDIF(SCPINode):
            """
            CALCulate:TDIF

            Arguments:
            """
            _cmd = "TDIF"
            args = []

            class IMBalance(SCPINode):
                """
                CALCulate:TDIF:IMBalance

                Arguments:
                """
                _cmd = "IMBalance"
                args = []

                class COMPensation(SCPINode, SCPIBool):
                    """
                    CALCulate:TDIF:IMBalance:COMPensation

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "COMPensation"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `CALCulate:TDIF:IMBalance:COMPensation:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_tdif.htm#IMBalance_COMPensation>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `CALCulate:TDIF:IMBalance:COMPensation:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_tdif.htm#IMBalance_COMPensation>`_

                    Arguments: 1, OFF, ON
                    """

                COMPensation = COMPensation()
                """
                CALCulate:TDIF:IMBalance:COMPensation

                Arguments: 1, OFF, ON
                """

            IMBalance = IMBalance()
            """
            CALCulate:TDIF:IMBalance

            Arguments:
            """

        TDIF = TDIF()
        """
        CALCulate:TDIF

        Arguments:
        """

        class TRANsform(SCPINode):
            """
            CALCulate:TRANsform

            Arguments:
            """
            _cmd = "TRANsform"
            args = []

            class COMPlex(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:TRANsform:COMPlex
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#COMPlex>`_

                Arguments: S, Y, Z
                """
                _cmd = "COMPlex"
                args = ["S", "Y", "Z"]

            COMPlex = COMPlex()
            """
            `CALCulate:TRANsform:COMPlex
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#COMPlex>`_

            Arguments: S, Y, Z
            """

            class IMPedance(SCPINode):
                """
                CALCulate:TRANsform:IMPedance

                Arguments:
                """
                _cmd = "IMPedance"
                args = []

                class RNORmal(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:IMPedance:RNORmal
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#IMPedance_RNORMal>`_

                    Arguments: PWAVes, TWAVes
                    """
                    _cmd = "RNORmal"
                    args = ["PWAVes", "TWAVes"]

                RNORmal = RNORmal()
                """
                `CALCulate:TRANsform:IMPedance:RNORmal
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#IMPedance_RNORMal>`_

                Arguments: PWAVes, TWAVes
                """

            IMPedance = IMPedance()
            """
            CALCulate:TRANsform:IMPedance

            Arguments:
            """

            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:TRANsform:TIME

                Arguments: BPASs, LPASs
                """
                _cmd = "TIME"
                args = ["BPASs", "LPASs"]

                class CENTer(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:CENTer
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#CENTer>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "CENTer"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                CENTer = CENTer()
                """
                `CALCulate:TRANsform:TIME:CENTer
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#CENTer>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class DCHebyshev(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:DCHebyshev
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#DCHebyshev>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DCHebyshev"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                DCHebyshev = DCHebyshev()
                """
                `CALCulate:TRANsform:TIME:DCHebyshev
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#DCHebyshev>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class LPASs(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:LPASs
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#LPASs>`_

                    Arguments: KDFRequency, KFSTop, KSDFrequency
                    """
                    _cmd = "LPASs"
                    args = ["KDFRequency", "KFSTop", "KSDFrequency"]

                    class DCSParam(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:TRANsform:TIME:LPASs:DCSParam
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#LPASs_DCSParam>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "DCSParam"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        class CONTinuous(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:TIME:LPASs:DCSParam:CONTinuous
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#LPASs_DCSParam_CONTinuous>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "CONTinuous"
                            args = ["1", "OFF", "ON"]

                        CONTinuous = CONTinuous()
                        """
                        `CALCulate:TRANsform:TIME:LPASs:DCSParam:CONTinuous
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#LPASs_DCSParam_CONTinuous>`_

                        Arguments: 1, OFF, ON
                        """

                        class EXTRapolate(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:TIME:LPASs:DCSParam:EXTRapolate
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#LPASs_DSCParam_EXTRapolate>`_

                            Arguments:
                            """
                            _cmd = "EXTRapolate"
                            args = []

                        EXTRapolate = EXTRapolate()
                        """
                        `CALCulate:TRANsform:TIME:LPASs:DCSParam:EXTRapolate
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#LPASs_DSCParam_EXTRapolate>`_

                        Arguments:
                        """

                    DCSParam = DCSParam()
                    """
                    `CALCulate:TRANsform:TIME:LPASs:DCSParam
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#LPASs_DCSParam>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                LPASs = LPASs()
                """
                `CALCulate:TRANsform:TIME:LPASs
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#LPASs>`_

                Arguments: KDFRequency, KFSTop, KSDFrequency
                """

                class LPFRequency(SCPINode, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:LPFRequency
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#LPFRequency>`_

                    Arguments:
                    """
                    _cmd = "LPFRequency"
                    args = []

                LPFRequency = LPFRequency()
                """
                `CALCulate:TRANsform:TIME:LPFRequency
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#LPFRequency>`_

                Arguments:
                """

                class METHod(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:TRANsform:TIME:METHod

                    Arguments: CHIRp
                    """
                    _cmd = "METHod"
                    args = ["CHIRp"]

                METHod = METHod()
                """
                CALCulate:TRANsform:TIME:METHod

                Arguments: CHIRp
                """

                class RESolution(SCPINode):
                    """
                    CALCulate:TRANsform:TIME:RESolution

                    Arguments:
                    """
                    _cmd = "RESolution"
                    args = []

                    class EFACtor(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:TRANsform:TIME:RESolution:EFACtor
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#RESolution_EFACtor>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "EFACtor"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    EFACtor = EFACtor()
                    """
                    `CALCulate:TRANsform:TIME:RESolution:EFACtor
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#RESolution_EFACtor>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                RESolution = RESolution()
                """
                CALCulate:TRANsform:TIME:RESolution

                Arguments:
                """

                class SPAN(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:SPAN
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#SPAN>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SPAN"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                SPAN = SPAN()
                """
                `CALCulate:TRANsform:TIME:SPAN
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#SPAN>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#STARt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "STARt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                STARt = STARt()
                """
                `CALCulate:TRANsform:TIME:STARt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#STARt>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:TRANsform:TIME:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `CALCulate:TRANsform:TIME:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#STATe>`_

                Arguments: 1, OFF, ON
                """

                class STIMulus(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STIMulus
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#STIMulus>`_

                    Arguments: IMPulse, STEP
                    """
                    _cmd = "STIMulus"
                    args = ["IMPulse", "STEP"]

                STIMulus = STIMulus()
                """
                `CALCulate:TRANsform:TIME:STIMulus
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#STIMulus>`_

                Arguments: IMPulse, STEP
                """

                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#STOP>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "STOP"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                STOP = STOP()
                """
                `CALCulate:TRANsform:TIME:STOP
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#STOP>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:TYPE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#TYPE>`_

                    Arguments: BPASs, LPASs
                    """
                    _cmd = "TYPE"
                    args = ["BPASs", "LPASs"]

                TYPE = TYPE()
                """
                `CALCulate:TRANsform:TIME:TYPE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#TYPE>`_

                Arguments: BPASs, LPASs
                """

                class WINDow(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:WINDow
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#WINDow>`_

                    Arguments: BOHMan, DCHebyshev, HAMMing, HANNing, RECT
                    """
                    _cmd = "WINDow"
                    args = ["BOHMan", "DCHebyshev", "HAMMing", "HANNing", "RECT"]

                WINDow = WINDow()
                """
                `CALCulate:TRANsform:TIME:WINDow
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#WINDow>`_

                Arguments: BOHMan, DCHebyshev, HAMMing, HANNing, RECT
                """

                class XAXis(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:XAXis
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#XAXis>`_

                    Arguments: DISTance, TIME
                    """
                    _cmd = "XAXis"
                    args = ["DISTance", "TIME"]

                XAXis = XAXis()
                """
                `CALCulate:TRANsform:TIME:XAXis
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform.htm#XAXis>`_

                Arguments: DISTance, TIME
                """

            TIME = TIME()
            """
            CALCulate:TRANsform:TIME

            Arguments: BPASs, LPASs
            """

            class VNETworks(SCPINode):
                """
                CALCulate:TRANsform:VNETworks

                Arguments:
                """
                _cmd = "VNETworks"
                args = []

                class BALanced(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:BALanced

                    Arguments:
                    """
                    _cmd = "BALanced"
                    args = []

                    class DEEMbedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "DEEMbedding"
                        args = ["1", "OFF", "ON"]

                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters

                            Arguments:
                            """
                            _cmd = "PARameters"
                            args = []

                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_PARameters_C>`_

                                Arguments: CSSC, CSSL, LSSC, SCCS, SCLS, SCST, SLCS, STSC
                                """
                                _cmd = "C"
                                args = ["CSSC", "CSSL", "LSSC", "SCCS", "SCLS", "SCST", "SLCS", "STSC"]

                            C = C()
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:C
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_PARameters_C>`_

                            Arguments: CSSC, CSSL, LSSC, SCCS, SCLS, SCST, SLCS, STSC
                            """

                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_PARameters_L>`_

                                Arguments: CSSL, LSSC, LSSL, SCLS, SLCS, SLLS, SLST, STSL
                                """
                                _cmd = "L"
                                args = ["CSSL", "LSSC", "LSSL", "SCLS", "SLCS", "SLLS", "SLST", "STSL"]

                            L = L()
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:L
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_PARameters_L>`_

                            Arguments: CSSL, LSSC, LSSL, SCLS, SLCS, SLLS, SLST, STSL
                            """

                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_PARameters_R>`_

                                Arguments: CSSC, CSSL, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                                """
                                _cmd = "R"
                                args = ["CSSC", "CSSL", "LSSC", "LSSL", "SCCS", "SCLS", "SCST", "SLCS", "SLLS", "SLST", "STSC", "STSL"]

                            R = R()
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:R
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_PARameters_R>`_

                            Arguments: CSSC, CSSL, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                            """

                        PARameters = PARameters()
                        """
                        CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters

                        Arguments:
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_STATe>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_STATe>`_

                        Arguments: 1, OFF, ON
                        """

                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_TNDefinition>`_

                            Arguments: CSSC, CSSL, FIMPort, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSSC", "CSSL", "FIMPort", "LSSC", "LSSL", "SCCS", "SCLS", "SCST", "SLCS", "SLLS", "SLST", "STSC", "STSL"]

                        TNDefinition = TNDefinition()
                        """
                        `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:TNDefinition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_TNDefinition>`_

                        Arguments: CSSC, CSSL, FIMPort, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                        """

                    DEEMbedding = DEEMbedding()
                    """
                    CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding

                    Arguments: 1, OFF, ON
                    """

                    class EMBedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:BALanced:EMBedding

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EMBedding"
                        args = ["1", "OFF", "ON"]

                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters

                            Arguments:
                            """
                            _cmd = "PARameters"
                            args = []

                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_PARameters_C>`_

                                Arguments: CSSC, CSSL, LSSC, SCCS, SCLS, SCST, SLCS, STSC
                                """
                                _cmd = "C"
                                args = ["CSSC", "CSSL", "LSSC", "SCCS", "SCLS", "SCST", "SLCS", "STSC"]

                            C = C()
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:C
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_PARameters_C>`_

                            Arguments: CSSC, CSSL, LSSC, SCCS, SCLS, SCST, SLCS, STSC
                            """

                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_PARameters_L>`_

                                Arguments: CSSL, LSSC, LSSL, SCLS, SLCS, SLLS, SLST, STSL
                                """
                                _cmd = "L"
                                args = ["CSSL", "LSSC", "LSSL", "SCLS", "SLCS", "SLLS", "SLST", "STSL"]

                            L = L()
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:L
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_PARameters_L>`_

                            Arguments: CSSL, LSSC, LSSL, SCLS, SLCS, SLLS, SLST, STSL
                            """

                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_PARameters_R>`_

                                Arguments: CSSC, CSSL, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                                """
                                _cmd = "R"
                                args = ["CSSC", "CSSL", "LSSC", "LSSL", "SCCS", "SCLS", "SCST", "SLCS", "SLLS", "SLST", "STSC", "STSL"]

                            R = R()
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:R
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_PARameters_R>`_

                            Arguments: CSSC, CSSL, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                            """

                        PARameters = PARameters()
                        """
                        CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters

                        Arguments:
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_STATe>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_STATe>`_

                        Arguments: 1, OFF, ON
                        """

                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_TNDefinition>`_

                            Arguments: CSSC, CSSL, FIMPort, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSSC", "CSSL", "FIMPort", "LSSC", "LSSL", "SCCS", "SCLS", "SCST", "SLCS", "SLLS", "SLST", "STSC", "STSL"]

                        TNDefinition = TNDefinition()
                        """
                        `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:TNDefinition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_TNDefinition>`_

                        Arguments: CSSC, CSSL, FIMPort, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                        """

                    EMBedding = EMBedding()
                    """
                    CALCulate:TRANsform:VNETworks:BALanced:EMBedding

                    Arguments: 1, OFF, ON
                    """

                BALanced = BALanced()
                """
                CALCulate:TRANsform:VNETworks:BALanced

                Arguments:
                """

                class GLOop(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:GLOop

                    Arguments:
                    """
                    _cmd = "GLOop"
                    args = []

                    class DEEMbedding(SCPINode, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "DEEMbedding"
                        args = ["1", "OFF", "ON"]

                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters

                            Arguments:
                            """
                            _cmd = "PARameters"
                            args = []

                            class C(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_PARameters_C>`_

                                Arguments: SC
                                """
                                _cmd = "C"
                                args = ["SC"]

                            C = C()
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:C
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_PARameters_C>`_

                            Arguments: SC
                            """

                            class L(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_PARameters_L>`_

                                Arguments: SL
                                """
                                _cmd = "L"
                                args = ["SL"]

                            L = L()
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:L
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_PARameters_L>`_

                            Arguments: SL
                            """

                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_PARameters_R>`_

                                Arguments: SC, SL
                                """
                                _cmd = "R"
                                args = ["SC", "SL"]

                            R = R()
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:R
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_PARameters_R>`_

                            Arguments: SC, SL
                            """

                        PARameters = PARameters()
                        """
                        CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters

                        Arguments:
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_STATe>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_STATe>`_

                        Arguments: 1, OFF, ON
                        """

                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_TNDefinition>`_

                            Arguments: FIMPort, SC, SL
                            """
                            _cmd = "TNDefinition"
                            args = ["FIMPort", "SC", "SL"]

                        TNDefinition = TNDefinition()
                        """
                        `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:TNDefinition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_TNDefinition>`_

                        Arguments: FIMPort, SC, SL
                        """

                    DEEMbedding = DEEMbedding()
                    """
                    CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding

                    Arguments: 1, OFF, ON
                    """

                    class EMBedding(SCPINode, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:GLOop:EMBedding

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EMBedding"
                        args = ["1", "OFF", "ON"]

                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters

                            Arguments:
                            """
                            _cmd = "PARameters"
                            args = []

                            class C(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_PARameters_C>`_

                                Arguments: SC
                                """
                                _cmd = "C"
                                args = ["SC"]

                            C = C()
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:C
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_PARameters_C>`_

                            Arguments: SC
                            """

                            class L(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_PARameters_L>`_

                                Arguments: SL
                                """
                                _cmd = "L"
                                args = ["SL"]

                            L = L()
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:L
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_PARameters_L>`_

                            Arguments: SL
                            """

                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_PARameters_R>`_

                                Arguments: SC, SL
                                """
                                _cmd = "R"
                                args = ["SC", "SL"]

                            R = R()
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:R
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_PARameters_R>`_

                            Arguments: SC, SL
                            """

                        PARameters = PARameters()
                        """
                        CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters

                        Arguments:
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_STATe>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_STATe>`_

                        Arguments: 1, OFF, ON
                        """

                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            CALCulate:TRANsform:VNETworks:GLOop:EMBedding:TNDefinition

                            Arguments: FIMPort, SC, SL
                            """
                            _cmd = "TNDefinition"
                            args = ["FIMPort", "SC", "SL"]

                        TNDefinition = TNDefinition()
                        """
                        CALCulate:TRANsform:VNETworks:GLOop:EMBedding:TNDefinition

                        Arguments: FIMPort, SC, SL
                        """

                    EMBedding = EMBedding()
                    """
                    CALCulate:TRANsform:VNETworks:GLOop:EMBedding

                    Arguments: 1, OFF, ON
                    """

                GLOop = GLOop()
                """
                CALCulate:TRANsform:VNETworks:GLOop

                Arguments:
                """

                class PPAir(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:PPAir

                    Arguments:
                    """
                    _cmd = "PPAir"
                    args = []

                    class DEEMbedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "DEEMbedding"
                        args = ["1", "OFF", "ON"]

                        class DEFine(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:DEFine
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_DEFine>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "DEFine"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        DEFine = DEFine()
                        """
                        `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:DEFine
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_DEFine>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class DELete(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:DELete
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_DELete>`_

                            Arguments:
                            """
                            _cmd = "DELete"
                            args = []

                        DELete = DELete()
                        """
                        `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:DELete
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_DELete>`_

                        Arguments:
                        """

                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters

                            Arguments:
                            """
                            _cmd = "PARameters"
                            args = []

                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_PARameters_C>`_

                                Arguments: CSSC, CSSL, LSSC, SCCS, SCLS, SCST, SLCS, STSC
                                """
                                _cmd = "C"
                                args = ["CSSC", "CSSL", "LSSC", "SCCS", "SCLS", "SCST", "SLCS", "STSC"]

                            C = C()
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:C
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_PARameters_C>`_

                            Arguments: CSSC, CSSL, LSSC, SCCS, SCLS, SCST, SLCS, STSC
                            """

                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_PARameters_L>`_

                                Arguments: CSSL, LSSC, LSSL, SCLS, SLCS, SLLS, SLST, STSL
                                """
                                _cmd = "L"
                                args = ["CSSL", "LSSC", "LSSL", "SCLS", "SLCS", "SLLS", "SLST", "STSL"]

                            L = L()
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:L
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_PARameters_L>`_

                            Arguments: CSSL, LSSC, LSSL, SCLS, SLCS, SLLS, SLST, STSL
                            """

                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_PARameters_R>`_

                                Arguments: CSSC, CSSL, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                                """
                                _cmd = "R"
                                args = ["CSSC", "CSSL", "LSSC", "LSSL", "SCCS", "SCLS", "SCST", "SLCS", "SLLS", "SLST", "STSC", "STSL"]

                            R = R()
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:R
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_PARameters_R>`_

                            Arguments: CSSC, CSSL, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                            """

                        PARameters = PARameters()
                        """
                        CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters

                        Arguments:
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_STATe>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_STATe>`_

                        Arguments: 1, OFF, ON
                        """

                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_TNDefinition>`_

                            Arguments: CSSC, CSSL, FIMPort, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSSC", "CSSL", "FIMPort", "LSSC", "LSSL", "SCCS", "SCLS", "SCST", "SLCS", "SLLS", "SLST", "STSC", "STSL"]

                        TNDefinition = TNDefinition()
                        """
                        `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:TNDefinition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_TNDefinition>`_

                        Arguments: CSSC, CSSL, FIMPort, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                        """

                    DEEMbedding = DEEMbedding()
                    """
                    CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding

                    Arguments: 1, OFF, ON
                    """

                    class EMBedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:PPAir:EMBedding

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EMBedding"
                        args = ["1", "OFF", "ON"]

                        class DEFine(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:DEFine
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_DEFine>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "DEFine"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        DEFine = DEFine()
                        """
                        `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:DEFine
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_DEFine>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class DELete(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:DELete
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_DELete>`_

                            Arguments:
                            """
                            _cmd = "DELete"
                            args = []

                        DELete = DELete()
                        """
                        `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:DELete
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_DELete>`_

                        Arguments:
                        """

                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters

                            Arguments:
                            """
                            _cmd = "PARameters"
                            args = []

                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_PARameters_C>`_

                                Arguments: CSSC, CSSL, LSSC, SCCS, SCLS, SCST, SLCS, STSC
                                """
                                _cmd = "C"
                                args = ["CSSC", "CSSL", "LSSC", "SCCS", "SCLS", "SCST", "SLCS", "STSC"]

                            C = C()
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:C
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_PARameters_C>`_

                            Arguments: CSSC, CSSL, LSSC, SCCS, SCLS, SCST, SLCS, STSC
                            """

                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_PARameters_L>`_

                                Arguments: CSSL, LSSC, LSSL, SCLS, SLCS, SLLS, SLST, STSL
                                """
                                _cmd = "L"
                                args = ["CSSL", "LSSC", "LSSL", "SCLS", "SLCS", "SLLS", "SLST", "STSL"]

                            L = L()
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:L
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_PARameters_L>`_

                            Arguments: CSSL, LSSC, LSSL, SCLS, SLCS, SLLS, SLST, STSL
                            """

                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_PARameters_R>`_

                                Arguments: CSSC, CSSL, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                                """
                                _cmd = "R"
                                args = ["CSSC", "CSSL", "LSSC", "LSSL", "SCCS", "SCLS", "SCST", "SLCS", "SLLS", "SLST", "STSC", "STSL"]

                            R = R()
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:R
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_PARameters_R>`_

                            Arguments: CSSC, CSSL, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                            """

                        PARameters = PARameters()
                        """
                        CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters

                        Arguments:
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_STATe>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_STATe>`_

                        Arguments: 1, OFF, ON
                        """

                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_TNDefinition>`_

                            Arguments: CSSC, CSSL, FIMPort, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSSC", "CSSL", "FIMPort", "LSSC", "LSSL", "SCCS", "SCLS", "SCST", "SLCS", "SLLS", "SLST", "STSC", "STSL"]

                        TNDefinition = TNDefinition()
                        """
                        `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:TNDefinition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_TNDefinition>`_

                        Arguments: CSSC, CSSL, FIMPort, LSSC, LSSL, SCCS, SCLS, SCST, SLCS, SLLS, SLST, STSC, STSL
                        """

                    EMBedding = EMBedding()
                    """
                    CALCulate:TRANsform:VNETworks:PPAir:EMBedding

                    Arguments: 1, OFF, ON
                    """

                PPAir = PPAir()
                """
                CALCulate:TRANsform:VNETworks:PPAir

                Arguments:
                """

                class SENDed(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:SENDed

                    Arguments:
                    """
                    _cmd = "SENDed"
                    args = []

                    class DEEMbedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "DEEMbedding"
                        args = ["1", "OFF", "ON"]

                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters

                            Arguments:
                            """
                            _cmd = "PARameters"
                            args = []

                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_PARameters_C>`_

                                Arguments: CSC, CSL, LSC, SCC, SCL, SLC
                                """
                                _cmd = "C"
                                args = ["CSC", "CSL", "LSC", "SCC", "SCL", "SLC"]

                            C = C()
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:C
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_PARameters_C>`_

                            Arguments: CSC, CSL, LSC, SCC, SCL, SLC
                            """

                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_PARameters_L>`_

                                Arguments: CSL, LSC, LSL, SCL, SLC, SLL
                                """
                                _cmd = "L"
                                args = ["CSL", "LSC", "LSL", "SCL", "SLC", "SLL"]

                            L = L()
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:L
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_PARameters_L>`_

                            Arguments: CSL, LSC, LSL, SCL, SLC, SLL
                            """

                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_PARameters_R>`_

                                Arguments: CSC, CSL, LSC, LSL, SCC, SCL, SLC, SLL
                                """
                                _cmd = "R"
                                args = ["CSC", "CSL", "LSC", "LSL", "SCC", "SCL", "SLC", "SLL"]

                            R = R()
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:R
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_PARameters_R>`_

                            Arguments: CSC, CSL, LSC, LSL, SCC, SCL, SLC, SLL
                            """

                        PARameters = PARameters()
                        """
                        CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters

                        Arguments:
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_STATe>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_STATe>`_

                        Arguments: 1, OFF, ON
                        """

                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_TNDefinition>`_

                            Arguments: CSC, CSL, FIMPort, LSC, LSL, SCC, SCL, SLC, SLL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSC", "CSL", "FIMPort", "LSC", "LSL", "SCC", "SCL", "SLC", "SLL"]

                        TNDefinition = TNDefinition()
                        """
                        `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:TNDefinition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_TNDefinition>`_

                        Arguments: CSC, CSL, FIMPort, LSC, LSL, SCC, SCL, SLC, SLL
                        """

                    DEEMbedding = DEEMbedding()
                    """
                    CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding

                    Arguments: 1, OFF, ON
                    """

                    class EMBedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:SENDed:EMBedding

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EMBedding"
                        args = ["1", "OFF", "ON"]

                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters

                            Arguments:
                            """
                            _cmd = "PARameters"
                            args = []

                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_PARameters_C>`_

                                Arguments: CSC, CSL, LSC, SCC, SCL, SLC
                                """
                                _cmd = "C"
                                args = ["CSC", "CSL", "LSC", "SCC", "SCL", "SLC"]

                            C = C()
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:C
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_PARameters_C>`_

                            Arguments: CSC, CSL, LSC, SCC, SCL, SLC
                            """

                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_PARameters_L>`_

                                Arguments: CSL, LSC, LSL, SCL, SLC, SLL
                                """
                                _cmd = "L"
                                args = ["CSL", "LSC", "LSL", "SCL", "SLC", "SLL"]

                            L = L()
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:L
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_PARameters_L>`_

                            Arguments: CSL, LSC, LSL, SCL, SLC, SLL
                            """

                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_PARameters_R>`_

                                Arguments: CSC, CSL, LSC, LSL, SCC, SCL, SLC, SLL
                                """
                                _cmd = "R"
                                args = ["CSC", "CSL", "LSC", "LSL", "SCC", "SCL", "SLC", "SLL"]

                            R = R()
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:R
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_PARameters_R>`_

                            Arguments: CSC, CSL, LSC, LSL, SCC, SCL, SLC, SLL
                            """

                        PARameters = PARameters()
                        """
                        CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters

                        Arguments:
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_STATe>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_STATe>`_

                        Arguments: 1, OFF, ON
                        """

                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_TNDefinition>`_

                            Arguments: CSC, CSL, FIMPort, LSC, LSL, SCC, SCL, SLC, SLL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSC", "CSL", "FIMPort", "LSC", "LSL", "SCC", "SCL", "SLC", "SLL"]

                        TNDefinition = TNDefinition()
                        """
                        `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:TNDefinition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_TNDefinition>`_

                        Arguments: CSC, CSL, FIMPort, LSC, LSL, SCC, SCL, SLC, SLL
                        """

                    EMBedding = EMBedding()
                    """
                    CALCulate:TRANsform:VNETworks:SENDed:EMBedding

                    Arguments: 1, OFF, ON
                    """

                SENDed = SENDed()
                """
                CALCulate:TRANsform:VNETworks:SENDed

                Arguments:
                """

            VNETworks = VNETworks()
            """
            CALCulate:TRANsform:VNETworks

            Arguments:
            """

        TRANsform = TRANsform()
        """
        CALCulate:TRANsform

        Arguments:
        """

    CALCulate = CALCulate()
    """
    CALCulate

    Arguments:
    """

    class CONFigure(SCPINode):
        """
        CONFigure

        Arguments:
        """
        _cmd = "CONFigure"
        args = []

        class CHANnel(SCPINodeN, SCPIBool):
            """
            CONFigure:CHANnel

            Arguments: 1, OFF, ON
            """
            _cmd = "CHANnel"
            args = ["1", "OFF", "ON"]

            class CATalog(SCPINode, SCPIQuery):
                """
                `CONFigure:CHANnel:CATalog
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#CATalog>`_

                Arguments:
                """
                _cmd = "CATalog"
                args = []

            CATalog = CATalog()
            """
            `CONFigure:CHANnel:CATalog
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#CATalog>`_

            Arguments:
            """

            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:CHANnel:NAME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#NAME>`_

                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]

                class ID(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:CHANnel:NAME:ID
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#NAME_ID>`_

                    Arguments: 'string'
                    """
                    _cmd = "ID"
                    args = ["'string'"]

                ID = ID()
                """
                `CONFigure:CHANnel:NAME:ID
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#NAME_ID>`_

                Arguments: 'string'
                """

            NAME = NAME()
            """
            `CONFigure:CHANnel:NAME
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#NAME>`_

            Arguments: 'string'
            """

            class STATe(SCPINode, SCPIBool):
                """
                `CONFigure:CHANnel:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `CONFigure:CHANnel:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#STATe>`_

            Arguments: 1, OFF, ON
            """

            class TRACe(SCPINode):
                """
                CONFigure:CHANnel:TRACe

                Arguments:
                """
                _cmd = "TRACe"
                args = []

                class REName(SCPINode, SCPISet):
                    """
                    `CONFigure:CHANnel:TRACe:REName
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#Channel_Trace_Rename>`_

                    Arguments: 'string'
                    """
                    _cmd = "REName"
                    args = ["'string'"]

                REName = REName()
                """
                `CONFigure:CHANnel:TRACe:REName
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#Channel_Trace_Rename>`_

                Arguments: 'string'
                """

            TRACe = TRACe()
            """
            CONFigure:CHANnel:TRACe

            Arguments:
            """

        CHANnel = CHANnel()
        """
        CONFigure:CHANnel

        Arguments: 1, OFF, ON
        """

        class TRACe(SCPINodeN):
            """
            CONFigure:TRACe

            Arguments:
            """
            _cmd = "TRACe"
            args = []

            class CATalog(SCPINode, SCPIQuery):
                """
                `CONFigure:TRACe:CATalog
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_CATalog_>`_

                Arguments:
                """
                _cmd = "CATalog"
                args = []

            CATalog = CATalog()
            """
            `CONFigure:TRACe:CATalog
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_CATalog_>`_

            Arguments:
            """

            class CHANnel(SCPINode):
                """
                CONFigure:TRACe:CHANnel

                Arguments:
                """
                _cmd = "CHANnel"
                args = []

                class NAME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:TRACe:CHANnel:NAME
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_CHANnel_NAME>`_

                    Arguments: 'string'
                    """
                    _cmd = "NAME"
                    args = ["'string'"]

                    class ID(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONFigure:TRACe:CHANnel:NAME:ID
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_CHANnel_ID>`_

                        Arguments: 'string'
                        """
                        _cmd = "ID"
                        args = ["'string'"]

                    ID = ID()
                    """
                    `CONFigure:TRACe:CHANnel:NAME:ID
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_CHANnel_ID>`_

                    Arguments: 'string'
                    """

                NAME = NAME()
                """
                `CONFigure:TRACe:CHANnel:NAME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_CHANnel_NAME>`_

                Arguments: 'string'
                """

            CHANnel = CHANnel()
            """
            CONFigure:TRACe:CHANnel

            Arguments:
            """

            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:TRACe:NAME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_NAME>`_

                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]

                class ID(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:TRACe:NAME:ID
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_NAME_ID>`_

                    Arguments: 'string'
                    """
                    _cmd = "ID"
                    args = ["'string'"]

                ID = ID()
                """
                `CONFigure:TRACe:NAME:ID
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_NAME_ID>`_

                Arguments: 'string'
                """

            NAME = NAME()
            """
            `CONFigure:TRACe:NAME
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_NAME>`_

            Arguments: 'string'
            """

            class REName(SCPINode, SCPISet):
                """
                `CONFigure:TRACe:REName
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_REName>`_

                Arguments: 'string'
                """
                _cmd = "REName"
                args = ["'string'"]

            REName = REName()
            """
            `CONFigure:TRACe:REName
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/configure/configure.htm#TRACe_REName>`_

            Arguments: 'string'
            """

        TRACe = TRACe()
        """
        CONFigure:TRACe

        Arguments:
        """

    CONFigure = CONFigure()
    """
    CONFigure

    Arguments:
    """

    class CONTrol(SCPINode):
        """
        CONTrol

        Arguments:
        """
        _cmd = "CONTrol"
        args = []

        class AUXiliary(SCPINode):
            """
            CONTrol:AUXiliary

            Arguments:
            """
            _cmd = "AUXiliary"
            args = []

            class A(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:AUXiliary:A

                Arguments: 1
                """
                _cmd = "A"
                args = ["1"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:AUXiliary:A:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control.htm#A_B_DATA>`_

                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]

                DATA = DATA()
                """
                `CONTrol:AUXiliary:A:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control.htm#A_B_DATA>`_

                Arguments: 1
                """

            A = A()
            """
            CONTrol:AUXiliary:A

            Arguments: 1
            """

            class B(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:AUXiliary:B

                Arguments: 1
                """
                _cmd = "B"
                args = ["1"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:AUXiliary:B:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control.htm#A_B_DATA>`_

                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]

                DATA = DATA()
                """
                `CONTrol:AUXiliary:B:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control.htm#A_B_DATA>`_

                Arguments: 1
                """

            B = B()
            """
            CONTrol:AUXiliary:B

            Arguments: 1
            """

            class C(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:AUXiliary:C

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "C"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:AUXiliary:C:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control.htm#DATA>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                DATA = DATA()
                """
                `CONTrol:AUXiliary:C:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control.htm#DATA>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            C = C()
            """
            CONTrol:AUXiliary:C

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        AUXiliary = AUXiliary()
        """
        CONTrol:AUXiliary

        Arguments:
        """

        class HANDler(SCPINode):
            """
            CONTrol:HANDler

            Arguments:
            """
            _cmd = "HANDler"
            args = []

            class A(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:A

                Arguments: 1
                """
                _cmd = "A"
                args = ["1"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:A:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]

                DATA = DATA()
                """
                `CONTrol:HANDler:A:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                Arguments: 1
                """

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:A:MODE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_MODE>`_

                    Arguments: INPut, OUTPut
                    """
                    _cmd = "MODE"
                    args = ["INPut", "OUTPut"]

                MODE = MODE()
                """
                `CONTrol:HANDler:A:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_MODE>`_

                Arguments: INPut, OUTPut
                """

            A = A()
            """
            CONTrol:HANDler:A

            Arguments: 1
            """

            class B(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:B

                Arguments: 1
                """
                _cmd = "B"
                args = ["1"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:B:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]

                DATA = DATA()
                """
                `CONTrol:HANDler:B:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                Arguments: 1
                """

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:B:MODE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_MODE>`_

                    Arguments: INPut, OUTPut
                    """
                    _cmd = "MODE"
                    args = ["INPut", "OUTPut"]

                MODE = MODE()
                """
                `CONTrol:HANDler:B:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_MODE>`_

                Arguments: INPut, OUTPut
                """

            B = B()
            """
            CONTrol:HANDler:B

            Arguments: 1
            """

            class C(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:C

                Arguments: 1
                """
                _cmd = "C"
                args = ["1"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:C:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]

                DATA = DATA()
                """
                `CONTrol:HANDler:C:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                Arguments: 1
                """

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:C:MODE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_MODE>`_

                    Arguments: INPut, OUTPut
                    """
                    _cmd = "MODE"
                    args = ["INPut", "OUTPut"]

                MODE = MODE()
                """
                `CONTrol:HANDler:C:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_MODE>`_

                Arguments: INPut, OUTPut
                """

            C = C()
            """
            CONTrol:HANDler:C

            Arguments: 1
            """

            class D(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:D

                Arguments: 1
                """
                _cmd = "D"
                args = ["1"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:D:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]

                DATA = DATA()
                """
                `CONTrol:HANDler:D:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                Arguments: 1
                """

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:D:MODE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_MODE>`_

                    Arguments: INPut, OUTPut
                    """
                    _cmd = "MODE"
                    args = ["INPut", "OUTPut"]

                MODE = MODE()
                """
                `CONTrol:HANDler:D:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_MODE>`_

                Arguments: INPut, OUTPut
                """

            D = D()
            """
            CONTrol:HANDler:D

            Arguments: 1
            """

            class E(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:E

                Arguments: 1
                """
                _cmd = "E"
                args = ["1"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:E:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]

                DATA = DATA()
                """
                `CONTrol:HANDler:E:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                Arguments: 1
                """

            E = E()
            """
            CONTrol:HANDler:E

            Arguments: 1
            """

            class EXTension(SCPINode):
                """
                CONTrol:HANDler:EXTension

                Arguments:
                """
                _cmd = "EXTension"
                args = []

                class INDex(SCPINode):
                    """
                    CONTrol:HANDler:EXTension:INDex

                    Arguments:
                    """
                    _cmd = "INDex"
                    args = []

                    class STATe(SCPINode, SCPIBool):
                        """
                        `CONTrol:HANDler:EXTension:INDex:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#EXTension_INDEX_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `CONTrol:HANDler:EXTension:INDex:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#EXTension_INDEX_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                INDex = INDex()
                """
                CONTrol:HANDler:EXTension:INDex

                Arguments:
                """

                class RTRigger(SCPINode):
                    """
                    CONTrol:HANDler:EXTension:RTRigger

                    Arguments:
                    """
                    _cmd = "RTRigger"
                    args = []

                    class STATe(SCPINode, SCPIBool):
                        """
                        `CONTrol:HANDler:EXTension:RTRigger:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#EXTension_RTRigger_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `CONTrol:HANDler:EXTension:RTRigger:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#EXTension_RTRigger_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                RTRigger = RTRigger()
                """
                CONTrol:HANDler:EXTension:RTRigger

                Arguments:
                """

            EXTension = EXTension()
            """
            CONTrol:HANDler:EXTension

            Arguments:
            """

            class F(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:F

                Arguments: 1
                """
                _cmd = "F"
                args = ["1"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:F:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]

                DATA = DATA()
                """
                `CONTrol:HANDler:F:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#A_DATA>`_

                Arguments: 1
                """

            F = F()
            """
            CONTrol:HANDler:F

            Arguments: 1
            """

            class OUTPut(SCPINodeN, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:OUTPut

                Arguments: 1
                """
                _cmd = "OUTPut"
                args = ["1"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:OUTPut:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#OUTPut_DATA>`_

                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]

                DATA = DATA()
                """
                `CONTrol:HANDler:OUTPut:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#OUTPut_DATA>`_

                Arguments: 1
                """

                class USER(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:OUTPut:USER
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#OUTPut_USER>`_

                    Arguments: 1
                    """
                    _cmd = "USER"
                    args = ["1"]

                USER = USER()
                """
                `CONTrol:HANDler:OUTPut:USER
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#OUTPut_USER>`_

                Arguments: 1
                """

            OUTPut = OUTPut()
            """
            CONTrol:HANDler:OUTPut

            Arguments: 1
            """

            class RESet(SCPINode, SCPISet):
                """
                `CONTrol:HANDler:RESet
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#RESet>`_

                Arguments:
                """
                _cmd = "RESet"
                args = []

            RESet = RESet()
            """
            `CONTrol:HANDler:RESet
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/control/control_handler.htm#RESet>`_

            Arguments:
            """

        HANDler = HANDler()
        """
        CONTrol:HANDler

        Arguments:
        """

    CONTrol = CONTrol()
    """
    CONTrol

    Arguments:
    """

    class DIAGnostic(SCPINode):
        """
        DIAGnostic

        Arguments:
        """
        _cmd = "DIAGnostic"
        args = []

        class ALC(SCPINode):
            """
            DIAGnostic:ALC

            Arguments:
            """
            _cmd = "ALC"
            args = []

            class AUBW(SCPINode, SCPIBool):
                """
                `DIAGnostic:ALC:AUBW
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_AUBW>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "AUBW"
                args = ["1", "OFF", "ON"]

            AUBW = AUBW()
            """
            `DIAGnostic:ALC:AUBW
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_AUBW>`_

            Arguments: 1, OFF, ON
            """

            class BW(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:BW
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_BW>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "BW"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            BW = BW()
            """
            `DIAGnostic:ALC:BW
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_BW>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class CLAMp(SCPINode, SCPIBool):
                """
                `DIAGnostic:ALC:CLAMp
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_CLAMp>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "CLAMp"
                args = ["1", "OFF", "ON"]

            CLAMp = CLAMp()
            """
            `DIAGnostic:ALC:CLAMp
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_CLAMp>`_

            Arguments: 1, OFF, ON
            """

            class DMODe(SCPINode):
                """
                DIAGnostic:ALC:DMODe

                Arguments:
                """
                _cmd = "DMODe"
                args = []

                class MSTimulus(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:ALC:DMODe:MSTimulus

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "MSTimulus"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                MSTimulus = MSTimulus()
                """
                DIAGnostic:ALC:DMODe:MSTimulus

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class POINts(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:ALC:DMODe:POINts

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "POINts"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                POINts = POINts()
                """
                DIAGnostic:ALC:DMODe:POINts

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class RTIMe(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:ALC:DMODe:RTIMe

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RTIMe"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                RTIMe = RTIMe()
                """
                DIAGnostic:ALC:DMODe:RTIMe

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            DMODe = DMODe()
            """
            DIAGnostic:ALC:DMODe

            Arguments:
            """

            class PIParameter(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:PIParameter
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_PIParameter>`_

                Arguments: AUTO, MANual
                """
                _cmd = "PIParameter"
                args = ["AUTO", "MANual"]

                class GAIN(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DIAGnostic:ALC:PIParameter:GAIN
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_PIParameter_GAIN>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "GAIN"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                GAIN = GAIN()
                """
                `DIAGnostic:ALC:PIParameter:GAIN
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_PIParameter_GAIN>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class ITIMe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DIAGnostic:ALC:PIParameter:ITIMe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_PIParameter_ITIMe>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "ITIMe"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                ITIMe = ITIMe()
                """
                `DIAGnostic:ALC:PIParameter:ITIMe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_PIParameter_ITIMe>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            PIParameter = PIParameter()
            """
            `DIAGnostic:ALC:PIParameter
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_PIParameter>`_

            Arguments: AUTO, MANual
            """

            class POFFset(SCPINode, SCPIBool):
                """
                `DIAGnostic:ALC:POFFset
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_POFFset>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "POFFset"
                args = ["1", "OFF", "ON"]

            POFFset = POFFset()
            """
            `DIAGnostic:ALC:POFFset
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_POFFset>`_

            Arguments: 1, OFF, ON
            """

            class RANGe(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:RANGe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_RANGe>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "RANGe"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            RANGe = RANGe()
            """
            `DIAGnostic:ALC:RANGe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_RANGe>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class SETTings(SCPINode, SCPIBool):
                """
                DIAGnostic:ALC:SETTings

                Arguments: 1, OFF, ON
                """
                _cmd = "SETTings"
                args = ["1", "OFF", "ON"]

                class CMODe(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:ALC:SETTings:CMODe

                    Arguments: FSETtling, LOVershoot
                    """
                    _cmd = "CMODe"
                    args = ["FSETtling", "LOVershoot"]

                CMODe = CMODe()
                """
                DIAGnostic:ALC:SETTings:CMODe

                Arguments: FSETtling, LOVershoot
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `DIAGnostic:ALC:SETTings:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_SETTings>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `DIAGnostic:ALC:SETTings:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_SETTings>`_

                Arguments: 1, OFF, ON
                """

            SETTings = SETTings()
            """
            DIAGnostic:ALC:SETTings

            Arguments: 1, OFF, ON
            """

            class SOFFset(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:SOFFset
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_SOFFset>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SOFFset"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            SOFFset = SOFFset()
            """
            `DIAGnostic:ALC:SOFFset
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_SOFFset>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class STOLerance(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:STOLerance
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_STOLerance>`_

                Arguments: HIGH, NORMal, WIDE
                """
                _cmd = "STOLerance"
                args = ["HIGH", "NORMal", "WIDE"]

            STOLerance = STOLerance()
            """
            `DIAGnostic:ALC:STOLerance
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#ALC_STOLerance>`_

            Arguments: HIGH, NORMal, WIDE
            """

        ALC = ALC()
        """
        DIAGnostic:ALC

        Arguments:
        """

        class DEVice(SCPINode):
            """
            DIAGnostic:DEVice

            Arguments:
            """
            _cmd = "DEVice"
            args = []

            class STATe(SCPINode, SCPISet):
                """
                `DIAGnostic:DEVice:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#DEVice_STATe>`_

                Arguments: 'string'
                """
                _cmd = "STATe"
                args = ["'string'"]

            STATe = STATe()
            """
            `DIAGnostic:DEVice:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#DEVice_STATe>`_

            Arguments: 'string'
            """

        DEVice = DEVice()
        """
        DIAGnostic:DEVice

        Arguments:
        """

        class PRODuct(SCPINode):
            """
            DIAGnostic:PRODuct

            Arguments:
            """
            _cmd = "PRODuct"
            args = []

            class CATalog(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:CATalog

                Arguments:
                """
                _cmd = "CATalog"
                args = []

            CATalog = CATalog()
            """
            DIAGnostic:PRODuct:CATalog

            Arguments:
            """

            class DESCription(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:DESCription

                Arguments:
                """
                _cmd = "DESCription"
                args = []

            DESCription = DESCription()
            """
            DIAGnostic:PRODuct:DESCription

            Arguments:
            """

            class ID(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:ID

                Arguments:
                """
                _cmd = "ID"
                args = []

            ID = ID()
            """
            DIAGnostic:PRODuct:ID

            Arguments:
            """

            class MACaddress(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:MACaddress

                Arguments:
                """
                _cmd = "MACaddress"
                args = []

            MACaddress = MACaddress()
            """
            DIAGnostic:PRODuct:MACaddress

            Arguments:
            """

            class OPTion(SCPINode):
                """
                DIAGnostic:PRODuct:OPTion

                Arguments:
                """
                _cmd = "OPTion"
                args = []

                class LICence(SCPINode):
                    """
                    DIAGnostic:PRODuct:OPTion:LICence

                    Arguments:
                    """
                    _cmd = "LICence"
                    args = []

                    class CHECk(SCPINode, SCPIQuery, SCPISet):
                        """
                        DIAGnostic:PRODuct:OPTion:LICence:CHECk

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "CHECk"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    CHECk = CHECk()
                    """
                    DIAGnostic:PRODuct:OPTion:LICence:CHECk

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class UNLock(SCPINode, SCPISet):
                        """
                        DIAGnostic:PRODuct:OPTion:LICence:UNLock

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "UNLock"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    UNLock = UNLock()
                    """
                    DIAGnostic:PRODuct:OPTion:LICence:UNLock

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                LICence = LICence()
                """
                DIAGnostic:PRODuct:OPTion:LICence

                Arguments:
                """

                class LIST(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:PRODuct:OPTion:LIST

                    Arguments:
                    """
                    _cmd = "LIST"
                    args = []

                LIST = LIST()
                """
                DIAGnostic:PRODuct:OPTion:LIST

                Arguments:
                """

                class STATus(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:PRODuct:OPTion:STATus

                    Arguments: #<block, 'string'
                    """
                    _cmd = "STATus"
                    args = ["#<block", "'string'"]

                STATus = STATus()
                """
                DIAGnostic:PRODuct:OPTion:STATus

                Arguments: #<block, 'string'
                """

            OPTion = OPTion()
            """
            DIAGnostic:PRODuct:OPTion

            Arguments:
            """

            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                DIAGnostic:PRODuct:SELect

                Arguments: 'string'
                """
                _cmd = "SELect"
                args = ["'string'"]

            SELect = SELect()
            """
            DIAGnostic:PRODuct:SELect

            Arguments: 'string'
            """

            class TIME(SCPINode):
                """
                DIAGnostic:PRODuct:TIME

                Arguments:
                """
                _cmd = "TIME"
                args = []

                class OPERating(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:PRODuct:TIME:OPERating

                    Arguments:
                    """
                    _cmd = "OPERating"
                    args = []

                OPERating = OPERating()
                """
                DIAGnostic:PRODuct:TIME:OPERating

                Arguments:
                """

            TIME = TIME()
            """
            DIAGnostic:PRODuct:TIME

            Arguments:
            """

        PRODuct = PRODuct()
        """
        DIAGnostic:PRODuct

        Arguments:
        """

        class SERVice(SCPINode):
            """
            DIAGnostic:SERVice

            Arguments:
            """
            _cmd = "SERVice"
            args = []

            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:SERVice:FUNCtion
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#FUNCtion>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "FUNCtion"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            FUNCtion = FUNCtion()
            """
            `DIAGnostic:SERVice:FUNCtion
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#FUNCtion>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class RFPower(SCPINode, SCPIBool):
                """
                `DIAGnostic:SERVice:RFPower
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#RFPower>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "RFPower"
                args = ["1", "OFF", "ON"]

            RFPower = RFPower()
            """
            `DIAGnostic:SERVice:RFPower
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#RFPower>`_

            Arguments: 1, OFF, ON
            """

            class SFUNction(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:SERVice:SFUNction
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#SFUNction>`_

                Arguments: 'string'
                """
                _cmd = "SFUNction"
                args = ["'string'"]

            SFUNction = SFUNction()
            """
            `DIAGnostic:SERVice:SFUNction
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/diagnostic/diagnostic.htm#SFUNction>`_

            Arguments: 'string'
            """

        SERVice = SERVice()
        """
        DIAGnostic:SERVice

        Arguments:
        """

        class UPDate(SCPINode):
            """
            DIAGnostic:UPDate

            Arguments:
            """
            _cmd = "UPDate"
            args = []

            class BOOT(SCPINode, SCPISet):
                """
                DIAGnostic:UPDate:BOOT

                Arguments:
                """
                _cmd = "BOOT"
                args = []

            BOOT = BOOT()
            """
            DIAGnostic:UPDate:BOOT

            Arguments:
            """

            class CATalog(SCPINode, SCPIQuery):
                """
                DIAGnostic:UPDate:CATalog

                Arguments:
                """
                _cmd = "CATalog"
                args = []

            CATalog = CATalog()
            """
            DIAGnostic:UPDate:CATalog

            Arguments:
            """

            class CHAP(SCPINode):
                """
                DIAGnostic:UPDate:CHAP

                Arguments:
                """
                _cmd = "CHAP"
                args = []

                class CHALlenge(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:UPDate:CHAP:CHALlenge

                    Arguments:
                    """
                    _cmd = "CHALlenge"
                    args = []

                CHALlenge = CHALlenge()
                """
                DIAGnostic:UPDate:CHAP:CHALlenge

                Arguments:
                """

                class PRESet(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:CHAP:PRESet

                    Arguments:
                    """
                    _cmd = "PRESet"
                    args = []

                PRESet = PRESet()
                """
                DIAGnostic:UPDate:CHAP:PRESet

                Arguments:
                """

                class RESPonse(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:CHAP:RESPonse

                    Arguments: #<block
                    """
                    _cmd = "RESPonse"
                    args = ["#<block"]

                RESPonse = RESPonse()
                """
                DIAGnostic:UPDate:CHAP:RESPonse

                Arguments: #<block
                """

            CHAP = CHAP()
            """
            DIAGnostic:UPDate:CHAP

            Arguments:
            """

            class EXECute(SCPINode, SCPISet):
                """
                DIAGnostic:UPDate:EXECute

                Arguments: NOWait, OVERlay, WAIT
                """
                _cmd = "EXECute"
                args = ["NOWait", "OVERlay", "WAIT"]

            EXECute = EXECute()
            """
            DIAGnostic:UPDate:EXECute

            Arguments: NOWait, OVERlay, WAIT
            """

            class INSTall(SCPINode, SCPISet):
                """
                DIAGnostic:UPDate:INSTall

                Arguments: 'string'
                """
                _cmd = "INSTall"
                args = ["'string'"]

                class BEGin(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:INSTall:BEGin

                    Arguments:
                    """
                    _cmd = "BEGin"
                    args = []

                BEGin = BEGin()
                """
                DIAGnostic:UPDate:INSTall:BEGin

                Arguments:
                """

                class END(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:INSTall:END

                    Arguments:
                    """
                    _cmd = "END"
                    args = []

                END = END()
                """
                DIAGnostic:UPDate:INSTall:END

                Arguments:
                """

                class STATus(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:UPDate:INSTall:STATus

                    Arguments:
                    """
                    _cmd = "STATus"
                    args = []

                STATus = STATus()
                """
                DIAGnostic:UPDate:INSTall:STATus

                Arguments:
                """

            INSTall = INSTall()
            """
            DIAGnostic:UPDate:INSTall

            Arguments: 'string'
            """

            class PROGress(SCPINode, SCPIQuery, SCPISet):
                """
                DIAGnostic:UPDate:PROGress

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "PROGress"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            PROGress = PROGress()
            """
            DIAGnostic:UPDate:PROGress

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class TRANsfer(SCPINode):
                """
                DIAGnostic:UPDate:TRANsfer

                Arguments:
                """
                _cmd = "TRANsfer"
                args = []

                class CLOSe(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:TRANsfer:CLOSe

                    Arguments:
                    """
                    _cmd = "CLOSe"
                    args = []

                CLOSe = CLOSe()
                """
                DIAGnostic:UPDate:TRANsfer:CLOSe

                Arguments:
                """

                class DATA(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:TRANsfer:DATA

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                DATA = DATA()
                """
                DIAGnostic:UPDate:TRANsfer:DATA

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class OPEN(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:TRANsfer:OPEN

                    Arguments: DATA, DESCr
                    """
                    _cmd = "OPEN"
                    args = ["DATA", "DESCr"]

                OPEN = OPEN()
                """
                DIAGnostic:UPDate:TRANsfer:OPEN

                Arguments: DATA, DESCr
                """

                class VERSion(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:UPDate:TRANsfer:VERSion

                    Arguments:
                    """
                    _cmd = "VERSion"
                    args = []

                VERSion = VERSion()
                """
                DIAGnostic:UPDate:TRANsfer:VERSion

                Arguments:
                """

            TRANsfer = TRANsfer()
            """
            DIAGnostic:UPDate:TRANsfer

            Arguments:
            """

        UPDate = UPDate()
        """
        DIAGnostic:UPDate

        Arguments:
        """

    DIAGnostic = DIAGnostic()
    """
    DIAGnostic

    Arguments:
    """

    class DISPlay(SCPINode):
        """
        DISPlay

        Arguments:
        """
        _cmd = "DISPlay"
        args = []

        class ANNotation(SCPINode):
            """
            DISPlay:ANNotation

            Arguments:
            """
            _cmd = "ANNotation"
            args = []

            class CHANnel(SCPINode, SCPIBool):
                """
                DISPlay:ANNotation:CHANnel

                Arguments: 1, OFF, ON
                """
                _cmd = "CHANnel"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `DISPlay:ANNotation:CHANnel:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#ANNotation_CHANnel>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `DISPlay:ANNotation:CHANnel:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#ANNotation_CHANnel>`_

                Arguments: 1, OFF, ON
                """

            CHANnel = CHANnel()
            """
            DISPlay:ANNotation:CHANnel

            Arguments: 1, OFF, ON
            """

            class FREQuency(SCPINode, SCPIBool):
                """
                DISPlay:ANNotation:FREQuency

                Arguments: 1, OFF, ON
                """
                _cmd = "FREQuency"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `DISPlay:ANNotation:FREQuency:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#ANNotation>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `DISPlay:ANNotation:FREQuency:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#ANNotation>`_

                Arguments: 1, OFF, ON
                """

            FREQuency = FREQuency()
            """
            DISPlay:ANNotation:FREQuency

            Arguments: 1, OFF, ON
            """

        ANNotation = ANNotation()
        """
        DISPlay:ANNotation

        Arguments:
        """

        class CMAP(SCPINodeN):
            """
            DISPlay:CMAP

            Arguments:
            """
            _cmd = "CMAP"
            args = []

            class MARKer(SCPINode, SCPIBool):
                """
                DISPlay:CMAP:MARKer

                Arguments: 1, OFF, ON
                """
                _cmd = "MARKer"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `DISPlay:CMAP:MARKer:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `DISPlay:CMAP:MARKer:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm>`_

                Arguments: 1, OFF, ON
                """

            MARKer = MARKer()
            """
            DISPlay:CMAP:MARKer

            Arguments: 1, OFF, ON
            """

            class RGB(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:CMAP:RGB
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "RGB"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            RGB = RGB()
            """
            `DISPlay:CMAP:RGB
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class TRACe(SCPINode):
                """
                DISPlay:CMAP:TRACe

                Arguments:
                """
                _cmd = "TRACe"
                args = []

                class COLor(SCPINode, SCPIBool):
                    """
                    DISPlay:CMAP:TRACe:COLor

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "COLor"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `DISPlay:CMAP:TRACe:COLor:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `DISPlay:CMAP:TRACe:COLor:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm>`_

                    Arguments: 1, OFF, ON
                    """

                COLor = COLor()
                """
                DISPlay:CMAP:TRACe:COLor

                Arguments: 1, OFF, ON
                """

                class RGB(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:CMAP:TRACe:RGB
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#CMAP_TRACe_RGB>`_

                    Arguments: 'string'
                    """
                    _cmd = "RGB"
                    args = ["'string'"]

                RGB = RGB()
                """
                `DISPlay:CMAP:TRACe:RGB
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#CMAP_TRACe_RGB>`_

                Arguments: 'string'
                """

            TRACe = TRACe()
            """
            DISPlay:CMAP:TRACe

            Arguments:
            """

        CMAP = CMAP()
        """
        DISPlay:CMAP

        Arguments:
        """

        class MENU(SCPINode):
            """
            DISPlay:MENU

            Arguments:
            """
            _cmd = "MENU"
            args = []

            class KEY(SCPINode):
                """
                DISPlay:MENU:KEY

                Arguments:
                """
                _cmd = "KEY"
                args = []

                class EXECute(SCPINode, SCPISet):
                    """
                    `DISPlay:MENU:KEY:EXECute
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#MENU_KEY_EXECute>`_

                    Arguments: 'string'
                    """
                    _cmd = "EXECute"
                    args = ["'string'"]

                EXECute = EXECute()
                """
                `DISPlay:MENU:KEY:EXECute
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#MENU_KEY_EXECute>`_

                Arguments: 'string'
                """

                class SELect(SCPINode, SCPISet):
                    """
                    `DISPlay:MENU:KEY:SELect
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#MENU_KEY_SELect>`_

                    Arguments: 'string'
                    """
                    _cmd = "SELect"
                    args = ["'string'"]

                SELect = SELect()
                """
                `DISPlay:MENU:KEY:SELect
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#MENU_KEY_SELect>`_

                Arguments: 'string'
                """

            KEY = KEY()
            """
            DISPlay:MENU:KEY

            Arguments:
            """

        MENU = MENU()
        """
        DISPlay:MENU

        Arguments:
        """

        class RFSize(SCPINode, SCPIQuery, SCPISet):
            """
            `DISPlay:RFSize
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#RFSize>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "RFSize"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

        RFSize = RFSize()
        """
        `DISPlay:RFSize
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#RFSize>`_

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class WINDow(SCPINodeN):
            """
            DISPlay:WINDow

            Arguments:
            """
            _cmd = "WINDow"
            args = []

            class CATalog(SCPINode, SCPIQuery):
                """
                `DISPlay:WINDow:CATalog
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#WINDow_CATalog>`_

                Arguments:
                """
                _cmd = "CATalog"
                args = []

            CATalog = CATalog()
            """
            `DISPlay:WINDow:CATalog
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#WINDow_CATalog>`_

            Arguments:
            """

            class MAXimize(SCPINode, SCPIBool):
                """
                `DISPlay:WINDow:MAXimize
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#MAXimize>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "MAXimize"
                args = ["1", "OFF", "ON"]

            MAXimize = MAXimize()
            """
            `DISPlay:WINDow:MAXimize
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#MAXimize>`_

            Arguments: 1, OFF, ON
            """

            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:WINDow:NAME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#Diagram_NAME>`_

                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]

            NAME = NAME()
            """
            `DISPlay:WINDow:NAME
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#Diagram_NAME>`_

            Arguments: 'string'
            """

            class STATe(SCPINode, SCPIBool):
                """
                `DISPlay:WINDow:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `DISPlay:WINDow:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#STATe>`_

            Arguments: 1, OFF, ON
            """

            class TITLe(SCPINode, SCPIBool):
                """
                DISPlay:WINDow:TITLe

                Arguments: 1, OFF, ON
                """
                _cmd = "TITLe"
                args = ["1", "OFF", "ON"]

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TITLe:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#TITLe_DATA>`_

                    Arguments: 'string'
                    """
                    _cmd = "DATA"
                    args = ["'string'"]

                DATA = DATA()
                """
                `DISPlay:WINDow:TITLe:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#TITLe_DATA>`_

                Arguments: 'string'
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `DISPlay:WINDow:TITLe:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#TITLe_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `DISPlay:WINDow:TITLe:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#TITLe_STATe>`_

                Arguments: 1, OFF, ON
                """

            TITLe = TITLe()
            """
            DISPlay:WINDow:TITLe

            Arguments: 1, OFF, ON
            """

            class TRACe(SCPINodeN):
                """
                DISPlay:WINDow:TRACe

                Arguments:
                """
                _cmd = "TRACe"
                args = []

                class CATalog(SCPINode, SCPIQuery):
                    """
                    `DISPlay:WINDow:TRACe:CATalog
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#WINDow_TRACe_CATalog>`_

                    Arguments:
                    """
                    _cmd = "CATalog"
                    args = []

                CATalog = CATalog()
                """
                `DISPlay:WINDow:TRACe:CATalog
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#WINDow_TRACe_CATalog>`_

                Arguments:
                """

                class DELete(SCPINode, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:DELete
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#DELete>`_

                    Arguments:
                    """
                    _cmd = "DELete"
                    args = []

                DELete = DELete()
                """
                `DISPlay:WINDow:TRACe:DELete
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#DELete>`_

                Arguments:
                """

                class EFEed(SCPINode, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:EFEed
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#EFEed>`_

                    Arguments: 'string'
                    """
                    _cmd = "EFEed"
                    args = ["'string'"]

                EFEed = EFEed()
                """
                `DISPlay:WINDow:TRACe:EFEed
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#EFEed>`_

                Arguments: 'string'
                """

                class FEED(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:FEED
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#FEED>`_

                    Arguments: 'string'
                    """
                    _cmd = "FEED"
                    args = ["'string'"]

                FEED = FEED()
                """
                `DISPlay:WINDow:TRACe:FEED
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#FEED>`_

                Arguments: 'string'
                """

                class SHOW(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:SHOW
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#SHOW>`_

                    Arguments: DALL, MALL, 'string'
                    """
                    _cmd = "SHOW"
                    args = ["DALL", "MALL", "'string'"]

                SHOW = SHOW()
                """
                `DISPlay:WINDow:TRACe:SHOW
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#SHOW>`_

                Arguments: DALL, MALL, 'string'
                """

                class X(SCPINode):
                    """
                    DISPlay:WINDow:TRACe:X

                    Arguments:
                    """
                    _cmd = "X"
                    args = []

                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:X:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#X_OFFSet>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "OFFSet"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    OFFSet = OFFSet()
                    """
                    `DISPlay:WINDow:TRACe:X:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#X_OFFSet>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                X = X()
                """
                DISPlay:WINDow:TRACe:X

                Arguments:
                """

                class Y(SCPINode):
                    """
                    DISPlay:WINDow:TRACe:Y

                    Arguments:
                    """
                    _cmd = "Y"
                    args = []

                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:Y:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#Y_OFFSet>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "OFFSet"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    OFFSet = OFFSet()
                    """
                    `DISPlay:WINDow:TRACe:Y:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#Y_OFFSet>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class SCALe(SCPINode):
                        """
                        DISPlay:WINDow:TRACe:Y:SCALe

                        Arguments:
                        """
                        _cmd = "SCALe"
                        args = []

                        class AUTO(SCPINode, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:AUTO
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#AUTO>`_

                            Arguments: ONCE
                            """
                            _cmd = "AUTO"
                            args = ["ONCE"]

                        AUTO = AUTO()
                        """
                        `DISPlay:WINDow:TRACe:Y:SCALe:AUTO
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#AUTO>`_

                        Arguments: ONCE
                        """

                        class BOTTom(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:BOTTom
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#BOTTom>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "BOTTom"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        BOTTom = BOTTom()
                        """
                        `DISPlay:WINDow:TRACe:Y:SCALe:BOTTom
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#BOTTom>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class PDIVision(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:PDIVision
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#PDIVision>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "PDIVision"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        PDIVision = PDIVision()
                        """
                        `DISPlay:WINDow:TRACe:Y:SCALe:PDIVision
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#PDIVision>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class RLEVel(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:RLEVel
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#RLEVel>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "RLEVel"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        RLEVel = RLEVel()
                        """
                        `DISPlay:WINDow:TRACe:Y:SCALe:RLEVel
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#RLEVel>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class RPOSition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:RPOSition
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#RPOSition>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "RPOSition"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        RPOSition = RPOSition()
                        """
                        `DISPlay:WINDow:TRACe:Y:SCALe:RPOSition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#RPOSition>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class TOP(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:TOP
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#TOP>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "TOP"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        TOP = TOP()
                        """
                        `DISPlay:WINDow:TRACe:Y:SCALe:TOP
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/display/display.htm#TOP>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                    SCALe = SCALe()
                    """
                    DISPlay:WINDow:TRACe:Y:SCALe

                    Arguments:
                    """

                Y = Y()
                """
                DISPlay:WINDow:TRACe:Y

                Arguments:
                """

            TRACe = TRACe()
            """
            DISPlay:WINDow:TRACe

            Arguments:
            """

        WINDow = WINDow()
        """
        DISPlay:WINDow

        Arguments:
        """

    DISPlay = DISPlay()
    """
    DISPlay

    Arguments:
    """

    class FORMat(SCPINode, SCPIQuery, SCPISet):
        """
        FORMat

        Arguments: ASCii, REAL
        """
        _cmd = "FORMat"
        args = ["ASCii", "REAL"]

        class BORDer(SCPINode, SCPIQuery, SCPISet):
            """
            `FORMat:BORDer
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/format/format.htm#BORDer>`_

            Arguments: NORMal, SWAPped
            """
            _cmd = "BORDer"
            args = ["NORMal", "SWAPped"]

        BORDer = BORDer()
        """
        `FORMat:BORDer
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/format/format.htm#BORDer>`_

        Arguments: NORMal, SWAPped
        """

        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `FORMat:DATA
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/format/format.htm#DATA>`_

            Arguments: ASCii, REAL
            """
            _cmd = "DATA"
            args = ["ASCii", "REAL"]

        DATA = DATA()
        """
        `FORMat:DATA
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/format/format.htm#DATA>`_

        Arguments: ASCii, REAL
        """

        class DEXPort(SCPINode):
            """
            FORMat:DEXPort

            Arguments:
            """
            _cmd = "DEXPort"
            args = []

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `FORMat:DEXPort:SOURce
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/format/format.htm#DEXPort_SOURce>`_

                Arguments: FDATa, MDATa, SDATa
                """
                _cmd = "SOURce"
                args = ["FDATa", "MDATa", "SDATa"]

            SOURce = SOURce()
            """
            `FORMat:DEXPort:SOURce
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/format/format.htm#DEXPort_SOURce>`_

            Arguments: FDATa, MDATa, SDATa
            """

        DEXPort = DEXPort()
        """
        FORMat:DEXPort

        Arguments:
        """

    FORMat = FORMat()
    """
    FORMat

    Arguments: ASCii, REAL
    """

    class HCOPy(SCPINode, SCPISet):
        """
        HCOPy

        Arguments:
        """
        _cmd = "HCOPy"
        args = []

        class DESTination(SCPINode, SCPIQuery, SCPISet):
            """
            `HCOPy:DESTination
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#DESTination>`_

            Arguments: 'string'
            """
            _cmd = "DESTination"
            args = ["'string'"]

        DESTination = DESTination()
        """
        `HCOPy:DESTination
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#DESTination>`_

        Arguments: 'string'
        """

        class DEVice(SCPINode):
            """
            HCOPy:DEVice

            Arguments:
            """
            _cmd = "DEVice"
            args = []

            class LANGuage(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:DEVice:LANGuage
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#DEVice_LANGuage>`_

                Arguments: BMP, EMF, EWMF, JPG, PNG, WMF
                """
                _cmd = "LANGuage"
                args = ["BMP", "EMF", "EWMF", "JPG", "PNG", "WMF"]

            LANGuage = LANGuage()
            """
            `HCOPy:DEVice:LANGuage
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#DEVice_LANGuage>`_

            Arguments: BMP, EMF, EWMF, JPG, PNG, WMF
            """

        DEVice = DEVice()
        """
        HCOPy:DEVice

        Arguments:
        """

        class IMMediate(SCPINode, SCPISet):
            """
            `HCOPy:IMMediate
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#IMMediate>`_

            Arguments:
            """
            _cmd = "IMMediate"
            args = []

        IMMediate = IMMediate()
        """
        `HCOPy:IMMediate
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#IMMediate>`_

        Arguments:
        """

        class ITEM(SCPINode):
            """
            HCOPy:ITEM

            Arguments:
            """
            _cmd = "ITEM"
            args = []

            class ALL(SCPINode, SCPISet):
                """
                `HCOPy:ITEM:ALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#ITEM_ALL>`_

                Arguments:
                """
                _cmd = "ALL"
                args = []

            ALL = ALL()
            """
            `HCOPy:ITEM:ALL
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#ITEM_ALL>`_

            Arguments:
            """

            class LOGO(SCPINode, SCPIBool):
                """
                HCOPy:ITEM:LOGO

                Arguments: 1, OFF, ON
                """
                _cmd = "LOGO"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `HCOPy:ITEM:LOGO:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#LOGO>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `HCOPy:ITEM:LOGO:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#LOGO>`_

                Arguments: 1, OFF, ON
                """

            LOGO = LOGO()
            """
            HCOPy:ITEM:LOGO

            Arguments: 1, OFF, ON
            """

            class MLISt(SCPINode, SCPIBool):
                """
                HCOPy:ITEM:MLISt

                Arguments: 1, OFF, ON
                """
                _cmd = "MLISt"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    HCOPy:ITEM:MLISt:STATe

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                HCOPy:ITEM:MLISt:STATe

                Arguments: 1, OFF, ON
                """

            MLISt = MLISt()
            """
            HCOPy:ITEM:MLISt

            Arguments: 1, OFF, ON
            """

            class TIME(SCPINode, SCPIBool):
                """
                HCOPy:ITEM:TIME

                Arguments: 1, OFF, ON
                """
                _cmd = "TIME"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `HCOPy:ITEM:TIME:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#TIME>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `HCOPy:ITEM:TIME:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#TIME>`_

                Arguments: 1, OFF, ON
                """

            TIME = TIME()
            """
            HCOPy:ITEM:TIME

            Arguments: 1, OFF, ON
            """

        ITEM = ITEM()
        """
        HCOPy:ITEM

        Arguments:
        """

        class MITem(SCPINode):
            """
            HCOPy:MITem

            Arguments:
            """
            _cmd = "MITem"
            args = []

            class LOGO(SCPINode, SCPIBool):
                """
                HCOPy:MITem:LOGO

                Arguments: 1, OFF, ON
                """
                _cmd = "LOGO"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `HCOPy:MITem:LOGO:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#MITEM_LOGO>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `HCOPy:MITem:LOGO:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#MITEM_LOGO>`_

                Arguments: 1, OFF, ON
                """

            LOGO = LOGO()
            """
            HCOPy:MITem:LOGO

            Arguments: 1, OFF, ON
            """

            class TIME(SCPINode, SCPIBool):
                """
                HCOPy:MITem:TIME

                Arguments: 1, OFF, ON
                """
                _cmd = "TIME"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `HCOPy:MITem:TIME:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#MITEM_TIME>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `HCOPy:MITem:TIME:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#MITEM_TIME>`_

                Arguments: 1, OFF, ON
                """

            TIME = TIME()
            """
            HCOPy:MITem:TIME

            Arguments: 1, OFF, ON
            """

        MITem = MITem()
        """
        HCOPy:MITem

        Arguments:
        """

        class MPAGe(SCPINode):
            """
            HCOPy:MPAGe

            Arguments:
            """
            _cmd = "MPAGe"
            args = []

            class WINDow(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:MPAGe:WINDow
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#MPAGe_WINDow>`_

                Arguments: ACTive, ALL, MARKer
                """
                _cmd = "WINDow"
                args = ["ACTive", "ALL", "MARKer"]

            WINDow = WINDow()
            """
            `HCOPy:MPAGe:WINDow
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#MPAGe_WINDow>`_

            Arguments: ACTive, ALL, MARKer
            """

        MPAGe = MPAGe()
        """
        HCOPy:MPAGe

        Arguments:
        """

        class PAGE(SCPINode):
            """
            HCOPy:PAGE

            Arguments:
            """
            _cmd = "PAGE"
            args = []

            class MARGin(SCPINode):
                """
                HCOPy:PAGE:MARGin

                Arguments:
                """
                _cmd = "MARGin"
                args = []

                class BOTTom(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:BOTTom
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#BOTTom>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "BOTTom"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                BOTTom = BOTTom()
                """
                `HCOPy:PAGE:MARGin:BOTTom
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#BOTTom>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class LEFT(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:LEFT
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_LEFT>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "LEFT"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                LEFT = LEFT()
                """
                `HCOPy:PAGE:MARGin:LEFT
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/calculate/calculate_marker.htm#SEARch_LEFT>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class RIGHt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:RIGHt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#RIGHt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RIGHt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                RIGHt = RIGHt()
                """
                `HCOPy:PAGE:MARGin:RIGHt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#RIGHt>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class TOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:TOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#TOP>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TOP"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                TOP = TOP()
                """
                `HCOPy:PAGE:MARGin:TOP
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#TOP>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            MARGin = MARGin()
            """
            HCOPy:PAGE:MARGin

            Arguments:
            """

            class ORIentation(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:PAGE:ORIentation
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#ORIentation>`_

                Arguments: LANDscape, PORTrait
                """
                _cmd = "ORIentation"
                args = ["LANDscape", "PORTrait"]

            ORIentation = ORIentation()
            """
            `HCOPy:PAGE:ORIentation
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#ORIentation>`_

            Arguments: LANDscape, PORTrait
            """

            class WINDow(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:PAGE:WINDow
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#WINDow>`_

                Arguments: ACTive, ALL, SINGle
                """
                _cmd = "WINDow"
                args = ["ACTive", "ALL", "SINGle"]

            WINDow = WINDow()
            """
            `HCOPy:PAGE:WINDow
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/hcopy/hcopy.htm#WINDow>`_

            Arguments: ACTive, ALL, SINGle
            """

        PAGE = PAGE()
        """
        HCOPy:PAGE

        Arguments:
        """

    HCOPy = HCOPy()
    """
    HCOPy

    Arguments:
    """

    class INITiate(SCPINodeN, SCPIQuery, SCPISet):
        """
        INITiate

        Arguments:
        """
        _cmd = "INITiate"
        args = []

        class CONTinuous(SCPINode, SCPIBool):
            """
            `INITiate:CONTinuous
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/initiate/initiate.htm#CONTinuous>`_

            Arguments: 1, OFF, ON
            """
            _cmd = "CONTinuous"
            args = ["1", "OFF", "ON"]

        CONTinuous = CONTinuous()
        """
        `INITiate:CONTinuous
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/initiate/initiate.htm#CONTinuous>`_

        Arguments: 1, OFF, ON
        """

        class IMMediate(SCPINode, SCPIQuery, SCPISet):
            """
            `INITiate:IMMediate
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/initiate/initiate.htm#IMMediate>`_

            Arguments:
            """
            _cmd = "IMMediate"
            args = []

            class DUMMy(SCPINode, SCPIQuery, SCPISet):
                """
                INITiate:IMMediate:DUMMy

                Arguments:
                """
                _cmd = "DUMMy"
                args = []

            DUMMy = DUMMy()
            """
            INITiate:IMMediate:DUMMy

            Arguments:
            """

            class SCOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `INITiate:IMMediate:SCOPe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/initiate/initiate.htm#SCOPe>`_

                Arguments: ALL, SINGle
                """
                _cmd = "SCOPe"
                args = ["ALL", "SINGle"]

            SCOPe = SCOPe()
            """
            `INITiate:IMMediate:SCOPe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/initiate/initiate.htm#SCOPe>`_

            Arguments: ALL, SINGle
            """

        IMMediate = IMMediate()
        """
        `INITiate:IMMediate
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/initiate/initiate.htm#IMMediate>`_

        Arguments:
        """

    INITiate = INITiate()
    """
    INITiate

    Arguments:
    """

    class INPut(SCPINodeN):
        """
        INPut

        Arguments:
        """
        _cmd = "INPut"
        args = []

        class ATTenuation(SCPINode, SCPIQuery, SCPISet):
            """
            `INPut:ATTenuation
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/input/input.htm#ATTenuation>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "ATTenuation"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

        ATTenuation = ATTenuation()
        """
        `INPut:ATTenuation
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/input/input.htm#ATTenuation>`_

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

    INPut = INPut()
    """
    INPut

    Arguments:
    """

    class INSTrument(SCPINode, SCPIQuery, SCPISet):
        """
        INSTrument

        Arguments: CHANnel1, CHANnel2, CHANnel3, CHANnel4
        """
        _cmd = "INSTrument"
        args = ["CHANnel1", "CHANnel2", "CHANnel3", "CHANnel4"]

        class NSELect(SCPINode, SCPIQuery, SCPISet):
            """
            `INSTrument:NSELect
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/instrument/instrument.htm#NSELect>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "NSELect"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

        NSELect = NSELect()
        """
        `INSTrument:NSELect
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/instrument/instrument.htm#NSELect>`_

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class PORT(SCPINode):
            """
            INSTrument:PORT

            Arguments:
            """
            _cmd = "PORT"
            args = []

            class COUNt(SCPINode, SCPIQuery):
                """
                `INSTrument:PORT:COUNt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/instrument/instrument.htm#PORT_COUNt>`_

                Arguments:
                """
                _cmd = "COUNt"
                args = []

            COUNt = COUNt()
            """
            `INSTrument:PORT:COUNt
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/instrument/instrument.htm#PORT_COUNt>`_

            Arguments:
            """

        PORT = PORT()
        """
        INSTrument:PORT

        Arguments:
        """

        class SELect(SCPINode, SCPIQuery, SCPISet):
            """
            `INSTrument:SELect
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/instrument/instrument.htm#SELect>`_

            Arguments: CHANnel1, CHANnel2, CHANnel3, CHANnel4
            """
            _cmd = "SELect"
            args = ["CHANnel1", "CHANnel2", "CHANnel3", "CHANnel4"]

        SELect = SELect()
        """
        `INSTrument:SELect
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/instrument/instrument.htm#SELect>`_

        Arguments: CHANnel1, CHANnel2, CHANnel3, CHANnel4
        """

    INSTrument = INSTrument()
    """
    INSTrument

    Arguments: CHANnel1, CHANnel2, CHANnel3, CHANnel4
    """

    class MEMory(SCPINode):
        """
        MEMory

        Arguments:
        """
        _cmd = "MEMory"
        args = []

        class CATalog(SCPINode, SCPIQuery):
            """
            `MEMory:CATalog
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/memory/memory.htm#CATalog>`_

            Arguments:
            """
            _cmd = "CATalog"
            args = []

        CATalog = CATalog()
        """
        `MEMory:CATalog
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/memory/memory.htm#CATalog>`_

        Arguments:
        """

        class DEFine(SCPINode, SCPISet):
            """
            `MEMory:DEFine
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/memory/memory.htm#DEFine>`_

            Arguments: 'string'
            """
            _cmd = "DEFine"
            args = ["'string'"]

        DEFine = DEFine()
        """
        `MEMory:DEFine
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/memory/memory.htm#DEFine>`_

        Arguments: 'string'
        """

        class DELete(SCPINode, SCPISet):
            """
            MEMory:DELete

            Arguments: 'string'
            """
            _cmd = "DELete"
            args = ["'string'"]

            class ALL(SCPINode, SCPISet):
                """
                `MEMory:DELete:ALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/memory/memory.htm#DELete_ALL>`_

                Arguments:
                """
                _cmd = "ALL"
                args = []

            ALL = ALL()
            """
            `MEMory:DELete:ALL
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/memory/memory.htm#DELete_ALL>`_

            Arguments:
            """

            class NAME(SCPINode, SCPISet):
                """
                `MEMory:DELete:NAME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/memory/memory.htm#DELete_NAME>`_

                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]

            NAME = NAME()
            """
            `MEMory:DELete:NAME
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/memory/memory.htm#DELete_NAME>`_

            Arguments: 'string'
            """

        DELete = DELete()
        """
        MEMory:DELete

        Arguments: 'string'
        """

        class SELect(SCPINode, SCPIQuery, SCPISet):
            """
            `MEMory:SELect
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/memory/memory.htm#SELect>`_

            Arguments: 'string'
            """
            _cmd = "SELect"
            args = ["'string'"]

        SELect = SELect()
        """
        `MEMory:SELect
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/memory/memory.htm#SELect>`_

        Arguments: 'string'
        """

    MEMory = MEMory()
    """
    MEMory

    Arguments:
    """

    class MMEMory(SCPINode):
        """
        MMEMory

        Arguments:
        """
        _cmd = "MMEMory"
        args = []

        class AKAL(SCPINode):
            """
            MMEMory:AKAL

            Arguments:
            """
            _cmd = "AKAL"
            args = []

            class FACTory(SCPINode):
                """
                MMEMory:AKAL:FACTory

                Arguments:
                """
                _cmd = "FACTory"
                args = []

                class CONVersion(SCPINode, SCPISet):
                    """
                    `MMEMory:AKAL:FACTory:CONVersion
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#AKAL_FACTory_CONVersion>`_

                    Arguments: 'string'
                    """
                    _cmd = "CONVersion"
                    args = ["'string'"]

                CONVersion = CONVersion()
                """
                `MMEMory:AKAL:FACTory:CONVersion
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#AKAL_FACTory_CONVersion>`_

                Arguments: 'string'
                """

            FACTory = FACTory()
            """
            MMEMory:AKAL:FACTory

            Arguments:
            """

            class USER(SCPINode):
                """
                MMEMory:AKAL:USER

                Arguments:
                """
                _cmd = "USER"
                args = []

                class CONVersion(SCPINode, SCPISet):
                    """
                    `MMEMory:AKAL:USER:CONVersion
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#AKAL_USER_CONVersion>`_

                    Arguments: 'string'
                    """
                    _cmd = "CONVersion"
                    args = ["'string'"]

                CONVersion = CONVersion()
                """
                `MMEMory:AKAL:USER:CONVersion
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#AKAL_USER_CONVersion>`_

                Arguments: 'string'
                """

            USER = USER()
            """
            MMEMory:AKAL:USER

            Arguments:
            """

        AKAL = AKAL()
        """
        MMEMory:AKAL

        Arguments:
        """

        class CATalog(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:CATalog
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#CATalog>`_

            Arguments: 'string'
            """
            _cmd = "CATalog"
            args = ["'string'"]

            class ALL(SCPINode, SCPIQuery, SCPISet):
                """
                `MMEMory:CATalog:ALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#CATalog_All>`_

                Arguments: 'string'
                """
                _cmd = "ALL"
                args = ["'string'"]

            ALL = ALL()
            """
            `MMEMory:CATalog:ALL
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#CATalog_All>`_

            Arguments: 'string'
            """

        CATalog = CATalog()
        """
        `MMEMory:CATalog
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#CATalog>`_

        Arguments: 'string'
        """

        class CDIRectory(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:CDIRectory
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#CDIRecotry>`_

            Arguments: DEFault, 'string'
            """
            _cmd = "CDIRectory"
            args = ["DEFault", "'string'"]

        CDIRectory = CDIRectory()
        """
        `MMEMory:CDIRectory
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#CDIRecotry>`_

        Arguments: DEFault, 'string'
        """

        class COPY(SCPINode, SCPISet):
            """
            `MMEMory:COPY
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#COPY>`_

            Arguments: 'string'
            """
            _cmd = "COPY"
            args = ["'string'"]

        COPY = COPY()
        """
        `MMEMory:COPY
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#COPY>`_

        Arguments: 'string'
        """

        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:DATA
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#DATA>`_

            Arguments: 'string'
            """
            _cmd = "DATA"
            args = ["'string'"]

        DATA = DATA()
        """
        `MMEMory:DATA
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#DATA>`_

        Arguments: 'string'
        """

        class DELete(SCPINode, SCPISet):
            """
            `MMEMory:DELete
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#DELete>`_

            Arguments: 'string'
            """
            _cmd = "DELete"
            args = ["'string'"]

            class CORRection(SCPINode, SCPISet):
                """
                `MMEMory:DELete:CORRection
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#DELete_CORRection>`_

                Arguments: 'string'
                """
                _cmd = "CORRection"
                args = ["'string'"]

            CORRection = CORRection()
            """
            `MMEMory:DELete:CORRection
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#DELete_CORRection>`_

            Arguments: 'string'
            """

        DELete = DELete()
        """
        `MMEMory:DELete
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#DELete>`_

        Arguments: 'string'
        """

        class LOAD(SCPINode, SCPISet):
            """
            MMEMory:LOAD

            Arguments: 'string'
            """
            _cmd = "LOAD"
            args = ["'string'"]

            class CKIT(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:CKIT
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CKIT>`_

                Arguments: 'string'
                """
                _cmd = "CKIT"
                args = ["'string'"]

                class SDATa(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CKIT:SDATa
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CKIT:SDATa>`_

                    Arguments: 'string'
                    """
                    _cmd = "SDATa"
                    args = ["'string'"]

                SDATa = SDATa()
                """
                `MMEMory:LOAD:CKIT:SDATa
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CKIT:SDATa>`_

                Arguments: 'string'
                """

                class UDIRectory(SCPINode, SCPIQuery, SCPISet):
                    """
                    `MMEMory:LOAD:CKIT:UDIRectory
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CKIT_UDIRectory>`_

                    Arguments: 'string'
                    """
                    _cmd = "UDIRectory"
                    args = ["'string'"]

                UDIRectory = UDIRectory()
                """
                `MMEMory:LOAD:CKIT:UDIRectory
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CKIT_UDIRectory>`_

                Arguments: 'string'
                """

            CKIT = CKIT()
            """
            `MMEMory:LOAD:CKIT
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CKIT>`_

            Arguments: 'string'
            """

            class CMAP(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:CMAP
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CMAP>`_

                Arguments: 'string'
                """
                _cmd = "CMAP"
                args = ["'string'"]

            CMAP = CMAP()
            """
            `MMEMory:LOAD:CMAP
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CMAP>`_

            Arguments: 'string'
            """

            class CORRection(SCPINode, SCPIQuery, SCPISet):
                """
                `MMEMory:LOAD:CORRection
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection>`_

                Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CORRection"
                args = ["1", "ALL", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class MERGe(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:MERGe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection_MERGE>`_

                    Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "MERGe"
                    args = ["1", "ALL", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                MERGe = MERGe()
                """
                `MMEMory:LOAD:CORRection:MERGe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection_MERGE>`_

                Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class RESolve(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:RESolve
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection_RESolve>`_

                    Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RESolve"
                    args = ["1", "ALL", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                RESolve = RESolve()
                """
                `MMEMory:LOAD:CORRection:RESolve
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection_RESolve>`_

                Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class TCOefficient(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:TCOefficient
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection_TCOefficient>`_

                    Arguments: 'string'
                    """
                    _cmd = "TCOefficient"
                    args = ["'string'"]

                TCOefficient = TCOefficient()
                """
                `MMEMory:LOAD:CORRection:TCOefficient
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection_TCOefficient>`_

                Arguments: 'string'
                """

            CORRection = CORRection()
            """
            `MMEMory:LOAD:CORRection
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection>`_

            Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class LIMit(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:LIMit
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_LIMit>`_

                Arguments: 'string'
                """
                _cmd = "LIMit"
                args = ["'string'"]

            LIMit = LIMit()
            """
            `MMEMory:LOAD:LIMit
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_LIMit>`_

            Arguments: 'string'
            """

            class MDAData(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:MDAData
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_MDAData>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "MDAData"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            MDAData = MDAData()
            """
            `MMEMory:LOAD:MDAData
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_MDAData>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class MDCData(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:MDCData
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_MDCData>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "MDCData"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            MDCData = MDCData()
            """
            `MMEMory:LOAD:MDCData
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_MDCData>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class PTRain(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:PTRain
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_PTRain>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "PTRain"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            PTRain = PTRain()
            """
            `MMEMory:LOAD:PTRain
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_PTRain>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class RIPPle(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:RIPPle
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_RIPPle>`_

                Arguments: 'string'
                """
                _cmd = "RIPPle"
                args = ["'string'"]

            RIPPle = RIPPle()
            """
            `MMEMory:LOAD:RIPPle
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_RIPPle>`_

            Arguments: 'string'
            """

            class SEGMent(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:SEGMent
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_SEGMent>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SEGMent"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            SEGMent = SEGMent()
            """
            `MMEMory:LOAD:SEGMent
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_SEGMent>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class STATe(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_STATe>`_

                Arguments: 1
                """
                _cmd = "STATe"
                args = ["1"]

            STATe = STATe()
            """
            `MMEMory:LOAD:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_STATe>`_

            Arguments: 1
            """

            class TRACe(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:TRACe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_TRACE>`_

                Arguments: 'string'
                """
                _cmd = "TRACe"
                args = ["'string'"]

            TRACe = TRACe()
            """
            `MMEMory:LOAD:TRACe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_TRACE>`_

            Arguments: 'string'
            """

            class VNETworks(SCPINodeN):
                """
                MMEMory:LOAD:VNETworks

                Arguments:
                """
                _cmd = "VNETworks"
                args = []

                class BALanced(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:BALanced

                    Arguments:
                    """
                    _cmd = "BALanced"
                    args = []

                    class DEEMbedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:BALanced:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_BALanced_DEEMbedding>`_

                        Arguments: 'string'
                        """
                        _cmd = "DEEMbedding"
                        args = ["'string'"]

                    DEEMbedding = DEEMbedding()
                    """
                    `MMEMory:LOAD:VNETworks:BALanced:DEEMbedding
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_BALanced_DEEMbedding>`_

                    Arguments: 'string'
                    """

                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:BALanced:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_BALanced_EMBedding>`_

                        Arguments: 'string'
                        """
                        _cmd = "EMBedding"
                        args = ["'string'"]

                    EMBedding = EMBedding()
                    """
                    `MMEMory:LOAD:VNETworks:BALanced:EMBedding
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_BALanced_EMBedding>`_

                    Arguments: 'string'
                    """

                BALanced = BALanced()
                """
                MMEMory:LOAD:VNETworks:BALanced

                Arguments:
                """

                class GLOop(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:GLOop

                    Arguments:
                    """
                    _cmd = "GLOop"
                    args = []

                    class DEEMbedding(SCPINode, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:GLOop:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_GLOop_DEEMbedding>`_

                        Arguments: 'string'
                        """
                        _cmd = "DEEMbedding"
                        args = ["'string'"]

                    DEEMbedding = DEEMbedding()
                    """
                    `MMEMory:LOAD:VNETworks:GLOop:DEEMbedding
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_GLOop_DEEMbedding>`_

                    Arguments: 'string'
                    """

                    class EMBedding(SCPINode, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:GLOop:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_GLOop_EMBedding>`_

                        Arguments: 'string'
                        """
                        _cmd = "EMBedding"
                        args = ["'string'"]

                    EMBedding = EMBedding()
                    """
                    `MMEMory:LOAD:VNETworks:GLOop:EMBedding
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_GLOop_EMBedding>`_

                    Arguments: 'string'
                    """

                GLOop = GLOop()
                """
                MMEMory:LOAD:VNETworks:GLOop

                Arguments:
                """

                class PPAir(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:PPAir

                    Arguments:
                    """
                    _cmd = "PPAir"
                    args = []

                    class DEEMbedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:PPAir:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_PPAir_DEEMbedding>`_

                        Arguments: 'string'
                        """
                        _cmd = "DEEMbedding"
                        args = ["'string'"]

                    DEEMbedding = DEEMbedding()
                    """
                    `MMEMory:LOAD:VNETworks:PPAir:DEEMbedding
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_PPAir_DEEMbedding>`_

                    Arguments: 'string'
                    """

                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:PPAir:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_PPAir_EMBedding>`_

                        Arguments: 'string'
                        """
                        _cmd = "EMBedding"
                        args = ["'string'"]

                    EMBedding = EMBedding()
                    """
                    `MMEMory:LOAD:VNETworks:PPAir:EMBedding
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_PPAir_EMBedding>`_

                    Arguments: 'string'
                    """

                PPAir = PPAir()
                """
                MMEMory:LOAD:VNETworks:PPAir

                Arguments:
                """

                class SENDed(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:SENDed

                    Arguments:
                    """
                    _cmd = "SENDed"
                    args = []

                    class DEEMbedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:SENDed:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_SENDed_DEEMbedding>`_

                        Arguments: 'string'
                        """
                        _cmd = "DEEMbedding"
                        args = ["'string'"]

                    DEEMbedding = DEEMbedding()
                    """
                    `MMEMory:LOAD:VNETworks:SENDed:DEEMbedding
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_SENDed_DEEMbedding>`_

                    Arguments: 'string'
                    """

                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:SENDed:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_SENDed_EMBedding>`_

                        Arguments: 'string'
                        """
                        _cmd = "EMBedding"
                        args = ["'string'"]

                    EMBedding = EMBedding()
                    """
                    `MMEMory:LOAD:VNETworks:SENDed:EMBedding
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_SENDed_EMBedding>`_

                    Arguments: 'string'
                    """

                SENDed = SENDed()
                """
                MMEMory:LOAD:VNETworks:SENDed

                Arguments:
                """

            VNETworks = VNETworks()
            """
            MMEMory:LOAD:VNETworks

            Arguments:
            """

        LOAD = LOAD()
        """
        MMEMory:LOAD

        Arguments: 'string'
        """

        class MDIRectory(SCPINode, SCPISet):
            """
            `MMEMory:MDIRectory
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#MDIRectory>`_

            Arguments: 'string'
            """
            _cmd = "MDIRectory"
            args = ["'string'"]

        MDIRectory = MDIRectory()
        """
        `MMEMory:MDIRectory
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#MDIRectory>`_

        Arguments: 'string'
        """

        class MOVE(SCPINode, SCPISet):
            """
            `MMEMory:MOVE
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#MOVE>`_

            Arguments: 'string'
            """
            _cmd = "MOVE"
            args = ["'string'"]

        MOVE = MOVE()
        """
        `MMEMory:MOVE
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#MOVE>`_

        Arguments: 'string'
        """

        class MSIS(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:MSIS
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#MSIS>`_

            Arguments: 'string'
            """
            _cmd = "MSIS"
            args = ["'string'"]

        MSIS = MSIS()
        """
        `MMEMory:MSIS
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#MSIS>`_

        Arguments: 'string'
        """

        class NAME(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:NAME
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#NAME>`_

            Arguments: 'string'
            """
            _cmd = "NAME"
            args = ["'string'"]

        NAME = NAME()
        """
        `MMEMory:NAME
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#NAME>`_

        Arguments: 'string'
        """

        class RDIRectory(SCPINode, SCPISet):
            """
            `MMEMory:RDIRectory
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#RDIRectory>`_

            Arguments: 'string'
            """
            _cmd = "RDIRectory"
            args = ["'string'"]

        RDIRectory = RDIRectory()
        """
        `MMEMory:RDIRectory
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#RDIRectory>`_

        Arguments: 'string'
        """

        class SETTings(SCPINode):
            """
            MMEMory:SETTings

            Arguments:
            """
            _cmd = "SETTings"
            args = []

            class RENorm(SCPINode):
                """
                MMEMory:SETTings:RENorm

                Arguments:
                """
                _cmd = "RENorm"
                args = []

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `MMEMory:SETTings:RENorm:MODE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#SETTings_RENorm_MODE>`_

                    Arguments: AUTO, EXPLicit
                    """
                    _cmd = "MODE"
                    args = ["AUTO", "EXPLicit"]

                MODE = MODE()
                """
                `MMEMory:SETTings:RENorm:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#SETTings_RENorm_MODE>`_

                Arguments: AUTO, EXPLicit
                """

                class RIMPedance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `MMEMory:SETTings:RENorm:RIMPedance
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#SETTings_RENorm_RIMPedance>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RIMPedance"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                RIMPedance = RIMPedance()
                """
                `MMEMory:SETTings:RENorm:RIMPedance
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#SETTings_RENorm_RIMPedance>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `MMEMory:SETTings:RENorm:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#SETTings_RENorm_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `MMEMory:SETTings:RENorm:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#SETTings_RENorm_STATe>`_

                Arguments: 1, OFF, ON
                """

            RENorm = RENorm()
            """
            MMEMory:SETTings:RENorm

            Arguments:
            """

        SETTings = SETTings()
        """
        MMEMory:SETTings

        Arguments:
        """

        class STORe(SCPINode):
            """
            MMEMory:STORe

            Arguments:
            """
            _cmd = "STORe"
            args = []

            class CKIT(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CKIT
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_CKIT>`_

                Arguments: 'string'
                """
                _cmd = "CKIT"
                args = ["'string'"]

                class WLABel(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:CKIT:WLABel
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_CKIT_WLABel>`_

                    Arguments: 'string'
                    """
                    _cmd = "WLABel"
                    args = ["'string'"]

                WLABel = WLABel()
                """
                `MMEMory:STORe:CKIT:WLABel
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_CKIT_WLABel>`_

                Arguments: 'string'
                """

            CKIT = CKIT()
            """
            `MMEMory:STORe:CKIT
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_CKIT>`_

            Arguments: 'string'
            """

            class CMAP(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CMAP
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_CMAP>`_

                Arguments: 'string'
                """
                _cmd = "CMAP"
                args = ["'string'"]

            CMAP = CMAP()
            """
            `MMEMory:STORe:CMAP
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_CMAP>`_

            Arguments: 'string'
            """

            class CORRection(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CORRection
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_CORRection>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CORRection"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class TCOefficient(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:CORRection:TCOefficient
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_CORRection_TCOefficient>`_

                    Arguments: 'string'
                    """
                    _cmd = "TCOefficient"
                    args = ["'string'"]

                TCOefficient = TCOefficient()
                """
                `MMEMory:STORe:CORRection:TCOefficient
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_CORRection_TCOefficient>`_

                Arguments: 'string'
                """

            CORRection = CORRection()
            """
            `MMEMory:STORe:CORRection
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_CORRection>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class LIMit(SCPINode, SCPISet):
                """
                `MMEMory:STORe:LIMit
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_LIMit>`_

                Arguments: 'string'
                """
                _cmd = "LIMit"
                args = ["'string'"]

            LIMit = LIMit()
            """
            `MMEMory:STORe:LIMit
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_LIMit>`_

            Arguments: 'string'
            """

            class MARKer(SCPINode, SCPISet):
                """
                `MMEMory:STORe:MARKer
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_MARKer>`_

                Arguments: 'string'
                """
                _cmd = "MARKer"
                args = ["'string'"]

            MARKer = MARKer()
            """
            `MMEMory:STORe:MARKer
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_MARKer>`_

            Arguments: 'string'
            """

            class MDCData(SCPINode, SCPISet):
                """
                `MMEMory:STORe:MDCData
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_MDCData>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "MDCData"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            MDCData = MDCData()
            """
            `MMEMory:STORe:MDCData
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_MDCData>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class PTRain(SCPINode, SCPISet):
                """
                `MMEMory:STORe:PTRain
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_PTRain>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "PTRain"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            PTRain = PTRain()
            """
            `MMEMory:STORe:PTRain
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_PTRain>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class RIPPle(SCPINode, SCPISet):
                """
                `MMEMory:STORe:RIPPle
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_RIPPle>`_

                Arguments: 'string'
                """
                _cmd = "RIPPle"
                args = ["'string'"]

            RIPPle = RIPPle()
            """
            `MMEMory:STORe:RIPPle
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_RIPPle>`_

            Arguments: 'string'
            """

            class SEGMent(SCPINode, SCPISet):
                """
                `MMEMory:STORe:SEGMent
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_SEGMent>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SEGMent"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            SEGMent = SEGMent()
            """
            `MMEMory:STORe:SEGMent
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_SEGMent>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class STATe(SCPINode, SCPISet):
                """
                `MMEMory:STORe:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_STATe>`_

                Arguments: 1
                """
                _cmd = "STATe"
                args = ["1"]

            STATe = STATe()
            """
            `MMEMory:STORe:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_STATe>`_

            Arguments: 1
            """

            class TRACe(SCPINode, SCPISet):
                """
                `MMEMory:STORe:TRACe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_TRACE>`_

                Arguments: 'string'
                """
                _cmd = "TRACe"
                args = ["'string'"]

                class CHANnel(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:TRACe:CHANnel
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_TRACE_CHANnel>`_

                    Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "CHANnel"
                    args = ["1", "ALL", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                CHANnel = CHANnel()
                """
                `MMEMory:STORe:TRACe:CHANnel
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_TRACE_CHANnel>`_

                Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class PORTs(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:TRACe:PORTs
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_TRACE_PORTs>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "PORTs"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    class INComplete(SCPINode, SCPISet):
                        """
                        `MMEMory:STORe:TRACe:PORTs:INComplete
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_TRACE_PORTs_INComplete>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "INComplete"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    INComplete = INComplete()
                    """
                    `MMEMory:STORe:TRACe:PORTs:INComplete
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_TRACE_PORTs_INComplete>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                PORTs = PORTs()
                """
                `MMEMory:STORe:TRACe:PORTs
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_TRACE_PORTs>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            TRACe = TRACe()
            """
            `MMEMory:STORe:TRACe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/mmemory/mmemory.htm#STORe_TRACE>`_

            Arguments: 'string'
            """

        STORe = STORe()
        """
        MMEMory:STORe

        Arguments:
        """

    MMEMory = MMEMory()
    """
    MMEMory

    Arguments:
    """

    class OUTPut(SCPINodeN, SCPIBool):
        """
        OUTPut

        Arguments: 1, OFF, ON
        """
        _cmd = "OUTPut"
        args = ["1", "OFF", "ON"]

        class ATTenuation(SCPINode, SCPIQuery, SCPISet):
            """
            `OUTPut:ATTenuation
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#Attenuation>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "ATTenuation"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

        ATTenuation = ATTenuation()
        """
        `OUTPut:ATTenuation
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#Attenuation>`_

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class DPORt(SCPINode, SCPIQuery, SCPISet):
            """
            `OUTPut:DPORt
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#DPORt>`_

            Arguments: PORT1, PORT2, PORT3, PORT4
            """
            _cmd = "DPORt"
            args = ["PORT1", "PORT2", "PORT3", "PORT4"]

        DPORt = DPORt()
        """
        `OUTPut:DPORt
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#DPORt>`_

        Arguments: PORT1, PORT2, PORT3, PORT4
        """

        class STATe(SCPINode, SCPIBool):
            """
            `OUTPut:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#DPORt>`_

            Arguments: 1, OFF, ON
            """
            _cmd = "STATe"
            args = ["1", "OFF", "ON"]

            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `OUTPut:STATe:TYPE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#STATe_TYPE>`_

                Arguments: FAST, LBNoise
                """
                _cmd = "TYPE"
                args = ["FAST", "LBNoise"]

            TYPE = TYPE()
            """
            `OUTPut:STATe:TYPE
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#STATe_TYPE>`_

            Arguments: FAST, LBNoise
            """

        STATe = STATe()
        """
        `OUTPut:STATe
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#DPORt>`_

        Arguments: 1, OFF, ON
        """

        class UPORt(SCPINode, SCPIQuery):
            """
            OUTPut:UPORt

            Arguments:
            """
            _cmd = "UPORt"
            args = []

            class BUSY(SCPINode):
                """
                OUTPut:UPORt:BUSY

                Arguments:
                """
                _cmd = "BUSY"
                args = []

                class LINK(SCPINode, SCPIQuery, SCPISet):
                    """
                    `OUTPut:UPORt:BUSY:LINK
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#UPORt_BUSY_LINK>`_

                    Arguments: AUTO, POINt, PPOint, SEGMent, SWEep
                    """
                    _cmd = "LINK"
                    args = ["AUTO", "POINt", "PPOint", "SEGMent", "SWEep"]

                LINK = LINK()
                """
                `OUTPut:UPORt:BUSY:LINK
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#UPORt_BUSY_LINK>`_

                Arguments: AUTO, POINt, PPOint, SEGMent, SWEep
                """

            BUSY = BUSY()
            """
            OUTPut:UPORt:BUSY

            Arguments:
            """

            class ECBits(SCPINode, SCPIBool):
                """
                `OUTPut:UPORt:ECBits
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#UPORt_ECBits>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "ECBits"
                args = ["1", "OFF", "ON"]

            ECBits = ECBits()
            """
            `OUTPut:UPORt:ECBits
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#UPORt_ECBits>`_

            Arguments: 1, OFF, ON
            """

            class SEGMent(SCPINodeN, SCPIQuery):
                """
                OUTPut:UPORt:SEGMent

                Arguments:
                """
                _cmd = "SEGMent"
                args = []

                class STATe(SCPINode, SCPIBool):
                    """
                    `OUTPut:UPORt:SEGMent:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#UPORt_SEGMent_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `OUTPut:UPORt:SEGMent:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#UPORt_SEGMent_STATe>`_

                Arguments: 1, OFF, ON
                """

                class VALue(SCPINode, SCPIQuery):
                    """
                    `OUTPut:UPORt:SEGMent:VALue
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#UPORt_SEGMent_VALue>`_

                    Arguments:
                    """
                    _cmd = "VALue"
                    args = []

                VALue = VALue()
                """
                `OUTPut:UPORt:SEGMent:VALue
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#UPORt_SEGMent_VALue>`_

                Arguments:
                """

            SEGMent = SEGMent()
            """
            OUTPut:UPORt:SEGMent

            Arguments:
            """

            class VALue(SCPINode, SCPIQuery):
                """
                `OUTPut:UPORt:VALue
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#UPORt_VALue>`_

                Arguments:
                """
                _cmd = "VALue"
                args = []

            VALue = VALue()
            """
            `OUTPut:UPORt:VALue
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/output/output.htm#UPORt_VALue>`_

            Arguments:
            """

        UPORt = UPORt()
        """
        OUTPut:UPORt

        Arguments:
        """

    OUTPut = OUTPut()
    """
    OUTPut

    Arguments: 1, OFF, ON
    """

    class PROGram(SCPINode):
        """
        PROGram

        Arguments:
        """
        _cmd = "PROGram"
        args = []

        class SELected(SCPINode):
            """
            PROGram:SELected

            Arguments:
            """
            _cmd = "SELected"
            args = []

            class EXECute(SCPINode, SCPISet):
                """
                `PROGram:SELected:EXECute
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#EXECute>`_

                Arguments: 'string'
                """
                _cmd = "EXECute"
                args = ["'string'"]

            EXECute = EXECute()
            """
            `PROGram:SELected:EXECute
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#EXECute>`_

            Arguments: 'string'
            """

            class INIMessage(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:INIMessage
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#INIMessage>`_

                Arguments: 'string'
                """
                _cmd = "INIMessage"
                args = ["'string'"]

            INIMessage = INIMessage()
            """
            `PROGram:SELected:INIMessage
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#INIMessage>`_

            Arguments: 'string'
            """

            class INIParameter(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:INIParameter
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#INIParameter>`_

                Arguments: 'string'
                """
                _cmd = "INIParameter"
                args = ["'string'"]

            INIParameter = INIParameter()
            """
            `PROGram:SELected:INIParameter
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#INIParameter>`_

            Arguments: 'string'
            """

            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:NAME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#NAME>`_

                Arguments: PROG
                """
                _cmd = "NAME"
                args = ["PROG"]

            NAME = NAME()
            """
            `PROGram:SELected:NAME
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#NAME>`_

            Arguments: PROG
            """

            class RETVal(SCPINode, SCPIQuery):
                """
                `PROGram:SELected:RETVal
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#RETVal>`_

                Arguments:
                """
                _cmd = "RETVal"
                args = []

            RETVal = RETVal()
            """
            `PROGram:SELected:RETVal
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#RETVal>`_

            Arguments:
            """

            class STRing(SCPINode, SCPIQuery, SCPISet):
                """
                PROGram:SELected:STRing

                Arguments: 'string'
                """
                _cmd = "STRing"
                args = ["'string'"]

            STRing = STRing()
            """
            PROGram:SELected:STRing

            Arguments: 'string'
            """

            class WAIT(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:WAIT
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#WAIT>`_

                Arguments:
                """
                _cmd = "WAIT"
                args = []

            WAIT = WAIT()
            """
            `PROGram:SELected:WAIT
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/program/program.htm#WAIT>`_

            Arguments:
            """

        SELected = SELected()
        """
        PROGram:SELected

        Arguments:
        """

    PROGram = PROGram()
    """
    PROGram

    Arguments:
    """

    class ROUTe(SCPINodeN):
        """
        ROUTe

        Arguments:
        """
        _cmd = "ROUTe"
        args = []

        class CFILe(SCPINode, SCPIBool):
            """
            `ROUTe:CFILe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/route/route.htm#CFILe>`_

            Arguments: 1, OFF, ON
            """
            _cmd = "CFILe"
            args = ["1", "OFF", "ON"]

        CFILe = CFILe()
        """
        `ROUTe:CFILe
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/route/route.htm#CFILe>`_

        Arguments: 1, OFF, ON
        """

        class PORTs(SCPINodeN, SCPIQuery, SCPISet):
            """
            `ROUTe:PORTs
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/route/route.htm#PORTs>`_

            Arguments: A, B, C, D
            """
            _cmd = "PORTs"
            args = ["A", "B", "C", "D"]

        PORTs = PORTs()
        """
        `ROUTe:PORTs
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/route/route.htm#PORTs>`_

        Arguments: A, B, C, D
        """

    ROUTe = ROUTe()
    """
    ROUTe

    Arguments:
    """

    class SENSe(SCPINodeN):
        """
        SENSe

        Arguments:
        """
        _cmd = "SENSe"
        args = []

        class AVERage(SCPINode, SCPIBool):
            """
            `SENSe:AVERage
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___average.htm>`_

            Arguments: 1, OFF, ON
            """
            _cmd = "AVERage"
            args = ["1", "OFF", "ON"]

            class CLEar(SCPINode, SCPISet):
                """
                `SENSe:AVERage:CLEar
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___average.htm#CLEar>`_

                Arguments:
                """
                _cmd = "CLEar"
                args = []

            CLEar = CLEar()
            """
            `SENSe:AVERage:CLEar
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___average.htm#CLEar>`_

            Arguments:
            """

            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:AVERage:COUNt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___average.htm#Count>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "COUNt"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class ACTual(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:AVERage:COUNt:ACTual

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "ACTual"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                ACTual = ACTual()
                """
                SENSe:AVERage:COUNt:ACTual

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class CURRent(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:AVERage:COUNt:CURRent
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___average.htm#Count_CURRent>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "CURRent"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                CURRent = CURRent()
                """
                `SENSe:AVERage:COUNt:CURRent
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___average.htm#Count_CURRent>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            COUNt = COUNt()
            """
            `SENSe:AVERage:COUNt
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___average.htm#Count>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SENSe:AVERage:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___average.htm#State>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `SENSe:AVERage:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___average.htm#State>`_

            Arguments: 1, OFF, ON
            """

        AVERage = AVERage()
        """
        `SENSe:AVERage
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___average.htm>`_

        Arguments: 1, OFF, ON
        """

        class BANDwidth(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:BANDwidth

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "BANDwidth"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            class RESolution(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:BANDwidth:RESolution

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "RESolution"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class DREDuction(SCPINode, SCPIBool):
                    """
                    SENSe:BANDwidth:RESolution:DREDuction

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "DREDuction"
                    args = ["1", "OFF", "ON"]

                DREDuction = DREDuction()
                """
                SENSe:BANDwidth:RESolution:DREDuction

                Arguments: 1, OFF, ON
                """

                class GENerator(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:BANDwidth:RESolution:GENerator

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "GENerator"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                GENerator = GENerator()
                """
                SENSe:BANDwidth:RESolution:GENerator

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:BANDwidth:RESolution:MODE

                    Arguments: PALL, PSPecific
                    """
                    _cmd = "MODE"
                    args = ["PALL", "PSPecific"]

                MODE = MODE()
                """
                SENSe:BANDwidth:RESolution:MODE

                Arguments: PALL, PSPecific
                """

                class PORT(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:BANDwidth:RESolution:PORT

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "PORT"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                PORT = PORT()
                """
                SENSe:BANDwidth:RESolution:PORT

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:BANDwidth:RESolution:SELect

                    Arguments: HIGH, NORMal
                    """
                    _cmd = "SELect"
                    args = ["HIGH", "NORMal"]

                SELect = SELect()
                """
                SENSe:BANDwidth:RESolution:SELect

                Arguments: HIGH, NORMal
                """

            RESolution = RESolution()
            """
            SENSe:BANDwidth:RESolution

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        BANDwidth = BANDwidth()
        """
        SENSe:BANDwidth

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class BWIDth(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:BWIDth

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "BWIDth"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            class RESolution(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:BWIDth:RESolution

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "RESolution"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class DREDuction(SCPINode, SCPIBool):
                    """
                    SENSe:BWIDth:RESolution:DREDuction

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "DREDuction"
                    args = ["1", "OFF", "ON"]

                DREDuction = DREDuction()
                """
                SENSe:BWIDth:RESolution:DREDuction

                Arguments: 1, OFF, ON
                """

                class GENerator(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:BWIDth:RESolution:GENerator

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "GENerator"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                GENerator = GENerator()
                """
                SENSe:BWIDth:RESolution:GENerator

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:BWIDth:RESolution:MODE

                    Arguments: PALL, PSPecific
                    """
                    _cmd = "MODE"
                    args = ["PALL", "PSPecific"]

                MODE = MODE()
                """
                SENSe:BWIDth:RESolution:MODE

                Arguments: PALL, PSPecific
                """

                class PORT(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:BWIDth:RESolution:PORT

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "PORT"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                PORT = PORT()
                """
                SENSe:BWIDth:RESolution:PORT

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:BWIDth:RESolution:SELect

                    Arguments: HIGH, NORMal
                    """
                    _cmd = "SELect"
                    args = ["HIGH", "NORMal"]

                SELect = SELect()
                """
                SENSe:BWIDth:RESolution:SELect

                Arguments: HIGH, NORMal
                """

            RESolution = RESolution()
            """
            SENSe:BWIDth:RESolution

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        BWIDth = BWIDth()
        """
        SENSe:BWIDth

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class CONVerter(SCPINode):
            """
            SENSe:CONVerter

            Arguments:
            """
            _cmd = "CONVerter"
            args = []

            class AMODel(SCPINode, SCPIBool):
                """
                `SENSe:CONVerter:AMODel
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_converter.htm#AMODel>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "AMODel"
                args = ["1", "OFF", "ON"]

            AMODel = AMODel()
            """
            `SENSe:CONVerter:AMODel
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_converter.htm#AMODel>`_

            Arguments: 1, OFF, ON
            """

            class ASSign(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:CONVerter:ASSign
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_converter.htm#ASSign>`_

                Arguments: 'string'
                """
                _cmd = "ASSign"
                args = ["'string'"]

            ASSign = ASSign()
            """
            `SENSe:CONVerter:ASSign
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_converter.htm#ASSign>`_

            Arguments: 'string'
            """

            class DESCription(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CONVerter:DESCription
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_converter.htm#DESCription>`_

                Arguments: DSET, ELECtronic, LAPProx, NONE
                """
                _cmd = "DESCription"
                args = ["DSET", "ELECtronic", "LAPProx", "NONE"]

            DESCription = DESCription()
            """
            `SENSe:CONVerter:DESCription
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_converter.htm#DESCription>`_

            Arguments: DSET, ELECtronic, LAPProx, NONE
            """

            class PATH(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CONVerter:PATH
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_converter.htm#PATH>`_

                Arguments: 'string'
                """
                _cmd = "PATH"
                args = ["'string'"]

            PATH = PATH()
            """
            `SENSe:CONVerter:PATH
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_converter.htm#PATH>`_

            Arguments: 'string'
            """

        CONVerter = CONVerter()
        """
        SENSe:CONVerter

        Arguments:
        """

        class CORRection(SCPINode, SCPIBool):
            """
            SENSe:CORRection

            Arguments: 1, OFF, ON
            """
            _cmd = "CORRection"
            args = ["1", "OFF", "ON"]

            class CBFReq(SCPINode, SCPIBool):
                """
                SENSe:CORRection:CBFReq

                Arguments: 1, OFF, ON
                """
                _cmd = "CBFReq"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:CORRection:CBFReq:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction.htm#CBFReq>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:CORRection:CBFReq:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction.htm#CBFReq>`_

                Arguments: 1, OFF, ON
                """

            CBFReq = CBFReq()
            """
            SENSe:CORRection:CBFReq

            Arguments: 1, OFF, ON
            """

            class CDATa(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:CDATa
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction.htm#CDATa>`_

                Arguments: 'string'
                """
                _cmd = "CDATa"
                args = ["'string'"]

            CDATa = CDATa()
            """
            `SENSe:CORRection:CDATa
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction.htm#CDATa>`_

            Arguments: 'string'
            """

            class CKIT(SCPINode):
                """
                SENSe:CORRection:CKIT

                Arguments:
                """
                _cmd = "CKIT"
                args = []

                class CATalog(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:CATalog
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#CATalog>`_

                    Arguments: 'string'
                    """
                    _cmd = "CATalog"
                    args = ["'string'"]

                CATalog = CATalog()
                """
                `SENSe:CORRection:CKIT:CATalog
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#CATalog>`_

                Arguments: 'string'
                """

                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:DELete
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#DELete>`_

                    Arguments: 'string'
                    """
                    _cmd = "DELete"
                    args = ["'string'"]

                DELete = DELete()
                """
                `SENSe:CORRection:CKIT:DELete
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#DELete>`_

                Arguments: 'string'
                """

                class FFATten(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFATten

                    Arguments: 'string'
                    """
                    _cmd = "FFATten"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFATten:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:FFATten:WLABel

                    Arguments: 'string'
                    """

                FFATten = FFATten()
                """
                SENSe:CORRection:CKIT:FFATten

                Arguments: 'string'
                """

                class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFLine

                    Arguments: 'string'
                    """
                    _cmd = "FFLine"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFLine:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:FFLine:WLABel

                    Arguments: 'string'
                    """

                FFLine = FFLine()
                """
                SENSe:CORRection:CKIT:FFLine

                Arguments: 'string'
                """

                class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFSNetwork

                    Arguments: 'string'
                    """
                    _cmd = "FFSNetwork"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFSNetwork:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:FFSNetwork:WLABel

                    Arguments: 'string'
                    """

                FFSNetwork = FFSNetwork()
                """
                SENSe:CORRection:CKIT:FFSNetwork

                Arguments: 'string'
                """

                class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFTHrough

                    Arguments: 'string'
                    """
                    _cmd = "FFTHrough"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFTHrough:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:FFTHrough:WLABel

                    Arguments: 'string'
                    """

                FFTHrough = FFTHrough()
                """
                SENSe:CORRection:CKIT:FFTHrough

                Arguments: 'string'
                """

                class FMTCh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FMTCh

                    Arguments: 'string'
                    """
                    _cmd = "FMTCh"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FMTCh:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:FMTCh:WLABel

                    Arguments: 'string'
                    """

                FMTCh = FMTCh()
                """
                SENSe:CORRection:CKIT:FMTCh

                Arguments: 'string'
                """

                class FOPen(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FOPen

                    Arguments: 'string'
                    """
                    _cmd = "FOPen"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FOPen:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:FOPen:WLABel

                    Arguments: 'string'
                    """

                FOPen = FOPen()
                """
                SENSe:CORRection:CKIT:FOPen

                Arguments: 'string'
                """

                class FOSHort(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FOSHort

                    Arguments: 'string'
                    """
                    _cmd = "FOSHort"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FOSHort:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:FOSHort:WLABel

                    Arguments: 'string'
                    """

                FOSHort = FOSHort()
                """
                SENSe:CORRection:CKIT:FOSHort

                Arguments: 'string'
                """

                class FREFlect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FREFlect

                    Arguments: 'string'
                    """
                    _cmd = "FREFlect"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FREFlect:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:FREFlect:WLABel

                    Arguments: 'string'
                    """

                FREFlect = FREFlect()
                """
                SENSe:CORRection:CKIT:FREFlect

                Arguments: 'string'
                """

                class FSHort(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FSHort

                    Arguments: 'string'
                    """
                    _cmd = "FSHort"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FSHort:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:FSHort:WLABel

                    Arguments: 'string'
                    """

                FSHort = FSHort()
                """
                SENSe:CORRection:CKIT:FSHort

                Arguments: 'string'
                """

                class FSMatch(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FSMatch

                    Arguments: 'string'
                    """
                    _cmd = "FSMatch"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FSMatch:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:FSMatch:WLABel

                    Arguments: 'string'
                    """

                FSMatch = FSMatch()
                """
                SENSe:CORRection:CKIT:FSMatch

                Arguments: 'string'
                """

                class INSTall(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:INSTall
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#INSTall>`_

                    Arguments: 'string'
                    """
                    _cmd = "INSTall"
                    args = ["'string'"]

                INSTall = INSTall()
                """
                `SENSe:CORRection:CKIT:INSTall
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#INSTall>`_

                Arguments: 'string'
                """

                class LABel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LABel
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#LABel>`_

                    Arguments: 'string'
                    """
                    _cmd = "LABel"
                    args = ["'string'"]

                LABel = LABel()
                """
                `SENSe:CORRection:CKIT:LABel
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#LABel>`_

                Arguments: 'string'
                """

                class LCATalog(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LCATalog
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit_l(abel).htm#CATalog>`_

                    Arguments: 'string'
                    """
                    _cmd = "LCATalog"
                    args = ["'string'"]

                LCATalog = LCATalog()
                """
                `SENSe:CORRection:CKIT:LCATalog
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit_l(abel).htm#CATalog>`_

                Arguments: 'string'
                """

                class LDELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LDELete
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit_l(abel).htm#DELete>`_

                    Arguments: 'string'
                    """
                    _cmd = "LDELete"
                    args = ["'string'"]

                LDELete = LDELete()
                """
                `SENSe:CORRection:CKIT:LDELete
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit_l(abel).htm#DELete>`_

                Arguments: 'string'
                """

                class LLABel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LLABel
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit_l(abel).htm#LABel>`_

                    Arguments: 'string'
                    """
                    _cmd = "LLABel"
                    args = ["'string'"]

                LLABel = LLABel()
                """
                `SENSe:CORRection:CKIT:LLABel
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit_l(abel).htm#LABel>`_

                Arguments: 'string'
                """

                class LSELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LSELect
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit_l(abel).htm#SELect_String>`_

                    Arguments: 'string'
                    """
                    _cmd = "LSELect"
                    args = ["'string'"]

                LSELect = LSELect()
                """
                `SENSe:CORRection:CKIT:LSELect
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit_l(abel).htm#SELect_String>`_

                Arguments: 'string'
                """

                class MDATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:MDATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#MDATe>`_

                    Arguments: 'string'
                    """
                    _cmd = "MDATe"
                    args = ["'string'"]

                MDATe = MDATe()
                """
                `SENSe:CORRection:CKIT:MDATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#MDATe>`_

                Arguments: 'string'
                """

                class MFATten(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFATten

                    Arguments: 'string'
                    """
                    _cmd = "MFATten"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFATten:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MFATten:WLABel

                    Arguments: 'string'
                    """

                MFATten = MFATten()
                """
                SENSe:CORRection:CKIT:MFATten

                Arguments: 'string'
                """

                class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFLine

                    Arguments: 'string'
                    """
                    _cmd = "MFLine"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFLine:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MFLine:WLABel

                    Arguments: 'string'
                    """

                MFLine = MFLine()
                """
                SENSe:CORRection:CKIT:MFLine

                Arguments: 'string'
                """

                class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFSNetwork

                    Arguments: 'string'
                    """
                    _cmd = "MFSNetwork"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFSNetwork:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MFSNetwork:WLABel

                    Arguments: 'string'
                    """

                MFSNetwork = MFSNetwork()
                """
                SENSe:CORRection:CKIT:MFSNetwork

                Arguments: 'string'
                """

                class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFTHrough

                    Arguments: 'string'
                    """
                    _cmd = "MFTHrough"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFTHrough:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MFTHrough:WLABel

                    Arguments: 'string'
                    """

                MFTHrough = MFTHrough()
                """
                SENSe:CORRection:CKIT:MFTHrough

                Arguments: 'string'
                """

                class MMATten(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMATten

                    Arguments: 'string'
                    """
                    _cmd = "MMATten"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMATten:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MMATten:WLABel

                    Arguments: 'string'
                    """

                MMATten = MMATten()
                """
                SENSe:CORRection:CKIT:MMATten

                Arguments: 'string'
                """

                class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMLine

                    Arguments: 'string'
                    """
                    _cmd = "MMLine"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMLine:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MMLine:WLABel

                    Arguments: 'string'
                    """

                MMLine = MMLine()
                """
                SENSe:CORRection:CKIT:MMLine

                Arguments: 'string'
                """

                class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMSNetwork

                    Arguments: 'string'
                    """
                    _cmd = "MMSNetwork"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMSNetwork:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MMSNetwork:WLABel

                    Arguments: 'string'
                    """

                MMSNetwork = MMSNetwork()
                """
                SENSe:CORRection:CKIT:MMSNetwork

                Arguments: 'string'
                """

                class MMTCh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMTCh

                    Arguments: 'string'
                    """
                    _cmd = "MMTCh"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMTCh:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MMTCh:WLABel

                    Arguments: 'string'
                    """

                MMTCh = MMTCh()
                """
                SENSe:CORRection:CKIT:MMTCh

                Arguments: 'string'
                """

                class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMTHrough

                    Arguments: 'string'
                    """
                    _cmd = "MMTHrough"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMTHrough:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MMTHrough:WLABel

                    Arguments: 'string'
                    """

                MMTHrough = MMTHrough()
                """
                SENSe:CORRection:CKIT:MMTHrough

                Arguments: 'string'
                """

                class MOPen(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MOPen

                    Arguments: 'string'
                    """
                    _cmd = "MOPen"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MOPen:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MOPen:WLABel

                    Arguments: 'string'
                    """

                MOPen = MOPen()
                """
                SENSe:CORRection:CKIT:MOPen

                Arguments: 'string'
                """

                class MOSHort(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MOSHort

                    Arguments: 'string'
                    """
                    _cmd = "MOSHort"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MOSHort:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MOSHort:WLABel

                    Arguments: 'string'
                    """

                MOSHort = MOSHort()
                """
                SENSe:CORRection:CKIT:MOSHort

                Arguments: 'string'
                """

                class MREFlect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MREFlect

                    Arguments: 'string'
                    """
                    _cmd = "MREFlect"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MREFlect:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MREFlect:WLABel

                    Arguments: 'string'
                    """

                MREFlect = MREFlect()
                """
                SENSe:CORRection:CKIT:MREFlect

                Arguments: 'string'
                """

                class MSHort(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MSHort

                    Arguments: 'string'
                    """
                    _cmd = "MSHort"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MSHort:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MSHort:WLABel

                    Arguments: 'string'
                    """

                MSHort = MSHort()
                """
                SENSe:CORRection:CKIT:MSHort

                Arguments: 'string'
                """

                class MSMatch(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MSMatch

                    Arguments: 'string'
                    """
                    _cmd = "MSMatch"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MSMatch:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:MSMatch:WLABel

                    Arguments: 'string'
                    """

                MSMatch = MSMatch()
                """
                SENSe:CORRection:CKIT:MSMatch

                Arguments: 'string'
                """

                class N(SCPINodeN):
                    """
                    SENSe:CORRection:CKIT:N

                    Arguments:
                    """
                    _cmd = "N"
                    args = []

                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFATten

                        Arguments: 'string'
                        """
                        _cmd = "FFATten"
                        args = ["'string'"]

                    FFATten = FFATten()
                    """
                    SENSe:CORRection:CKIT:N:FFATten

                    Arguments: 'string'
                    """

                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFLine

                        Arguments: 'string'
                        """
                        _cmd = "FFLine"
                        args = ["'string'"]

                    FFLine = FFLine()
                    """
                    SENSe:CORRection:CKIT:N:FFLine

                    Arguments: 'string'
                    """

                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "FFSNetwork"
                        args = ["'string'"]

                    FFSNetwork = FFSNetwork()
                    """
                    SENSe:CORRection:CKIT:N:FFSNetwork

                    Arguments: 'string'
                    """

                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFTHrough

                        Arguments: 'string'
                        """
                        _cmd = "FFTHrough"
                        args = ["'string'"]

                    FFTHrough = FFTHrough()
                    """
                    SENSe:CORRection:CKIT:N:FFTHrough

                    Arguments: 'string'
                    """

                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FMTCh

                        Arguments: 'string'
                        """
                        _cmd = "FMTCh"
                        args = ["'string'"]

                    FMTCh = FMTCh()
                    """
                    SENSe:CORRection:CKIT:N:FMTCh

                    Arguments: 'string'
                    """

                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FOPen

                        Arguments: 'string'
                        """
                        _cmd = "FOPen"
                        args = ["'string'"]

                    FOPen = FOPen()
                    """
                    SENSe:CORRection:CKIT:N:FOPen

                    Arguments: 'string'
                    """

                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FREFlect

                        Arguments: 'string'
                        """
                        _cmd = "FREFlect"
                        args = ["'string'"]

                    FREFlect = FREFlect()
                    """
                    SENSe:CORRection:CKIT:N:FREFlect

                    Arguments: 'string'
                    """

                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FSHort

                        Arguments: 'string'
                        """
                        _cmd = "FSHort"
                        args = ["'string'"]

                    FSHort = FSHort()
                    """
                    SENSe:CORRection:CKIT:N:FSHort

                    Arguments: 'string'
                    """

                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FSMatch

                        Arguments: 'string'
                        """
                        _cmd = "FSMatch"
                        args = ["'string'"]

                    FSMatch = FSMatch()
                    """
                    SENSe:CORRection:CKIT:N:FSMatch

                    Arguments: 'string'
                    """

                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:LSELect

                        Arguments: 'string'
                        """
                        _cmd = "LSELect"
                        args = ["'string'"]

                    LSELect = LSELect()
                    """
                    SENSe:CORRection:CKIT:N:LSELect

                    Arguments: 'string'
                    """

                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFATten

                        Arguments: 'string'
                        """
                        _cmd = "MFATten"
                        args = ["'string'"]

                    MFATten = MFATten()
                    """
                    SENSe:CORRection:CKIT:N:MFATten

                    Arguments: 'string'
                    """

                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFLine

                        Arguments: 'string'
                        """
                        _cmd = "MFLine"
                        args = ["'string'"]

                    MFLine = MFLine()
                    """
                    SENSe:CORRection:CKIT:N:MFLine

                    Arguments: 'string'
                    """

                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "MFSNetwork"
                        args = ["'string'"]

                    MFSNetwork = MFSNetwork()
                    """
                    SENSe:CORRection:CKIT:N:MFSNetwork

                    Arguments: 'string'
                    """

                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFTHrough

                        Arguments: 'string'
                        """
                        _cmd = "MFTHrough"
                        args = ["'string'"]

                    MFTHrough = MFTHrough()
                    """
                    SENSe:CORRection:CKIT:N:MFTHrough

                    Arguments: 'string'
                    """

                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMATten

                        Arguments: 'string'
                        """
                        _cmd = "MMATten"
                        args = ["'string'"]

                    MMATten = MMATten()
                    """
                    SENSe:CORRection:CKIT:N:MMATten

                    Arguments: 'string'
                    """

                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMLine

                        Arguments: 'string'
                        """
                        _cmd = "MMLine"
                        args = ["'string'"]

                    MMLine = MMLine()
                    """
                    SENSe:CORRection:CKIT:N:MMLine

                    Arguments: 'string'
                    """

                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "MMSNetwork"
                        args = ["'string'"]

                    MMSNetwork = MMSNetwork()
                    """
                    SENSe:CORRection:CKIT:N:MMSNetwork

                    Arguments: 'string'
                    """

                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMTCh

                        Arguments: 'string'
                        """
                        _cmd = "MMTCh"
                        args = ["'string'"]

                    MMTCh = MMTCh()
                    """
                    SENSe:CORRection:CKIT:N:MMTCh

                    Arguments: 'string'
                    """

                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMTHrough

                        Arguments: 'string'
                        """
                        _cmd = "MMTHrough"
                        args = ["'string'"]

                    MMTHrough = MMTHrough()
                    """
                    SENSe:CORRection:CKIT:N:MMTHrough

                    Arguments: 'string'
                    """

                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MOPen

                        Arguments: 'string'
                        """
                        _cmd = "MOPen"
                        args = ["'string'"]

                    MOPen = MOPen()
                    """
                    SENSe:CORRection:CKIT:N:MOPen

                    Arguments: 'string'
                    """

                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MREFlect

                        Arguments: 'string'
                        """
                        _cmd = "MREFlect"
                        args = ["'string'"]

                    MREFlect = MREFlect()
                    """
                    SENSe:CORRection:CKIT:N:MREFlect

                    Arguments: 'string'
                    """

                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MSHort

                        Arguments: 'string'
                        """
                        _cmd = "MSHort"
                        args = ["'string'"]

                    MSHort = MSHort()
                    """
                    SENSe:CORRection:CKIT:N:MSHort

                    Arguments: 'string'
                    """

                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MSMatch

                        Arguments: 'string'
                        """
                        _cmd = "MSMatch"
                        args = ["'string'"]

                    MSMatch = MSMatch()
                    """
                    SENSe:CORRection:CKIT:N:MSMatch

                    Arguments: 'string'
                    """

                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:SELect

                        Arguments: 'string'
                        """
                        _cmd = "SELect"
                        args = ["'string'"]

                    SELect = SELect()
                    """
                    SENSe:CORRection:CKIT:N:SELect

                    Arguments: 'string'
                    """

                N = N()
                """
                SENSe:CORRection:CKIT:N

                Arguments:
                """

                class OSHort(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:OSHort

                    Arguments: 'string'
                    """
                    _cmd = "OSHort"
                    args = ["'string'"]

                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:OSHort:WLABel

                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]

                    WLABel = WLABel()
                    """
                    SENSe:CORRection:CKIT:OSHort:WLABel

                    Arguments: 'string'
                    """

                OSHort = OSHort()
                """
                SENSe:CORRection:CKIT:OSHort

                Arguments: 'string'
                """

                class PC(SCPINodeN):
                    """
                    SENSe:CORRection:CKIT:PC

                    Arguments:
                    """
                    _cmd = "PC"
                    args = []

                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFATten

                        Arguments: 'string'
                        """
                        _cmd = "FFATten"
                        args = ["'string'"]

                    FFATten = FFATten()
                    """
                    SENSe:CORRection:CKIT:PC:FFATten

                    Arguments: 'string'
                    """

                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFLine

                        Arguments: 'string'
                        """
                        _cmd = "FFLine"
                        args = ["'string'"]

                    FFLine = FFLine()
                    """
                    SENSe:CORRection:CKIT:PC:FFLine

                    Arguments: 'string'
                    """

                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "FFSNetwork"
                        args = ["'string'"]

                    FFSNetwork = FFSNetwork()
                    """
                    SENSe:CORRection:CKIT:PC:FFSNetwork

                    Arguments: 'string'
                    """

                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFTHrough

                        Arguments: 'string'
                        """
                        _cmd = "FFTHrough"
                        args = ["'string'"]

                    FFTHrough = FFTHrough()
                    """
                    SENSe:CORRection:CKIT:PC:FFTHrough

                    Arguments: 'string'
                    """

                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FMTCh

                        Arguments: 'string'
                        """
                        _cmd = "FMTCh"
                        args = ["'string'"]

                    FMTCh = FMTCh()
                    """
                    SENSe:CORRection:CKIT:PC:FMTCh

                    Arguments: 'string'
                    """

                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FOPen

                        Arguments: 'string'
                        """
                        _cmd = "FOPen"
                        args = ["'string'"]

                    FOPen = FOPen()
                    """
                    SENSe:CORRection:CKIT:PC:FOPen

                    Arguments: 'string'
                    """

                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FREFlect

                        Arguments: 'string'
                        """
                        _cmd = "FREFlect"
                        args = ["'string'"]

                    FREFlect = FREFlect()
                    """
                    SENSe:CORRection:CKIT:PC:FREFlect

                    Arguments: 'string'
                    """

                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FSHort

                        Arguments: 'string'
                        """
                        _cmd = "FSHort"
                        args = ["'string'"]

                    FSHort = FSHort()
                    """
                    SENSe:CORRection:CKIT:PC:FSHort

                    Arguments: 'string'
                    """

                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FSMatch

                        Arguments: 'string'
                        """
                        _cmd = "FSMatch"
                        args = ["'string'"]

                    FSMatch = FSMatch()
                    """
                    SENSe:CORRection:CKIT:PC:FSMatch

                    Arguments: 'string'
                    """

                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:LSELect

                        Arguments: 'string'
                        """
                        _cmd = "LSELect"
                        args = ["'string'"]

                    LSELect = LSELect()
                    """
                    SENSe:CORRection:CKIT:PC:LSELect

                    Arguments: 'string'
                    """

                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFATten

                        Arguments: 'string'
                        """
                        _cmd = "MFATten"
                        args = ["'string'"]

                    MFATten = MFATten()
                    """
                    SENSe:CORRection:CKIT:PC:MFATten

                    Arguments: 'string'
                    """

                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFLine

                        Arguments: 'string'
                        """
                        _cmd = "MFLine"
                        args = ["'string'"]

                    MFLine = MFLine()
                    """
                    SENSe:CORRection:CKIT:PC:MFLine

                    Arguments: 'string'
                    """

                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "MFSNetwork"
                        args = ["'string'"]

                    MFSNetwork = MFSNetwork()
                    """
                    SENSe:CORRection:CKIT:PC:MFSNetwork

                    Arguments: 'string'
                    """

                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFTHrough

                        Arguments: 'string'
                        """
                        _cmd = "MFTHrough"
                        args = ["'string'"]

                    MFTHrough = MFTHrough()
                    """
                    SENSe:CORRection:CKIT:PC:MFTHrough

                    Arguments: 'string'
                    """

                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMATten

                        Arguments: 'string'
                        """
                        _cmd = "MMATten"
                        args = ["'string'"]

                    MMATten = MMATten()
                    """
                    SENSe:CORRection:CKIT:PC:MMATten

                    Arguments: 'string'
                    """

                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMLine

                        Arguments: 'string'
                        """
                        _cmd = "MMLine"
                        args = ["'string'"]

                    MMLine = MMLine()
                    """
                    SENSe:CORRection:CKIT:PC:MMLine

                    Arguments: 'string'
                    """

                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "MMSNetwork"
                        args = ["'string'"]

                    MMSNetwork = MMSNetwork()
                    """
                    SENSe:CORRection:CKIT:PC:MMSNetwork

                    Arguments: 'string'
                    """

                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMTCh

                        Arguments: 'string'
                        """
                        _cmd = "MMTCh"
                        args = ["'string'"]

                    MMTCh = MMTCh()
                    """
                    SENSe:CORRection:CKIT:PC:MMTCh

                    Arguments: 'string'
                    """

                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMTHrough

                        Arguments: 'string'
                        """
                        _cmd = "MMTHrough"
                        args = ["'string'"]

                    MMTHrough = MMTHrough()
                    """
                    SENSe:CORRection:CKIT:PC:MMTHrough

                    Arguments: 'string'
                    """

                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MOPen

                        Arguments: 'string'
                        """
                        _cmd = "MOPen"
                        args = ["'string'"]

                    MOPen = MOPen()
                    """
                    SENSe:CORRection:CKIT:PC:MOPen

                    Arguments: 'string'
                    """

                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MREFlect

                        Arguments: 'string'
                        """
                        _cmd = "MREFlect"
                        args = ["'string'"]

                    MREFlect = MREFlect()
                    """
                    SENSe:CORRection:CKIT:PC:MREFlect

                    Arguments: 'string'
                    """

                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MSHort

                        Arguments: 'string'
                        """
                        _cmd = "MSHort"
                        args = ["'string'"]

                    MSHort = MSHort()
                    """
                    SENSe:CORRection:CKIT:PC:MSHort

                    Arguments: 'string'
                    """

                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MSMatch

                        Arguments: 'string'
                        """
                        _cmd = "MSMatch"
                        args = ["'string'"]

                    MSMatch = MSMatch()
                    """
                    SENSe:CORRection:CKIT:PC:MSMatch

                    Arguments: 'string'
                    """

                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:SELect

                        Arguments: 'string'
                        """
                        _cmd = "SELect"
                        args = ["'string'"]

                    SELect = SELect()
                    """
                    SENSe:CORRection:CKIT:PC:SELect

                    Arguments: 'string'
                    """

                PC = PC()
                """
                SENSe:CORRection:CKIT:PC

                Arguments:
                """

                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:SELect
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#SELect_String>`_

                    Arguments: 'string'
                    """
                    _cmd = "SELect"
                    args = ["'string'"]

                SELect = SELect()
                """
                `SENSe:CORRection:CKIT:SELect
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#SELect_String>`_

                Arguments: 'string'
                """

                class SMA(SCPINode):
                    """
                    SENSe:CORRection:CKIT:SMA

                    Arguments:
                    """
                    _cmd = "SMA"
                    args = []

                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFATten

                        Arguments: 'string'
                        """
                        _cmd = "FFATten"
                        args = ["'string'"]

                    FFATten = FFATten()
                    """
                    SENSe:CORRection:CKIT:SMA:FFATten

                    Arguments: 'string'
                    """

                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFLine

                        Arguments: 'string'
                        """
                        _cmd = "FFLine"
                        args = ["'string'"]

                    FFLine = FFLine()
                    """
                    SENSe:CORRection:CKIT:SMA:FFLine

                    Arguments: 'string'
                    """

                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "FFSNetwork"
                        args = ["'string'"]

                    FFSNetwork = FFSNetwork()
                    """
                    SENSe:CORRection:CKIT:SMA:FFSNetwork

                    Arguments: 'string'
                    """

                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFTHrough

                        Arguments: 'string'
                        """
                        _cmd = "FFTHrough"
                        args = ["'string'"]

                    FFTHrough = FFTHrough()
                    """
                    SENSe:CORRection:CKIT:SMA:FFTHrough

                    Arguments: 'string'
                    """

                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FMTCh

                        Arguments: 'string'
                        """
                        _cmd = "FMTCh"
                        args = ["'string'"]

                    FMTCh = FMTCh()
                    """
                    SENSe:CORRection:CKIT:SMA:FMTCh

                    Arguments: 'string'
                    """

                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FOPen

                        Arguments: 'string'
                        """
                        _cmd = "FOPen"
                        args = ["'string'"]

                    FOPen = FOPen()
                    """
                    SENSe:CORRection:CKIT:SMA:FOPen

                    Arguments: 'string'
                    """

                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FREFlect

                        Arguments: 'string'
                        """
                        _cmd = "FREFlect"
                        args = ["'string'"]

                    FREFlect = FREFlect()
                    """
                    SENSe:CORRection:CKIT:SMA:FREFlect

                    Arguments: 'string'
                    """

                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FSHort

                        Arguments: 'string'
                        """
                        _cmd = "FSHort"
                        args = ["'string'"]

                    FSHort = FSHort()
                    """
                    SENSe:CORRection:CKIT:SMA:FSHort

                    Arguments: 'string'
                    """

                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FSMatch

                        Arguments: 'string'
                        """
                        _cmd = "FSMatch"
                        args = ["'string'"]

                    FSMatch = FSMatch()
                    """
                    SENSe:CORRection:CKIT:SMA:FSMatch

                    Arguments: 'string'
                    """

                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:LSELect

                        Arguments: 'string'
                        """
                        _cmd = "LSELect"
                        args = ["'string'"]

                    LSELect = LSELect()
                    """
                    SENSe:CORRection:CKIT:SMA:LSELect

                    Arguments: 'string'
                    """

                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFATten

                        Arguments: 'string'
                        """
                        _cmd = "MFATten"
                        args = ["'string'"]

                    MFATten = MFATten()
                    """
                    SENSe:CORRection:CKIT:SMA:MFATten

                    Arguments: 'string'
                    """

                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFLine

                        Arguments: 'string'
                        """
                        _cmd = "MFLine"
                        args = ["'string'"]

                    MFLine = MFLine()
                    """
                    SENSe:CORRection:CKIT:SMA:MFLine

                    Arguments: 'string'
                    """

                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "MFSNetwork"
                        args = ["'string'"]

                    MFSNetwork = MFSNetwork()
                    """
                    SENSe:CORRection:CKIT:SMA:MFSNetwork

                    Arguments: 'string'
                    """

                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFTHrough

                        Arguments: 'string'
                        """
                        _cmd = "MFTHrough"
                        args = ["'string'"]

                    MFTHrough = MFTHrough()
                    """
                    SENSe:CORRection:CKIT:SMA:MFTHrough

                    Arguments: 'string'
                    """

                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMATten

                        Arguments: 'string'
                        """
                        _cmd = "MMATten"
                        args = ["'string'"]

                    MMATten = MMATten()
                    """
                    SENSe:CORRection:CKIT:SMA:MMATten

                    Arguments: 'string'
                    """

                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMLine

                        Arguments: 'string'
                        """
                        _cmd = "MMLine"
                        args = ["'string'"]

                    MMLine = MMLine()
                    """
                    SENSe:CORRection:CKIT:SMA:MMLine

                    Arguments: 'string'
                    """

                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "MMSNetwork"
                        args = ["'string'"]

                    MMSNetwork = MMSNetwork()
                    """
                    SENSe:CORRection:CKIT:SMA:MMSNetwork

                    Arguments: 'string'
                    """

                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMTCh

                        Arguments: 'string'
                        """
                        _cmd = "MMTCh"
                        args = ["'string'"]

                    MMTCh = MMTCh()
                    """
                    SENSe:CORRection:CKIT:SMA:MMTCh

                    Arguments: 'string'
                    """

                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMTHrough

                        Arguments: 'string'
                        """
                        _cmd = "MMTHrough"
                        args = ["'string'"]

                    MMTHrough = MMTHrough()
                    """
                    SENSe:CORRection:CKIT:SMA:MMTHrough

                    Arguments: 'string'
                    """

                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MOPen

                        Arguments: 'string'
                        """
                        _cmd = "MOPen"
                        args = ["'string'"]

                    MOPen = MOPen()
                    """
                    SENSe:CORRection:CKIT:SMA:MOPen

                    Arguments: 'string'
                    """

                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MREFlect

                        Arguments: 'string'
                        """
                        _cmd = "MREFlect"
                        args = ["'string'"]

                    MREFlect = MREFlect()
                    """
                    SENSe:CORRection:CKIT:SMA:MREFlect

                    Arguments: 'string'
                    """

                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MSHort

                        Arguments: 'string'
                        """
                        _cmd = "MSHort"
                        args = ["'string'"]

                    MSHort = MSHort()
                    """
                    SENSe:CORRection:CKIT:SMA:MSHort

                    Arguments: 'string'
                    """

                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MSMatch

                        Arguments: 'string'
                        """
                        _cmd = "MSMatch"
                        args = ["'string'"]

                    MSMatch = MSMatch()
                    """
                    SENSe:CORRection:CKIT:SMA:MSMatch

                    Arguments: 'string'
                    """

                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:SELect

                        Arguments: 'string'
                        """
                        _cmd = "SELect"
                        args = ["'string'"]

                    SELect = SELect()
                    """
                    SENSe:CORRection:CKIT:SMA:SELect

                    Arguments: 'string'
                    """

                SMA = SMA()
                """
                SENSe:CORRection:CKIT:SMA

                Arguments:
                """

                class STANdard(SCPINode):
                    """
                    SENSe:CORRection:CKIT:STANdard

                    Arguments:
                    """
                    _cmd = "STANdard"
                    args = []

                    class CATalog(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:CKIT:STANdard:CATalog
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#STANdard_CATalog>`_

                        Arguments: 'string'
                        """
                        _cmd = "CATalog"
                        args = ["'string'"]

                    CATalog = CATalog()
                    """
                    `SENSe:CORRection:CKIT:STANdard:CATalog
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit.htm#STANdard_CATalog>`_

                    Arguments: 'string'
                    """

                    class LCATalog(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:CKIT:STANdard:LCATalog
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit_l(abel).htm#STANdard_CATalog>`_

                        Arguments: 'string'
                        """
                        _cmd = "LCATalog"
                        args = ["'string'"]

                    LCATalog = LCATalog()
                    """
                    `SENSe:CORRection:CKIT:STANdard:LCATalog
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_ckit_l(abel).htm#STANdard_CATalog>`_

                    Arguments: 'string'
                    """

                STANdard = STANdard()
                """
                SENSe:CORRection:CKIT:STANdard

                Arguments:
                """

                class USER(SCPINodeN):
                    """
                    SENSe:CORRection:CKIT:USER

                    Arguments:
                    """
                    _cmd = "USER"
                    args = []

                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFATten

                        Arguments: 'string'
                        """
                        _cmd = "FFATten"
                        args = ["'string'"]

                    FFATten = FFATten()
                    """
                    SENSe:CORRection:CKIT:USER:FFATten

                    Arguments: 'string'
                    """

                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFLine

                        Arguments: 'string'
                        """
                        _cmd = "FFLine"
                        args = ["'string'"]

                    FFLine = FFLine()
                    """
                    SENSe:CORRection:CKIT:USER:FFLine

                    Arguments: 'string'
                    """

                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "FFSNetwork"
                        args = ["'string'"]

                    FFSNetwork = FFSNetwork()
                    """
                    SENSe:CORRection:CKIT:USER:FFSNetwork

                    Arguments: 'string'
                    """

                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFTHrough

                        Arguments: 'string'
                        """
                        _cmd = "FFTHrough"
                        args = ["'string'"]

                    FFTHrough = FFTHrough()
                    """
                    SENSe:CORRection:CKIT:USER:FFTHrough

                    Arguments: 'string'
                    """

                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FMTCh

                        Arguments: 'string'
                        """
                        _cmd = "FMTCh"
                        args = ["'string'"]

                    FMTCh = FMTCh()
                    """
                    SENSe:CORRection:CKIT:USER:FMTCh

                    Arguments: 'string'
                    """

                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FOPen

                        Arguments: 'string'
                        """
                        _cmd = "FOPen"
                        args = ["'string'"]

                    FOPen = FOPen()
                    """
                    SENSe:CORRection:CKIT:USER:FOPen

                    Arguments: 'string'
                    """

                    class FOSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FOSHort

                        Arguments: 'string'
                        """
                        _cmd = "FOSHort"
                        args = ["'string'"]

                    FOSHort = FOSHort()
                    """
                    SENSe:CORRection:CKIT:USER:FOSHort

                    Arguments: 'string'
                    """

                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FREFlect

                        Arguments: 'string'
                        """
                        _cmd = "FREFlect"
                        args = ["'string'"]

                    FREFlect = FREFlect()
                    """
                    SENSe:CORRection:CKIT:USER:FREFlect

                    Arguments: 'string'
                    """

                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FSHort

                        Arguments: 'string'
                        """
                        _cmd = "FSHort"
                        args = ["'string'"]

                    FSHort = FSHort()
                    """
                    SENSe:CORRection:CKIT:USER:FSHort

                    Arguments: 'string'
                    """

                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FSMatch

                        Arguments: 'string'
                        """
                        _cmd = "FSMatch"
                        args = ["'string'"]

                    FSMatch = FSMatch()
                    """
                    SENSe:CORRection:CKIT:USER:FSMatch

                    Arguments: 'string'
                    """

                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFATten

                        Arguments: 'string'
                        """
                        _cmd = "MFATten"
                        args = ["'string'"]

                    MFATten = MFATten()
                    """
                    SENSe:CORRection:CKIT:USER:MFATten

                    Arguments: 'string'
                    """

                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFLine

                        Arguments: 'string'
                        """
                        _cmd = "MFLine"
                        args = ["'string'"]

                    MFLine = MFLine()
                    """
                    SENSe:CORRection:CKIT:USER:MFLine

                    Arguments: 'string'
                    """

                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "MFSNetwork"
                        args = ["'string'"]

                    MFSNetwork = MFSNetwork()
                    """
                    SENSe:CORRection:CKIT:USER:MFSNetwork

                    Arguments: 'string'
                    """

                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFTHrough

                        Arguments: 'string'
                        """
                        _cmd = "MFTHrough"
                        args = ["'string'"]

                    MFTHrough = MFTHrough()
                    """
                    SENSe:CORRection:CKIT:USER:MFTHrough

                    Arguments: 'string'
                    """

                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMATten

                        Arguments: 'string'
                        """
                        _cmd = "MMATten"
                        args = ["'string'"]

                    MMATten = MMATten()
                    """
                    SENSe:CORRection:CKIT:USER:MMATten

                    Arguments: 'string'
                    """

                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMLine

                        Arguments: 'string'
                        """
                        _cmd = "MMLine"
                        args = ["'string'"]

                    MMLine = MMLine()
                    """
                    SENSe:CORRection:CKIT:USER:MMLine

                    Arguments: 'string'
                    """

                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMSNetwork

                        Arguments: 'string'
                        """
                        _cmd = "MMSNetwork"
                        args = ["'string'"]

                    MMSNetwork = MMSNetwork()
                    """
                    SENSe:CORRection:CKIT:USER:MMSNetwork

                    Arguments: 'string'
                    """

                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMTCh

                        Arguments: 'string'
                        """
                        _cmd = "MMTCh"
                        args = ["'string'"]

                    MMTCh = MMTCh()
                    """
                    SENSe:CORRection:CKIT:USER:MMTCh

                    Arguments: 'string'
                    """

                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMTHrough

                        Arguments: 'string'
                        """
                        _cmd = "MMTHrough"
                        args = ["'string'"]

                    MMTHrough = MMTHrough()
                    """
                    SENSe:CORRection:CKIT:USER:MMTHrough

                    Arguments: 'string'
                    """

                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MOPen

                        Arguments: 'string'
                        """
                        _cmd = "MOPen"
                        args = ["'string'"]

                    MOPen = MOPen()
                    """
                    SENSe:CORRection:CKIT:USER:MOPen

                    Arguments: 'string'
                    """

                    class MOSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MOSHort

                        Arguments: 'string'
                        """
                        _cmd = "MOSHort"
                        args = ["'string'"]

                    MOSHort = MOSHort()
                    """
                    SENSe:CORRection:CKIT:USER:MOSHort

                    Arguments: 'string'
                    """

                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MREFlect

                        Arguments: 'string'
                        """
                        _cmd = "MREFlect"
                        args = ["'string'"]

                    MREFlect = MREFlect()
                    """
                    SENSe:CORRection:CKIT:USER:MREFlect

                    Arguments: 'string'
                    """

                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MSHort

                        Arguments: 'string'
                        """
                        _cmd = "MSHort"
                        args = ["'string'"]

                    MSHort = MSHort()
                    """
                    SENSe:CORRection:CKIT:USER:MSHort

                    Arguments: 'string'
                    """

                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MSMatch

                        Arguments: 'string'
                        """
                        _cmd = "MSMatch"
                        args = ["'string'"]

                    MSMatch = MSMatch()
                    """
                    SENSe:CORRection:CKIT:USER:MSMatch

                    Arguments: 'string'
                    """

                    class OSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:OSHort

                        Arguments: 'string'
                        """
                        _cmd = "OSHort"
                        args = ["'string'"]

                    OSHort = OSHort()
                    """
                    SENSe:CORRection:CKIT:USER:OSHort

                    Arguments: 'string'
                    """

                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:SELect

                        Arguments: 'string'
                        """
                        _cmd = "SELect"
                        args = ["'string'"]

                    SELect = SELect()
                    """
                    SENSe:CORRection:CKIT:USER:SELect

                    Arguments: 'string'
                    """

                USER = USER()
                """
                SENSe:CORRection:CKIT:USER

                Arguments:
                """

            CKIT = CKIT()
            """
            SENSe:CORRection:CKIT

            Arguments:
            """

            class COLLect(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:COLLect

                Arguments: ATT, IMATch12, ISOLation, LINE1, LINE2, LINE3, M1O2, M1S2, MATCh1, MATCh12, MATCh2, NET, O1M2, OPEN1, OPEN12, OPEN2, OSHort1, OSHORT11, OSHORT12, OSHORT13, OSHort2, OSHORT21, OSHORT22, OSHORT23, REFL1, REFL2, S1M2, SHORt1, SHORt12, SHORt2, SLIDe1, SLIDe12, SLIDe2, THRough, UTHRough
                """
                _cmd = "COLLect"
                args = ["ATT", "IMATch12", "ISOLation", "LINE1", "LINE2", "LINE3", "M1O2", "M1S2", "MATCh1", "MATCh12", "MATCh2", "NET", "O1M2", "OPEN1", "OPEN12", "OPEN2", "OSHort1", "OSHORT11", "OSHORT12", "OSHORT13", "OSHort2", "OSHORT21", "OSHORT22", "OSHORT23", "REFL1", "REFL2", "S1M2", "SHORt1", "SHORt12", "SHORt2", "SLIDe1", "SLIDe12", "SLIDe2", "THRough", "UTHRough"]

                class ACQuire(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:COLLect:ACQuire

                    Arguments: ATT, IMATch12, ISOLation, LINE1, LINE2, LINE3, M1O2, M1S2, MATCh1, MATCh12, MATCh2, NET, O1M2, OPEN1, OPEN12, OPEN2, OSHort1, OSHORT11, OSHORT12, OSHORT13, OSHort2, OSHORT21, OSHORT22, OSHORT23, REFL1, REFL2, S1M2, SHORt1, SHORt12, SHORt2, SLIDe1, SLIDe12, SLIDe2, THRough, UTHRough
                    """
                    _cmd = "ACQuire"
                    args = ["ATT", "IMATch12", "ISOLation", "LINE1", "LINE2", "LINE3", "M1O2", "M1S2", "MATCh1", "MATCh12", "MATCh2", "NET", "O1M2", "OPEN1", "OPEN12", "OPEN2", "OSHort1", "OSHORT11", "OSHORT12", "OSHORT13", "OSHort2", "OSHORT21", "OSHORT22", "OSHORT23", "REFL1", "REFL2", "S1M2", "SHORt1", "SHORt12", "SHORt2", "SLIDe1", "SLIDe12", "SLIDe2", "THRough", "UTHRough"]

                    class RSAVe(SCPINode, SCPIBool):
                        """
                        `SENSe:CORRection:COLLect:ACQuire:RSAVe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AQUire_SAVE>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "RSAVe"
                        args = ["1", "OFF", "ON"]

                        class DEFault(SCPINode, SCPIBool):
                            """
                            `SENSe:CORRection:COLLect:ACQuire:RSAVe:DEFault
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AQUire_SAVE_DEFault>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "DEFault"
                            args = ["1", "OFF", "ON"]

                        DEFault = DEFault()
                        """
                        `SENSe:CORRection:COLLect:ACQuire:RSAVe:DEFault
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AQUire_SAVE_DEFault>`_

                        Arguments: 1, OFF, ON
                        """

                    RSAVe = RSAVe()
                    """
                    `SENSe:CORRection:COLLect:ACQuire:RSAVe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AQUire_SAVE>`_

                    Arguments: 1, OFF, ON
                    """

                    class SELected(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:COLLect:ACQuire:SELected

                        Arguments: ATT, ISOLation, LINE, LINE1, LINE2, LINE3, LINEN, MATCh, NET, OPEN, OSHort, OSHORT1, OSHORT2, OSHORT3, REFL, SHORt, SLIDe, THRough, UTHRough
                        """
                        _cmd = "SELected"
                        args = ["ATT", "ISOLation", "LINE", "LINE1", "LINE2", "LINE3", "LINEN", "MATCh", "NET", "OPEN", "OSHort", "OSHORT1", "OSHORT2", "OSHORT3", "REFL", "SHORt", "SLIDe", "THRough", "UTHRough"]

                    SELected = SELected()
                    """
                    SENSe:CORRection:COLLect:ACQuire:SELected

                    Arguments: ATT, ISOLation, LINE, LINE1, LINE2, LINE3, LINEN, MATCh, NET, OPEN, OSHort, OSHORT1, OSHORT2, OSHORT3, REFL, SHORt, SLIDe, THRough, UTHRough
                    """

                ACQuire = ACQuire()
                """
                SENSe:CORRection:COLLect:ACQuire

                Arguments: ATT, IMATch12, ISOLation, LINE1, LINE2, LINE3, M1O2, M1S2, MATCh1, MATCh12, MATCh2, NET, O1M2, OPEN1, OPEN12, OPEN2, OSHort1, OSHORT11, OSHORT12, OSHORT13, OSHort2, OSHORT21, OSHORT22, OSHORT23, REFL1, REFL2, S1M2, SHORt1, SHORt12, SHORt2, SLIDe1, SLIDe12, SLIDe2, THRough, UTHRough
                """

                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:AUTO
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO>`_

                    Arguments: 'string'
                    """
                    _cmd = "AUTO"
                    args = ["'string'"]

                    class ASSignment(SCPINodeN):
                        """
                        SENSe:CORRection:COLLect:AUTO:ASSignment

                        Arguments:
                        """
                        _cmd = "ASSignment"
                        args = []

                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:ASSignment:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_ASSignment_ACQuire>`_

                            Arguments:
                            """
                            _cmd = "ACQuire"
                            args = []

                        ACQuire = ACQuire()
                        """
                        `SENSe:CORRection:COLLect:AUTO:ASSignment:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_ASSignment_ACQuire>`_

                        Arguments:
                        """

                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:ASSignment:DEFine
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_ASSignment_DEFine>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "DEFine"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        DEFine = DEFine()
                        """
                        `SENSe:CORRection:COLLect:AUTO:ASSignment:DEFine
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_ASSignment_DEFine>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class DELete(SCPINode):
                            """
                            SENSe:CORRection:COLLect:AUTO:ASSignment:DELete

                            Arguments:
                            """
                            _cmd = "DELete"
                            args = []

                            class ALL(SCPINode, SCPISet):
                                """
                                `SENSe:CORRection:COLLect:AUTO:ASSignment:DELete:ALL
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_ASSignment_DELete>`_

                                Arguments:
                                """
                                _cmd = "ALL"
                                args = []

                            ALL = ALL()
                            """
                            `SENSe:CORRection:COLLect:AUTO:ASSignment:DELete:ALL
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_ASSignment_DELete>`_

                            Arguments:
                            """

                        DELete = DELete()
                        """
                        SENSe:CORRection:COLLect:AUTO:ASSignment:DELete

                        Arguments:
                        """

                    ASSignment = ASSignment()
                    """
                    SENSe:CORRection:COLLect:AUTO:ASSignment

                    Arguments:
                    """

                    class CKIT(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:CKIT
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_CKIT>`_

                        Arguments: 'string'
                        """
                        _cmd = "CKIT"
                        args = ["'string'"]

                        class PORTs(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:CKIT:PORTs
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_CKIT_Ports>`_

                            Arguments: 'string'
                            """
                            _cmd = "PORTs"
                            args = ["'string'"]

                        PORTs = PORTs()
                        """
                        `SENSe:CORRection:COLLect:AUTO:CKIT:PORTs
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_CKIT_Ports>`_

                        Arguments: 'string'
                        """

                    CKIT = CKIT()
                    """
                    `SENSe:CORRection:COLLect:AUTO:CKIT
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_CKIT>`_

                    Arguments: 'string'
                    """

                    class CONFigure(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:CONFigure
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_CONFigure>`_

                        Arguments: FNPort, FOPort, FRTRans, FTRans, OPTPort, RTRans, SFTPort
                        """
                        _cmd = "CONFigure"
                        args = ["FNPort", "FOPort", "FRTRans", "FTRans", "OPTPort", "RTRans", "SFTPort"]

                    CONFigure = CONFigure()
                    """
                    `SENSe:CORRection:COLLect:AUTO:CONFigure
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_CONFigure>`_

                    Arguments: FNPort, FOPort, FRTRans, FTRans, OPTPort, RTRans, SFTPort
                    """

                    class PORTs(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:PORTs
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_PORTs>`_

                        Arguments: 'string'
                        """
                        _cmd = "PORTs"
                        args = ["'string'"]

                        class CONNection(SCPINode, SCPIQuery):
                            """
                            `SENSe:CORRection:COLLect:AUTO:PORTs:CONNection
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_PORTs_CONNection>`_

                            Arguments:
                            """
                            _cmd = "CONNection"
                            args = []

                        CONNection = CONNection()
                        """
                        `SENSe:CORRection:COLLect:AUTO:PORTs:CONNection
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_PORTs_CONNection>`_

                        Arguments:
                        """

                        class TYPE(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:PORTs:TYPE
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_PORTs_TYPE>`_

                            Arguments: FNPort, FOPort, FRTRans, FTRans, OPTPort, RTRans, SFTPort
                            """
                            _cmd = "TYPE"
                            args = ["FNPort", "FOPort", "FRTRans", "FTRans", "OPTPort", "RTRans", "SFTPort"]

                        TYPE = TYPE()
                        """
                        `SENSe:CORRection:COLLect:AUTO:PORTs:TYPE
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_PORTs_TYPE>`_

                        Arguments: FNPort, FOPort, FRTRans, FTRans, OPTPort, RTRans, SFTPort
                        """

                    PORTs = PORTs()
                    """
                    `SENSe:CORRection:COLLect:AUTO:PORTs
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_PORTs>`_

                    Arguments: 'string'
                    """

                    class RPGRoup(SCPINode, SCPIBool):
                        """
                        `SENSe:CORRection:COLLect:AUTO:RPGRoup
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_RPGRoup>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "RPGRoup"
                        args = ["1", "OFF", "ON"]

                    RPGRoup = RPGRoup()
                    """
                    `SENSe:CORRection:COLLect:AUTO:RPGRoup
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_RPGRoup>`_

                    Arguments: 1, OFF, ON
                    """

                    class SAVE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:SAVE
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_SAVE>`_

                        Arguments:
                        """
                        _cmd = "SAVE"
                        args = []

                    SAVE = SAVE()
                    """
                    `SENSe:CORRection:COLLect:AUTO:SAVE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_SAVE>`_

                    Arguments:
                    """

                    class TYPE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:TYPE
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_TYPE>`_

                        Arguments: FNPort, FOPort, FRTRans, FTRans, OPTPort, RTRans, SFTPort
                        """
                        _cmd = "TYPE"
                        args = ["FNPort", "FOPort", "FRTRans", "FTRans", "OPTPort", "RTRans", "SFTPort"]

                    TYPE = TYPE()
                    """
                    `SENSe:CORRection:COLLect:AUTO:TYPE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_TYPE>`_

                    Arguments: FNPort, FOPort, FRTRans, FTRans, OPTPort, RTRans, SFTPort
                    """

                    class VMIXer(SCPINode):
                        """
                        SENSe:CORRection:COLLect:AUTO:VMIXer

                        Arguments:
                        """
                        _cmd = "VMIXer"
                        args = []

                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:VMIXer:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_VMIXer>`_

                            Arguments: BASE, MIXer
                            """
                            _cmd = "ACQuire"
                            args = ["BASE", "MIXer"]

                        ACQuire = ACQuire()
                        """
                        `SENSe:CORRection:COLLect:AUTO:VMIXer:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO_VMIXer>`_

                        Arguments: BASE, MIXer
                        """

                    VMIXer = VMIXer()
                    """
                    SENSe:CORRection:COLLect:AUTO:VMIXer

                    Arguments:
                    """

                AUTO = AUTO()
                """
                `SENSe:CORRection:COLLect:AUTO
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#AUTO>`_

                Arguments: 'string'
                """

                class CONNection(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:CONNection
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#CONNection>`_

                    Arguments: N50Female, N50Male, N75Female, N75Male, PC185Female, PC185Male, PC1Female, PC1Male, PC24Female, PC24Male, PC292female, PC292male, PC35female, PC35male, PC7, SMAFemale, SMAMale, UFEMale1, UFEMale2, UMALe1, UMALe2
                    """
                    _cmd = "CONNection"
                    args = ["N50Female", "N50Male", "N75Female", "N75Male", "PC185Female", "PC185Male", "PC1Female", "PC1Male", "PC24Female", "PC24Male", "PC292female", "PC292male", "PC35female", "PC35male", "PC7", "SMAFemale", "SMAMale", "UFEMale1", "UFEMale2", "UMALe1", "UMALe2"]

                    class GENDers(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CONNection:GENDers
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#CONNection_GENDers>`_

                        Arguments: ALL, SINGle
                        """
                        _cmd = "GENDers"
                        args = ["ALL", "SINGle"]

                    GENDers = GENDers()
                    """
                    `SENSe:CORRection:COLLect:CONNection:GENDers
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#CONNection_GENDers>`_

                    Arguments: ALL, SINGle
                    """

                    class PORTs(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CONNection:PORTs
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#CONNection_PORTs>`_

                        Arguments: ALL, SINGle
                        """
                        _cmd = "PORTs"
                        args = ["ALL", "SINGle"]

                    PORTs = PORTs()
                    """
                    `SENSe:CORRection:COLLect:CONNection:PORTs
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#CONNection_PORTs>`_

                    Arguments: ALL, SINGle
                    """

                CONNection = CONNection()
                """
                `SENSe:CORRection:COLLect:CONNection
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#CONNection>`_

                Arguments: N50Female, N50Male, N75Female, N75Male, PC185Female, PC185Male, PC1Female, PC1Male, PC24Female, PC24Male, PC292female, PC292male, PC35female, PC35male, PC7, SMAFemale, SMAMale, UFEMale1, UFEMale2, UMALe1, UMALe2
                """

                class CSETup(SCPINode, SCPIBool):
                    """
                    `SENSe:CORRection:COLLect:CSETup
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#CSETup>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "CSETup"
                    args = ["1", "OFF", "ON"]

                CSETup = CSETup()
                """
                `SENSe:CORRection:COLLect:CSETup
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#CSETup>`_

                Arguments: 1, OFF, ON
                """

                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:DELete
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#DELete>`_

                    Arguments: ALL, 'string'
                    """
                    _cmd = "DELete"
                    args = ["ALL", "'string'"]

                DELete = DELete()
                """
                `SENSe:CORRection:COLLect:DELete
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#DELete>`_

                Arguments: ALL, 'string'
                """

                class DETector(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:DETector
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#DETector>`_

                    Arguments: AVERage, NORMal
                    """
                    _cmd = "DETector"
                    args = ["AVERage", "NORMal"]

                DETector = DETector()
                """
                `SENSe:CORRection:COLLect:DETector
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#DETector>`_

                Arguments: AVERage, NORMal
                """

                class FIXTure(SCPINode, SCPISet):
                    """
                    SENSe:CORRection:COLLect:FIXTure

                    Arguments: OPEN, SHORt
                    """
                    _cmd = "FIXTure"
                    args = ["OPEN", "SHORt"]

                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#FIXTure_AQUire>`_

                        Arguments: OPEN, SHORt
                        """
                        _cmd = "ACQuire"
                        args = ["OPEN", "SHORt"]

                    ACQuire = ACQuire()
                    """
                    `SENSe:CORRection:COLLect:FIXTure:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#FIXTure_AQUire>`_

                    Arguments: OPEN, SHORt
                    """

                    class LMParameter(SCPINode, SCPIBool):
                        """
                        SENSe:CORRection:COLLect:FIXTure:LMParameter

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "LMParameter"
                        args = ["1", "OFF", "ON"]

                        class LOSS(SCPINode, SCPIBool):
                            """
                            SENSe:CORRection:COLLect:FIXTure:LMParameter:LOSS

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "LOSS"
                            args = ["1", "OFF", "ON"]

                            class STATe(SCPINode, SCPIBool):
                                """
                                `SENSe:CORRection:COLLect:FIXTure:LMParameter:LOSS:STATe
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#FIXTure_LMParameter_LOSS>`_

                                Arguments: 1, OFF, ON
                                """
                                _cmd = "STATe"
                                args = ["1", "OFF", "ON"]

                            STATe = STATe()
                            """
                            `SENSe:CORRection:COLLect:FIXTure:LMParameter:LOSS:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#FIXTure_LMParameter_LOSS>`_

                            Arguments: 1, OFF, ON
                            """

                        LOSS = LOSS()
                        """
                        SENSe:CORRection:COLLect:FIXTure:LMParameter:LOSS

                        Arguments: 1, OFF, ON
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            `SENSe:CORRection:COLLect:FIXTure:LMParameter:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#FIXTure_LMParameter>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `SENSe:CORRection:COLLect:FIXTure:LMParameter:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#FIXTure_LMParameter>`_

                        Arguments: 1, OFF, ON
                        """

                    LMParameter = LMParameter()
                    """
                    SENSe:CORRection:COLLect:FIXTure:LMParameter

                    Arguments: 1, OFF, ON
                    """

                    class SAVE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:SAVE
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#FIXTure_SAVE>`_

                        Arguments:
                        """
                        _cmd = "SAVE"
                        args = []

                    SAVE = SAVE()
                    """
                    `SENSe:CORRection:COLLect:FIXTure:SAVE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#FIXTure_SAVE>`_

                    Arguments:
                    """

                    class STARt(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:STARt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#FIXTure_STARt>`_

                        Arguments:
                        """
                        _cmd = "STARt"
                        args = []

                    STARt = STARt()
                    """
                    `SENSe:CORRection:COLLect:FIXTure:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#FIXTure_STARt>`_

                    Arguments:
                    """

                FIXTure = FIXTure()
                """
                SENSe:CORRection:COLLect:FIXTure

                Arguments: OPEN, SHORt
                """

                class IMODulation(SCPINode, SCPIBool):
                    """
                    SENSe:CORRection:COLLect:IMODulation

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "IMODulation"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:CORRection:COLLect:IMODulation:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#IMODulation>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SENSe:CORRection:COLLect:IMODulation:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#IMODulation>`_

                    Arguments: 1, OFF, ON
                    """

                IMODulation = IMODulation()
                """
                SENSe:CORRection:COLLect:IMODulation

                Arguments: 1, OFF, ON
                """

                class METHod(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:METHod
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#METHod>`_

                    Arguments: ETOM, ETSM, FOPort1, FOPort12, FOPort2, FOPTport, FRTRans, FTRans, REFL1, REFL12, REFL2, ROPTport, RTRans, TNA, TOM, TOSM, TPORt, TRL, TRM, UOSM
                    """
                    _cmd = "METHod"
                    args = ["ETOM", "ETSM", "FOPort1", "FOPort12", "FOPort2", "FOPTport", "FRTRans", "FTRans", "REFL1", "REFL12", "REFL2", "ROPTport", "RTRans", "TNA", "TOM", "TOSM", "TPORt", "TRL", "TRM", "UOSM"]

                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:METHod:DEFine
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#METHod_DEFine>`_

                        Arguments: 'string'
                        """
                        _cmd = "DEFine"
                        args = ["'string'"]

                    DEFine = DEFine()
                    """
                    `SENSe:CORRection:COLLect:METHod:DEFine
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#METHod_DEFine>`_

                    Arguments: 'string'
                    """

                METHod = METHod()
                """
                `SENSe:CORRection:COLLect:METHod
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#METHod>`_

                Arguments: ETOM, ETSM, FOPort1, FOPort12, FOPort2, FOPTport, FRTRans, FTRans, REFL1, REFL12, REFL2, ROPTport, RTRans, TNA, TOM, TOSM, TPORt, TRL, TRM, UOSM
                """

                class NFIGure(SCPINode, SCPISet):
                    """
                    SENSe:CORRection:COLLect:NFIGure

                    Arguments: ATTenuator, RECeiver, SOURce
                    """
                    _cmd = "NFIGure"
                    args = ["ATTenuator", "RECeiver", "SOURce"]

                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:NFIGure:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#NFIGure_STARt>`_

                        Arguments: ATTenuator, RECeiver, SOURce
                        """
                        _cmd = "ACQuire"
                        args = ["ATTenuator", "RECeiver", "SOURce"]

                    ACQuire = ACQuire()
                    """
                    `SENSe:CORRection:COLLect:NFIGure:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#NFIGure_STARt>`_

                    Arguments: ATTenuator, RECeiver, SOURce
                    """

                    class END(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:NFIGure:END
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#NFIGure_END>`_

                        Arguments:
                        """
                        _cmd = "END"
                        args = []

                    END = END()
                    """
                    `SENSe:CORRection:COLLect:NFIGure:END
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#NFIGure_END>`_

                    Arguments:
                    """

                    class SAVE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:NFIGure:SAVE
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#NFIGure_AQUire>`_

                        Arguments:
                        """
                        _cmd = "SAVE"
                        args = []

                    SAVE = SAVE()
                    """
                    `SENSe:CORRection:COLLect:NFIGure:SAVE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#NFIGure_AQUire>`_

                    Arguments:
                    """

                    class STARt(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:NFIGure:STARt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#NFIGure_SAVE>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STARt = STARt()
                    """
                    `SENSe:CORRection:COLLect:NFIGure:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#NFIGure_SAVE>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                NFIGure = NFIGure()
                """
                SENSe:CORRection:COLLect:NFIGure

                Arguments: ATTenuator, RECeiver, SOURce
                """

                class RPSHift(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:RPSHift
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#RPSHift>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, 'string', UP
                    """
                    _cmd = "RPSHift"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "'string'", "UP"]

                RPSHift = RPSHift()
                """
                `SENSe:CORRection:COLLect:RPSHift
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#RPSHift>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, 'string', UP
                """

                class SAVE(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:SAVE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#SAVE>`_

                    Arguments:
                    """
                    _cmd = "SAVE"
                    args = []

                    class DEFault(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:SAVE:DEFault
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#SAVE_DEFault>`_

                        Arguments:
                        """
                        _cmd = "DEFault"
                        args = []

                    DEFault = DEFault()
                    """
                    `SENSe:CORRection:COLLect:SAVE:DEFault
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#SAVE_DEFault>`_

                    Arguments:
                    """

                    class DUMMy(SCPINode, SCPISet):
                        """
                        SENSe:CORRection:COLLect:SAVE:DUMMy

                        Arguments:
                        """
                        _cmd = "DUMMy"
                        args = []

                    DUMMy = DUMMy()
                    """
                    SENSe:CORRection:COLLect:SAVE:DUMMy

                    Arguments:
                    """

                    class SELected(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:SAVE:SELected
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#SAVE_SELected>`_

                        Arguments:
                        """
                        _cmd = "SELected"
                        args = []

                        class DEFault(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:SAVE:SELected:DEFault
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#SAVE_SELected_DEFault>`_

                            Arguments:
                            """
                            _cmd = "DEFault"
                            args = []

                        DEFault = DEFault()
                        """
                        `SENSe:CORRection:COLLect:SAVE:SELected:DEFault
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#SAVE_SELected_DEFault>`_

                        Arguments:
                        """

                        class DUMMy(SCPINode, SCPISet):
                            """
                            SENSe:CORRection:COLLect:SAVE:SELected:DUMMy

                            Arguments:
                            """
                            _cmd = "DUMMy"
                            args = []

                        DUMMy = DUMMy()
                        """
                        SENSe:CORRection:COLLect:SAVE:SELected:DUMMy

                        Arguments:
                        """

                    SELected = SELected()
                    """
                    `SENSe:CORRection:COLLect:SAVE:SELected
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#SAVE_SELected>`_

                    Arguments:
                    """

                SAVE = SAVE()
                """
                `SENSe:CORRection:COLLect:SAVE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#SAVE>`_

                Arguments:
                """

                class SCONnection(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:SCONnection
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#SCONnection>`_

                    Arguments: 'string'
                    """
                    _cmd = "SCONnection"
                    args = ["'string'"]

                SCONnection = SCONnection()
                """
                `SENSe:CORRection:COLLect:SCONnection
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_collect.htm#SCONnection>`_

                Arguments: 'string'
                """

            COLLect = COLLect()
            """
            SENSe:CORRection:COLLect

            Arguments: ATT, IMATch12, ISOLation, LINE1, LINE2, LINE3, M1O2, M1S2, MATCh1, MATCh12, MATCh2, NET, O1M2, OPEN1, OPEN12, OPEN2, OSHort1, OSHORT11, OSHORT12, OSHORT13, OSHort2, OSHORT21, OSHORT22, OSHORT23, REFL1, REFL2, S1M2, SHORt1, SHORt12, SHORt2, SLIDe1, SLIDe12, SLIDe2, THRough, UTHRough
            """

            class CONNection(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:CONNection
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#CONNection>`_

                Arguments: 'string'
                """
                _cmd = "CONNection"
                args = ["'string'"]

                class CATalog(SCPINode, SCPIQuery):
                    """
                    `SENSe:CORRection:CONNection:CATalog
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#CONNection_CATalog>`_

                    Arguments:
                    """
                    _cmd = "CATalog"
                    args = []

                CATalog = CATalog()
                """
                `SENSe:CORRection:CONNection:CATalog
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#CONNection_CATalog>`_

                Arguments:
                """

                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CONNection:DELete
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#CONNection_DELete>`_

                    Arguments: 'string'
                    """
                    _cmd = "DELete"
                    args = ["'string'"]

                DELete = DELete()
                """
                `SENSe:CORRection:CONNection:DELete
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#CONNection_DELete>`_

                Arguments: 'string'
                """

            CONNection = CONNection()
            """
            `SENSe:CORRection:CONNection
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#CONNection>`_

            Arguments: 'string'
            """

            class CSET(SCPINode):
                """
                SENSe:CORRection:CSET

                Arguments:
                """
                _cmd = "CSET"
                args = []

                class DESCription(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CSET:DESCription

                    Arguments: 'string'
                    """
                    _cmd = "DESCription"
                    args = ["'string'"]

                DESCription = DESCription()
                """
                SENSe:CORRection:CSET:DESCription

                Arguments: 'string'
                """

            CSET = CSET()
            """
            SENSe:CORRection:CSET

            Arguments:
            """

            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:DATA

                Arguments: 'string'
                """
                _cmd = "DATA"
                args = ["'string'"]

                class PARameter(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:DATA:PARameter
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#DATA_PARameter_>`_

                    Arguments: BANDwidth, PDLY, POINts, PORTs, RATTenuation, RPSHift, SPOWer, STARt, STOP, STYPe, THRoughs, TSTamp, TYPE
                    """
                    _cmd = "PARameter"
                    args = ["BANDwidth", "PDLY", "POINts", "PORTs", "RATTenuation", "RPSHift", "SPOWer", "STARt", "STOP", "STYPe", "THRoughs", "TSTamp", "TYPE"]

                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SENSe:CORRection:DATA:PARameter:COUNt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#DATA_PARameter_COUNt>`_

                        Arguments:
                        """
                        _cmd = "COUNt"
                        args = []

                    COUNt = COUNt()
                    """
                    `SENSe:CORRection:DATA:PARameter:COUNt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#DATA_PARameter_COUNt>`_

                    Arguments:
                    """

                PARameter = PARameter()
                """
                `SENSe:CORRection:DATA:PARameter
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#DATA_PARameter_>`_

                Arguments: BANDwidth, PDLY, POINts, PORTs, RATTenuation, RPSHift, SPOWer, STARt, STOP, STYPe, THRoughs, TSTamp, TYPE
                """

            DATA = DATA()
            """
            SENSe:CORRection:DATA

            Arguments: 'string'
            """

            class DATE(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:DATE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#DATE>`_

                Arguments:
                """
                _cmd = "DATE"
                args = []

            DATE = DATE()
            """
            `SENSe:CORRection:DATE
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#DATE>`_

            Arguments:
            """

            class EDELay(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:EDELay

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "EDELay"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:AUTO
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EDELay_AUTO>`_

                    Arguments: ONCE
                    """
                    _cmd = "AUTO"
                    args = ["ONCE"]

                AUTO = AUTO()
                """
                `SENSe:CORRection:EDELay:AUTO
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EDELay_AUTO>`_

                Arguments: ONCE
                """

                class DIELectric(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:DIELectric
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EDELay_DIELectric>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DIELectric"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                DIELectric = DIELectric()
                """
                `SENSe:CORRection:EDELay:DIELectric
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EDELay_DIELectric>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class DISTance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:DISTance
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EDELay_DISTance>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DISTance"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                DISTance = DISTance()
                """
                `SENSe:CORRection:EDELay:DISTance
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EDELay_DISTance>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class ELENgth(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:ELENgth
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EDELay_ELENgth>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "ELENgth"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                ELENgth = ELENgth()
                """
                `SENSe:CORRection:EDELay:ELENgth
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EDELay_ELENgth>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:TIME
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EDELay_TIME>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TIME"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                TIME = TIME()
                """
                `SENSe:CORRection:EDELay:TIME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EDELay_TIME>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            EDELay = EDELay()
            """
            SENSe:CORRection:EDELay

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class EWAVe(SCPINode, SCPIBool):
                """
                SENSe:CORRection:EWAVe

                Arguments: 1, OFF, ON
                """
                _cmd = "EWAVe"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:CORRection:EWAVe:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EWAVe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:CORRection:EWAVe:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#EWAVe>`_

                Arguments: 1, OFF, ON
                """

            EWAVe = EWAVe()
            """
            SENSe:CORRection:EWAVe

            Arguments: 1, OFF, ON
            """

            class FACTory(SCPINode, SCPIBool):
                """
                SENSe:CORRection:FACTory

                Arguments: 1, OFF, ON
                """
                _cmd = "FACTory"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:CORRection:FACTory:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#FACTory_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:CORRection:FACTory:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#FACTory_STATe>`_

                Arguments: 1, OFF, ON
                """

            FACTory = FACTory()
            """
            SENSe:CORRection:FACTory

            Arguments: 1, OFF, ON
            """

            class LOSS(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:LOSS
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#LOSS>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "LOSS"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:AUTO
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#LOSS_AUTO>`_

                    Arguments: ONCE
                    """
                    _cmd = "AUTO"
                    args = ["ONCE"]

                AUTO = AUTO()
                """
                `SENSe:CORRection:LOSS:AUTO
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#LOSS_AUTO>`_

                Arguments: ONCE
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#LOSS_FREQuency>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "FREQuency"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                FREQuency = FREQuency()
                """
                `SENSe:CORRection:LOSS:FREQuency
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#LOSS_FREQuency>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#LOSS_OFFSet>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "OFFSet"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                OFFSet = OFFSet()
                """
                `SENSe:CORRection:LOSS:OFFSet
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#LOSS_OFFSet>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            LOSS = LOSS()
            """
            `SENSe:CORRection:LOSS
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#LOSS>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class NFIGure(SCPINode, SCPIBool):
                """
                SENSe:CORRection:NFIGure

                Arguments: 1, OFF, ON
                """
                _cmd = "NFIGure"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:CORRection:NFIGure:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#NFIGure_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:CORRection:NFIGure:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#NFIGure_STATe>`_

                Arguments: 1, OFF, ON
                """

            NFIGure = NFIGure()
            """
            SENSe:CORRection:NFIGure

            Arguments: 1, OFF, ON
            """

            class NSTate(SCPINode, SCPIQuery):
                """
                SENSe:CORRection:NSTate

                Arguments:
                """
                _cmd = "NSTate"
                args = []

            NSTate = NSTate()
            """
            SENSe:CORRection:NSTate

            Arguments:
            """

            class OFFSet(SCPINodeN, SCPIBool):
                """
                SENSe:CORRection:OFFSet

                Arguments: 1, OFF, ON
                """
                _cmd = "OFFSet"
                args = ["1", "OFF", "ON"]

                class DFComp(SCPINode, SCPIBool):
                    """
                    SENSe:CORRection:OFFSet:DFComp

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "DFComp"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:CORRection:OFFSet:DFComp:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#OFFset_DFComp_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SENSe:CORRection:OFFSet:DFComp:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#OFFset_DFComp_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                DFComp = DFComp()
                """
                SENSe:CORRection:OFFSet:DFComp

                Arguments: 1, OFF, ON
                """

                class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:OFFSet:MAGNitude
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#OFFSet_MAGNitude>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "MAGNitude"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                MAGNitude = MAGNitude()
                """
                `SENSe:CORRection:OFFSet:MAGNitude
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#OFFSet_MAGNitude>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:CORRection:OFFSet:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#OFFset_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:CORRection:OFFSet:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_data.htm#OFFset_STATe>`_

                Arguments: 1, OFF, ON
                """

            OFFSet = OFFSet()
            """
            SENSe:CORRection:OFFSet

            Arguments: 1, OFF, ON
            """

            class POWer(SCPINodeN, SCPIBool):
                """
                SENSe:CORRection:POWer

                Arguments: 1, OFF, ON
                """
                _cmd = "POWer"
                args = ["1", "OFF", "ON"]

                class ACQuire(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:POWer:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#POWer_ACQuire>`_

                    Arguments: AWAVe, B1, B2, B3, B4, BWAVe
                    """
                    _cmd = "ACQuire"
                    args = ["AWAVe", "B1", "B2", "B3", "B4", "BWAVe"]

                ACQuire = ACQuire()
                """
                `SENSe:CORRection:POWer:ACQuire
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#POWer_ACQuire>`_

                Arguments: AWAVe, B1, B2, B3, B4, BWAVe
                """

                class AWAVe(SCPINode, SCPIBool):
                    """
                    SENSe:CORRection:POWer:AWAVe

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "AWAVe"
                    args = ["1", "OFF", "ON"]

                    class IPMMatch(SCPINode, SCPIBool):
                        """
                        SENSe:CORRection:POWer:AWAVe:IPMMatch

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "IPMMatch"
                        args = ["1", "OFF", "ON"]

                        class STATe(SCPINode, SCPIBool):
                            """
                            `SENSe:CORRection:POWer:AWAVe:IPMMatch:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#POWer_AWAVe_IPMMatch_STATe>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `SENSe:CORRection:POWer:AWAVe:IPMMatch:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#POWer_AWAVe_IPMMatch_STATe>`_

                        Arguments: 1, OFF, ON
                        """

                    IPMMatch = IPMMatch()
                    """
                    SENSe:CORRection:POWer:AWAVe:IPMMatch

                    Arguments: 1, OFF, ON
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:CORRection:POWer:AWAVe:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#POWer_AWAVe_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SENSe:CORRection:POWer:AWAVe:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#POWer_AWAVe_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                AWAVe = AWAVe()
                """
                SENSe:CORRection:POWer:AWAVe

                Arguments: 1, OFF, ON
                """

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:POWer:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#POWer_DATA>`_

                    Arguments: 'string'
                    """
                    _cmd = "DATA"
                    args = ["'string'"]

                DATA = DATA()
                """
                `SENSe:CORRection:POWer:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#POWer_DATA>`_

                Arguments: 'string'
                """

                class HARMonic(SCPINode):
                    """
                    SENSe:CORRection:POWer:HARMonic

                    Arguments:
                    """
                    _cmd = "HARMonic"
                    args = []

                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:POWer:HARMonic:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#HARMonic_ACQuire>`_

                        Arguments:
                        """
                        _cmd = "ACQuire"
                        args = []

                    ACQuire = ACQuire()
                    """
                    `SENSe:CORRection:POWer:HARMonic:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#HARMonic_ACQuire>`_

                    Arguments:
                    """

                HARMonic = HARMonic()
                """
                SENSe:CORRection:POWer:HARMonic

                Arguments:
                """

                class IMODulation(SCPINode):
                    """
                    SENSe:CORRection:POWer:IMODulation

                    Arguments:
                    """
                    _cmd = "IMODulation"
                    args = []

                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:POWer:IMODulation:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#IMODulation_ACQuire>`_

                        Arguments:
                        """
                        _cmd = "ACQuire"
                        args = []

                    ACQuire = ACQuire()
                    """
                    `SENSe:CORRection:POWer:IMODulation:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#IMODulation_ACQuire>`_

                    Arguments:
                    """

                    class RPORt(SCPINode):
                        """
                        SENSe:CORRection:POWer:IMODulation:RPORt

                        Arguments:
                        """
                        _cmd = "RPORt"
                        args = []

                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:POWer:IMODulation:RPORt:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#IMODulation_RPORt_ACQuire>`_

                            Arguments:
                            """
                            _cmd = "ACQuire"
                            args = []

                        ACQuire = ACQuire()
                        """
                        `SENSe:CORRection:POWer:IMODulation:RPORt:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#IMODulation_RPORt_ACQuire>`_

                        Arguments:
                        """

                    RPORt = RPORt()
                    """
                    SENSe:CORRection:POWer:IMODulation:RPORt

                    Arguments:
                    """

                IMODulation = IMODulation()
                """
                SENSe:CORRection:POWer:IMODulation

                Arguments:
                """

                class MIXer(SCPINode):
                    """
                    SENSe:CORRection:POWer:MIXer

                    Arguments:
                    """
                    _cmd = "MIXer"
                    args = []

                    class IF(SCPINode):
                        """
                        SENSe:CORRection:POWer:MIXer:IF

                        Arguments:
                        """
                        _cmd = "IF"
                        args = []

                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:POWer:MIXer:IF:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#MIXer_IF_ACQuire>`_

                            Arguments:
                            """
                            _cmd = "ACQuire"
                            args = []

                        ACQuire = ACQuire()
                        """
                        `SENSe:CORRection:POWer:MIXer:IF:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#MIXer_IF_ACQuire>`_

                        Arguments:
                        """

                        class NFIGure(SCPINode):
                            """
                            SENSe:CORRection:POWer:MIXer:IF:NFIGure

                            Arguments:
                            """
                            _cmd = "NFIGure"
                            args = []

                            class ACQuire(SCPINode, SCPISet):
                                """
                                `SENSe:CORRection:POWer:MIXer:IF:NFIGure:ACQuire
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#MIXer_IF_NFIGure_ACQuire>`_

                                Arguments:
                                """
                                _cmd = "ACQuire"
                                args = []

                            ACQuire = ACQuire()
                            """
                            `SENSe:CORRection:POWer:MIXer:IF:NFIGure:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#MIXer_IF_NFIGure_ACQuire>`_

                            Arguments:
                            """

                        NFIGure = NFIGure()
                        """
                        SENSe:CORRection:POWer:MIXer:IF:NFIGure

                        Arguments:
                        """

                    IF = IF()
                    """
                    SENSe:CORRection:POWer:MIXer:IF

                    Arguments:
                    """

                MIXer = MIXer()
                """
                SENSe:CORRection:POWer:MIXer

                Arguments:
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:CORRection:POWer:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#POWer_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:CORRection:POWer:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#POWer_STATe>`_

                Arguments: 1, OFF, ON
                """

            POWer = POWer()
            """
            SENSe:CORRection:POWer

            Arguments: 1, OFF, ON
            """

            class PSTate(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:PSTate
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#PSTate>`_

                Arguments:
                """
                _cmd = "PSTate"
                args = []

            PSTate = PSTate()
            """
            `SENSe:CORRection:PSTate
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#PSTate>`_

            Arguments:
            """

            class SSTate(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:SSTate
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#SSTate>`_

                Arguments:
                """
                _cmd = "SSTate"
                args = []

            SSTate = SSTate()
            """
            `SENSe:CORRection:SSTate
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#SSTate>`_

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SENSe:CORRection:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `SENSe:CORRection:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#STATe>`_

            Arguments: 1, OFF, ON
            """

            class STIMulus(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:STIMulus
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#STIMulus>`_

                Arguments:
                """
                _cmd = "STIMulus"
                args = []

            STIMulus = STIMulus()
            """
            `SENSe:CORRection:STIMulus
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_correction_power.htm#STIMulus>`_

            Arguments:
            """

        CORRection = CORRection()
        """
        SENSe:CORRection

        Arguments: 1, OFF, ON
        """

        class COUPle(SCPINode, SCPIQuery, SCPISet):
            """
            `SENSe:COUPle
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_cmode.htm#COUPle>`_

            Arguments: ALL, NONE
            """
            _cmd = "COUPle"
            args = ["ALL", "NONE"]

        COUPle = COUPle()
        """
        `SENSe:COUPle
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_cmode.htm#COUPle>`_

        Arguments: ALL, NONE
        """

        class EUNit(SCPINode):
            """
            SENSe:EUNit

            Arguments:
            """
            _cmd = "EUNit"
            args = []

            class COMBiner(SCPINodeN, SCPIBool):
                """
                SENSe:EUNit:COMBiner

                Arguments: 1, OFF, ON
                """
                _cmd = "COMBiner"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:EUNit:COMBiner:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#COMBiner_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:EUNit:COMBiner:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#COMBiner_STATe>`_

                Arguments: 1, OFF, ON
                """

            COMBiner = COMBiner()
            """
            SENSe:EUNit:COMBiner

            Arguments: 1, OFF, ON
            """

            class HFILter(SCPINodeN, SCPIBool):
                """
                SENSe:EUNit:HFILter

                Arguments: 1, OFF, ON
                """
                _cmd = "HFILter"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:EUNit:HFILter:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#HFILter_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:EUNit:HFILter:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#HFILter_STATe>`_

                Arguments: 1, OFF, ON
                """

            HFILter = HFILter()
            """
            SENSe:EUNit:HFILter

            Arguments: 1, OFF, ON
            """

            class LNAMplifier(SCPINode, SCPIBool):
                """
                SENSe:EUNit:LNAMplifier

                Arguments: 1, OFF, ON
                """
                _cmd = "LNAMplifier"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:EUNit:LNAMplifier:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#LNAMplifier_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:EUNit:LNAMplifier:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#LNAMplifier_STATe>`_

                Arguments: 1, OFF, ON
                """

            LNAMplifier = LNAMplifier()
            """
            SENSe:EUNit:LNAMplifier

            Arguments: 1, OFF, ON
            """

            class PGENerator(SCPINode):
                """
                SENSe:EUNit:PGENerator

                Arguments:
                """
                _cmd = "PGENerator"
                args = []

                class ASSignment(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:EUNit:PGENerator:ASSignment
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#PGENerator_ASSignment>`_

                    Arguments: G1M2, G1M3, G1Mall, G2Mall
                    """
                    _cmd = "ASSignment"
                    args = ["G1M2", "G1M3", "G1Mall", "G2Mall"]

                ASSignment = ASSignment()
                """
                `SENSe:EUNit:PGENerator:ASSignment
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#PGENerator_ASSignment>`_

                Arguments: G1M2, G1M3, G1Mall, G2Mall
                """

                class INPut(SCPINode):
                    """
                    SENSe:EUNit:PGENerator:INPut

                    Arguments:
                    """
                    _cmd = "INPut"
                    args = []

                    class EXTernal(SCPINode, SCPIBool):
                        """
                        `SENSe:EUNit:PGENerator:INPut:EXTernal
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#PGENerator_INPut_EXTernal>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EXTernal"
                        args = ["1", "OFF", "ON"]

                    EXTernal = EXTernal()
                    """
                    `SENSe:EUNit:PGENerator:INPut:EXTernal
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#PGENerator_INPut_EXTernal>`_

                    Arguments: 1, OFF, ON
                    """

                INPut = INPut()
                """
                SENSe:EUNit:PGENerator:INPut

                Arguments:
                """

                class OUTPut(SCPINode):
                    """
                    SENSe:EUNit:PGENerator:OUTPut

                    Arguments:
                    """
                    _cmd = "OUTPut"
                    args = []

                    class EXTernal(SCPINode, SCPIBool):
                        """
                        `SENSe:EUNit:PGENerator:OUTPut:EXTernal
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#PGENerator_OUTPut_EXTernal>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EXTernal"
                        args = ["1", "OFF", "ON"]

                    EXTernal = EXTernal()
                    """
                    `SENSe:EUNit:PGENerator:OUTPut:EXTernal
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#PGENerator_OUTPut_EXTernal>`_

                    Arguments: 1, OFF, ON
                    """

                OUTPut = OUTPut()
                """
                SENSe:EUNit:PGENerator:OUTPut

                Arguments:
                """

            PGENerator = PGENerator()
            """
            SENSe:EUNit:PGENerator

            Arguments:
            """

            class PMODulator(SCPINodeN, SCPIBool):
                """
                SENSe:EUNit:PMODulator

                Arguments: 1, OFF, ON
                """
                _cmd = "PMODulator"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:EUNit:PMODulator:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#PMODulator_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:EUNit:PMODulator:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_eunit.htm#PMODulator_STATe>`_

                Arguments: 1, OFF, ON
                """

            PMODulator = PMODulator()
            """
            SENSe:EUNit:PMODulator

            Arguments: 1, OFF, ON
            """

        EUNit = EUNit()
        """
        SENSe:EUNit

        Arguments:
        """

        class FREQuency(SCPINodeN, SCPIQuery, SCPISet):
            """
            SENSe:FREQuency

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "FREQuency"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            class CENTer(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CENTer
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CENTer>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CENTer"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            CENTer = CENTer()
            """
            `SENSe:FREQuency:CENTer
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CENTer>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class CONVersion(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CONVersion
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion>`_

                Arguments: ARBitrary, FUNDamental, HARMonic, MIXer, SHARmonic, THARmonic, VMIXer
                """
                _cmd = "CONVersion"
                args = ["ARBitrary", "FUNDamental", "HARMonic", "MIXer", "SHARmonic", "THARmonic", "VMIXer"]

                class ARBitrary(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:CONVersion:ARBitrary
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_ARBitrary>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "ARBitrary"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    class PMETer(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:ARBitrary:PMETer
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_ARBitrary_PMETer>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PMETer"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    PMETer = PMETer()
                    """
                    `SENSe:FREQuency:CONVersion:ARBitrary:PMETer
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_ARBitrary_PMETer>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                ARBitrary = ARBitrary()
                """
                `SENSe:FREQuency:CONVersion:ARBitrary
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_ARBitrary>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class AWReceiver(SCPINode, SCPIBool):
                    """
                    SENSe:FREQuency:CONVersion:AWReceiver

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "AWReceiver"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:CONVersion:AWReceiver:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_AWReceiver__STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SENSe:FREQuency:CONVersion:AWReceiver:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_AWReceiver__STATe>`_

                    Arguments: 1, OFF, ON
                    """

                AWReceiver = AWReceiver()
                """
                SENSe:FREQuency:CONVersion:AWReceiver

                Arguments: 1, OFF, ON
                """

                class DEVice(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:DEVice

                    Arguments:
                    """
                    _cmd = "DEVice"
                    args = []

                    class MODE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:DEVice:MODE
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_MODE>`_

                        Arguments: RELE, RILE, RILI, RILI4, RILI56
                        """
                        _cmd = "MODE"
                        args = ["RELE", "RILE", "RILI", "RILI4", "RILI56"]

                    MODE = MODE()
                    """
                    `SENSe:FREQuency:CONVersion:DEVice:MODE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_MODE>`_

                    Arguments: RELE, RILE, RILI, RILI4, RILI56
                    """

                    class NAME(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:DEVice:NAME
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_NAME>`_

                        Arguments: 'string'
                        """
                        _cmd = "NAME"
                        args = ["'string'"]

                    NAME = NAME()
                    """
                    `SENSe:FREQuency:CONVersion:DEVice:NAME
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_NAME>`_

                    Arguments: 'string'
                    """

                    class PCOefficient(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:DEVice:PCOefficient
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_PCOefficient>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PCOefficient"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        class DEFault(SCPINode, SCPIBool):
                            """
                            `SENSe:FREQuency:CONVersion:DEVice:PCOefficient:DEFault
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_PCOefficient_DEFault>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "DEFault"
                            args = ["1", "OFF", "ON"]

                        DEFault = DEFault()
                        """
                        `SENSe:FREQuency:CONVersion:DEVice:PCOefficient:DEFault
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_PCOefficient_DEFault>`_

                        Arguments: 1, OFF, ON
                        """

                    PCOefficient = PCOefficient()
                    """
                    `SENSe:FREQuency:CONVersion:DEVice:PCOefficient
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_PCOefficient>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                DEVice = DEVice()
                """
                SENSe:FREQuency:CONVersion:DEVice

                Arguments:
                """

                class GAIN(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:GAIN

                    Arguments:
                    """
                    _cmd = "GAIN"
                    args = []

                    class LMCorrection(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:CONVersion:GAIN:LMCorrection
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_GAIN_LMCorrection>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "LMCorrection"
                        args = ["1", "OFF", "ON"]

                    LMCorrection = LMCorrection()
                    """
                    `SENSe:FREQuency:CONVersion:GAIN:LMCorrection
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_GAIN_LMCorrection>`_

                    Arguments: 1, OFF, ON
                    """

                GAIN = GAIN()
                """
                SENSe:FREQuency:CONVersion:GAIN

                Arguments:
                """

                class HARMonic(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:HARMonic

                    Arguments:
                    """
                    _cmd = "HARMonic"
                    args = []

                    class ORDer(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:HARMonic:ORDer
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_ORDer>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "ORDer"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    ORDer = ORDer()
                    """
                    `SENSe:FREQuency:CONVersion:HARMonic:ORDer
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_ORDer>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class RELative(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:CONVersion:HARMonic:RELative
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_RELative>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "RELative"
                        args = ["1", "OFF", "ON"]

                    RELative = RELative()
                    """
                    `SENSe:FREQuency:CONVersion:HARMonic:RELative
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_RELative>`_

                    Arguments: 1, OFF, ON
                    """

                    class RPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:HARMonic:RPORt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_RPORt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RPORt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    RPORt = RPORt()
                    """
                    `SENSe:FREQuency:CONVersion:HARMonic:RPORt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_RPORt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class SPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:HARMonic:SPORt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_SPORt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "SPORt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    SPORt = SPORt()
                    """
                    `SENSe:FREQuency:CONVersion:HARMonic:SPORt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_SPORt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                HARMonic = HARMonic()
                """
                SENSe:FREQuency:CONVersion:HARMonic

                Arguments:
                """

                class MIXer(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:MIXer

                    Arguments:
                    """
                    _cmd = "MIXer"
                    args = []

                    class AEXTernal(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:AEXTernal
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#AEXTernal>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, NONE, UP
                        """
                        _cmd = "AEXTernal"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "NONE", "UP"]

                    AEXTernal = AEXTernal()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:AEXTernal
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#AEXTernal>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, NONE, UP
                    """

                    class AINTernal(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:AINTernal
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#AINTernal>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, NONE, UP
                        """
                        _cmd = "AINTernal"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "NONE", "UP"]

                    AINTernal = AINTernal()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:AINTernal
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#AINTernal>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, NONE, UP
                    """

                    class APORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:APORt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#APORt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "APORt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    APORt = APORt()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:APORt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#APORt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class FFIXed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:FFIXed
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#FFIXed>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "FFIXed"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    FFIXed = FFIXed()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:FFIXed
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#FFIXed>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class FIXed(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:FIXed
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#FIXed>`_

                        Arguments: IF, LO, LO1, LO2, RF
                        """
                        _cmd = "FIXed"
                        args = ["IF", "LO", "LO1", "LO2", "RF"]

                    FIXed = FIXed()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:FIXed
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#FIXed>`_

                    Arguments: IF, LO, LO1, LO2, RF
                    """

                    class FUNDamental(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:FUNDamental
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#FUNDamental>`_

                        Arguments: IF, LO, LO1, LO2, RF
                        """
                        _cmd = "FUNDamental"
                        args = ["IF", "LO", "LO1", "LO2", "RF"]

                    FUNDamental = FUNDamental()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:FUNDamental
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#FUNDamental>`_

                    Arguments: IF, LO, LO1, LO2, RF
                    """

                    class HACCuracy(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:HACCuracy
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#HACCuracy>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "HACCuracy"
                        args = ["1", "OFF", "ON"]

                    HACCuracy = HACCuracy()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:HACCuracy
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#HACCuracy>`_

                    Arguments: 1, OFF, ON
                    """

                    class IFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:IFFixed
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#IFFixed>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "IFFixed"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    IFFixed = IFFixed()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:IFFixed
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#IFFixed>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class IFPort(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:IFPort
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#IFSource>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "IFPort"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    IFPort = IFPort()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:IFPort
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#IFSource>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class LOEXternal(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOEXternal
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOEXternal>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, NONE, SOURCE1, SOURCE2, UP
                        """
                        _cmd = "LOEXternal"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "NONE", "SOURCE1", "SOURCE2", "UP"]

                    LOEXternal = LOEXternal()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:LOEXternal
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOEXternal>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, NONE, SOURCE1, SOURCE2, UP
                    """

                    class LOFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOFixed
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOFixed>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "LOFixed"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    LOFixed = LOFixed()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:LOFixed
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOFixed>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class LOINternal(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOINternal
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOINternal>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, NONE, UP
                        """
                        _cmd = "LOINternal"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "NONE", "UP"]

                    LOINternal = LOINternal()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:LOINternal
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOINternal>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, NONE, UP
                    """

                    class LOMultiplier(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOMultiplier
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOMultiplier>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "LOMultiplier"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    LOMultiplier = LOMultiplier()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:LOMultiplier
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOMultiplier>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class LOPort(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOPort
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOPort>`_

                        Arguments: EMBedded, GENerator, NONE, PORT
                        """
                        _cmd = "LOPort"
                        args = ["EMBedded", "GENerator", "NONE", "PORT"]

                    LOPort = LOPort()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:LOPort
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOPort>`_

                    Arguments: EMBedded, GENerator, NONE, PORT
                    """

                    class MFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:MFFixed
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#MFFixed>`_

                        Arguments: IF, LO, LO1, LO2, RF
                        """
                        _cmd = "MFFixed"
                        args = ["IF", "LO", "LO1", "LO2", "RF"]

                    MFFixed = MFFixed()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:MFFixed
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#MFFixed>`_

                    Arguments: IF, LO, LO1, LO2, RF
                    """

                    class PRFimage(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:PRFimage
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#PRFimage>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "PRFimage"
                        args = ["1", "OFF", "ON"]

                    PRFimage = PRFimage()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:PRFimage
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#PRFimage>`_

                    Arguments: 1, OFF, ON
                    """

                    class RFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:RFFixed
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#RFFixed>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RFFixed"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    RFFixed = RFFixed()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:RFFixed
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#RFFixed>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class RFMultiplier(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:RFMultiplier
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#RFMultiplier>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RFMultiplier"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    RFMultiplier = RFMultiplier()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:RFMultiplier
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#RFMultiplier>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class RFPort(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:RFPort
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#RFSource>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RFPort"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    RFPort = RFPort()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:RFPort
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#RFSource>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STAGes(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:STAGes
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#STAGes>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STAGes"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STAGes = STAGes()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:STAGes
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#STAGes>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class TFRequency(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:TFRequency
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#TFRequency>`_

                        Arguments: BAND1, BAND2, DCLower, DCUPper, UCONversion
                        """
                        _cmd = "TFRequency"
                        args = ["BAND1", "BAND2", "DCLower", "DCUPper", "UCONversion"]

                    TFRequency = TFRequency()
                    """
                    `SENSe:FREQuency:CONVersion:MIXer:TFRequency
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_conversion_mixer.htm#TFRequency>`_

                    Arguments: BAND1, BAND2, DCLower, DCUPper, UCONversion
                    """

                MIXer = MIXer()
                """
                SENSe:FREQuency:CONVersion:MIXer

                Arguments:
                """

            CONVersion = CONVersion()
            """
            `SENSe:FREQuency:CONVersion
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency.htm#CONVersion>`_

            Arguments: ARBitrary, FUNDamental, HARMonic, MIXer, SHARmonic, THARmonic, VMIXer
            """

            class CW(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CW
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#CW>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CW"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            CW = CW()
            """
            `SENSe:FREQuency:CW
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#CW>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class FIXed(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:FIXed
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#CW>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "FIXed"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            FIXed = FIXed()
            """
            `SENSe:FREQuency:FIXed
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#CW>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class IMODulation(SCPINode):
                """
                SENSe:FREQuency:IMODulation

                Arguments:
                """
                _cmd = "IMODulation"
                args = []

                class COMBiner(SCPINode, SCPIBool):
                    """
                    SENSe:FREQuency:IMODulation:COMBiner

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "COMBiner"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:IMODulation:COMBiner:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#COMBiner_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SENSe:FREQuency:IMODulation:COMBiner:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#COMBiner_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                COMBiner = COMBiner()
                """
                SENSe:FREQuency:IMODulation:COMBiner

                Arguments: 1, OFF, ON
                """

                class CONVersion(SCPINode, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:CONVersion
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#CONVersion>`_

                    Arguments: OFF
                    """
                    _cmd = "CONVersion"
                    args = ["OFF"]

                CONVersion = CONVersion()
                """
                `SENSe:FREQuency:IMODulation:CONVersion
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#CONVersion>`_

                Arguments: OFF
                """

                class LTONe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:LTONe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#LTONe>`_

                    Arguments: GENerator, NONE, PORT
                    """
                    _cmd = "LTONe"
                    args = ["GENerator", "NONE", "PORT"]

                LTONe = LTONe()
                """
                `SENSe:FREQuency:IMODulation:LTONe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#LTONe>`_

                Arguments: GENerator, NONE, PORT
                """

                class ORDer(SCPINodeN, SCPIBool):
                    """
                    SENSe:FREQuency:IMODulation:ORDer

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "ORDer"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:IMODulation:ORDer:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#ORDer>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SENSe:FREQuency:IMODulation:ORDer:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#ORDer>`_

                    Arguments: 1, OFF, ON
                    """

                ORDer = ORDer()
                """
                SENSe:FREQuency:IMODulation:ORDer

                Arguments: 1, OFF, ON
                """

                class PEWCorr(SCPINode, SCPIBool):
                    """
                    SENSe:FREQuency:IMODulation:PEWCorr

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "PEWCorr"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:IMODulation:PEWCorr:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#PEWCorr>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SENSe:FREQuency:IMODulation:PEWCorr:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#PEWCorr>`_

                    Arguments: 1, OFF, ON
                    """

                PEWCorr = PEWCorr()
                """
                SENSe:FREQuency:IMODulation:PEWCorr

                Arguments: 1, OFF, ON
                """

                class RECeiver(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:RECeiver
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#RECeiver>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RECeiver"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                RECeiver = RECeiver()
                """
                `SENSe:FREQuency:IMODulation:RECeiver
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#RECeiver>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class SPECtrum(SCPINode, SCPIBool):
                    """
                    SENSe:FREQuency:IMODulation:SPECtrum

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "SPECtrum"
                    args = ["1", "OFF", "ON"]

                    class MORDer(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:IMODulation:SPECtrum:MORDer
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#SPECtrum_MORDer>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "MORDer"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    MORDer = MORDer()
                    """
                    `SENSe:FREQuency:IMODulation:SPECtrum:MORDer
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#SPECtrum_MORDer>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:IMODulation:SPECtrum:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#SPECtrum_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SENSe:FREQuency:IMODulation:SPECtrum:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#SPECtrum_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                SPECtrum = SPECtrum()
                """
                SENSe:FREQuency:IMODulation:SPECtrum

                Arguments: 1, OFF, ON
                """

                class TDIStance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:TDIStance
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#TDISTance>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TDIStance"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                TDIStance = TDIStance()
                """
                `SENSe:FREQuency:IMODulation:TDIStance
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#TDISTance>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class TTOutput(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:TTOutput
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#TTOutput>`_

                    Arguments: EDEVice, PORT
                    """
                    _cmd = "TTOutput"
                    args = ["EDEVice", "PORT"]

                TTOutput = TTOutput()
                """
                `SENSe:FREQuency:IMODulation:TTOutput
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#TTOutput>`_

                Arguments: EDEVice, PORT
                """

                class UTONe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:UTONe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#UTONe>`_

                    Arguments: GENerator, NONE, PORT
                    """
                    _cmd = "UTONe"
                    args = ["GENerator", "NONE", "PORT"]

                UTONe = UTONe()
                """
                `SENSe:FREQuency:IMODulation:UTONe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_imodulation.htm#UTONe>`_

                Arguments: GENerator, NONE, PORT
                """

            IMODulation = IMODulation()
            """
            SENSe:FREQuency:IMODulation

            Arguments:
            """

            class LPNoise(SCPINode, SCPIBool):
                """
                `SENSe:FREQuency:LPNoise
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#LPNoise>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "LPNoise"
                args = ["1", "OFF", "ON"]

            LPNoise = LPNoise()
            """
            `SENSe:FREQuency:LPNoise
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#LPNoise>`_

            Arguments: 1, OFF, ON
            """

            class MDELay(SCPINode):
                """
                SENSe:FREQuency:MDELay

                Arguments:
                """
                _cmd = "MDELay"
                args = []

                class ACQuire(SCPINode, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#ACQuire>`_

                    Arguments:
                    """
                    _cmd = "ACQuire"
                    args = []

                ACQuire = ACQuire()
                """
                `SENSe:FREQuency:MDELay:ACQuire
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#ACQuire>`_

                Arguments:
                """

                class APERture(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:APERture
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#APERture>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "APERture"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                APERture = APERture()
                """
                `SENSe:FREQuency:MDELay:APERture
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#APERture>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class CDELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:CDELay
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#CDELay>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "CDELay"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                CDELay = CDELay()
                """
                `SENSe:FREQuency:MDELay:CDELay
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#CDELay>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class CDMode(SCPINode, SCPIBool):
                    """
                    `SENSe:FREQuency:MDELay:CDMode
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#CDMode>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "CDMode"
                    args = ["1", "OFF", "ON"]

                CDMode = CDMode()
                """
                `SENSe:FREQuency:MDELay:CDMode
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#CDMode>`_

                Arguments: 1, OFF, ON
                """

                class COMBiner(SCPINode, SCPIBool):
                    """
                    SENSe:FREQuency:MDELay:COMBiner

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "COMBiner"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:MDELay:COMBiner:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#COMBiner_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SENSe:FREQuency:MDELay:COMBiner:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#COMBiner_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                COMBiner = COMBiner()
                """
                SENSe:FREQuency:MDELay:COMBiner

                Arguments: 1, OFF, ON
                """

                class CONVersion(SCPINode, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:CONVersion
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#CONVersion>`_

                    Arguments: OFF
                    """
                    _cmd = "CONVersion"
                    args = ["OFF"]

                CONVersion = CONVersion()
                """
                `SENSe:FREQuency:MDELay:CONVersion
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#CONVersion>`_

                Arguments: OFF
                """

                class CORRection(SCPINode, SCPIBool):
                    """
                    SENSe:FREQuency:MDELay:CORRection

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "CORRection"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:MDELay:CORRection:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#CORRection_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SENSe:FREQuency:MDELay:CORRection:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#CORRection_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                CORRection = CORRection()
                """
                SENSe:FREQuency:MDELay:CORRection

                Arguments: 1, OFF, ON
                """

                class DIVide(SCPINode, SCPIBool):
                    """
                    `SENSe:FREQuency:MDELay:DIVide
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#DIVide>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "DIVide"
                    args = ["1", "OFF", "ON"]

                DIVide = DIVide()
                """
                `SENSe:FREQuency:MDELay:DIVide
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#DIVide>`_

                Arguments: 1, OFF, ON
                """

                class RECeiver(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:RECeiver
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#RECeiver>`_

                    Arguments: EXTernal, INTernal
                    """
                    _cmd = "RECeiver"
                    args = ["EXTernal", "INTernal"]

                    class USE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:MDELay:RECeiver:USE
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#RECeiver_USE>`_

                        Arguments: LAN1, LAN2
                        """
                        _cmd = "USE"
                        args = ["LAN1", "LAN2"]

                    USE = USE()
                    """
                    `SENSe:FREQuency:MDELay:RECeiver:USE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#RECeiver_USE>`_

                    Arguments: LAN1, LAN2
                    """

                RECeiver = RECeiver()
                """
                `SENSe:FREQuency:MDELay:RECeiver
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#RECeiver>`_

                Arguments: EXTernal, INTernal
                """

                class UTONe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:UTONe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#UTONe>`_

                    Arguments: GENerator, NONE, PORT
                    """
                    _cmd = "UTONe"
                    args = ["GENerator", "NONE", "PORT"]

                UTONe = UTONe()
                """
                `SENSe:FREQuency:MDELay:UTONe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_mdelay.htm#UTONe>`_

                Arguments: GENerator, NONE, PORT
                """

            MDELay = MDELay()
            """
            SENSe:FREQuency:MDELay

            Arguments:
            """

            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#MODE>`_

                Arguments: CW, FIXed, SEGMent, SWEEp
                """
                _cmd = "MODE"
                args = ["CW", "FIXed", "SEGMent", "SWEEp"]

            MODE = MODE()
            """
            `SENSe:FREQuency:MODE
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#MODE>`_

            Arguments: CW, FIXed, SEGMent, SWEEp
            """

            class OFFSet(SCPINode):
                """
                SENSe:FREQuency:OFFSet

                Arguments:
                """
                _cmd = "OFFSet"
                args = []

                class PWAVes(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:OFFSet:PWAVes
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#OFFSet_PWAVes>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "PWAVes"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                PWAVes = PWAVes()
                """
                `SENSe:FREQuency:OFFSet:PWAVes
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#OFFSet_PWAVes>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class WAVes(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:OFFSet:WAVes
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#OFFSet_WAVes>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "WAVes"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                WAVes = WAVes()
                """
                `SENSe:FREQuency:OFFSet:WAVes
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#OFFSet_WAVes>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            OFFSet = OFFSet()
            """
            SENSe:FREQuency:OFFSet

            Arguments:
            """

            class SBANd(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:SBANd
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#SBANd>`_

                Arguments: AUTO, NEGative, POSitive
                """
                _cmd = "SBANd"
                args = ["AUTO", "NEGative", "POSitive"]

            SBANd = SBANd()
            """
            `SENSe:FREQuency:SBANd
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#SBANd>`_

            Arguments: AUTO, NEGative, POSitive
            """

            class SPAN(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:SPAN
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#SPAN>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SPAN"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            SPAN = SPAN()
            """
            `SENSe:FREQuency:SPAN
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#SPAN>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:STARt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#STARt>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "STARt"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            STARt = STARt()
            """
            `SENSe:FREQuency:STARt
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#STARt>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class STOP(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:STOP
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#STOP>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "STOP"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            STOP = STOP()
            """
            `SENSe:FREQuency:STOP
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_frequency_cw.htm#STOP>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        FREQuency = FREQuency()
        """
        SENSe:FREQuency

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class FUNCtion(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:FUNCtion

            Arguments: 'string'
            """
            _cmd = "FUNCtion"
            args = ["'string'"]

            class ON(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FUNCtion:ON
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_function.htm#FUNCtion>`_

                Arguments: 'XFRequency:POWer:A1', 'XFRequency:POWer:B1', 'XFRequency:POWer:KFACtor', 'XFRequency:POWer:MUFactor1', 'XFRequency:POWer:RATio', 'XFRequency:POWer:S1', 'XFRequency:POWer:S1:DUMMy', 'XFRequency:POWer:Y1', 'XFRequency:POWer:Z1', 'XFRequency:VOLTage', 'XFRequency:VOLTage:DC', 'XPOWer:POWer:A1', 'XPOWer:POWer:B1', 'XPOWer:POWer:RATio', 'XPOWer:POWer:S1', 'XPOWer:POWer:S1:DUMMy', 'XPOWer:POWer:Y1', 'XPOWer:POWer:Z1', 'XPOWer:VOLTage', 'XPOWer:VOLTage:DC', 'XTIMe:POWer:A1', 'XTIMe:POWer:B1', 'XTIMe:POWer:KFACtor', 'XTIMe:POWer:MUFactor1', 'XTIMe:POWer:RATio', 'XTIMe:POWer:S1', 'XTIMe:POWer:S1:DUMMy', 'XTIMe:POWer:Y1', 'XTIMe:POWer:Z1', 'XTIMe:VOLTage', 'XTIMe:VOLTage:DC'
                """
                _cmd = "ON"
                args = ["'XFRequency:POWer:A1'", "'XFRequency:POWer:B1'", "'XFRequency:POWer:KFACtor'", "'XFRequency:POWer:MUFactor1'", "'XFRequency:POWer:RATio'", "'XFRequency:POWer:S1'", "'XFRequency:POWer:S1:DUMMy'", "'XFRequency:POWer:Y1'", "'XFRequency:POWer:Z1'", "'XFRequency:VOLTage'", "'XFRequency:VOLTage:DC'", "'XPOWer:POWer:A1'", "'XPOWer:POWer:B1'", "'XPOWer:POWer:RATio'", "'XPOWer:POWer:S1'", "'XPOWer:POWer:S1:DUMMy'", "'XPOWer:POWer:Y1'", "'XPOWer:POWer:Z1'", "'XPOWer:VOLTage'", "'XPOWer:VOLTage:DC'", "'XTIMe:POWer:A1'", "'XTIMe:POWer:B1'", "'XTIMe:POWer:KFACtor'", "'XTIMe:POWer:MUFactor1'", "'XTIMe:POWer:RATio'", "'XTIMe:POWer:S1'", "'XTIMe:POWer:S1:DUMMy'", "'XTIMe:POWer:Y1'", "'XTIMe:POWer:Z1'", "'XTIMe:VOLTage'", "'XTIMe:VOLTage:DC'"]

            ON = ON()
            """
            `SENSe:FUNCtion:ON
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_function.htm#FUNCtion>`_

            Arguments: 'XFRequency:POWer:A1', 'XFRequency:POWer:B1', 'XFRequency:POWer:KFACtor', 'XFRequency:POWer:MUFactor1', 'XFRequency:POWer:RATio', 'XFRequency:POWer:S1', 'XFRequency:POWer:S1:DUMMy', 'XFRequency:POWer:Y1', 'XFRequency:POWer:Z1', 'XFRequency:VOLTage', 'XFRequency:VOLTage:DC', 'XPOWer:POWer:A1', 'XPOWer:POWer:B1', 'XPOWer:POWer:RATio', 'XPOWer:POWer:S1', 'XPOWer:POWer:S1:DUMMy', 'XPOWer:POWer:Y1', 'XPOWer:POWer:Z1', 'XPOWer:VOLTage', 'XPOWer:VOLTage:DC', 'XTIMe:POWer:A1', 'XTIMe:POWer:B1', 'XTIMe:POWer:KFACtor', 'XTIMe:POWer:MUFactor1', 'XTIMe:POWer:RATio', 'XTIMe:POWer:S1', 'XTIMe:POWer:S1:DUMMy', 'XTIMe:POWer:Y1', 'XTIMe:POWer:Z1', 'XTIMe:VOLTage', 'XTIMe:VOLTage:DC'
            """

        FUNCtion = FUNCtion()
        """
        SENSe:FUNCtion

        Arguments: 'string'
        """

        class IFRequency(SCPINodeN):
            """
            SENSe:IFRequency

            Arguments:
            """
            _cmd = "IFRequency"
            args = []

            class CONVersion(SCPINode):
                """
                SENSe:IFRequency:CONVersion

                Arguments:
                """
                _cmd = "CONVersion"
                args = []

                class ARBitrary(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:IFRequency:CONVersion:ARBitrary

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "ARBitrary"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                ARBitrary = ARBitrary()
                """
                SENSe:IFRequency:CONVersion:ARBitrary

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            CONVersion = CONVersion()
            """
            SENSe:IFRequency:CONVersion

            Arguments:
            """

        IFRequency = IFRequency()
        """
        SENSe:IFRequency

        Arguments:
        """

        class LOMeasure(SCPINodeN, SCPIBool):
            """
            SENSe:LOMeasure

            Arguments: 1, OFF, ON
            """
            _cmd = "LOMeasure"
            args = ["1", "OFF", "ON"]

            class STATe(SCPINode, SCPIBool):
                """
                `SENSe:LOMeasure:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_lomeasure.htm#LOMeasure>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `SENSe:LOMeasure:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_lomeasure.htm#LOMeasure>`_

            Arguments: 1, OFF, ON
            """

        LOMeasure = LOMeasure()
        """
        SENSe:LOMeasure

        Arguments: 1, OFF, ON
        """

        class LOReference(SCPINodeN, SCPIBool):
            """
            SENSe:LOReference

            Arguments: 1, OFF, ON
            """
            _cmd = "LOReference"
            args = ["1", "OFF", "ON"]

            class STATe(SCPINode, SCPIBool):
                """
                `SENSe:LOReference:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_lomeasure.htm#LOReference>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `SENSe:LOReference:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_lomeasure.htm#LOReference>`_

            Arguments: 1, OFF, ON
            """

        LOReference = LOReference()
        """
        SENSe:LOReference

        Arguments: 1, OFF, ON
        """

        class LPORt(SCPINodeN):
            """
            SENSe:LPORt

            Arguments:
            """
            _cmd = "LPORt"
            args = []

            class ZCOMmon(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:LPORt:ZCOMmon
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_lport.htm#ZCOMmon>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "ZCOMmon"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            ZCOMmon = ZCOMmon()
            """
            `SENSe:LPORt:ZCOMmon
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_lport.htm#ZCOMmon>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class ZDIFferent(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:LPORt:ZDIFferent
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_lport.htm#ZDIFferent>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "ZDIFferent"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            ZDIFferent = ZDIFferent()
            """
            `SENSe:LPORt:ZDIFferent
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_lport.htm#ZDIFferent>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        LPORt = LPORt()
        """
        SENSe:LPORt

        Arguments:
        """

        class NFIGure(SCPINode):
            """
            SENSe:NFIGure

            Arguments:
            """
            _cmd = "NFIGure"
            args = []

            class ISNoise(SCPINode, SCPIBool):
                """
                `SENSe:NFIGure:ISNoise
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_nfigure.htm#ISNoise>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "ISNoise"
                args = ["1", "OFF", "ON"]

            ISNoise = ISNoise()
            """
            `SENSe:NFIGure:ISNoise
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_nfigure.htm#ISNoise>`_

            Arguments: 1, OFF, ON
            """

            class NDUT(SCPINode, SCPIBool):
                """
                `SENSe:NFIGure:NDUT
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_nfigure.htm#NDUT>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "NDUT"
                args = ["1", "OFF", "ON"]

            NDUT = NDUT()
            """
            `SENSe:NFIGure:NDUT
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_nfigure.htm#NDUT>`_

            Arguments: 1, OFF, ON
            """

            class RFICorr(SCPINode, SCPIBool):
                """
                `SENSe:NFIGure:RFICorr
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_nfigure.htm#RFICorr>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "RFICorr"
                args = ["1", "OFF", "ON"]

            RFICorr = RFICorr()
            """
            `SENSe:NFIGure:RFICorr
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_nfigure.htm#RFICorr>`_

            Arguments: 1, OFF, ON
            """

            class SEQuential(SCPINode, SCPIBool):
                """
                `SENSe:NFIGure:SEQuential
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_nfigure.htm#SEQuential>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "SEQuential"
                args = ["1", "OFF", "ON"]

            SEQuential = SEQuential()
            """
            `SENSe:NFIGure:SEQuential
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_nfigure.htm#SEQuential>`_

            Arguments: 1, OFF, ON
            """

        NFIGure = NFIGure()
        """
        SENSe:NFIGure

        Arguments:
        """

        class PAE(SCPINode):
            """
            SENSe:PAE

            Arguments:
            """
            _cmd = "PAE"
            args = []

            class C(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PAE:C
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pae.htm#C>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "C"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            C = C()
            """
            `SENSe:PAE:C
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pae.htm#C>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class EXPRession(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PAE:EXPRession
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pae.htm#EXPRession>`_

                Arguments: C1, C10, CK11, K101
                """
                _cmd = "EXPRession"
                args = ["C1", "C10", "CK11", "K101"]

            EXPRession = EXPRession()
            """
            `SENSe:PAE:EXPRession
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pae.htm#EXPRession>`_

            Arguments: C1, C10, CK11, K101
            """

            class K(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PAE:K
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pae.htm#K>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "K"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            K = K()
            """
            `SENSe:PAE:K
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pae.htm#K>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        PAE = PAE()
        """
        SENSe:PAE

        Arguments:
        """

        class PMMO(SCPINode, SCPIBool):
            """
            `SENSe:PMMO
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pmmo.htm#PMMO>`_

            Arguments: 1, OFF, ON
            """
            _cmd = "PMMO"
            args = ["1", "OFF", "ON"]

        PMMO = PMMO()
        """
        `SENSe:PMMO
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pmmo.htm#PMMO>`_

        Arguments: 1, OFF, ON
        """

        class PORT(SCPINodeN):
            """
            SENSe:PORT

            Arguments:
            """
            _cmd = "PORT"
            args = []

            class ZREFerence(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PORT:ZREFerence
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_port.htm#ZREFerence>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "ZREFerence"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            ZREFerence = ZREFerence()
            """
            `SENSe:PORT:ZREFerence
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_port.htm#ZREFerence>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        PORT = PORT()
        """
        SENSe:PORT

        Arguments:
        """

        class POWer(SCPINode):
            """
            SENSe:POWer

            Arguments:
            """
            _cmd = "POWer"
            args = []

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:POWer:ATTenuation
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_power.htm#ATTenuation>`_

                Arguments: 1, ARECeiver, BRECeiver, CRECeiver, DEFault, DOWN, DRECeiver, MAXimum, MINimum, UP
                """
                _cmd = "ATTenuation"
                args = ["1", "ARECeiver", "BRECeiver", "CRECeiver", "DEFault", "DOWN", "DRECeiver", "MAXimum", "MINimum", "UP"]

            ATTenuation = ATTenuation()
            """
            `SENSe:POWer:ATTenuation
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_power.htm#ATTenuation>`_

            Arguments: 1, ARECeiver, BRECeiver, CRECeiver, DEFault, DOWN, DRECeiver, MAXimum, MINimum, UP
            """

            class IFGain(SCPINodeN):
                """
                SENSe:POWer:IFGain

                Arguments:
                """
                _cmd = "IFGain"
                args = []

                class MEASure(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:POWer:IFGain:MEASure
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_power.htm#IFGain_MEASure>`_

                    Arguments: AUTO, LDIStortion, LNOise
                    """
                    _cmd = "MEASure"
                    args = ["AUTO", "LDIStortion", "LNOise"]

                MEASure = MEASure()
                """
                `SENSe:POWer:IFGain:MEASure
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_power.htm#IFGain_MEASure>`_

                Arguments: AUTO, LDIStortion, LNOise
                """

                class REFerence(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:POWer:IFGain:REFerence
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_power.htm#IFGain_REFerence>`_

                    Arguments: AUTO, LDIStortion, LNOise
                    """
                    _cmd = "REFerence"
                    args = ["AUTO", "LDIStortion", "LNOise"]

                REFerence = REFerence()
                """
                `SENSe:POWer:IFGain:REFerence
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_power.htm#IFGain_REFerence>`_

                Arguments: AUTO, LDIStortion, LNOise
                """

            IFGain = IFGain()
            """
            SENSe:POWer:IFGain

            Arguments:
            """

        POWer = POWer()
        """
        SENSe:POWer

        Arguments:
        """

        class PULSe(SCPINode):
            """
            SENSe:PULSe

            Arguments:
            """
            _cmd = "PULSe"
            args = []

            class COUPled(SCPINode, SCPIBool):
                """
                SENSe:PULSe:COUPled

                Arguments: 1, OFF, ON
                """
                _cmd = "COUPled"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:PULSe:COUPled:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#COUPled_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:PULSe:COUPled:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#COUPled_STATe>`_

                Arguments: 1, OFF, ON
                """

            COUPled = COUPled()
            """
            SENSe:PULSe:COUPled

            Arguments: 1, OFF, ON
            """

            class GENerator(SCPINodeN, SCPIBool):
                """
                SENSe:PULSe:GENerator

                Arguments: 1, OFF, ON
                """
                _cmd = "GENerator"
                args = ["1", "OFF", "ON"]

                class CPPRofile(SCPINode, SCPIBool):
                    """
                    `SENSe:PULSe:GENerator:CPPRofile
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#CPPRofile>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "CPPRofile"
                    args = ["1", "OFF", "ON"]

                CPPRofile = CPPRofile()
                """
                `SENSe:PULSe:GENerator:CPPRofile
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#CPPRofile>`_

                Arguments: 1, OFF, ON
                """

                class DELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:DELay
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#DELay>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DELay"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                DELay = DELay()
                """
                `SENSe:PULSe:GENerator:DELay
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#DELay>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class DINCrement(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:DINCrement
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#DINCrement>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DINCrement"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                DINCrement = DINCrement()
                """
                `SENSe:PULSe:GENerator:DINCrement
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#DINCrement>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class MCHannel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:MCHannel
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#MCHannel>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "MCHannel"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                MCHannel = MCHannel()
                """
                `SENSe:PULSe:GENerator:MCHannel
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#MCHannel>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:MODE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#MODE>`_

                    Arguments: CONTinuous, CSPecific
                    """
                    _cmd = "MODE"
                    args = ["CONTinuous", "CSPecific"]

                MODE = MODE()
                """
                `SENSe:PULSe:GENerator:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#MODE>`_

                Arguments: CONTinuous, CSPecific
                """

                class PERiod(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:PERiod
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#PERiod>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "PERiod"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                PERiod = PERiod()
                """
                `SENSe:PULSe:GENerator:PERiod
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#PERiod>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:POLarity
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#POLarity>`_

                    Arguments: INVerted, NORMal
                    """
                    _cmd = "POLarity"
                    args = ["INVerted", "NORMal"]

                POLarity = POLarity()
                """
                `SENSe:PULSe:GENerator:POLarity
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#POLarity>`_

                Arguments: INVerted, NORMal
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:PULSe:GENerator:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:PULSe:GENerator:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#STATe>`_

                Arguments: 1, OFF, ON
                """

                class TRAin(SCPINode):
                    """
                    SENSe:PULSe:GENerator:TRAin

                    Arguments:
                    """
                    _cmd = "TRAin"
                    args = []

                    class DATA(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:PULSe:GENerator:TRAin:DATA
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_DATA>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "DATA"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    DATA = DATA()
                    """
                    `SENSe:PULSe:GENerator:TRAin:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_DATA>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class DELete(SCPINode):
                        """
                        SENSe:PULSe:GENerator:TRAin:DELete

                        Arguments:
                        """
                        _cmd = "DELete"
                        args = []

                        class ALL(SCPINode, SCPISet):
                            """
                            `SENSe:PULSe:GENerator:TRAin:DELete:ALL
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_DELete_ALL>`_

                            Arguments:
                            """
                            _cmd = "ALL"
                            args = []

                        ALL = ALL()
                        """
                        `SENSe:PULSe:GENerator:TRAin:DELete:ALL
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_DELete_ALL>`_

                        Arguments:
                        """

                    DELete = DELete()
                    """
                    SENSe:PULSe:GENerator:TRAin:DELete

                    Arguments:
                    """

                    class PERiod(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:PULSe:GENerator:TRAin:PERiod
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAIn_PERiod>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PERiod"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    PERiod = PERiod()
                    """
                    `SENSe:PULSe:GENerator:TRAin:PERiod
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAIn_PERiod>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class SEGMent(SCPINodeN, SCPIBool):
                        """
                        SENSe:PULSe:GENerator:TRAin:SEGMent

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "SEGMent"
                        args = ["1", "OFF", "ON"]

                        class COUNt(SCPINode, SCPIQuery):
                            """
                            `SENSe:PULSe:GENerator:TRAin:SEGMent:COUNt
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGMent_COUNt>`_

                            Arguments:
                            """
                            _cmd = "COUNt"
                            args = []

                        COUNt = COUNt()
                        """
                        `SENSe:PULSe:GENerator:TRAin:SEGMent:COUNt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGMent_COUNt>`_

                        Arguments:
                        """

                        class STARt(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:PULSe:GENerator:TRAin:SEGMent:STARt
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGment_STATe>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "STARt"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        STARt = STARt()
                        """
                        `SENSe:PULSe:GENerator:TRAin:SEGMent:STARt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGment_STATe>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            `SENSe:PULSe:GENerator:TRAin:SEGMent:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGment_STIMulus_STOP>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `SENSe:PULSe:GENerator:TRAin:SEGMent:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGment_STIMulus_STOP>`_

                        Arguments: 1, OFF, ON
                        """

                        class STOP(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:PULSe:GENerator:TRAin:SEGMent:STOP
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGMent_STIMulus_STARt>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "STOP"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        STOP = STOP()
                        """
                        `SENSe:PULSe:GENerator:TRAin:SEGMent:STOP
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGMent_STIMulus_STARt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                    SEGMent = SEGMent()
                    """
                    SENSe:PULSe:GENerator:TRAin:SEGMent

                    Arguments: 1, OFF, ON
                    """

                TRAin = TRAin()
                """
                SENSe:PULSe:GENerator:TRAin

                Arguments:
                """

                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:TYPE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TYPE>`_

                    Arguments: CHIGh, CLOW, SINGle, TRAin
                    """
                    _cmd = "TYPE"
                    args = ["CHIGh", "CLOW", "SINGle", "TRAin"]

                TYPE = TYPE()
                """
                `SENSe:PULSe:GENerator:TYPE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#TYPE>`_

                Arguments: CHIGh, CLOW, SINGle, TRAin
                """

                class WIDTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:WIDTh
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#WIDTh>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "WIDTh"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                WIDTh = WIDTh()
                """
                `SENSe:PULSe:GENerator:WIDTh
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse_generator.htm#WIDTh>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            GENerator = GENerator()
            """
            SENSe:PULSe:GENerator

            Arguments: 1, OFF, ON
            """

            class RECeiver(SCPINode):
                """
                SENSe:PULSe:RECeiver

                Arguments:
                """
                _cmd = "RECeiver"
                args = []

                class A(SCPINodeN):
                    """
                    SENSe:PULSe:RECeiver:A

                    Arguments:
                    """
                    _cmd = "A"
                    args = []

                    class GENerator(SCPINodeN):
                        """
                        SENSe:PULSe:RECeiver:A:GENerator

                        Arguments:
                        """
                        _cmd = "GENerator"
                        args = []

                        class EVALuation(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:A:GENerator:EVALuation

                            Arguments:
                            """
                            _cmd = "EVALuation"
                            args = []

                            class MODE(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:GENerator:EVALuation:MODE
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__EVALuation_MODE>`_

                                Arguments: MEAN, NORMal
                                """
                                _cmd = "MODE"
                                args = ["MEAN", "NORMal"]

                            MODE = MODE()
                            """
                            `SENSe:PULSe:RECeiver:A:GENerator:EVALuation:MODE
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__EVALuation_MODE>`_

                            Arguments: MEAN, NORMal
                            """

                            class STARt(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:GENerator:EVALuation:STARt
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__EVALuation_STARt>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "STARt"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            STARt = STARt()
                            """
                            `SENSe:PULSe:RECeiver:A:GENerator:EVALuation:STARt
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__EVALuation_STARt>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                            class STOP(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:GENerator:EVALuation:STOP
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__EVALuation_STOP>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "STOP"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            STOP = STOP()
                            """
                            `SENSe:PULSe:RECeiver:A:GENerator:EVALuation:STOP
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__EVALuation_STOP>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                        EVALuation = EVALuation()
                        """
                        SENSe:PULSe:RECeiver:A:GENerator:EVALuation

                        Arguments:
                        """

                        class LINes(SCPINode, SCPIBool):
                            """
                            SENSe:PULSe:RECeiver:A:GENerator:LINes

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "LINes"
                            args = ["1", "OFF", "ON"]

                            class STATe(SCPINode, SCPIBool):
                                """
                                `SENSe:PULSe:RECeiver:A:GENerator:LINes:STATe
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__LINEs_STATe>`_

                                Arguments: 1, OFF, ON
                                """
                                _cmd = "STATe"
                                args = ["1", "OFF", "ON"]

                            STATe = STATe()
                            """
                            `SENSe:PULSe:RECeiver:A:GENerator:LINes:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__LINEs_STATe>`_

                            Arguments: 1, OFF, ON
                            """

                        LINes = LINes()
                        """
                        SENSe:PULSe:RECeiver:A:GENerator:LINes

                        Arguments: 1, OFF, ON
                        """

                        class TRIGger(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:A:GENerator:TRIGger

                            Arguments:
                            """
                            _cmd = "TRIGger"
                            args = []

                            class DELay(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:GENerator:TRIGger:DELay
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__TRIGger_DELay>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "DELay"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            DELay = DELay()
                            """
                            `SENSe:PULSe:RECeiver:A:GENerator:TRIGger:DELay
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__TRIGger_DELay>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                        TRIGger = TRIGger()
                        """
                        SENSe:PULSe:RECeiver:A:GENerator:TRIGger

                        Arguments:
                        """

                    GENerator = GENerator()
                    """
                    SENSe:PULSe:RECeiver:A:GENerator

                    Arguments:
                    """

                    class SRCPort(SCPINodeN):
                        """
                        SENSe:PULSe:RECeiver:A:SRCPort

                        Arguments:
                        """
                        _cmd = "SRCPort"
                        args = []

                        class EVALuation(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:A:SRCPort:EVALuation

                            Arguments:
                            """
                            _cmd = "EVALuation"
                            args = []

                            class MODE(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:SRCPort:EVALuation:MODE
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__EVALuation_MODE>`_

                                Arguments: MEAN, NORMal
                                """
                                _cmd = "MODE"
                                args = ["MEAN", "NORMal"]

                            MODE = MODE()
                            """
                            `SENSe:PULSe:RECeiver:A:SRCPort:EVALuation:MODE
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__EVALuation_MODE>`_

                            Arguments: MEAN, NORMal
                            """

                            class STARt(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:SRCPort:EVALuation:STARt
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__EVALuation_STARt>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "STARt"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            STARt = STARt()
                            """
                            `SENSe:PULSe:RECeiver:A:SRCPort:EVALuation:STARt
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__EVALuation_STARt>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                            class STOP(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:SRCPort:EVALuation:STOP
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__EVALuation_STOP>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "STOP"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            STOP = STOP()
                            """
                            `SENSe:PULSe:RECeiver:A:SRCPort:EVALuation:STOP
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__EVALuation_STOP>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                        EVALuation = EVALuation()
                        """
                        SENSe:PULSe:RECeiver:A:SRCPort:EVALuation

                        Arguments:
                        """

                        class LINes(SCPINode, SCPIBool):
                            """
                            SENSe:PULSe:RECeiver:A:SRCPort:LINes

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "LINes"
                            args = ["1", "OFF", "ON"]

                            class STATe(SCPINode, SCPIBool):
                                """
                                `SENSe:PULSe:RECeiver:A:SRCPort:LINes:STATe
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__LINEs_STATe>`_

                                Arguments: 1, OFF, ON
                                """
                                _cmd = "STATe"
                                args = ["1", "OFF", "ON"]

                            STATe = STATe()
                            """
                            `SENSe:PULSe:RECeiver:A:SRCPort:LINes:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__LINEs_STATe>`_

                            Arguments: 1, OFF, ON
                            """

                        LINes = LINes()
                        """
                        SENSe:PULSe:RECeiver:A:SRCPort:LINes

                        Arguments: 1, OFF, ON
                        """

                        class TRIGger(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:A:SRCPort:TRIGger

                            Arguments:
                            """
                            _cmd = "TRIGger"
                            args = []

                            class DELay(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:SRCPort:TRIGger:DELay
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__TRIGger_DELay>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "DELay"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            DELay = DELay()
                            """
                            `SENSe:PULSe:RECeiver:A:SRCPort:TRIGger:DELay
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__TRIGger_DELay>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                        TRIGger = TRIGger()
                        """
                        SENSe:PULSe:RECeiver:A:SRCPort:TRIGger

                        Arguments:
                        """

                    SRCPort = SRCPort()
                    """
                    SENSe:PULSe:RECeiver:A:SRCPort

                    Arguments:
                    """

                A = A()
                """
                SENSe:PULSe:RECeiver:A

                Arguments:
                """

                class B(SCPINodeN):
                    """
                    SENSe:PULSe:RECeiver:B

                    Arguments:
                    """
                    _cmd = "B"
                    args = []

                    class GENerator(SCPINodeN):
                        """
                        SENSe:PULSe:RECeiver:B:GENerator

                        Arguments:
                        """
                        _cmd = "GENerator"
                        args = []

                        class EVALuation(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:B:GENerator:EVALuation

                            Arguments:
                            """
                            _cmd = "EVALuation"
                            args = []

                            class MODE(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:GENerator:EVALuation:MODE
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__EVALuation_MODE>`_

                                Arguments: MEAN, NORMal
                                """
                                _cmd = "MODE"
                                args = ["MEAN", "NORMal"]

                            MODE = MODE()
                            """
                            `SENSe:PULSe:RECeiver:B:GENerator:EVALuation:MODE
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__EVALuation_MODE>`_

                            Arguments: MEAN, NORMal
                            """

                            class STARt(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:GENerator:EVALuation:STARt
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__EVALuation_STARt>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "STARt"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            STARt = STARt()
                            """
                            `SENSe:PULSe:RECeiver:B:GENerator:EVALuation:STARt
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__EVALuation_STARt>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                            class STOP(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:GENerator:EVALuation:STOP
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__EVALuation_STOP>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "STOP"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            STOP = STOP()
                            """
                            `SENSe:PULSe:RECeiver:B:GENerator:EVALuation:STOP
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__EVALuation_STOP>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                        EVALuation = EVALuation()
                        """
                        SENSe:PULSe:RECeiver:B:GENerator:EVALuation

                        Arguments:
                        """

                        class LINes(SCPINode, SCPIBool):
                            """
                            SENSe:PULSe:RECeiver:B:GENerator:LINes

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "LINes"
                            args = ["1", "OFF", "ON"]

                            class STATe(SCPINode, SCPIBool):
                                """
                                `SENSe:PULSe:RECeiver:B:GENerator:LINes:STATe
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__LINEs_STATe>`_

                                Arguments: 1, OFF, ON
                                """
                                _cmd = "STATe"
                                args = ["1", "OFF", "ON"]

                            STATe = STATe()
                            """
                            `SENSe:PULSe:RECeiver:B:GENerator:LINes:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__LINEs_STATe>`_

                            Arguments: 1, OFF, ON
                            """

                        LINes = LINes()
                        """
                        SENSe:PULSe:RECeiver:B:GENerator:LINes

                        Arguments: 1, OFF, ON
                        """

                        class TRIGger(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:B:GENerator:TRIGger

                            Arguments:
                            """
                            _cmd = "TRIGger"
                            args = []

                            class DELay(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:GENerator:TRIGger:DELay
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__TRIGger_DELay>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "DELay"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            DELay = DELay()
                            """
                            `SENSe:PULSe:RECeiver:B:GENerator:TRIGger:DELay
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__TRIGger_DELay>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                        TRIGger = TRIGger()
                        """
                        SENSe:PULSe:RECeiver:B:GENerator:TRIGger

                        Arguments:
                        """

                    GENerator = GENerator()
                    """
                    SENSe:PULSe:RECeiver:B:GENerator

                    Arguments:
                    """

                    class SRCPort(SCPINodeN):
                        """
                        SENSe:PULSe:RECeiver:B:SRCPort

                        Arguments:
                        """
                        _cmd = "SRCPort"
                        args = []

                        class EVALuation(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:B:SRCPort:EVALuation

                            Arguments:
                            """
                            _cmd = "EVALuation"
                            args = []

                            class MODE(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:SRCPort:EVALuation:MODE
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__EVALuation_MODE>`_

                                Arguments: MEAN, NORMal
                                """
                                _cmd = "MODE"
                                args = ["MEAN", "NORMal"]

                            MODE = MODE()
                            """
                            `SENSe:PULSe:RECeiver:B:SRCPort:EVALuation:MODE
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__EVALuation_MODE>`_

                            Arguments: MEAN, NORMal
                            """

                            class STARt(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:SRCPort:EVALuation:STARt
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__EVALuation_STARt>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "STARt"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            STARt = STARt()
                            """
                            `SENSe:PULSe:RECeiver:B:SRCPort:EVALuation:STARt
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__EVALuation_STARt>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                            class STOP(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:SRCPort:EVALuation:STOP
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__EVALuation_STOP>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "STOP"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            STOP = STOP()
                            """
                            `SENSe:PULSe:RECeiver:B:SRCPort:EVALuation:STOP
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__EVALuation_STOP>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                        EVALuation = EVALuation()
                        """
                        SENSe:PULSe:RECeiver:B:SRCPort:EVALuation

                        Arguments:
                        """

                        class LINes(SCPINode, SCPIBool):
                            """
                            SENSe:PULSe:RECeiver:B:SRCPort:LINes

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "LINes"
                            args = ["1", "OFF", "ON"]

                            class STATe(SCPINode, SCPIBool):
                                """
                                `SENSe:PULSe:RECeiver:B:SRCPort:LINes:STATe
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__LINEs_STATe>`_

                                Arguments: 1, OFF, ON
                                """
                                _cmd = "STATe"
                                args = ["1", "OFF", "ON"]

                            STATe = STATe()
                            """
                            `SENSe:PULSe:RECeiver:B:SRCPort:LINes:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__LINEs_STATe>`_

                            Arguments: 1, OFF, ON
                            """

                        LINes = LINes()
                        """
                        SENSe:PULSe:RECeiver:B:SRCPort:LINes

                        Arguments: 1, OFF, ON
                        """

                        class TRIGger(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:B:SRCPort:TRIGger

                            Arguments:
                            """
                            _cmd = "TRIGger"
                            args = []

                            class DELay(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:SRCPort:TRIGger:DELay
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__TRIGger_DELay>`_

                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "DELay"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                            DELay = DELay()
                            """
                            `SENSe:PULSe:RECeiver:B:SRCPort:TRIGger:DELay
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__TRIGger_DELay>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """

                        TRIGger = TRIGger()
                        """
                        SENSe:PULSe:RECeiver:B:SRCPort:TRIGger

                        Arguments:
                        """

                    SRCPort = SRCPort()
                    """
                    SENSe:PULSe:RECeiver:B:SRCPort

                    Arguments:
                    """

                B = B()
                """
                SENSe:PULSe:RECeiver:B

                Arguments:
                """

            RECeiver = RECeiver()
            """
            SENSe:PULSe:RECeiver

            Arguments:
            """

            class TIME(SCPINode):
                """
                SENSe:PULSe:TIME

                Arguments:
                """
                _cmd = "TIME"
                args = []

                class BWIDth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:PULSe:TIME:BWIDth

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "BWIDth"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    class RESolution(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:PULSe:TIME:BWIDth:RESolution
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#TIME_BWIDth>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RESolution"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    RESolution = RESolution()
                    """
                    `SENSe:PULSe:TIME:BWIDth:RESolution
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#TIME_BWIDth>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                BWIDth = BWIDth()
                """
                SENSe:PULSe:TIME:BWIDth

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:TIME:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#TIME_STARt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "STARt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                STARt = STARt()
                """
                `SENSe:PULSe:TIME:STARt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#TIME_STARt>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:TIME:STOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#TIME_STOP>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "STOP"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                STOP = STOP()
                """
                `SENSe:PULSe:TIME:STOP
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_pulse.htm#TIME_STOP>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            TIME = TIME()
            """
            SENSe:PULSe:TIME

            Arguments:
            """

        PULSe = PULSe()
        """
        SENSe:PULSe

        Arguments:
        """

        class ROSCillator(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:ROSCillator

            Arguments: EXTernal, INTernal
            """
            _cmd = "ROSCillator"
            args = ["EXTernal", "INTernal"]

            class EXTernal(SCPINode):
                """
                SENSe:ROSCillator:EXTernal

                Arguments:
                """
                _cmd = "EXTernal"
                args = []

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:ROSCillator:EXTernal:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_roscillator.htm#EXTernal_FREQuency>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "FREQuency"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                FREQuency = FREQuency()
                """
                `SENSe:ROSCillator:EXTernal:FREQuency
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_roscillator.htm#EXTernal_FREQuency>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            EXTernal = EXTernal()
            """
            SENSe:ROSCillator:EXTernal

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:ROSCillator:SOURce
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_roscillator.htm#SOURce>`_

                Arguments: EXTernal, INTernal
                """
                _cmd = "SOURce"
                args = ["EXTernal", "INTernal"]

            SOURce = SOURce()
            """
            `SENSe:ROSCillator:SOURce
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_roscillator.htm#SOURce>`_

            Arguments: EXTernal, INTernal
            """

        ROSCillator = ROSCillator()
        """
        SENSe:ROSCillator

        Arguments: EXTernal, INTernal
        """

        class SEGMent(SCPINodeN, SCPIBool):
            """
            SENSe:SEGMent

            Arguments: 1, OFF, ON
            """
            _cmd = "SEGMent"
            args = ["1", "OFF", "ON"]

            class ADD(SCPINode, SCPISet):
                """
                `SENSe:SEGMent:ADD
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#ADD>`_

                Arguments:
                """
                _cmd = "ADD"
                args = []

            ADD = ADD()
            """
            `SENSe:SEGMent:ADD
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#ADD>`_

            Arguments:
            """

            class BWIDth(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SEGMent:BWIDth

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "BWIDth"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class RESolution(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:BWIDth:RESolution
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#BWIDth>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RESolution"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    class CONTrol(SCPINode, SCPIBool):
                        """
                        `SENSe:SEGMent:BWIDth:RESolution:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#BWIDth_CONTrol>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "CONTrol"
                        args = ["1", "OFF", "ON"]

                    CONTrol = CONTrol()
                    """
                    `SENSe:SEGMent:BWIDth:RESolution:CONTrol
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#BWIDth_CONTrol>`_

                    Arguments: 1, OFF, ON
                    """

                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:BWIDth:RESolution:SELect
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#BWIDth_SELect>`_

                        Arguments: HIGH, NORMal
                        """
                        _cmd = "SELect"
                        args = ["HIGH", "NORMal"]

                        class CONTrol(SCPINode, SCPIBool):
                            """
                            `SENSe:SEGMent:BWIDth:RESolution:SELect:CONTrol
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#BWIDth_SELect_CONTrol>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "CONTrol"
                            args = ["1", "OFF", "ON"]

                        CONTrol = CONTrol()
                        """
                        `SENSe:SEGMent:BWIDth:RESolution:SELect:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#BWIDth_SELect_CONTrol>`_

                        Arguments: 1, OFF, ON
                        """

                    SELect = SELect()
                    """
                    `SENSe:SEGMent:BWIDth:RESolution:SELect
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#BWIDth_SELect>`_

                    Arguments: HIGH, NORMal
                    """

                RESolution = RESolution()
                """
                `SENSe:SEGMent:BWIDth:RESolution
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#BWIDth>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            BWIDth = BWIDth()
            """
            SENSe:SEGMent:BWIDth

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class CLEar(SCPINode, SCPISet):
                """
                `SENSe:SEGMent:CLEar
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#CLEAr>`_

                Arguments:
                """
                _cmd = "CLEar"
                args = []

            CLEar = CLEar()
            """
            `SENSe:SEGMent:CLEar
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#CLEAr>`_

            Arguments:
            """

            class COUNt(SCPINode, SCPIQuery):
                """
                `SENSe:SEGMent:COUNt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#COUNt>`_

                Arguments:
                """
                _cmd = "COUNt"
                args = []

            COUNt = COUNt()
            """
            `SENSe:SEGMent:COUNt
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#COUNt>`_

            Arguments:
            """

            class DEFine(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:DEFine
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DEFine>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "DEFine"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:DEFine:SELect
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DEFine_SELect>`_

                    Arguments: DWELl, SWTime
                    """
                    _cmd = "SELect"
                    args = ["DWELl", "SWTime"]

                SELect = SELect()
                """
                `SENSe:SEGMent:DEFine:SELect
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DEFine_SELect>`_

                Arguments: DWELl, SWTime
                """

            DEFine = DEFine()
            """
            `SENSe:SEGMent:DEFine
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DEFine>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class DELete(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:DELete
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DELete>`_

                Arguments:
                """
                _cmd = "DELete"
                args = []

                class ALL(SCPINode, SCPISet):
                    """
                    `SENSe:SEGMent:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DELete_ALL>`_

                    Arguments:
                    """
                    _cmd = "ALL"
                    args = []

                ALL = ALL()
                """
                `SENSe:SEGMent:DELete:ALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DELete_ALL>`_

                Arguments:
                """

                class DUMMy(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:SEGMent:DELete:DUMMy

                    Arguments:
                    """
                    _cmd = "DUMMy"
                    args = []

                DUMMy = DUMMy()
                """
                SENSe:SEGMent:DELete:DUMMy

                Arguments:
                """

            DELete = DELete()
            """
            `SENSe:SEGMent:DELete
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DELete>`_

            Arguments:
            """

            class FREQuency(SCPINode):
                """
                SENSe:SEGMent:FREQuency

                Arguments:
                """
                _cmd = "FREQuency"
                args = []

                class CENTer(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:CENTer
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#CENTer>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "CENTer"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                CENTer = CENTer()
                """
                `SENSe:SEGMent:FREQuency:CENTer
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#CENTer>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class SPAN(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:SPAN
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#SPAN>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SPAN"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                SPAN = SPAN()
                """
                `SENSe:SEGMent:FREQuency:SPAN
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#SPAN>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#STARt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "STARt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                STARt = STARt()
                """
                `SENSe:SEGMent:FREQuency:STARt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#STARt>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:STOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#STOP>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "STOP"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                STOP = STOP()
                """
                `SENSe:SEGMent:FREQuency:STOP
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#STOP>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            FREQuency = FREQuency()
            """
            SENSe:SEGMent:FREQuency

            Arguments:
            """

            class INSert(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:INSert
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#INSert>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "INSert"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:INSert:SELect
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#OVERlap>`_

                    Arguments: DWELl, SWTime
                    """
                    _cmd = "SELect"
                    args = ["DWELl", "SWTime"]

                SELect = SELect()
                """
                `SENSe:SEGMent:INSert:SELect
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#OVERlap>`_

                Arguments: DWELl, SWTime
                """

            INSert = INSert()
            """
            `SENSe:SEGMent:INSert
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#INSert>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:NAME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#NAME>`_

                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]

            NAME = NAME()
            """
            `SENSe:SEGMent:NAME
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#NAME>`_

            Arguments: 'string'
            """

            class OVERlap(SCPINode, SCPIBool):
                """
                `SENSe:SEGMent:OVERlap
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#OVERlap>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "OVERlap"
                args = ["1", "OFF", "ON"]

            OVERlap = OVERlap()
            """
            `SENSe:SEGMent:OVERlap
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#OVERlap>`_

            Arguments: 1, OFF, ON
            """

            class POWer(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SEGMent:POWer

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "POWer"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class LEVel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:POWer:LEVel
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#POWer>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "LEVel"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    class CONTrol(SCPINode, SCPIBool):
                        """
                        `SENSe:SEGMent:POWer:LEVel:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#POWer_CONTrol>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "CONTrol"
                        args = ["1", "OFF", "ON"]

                    CONTrol = CONTrol()
                    """
                    `SENSe:SEGMent:POWer:LEVel:CONTrol
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#POWer_CONTrol>`_

                    Arguments: 1, OFF, ON
                    """

                LEVel = LEVel()
                """
                `SENSe:SEGMent:POWer:LEVel
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#POWer>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            POWer = POWer()
            """
            SENSe:SEGMent:POWer

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class SBANd(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:SBANd
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#SBANd>`_

                Arguments: AUTO, NEGative, POSitive
                """
                _cmd = "SBANd"
                args = ["AUTO", "NEGative", "POSitive"]

                class CONTrol(SCPINode, SCPIBool):
                    """
                    `SENSe:SEGMent:SBANd:CONTrol
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#SBANd_CONTrol>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "CONTrol"
                    args = ["1", "OFF", "ON"]

                CONTrol = CONTrol()
                """
                `SENSe:SEGMent:SBANd:CONTrol
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#SBANd_CONTrol>`_

                Arguments: 1, OFF, ON
                """

            SBANd = SBANd()
            """
            `SENSe:SEGMent:SBANd
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#SBANd>`_

            Arguments: AUTO, NEGative, POSitive
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SENSe:SEGMent:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `SENSe:SEGMent:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#STATe>`_

            Arguments: 1, OFF, ON
            """

            class SWEep(SCPINode):
                """
                SENSe:SEGMent:SWEep

                Arguments:
                """
                _cmd = "SWEep"
                args = []

                class DWELl(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:DWELl
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DWELl>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DWELl"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    class CONTrol(SCPINode, SCPIBool):
                        """
                        `SENSe:SEGMent:SWEep:DWELl:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DWELl_CONTrol>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "CONTrol"
                        args = ["1", "OFF", "ON"]

                    CONTrol = CONTrol()
                    """
                    `SENSe:SEGMent:SWEep:DWELl:CONTrol
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DWELl_CONTrol>`_

                    Arguments: 1, OFF, ON
                    """

                DWELl = DWELl()
                """
                `SENSe:SEGMent:SWEep:DWELl
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#DWELl>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class POINts(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:POINts
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#POINts>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "POINts"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                POINts = POINts()
                """
                `SENSe:SEGMent:SWEep:POINts
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#POINts>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:TIME
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#TIME>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TIME"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    class CONTrol(SCPINode, SCPIBool):
                        """
                        `SENSe:SEGMent:SWEep:TIME:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#TIME_CONTrol>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "CONTrol"
                        args = ["1", "OFF", "ON"]

                    CONTrol = CONTrol()
                    """
                    `SENSe:SEGMent:SWEep:TIME:CONTrol
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#TIME_CONTrol>`_

                    Arguments: 1, OFF, ON
                    """

                    class SUM(SCPINode, SCPIQuery):
                        """
                        `SENSe:SEGMent:SWEep:TIME:SUM
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#TIME_SUM>`_

                        Arguments:
                        """
                        _cmd = "SUM"
                        args = []

                    SUM = SUM()
                    """
                    `SENSe:SEGMent:SWEep:TIME:SUM
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#TIME_SUM>`_

                    Arguments:
                    """

                TIME = TIME()
                """
                `SENSe:SEGMent:SWEep:TIME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#TIME>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            SWEep = SWEep()
            """
            SENSe:SEGMent:SWEep

            Arguments:
            """

            class TRIGger(SCPINode, SCPIBool):
                """
                SENSe:SEGMent:TRIGger

                Arguments: 1, OFF, ON
                """
                _cmd = "TRIGger"
                args = ["1", "OFF", "ON"]

                class CONTrol(SCPINode, SCPIBool):
                    """
                    `SENSe:SEGMent:TRIGger:CONTrol
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#TRIGger_CONTrol>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "CONTrol"
                    args = ["1", "OFF", "ON"]

                CONTrol = CONTrol()
                """
                `SENSe:SEGMent:TRIGger:CONTrol
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#TRIGger_CONTrol>`_

                Arguments: 1, OFF, ON
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:SEGMent:TRIGger:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#TRIGger_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:SEGMent:TRIGger:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_segment.htm#TRIGger_STATe>`_

                Arguments: 1, OFF, ON
                """

            TRIGger = TRIGger()
            """
            SENSe:SEGMent:TRIGger

            Arguments: 1, OFF, ON
            """

        SEGMent = SEGMent()
        """
        SENSe:SEGMent

        Arguments: 1, OFF, ON
        """

        class SWEep(SCPINode):
            """
            SENSe:SWEep

            Arguments:
            """
            _cmd = "SWEep"
            args = []

            class AXIS(SCPINode):
                """
                SENSe:SWEep:AXIS

                Arguments:
                """
                _cmd = "AXIS"
                args = []

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:AXIS:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#AXIS_FREQuency>`_

                    Arguments: 'string'
                    """
                    _cmd = "FREQuency"
                    args = ["'string'"]

                FREQuency = FREQuency()
                """
                `SENSe:SWEep:AXIS:FREQuency
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#AXIS_FREQuency>`_

                Arguments: 'string'
                """

                class POWer(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:AXIS:POWer
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#AXIS_POWer>`_

                    Arguments: 'string'
                    """
                    _cmd = "POWer"
                    args = ["'string'"]

                POWer = POWer()
                """
                `SENSe:SWEep:AXIS:POWer
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#AXIS_POWer>`_

                Arguments: 'string'
                """

            AXIS = AXIS()
            """
            SENSe:SWEep:AXIS

            Arguments:
            """

            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SWEep:COUNt

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "COUNt"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            COUNt = COUNt()
            """
            SENSe:SWEep:COUNt

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class DETector(SCPINode):
                """
                SENSe:SWEep:DETector

                Arguments:
                """
                _cmd = "DETector"
                args = []

                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:DETector:TIME
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#DETector_TIME>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TIME"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                TIME = TIME()
                """
                `SENSe:SWEep:DETector:TIME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#DETector_TIME>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            DETector = DETector()
            """
            SENSe:SWEep:DETector

            Arguments:
            """

            class DWELl(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:DWELl
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#Dwell>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "DWELl"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            DWELl = DWELl()
            """
            `SENSe:SWEep:DWELl
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#Dwell>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class GENeration(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SWEep:GENeration

                Arguments: ANALog, STEPped
                """
                _cmd = "GENeration"
                args = ["ANALog", "STEPped"]

            GENeration = GENeration()
            """
            SENSe:SWEep:GENeration

            Arguments: ANALog, STEPped
            """

            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SWEep:MODE

                Arguments: CONTinuous, HOLD
                """
                _cmd = "MODE"
                args = ["CONTinuous", "HOLD"]

            MODE = MODE()
            """
            SENSe:SWEep:MODE

            Arguments: CONTinuous, HOLD
            """

            class POINts(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:POINts
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "POINts"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            POINts = POINts()
            """
            `SENSe:SWEep:POINts
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class SPACing(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:SPACing
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#SPACing>`_

                Arguments: LINear, LOGarithmic
                """
                _cmd = "SPACing"
                args = ["LINear", "LOGarithmic"]

            SPACing = SPACing()
            """
            `SENSe:SWEep:SPACing
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#SPACing>`_

            Arguments: LINear, LOGarithmic
            """

            class SRCPort(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:SRCPort
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#SRCPort>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SRCPort"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            SRCPort = SRCPort()
            """
            `SENSe:SWEep:SRCPort
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#SRCPort>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class STEP(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:STEP
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#STEP>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "STEP"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            STEP = STEP()
            """
            `SENSe:SWEep:STEP
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#STEP>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:TIME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#Time>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "TIME"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class AUTO(SCPINode, SCPIBool):
                    """
                    `SENSe:SWEep:TIME:AUTO
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#TIME_Auto>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "AUTO"
                    args = ["1", "OFF", "ON"]

                AUTO = AUTO()
                """
                `SENSe:SWEep:TIME:AUTO
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#TIME_Auto>`_

                Arguments: 1, OFF, ON
                """

            TIME = TIME()
            """
            `SENSe:SWEep:TIME
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#Time>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:TYPE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#TYPE>`_

                Arguments: CW, IAMPlitude, IPHase, LINear, LOGarithmic, POINt, POWer, PULSe, SEGMent
                """
                _cmd = "TYPE"
                args = ["CW", "IAMPlitude", "IPHase", "LINear", "LOGarithmic", "POINt", "POWer", "PULSe", "SEGMent"]

            TYPE = TYPE()
            """
            `SENSe:SWEep:TYPE
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_ch___sweep.htm#TYPE>`_

            Arguments: CW, IAMPlitude, IPHase, LINear, LOGarithmic, POINt, POWer, PULSe, SEGMent
            """

        SWEep = SWEep()
        """
        SENSe:SWEep

        Arguments:
        """

        class TEUNit(SCPINode):
            """
            SENSe:TEUNit

            Arguments:
            """
            _cmd = "TEUNit"
            args = []

            class AMONitor(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:TEUNit:AMONitor
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#AMONitor>`_

                Arguments: COMBiner, OUTPut, PMODulator
                """
                _cmd = "AMONitor"
                args = ["COMBiner", "OUTPut", "PMODulator"]

            AMONitor = AMONitor()
            """
            `SENSe:TEUNit:AMONitor
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#AMONitor>`_

            Arguments: COMBiner, OUTPut, PMODulator
            """

            class COMBiner(SCPINodeN, SCPIBool):
                """
                SENSe:TEUNit:COMBiner

                Arguments: 1, OFF, ON
                """
                _cmd = "COMBiner"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:TEUNit:COMBiner:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#COMBiner_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:TEUNit:COMBiner:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#COMBiner_STATe>`_

                Arguments: 1, OFF, ON
                """

            COMBiner = COMBiner()
            """
            SENSe:TEUNit:COMBiner

            Arguments: 1, OFF, ON
            """

            class LNAMplifier(SCPINodeN, SCPIBool):
                """
                SENSe:TEUNit:LNAMplifier

                Arguments: 1, OFF, ON
                """
                _cmd = "LNAMplifier"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:TEUNit:LNAMplifier:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#LNAMplifier_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:TEUNit:LNAMplifier:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#LNAMplifier_STATe>`_

                Arguments: 1, OFF, ON
                """

            LNAMplifier = LNAMplifier()
            """
            SENSe:TEUNit:LNAMplifier

            Arguments: 1, OFF, ON
            """

            class PAMPlifier(SCPINodeN, SCPIBool):
                """
                SENSe:TEUNit:PAMPlifier

                Arguments: 1, OFF, ON
                """
                _cmd = "PAMPlifier"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:TEUNit:PAMPlifier:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#PAMPlifier_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:TEUNit:PAMPlifier:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#PAMPlifier_STATe>`_

                Arguments: 1, OFF, ON
                """

            PAMPlifier = PAMPlifier()
            """
            SENSe:TEUNit:PAMPlifier

            Arguments: 1, OFF, ON
            """

            class PMODulator(SCPINodeN, SCPIBool):
                """
                SENSe:TEUNit:PMODulator

                Arguments: 1, OFF, ON
                """
                _cmd = "PMODulator"
                args = ["1", "OFF", "ON"]

                class INVert(SCPINode, SCPIBool):
                    """
                    `SENSe:TEUNit:PMODulator:INVert
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#PMODulator_INVert>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "INVert"
                    args = ["1", "OFF", "ON"]

                INVert = INVert()
                """
                `SENSe:TEUNit:PMODulator:INVert
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#PMODulator_INVert>`_

                Arguments: 1, OFF, ON
                """

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:PMODulator:SOURce
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#PMODulator_SOURce>`_

                    Arguments: G1EXt, G1INt, G2EXt, G2INt, OFF
                    """
                    _cmd = "SOURce"
                    args = ["G1EXt", "G1INt", "G2EXt", "G2INt", "OFF"]

                SOURce = SOURce()
                """
                `SENSe:TEUNit:PMODulator:SOURce
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#PMODulator_SOURce>`_

                Arguments: G1EXt, G1INt, G2EXt, G2INt, OFF
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:TEUNit:PMODulator:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#PMODulator_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:TEUNit:PMODulator:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#PMODulator_STATe>`_

                Arguments: 1, OFF, ON
                """

            PMODulator = PMODulator()
            """
            SENSe:TEUNit:PMODulator

            Arguments: 1, OFF, ON
            """

            class REAR(SCPINodeN):
                """
                SENSe:TEUNit:REAR

                Arguments:
                """
                _cmd = "REAR"
                args = []

                class INVert(SCPINode, SCPIBool):
                    """
                    `SENSe:TEUNit:REAR:INVert
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#REAR_INVert>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "INVert"
                    args = ["1", "OFF", "ON"]

                INVert = INVert()
                """
                `SENSe:TEUNit:REAR:INVert
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#REAR_INVert>`_

                Arguments: 1, OFF, ON
                """

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:REAR:SOURce
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#REAR_SOURce>`_

                    Arguments: G1EXt, G1INt, G2EXt, G2INt, OFF
                    """
                    _cmd = "SOURce"
                    args = ["G1EXt", "G1INt", "G2EXt", "G2INt", "OFF"]

                SOURce = SOURce()
                """
                `SENSe:TEUNit:REAR:SOURce
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#REAR_SOURce>`_

                Arguments: G1EXt, G1INt, G2EXt, G2INt, OFF
                """

            REAR = REAR()
            """
            SENSe:TEUNit:REAR

            Arguments:
            """

            class UMEas(SCPINodeN, SCPIBool):
                """
                SENSe:TEUNit:UMEas

                Arguments: 1, OFF, ON
                """
                _cmd = "UMEas"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:TEUNit:UMEas:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#UMEas_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:TEUNit:UMEas:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#UMEas_STATe>`_

                Arguments: 1, OFF, ON
                """

            UMEas = UMEas()
            """
            SENSe:TEUNit:UMEas

            Arguments: 1, OFF, ON
            """

            class USOurce(SCPINodeN, SCPIBool):
                """
                SENSe:TEUNit:USOurce

                Arguments: 1, OFF, ON
                """
                _cmd = "USOurce"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:TEUNit:USOurce:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#USOurce_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SENSe:TEUNit:USOurce:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_teunit.htm#USOurce_STATe>`_

                Arguments: 1, OFF, ON
                """

            USOurce = USOurce()
            """
            SENSe:TEUNit:USOurce

            Arguments: 1, OFF, ON
            """

        TEUNit = TEUNit()
        """
        SENSe:TEUNit

        Arguments:
        """

        class UDSParams(SCPINodeN):
            """
            SENSe:UDSParams

            Arguments:
            """
            _cmd = "UDSParams"
            args = []

            class ACTive(SCPINode, SCPIBool):
                """
                `SENSe:UDSParams:ACTive
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_udsparams.htm#ACTive>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "ACTive"
                args = ["1", "OFF", "ON"]

            ACTive = ACTive()
            """
            `SENSe:UDSParams:ACTive
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_udsparams.htm#ACTive>`_

            Arguments: 1, OFF, ON
            """

            class PARam(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:UDSParams:PARam
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_udsparams.htm#PARam>`_

                Arguments: 'string'
                """
                _cmd = "PARam"
                args = ["'string'"]

            PARam = PARam()
            """
            `SENSe:UDSParams:PARam
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/sense/sense_udsparams.htm#PARam>`_

            Arguments: 'string'
            """

        UDSParams = UDSParams()
        """
        SENSe:UDSParams

        Arguments:
        """

    SENSe = SENSe()
    """
    SENSe

    Arguments:
    """

    class SOURce(SCPINodeN):
        """
        SOURce

        Arguments:
        """
        _cmd = "SOURce"
        args = []

        class CMODe(SCPINode):
            """
            SOURce:CMODe

            Arguments:
            """
            _cmd = "CMODe"
            args = []

            class PORT(SCPINodeN, SCPIBool):
                """
                SOURce:CMODe:PORT

                Arguments: 1, OFF, ON
                """
                _cmd = "PORT"
                args = ["1", "OFF", "ON"]

                class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:CMODe:PORT:AMPLitude

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "AMPLitude"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                AMPLitude = AMPLitude()
                """
                SOURce:CMODe:PORT:AMPLitude

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class PHASe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:CMODe:PORT:PHASe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_cmode.htm#PORT_PHASe>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "PHASe"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                PHASe = PHASe()
                """
                `SOURce:CMODe:PORT:PHASe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_cmode.htm#PORT_PHASe>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:CMODe:PORT:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_cmode.htm#PORT_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SOURce:CMODe:PORT:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_cmode.htm#PORT_STATe>`_

                Arguments: 1, OFF, ON
                """

            PORT = PORT()
            """
            SOURce:CMODe:PORT

            Arguments: 1, OFF, ON
            """

            class RPORt(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:CMODe:RPORt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_cmode.htm#REFerence_PORT>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "RPORt"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            RPORt = RPORt()
            """
            `SOURce:CMODe:RPORt
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_cmode.htm#REFerence_PORT>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class TOLerance(SCPINode):
                """
                SOURce:CMODe:TOLerance

                Arguments:
                """
                _cmd = "TOLerance"
                args = []

                class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:CMODe:TOLerance:AMPLitude

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "AMPLitude"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                AMPLitude = AMPLitude()
                """
                SOURce:CMODe:TOLerance:AMPLitude

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class PHASe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:CMODe:TOLerance:PHASe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#TOLerance_PHASe>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "PHASe"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                PHASe = PHASe()
                """
                `SOURce:CMODe:TOLerance:PHASe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#TOLerance_PHASe>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            TOLerance = TOLerance()
            """
            SOURce:CMODe:TOLerance

            Arguments:
            """

        CMODe = CMODe()
        """
        SOURce:CMODe

        Arguments:
        """

        class FREQuency(SCPINodeN, SCPIQuery, SCPISet):
            """
            SOURce:FREQuency

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "FREQuency"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            class CONVersion(SCPINode):
                """
                SOURce:FREQuency:CONVersion

                Arguments:
                """
                _cmd = "CONVersion"
                args = []

                class ARBitrary(SCPINode):
                    """
                    SOURce:FREQuency:CONVersion:ARBitrary

                    Arguments:
                    """
                    _cmd = "ARBitrary"
                    args = []

                    class CFRequency(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:ARBitrary:CFRequency
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#CONVersion_ARBitrary_CFRequency>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "CFRequency"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    CFRequency = CFRequency()
                    """
                    `SOURce:FREQuency:CONVersion:ARBitrary:CFRequency
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#CONVersion_ARBitrary_CFRequency>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class EFRequency(SCPINodeN, SCPIBool):
                        """
                        `SOURce:FREQuency:CONVersion:ARBitrary:EFRequency
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#CONVersion_ARBitrary_EFRequency>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EFRequency"
                        args = ["1", "OFF", "ON"]

                    EFRequency = EFRequency()
                    """
                    `SOURce:FREQuency:CONVersion:ARBitrary:EFRequency
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#CONVersion_ARBitrary_EFRequency>`_

                    Arguments: 1, OFF, ON
                    """

                    class IFRequency(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:ARBitrary:IFRequency
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#CONVersion_ARBitrary_IFRequency>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "IFRequency"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    IFRequency = IFRequency()
                    """
                    `SOURce:FREQuency:CONVersion:ARBitrary:IFRequency
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#CONVersion_ARBitrary_IFRequency>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                ARBitrary = ARBitrary()
                """
                SOURce:FREQuency:CONVersion:ARBitrary

                Arguments:
                """

                class MIXer(SCPINode):
                    """
                    SOURce:FREQuency:CONVersion:MIXer

                    Arguments:
                    """
                    _cmd = "MIXer"
                    args = []

                    class FUNDamental(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:FUNDamental
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#FREQuency_CONVersion_MIXer_FUNDamental>`_

                        Arguments: LO, RF
                        """
                        _cmd = "FUNDamental"
                        args = ["LO", "RF"]

                    FUNDamental = FUNDamental()
                    """
                    `SOURce:FREQuency:CONVersion:MIXer:FUNDamental
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#FREQuency_CONVersion_MIXer_FUNDamental>`_

                    Arguments: LO, RF
                    """

                    class PAFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PAFixed
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#FREQuency_CONVersion_MIXer_PAFIXed>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PAFixed"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    PAFixed = PAFixed()
                    """
                    `SOURce:FREQuency:CONVersion:MIXer:PAFixed
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#FREQuency_CONVersion_MIXer_PAFIXed>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class PFIXed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PFIXed
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#FREQuency_CONVersion_MIXer_PFIXed>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PFIXed"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    PFIXed = PFIXed()
                    """
                    `SOURce:FREQuency:CONVersion:MIXer:PFIXed
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#FREQuency_CONVersion_MIXer_PFIXed>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class PMFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PMFixed
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#PMFixed>`_

                        Arguments: AUXLO, IF, LO, LO1, LO2, RF
                        """
                        _cmd = "PMFixed"
                        args = ["AUXLO", "IF", "LO", "LO1", "LO2", "RF"]

                    PMFixed = PMFixed()
                    """
                    `SOURce:FREQuency:CONVersion:MIXer:PMFixed
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#PMFixed>`_

                    Arguments: AUXLO, IF, LO, LO1, LO2, RF
                    """

                    class PMODe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PMODe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#PMODe>`_

                        Arguments: AUXLO, IF, LO, LO1, LO2, RF
                        """
                        _cmd = "PMODe"
                        args = ["AUXLO", "IF", "LO", "LO1", "LO2", "RF"]

                    PMODe = PMODe()
                    """
                    `SOURce:FREQuency:CONVersion:MIXer:PMODe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#PMODe>`_

                    Arguments: AUXLO, IF, LO, LO1, LO2, RF
                    """

                MIXer = MIXer()
                """
                SOURce:FREQuency:CONVersion:MIXer

                Arguments:
                """

            CONVersion = CONVersion()
            """
            SOURce:FREQuency:CONVersion

            Arguments:
            """

            class CW(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FREQuency:CW

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CW"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            CW = CW()
            """
            SOURce:FREQuency:CW

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class FIXed(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FREQuency:FIXed

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "FIXed"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            FIXed = FIXed()
            """
            SOURce:FREQuency:FIXed

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        FREQuency = FREQuency()
        """
        SOURce:FREQuency

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class GROup(SCPINodeN, SCPIQuery, SCPISet):
            """
            `SOURce:GROup
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "GROup"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            class CLEar(SCPINode, SCPISet):
                """
                `SOURce:GROup:CLEar
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_CLEar>`_

                Arguments: ALL
                """
                _cmd = "CLEar"
                args = ["ALL"]

            CLEar = CLEar()
            """
            `SOURce:GROup:CLEar
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_CLEar>`_

            Arguments: ALL
            """

            class COUNt(SCPINode, SCPIQuery):
                """
                `SOURce:GROup:COUNt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_COUNt>`_

                Arguments:
                """
                _cmd = "COUNt"
                args = []

            COUNt = COUNt()
            """
            `SOURce:GROup:COUNt
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_COUNt>`_

            Arguments:
            """

            class PORTs(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:GROup:PORTs
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_PORTs>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "PORTs"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            PORTs = PORTs()
            """
            `SOURce:GROup:PORTs
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_PORTs>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class SIMultaneous(SCPINode, SCPIBool):
                """
                SOURce:GROup:SIMultaneous

                Arguments: 1, OFF, ON
                """
                _cmd = "SIMultaneous"
                args = ["1", "OFF", "ON"]

                class FOFFset(SCPINode, SCPIBool):
                    """
                    SOURce:GROup:SIMultaneous:FOFFset

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "FOFFset"
                    args = ["1", "OFF", "ON"]

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        `SOURce:GROup:SIMultaneous:FOFFset:CONDition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_CONDition>`_

                        Arguments:
                        """
                        _cmd = "CONDition"
                        args = []

                    CONDition = CONDition()
                    """
                    `SOURce:GROup:SIMultaneous:FOFFset:CONDition
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_CONDition>`_

                    Arguments:
                    """

                    class MOFFset(SCPINode):
                        """
                        SOURce:GROup:SIMultaneous:FOFFset:MOFFset

                        Arguments:
                        """
                        _cmd = "MOFFset"
                        args = []

                        class BWFactor(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:BWFactor
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_MOFFset_BWFactor>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "BWFactor"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        BWFactor = BWFactor()
                        """
                        `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:BWFactor
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_MOFFset_BWFactor>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class DVALue(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:DVALue
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_MOFFset_DVALue>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "DVALue"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        DVALue = DVALue()
                        """
                        `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:DVALue
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_MOFFset_DVALue>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class MODE(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:MODE
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_MOFFset_MODE>`_

                            Arguments: BANDWIDTH, DIRECT
                            """
                            _cmd = "MODE"
                            args = ["BANDWIDTH", "DIRECT"]

                        MODE = MODE()
                        """
                        `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:MODE
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_MOFFset_MODE>`_

                        Arguments: BANDWIDTH, DIRECT
                        """

                    MOFFset = MOFFset()
                    """
                    SOURce:GROup:SIMultaneous:FOFFset:MOFFset

                    Arguments:
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:GROup:SIMultaneous:FOFFset:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SOURce:GROup:SIMultaneous:FOFFset:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                FOFFset = FOFFset()
                """
                SOURce:GROup:SIMultaneous:FOFFset

                Arguments: 1, OFF, ON
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:GROup:SIMultaneous:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SOURce:GROup:SIMultaneous:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_STATe>`_

                Arguments: 1, OFF, ON
                """

            SIMultaneous = SIMultaneous()
            """
            SOURce:GROup:SIMultaneous

            Arguments: 1, OFF, ON
            """

        GROup = GROup()
        """
        `SOURce:GROup
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#GROup>`_

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class LPORt(SCPINodeN, SCPIQuery, SCPISet):
            """
            `SOURce:LPORt
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#LPORt>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "LPORt"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            class CLEar(SCPINode, SCPISet):
                """
                `SOURce:LPORt:CLEar
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#LPORt_CLEar>`_

                Arguments: ALL
                """
                _cmd = "CLEar"
                args = ["ALL"]

            CLEar = CLEar()
            """
            `SOURce:LPORt:CLEar
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#LPORt_CLEar>`_

            Arguments: ALL
            """

        LPORt = LPORt()
        """
        `SOURce:LPORt
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch.htm#LPORt>`_

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class POWer(SCPINodeN, SCPIQuery, SCPISet):
            """
            SOURce:POWer

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "POWer"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            class ALC(SCPINode, SCPIBool):
                """
                SOURce:POWer:ALC

                Arguments: 1, OFF, ON
                """
                _cmd = "ALC"
                args = ["1", "OFF", "ON"]

                class AUBW(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:ALC:AUBW
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#AUBW>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "AUBW"
                    args = ["1", "OFF", "ON"]

                AUBW = AUBW()
                """
                `SOURce:POWer:ALC:AUBW
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#AUBW>`_

                Arguments: 1, OFF, ON
                """

                class BANDwidth(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:BANDwidth
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#BANDwidth>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "BANDwidth"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                BANDwidth = BANDwidth()
                """
                `SOURce:POWer:ALC:BANDwidth
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#BANDwidth>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class CLAMp(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:ALC:CLAMp
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#CLAMp>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "CLAMp"
                    args = ["1", "OFF", "ON"]

                CLAMp = CLAMp()
                """
                `SOURce:POWer:ALC:CLAMp
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#CLAMp>`_

                Arguments: 1, OFF, ON
                """

                class CONTrol(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:ALC:CONTrol
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#CONTrol>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "CONTrol"
                    args = ["1", "OFF", "ON"]

                CONTrol = CONTrol()
                """
                `SOURce:POWer:ALC:CONTrol
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#CONTrol>`_

                Arguments: 1, OFF, ON
                """

                class COUPle(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:ALC:COUPle
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#COUPle>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "COUPle"
                    args = ["1", "OFF", "ON"]

                COUPle = COUPle()
                """
                `SOURce:POWer:ALC:COUPle
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#COUPle>`_

                Arguments: 1, OFF, ON
                """

                class CSTate(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:ALC:CSTate
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#CSTate>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "CSTate"
                    args = ["1", "OFF", "ON"]

                CSTate = CSTate()
                """
                `SOURce:POWer:ALC:CSTate
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#CSTate>`_

                Arguments: 1, OFF, ON
                """

                class LPNoise(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:ALC:LPNoise
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#LPNoise>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "LPNoise"
                    args = ["1", "OFF", "ON"]

                LPNoise = LPNoise()
                """
                `SOURce:POWer:ALC:LPNoise
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#LPNoise>`_

                Arguments: 1, OFF, ON
                """

                class PIParameter(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:PIParameter
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#PIParameter>`_

                    Arguments: AUTO, MANual
                    """
                    _cmd = "PIParameter"
                    args = ["AUTO", "MANual"]

                    class GAIN(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:ALC:PIParameter:GAIN
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#PIParameter_GAIN>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "GAIN"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    GAIN = GAIN()
                    """
                    `SOURce:POWer:ALC:PIParameter:GAIN
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#PIParameter_GAIN>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class ITIMe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:ALC:PIParameter:ITIMe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#PIParameter_ITIMe>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "ITIMe"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    ITIMe = ITIMe()
                    """
                    `SOURce:POWer:ALC:PIParameter:ITIMe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#PIParameter_ITIMe>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                PIParameter = PIParameter()
                """
                `SOURce:POWer:ALC:PIParameter
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#PIParameter>`_

                Arguments: AUTO, MANual
                """

                class POFFset(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:ALC:POFFset
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#POFFset>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "POFFset"
                    args = ["1", "OFF", "ON"]

                POFFset = POFFset()
                """
                `SOURce:POWer:ALC:POFFset
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#POFFset>`_

                Arguments: 1, OFF, ON
                """

                class RANGe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:RANGe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#RANGe>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RANGe"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                RANGe = RANGe()
                """
                `SOURce:POWer:ALC:RANGe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#RANGe>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class SOFFset(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:SOFFset
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#SOFFset>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SOFFset"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                SOFFset = SOFFset()
                """
                `SOURce:POWer:ALC:SOFFset
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#SOFFset>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:ALC:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SOURce:POWer:ALC:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#STATe>`_

                Arguments: 1, OFF, ON
                """

                class STOLerance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:STOLerance
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#STOLerance>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "STOLerance"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                STOLerance = STOLerance()
                """
                `SOURce:POWer:ALC:STOLerance
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_alc.htm#STOLerance>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            ALC = ALC()
            """
            SOURce:POWer:ALC

            Arguments: 1, OFF, ON
            """

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:ATTenuation
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#ATTenuation>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "ATTenuation"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class AUTO(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:ATTenuation:AUTO
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#ATTenuation_AUTO>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "AUTO"
                    args = ["1", "OFF", "ON"]

                    class VALue(SCPINode, SCPIQuery):
                        """
                        `SOURce:POWer:ATTenuation:AUTO:VALue
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#ATTenuation_AUTO_VALue>`_

                        Arguments:
                        """
                        _cmd = "VALue"
                        args = []

                    VALue = VALue()
                    """
                    `SOURce:POWer:ATTenuation:AUTO:VALue
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#ATTenuation_AUTO_VALue>`_

                    Arguments:
                    """

                AUTO = AUTO()
                """
                `SOURce:POWer:ATTenuation:AUTO
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#ATTenuation_AUTO>`_

                Arguments: 1, OFF, ON
                """

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ATTenuation:MODE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#ATTenuation_MODE>`_

                    Arguments: AUTO, LNOise, MANual
                    """
                    _cmd = "MODE"
                    args = ["AUTO", "LNOise", "MANual"]

                MODE = MODE()
                """
                `SOURce:POWer:ATTenuation:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#ATTenuation_MODE>`_

                Arguments: AUTO, LNOise, MANual
                """

            ATTenuation = ATTenuation()
            """
            `SOURce:POWer:ATTenuation
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#ATTenuation>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class COMBiner(SCPINode, SCPIBool):
                """
                SOURce:POWer:COMBiner

                Arguments: 1, OFF, ON
                """
                _cmd = "COMBiner"
                args = ["1", "OFF", "ON"]

            COMBiner = COMBiner()
            """
            SOURce:POWer:COMBiner

            Arguments: 1, OFF, ON
            """

            class CONVerter(SCPINode):
                """
                SOURce:POWer:CONVerter

                Arguments:
                """
                _cmd = "CONVerter"
                args = []

                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CONVerter:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#OFFSet>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "OFFSet"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                OFFSet = OFFSet()
                """
                `SOURce:POWer:CONVerter:OFFSet
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#OFFSet>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class TRANsfer(SCPINode):
                    """
                    SOURce:POWer:CONVerter:TRANsfer

                    Arguments:
                    """
                    _cmd = "TRANsfer"
                    args = []

                    class AMODel(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:AMODel
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_AMODel>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "AMODel"
                        args = ["1", "OFF", "ON"]

                    AMODel = AMODel()
                    """
                    `SOURce:POWer:CONVerter:TRANsfer:AMODel
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_AMODel>`_

                    Arguments: 1, OFF, ON
                    """

                    class ATTenuator(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:ATTenuator
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_ATTenuator>`_

                        Arguments: ELECtronic, MECHanical
                        """
                        _cmd = "ATTenuator"
                        args = ["ELECtronic", "MECHanical"]

                    ATTenuator = ATTenuator()
                    """
                    `SOURce:POWer:CONVerter:TRANsfer:ATTenuator
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_ATTenuator>`_

                    Arguments: ELECtronic, MECHanical
                    """

                    class DESCription(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:DESCription
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_DESCription>`_

                        Arguments: DSET, ELECtronic, LAPProx, NONE
                        """
                        _cmd = "DESCription"
                        args = ["DSET", "ELECtronic", "LAPProx", "NONE"]

                    DESCription = DESCription()
                    """
                    `SOURce:POWer:CONVerter:TRANsfer:DESCription
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_DESCription>`_

                    Arguments: DSET, ELECtronic, LAPProx, NONE
                    """

                    class DSET(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:DSET
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_DSET>`_

                        Arguments: FACTory, USER
                        """
                        _cmd = "DSET"
                        args = ["FACTory", "USER"]

                    DSET = DSET()
                    """
                    `SOURce:POWer:CONVerter:TRANsfer:DSET
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_DSET>`_

                    Arguments: FACTory, USER
                    """

                    class ELECtronic(SCPINode):
                        """
                        SOURce:POWer:CONVerter:TRANsfer:ELECtronic

                        Arguments:
                        """
                        _cmd = "ELECtronic"
                        args = []

                        class LIMit(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CONVerter:TRANsfer:ELECtronic:LIMit
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_ELECtronic_LIMit>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "LIMit"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        LIMit = LIMit()
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:ELECtronic:LIMit
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_ELECtronic_LIMit>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class MATTenuation(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CONVerter:TRANsfer:ELECtronic:MATTenuation
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_ELECtronic_MATTenuation>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "MATTenuation"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        MATTenuation = MATTenuation()
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:ELECtronic:MATTenuation
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_ELECtronic_MATTenuation>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class REDuction(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CONVerter:TRANsfer:ELECtronic:REDuction
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_ELECtronic_REDuction>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "REDuction"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        REDuction = REDuction()
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:ELECtronic:REDuction
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_ELECtronic_REDuction>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                    ELECtronic = ELECtronic()
                    """
                    SOURce:POWer:CONVerter:TRANsfer:ELECtronic

                    Arguments:
                    """

                    class MECHanical(SCPINode):
                        """
                        SOURce:POWer:CONVerter:TRANsfer:MECHanical

                        Arguments:
                        """
                        _cmd = "MECHanical"
                        args = []

                        class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CONVerter:TRANsfer:MECHanical:ATTenuation
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_MECHanical_ATTenuation>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "ATTenuation"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        ATTenuation = ATTenuation()
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:MECHanical:ATTenuation
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_MECHanical_ATTenuation>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                    MECHanical = MECHanical()
                    """
                    SOURce:POWer:CONVerter:TRANsfer:MECHanical

                    Arguments:
                    """

                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_OFFSet>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "OFFSet"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    OFFSet = OFFSet()
                    """
                    `SOURce:POWer:CONVerter:TRANsfer:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_OFFSet>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class PATH(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:PATH
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_PATH>`_

                        Arguments: 'string'
                        """
                        _cmd = "PATH"
                        args = ["'string'"]

                    PATH = PATH()
                    """
                    `SOURce:POWer:CONVerter:TRANsfer:PATH
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_PATH>`_

                    Arguments: 'string'
                    """

                    class SLOPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:SLOPe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_SLOPe>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "SLOPe"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    SLOPe = SLOPe()
                    """
                    `SOURce:POWer:CONVerter:TRANsfer:SLOPe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_power_converter.htm#TRANsfer_SLOPe>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                TRANsfer = TRANsfer()
                """
                SOURce:POWer:CONVerter:TRANsfer

                Arguments:
                """

            CONVerter = CONVerter()
            """
            SOURce:POWer:CONVerter

            Arguments:
            """

            class CORRection(SCPINode, SCPISet):
                """
                SOURce:POWer:CORRection

                Arguments: A1, A2, A3, A4, CONVerter, ESRC1, ESRC2, GENerator, PORT
                """
                _cmd = "CORRection"
                args = ["A1", "A2", "A3", "A4", "CONVerter", "ESRC1", "ESRC2", "GENerator", "PORT"]

                class ACQuire(SCPINode, SCPISet):
                    """
                    `SOURce:POWer:CORRection:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#ACQuire>`_

                    Arguments: A1, A2, A3, A4, CONVerter, ESRC1, ESRC2, GENerator, PORT
                    """
                    _cmd = "ACQuire"
                    args = ["A1", "A2", "A3", "A4", "CONVerter", "ESRC1", "ESRC2", "GENerator", "PORT"]

                    class VERification(SCPINode):
                        """
                        SOURce:POWer:CORRection:ACQuire:VERification

                        Arguments:
                        """
                        _cmd = "VERification"
                        args = []

                        class RESult(SCPINode, SCPIQuery):
                            """
                            `SOURce:POWer:CORRection:ACQuire:VERification:RESult
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#ACQuire_VERification_RESult>`_

                            Arguments:
                            """
                            _cmd = "RESult"
                            args = []

                        RESult = RESult()
                        """
                        `SOURce:POWer:CORRection:ACQuire:VERification:RESult
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#ACQuire_VERification_RESult>`_

                        Arguments:
                        """

                    VERification = VERification()
                    """
                    SOURce:POWer:CORRection:ACQuire:VERification

                    Arguments:
                    """

                ACQuire = ACQuire()
                """
                `SOURce:POWer:CORRection:ACQuire
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#ACQuire>`_

                Arguments: A1, A2, A3, A4, CONVerter, ESRC1, ESRC2, GENerator, PORT
                """

                class COLLect(SCPINode, SCPISet):
                    """
                    SOURce:POWer:CORRection:COLLect

                    Arguments: ASENsor, BSENsor
                    """
                    _cmd = "COLLect"
                    args = ["ASENsor", "BSENsor"]

                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire>`_

                        Arguments: ASENsor, BSENsor
                        """
                        _cmd = "ACQuire"
                        args = ["ASENsor", "BSENsor"]

                        class VERification(SCPINode, SCPIBool):
                            """
                            SOURce:POWer:CORRection:COLLect:ACQuire:VERification

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "VERification"
                            args = ["1", "OFF", "ON"]

                            class STATe(SCPINode, SCPIBool):
                                """
                                `SOURce:POWer:CORRection:COLLect:ACQuire:VERification:STATe
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire_VERification_STATe>`_

                                Arguments: 1, OFF, ON
                                """
                                _cmd = "STATe"
                                args = ["1", "OFF", "ON"]

                            STATe = STATe()
                            """
                            `SOURce:POWer:CORRection:COLLect:ACQuire:VERification:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire_VERification_STATe>`_

                            Arguments: 1, OFF, ON
                            """

                        VERification = VERification()
                        """
                        SOURce:POWer:CORRection:COLLect:ACQuire:VERification

                        Arguments: 1, OFF, ON
                        """

                    ACQuire = ACQuire()
                    """
                    `SOURce:POWer:CORRection:COLLect:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire>`_

                    Arguments: ASENsor, BSENsor
                    """

                    class AVERage(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CORRection:COLLect:AVERage

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "AVERage"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        class COUNt(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:COLLect:AVERage:COUNt
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_AVERage_COUNt>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "COUNt"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        COUNt = COUNt()
                        """
                        `SOURce:POWer:CORRection:COLLect:AVERage:COUNt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_AVERage_COUNt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                        class NTOLerance(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:COLLect:AVERage:NTOLerance
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_AVERage_NTOLerance>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "NTOLerance"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        NTOLerance = NTOLerance()
                        """
                        `SOURce:POWer:CORRection:COLLect:AVERage:NTOLerance
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_AVERage_NTOLerance>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                    AVERage = AVERage()
                    """
                    SOURce:POWer:CORRection:COLLect:AVERage

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class CFACtor(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:CFACtor
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_CFACtor>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "CFACtor"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    CFACtor = CFACtor()
                    """
                    `SOURce:POWer:CORRection:COLLect:CFACtor
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_CFACtor>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class FLATness(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CORRection:COLLect:FLATness
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire_VERification_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "FLATness"
                        args = ["1", "OFF", "ON"]

                    FLATness = FLATness()
                    """
                    `SOURce:POWer:CORRection:COLLect:FLATness
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire_VERification_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                    class METHod(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:METHod
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_METHod>`_

                        Arguments: PMONly, RRAFter, RRONly
                        """
                        _cmd = "METHod"
                        args = ["PMONly", "RRAFter", "RRONly"]

                    METHod = METHod()
                    """
                    `SOURce:POWer:CORRection:COLLect:METHod
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_METHod>`_

                    Arguments: PMONly, RRAFter, RRONly
                    """

                    class PMReadings(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:PMReadings
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_PMReadings>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PMReadings"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    PMReadings = PMReadings()
                    """
                    `SOURce:POWer:CORRection:COLLect:PMReadings
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_PMReadings>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class RRECeiver(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CORRection:COLLect:RRECeiver
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire_VERification_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "RRECeiver"
                        args = ["1", "OFF", "ON"]

                    RRECeiver = RRECeiver()
                    """
                    `SOURce:POWer:CORRection:COLLect:RRECeiver
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire_VERification_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                COLLect = COLLect()
                """
                SOURce:POWer:CORRection:COLLect

                Arguments: ASENsor, BSENsor
                """

                class CONVerter(SCPINodeN, SCPIBool):
                    """
                    SOURce:POWer:CORRection:CONVerter

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "CONVerter"
                    args = ["1", "OFF", "ON"]

                    class LEVel(SCPINode):
                        """
                        SOURce:POWer:CORRection:CONVerter:LEVel

                        Arguments:
                        """
                        _cmd = "LEVel"
                        args = []

                        class OFFSet(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:CONVerter:LEVel:OFFSet
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#CONVerter_LEVel_OFFset>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "OFFSet"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        OFFSet = OFFSet()
                        """
                        `SOURce:POWer:CORRection:CONVerter:LEVel:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#CONVerter_LEVel_OFFset>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                    LEVel = LEVel()
                    """
                    SOURce:POWer:CORRection:CONVerter:LEVel

                    Arguments:
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CORRection:CONVerter:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#CONVerter_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SOURce:POWer:CORRection:CONVerter:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#CONVerter_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                CONVerter = CONVerter()
                """
                SOURce:POWer:CORRection:CONVerter

                Arguments: 1, OFF, ON
                """

                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:DATA
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#DATA>`_

                    Arguments: 'string'
                    """
                    _cmd = "DATA"
                    args = ["'string'"]

                    class PARameter(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:DATA:PARameter
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#DATA_PARameter>`_

                        Arguments: ATTenuation, CFRequency, CPOWer, POINts, STARt, STOP, STYPe, TSTamp, WAVE
                        """
                        _cmd = "PARameter"
                        args = ["ATTenuation", "CFRequency", "CPOWer", "POINts", "STARt", "STOP", "STYPe", "TSTamp", "WAVE"]

                        class COUNt(SCPINode, SCPIQuery):
                            """
                            `SOURce:POWer:CORRection:DATA:PARameter:COUNt
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#DATA_PARameter_COUNt>`_

                            Arguments:
                            """
                            _cmd = "COUNt"
                            args = []

                        COUNt = COUNt()
                        """
                        `SOURce:POWer:CORRection:DATA:PARameter:COUNt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#DATA_PARameter_COUNt>`_

                        Arguments:
                        """

                    PARameter = PARameter()
                    """
                    `SOURce:POWer:CORRection:DATA:PARameter
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#DATA_PARameter>`_

                    Arguments: ATTenuation, CFRequency, CPOWer, POINts, STARt, STOP, STYPe, TSTamp, WAVE
                    """

                DATA = DATA()
                """
                `SOURce:POWer:CORRection:DATA
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#DATA>`_

                Arguments: 'string'
                """

                class DEFault(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:CORRection:DEFault
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#CORRection_DEFault>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "DEFault"
                    args = ["1", "OFF", "ON"]

                DEFault = DEFault()
                """
                `SOURce:POWer:CORRection:DEFault
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#CORRection_DEFault>`_

                Arguments: 1, OFF, ON
                """

                class FAST(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:CORRection:FAST
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#FAST>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "FAST"
                    args = ["1", "OFF", "ON"]

                FAST = FAST()
                """
                `SOURce:POWer:CORRection:FAST
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#FAST>`_

                Arguments: 1, OFF, ON
                """

                class GENerator(SCPINodeN, SCPIBool):
                    """
                    SOURce:POWer:CORRection:GENerator

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "GENerator"
                    args = ["1", "OFF", "ON"]

                    class LEVel(SCPINode):
                        """
                        SOURce:POWer:CORRection:GENerator:LEVel

                        Arguments:
                        """
                        _cmd = "LEVel"
                        args = []

                        class OFFSet(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:GENerator:LEVel:OFFSet
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#GENerator_LEVel_OFFset>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "OFFSet"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        OFFSet = OFFSet()
                        """
                        `SOURce:POWer:CORRection:GENerator:LEVel:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#GENerator_LEVel_OFFset>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                    LEVel = LEVel()
                    """
                    SOURce:POWer:CORRection:GENerator:LEVel

                    Arguments:
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CORRection:GENerator:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#GENerator_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SOURce:POWer:CORRection:GENerator:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#GENerator_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                GENerator = GENerator()
                """
                SOURce:POWer:CORRection:GENerator

                Arguments: 1, OFF, ON
                """

                class HARMonic(SCPINode, SCPISet):
                    """
                    SOURce:POWer:CORRection:HARMonic

                    Arguments:
                    """
                    _cmd = "HARMonic"
                    args = []

                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SOURce:POWer:CORRection:HARMonic:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#HARMonic_ACQuire>`_

                        Arguments:
                        """
                        _cmd = "ACQuire"
                        args = []

                    ACQuire = ACQuire()
                    """
                    `SOURce:POWer:CORRection:HARMonic:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#HARMonic_ACQuire>`_

                    Arguments:
                    """

                HARMonic = HARMonic()
                """
                SOURce:POWer:CORRection:HARMonic

                Arguments:
                """

                class IMODulation(SCPINode):
                    """
                    SOURce:POWer:CORRection:IMODulation

                    Arguments:
                    """
                    _cmd = "IMODulation"
                    args = []

                    class LTONe(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:IMODulation:LTONe

                        Arguments:
                        """
                        _cmd = "LTONe"
                        args = []

                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:IMODulation:LTONe:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#IMODulation_LOWer_ACQuire>`_

                            Arguments:
                            """
                            _cmd = "ACQuire"
                            args = []

                        ACQuire = ACQuire()
                        """
                        `SOURce:POWer:CORRection:IMODulation:LTONe:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#IMODulation_LOWer_ACQuire>`_

                        Arguments:
                        """

                    LTONe = LTONe()
                    """
                    SOURce:POWer:CORRection:IMODulation:LTONe

                    Arguments:
                    """

                    class RPORt(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:IMODulation:RPORt

                        Arguments:
                        """
                        _cmd = "RPORt"
                        args = []

                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:IMODulation:RPORt:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#IMODulation_RPORt_ACQuire>`_

                            Arguments:
                            """
                            _cmd = "ACQuire"
                            args = []

                        ACQuire = ACQuire()
                        """
                        `SOURce:POWer:CORRection:IMODulation:RPORt:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#IMODulation_RPORt_ACQuire>`_

                        Arguments:
                        """

                    RPORt = RPORt()
                    """
                    SOURce:POWer:CORRection:IMODulation:RPORt

                    Arguments:
                    """

                    class SPORts(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:IMODulation:SPORts

                        Arguments:
                        """
                        _cmd = "SPORts"
                        args = []

                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:IMODulation:SPORts:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#IMODulation_SPORts_ACQuire>`_

                            Arguments:
                            """
                            _cmd = "ACQuire"
                            args = []

                        ACQuire = ACQuire()
                        """
                        `SOURce:POWer:CORRection:IMODulation:SPORts:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#IMODulation_SPORts_ACQuire>`_

                        Arguments:
                        """

                    SPORts = SPORts()
                    """
                    SOURce:POWer:CORRection:IMODulation:SPORts

                    Arguments:
                    """

                    class UTONe(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:IMODulation:UTONe

                        Arguments:
                        """
                        _cmd = "UTONe"
                        args = []

                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:IMODulation:UTONe:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#IMODulation_UPPer_ACQuire>`_

                            Arguments:
                            """
                            _cmd = "ACQuire"
                            args = []

                        ACQuire = ACQuire()
                        """
                        `SOURce:POWer:CORRection:IMODulation:UTONe:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#IMODulation_UPPer_ACQuire>`_

                        Arguments:
                        """

                    UTONe = UTONe()
                    """
                    SOURce:POWer:CORRection:IMODulation:UTONe

                    Arguments:
                    """

                IMODulation = IMODulation()
                """
                SOURce:POWer:CORRection:IMODulation

                Arguments:
                """

                class LEVel(SCPINode):
                    """
                    SOURce:POWer:CORRection:LEVel

                    Arguments:
                    """
                    _cmd = "LEVel"
                    args = []

                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:LEVel:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#LEVel_OFFset>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "OFFSet"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    OFFSet = OFFSet()
                    """
                    `SOURce:POWer:CORRection:LEVel:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#LEVel_OFFset>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                LEVel = LEVel()
                """
                SOURce:POWer:CORRection:LEVel

                Arguments:
                """

                class MIXer(SCPINode):
                    """
                    SOURce:POWer:CORRection:MIXer

                    Arguments:
                    """
                    _cmd = "MIXer"
                    args = []

                    class IF(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:MIXer:IF

                        Arguments:
                        """
                        _cmd = "IF"
                        args = []

                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:MIXer:IF:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#MIXer_IF_ACQuire>`_

                            Arguments:
                            """
                            _cmd = "ACQuire"
                            args = []

                        ACQuire = ACQuire()
                        """
                        `SOURce:POWer:CORRection:MIXer:IF:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#MIXer_IF_ACQuire>`_

                        Arguments:
                        """

                    IF = IF()
                    """
                    SOURce:POWer:CORRection:MIXer:IF

                    Arguments:
                    """

                    class LO(SCPINodeN, SCPISet):
                        """
                        SOURce:POWer:CORRection:MIXer:LO

                        Arguments:
                        """
                        _cmd = "LO"
                        args = []

                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:MIXer:LO:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#MIXer_LO_ACQuire>`_

                            Arguments:
                            """
                            _cmd = "ACQuire"
                            args = []

                        ACQuire = ACQuire()
                        """
                        `SOURce:POWer:CORRection:MIXer:LO:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#MIXer_LO_ACQuire>`_

                        Arguments:
                        """

                    LO = LO()
                    """
                    SOURce:POWer:CORRection:MIXer:LO

                    Arguments:
                    """

                    class RF(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:MIXer:RF

                        Arguments:
                        """
                        _cmd = "RF"
                        args = []

                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:MIXer:RF:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#MIXer_RF_ACQuire>`_

                            Arguments:
                            """
                            _cmd = "ACQuire"
                            args = []

                        ACQuire = ACQuire()
                        """
                        `SOURce:POWer:CORRection:MIXer:RF:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#MIXer_RF_ACQuire>`_

                        Arguments:
                        """

                        class NFIGure(SCPINode, SCPISet):
                            """
                            SOURce:POWer:CORRection:MIXer:RF:NFIGure

                            Arguments:
                            """
                            _cmd = "NFIGure"
                            args = []

                            class ACQuire(SCPINode, SCPISet):
                                """
                                `SOURce:POWer:CORRection:MIXer:RF:NFIGure:ACQuire
                                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#MIXer_RF_NFIGure_ACQuire>`_

                                Arguments:
                                """
                                _cmd = "ACQuire"
                                args = []

                            ACQuire = ACQuire()
                            """
                            `SOURce:POWer:CORRection:MIXer:RF:NFIGure:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#MIXer_RF_NFIGure_ACQuire>`_

                            Arguments:
                            """

                        NFIGure = NFIGure()
                        """
                        SOURce:POWer:CORRection:MIXer:RF:NFIGure

                        Arguments:
                        """

                    RF = RF()
                    """
                    SOURce:POWer:CORRection:MIXer:RF

                    Arguments:
                    """

                MIXer = MIXer()
                """
                SOURce:POWer:CORRection:MIXer

                Arguments:
                """

                class NREadings(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:NREadings
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#NREadings>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "NREadings"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                NREadings = NREadings()
                """
                `SOURce:POWer:CORRection:NREadings
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#NREadings>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class OSOurces(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:CORRection:OSOurces

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "OSOurces"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CORRection:OSOurces:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#OSOurces_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SOURce:POWer:CORRection:OSOurces:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#OSOurces_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                OSOurces = OSOurces()
                """
                SOURce:POWer:CORRection:OSOurces

                Arguments: 1, OFF, ON
                """

                class PMETer(SCPINode):
                    """
                    SOURce:POWer:CORRection:PMETer

                    Arguments:
                    """
                    _cmd = "PMETer"
                    args = []

                    class ID(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:PMETer:ID
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#PMETer_ID>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "ID"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    ID = ID()
                    """
                    `SOURce:POWer:CORRection:PMETer:ID
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#PMETer_ID>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                PMETer = PMETer()
                """
                SOURce:POWer:CORRection:PMETer

                Arguments:
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:CORRection:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SOURce:POWer:CORRection:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction.htm#STATe>`_

                Arguments: 1, OFF, ON
                """

                class TCOefficient(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:CORRection:TCOefficient

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "TCOefficient"
                    args = ["1", "OFF", "ON"]

                    class CALibration(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:CALibration
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#CALibration>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "CALibration"
                        args = ["1", "OFF", "ON"]

                    CALibration = CALibration()
                    """
                    `SOURce:POWer:CORRection:TCOefficient:CALibration
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#CALibration>`_

                    Arguments: 1, OFF, ON
                    """

                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:COUNt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#COUNt>`_

                        Arguments:
                        """
                        _cmd = "COUNt"
                        args = []

                    COUNt = COUNt()
                    """
                    `SOURce:POWer:CORRection:TCOefficient:COUNt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#COUNt>`_

                    Arguments:
                    """

                    class DEFine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:DEFine
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#DEFine>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "DEFine"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    DEFine = DEFine()
                    """
                    `SOURce:POWer:CORRection:TCOefficient:DEFine
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#DEFine>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class DELete(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CORRection:TCOefficient:DELete

                        Arguments:
                        """
                        _cmd = "DELete"
                        args = []

                        class ALL(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:TCOefficient:DELete:ALL
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#DELete_ALL>`_

                            Arguments:
                            """
                            _cmd = "ALL"
                            args = []

                        ALL = ALL()
                        """
                        `SOURce:POWer:CORRection:TCOefficient:DELete:ALL
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#DELete_ALL>`_

                        Arguments:
                        """

                        class DUMMy(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:TCOefficient:DELete:DUMMy
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#DELete>`_

                            Arguments:
                            """
                            _cmd = "DUMMy"
                            args = []

                        DUMMy = DUMMy()
                        """
                        `SOURce:POWer:CORRection:TCOefficient:DELete:DUMMy
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#DELete>`_

                        Arguments:
                        """

                    DELete = DELete()
                    """
                    SOURce:POWer:CORRection:TCOefficient:DELete

                    Arguments:
                    """

                    class FEED(SCPINode, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:FEED
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#FEED>`_

                        Arguments: 'string'
                        """
                        _cmd = "FEED"
                        args = ["'string'"]

                    FEED = FEED()
                    """
                    `SOURce:POWer:CORRection:TCOefficient:FEED
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#FEED>`_

                    Arguments: 'string'
                    """

                    class INSert(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:INSert
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#INSert>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "INSert"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    INSert = INSert()
                    """
                    `SOURce:POWer:CORRection:TCOefficient:INSert
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#INSert>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SOURce:POWer:CORRection:TCOefficient:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#STATe>`_

                    Arguments: 1, OFF, ON
                    """

                TCOefficient = TCOefficient()
                """
                SOURce:POWer:CORRection:TCOefficient

                Arguments: 1, OFF, ON
                """

            CORRection = CORRection()
            """
            SOURce:POWer:CORRection

            Arguments: A1, A2, A3, A4, CONVerter, ESRC1, ESRC2, GENerator, PORT
            """

            class COUPle(SCPINode, SCPIBool):
                """
                SOURce:POWer:COUPle

                Arguments: 1, OFF, ON
                """
                _cmd = "COUPle"
                args = ["1", "OFF", "ON"]

            COUPle = COUPle()
            """
            SOURce:POWer:COUPle

            Arguments: 1, OFF, ON
            """

            class GENerator(SCPINodeN):
                """
                SOURce:POWer:GENerator

                Arguments:
                """
                _cmd = "GENerator"
                args = []

                class LLIMit(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:GENerator:LLIMit

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "LLIMit"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:GENerator:LLIMit:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#GENerator_LLIMit_Enable>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SOURce:POWer:GENerator:LLIMit:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#GENerator_LLIMit_Enable>`_

                    Arguments: 1, OFF, ON
                    """

                    class VALue(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:GENerator:LLIMit:VALue
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#GENerator_LLIMit_VALue>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "VALue"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    VALue = VALue()
                    """
                    `SOURce:POWer:GENerator:LLIMit:VALue
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#GENerator_LLIMit_VALue>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                LLIMit = LLIMit()
                """
                SOURce:POWer:GENerator:LLIMit

                Arguments: 1, OFF, ON
                """

                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:GENerator:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_GENerator_OFFSet>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "OFFSet"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                OFFSet = OFFSet()
                """
                `SOURce:POWer:GENerator:OFFSet
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_GENerator_OFFSet>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class PERManent(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:GENerator:PERManent

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "PERManent"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:GENerator:PERManent:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_GENerator_PERManent_STATe>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SOURce:POWer:GENerator:PERManent:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_GENerator_PERManent_STATe>`_

                    Arguments: 1, OFF, ON
                    """

                PERManent = PERManent()
                """
                SOURce:POWer:GENerator:PERManent

                Arguments: 1, OFF, ON
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:GENerator:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_GENerator_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SOURce:POWer:GENerator:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_GENerator_STATe>`_

                Arguments: 1, OFF, ON
                """

            GENerator = GENerator()
            """
            SOURce:POWer:GENerator

            Arguments:
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:LEVel

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "LEVel"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class IMMediate(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:LEVel:IMMediate

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "IMMediate"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:AMPLitude
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_LEVel>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "AMPLitude"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    AMPLitude = AMPLitude()
                    """
                    `SOURce:POWer:LEVel:IMMediate:AMPLitude
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_LEVel>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class LLIMit(SCPINode, SCPIBool):
                        """
                        SOURce:POWer:LEVel:IMMediate:LLIMit

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "LLIMit"
                        args = ["1", "OFF", "ON"]

                        class DGRaccess(SCPINode, SCPIBool):
                            """
                            `SOURce:POWer:LEVel:IMMediate:LLIMit:DGRaccess
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_LLIMit_DGRaccess>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "DGRaccess"
                            args = ["1", "OFF", "ON"]

                        DGRaccess = DGRaccess()
                        """
                        `SOURce:POWer:LEVel:IMMediate:LLIMit:DGRaccess
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_LLIMit_DGRaccess>`_

                        Arguments: 1, OFF, ON
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            `SOURce:POWer:LEVel:IMMediate:LLIMit:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_LLIMit_Enable>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `SOURce:POWer:LEVel:IMMediate:LLIMit:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_LLIMit_Enable>`_

                        Arguments: 1, OFF, ON
                        """

                        class VALue(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:LEVel:IMMediate:LLIMit:VALue
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_LLIMit_VALue>`_

                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "VALue"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        VALue = VALue()
                        """
                        `SOURce:POWer:LEVel:IMMediate:LLIMit:VALue
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_LLIMit_VALue>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """

                    LLIMit = LLIMit()
                    """
                    SOURce:POWer:LEVel:IMMediate:LLIMit

                    Arguments: 1, OFF, ON
                    """

                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_OFFSet>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "OFFSet"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    OFFSet = OFFSet()
                    """
                    `SOURce:POWer:LEVel:IMMediate:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_OFFSet>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class PHASe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:PHASe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_PHASe>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PHASe"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    PHASe = PHASe()
                    """
                    `SOURce:POWer:LEVel:IMMediate:PHASe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_PHASe>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class SLOPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:SLOPe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_SLOPe>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "SLOPe"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                        class STATe(SCPINode, SCPIBool):
                            """
                            SOURce:POWer:LEVel:IMMediate:SLOPe:STATe

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        SOURce:POWer:LEVel:IMMediate:SLOPe:STATe

                        Arguments: 1, OFF, ON
                        """

                    SLOPe = SLOPe()
                    """
                    `SOURce:POWer:LEVel:IMMediate:SLOPe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_SLOPe>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                IMMediate = IMMediate()
                """
                SOURce:POWer:LEVel:IMMediate

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            LEVel = LEVel()
            """
            SOURce:POWer:LEVel

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class PERManent(SCPINode, SCPIBool):
                """
                SOURce:POWer:PERManent

                Arguments: 1, OFF, ON
                """
                _cmd = "PERManent"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:PERManent:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_PERManent_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SOURce:POWer:PERManent:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_PERManent_STATe>`_

                Arguments: 1, OFF, ON
                """

            PERManent = PERManent()
            """
            SOURce:POWer:PERManent

            Arguments: 1, OFF, ON
            """

            class REDuce(SCPINode, SCPIBool):
                """
                `SOURce:POWer:REDuce
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_REDuce>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "REDuce"
                args = ["1", "OFF", "ON"]

            REDuce = REDuce()
            """
            `SOURce:POWer:REDuce
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_REDuce>`_

            Arguments: 1, OFF, ON
            """

            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:STARt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_STARt>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "STARt"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            STARt = STARt()
            """
            `SOURce:POWer:STARt
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_STARt>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SOURce:POWer:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `SOURce:POWer:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_STATe>`_

            Arguments: 1, OFF, ON
            """

            class STOP(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:STOP
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_STOP>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "STOP"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            STOP = STOP()
            """
            `SOURce:POWer:STOP
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__power__level_.htm#POWer_STOP>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        POWer = POWer()
        """
        SOURce:POWer

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class TDIF(SCPINode, SCPIBool):
            """
            SOURce:TDIF

            Arguments: 1, OFF, ON
            """
            _cmd = "TDIF"
            args = ["1", "OFF", "ON"]

            class CRFRequency(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:TDIF:CRFRequency
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#CRFRequency>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CRFRequency"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            CRFRequency = CRFRequency()
            """
            `SOURce:TDIF:CRFRequency
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#CRFRequency>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class IMBalance(SCPINode):
                """
                SOURce:TDIF:IMBalance

                Arguments:
                """
                _cmd = "IMBalance"
                args = []

                class AMPLitude(SCPINode):
                    """
                    SOURce:TDIF:IMBalance:AMPLitude

                    Arguments:
                    """
                    _cmd = "AMPLitude"
                    args = []

                    class LPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:AMPLitude:LPORt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_AMPlitude_LPORt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "LPORt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    LPORt = LPORt()
                    """
                    `SOURce:TDIF:IMBalance:AMPLitude:LPORt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_AMPlitude_LPORt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:AMPLitude:STARt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_AMPlitude_STARt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STARt = STARt()
                    """
                    `SOURce:TDIF:IMBalance:AMPLitude:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_AMPlitude_STARt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:AMPLitude:STOP
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_AMPlitude_STOP>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STOP = STOP()
                    """
                    `SOURce:TDIF:IMBalance:AMPLitude:STOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_AMPlitude_STOP>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                AMPLitude = AMPLitude()
                """
                SOURce:TDIF:IMBalance:AMPLitude

                Arguments:
                """

                class PHASe(SCPINode):
                    """
                    SOURce:TDIF:IMBalance:PHASe

                    Arguments:
                    """
                    _cmd = "PHASe"
                    args = []

                    class LPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:PHASe:LPORt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_PHASe_LPORt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "LPORt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    LPORt = LPORt()
                    """
                    `SOURce:TDIF:IMBalance:PHASe:LPORt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_PHASe_LPORt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:PHASe:STARt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_PHASe_STARt>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STARt = STARt()
                    """
                    `SOURce:TDIF:IMBalance:PHASe:STARt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_PHASe_STARt>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:PHASe:STOP
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_PHASe_STOP>`_

                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                    STOP = STOP()
                    """
                    `SOURce:TDIF:IMBalance:PHASe:STOP
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#IMBalance_PHASe_STOP>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """

                PHASe = PHASe()
                """
                SOURce:TDIF:IMBalance:PHASe

                Arguments:
                """

            IMBalance = IMBalance()
            """
            SOURce:TDIF:IMBalance

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SOURce:TDIF:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#TDIF_STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `SOURce:TDIF:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#TDIF_STATe>`_

            Arguments: 1, OFF, ON
            """

            class TOLerance(SCPINode):
                """
                SOURce:TDIF:TOLerance

                Arguments:
                """
                _cmd = "TOLerance"
                args = []

                class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:TDIF:TOLerance:AMPLitude

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "AMPLitude"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                AMPLitude = AMPLitude()
                """
                SOURce:TDIF:TOLerance:AMPLitude

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class PHASe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:TDIF:TOLerance:PHASe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#TOLerance_PHASe>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "PHASe"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                PHASe = PHASe()
                """
                `SOURce:TDIF:TOLerance:PHASe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#TOLerance_PHASe>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            TOLerance = TOLerance()
            """
            SOURce:TDIF:TOLerance

            Arguments:
            """

            class WAVes(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:TDIF:WAVes
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#TDIF_WAVes>`_

                Arguments: DCMode, SENDed
                """
                _cmd = "WAVes"
                args = ["DCMode", "SENDed"]

            WAVes = WAVes()
            """
            `SOURce:TDIF:WAVes
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/source/source_ch__tdif.htm#TDIF_WAVes>`_

            Arguments: DCMode, SENDed
            """

        TDIF = TDIF()
        """
        SOURce:TDIF

        Arguments: 1, OFF, ON
        """

    SOURce = SOURce()
    """
    SOURce

    Arguments:
    """

    class STATus(SCPINode):
        """
        `STATus
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/remote_control/status_reporting_system/status_registers.htm#IX_Operation_Register>`_

        Arguments:
        """
        _cmd = "STATus"
        args = []

        class OPERation(SCPINode, SCPIQuery, SCPISet):
            """
            STATus:OPERation

            Arguments:
            """
            _cmd = "OPERation"
            args = []

            class CONDition(SCPINode, SCPIQuery):
                """
                STATus:OPERation:CONDition

                Arguments:
                """
                _cmd = "CONDition"
                args = []

            CONDition = CONDition()
            """
            STATus:OPERation:CONDition

            Arguments:
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:ENABle

                Arguments: 1
                """
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()
            """
            STATus:OPERation:ENABle

            Arguments: 1
            """

            class EVENt(SCPINode, SCPIQuery):
                """
                STATus:OPERation:EVENt

                Arguments:
                """
                _cmd = "EVENt"
                args = []

            EVENt = EVENt()
            """
            STATus:OPERation:EVENt

            Arguments:
            """

            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:NTRansition

                Arguments: 1
                """
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()
            """
            STATus:OPERation:NTRansition

            Arguments: 1
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:PTRansition

                Arguments: 1
                """
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()
            """
            STATus:OPERation:PTRansition

            Arguments: 1
            """

        OPERation = OPERation()
        """
        STATus:OPERation

        Arguments:
        """

        class PRESet(SCPINode, SCPISet):
            """
            `STATus:PRESet
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#PRESet>`_

            Arguments:
            """
            _cmd = "PRESet"
            args = []

        PRESet = PRESet()
        """
        `STATus:PRESet
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#PRESet>`_

        Arguments:
        """

        class QUEStionable(SCPINode, SCPIQuery, SCPISet):
            """
            STATus:QUEStionable

            Arguments:
            """
            _cmd = "QUEStionable"
            args = []

            class CONDition(SCPINode, SCPIQuery):
                """
                `STATus:QUEStionable:CONDition
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#QUES_CONDition>`_

                Arguments:
                """
                _cmd = "CONDition"
                args = []

            CONDition = CONDition()
            """
            `STATus:QUEStionable:CONDition
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#QUES_CONDition>`_

            Arguments:
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:ENABle
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#QUES_ENABle>`_

                Arguments: 1
                """
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()
            """
            `STATus:QUEStionable:ENABle
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#QUES_ENABle>`_

            Arguments: 1
            """

            class EVENt(SCPINode, SCPIQuery):
                """
                `STATus:QUEStionable:EVENt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#LIMit_EVENt>`_

                Arguments:
                """
                _cmd = "EVENt"
                args = []

            EVENt = EVENt()
            """
            `STATus:QUEStionable:EVENt
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#LIMit_EVENt>`_

            Arguments:
            """

            class INTegrity(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:INTegrity

                Arguments:
                """
                _cmd = "INTegrity"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    `STATus:QUEStionable:INTegrity:CONDition
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_CONDition>`_

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                `STATus:QUEStionable:INTegrity:CONDition
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_CONDition>`_

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:ENABle
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_ENABle>`_

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                `STATus:QUEStionable:INTegrity:ENABle
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_ENABle>`_

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    `STATus:QUEStionable:INTegrity:EVENt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_EVENt>`_

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                `STATus:QUEStionable:INTegrity:EVENt
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_EVENt>`_

                Arguments:
                """

                class HARDware(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:INTegrity:HARDware

                    Arguments:
                    """
                    _cmd = "HARDware"
                    args = []

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:CONDition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_HARDware_CONDition>`_

                        Arguments:
                        """
                        _cmd = "CONDition"
                        args = []

                    CONDition = CONDition()
                    """
                    `STATus:QUEStionable:INTegrity:HARDware:CONDition
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_HARDware_CONDition>`_

                    Arguments:
                    """

                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:ENABle
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_HARDware_ENABle>`_

                        Arguments: 1
                        """
                        _cmd = "ENABle"
                        args = ["1"]

                    ENABle = ENABle()
                    """
                    `STATus:QUEStionable:INTegrity:HARDware:ENABle
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_HARDware_ENABle>`_

                    Arguments: 1
                    """

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:EVENt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_HARDware_EVENt>`_

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    `STATus:QUEStionable:INTegrity:HARDware:EVENt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_HARDware_EVENt>`_

                    Arguments:
                    """

                    class NTRansition(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:NTRansition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_HARDware_NTRansition>`_

                        Arguments: 1
                        """
                        _cmd = "NTRansition"
                        args = ["1"]

                    NTRansition = NTRansition()
                    """
                    `STATus:QUEStionable:INTegrity:HARDware:NTRansition
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_HARDware_NTRansition>`_

                    Arguments: 1
                    """

                    class PTRansition(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:PTRansition
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_HARDware_PTRansition>`_

                        Arguments: 1
                        """
                        _cmd = "PTRansition"
                        args = ["1"]

                    PTRansition = PTRansition()
                    """
                    `STATus:QUEStionable:INTegrity:HARDware:PTRansition
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_HARDware_PTRansition>`_

                    Arguments: 1
                    """

                HARDware = HARDware()
                """
                STATus:QUEStionable:INTegrity:HARDware

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:NTRansition
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_NTRansition>`_

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                `STATus:QUEStionable:INTegrity:NTRansition
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_NTRansition>`_

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:PTRansition
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_PTRansition>`_

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                `STATus:QUEStionable:INTegrity:PTRansition
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#INTegrity_PTRansition>`_

                Arguments: 1
                """

            INTegrity = INTegrity()
            """
            STATus:QUEStionable:INTegrity

            Arguments:
            """

            class LIMit(SCPINodeN, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:LIMit

                Arguments:
                """
                _cmd = "LIMit"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:LIMit:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:QUEStionable:LIMit:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:LIMit:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:QUEStionable:LIMit:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:LIMit:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:QUEStionable:LIMit:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:LIMit:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:QUEStionable:LIMit:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:LIMit:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:QUEStionable:LIMit:PTRansition

                Arguments: 1
                """

            LIMit = LIMit()
            """
            STATus:QUEStionable:LIMit

            Arguments:
            """

            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:NTRansition
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#QUES_NTRansition>`_

                Arguments: 1
                """
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()
            """
            `STATus:QUEStionable:NTRansition
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#QUES_NTRansition>`_

            Arguments: 1
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:PTRansition
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#QUES_PTRansition>`_

                Arguments: 1
                """
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()
            """
            `STATus:QUEStionable:PTRansition
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#QUES_PTRansition>`_

            Arguments: 1
            """

        QUEStionable = QUEStionable()
        """
        STATus:QUEStionable

        Arguments:
        """

        class QUEue(SCPINode, SCPIQuery, SCPISet):
            """
            STATus:QUEue

            Arguments:
            """
            _cmd = "QUEue"
            args = []

            class NEXT(SCPINode, SCPIQuery):
                """
                `STATus:QUEue:NEXT
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#QUEue>`_

                Arguments:
                """
                _cmd = "NEXT"
                args = []

            NEXT = NEXT()
            """
            `STATus:QUEue:NEXT
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/status/status.htm#QUEue>`_

            Arguments:
            """

        QUEue = QUEue()
        """
        STATus:QUEue

        Arguments:
        """

    STATus = STATus()
    """
    `STATus
    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/remote_control/status_reporting_system/status_registers.htm#IX_Operation_Register>`_

    Arguments:
    """

    class SYSTem(SCPINode):
        """
        SYSTem

        Arguments:
        """
        _cmd = "SYSTem"
        args = []

        class COMMunicate(SCPINode):
            """
            SYSTem:COMMunicate

            Arguments:
            """
            _cmd = "COMMunicate"
            args = []

            class AKAL(SCPINode):
                """
                SYSTem:COMMunicate:AKAL

                Arguments:
                """
                _cmd = "AKAL"
                args = []

                class CONNection(SCPINode, SCPISet):
                    """
                    `SYSTem:COMMunicate:AKAL:CONNection
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#AKAL_CONNection>`_

                    Arguments: MATCh, OPEN, SHORt, THRough
                    """
                    _cmd = "CONNection"
                    args = ["MATCh", "OPEN", "SHORt", "THRough"]

                CONNection = CONNection()
                """
                `SYSTem:COMMunicate:AKAL:CONNection
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#AKAL_CONNection>`_

                Arguments: MATCh, OPEN, SHORt, THRough
                """

                class MMEMory(SCPINode, SCPIBool):
                    """
                    SYSTem:COMMunicate:AKAL:MMEMory

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "MMEMory"
                    args = ["1", "OFF", "ON"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SYSTem:COMMunicate:AKAL:MMEMory:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#AKAL_MMEMory__STATe_>`_

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]

                    STATe = STATe()
                    """
                    `SYSTem:COMMunicate:AKAL:MMEMory:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#AKAL_MMEMory__STATe_>`_

                    Arguments: 1, OFF, ON
                    """

                MMEMory = MMEMory()
                """
                SYSTem:COMMunicate:AKAL:MMEMory

                Arguments: 1, OFF, ON
                """

            AKAL = AKAL()
            """
            SYSTem:COMMunicate:AKAL

            Arguments:
            """

            class GPIB(SCPINode):
                """
                SYSTem:COMMunicate:GPIB

                Arguments:
                """
                _cmd = "GPIB"
                args = []

                class SELF(SCPINode):
                    """
                    SYSTem:COMMunicate:GPIB:SELF

                    Arguments:
                    """
                    _cmd = "SELF"
                    args = []

                    class ADDRess(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:GPIB:SELF:ADDRess
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#ADDRess>`_

                        Arguments: 1
                        """
                        _cmd = "ADDRess"
                        args = ["1"]

                    ADDRess = ADDRess()
                    """
                    `SYSTem:COMMunicate:GPIB:SELF:ADDRess
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#ADDRess>`_

                    Arguments: 1
                    """

                    class RTERminator(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:GPIB:SELF:RTERminator
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RTERminator>`_

                        Arguments: EOI, LFEOi
                        """
                        _cmd = "RTERminator"
                        args = ["EOI", "LFEOi"]

                    RTERminator = RTERminator()
                    """
                    `SYSTem:COMMunicate:GPIB:SELF:RTERminator
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RTERminator>`_

                    Arguments: EOI, LFEOi
                    """

                SELF = SELF()
                """
                SYSTem:COMMunicate:GPIB:SELF

                Arguments:
                """

            GPIB = GPIB()
            """
            SYSTem:COMMunicate:GPIB

            Arguments:
            """

            class INTernal(SCPINode):
                """
                SYSTem:COMMunicate:INTernal

                Arguments:
                """
                _cmd = "INTernal"
                args = []

                class COMMand(SCPINode):
                    """
                    SYSTem:COMMunicate:INTernal:COMMand

                    Arguments:
                    """
                    _cmd = "COMMand"
                    args = []

                    class TABLes(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:INTernal:COMMand:TABLes

                        Arguments: 'string'
                        """
                        _cmd = "TABLes"
                        args = ["'string'"]

                    TABLes = TABLes()
                    """
                    SYSTem:COMMunicate:INTernal:COMMand:TABLes

                    Arguments: 'string'
                    """

                COMMand = COMMand()
                """
                SYSTem:COMMunicate:INTernal:COMMand

                Arguments:
                """

                class REMote(SCPINode, SCPIBool):
                    """
                    SYSTem:COMMunicate:INTernal:REMote

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "REMote"
                    args = ["1", "OFF", "ON"]

                REMote = REMote()
                """
                SYSTem:COMMunicate:INTernal:REMote

                Arguments: 1, OFF, ON
                """

            INTernal = INTernal()
            """
            SYSTem:COMMunicate:INTernal

            Arguments:
            """

            class NET(SCPINode):
                """
                SYSTem:COMMunicate:NET

                Arguments:
                """
                _cmd = "NET"
                args = []

                class HOSTname(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:COMMunicate:NET:HOSTname
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#NET_HOSTNAME>`_

                    Arguments: 'string'
                    """
                    _cmd = "HOSTname"
                    args = ["'string'"]

                HOSTname = HOSTname()
                """
                `SYSTem:COMMunicate:NET:HOSTname
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#NET_HOSTNAME>`_

                Arguments: 'string'
                """

            NET = NET()
            """
            SYSTem:COMMunicate:NET

            Arguments:
            """

            class RDEVice(SCPINode):
                """
                SYSTem:COMMunicate:RDEVice

                Arguments:
                """
                _cmd = "RDEVice"
                args = []

                class AKAL(SCPINode):
                    """
                    SYSTem:COMMunicate:RDEVice:AKAL

                    Arguments:
                    """
                    _cmd = "AKAL"
                    args = []

                    class ADDRess(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:ADDRess
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_AKAL_ADDRess>`_

                        Arguments: 'string'
                        """
                        _cmd = "ADDRess"
                        args = ["'string'"]

                        class ALL(SCPINode, SCPIQuery):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:ADDRess:ALL
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_AKAL_ADDRess_ALL>`_

                            Arguments:
                            """
                            _cmd = "ALL"
                            args = []

                        ALL = ALL()
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:ADDRess:ALL
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_AKAL_ADDRess_ALL>`_

                        Arguments:
                        """

                    ADDRess = ADDRess()
                    """
                    `SYSTem:COMMunicate:RDEVice:AKAL:ADDRess
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_AKAL_ADDRess>`_

                    Arguments: 'string'
                    """

                    class PREDuction(SCPINode, SCPIBool):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:PREDuction

                        Arguments: 1, OFF, ON
                        """
                        _cmd = "PREDuction"
                        args = ["1", "OFF", "ON"]

                        class STATe(SCPINode, SCPIBool):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:PREDuction:STATe
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#AKAL_PREDuction__STATe>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]

                        STATe = STATe()
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:PREDuction:STATe
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#AKAL_PREDuction__STATe>`_

                        Arguments: 1, OFF, ON
                        """

                    PREDuction = PREDuction()
                    """
                    SYSTem:COMMunicate:RDEVice:AKAL:PREDuction

                    Arguments: 1, OFF, ON
                    """

                AKAL = AKAL()
                """
                SYSTem:COMMunicate:RDEVice:AKAL

                Arguments:
                """

                class EUNit(SCPINode):
                    """
                    SYSTem:COMMunicate:RDEVice:EUNit

                    Arguments:
                    """
                    _cmd = "EUNit"
                    args = []

                    class IDN(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:EUNit:IDN
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_EUNit_IDN>`_

                        Arguments:
                        """
                        _cmd = "IDN"
                        args = []

                    IDN = IDN()
                    """
                    `SYSTem:COMMunicate:RDEVice:EUNit:IDN
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_EUNit_IDN>`_

                    Arguments:
                    """

                    class OPT(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:EUNit:OPT
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_EUNit_OPT>`_

                        Arguments:
                        """
                        _cmd = "OPT"
                        args = []

                    OPT = OPT()
                    """
                    `SYSTem:COMMunicate:RDEVice:EUNit:OPT
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_EUNit_OPT>`_

                    Arguments:
                    """

                EUNit = EUNit()
                """
                SYSTem:COMMunicate:RDEVice:EUNit

                Arguments:
                """

                class GENerator(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:GENerator

                    Arguments:
                    """
                    _cmd = "GENerator"
                    args = []

                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:CATalog
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_GENerator_CATalog>`_

                        Arguments:
                        """
                        _cmd = "CATalog"
                        args = []

                    CATalog = CATalog()
                    """
                    `SYSTem:COMMunicate:RDEVice:GENerator:CATalog
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_GENerator_CATalog>`_

                    Arguments:
                    """

                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:COUNt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_GENerator_COUNt>`_

                        Arguments:
                        """
                        _cmd = "COUNt"
                        args = []

                    COUNt = COUNt()
                    """
                    `SYSTem:COMMunicate:RDEVice:GENerator:COUNt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_GENerator_COUNt>`_

                    Arguments:
                    """

                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:DEFine
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_GENerator_DEFine>`_

                        Arguments: 'string'
                        """
                        _cmd = "DEFine"
                        args = ["'string'"]

                    DEFine = DEFine()
                    """
                    `SYSTem:COMMunicate:RDEVice:GENerator:DEFine
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_GENerator_DEFine>`_

                    Arguments: 'string'
                    """

                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:DELete
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_GENerator_DELete>`_

                        Arguments:
                        """
                        _cmd = "DELete"
                        args = []

                    DELete = DELete()
                    """
                    `SYSTem:COMMunicate:RDEVice:GENerator:DELete
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_GENerator_DELete>`_

                    Arguments:
                    """

                GENerator = GENerator()
                """
                SYSTem:COMMunicate:RDEVice:GENerator

                Arguments:
                """

                class PMETer(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:PMETer

                    Arguments:
                    """
                    _cmd = "PMETer"
                    args = []

                    class AZERo(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:AZERo
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_AZERo>`_

                        Arguments:
                        """
                        _cmd = "AZERo"
                        args = []

                    AZERo = AZERo()
                    """
                    `SYSTem:COMMunicate:RDEVice:PMETer:AZERo
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_AZERo>`_

                    Arguments:
                    """

                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:CATalog
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_CATalog>`_

                        Arguments:
                        """
                        _cmd = "CATalog"
                        args = []

                    CATalog = CATalog()
                    """
                    `SYSTem:COMMunicate:RDEVice:PMETer:CATalog
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_CATalog>`_

                    Arguments:
                    """

                    class CONFigure(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:PMETer:CONFigure

                        Arguments:
                        """
                        _cmd = "CONFigure"
                        args = []

                        class AUTO(SCPINode, SCPIBool):
                            """
                            `SYSTem:COMMunicate:RDEVice:PMETer:CONFigure:AUTO
                            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_CONFigure_AUTO>`_

                            Arguments: 1, OFF, ON
                            """
                            _cmd = "AUTO"
                            args = ["1", "OFF", "ON"]

                            class STATe(SCPINode, SCPIBool):
                                """
                                SYSTem:COMMunicate:RDEVice:PMETer:CONFigure:AUTO:STATe

                                Arguments: 1, OFF, ON
                                """
                                _cmd = "STATe"
                                args = ["1", "OFF", "ON"]

                            STATe = STATe()
                            """
                            SYSTem:COMMunicate:RDEVice:PMETer:CONFigure:AUTO:STATe

                            Arguments: 1, OFF, ON
                            """

                        AUTO = AUTO()
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:CONFigure:AUTO
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_CONFigure_AUTO>`_

                        Arguments: 1, OFF, ON
                        """

                    CONFigure = CONFigure()
                    """
                    SYSTem:COMMunicate:RDEVice:PMETer:CONFigure

                    Arguments:
                    """

                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:COUNt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_COUNt>`_

                        Arguments:
                        """
                        _cmd = "COUNt"
                        args = []

                    COUNt = COUNt()
                    """
                    `SYSTem:COMMunicate:RDEVice:PMETer:COUNt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_COUNt>`_

                    Arguments:
                    """

                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:DEFine
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_DEFine>`_

                        Arguments: 'string'
                        """
                        _cmd = "DEFine"
                        args = ["'string'"]

                    DEFine = DEFine()
                    """
                    `SYSTem:COMMunicate:RDEVice:PMETer:DEFine
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_DEFine>`_

                    Arguments: 'string'
                    """

                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:DELete
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_DELete>`_

                        Arguments:
                        """
                        _cmd = "DELete"
                        args = []

                    DELete = DELete()
                    """
                    `SYSTem:COMMunicate:RDEVice:PMETer:DELete
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_PMETer_DELete>`_

                    Arguments:
                    """

                PMETer = PMETer()
                """
                SYSTem:COMMunicate:RDEVice:PMETer

                Arguments:
                """

                class RECeiver(SCPINode):
                    """
                    SYSTem:COMMunicate:RDEVice:RECeiver

                    Arguments:
                    """
                    _cmd = "RECeiver"
                    args = []

                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:RECeiver:DEFine
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_RECeiver_DEFine>`_

                        Arguments: 'string'
                        """
                        _cmd = "DEFine"
                        args = ["'string'"]

                    DEFine = DEFine()
                    """
                    `SYSTem:COMMunicate:RDEVice:RECeiver:DEFine
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_RECeiver_DEFine>`_

                    Arguments: 'string'
                    """

                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:RECeiver:DELete
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_RECeiver_DELete>`_

                        Arguments:
                        """
                        _cmd = "DELete"
                        args = []

                    DELete = DELete()
                    """
                    `SYSTem:COMMunicate:RDEVice:RECeiver:DELete
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_RECeiver_DELete>`_

                    Arguments:
                    """

                RECeiver = RECeiver()
                """
                SYSTem:COMMunicate:RDEVice:RECeiver

                Arguments:
                """

                class TEUNit(SCPINode):
                    """
                    SYSTem:COMMunicate:RDEVice:TEUNit

                    Arguments:
                    """
                    _cmd = "TEUNit"
                    args = []

                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:TEUNit:COUNt
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_TEUNit_COUNt>`_

                        Arguments:
                        """
                        _cmd = "COUNt"
                        args = []

                    COUNt = COUNt()
                    """
                    `SYSTem:COMMunicate:RDEVice:TEUNit:COUNt
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_TEUNit_COUNt>`_

                    Arguments:
                    """

                    class IDN(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:TEUNit:IDN
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_TEUNit_IDN>`_

                        Arguments:
                        """
                        _cmd = "IDN"
                        args = []

                    IDN = IDN()
                    """
                    `SYSTem:COMMunicate:RDEVice:TEUNit:IDN
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_TEUNit_IDN>`_

                    Arguments:
                    """

                    class OPT(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:TEUNit:OPT
                        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_TEUNit_OPT>`_

                        Arguments:
                        """
                        _cmd = "OPT"
                        args = []

                    OPT = OPT()
                    """
                    `SYSTem:COMMunicate:RDEVice:TEUNit:OPT
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#RDEVice_TEUNit_OPT>`_

                    Arguments:
                    """

                TEUNit = TEUNit()
                """
                SYSTem:COMMunicate:RDEVice:TEUNit

                Arguments:
                """

            RDEVice = RDEVice()
            """
            SYSTem:COMMunicate:RDEVice

            Arguments:
            """

            class TCPip(SCPINode):
                """
                SYSTem:COMMunicate:TCPip

                Arguments:
                """
                _cmd = "TCPip"
                args = []

                class CONTrol(SCPINode, SCPIQuery):
                    """
                    SYSTem:COMMunicate:TCPip:CONTrol

                    Arguments:
                    """
                    _cmd = "CONTrol"
                    args = []

                CONTrol = CONTrol()
                """
                SYSTem:COMMunicate:TCPip:CONTrol

                Arguments:
                """

            TCPip = TCPip()
            """
            SYSTem:COMMunicate:TCPip

            Arguments:
            """

        COMMunicate = COMMunicate()
        """
        SYSTem:COMMunicate

        Arguments:
        """

        class CORRection(SCPINode):
            """
            SYSTem:CORRection

            Arguments:
            """
            _cmd = "CORRection"
            args = []

            class FMPort(SCPINode, SCPIBool):
                """
                SYSTem:CORRection:FMPort

                Arguments: 1, OFF, ON
                """
                _cmd = "FMPort"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SYSTem:CORRection:FMPort:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#CORRection_FMPort_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SYSTem:CORRection:FMPort:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#CORRection_FMPort_STATe>`_

                Arguments: 1, OFF, ON
                """

            FMPort = FMPort()
            """
            SYSTem:CORRection:FMPort

            Arguments: 1, OFF, ON
            """

        CORRection = CORRection()
        """
        SYSTem:CORRection

        Arguments:
        """

        class DATA(SCPINode):
            """
            SYSTem:DATA

            Arguments:
            """
            _cmd = "DATA"
            args = []

            class SIZE(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:DATA:SIZE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#DATA_SIZE>`_

                Arguments: ALL, AUTO
                """
                _cmd = "SIZE"
                args = ["ALL", "AUTO"]

            SIZE = SIZE()
            """
            `SYSTem:DATA:SIZE
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#DATA_SIZE>`_

            Arguments: ALL, AUTO
            """

        DATA = DATA()
        """
        SYSTem:DATA

        Arguments:
        """

        class DATE(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:DATE
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#DATE>`_

            Arguments: 1
            """
            _cmd = "DATE"
            args = ["1"]

        DATE = DATE()
        """
        `SYSTem:DATE
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#DATE>`_

        Arguments: 1
        """

        class DISPlay(SCPINode):
            """
            SYSTem:DISPlay

            Arguments:
            """
            _cmd = "DISPlay"
            args = []

            class COLor(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:DISPlay:COLor
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#DISPlay_COLor>`_

                Arguments: BWLStyles, BWSolid, DBACkground, LBACkground
                """
                _cmd = "COLor"
                args = ["BWLStyles", "BWSolid", "DBACkground", "LBACkground"]

            COLor = COLor()
            """
            `SYSTem:DISPlay:COLor
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#DISPlay_COLor>`_

            Arguments: BWLStyles, BWSolid, DBACkground, LBACkground
            """

            class UPDate(SCPINode, SCPIBool):
                """
                `SYSTem:DISPlay:UPDate
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#DISPlay_UPDate>`_

                Arguments: 1, FREeze, OFF, ON, ONCE
                """
                _cmd = "UPDate"
                args = ["1", "FREeze", "OFF", "ON", "ONCE"]

            UPDate = UPDate()
            """
            `SYSTem:DISPlay:UPDate
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#DISPlay_UPDate>`_

            Arguments: 1, FREeze, OFF, ON, ONCE
            """

        DISPlay = DISPlay()
        """
        SYSTem:DISPlay

        Arguments:
        """

        class ERRor(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:ERRor

            Arguments:
            """
            _cmd = "ERRor"
            args = []

            class ALL(SCPINode, SCPIQuery):
                """
                `SYSTem:ERRor:ALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#ERRor_ALL>`_

                Arguments:
                """
                _cmd = "ALL"
                args = []

            ALL = ALL()
            """
            `SYSTem:ERRor:ALL
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#ERRor_ALL>`_

            Arguments:
            """

            class DISPlay(SCPINode, SCPIBool):
                """
                `SYSTem:ERRor:DISPlay
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#ERRor_DISPlay>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "DISPlay"
                args = ["1", "OFF", "ON"]

            DISPlay = DISPlay()
            """
            `SYSTem:ERRor:DISPlay
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#ERRor_DISPlay>`_

            Arguments: 1, OFF, ON
            """

            class NEXT(SCPINode, SCPIQuery):
                """
                `SYSTem:ERRor:NEXT
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#ERRor_NEXT>`_

                Arguments:
                """
                _cmd = "NEXT"
                args = []

            NEXT = NEXT()
            """
            `SYSTem:ERRor:NEXT
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#ERRor_NEXT>`_

            Arguments:
            """

        ERRor = ERRor()
        """
        SYSTem:ERRor

        Arguments:
        """

        class FIRMware(SCPINode):
            """
            SYSTem:FIRMware

            Arguments:
            """
            _cmd = "FIRMware"
            args = []

            class UPDate(SCPINode, SCPISet):
                """
                `SYSTem:FIRMware:UPDate
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#FIRMware_UPDate>`_

                Arguments: 'string'
                """
                _cmd = "UPDate"
                args = ["'string'"]

            UPDate = UPDate()
            """
            `SYSTem:FIRMware:UPDate
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#FIRMware_UPDate>`_

            Arguments: 'string'
            """

        FIRMware = FIRMware()
        """
        SYSTem:FIRMware

        Arguments:
        """

        class FPReset(SCPINode, SCPISet):
            """
            `SYSTem:FPReset
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#FPReset>`_

            Arguments:
            """
            _cmd = "FPReset"
            args = []

        FPReset = FPReset()
        """
        `SYSTem:FPReset
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#FPReset>`_

        Arguments:
        """

        class FREQuency(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:FREQuency
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#FREQuency_>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "FREQuency"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

        FREQuency = FREQuency()
        """
        `SYSTem:FREQuency
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#FREQuency_>`_

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

        class IDENtify(SCPINode):
            """
            SYSTem:IDENtify

            Arguments:
            """
            _cmd = "IDENtify"
            args = []

            class FACTory(SCPINode, SCPISet):
                """
                `SYSTem:IDENtify:FACTory
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#IDENtify_FACTory>`_

                Arguments:
                """
                _cmd = "FACTory"
                args = []

            FACTory = FACTory()
            """
            `SYSTem:IDENtify:FACTory
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#IDENtify_FACTory>`_

            Arguments:
            """

            class STRing(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:IDENtify:STRing
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#IDENtify_STRing>`_

                Arguments: 'string'
                """
                _cmd = "STRing"
                args = ["'string'"]

            STRing = STRing()
            """
            `SYSTem:IDENtify:STRing
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#IDENtify_STRing>`_

            Arguments: 'string'
            """

        IDENtify = IDENtify()
        """
        SYSTem:IDENtify

        Arguments:
        """

        class KLOCk(SCPINode, SCPIBool):
            """
            `SYSTem:KLOCk
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#KLOCk>`_

            Arguments: 1, OFF, ON
            """
            _cmd = "KLOCk"
            args = ["1", "OFF", "ON"]

        KLOCk = KLOCk()
        """
        `SYSTem:KLOCk
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#KLOCk>`_

        Arguments: 1, OFF, ON
        """

        class LANGuage(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:LANGuage
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#LANGuage>`_

            Arguments: 'string'
            """
            _cmd = "LANGuage"
            args = ["'string'"]

        LANGuage = LANGuage()
        """
        `SYSTem:LANGuage
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#LANGuage>`_

        Arguments: 'string'
        """

        class LOGGing(SCPINode):
            """
            SYSTem:LOGGing

            Arguments:
            """
            _cmd = "LOGGing"
            args = []

            class REMote(SCPINode, SCPIBool):
                """
                SYSTem:LOGGing:REMote

                Arguments: 1, OFF, ON
                """
                _cmd = "REMote"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SYSTem:LOGGing:REMote:STATe

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                SYSTem:LOGGing:REMote:STATe

                Arguments: 1, OFF, ON
                """

            REMote = REMote()
            """
            SYSTem:LOGGing:REMote

            Arguments: 1, OFF, ON
            """

        LOGGing = LOGGing()
        """
        SYSTem:LOGGing

        Arguments:
        """

        class NOPeration(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:NOPeration

            Arguments:
            """
            _cmd = "NOPeration"
            args = []

        NOPeration = NOPeration()
        """
        SYSTem:NOPeration

        Arguments:
        """

        class PASSword(SCPINode, SCPISet):
            """
            SYSTem:PASSword

            Arguments: 'string'
            """
            _cmd = "PASSword"
            args = ["'string'"]

            class CENable(SCPINode, SCPISet):
                """
                `SYSTem:PASSword:CENable
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PASSword_ENABle>`_

                Arguments: 'string'
                """
                _cmd = "CENable"
                args = ["'string'"]

            CENable = CENable()
            """
            `SYSTem:PASSword:CENable
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PASSword_ENABle>`_

            Arguments: 'string'
            """

        PASSword = PASSword()
        """
        SYSTem:PASSword

        Arguments: 'string'
        """

        class PRESet(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:PRESet
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRESet>`_

            Arguments:
            """
            _cmd = "PRESet"
            args = []

            class DUMMy(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:PRESet:DUMMy

                Arguments:
                """
                _cmd = "DUMMy"
                args = []

            DUMMy = DUMMy()
            """
            SYSTem:PRESet:DUMMy

            Arguments:
            """

            class REMote(SCPINode, SCPIBool):
                """
                SYSTem:PRESet:REMote

                Arguments: 1, OFF, ON
                """
                _cmd = "REMote"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SYSTem:PRESet:REMote:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRESet_REMote_STATe>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SYSTem:PRESet:REMote:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRESet_REMote_STATe>`_

                Arguments: 1, OFF, ON
                """

            REMote = REMote()
            """
            SYSTem:PRESet:REMote

            Arguments: 1, OFF, ON
            """

            class SCOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:PRESet:SCOPe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRESet_SCOPe>`_

                Arguments: ALL, SINGle
                """
                _cmd = "SCOPe"
                args = ["ALL", "SINGle"]

            SCOPe = SCOPe()
            """
            `SYSTem:PRESet:SCOPe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRESet_SCOPe>`_

            Arguments: ALL, SINGle
            """

            class USER(SCPINode, SCPIBool):
                """
                SYSTem:PRESet:USER

                Arguments: 1, OFF, ON
                """
                _cmd = "USER"
                args = ["1", "OFF", "ON"]

                class NAME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:PRESet:USER:NAME
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRESet_USER_NAME>`_

                    Arguments: 'string'
                    """
                    _cmd = "NAME"
                    args = ["'string'"]

                NAME = NAME()
                """
                `SYSTem:PRESet:USER:NAME
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRESet_USER_NAME>`_

                Arguments: 'string'
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SYSTem:PRESet:USER:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRESet_USER>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SYSTem:PRESet:USER:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRESet_USER>`_

                Arguments: 1, OFF, ON
                """

            USER = USER()
            """
            SYSTem:PRESet:USER

            Arguments: 1, OFF, ON
            """

        PRESet = PRESet()
        """
        `SYSTem:PRESet
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRESet>`_

        Arguments:
        """

        class PRIority(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:PRIority
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRIority>`_

            Arguments: ANORmal, HIGH, NORMal
            """
            _cmd = "PRIority"
            args = ["ANORmal", "HIGH", "NORMal"]

        PRIority = PRIority()
        """
        `SYSTem:PRIority
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#PRIority>`_

        Arguments: ANORmal, HIGH, NORMal
        """

        class SETTings(SCPINode):
            """
            SYSTem:SETTings

            Arguments:
            """
            _cmd = "SETTings"
            args = []

            class UPDate(SCPINode, SCPISet):
                """
                SYSTem:SETTings:UPDate

                Arguments: ONCE
                """
                _cmd = "UPDate"
                args = ["ONCE"]

            UPDate = UPDate()
            """
            SYSTem:SETTings:UPDate

            Arguments: ONCE
            """

        SETTings = SETTings()
        """
        SYSTem:SETTings

        Arguments:
        """

        class SHUTdown(SCPINode, SCPISet):
            """
            `SYSTem:SHUTdown
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#SHUTdown>`_

            Arguments:
            """
            _cmd = "SHUTdown"
            args = []

        SHUTdown = SHUTdown()
        """
        `SYSTem:SHUTdown
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#SHUTdown>`_

        Arguments:
        """

        class SOUNd(SCPINode):
            """
            SYSTem:SOUNd

            Arguments:
            """
            _cmd = "SOUNd"
            args = []

            class ALARm(SCPINode, SCPIBool):
                """
                SYSTem:SOUNd:ALARm

                Arguments: 1, OFF, ON
                """
                _cmd = "ALARm"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SYSTem:SOUNd:ALARm:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#SOUNd_ALARm__STATe_>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SYSTem:SOUNd:ALARm:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#SOUNd_ALARm__STATe_>`_

                Arguments: 1, OFF, ON
                """

            ALARm = ALARm()
            """
            SYSTem:SOUNd:ALARm

            Arguments: 1, OFF, ON
            """

            class STATus(SCPINode, SCPIBool):
                """
                SYSTem:SOUNd:STATus

                Arguments: 1, OFF, ON
                """
                _cmd = "STATus"
                args = ["1", "OFF", "ON"]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SYSTem:SOUNd:STATus:STATe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#SOUNd_STATus__STATe_1>`_

                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]

                STATe = STATe()
                """
                `SYSTem:SOUNd:STATus:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#SOUNd_STATus__STATe_1>`_

                Arguments: 1, OFF, ON
                """

            STATus = STATus()
            """
            SYSTem:SOUNd:STATus

            Arguments: 1, OFF, ON
            """

        SOUNd = SOUNd()
        """
        SYSTem:SOUNd

        Arguments:
        """

        class TIME(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:TIME
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#TIME>`_

            Arguments: 1
            """
            _cmd = "TIME"
            args = ["1"]

        TIME = TIME()
        """
        `SYSTem:TIME
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#TIME>`_

        Arguments: 1
        """

        class TRESet(SCPINode, SCPIBool):
            """
            SYSTem:TRESet

            Arguments: 1, OFF, ON
            """
            _cmd = "TRESet"
            args = ["1", "OFF", "ON"]

            class STATe(SCPINode, SCPIBool):
                """
                `SYSTem:TRESet:STATe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#TRESet_STATe>`_

                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]

            STATe = STATe()
            """
            `SYSTem:TRESet:STATe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#TRESet_STATe>`_

            Arguments: 1, OFF, ON
            """

        TRESet = TRESet()
        """
        SYSTem:TRESet

        Arguments: 1, OFF, ON
        """

        class USER(SCPINode):
            """
            SYSTem:USER

            Arguments:
            """
            _cmd = "USER"
            args = []

            class DISPlay(SCPINode):
                """
                SYSTem:USER:DISPlay

                Arguments:
                """
                _cmd = "DISPlay"
                args = []

                class TITLe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:USER:DISPlay:TITLe
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#USER_DISPlay_TITle>`_

                    Arguments: 'string'
                    """
                    _cmd = "TITLe"
                    args = ["'string'"]

                TITLe = TITLe()
                """
                `SYSTem:USER:DISPlay:TITLe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#USER_DISPlay_TITle>`_

                Arguments: 'string'
                """

            DISPlay = DISPlay()
            """
            SYSTem:USER:DISPlay

            Arguments:
            """

            class FKEY(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:USER:FKEY

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "FKEY"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            FKEY = FKEY()
            """
            SYSTem:USER:FKEY

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class KEY(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:USER:KEY
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#USER_KEY>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "KEY"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:USER:KEY:FUNCtion
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#USER_KEY_FUNCtion>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "FUNCtion"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                FUNCtion = FUNCtion()
                """
                `SYSTem:USER:KEY:FUNCtion
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#USER_KEY_FUNCtion>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            KEY = KEY()
            """
            `SYSTem:USER:KEY
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#USER_KEY>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        USER = USER()
        """
        SYSTem:USER

        Arguments:
        """

        class VERSion(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:VERSion
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#VERSion_>`_

            Arguments:
            """
            _cmd = "VERSion"
            args = []

        VERSion = VERSion()
        """
        `SYSTem:VERSion
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/system/system.htm#VERSion_>`_

        Arguments:
        """

        class WAIT(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:WAIT

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "WAIT"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

        WAIT = WAIT()
        """
        SYSTem:WAIT

        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
        """

    SYSTem = SYSTem()
    """
    SYSTem

    Arguments:
    """

    class TRACe(SCPINode, SCPIQuery, SCPISet):
        """
        TRACe

        Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
        """
        _cmd = "TRACe"
        args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]

        class CLEar(SCPINode, SCPISet):
            """
            `TRACe:CLEar
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trace/trace.htm#CLEar>`_

            Arguments: MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
            """
            _cmd = "CLEar"
            args = ["MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]

        CLEar = CLEar()
        """
        `TRACe:CLEar
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trace/trace.htm#CLEar>`_

        Arguments: MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
        """

        class COPY(SCPINode, SCPISet):
            """
            `TRACe:COPY
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trace/trace.htm#COPY>`_

            Arguments: MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8, 'string'
            """
            _cmd = "COPY"
            args = ["MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8", "'string'"]

            class MATH(SCPINode, SCPISet):
                """
                `TRACe:COPY:MATH
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trace/trace.htm#COPY_MATH>`_

                Arguments: MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8, 'string'
                """
                _cmd = "MATH"
                args = ["MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8", "'string'"]

            MATH = MATH()
            """
            `TRACe:COPY:MATH
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trace/trace.htm#COPY_MATH>`_

            Arguments: MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8, 'string'
            """

        COPY = COPY()
        """
        `TRACe:COPY
        <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trace/trace.htm#COPY>`_

        Arguments: MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8, 'string'
        """

        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            TRACe:DATA

            Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
            """
            _cmd = "DATA"
            args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]

            class RESPonse(SCPINode, SCPIQuery, SCPISet):
                """
                TRACe:DATA:RESPonse

                Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
                """
                _cmd = "RESPonse"
                args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]

                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRACe:DATA:RESPonse:ALL
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trace/trace.htm#RESPonse>`_

                    Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
                    """
                    _cmd = "ALL"
                    args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]

                ALL = ALL()
                """
                `TRACe:DATA:RESPonse:ALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trace/trace.htm#RESPonse>`_

                Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
                """

            RESPonse = RESPonse()
            """
            TRACe:DATA:RESPonse

            Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
            """

            class STIMulus(SCPINode, SCPIQuery, SCPISet):
                """
                TRACe:DATA:STIMulus

                Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
                """
                _cmd = "STIMulus"
                args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]

                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRACe:DATA:STIMulus:ALL
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trace/trace.htm#STIMulus>`_

                    Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
                    """
                    _cmd = "ALL"
                    args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]

                ALL = ALL()
                """
                `TRACe:DATA:STIMulus:ALL
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trace/trace.htm#STIMulus>`_

                Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
                """

            STIMulus = STIMulus()
            """
            TRACe:DATA:STIMulus

            Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
            """

        DATA = DATA()
        """
        TRACe:DATA

        Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
        """

    TRACe = TRACe()
    """
    TRACe

    Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
    """

    class TRIGger(SCPINodeN):
        """
        TRIGger

        Arguments:
        """
        _cmd = "TRIGger"
        args = []

        class SEQuence(SCPINode):
            """
            TRIGger:SEQuence

            Arguments:
            """
            _cmd = "SEQuence"
            args = []

            class HOLDoff(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:HOLDoff
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#HOLDoff>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "HOLDoff"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                class GENerator(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:HOLDoff:GENerator
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#HOLDoff_GENerator>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "GENerator"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                GENerator = GENerator()
                """
                `TRIGger:SEQuence:HOLDoff:GENerator
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#HOLDoff_GENerator>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:HOLDoff:MODE
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#HOLDoff_MODE>`_

                    Arguments: PALL, PSPecific
                    """
                    _cmd = "MODE"
                    args = ["PALL", "PSPecific"]

                MODE = MODE()
                """
                `TRIGger:SEQuence:HOLDoff:MODE
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#HOLDoff_MODE>`_

                Arguments: PALL, PSPecific
                """

                class PORT(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:HOLDoff:PORT
                    <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#HOLDoff_PORT>`_

                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "PORT"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

                PORT = PORT()
                """
                `TRIGger:SEQuence:HOLDoff:PORT
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#HOLDoff_PORT>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """

            HOLDoff = HOLDoff()
            """
            `TRIGger:SEQuence:HOLDoff
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#HOLDoff>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

            class LINK(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:LINK
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#LINK>`_

                Arguments: 'POINt', 'PPOint', 'SEGMent', 'SWEep'
                """
                _cmd = "LINK"
                args = ["'POINt'", "'PPOint'", "'SEGMent'", "'SWEep'"]

            LINK = LINK()
            """
            `TRIGger:SEQuence:LINK
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#LINK>`_

            Arguments: 'POINt', 'PPOint', 'SEGMent', 'SWEep'
            """

            class PULSe(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:PULSe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#PULSe>`_

                Arguments: FEPulse, FESYnc, REPulse, RESYnc
                """
                _cmd = "PULSe"
                args = ["FEPulse", "FESYnc", "REPulse", "RESYnc"]

            PULSe = PULSe()
            """
            `TRIGger:SEQuence:PULSe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#PULSe>`_

            Arguments: FEPulse, FESYnc, REPulse, RESYnc
            """

            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:SLOPe
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#SLOPe>`_

                Arguments: NEGative, POSitive
                """
                _cmd = "SLOPe"
                args = ["NEGative", "POSitive"]

            SLOPe = SLOPe()
            """
            `TRIGger:SEQuence:SLOPe
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#SLOPe>`_

            Arguments: NEGative, POSitive
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:SOURce
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#SOURce>`_

                Arguments: EXTernal, IMMediate, MANual, PGENerator, RFPower, TIMer
                """
                _cmd = "SOURce"
                args = ["EXTernal", "IMMediate", "MANual", "PGENerator", "RFPower", "TIMer"]

            SOURce = SOURce()
            """
            `TRIGger:SEQuence:SOURce
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#SOURce>`_

            Arguments: EXTernal, IMMediate, MANual, PGENerator, RFPower, TIMer
            """

            class TIMer(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:TIMer
                <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#TIMer>`_

                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "TIMer"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]

            TIMer = TIMer()
            """
            `TRIGger:SEQuence:TIMer
            <http://www.rohde-schwarz.com/webhelp/webhelp_zva_8/scpi_reference/trigger/trigger.htm#TIMer>`_

            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """

        SEQuence = SEQuence()
        """
        TRIGger:SEQuence

        Arguments:
        """

    TRIGger = TRIGger()
    """
    TRIGger

    Arguments:
    """

    # END OF ZVA_gen
