# -*- coding: utf-8 -*-
# Generated from NRPxxSN_syntax.txt on 2017-07-29 18:55
from RSSscpi.SCPI_gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool
from RSSscpi.Instrument import Instrument


class NRPxxSN_gen(Instrument):
    class CLS(SCPINode, SCPISet):
        """
        *CLS

        Arguments:
        """
        _cmd = "*CLS"
        args = []

    CLS = CLS()
    """
    *CLS

    Arguments:
    """

    class ESE(SCPINode, SCPIQuery, SCPISet):
        """
        *ESE

        Arguments: 1
        """
        _cmd = "*ESE"
        args = ["1"]

    ESE = ESE()
    """
    *ESE

    Arguments: 1
    """

    class ESR(SCPINode, SCPIQuery):
        """
        *ESR

        Arguments:
        """
        _cmd = "*ESR"
        args = []

    ESR = ESR()
    """
    *ESR

    Arguments:
    """

    class IDN(SCPINode, SCPIQuery):
        """
        *IDN

        Arguments:
        """
        _cmd = "*IDN"
        args = []

    IDN = IDN()
    """
    *IDN

    Arguments:
    """

    class IST(SCPINode, SCPIQuery):
        """
        *IST

        Arguments:
        """
        _cmd = "*IST"
        args = []

    IST = IST()
    """
    *IST

    Arguments:
    """

    class OPC(SCPINode, SCPIQuery, SCPISet):
        """
        *OPC

        Arguments:
        """
        _cmd = "*OPC"
        args = []

    OPC = OPC()
    """
    *OPC

    Arguments:
    """

    class OPT(SCPINode, SCPIQuery):
        """
        *OPT

        Arguments:
        """
        _cmd = "*OPT"
        args = []

    OPT = OPT()
    """
    *OPT

    Arguments:
    """

    class PRE(SCPINode, SCPIQuery, SCPISet):
        """
        *PRE

        Arguments: 1
        """
        _cmd = "*PRE"
        args = ["1"]

    PRE = PRE()
    """
    *PRE

    Arguments: 1
    """

    class RCL(SCPINode, SCPISet):
        """
        *RCL

        Arguments: 1
        """
        _cmd = "*RCL"
        args = ["1"]

    RCL = RCL()
    """
    *RCL

    Arguments: 1
    """

    class RST(SCPINode, SCPISet):
        """
        *RST

        Arguments:
        """
        _cmd = "*RST"
        args = []

    RST = RST()
    """
    *RST

    Arguments:
    """

    class SAV(SCPINode, SCPISet):
        """
        *SAV

        Arguments: 1
        """
        _cmd = "*SAV"
        args = ["1"]

    SAV = SAV()
    """
    *SAV

    Arguments: 1
    """

    class SRE(SCPINode, SCPIQuery, SCPISet):
        """
        *SRE

        Arguments: 1
        """
        _cmd = "*SRE"
        args = ["1"]

    SRE = SRE()
    """
    *SRE

    Arguments: 1
    """

    class STB(SCPINode, SCPIQuery):
        """
        *STB

        Arguments:
        """
        _cmd = "*STB"
        args = []

    STB = STB()
    """
    *STB

    Arguments:
    """

    class TRG(SCPINode, SCPISet):
        """
        *TRG

        Arguments:
        """
        _cmd = "*TRG"
        args = []

    TRG = TRG()
    """
    *TRG

    Arguments:
    """

    class TST(SCPINode, SCPIQuery):
        """
        *TST

        Arguments:
        """
        _cmd = "*TST"
        args = []

    TST = TST()
    """
    *TST

    Arguments:
    """

    class WAI(SCPINode, SCPISet):
        """
        *WAI

        Arguments:
        """
        _cmd = "*WAI"
        args = []

    WAI = WAI()
    """
    *WAI

    Arguments:
    """

    class ABORt(SCPINode, SCPISet):
        """
        ABORt

        Arguments:
        """
        _cmd = "ABORt"
        args = []

    ABORt = ABORt()
    """
    ABORt

    Arguments:
    """

    class CALCulate(SCPINode):
        """
        CALCulate

        Arguments:
        """
        _cmd = "CALCulate"
        args = []

        class FEED(SCPINode, SCPIQuery, SCPISet):
            """
            CALCulate:FEED

            Arguments: 'string'
            """
            _cmd = "FEED"
            args = ["'string'"]

        FEED = FEED()
        """
        CALCulate:FEED

        Arguments: 'string'
        """

    CALCulate = CALCulate()
    """
    CALCulate

    Arguments:
    """

    class CALibration(SCPINode):
        """
        CALibration

        Arguments:
        """
        _cmd = "CALibration"
        args = []

        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            CALibration:DATA

            Arguments: <block_data>
            """
            _cmd = "DATA"
            args = ["<block_data>"]

            class LENGth(SCPINode, SCPIQuery):
                """
                CALibration:DATA:LENGth

                Arguments:
                """
                _cmd = "LENGth"
                args = []

            LENGth = LENGth()
            """
            CALibration:DATA:LENGth

            Arguments:
            """

        DATA = DATA()
        """
        CALibration:DATA

        Arguments: <block_data>
        """

        class USER(SCPINode):
            """
            CALibration:USER

            Arguments:
            """
            _cmd = "USER"
            args = []

            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                CALibration:USER:DATA

                Arguments: <block_data>
                """
                _cmd = "DATA"
                args = ["<block_data>"]

                class LENGth(SCPINode, SCPIQuery):
                    """
                    CALibration:USER:DATA:LENGth

                    Arguments:
                    """
                    _cmd = "LENGth"
                    args = []

                LENGth = LENGth()
                """
                CALibration:USER:DATA:LENGth

                Arguments:
                """

            DATA = DATA()
            """
            CALibration:USER:DATA

            Arguments: <block_data>
            """

        USER = USER()
        """
        CALibration:USER

        Arguments:
        """

        class ZERO(SCPINode):
            """
            CALibration:ZERO

            Arguments:
            """
            _cmd = "ZERO"
            args = []

            class AUTO(SCPINode, SCPIQuery, SCPISet):
                """
                CALibration:ZERO:AUTO

                Arguments: ONCE
                """
                _cmd = "AUTO"
                args = ["ONCE"]

            AUTO = AUTO()
            """
            CALibration:ZERO:AUTO

            Arguments: ONCE
            """

        ZERO = ZERO()
        """
        CALibration:ZERO

        Arguments:
        """

    CALibration = CALibration()
    """
    CALibration

    Arguments:
    """

    class FETCh(SCPINodeN, SCPIQuery):
        """
        FETCh

        Arguments:
        """
        _cmd = "FETCh"
        args = []

        class ARRay(SCPINode):
            """
            FETCh:ARRay

            Arguments:
            """
            _cmd = "ARRay"
            args = []

            class POWer(SCPINode):
                """
                FETCh:ARRay:POWer

                Arguments:
                """
                _cmd = "POWer"
                args = []

                class AVG(SCPINode, SCPIQuery):
                    """
                    FETCh:ARRay:POWer:AVG

                    Arguments:
                    """
                    _cmd = "AVG"
                    args = []

                AVG = AVG()
                """
                FETCh:ARRay:POWer:AVG

                Arguments:
                """

            POWer = POWer()
            """
            FETCh:ARRay:POWer

            Arguments:
            """

        ARRay = ARRay()
        """
        FETCh:ARRay

        Arguments:
        """

        class SCALar(SCPINode):
            """
            FETCh:SCALar

            Arguments:
            """
            _cmd = "SCALar"
            args = []

            class POWer(SCPINode):
                """
                FETCh:SCALar:POWer

                Arguments:
                """
                _cmd = "POWer"
                args = []

                class AVG(SCPINode, SCPIQuery):
                    """
                    FETCh:SCALar:POWer:AVG

                    Arguments:
                    """
                    _cmd = "AVG"
                    args = []

                AVG = AVG()
                """
                FETCh:SCALar:POWer:AVG

                Arguments:
                """

                class BURSt(SCPINode, SCPIQuery):
                    """
                    FETCh:SCALar:POWer:BURSt

                    Arguments:
                    """
                    _cmd = "BURSt"
                    args = []

                BURSt = BURSt()
                """
                FETCh:SCALar:POWer:BURSt

                Arguments:
                """

                class TSLot(SCPINode, SCPIQuery):
                    """
                    FETCh:SCALar:POWer:TSLot

                    Arguments:
                    """
                    _cmd = "TSLot"
                    args = []

                TSLot = TSLot()
                """
                FETCh:SCALar:POWer:TSLot

                Arguments:
                """

            POWer = POWer()
            """
            FETCh:SCALar:POWer

            Arguments:
            """

        SCALar = SCALar()
        """
        FETCh:SCALar

        Arguments:
        """

    FETCh = FETCh()
    """
    FETCh

    Arguments:
    """

    class FORMat(SCPINode):
        """
        FORMat

        Arguments:
        """
        _cmd = "FORMat"
        args = []

        class BORDer(SCPINode, SCPIQuery, SCPISet):
            """
            FORMat:BORDer

            Arguments: NORMal, SWAPped
            """
            _cmd = "BORDer"
            args = ["NORMal", "SWAPped"]

        BORDer = BORDer()
        """
        FORMat:BORDer

        Arguments: NORMal, SWAPped
        """

        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            FORMat:DATA

            Arguments: ASCii, REAL
            """
            _cmd = "DATA"
            args = ["ASCii", "REAL"]

        DATA = DATA()
        """
        FORMat:DATA

        Arguments: ASCii, REAL
        """

        class SREGister(SCPINode, SCPIQuery, SCPISet):
            """
            FORMat:SREGister

            Arguments: ASCii, BINary, HEXadecimal, OCTal
            """
            _cmd = "SREGister"
            args = ["ASCii", "BINary", "HEXadecimal", "OCTal"]

        SREGister = SREGister()
        """
        FORMat:SREGister

        Arguments: ASCii, BINary, HEXadecimal, OCTal
        """

    FORMat = FORMat()
    """
    FORMat

    Arguments:
    """

    class INITiate(SCPINode):
        """
        INITiate

        Arguments:
        """
        _cmd = "INITiate"
        args = []

        class ALL(SCPINode, SCPISet):
            """
            INITiate:ALL

            Arguments:
            """
            _cmd = "ALL"
            args = []

        ALL = ALL()
        """
        INITiate:ALL

        Arguments:
        """

        class CONTinuous(SCPINode, SCPIBool):
            """
            INITiate:CONTinuous

            Arguments: 1, ON, OFF
            """
            _cmd = "CONTinuous"
            args = ["1", "ON", "OFF"]

        CONTinuous = CONTinuous()
        """
        INITiate:CONTinuous

        Arguments: 1, ON, OFF
        """

        class IMMediate(SCPINode, SCPISet):
            """
            INITiate:IMMediate

            Arguments:
            """
            _cmd = "IMMediate"
            args = []

        IMMediate = IMMediate()
        """
        INITiate:IMMediate

        Arguments:
        """

    INITiate = INITiate()
    """
    INITiate

    Arguments:
    """

    class READ(SCPINodeN):
        """
        READ

        Arguments:
        """
        _cmd = "READ"
        args = []

        class ARRay(SCPINode):
            """
            READ:ARRay

            Arguments:
            """
            _cmd = "ARRay"
            args = []

            class POWer(SCPINode):
                """
                READ:ARRay:POWer

                Arguments:
                """
                _cmd = "POWer"
                args = []

                class AVG(SCPINode, SCPIQuery):
                    """
                    READ:ARRay:POWer:AVG

                    Arguments:
                    """
                    _cmd = "AVG"
                    args = []

                AVG = AVG()
                """
                READ:ARRay:POWer:AVG

                Arguments:
                """

            POWer = POWer()
            """
            READ:ARRay:POWer

            Arguments:
            """

        ARRay = ARRay()
        """
        READ:ARRay

        Arguments:
        """

        class SCALar(SCPINode):
            """
            READ:SCALar

            Arguments:
            """
            _cmd = "SCALar"
            args = []

            class POWer(SCPINode):
                """
                READ:SCALar:POWer

                Arguments:
                """
                _cmd = "POWer"
                args = []

                class AVG(SCPINode, SCPIQuery):
                    """
                    READ:SCALar:POWer:AVG

                    Arguments:
                    """
                    _cmd = "AVG"
                    args = []

                AVG = AVG()
                """
                READ:SCALar:POWer:AVG

                Arguments:
                """

                class BURSt(SCPINode, SCPIQuery):
                    """
                    READ:SCALar:POWer:BURSt

                    Arguments:
                    """
                    _cmd = "BURSt"
                    args = []

                BURSt = BURSt()
                """
                READ:SCALar:POWer:BURSt

                Arguments:
                """

                class TSLot(SCPINode, SCPIQuery):
                    """
                    READ:SCALar:POWer:TSLot

                    Arguments:
                    """
                    _cmd = "TSLot"
                    args = []

                TSLot = TSLot()
                """
                READ:SCALar:POWer:TSLot

                Arguments:
                """

            POWer = POWer()
            """
            READ:SCALar:POWer

            Arguments:
            """

        SCALar = SCALar()
        """
        READ:SCALar

        Arguments:
        """

        class XTIMe(SCPINode):
            """
            READ:XTIMe

            Arguments:
            """
            _cmd = "XTIMe"
            args = []

            class POWer(SCPINode, SCPIQuery):
                """
                READ:XTIMe:POWer

                Arguments:
                """
                _cmd = "POWer"
                args = []

            POWer = POWer()
            """
            READ:XTIMe:POWer

            Arguments:
            """

        XTIMe = XTIMe()
        """
        READ:XTIMe

        Arguments:
        """

    READ = READ()
    """
    READ

    Arguments:
    """

    class SENSe(SCPINodeN):
        """
        SENSe

        Arguments:
        """
        _cmd = "SENSe"
        args = []

        class AUXiliary(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:AUXiliary

            Arguments: MINMax, NONE, RNDMax
            """
            _cmd = "AUXiliary"
            args = ["MINMax", "NONE", "RNDMax"]

        AUXiliary = AUXiliary()
        """
        SENSe:AUXiliary

        Arguments: MINMax, NONE, RNDMax
        """

        class AVERage(SCPINode):
            """
            SENSe:AVERage

            Arguments:
            """
            _cmd = "AVERage"
            args = []

            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:AVERage:COUNt

                Arguments: 1
                """
                _cmd = "COUNt"
                args = ["1"]

                class AUTO(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:AVERage:COUNt:AUTO

                    Arguments: <boolean>, ONCE
                    """
                    _cmd = "AUTO"
                    args = ["<boolean>", "ONCE"]

                    class MTIMe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:AVERage:COUNt:AUTO:MTIMe

                        Arguments: 1
                        """
                        _cmd = "MTIMe"
                        args = ["1"]

                    MTIMe = MTIMe()
                    """
                    SENSe:AVERage:COUNt:AUTO:MTIMe

                    Arguments: 1
                    """

                    class NSRatio(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:AVERage:COUNt:AUTO:NSRatio

                        Arguments: 1
                        """
                        _cmd = "NSRatio"
                        args = ["1"]

                    NSRatio = NSRatio()
                    """
                    SENSe:AVERage:COUNt:AUTO:NSRatio

                    Arguments: 1
                    """

                    class RESolution(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:AVERage:COUNt:AUTO:RESolution

                        Arguments: 1
                        """
                        _cmd = "RESolution"
                        args = ["1"]

                    RESolution = RESolution()
                    """
                    SENSe:AVERage:COUNt:AUTO:RESolution

                    Arguments: 1
                    """

                    class SLOT(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:AVERage:COUNt:AUTO:SLOT

                        Arguments: 1
                        """
                        _cmd = "SLOT"
                        args = ["1"]

                    SLOT = SLOT()
                    """
                    SENSe:AVERage:COUNt:AUTO:SLOT

                    Arguments: 1
                    """

                    class TYPE(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:AVERage:COUNt:AUTO:TYPE

                        Arguments: NSRatio, RESolution
                        """
                        _cmd = "TYPE"
                        args = ["NSRatio", "RESolution"]

                    TYPE = TYPE()
                    """
                    SENSe:AVERage:COUNt:AUTO:TYPE

                    Arguments: NSRatio, RESolution
                    """

                AUTO = AUTO()
                """
                SENSe:AVERage:COUNt:AUTO

                Arguments: <boolean>, ONCE
                """

            COUNt = COUNt()
            """
            SENSe:AVERage:COUNt

            Arguments: 1
            """

            class RESet(SCPINode, SCPISet):
                """
                SENSe:AVERage:RESet

                Arguments:
                """
                _cmd = "RESet"
                args = []

            RESet = RESet()
            """
            SENSe:AVERage:RESet

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                SENSe:AVERage:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SENSe:AVERage:STATe

            Arguments: 1, ON, OFF
            """

            class TCONtrol(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:AVERage:TCONtrol

                Arguments: MOVing, REPeat
                """
                _cmd = "TCONtrol"
                args = ["MOVing", "REPeat"]

            TCONtrol = TCONtrol()
            """
            SENSe:AVERage:TCONtrol

            Arguments: MOVing, REPeat
            """

        AVERage = AVERage()
        """
        SENSe:AVERage

        Arguments:
        """

        class CORRection(SCPINode):
            """
            SENSe:CORRection

            Arguments:
            """
            _cmd = "CORRection"
            args = []

            class DCYCle(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:DCYCle

                Arguments: 1
                """
                _cmd = "DCYCle"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SENSe:CORRection:DCYCle:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SENSe:CORRection:DCYCle:STATe

                Arguments: 1, ON, OFF
                """

            DCYCle = DCYCle()
            """
            SENSe:CORRection:DCYCle

            Arguments: 1
            """

            class OFFSet(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:OFFSet

                Arguments: 1
                """
                _cmd = "OFFSet"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SENSe:CORRection:OFFSet:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SENSe:CORRection:OFFSet:STATe

                Arguments: 1, ON, OFF
                """

            OFFSet = OFFSet()
            """
            SENSe:CORRection:OFFSet

            Arguments: 1
            """

            class SPDevice(SCPINode):
                """
                SENSe:CORRection:SPDevice

                Arguments:
                """
                _cmd = "SPDevice"
                args = []

                class LIST(SCPINode, SCPIQuery):
                    """
                    SENSe:CORRection:SPDevice:LIST

                    Arguments:
                    """
                    _cmd = "LIST"
                    args = []

                LIST = LIST()
                """
                SENSe:CORRection:SPDevice:LIST

                Arguments:
                """

                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:SPDevice:SELect

                    Arguments: 1
                    """
                    _cmd = "SELect"
                    args = ["1"]

                SELect = SELect()
                """
                SENSe:CORRection:SPDevice:SELect

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SENSe:CORRection:SPDevice:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SENSe:CORRection:SPDevice:STATe

                Arguments: 1, ON, OFF
                """

            SPDevice = SPDevice()
            """
            SENSe:CORRection:SPDevice

            Arguments:
            """

        CORRection = CORRection()
        """
        SENSe:CORRection

        Arguments:
        """

        class FREQuency(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:FREQuency

            Arguments: 1
            """
            _cmd = "FREQuency"
            args = ["1"]

        FREQuency = FREQuency()
        """
        SENSe:FREQuency

        Arguments: 1
        """

        class FUNCtion(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:FUNCtion

            Arguments: 'string'
            """
            _cmd = "FUNCtion"
            args = ["'string'"]

        FUNCtion = FUNCtion()
        """
        SENSe:FUNCtion

        Arguments: 'string'
        """

        class POWer(SCPINode):
            """
            SENSe:POWer

            Arguments:
            """
            _cmd = "POWer"
            args = []

            class AVG(SCPINode):
                """
                SENSe:POWer:AVG

                Arguments:
                """
                _cmd = "AVG"
                args = []

                class APERture(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:POWer:AVG:APERture

                    Arguments: 1
                    """
                    _cmd = "APERture"
                    args = ["1"]

                APERture = APERture()
                """
                SENSe:POWer:AVG:APERture

                Arguments: 1
                """

                class BUFFer(SCPINode):
                    """
                    SENSe:POWer:AVG:BUFFer

                    Arguments:
                    """
                    _cmd = "BUFFer"
                    args = []

                    class CLEar(SCPINode, SCPISet):
                        """
                        SENSe:POWer:AVG:BUFFer:CLEar

                        Arguments:
                        """
                        _cmd = "CLEar"
                        args = []

                    CLEar = CLEar()
                    """
                    SENSe:POWer:AVG:BUFFer:CLEar

                    Arguments:
                    """

                    class COUNt(SCPINode, SCPIQuery):
                        """
                        SENSe:POWer:AVG:BUFFer:COUNt

                        Arguments:
                        """
                        _cmd = "COUNt"
                        args = []

                    COUNt = COUNt()
                    """
                    SENSe:POWer:AVG:BUFFer:COUNt

                    Arguments:
                    """

                    class DATA(SCPINode, SCPIQuery):
                        """
                        SENSe:POWer:AVG:BUFFer:DATA

                        Arguments:
                        """
                        _cmd = "DATA"
                        args = []

                    DATA = DATA()
                    """
                    SENSe:POWer:AVG:BUFFer:DATA

                    Arguments:
                    """

                    class INFO(SCPINode, SCPIQuery):
                        """
                        SENSe:POWer:AVG:BUFFer:INFO

                        Arguments: 'string'
                        """
                        _cmd = "INFO"
                        args = ["'string'"]

                    INFO = INFO()
                    """
                    SENSe:POWer:AVG:BUFFer:INFO

                    Arguments: 'string'
                    """

                    class SIZE(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:POWer:AVG:BUFFer:SIZE

                        Arguments: 1
                        """
                        _cmd = "SIZE"
                        args = ["1"]

                    SIZE = SIZE()
                    """
                    SENSe:POWer:AVG:BUFFer:SIZE

                    Arguments: 1
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SENSe:POWer:AVG:BUFFer:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SENSe:POWer:AVG:BUFFer:STATe

                    Arguments: 1, ON, OFF
                    """

                BUFFer = BUFFer()
                """
                SENSe:POWer:AVG:BUFFer

                Arguments:
                """

                class FAST(SCPINode, SCPIBool):
                    """
                    SENSe:POWer:AVG:FAST

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "FAST"
                    args = ["1", "ON", "OFF"]

                FAST = FAST()
                """
                SENSe:POWer:AVG:FAST

                Arguments: 1, ON, OFF
                """

                class SMOothing(SCPINode):
                    """
                    SENSe:POWer:AVG:SMOothing

                    Arguments:
                    """
                    _cmd = "SMOothing"
                    args = []

                    class STATe(SCPINode, SCPIBool):
                        """
                        SENSe:POWer:AVG:SMOothing:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SENSe:POWer:AVG:SMOothing:STATe

                    Arguments: 1, ON, OFF
                    """

                SMOothing = SMOothing()
                """
                SENSe:POWer:AVG:SMOothing

                Arguments:
                """

            AVG = AVG()
            """
            SENSe:POWer:AVG

            Arguments:
            """

            class BURSt(SCPINode):
                """
                SENSe:POWer:BURSt

                Arguments:
                """
                _cmd = "BURSt"
                args = []

                class DTOLerance(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:POWer:BURSt:DTOLerance

                    Arguments: 1
                    """
                    _cmd = "DTOLerance"
                    args = ["1"]

                DTOLerance = DTOLerance()
                """
                SENSe:POWer:BURSt:DTOLerance

                Arguments: 1
                """

                class LENGth(SCPINode, SCPIQuery):
                    """
                    SENSe:POWer:BURSt:LENGth

                    Arguments:
                    """
                    _cmd = "LENGth"
                    args = []

                LENGth = LENGth()
                """
                SENSe:POWer:BURSt:LENGth

                Arguments:
                """

            BURSt = BURSt()
            """
            SENSe:POWer:BURSt

            Arguments:
            """

            class TSLot(SCPINode):
                """
                SENSe:POWer:TSLot

                Arguments:
                """
                _cmd = "TSLot"
                args = []

                class AVG(SCPINode):
                    """
                    SENSe:POWer:TSLot:AVG

                    Arguments:
                    """
                    _cmd = "AVG"
                    args = []

                    class COUNt(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:POWer:TSLot:AVG:COUNt

                        Arguments: 1
                        """
                        _cmd = "COUNt"
                        args = ["1"]

                    COUNt = COUNt()
                    """
                    SENSe:POWer:TSLot:AVG:COUNt

                    Arguments: 1
                    """

                    class EXCLude(SCPINode):
                        """
                        SENSe:POWer:TSLot:AVG:EXCLude

                        Arguments:
                        """
                        _cmd = "EXCLude"
                        args = []

                        class MID(SCPINode):
                            """
                            SENSe:POWer:TSLot:AVG:EXCLude:MID

                            Arguments:
                            """
                            _cmd = "MID"
                            args = []

                            class OFFSet(SCPINode):
                                """
                                SENSe:POWer:TSLot:AVG:EXCLude:MID:OFFSet

                                Arguments:
                                """
                                _cmd = "OFFSet"
                                args = []

                                class TIME(SCPINode, SCPIQuery, SCPISet):
                                    """
                                    SENSe:POWer:TSLot:AVG:EXCLude:MID:OFFSet:TIME

                                    Arguments: 1
                                    """
                                    _cmd = "TIME"
                                    args = ["1"]

                                TIME = TIME()
                                """
                                SENSe:POWer:TSLot:AVG:EXCLude:MID:OFFSet:TIME

                                Arguments: 1
                                """

                            OFFSet = OFFSet()
                            """
                            SENSe:POWer:TSLot:AVG:EXCLude:MID:OFFSet

                            Arguments:
                            """

                            class STATe(SCPINode, SCPIBool):
                                """
                                SENSe:POWer:TSLot:AVG:EXCLude:MID:STATe

                                Arguments: 1, ON, OFF
                                """
                                _cmd = "STATe"
                                args = ["1", "ON", "OFF"]

                            STATe = STATe()
                            """
                            SENSe:POWer:TSLot:AVG:EXCLude:MID:STATe

                            Arguments: 1, ON, OFF
                            """

                            class TIME(SCPINode, SCPIQuery, SCPISet):
                                """
                                SENSe:POWer:TSLot:AVG:EXCLude:MID:TIME

                                Arguments: 1
                                """
                                _cmd = "TIME"
                                args = ["1"]

                            TIME = TIME()
                            """
                            SENSe:POWer:TSLot:AVG:EXCLude:MID:TIME

                            Arguments: 1
                            """

                        MID = MID()
                        """
                        SENSe:POWer:TSLot:AVG:EXCLude:MID

                        Arguments:
                        """

                    EXCLude = EXCLude()
                    """
                    SENSe:POWer:TSLot:AVG:EXCLude

                    Arguments:
                    """

                    class WIDTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:POWer:TSLot:AVG:WIDTh

                        Arguments: 1
                        """
                        _cmd = "WIDTh"
                        args = ["1"]

                    WIDTh = WIDTh()
                    """
                    SENSe:POWer:TSLot:AVG:WIDTh

                    Arguments: 1
                    """

                AVG = AVG()
                """
                SENSe:POWer:TSLot:AVG

                Arguments:
                """

            TSLot = TSLot()
            """
            SENSe:POWer:TSLot

            Arguments:
            """

        POWer = POWer()
        """
        SENSe:POWer

        Arguments:
        """

        class RANGe(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:RANGe

            Arguments: 0, 1, 2
            """
            _cmd = "RANGe"
            args = ["0", "1", "2"]

            class AUTO(SCPINode, SCPIBool):
                """
                SENSe:RANGe:AUTO

                Arguments: 1, ON, OFF
                """
                _cmd = "AUTO"
                args = ["1", "ON", "OFF"]

            AUTO = AUTO()
            """
            SENSe:RANGe:AUTO

            Arguments: 1, ON, OFF
            """

            class CLEVel(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:RANGe:CLEVel

                Arguments: 1
                """
                _cmd = "CLEVel"
                args = ["1"]

            CLEVel = CLEVel()
            """
            SENSe:RANGe:CLEVel

            Arguments: 1
            """

        RANGe = RANGe()
        """
        SENSe:RANGe

        Arguments: 0, 1, 2
        """

        class SAMPling(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:SAMPling

            Arguments: FREQ1
            """
            _cmd = "SAMPling"
            args = ["FREQ1"]

        SAMPling = SAMPling()
        """
        SENSe:SAMPling

        Arguments: FREQ1
        """

        class SGAMma(SCPINode):
            """
            SENSe:SGAMma

            Arguments:
            """
            _cmd = "SGAMma"
            args = []

            class CORRection(SCPINode):
                """
                SENSe:SGAMma:CORRection

                Arguments:
                """
                _cmd = "CORRection"
                args = []

                class STATe(SCPINode, SCPIBool):
                    """
                    SENSe:SGAMma:CORRection:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SENSe:SGAMma:CORRection:STATe

                Arguments: 1, ON, OFF
                """

            CORRection = CORRection()
            """
            SENSe:SGAMma:CORRection

            Arguments:
            """

            class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SGAMma:MAGNitude

                Arguments: 1
                """
                _cmd = "MAGNitude"
                args = ["1"]

            MAGNitude = MAGNitude()
            """
            SENSe:SGAMma:MAGNitude

            Arguments: 1
            """

            class PHASe(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SGAMma:PHASe

                Arguments: 1
                """
                _cmd = "PHASe"
                args = ["1"]

            PHASe = PHASe()
            """
            SENSe:SGAMma:PHASe

            Arguments: 1
            """

        SGAMma = SGAMma()
        """
        SENSe:SGAMma

        Arguments:
        """

        class TIMing(SCPINode):
            """
            SENSe:TIMing

            Arguments:
            """
            _cmd = "TIMing"
            args = []

            class EXCLude(SCPINode):
                """
                SENSe:TIMing:EXCLude

                Arguments:
                """
                _cmd = "EXCLude"
                args = []

                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TIMing:EXCLude:STARt

                    Arguments: 1
                    """
                    _cmd = "STARt"
                    args = ["1"]

                STARt = STARt()
                """
                SENSe:TIMing:EXCLude:STARt

                Arguments: 1
                """

                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TIMing:EXCLude:STOP

                    Arguments: 1
                    """
                    _cmd = "STOP"
                    args = ["1"]

                STOP = STOP()
                """
                SENSe:TIMing:EXCLude:STOP

                Arguments: 1
                """

            EXCLude = EXCLude()
            """
            SENSe:TIMing:EXCLude

            Arguments:
            """

        TIMing = TIMing()
        """
        SENSe:TIMing

        Arguments:
        """

        class TRACe(SCPINode):
            """
            SENSe:TRACe

            Arguments:
            """
            _cmd = "TRACe"
            args = []

            class AVERage(SCPINode):
                """
                SENSe:TRACe:AVERage

                Arguments:
                """
                _cmd = "AVERage"
                args = []

                class COUNt(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TRACe:AVERage:COUNt

                    Arguments: 1
                    """
                    _cmd = "COUNt"
                    args = ["1"]

                COUNt = COUNt()
                """
                SENSe:TRACe:AVERage:COUNt

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SENSe:TRACe:AVERage:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SENSe:TRACe:AVERage:STATe

                Arguments: 1, ON, OFF
                """

                class TCONtrol(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TRACe:AVERage:TCONtrol

                    Arguments: MOVing, REPeat
                    """
                    _cmd = "TCONtrol"
                    args = ["MOVing", "REPeat"]

                TCONtrol = TCONtrol()
                """
                SENSe:TRACe:AVERage:TCONtrol

                Arguments: MOVing, REPeat
                """

            AVERage = AVERage()
            """
            SENSe:TRACe:AVERage

            Arguments:
            """

            class DATA(SCPINode, SCPIQuery):
                """
                SENSe:TRACe:DATA

                Arguments:
                """
                _cmd = "DATA"
                args = []

            DATA = DATA()
            """
            SENSe:TRACe:DATA

            Arguments:
            """

            class MPWidth(SCPINode, SCPIQuery):
                """
                SENSe:TRACe:MPWidth

                Arguments:
                """
                _cmd = "MPWidth"
                args = []

            MPWidth = MPWidth()
            """
            SENSe:TRACe:MPWidth

            Arguments:
            """

            class OFFSet(SCPINode):
                """
                SENSe:TRACe:OFFSet

                Arguments:
                """
                _cmd = "OFFSet"
                args = []

                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TRACe:OFFSet:TIME

                    Arguments: 1
                    """
                    _cmd = "TIME"
                    args = ["1"]

                TIME = TIME()
                """
                SENSe:TRACe:OFFSet:TIME

                Arguments: 1
                """

            OFFSet = OFFSet()
            """
            SENSe:TRACe:OFFSet

            Arguments:
            """

            class POINts(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:TRACe:POINts

                Arguments: 1
                """
                _cmd = "POINts"
                args = ["1"]

            POINts = POINts()
            """
            SENSe:TRACe:POINts

            Arguments: 1
            """

            class REALtime(SCPINode, SCPIBool):
                """
                SENSe:TRACe:REALtime

                Arguments: 1, ON, OFF
                """
                _cmd = "REALtime"
                args = ["1", "ON", "OFF"]

            REALtime = REALtime()
            """
            SENSe:TRACe:REALtime

            Arguments: 1, ON, OFF
            """

            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:TRACe:TIME

                Arguments: 1
                """
                _cmd = "TIME"
                args = ["1"]

            TIME = TIME()
            """
            SENSe:TRACe:TIME

            Arguments: 1
            """

        TRACe = TRACe()
        """
        SENSe:TRACe

        Arguments:
        """

    SENSe = SENSe()
    """
    SENSe

    Arguments:
    """

    class STATus(SCPINode):
        """
        STATus

        Arguments:
        """
        _cmd = "STATus"
        args = []

        class DEVice(SCPINode):
            """
            STATus:DEVice

            Arguments:
            """
            _cmd = "DEVice"
            args = []

            class CONDition(SCPINode, SCPIQuery):
                """
                STATus:DEVice:CONDition

                Arguments:
                """
                _cmd = "CONDition"
                args = []

            CONDition = CONDition()
            """
            STATus:DEVice:CONDition

            Arguments:
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:DEVice:ENABle

                Arguments: 1
                """
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()
            """
            STATus:DEVice:ENABle

            Arguments: 1
            """

            class EVENt(SCPINode, SCPIQuery):
                """
                STATus:DEVice:EVENt

                Arguments:
                """
                _cmd = "EVENt"
                args = []

            EVENt = EVENt()
            """
            STATus:DEVice:EVENt

            Arguments:
            """

            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:DEVice:NTRansition

                Arguments: 1
                """
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()
            """
            STATus:DEVice:NTRansition

            Arguments: 1
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:DEVice:PTRansition

                Arguments: 1
                """
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()
            """
            STATus:DEVice:PTRansition

            Arguments: 1
            """

        DEVice = DEVice()
        """
        STATus:DEVice

        Arguments:
        """

        class OPERation(SCPINode):
            """
            STATus:OPERation

            Arguments:
            """
            _cmd = "OPERation"
            args = []

            class CALibrating(SCPINode):
                """
                STATus:OPERation:CALibrating

                Arguments:
                """
                _cmd = "CALibrating"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:CALibrating:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:OPERation:CALibrating:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:CALibrating:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:OPERation:CALibrating:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:CALibrating:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:OPERation:CALibrating:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:CALibrating:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:OPERation:CALibrating:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:CALibrating:SUMMary

                    Arguments:
                    """
                    _cmd = "SUMMary"
                    args = []

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:CALibrating:SUMMary:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:OPERation:CALibrating:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()
                """
                STATus:OPERation:CALibrating:SUMMary

                Arguments:
                """

            CALibrating = CALibrating()
            """
            STATus:OPERation:CALibrating

            Arguments:
            """

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

            class LLFail(SCPINode):
                """
                STATus:OPERation:LLFail

                Arguments:
                """
                _cmd = "LLFail"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:LLFail:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:OPERation:LLFail:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:LLFail:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:OPERation:LLFail:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:LLFail:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:OPERation:LLFail:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:LLFail:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:OPERation:LLFail:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:LLFail:SUMMary

                    Arguments:
                    """
                    _cmd = "SUMMary"
                    args = []

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:LLFail:SUMMary:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:OPERation:LLFail:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()
                """
                STATus:OPERation:LLFail:SUMMary

                Arguments:
                """

            LLFail = LLFail()
            """
            STATus:OPERation:LLFail

            Arguments:
            """

            class MEASuring(SCPINode):
                """
                STATus:OPERation:MEASuring

                Arguments:
                """
                _cmd = "MEASuring"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:MEASuring:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:OPERation:MEASuring:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:MEASuring:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:OPERation:MEASuring:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:MEASuring:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:OPERation:MEASuring:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:MEASuring:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:OPERation:MEASuring:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:MEASuring:SUMMary

                    Arguments:
                    """
                    _cmd = "SUMMary"
                    args = []

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:MEASuring:SUMMary:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:OPERation:MEASuring:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()
                """
                STATus:OPERation:MEASuring:SUMMary

                Arguments:
                """

            MEASuring = MEASuring()
            """
            STATus:OPERation:MEASuring

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

            class SENSe(SCPINode):
                """
                STATus:OPERation:SENSe

                Arguments:
                """
                _cmd = "SENSe"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:SENSe:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:OPERation:SENSe:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:SENSe:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:OPERation:SENSe:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:SENSe:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:OPERation:SENSe:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:SENSe:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:OPERation:SENSe:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:SENSe:SUMMary

                    Arguments:
                    """
                    _cmd = "SUMMary"
                    args = []

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:SENSe:SUMMary:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:OPERation:SENSe:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()
                """
                STATus:OPERation:SENSe:SUMMary

                Arguments:
                """

            SENSe = SENSe()
            """
            STATus:OPERation:SENSe

            Arguments:
            """

            class TRIGger(SCPINode):
                """
                STATus:OPERation:TRIGger

                Arguments:
                """
                _cmd = "TRIGger"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:TRIGger:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:OPERation:TRIGger:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:TRIGger:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:OPERation:TRIGger:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:TRIGger:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:OPERation:TRIGger:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:TRIGger:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:OPERation:TRIGger:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:TRIGger:SUMMary

                    Arguments:
                    """
                    _cmd = "SUMMary"
                    args = []

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:TRIGger:SUMMary:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:OPERation:TRIGger:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()
                """
                STATus:OPERation:TRIGger:SUMMary

                Arguments:
                """

            TRIGger = TRIGger()
            """
            STATus:OPERation:TRIGger

            Arguments:
            """

            class ULFail(SCPINode):
                """
                STATus:OPERation:ULFail

                Arguments:
                """
                _cmd = "ULFail"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:ULFail:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:OPERation:ULFail:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:ULFail:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:OPERation:ULFail:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:ULFail:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:OPERation:ULFail:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:ULFail:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:OPERation:ULFail:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:ULFail:SUMMary

                    Arguments:
                    """
                    _cmd = "SUMMary"
                    args = []

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:ULFail:SUMMary:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:OPERation:ULFail:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()
                """
                STATus:OPERation:ULFail:SUMMary

                Arguments:
                """

            ULFail = ULFail()
            """
            STATus:OPERation:ULFail

            Arguments:
            """

        OPERation = OPERation()
        """
        STATus:OPERation

        Arguments:
        """

        class PRESet(SCPINode, SCPISet):
            """
            STATus:PRESet

            Arguments:
            """
            _cmd = "PRESet"
            args = []

        PRESet = PRESet()
        """
        STATus:PRESet

        Arguments:
        """

        class QUEStionable(SCPINode):
            """
            STATus:QUEStionable

            Arguments:
            """
            _cmd = "QUEStionable"
            args = []

            class CALibration(SCPINode):
                """
                STATus:QUEStionable:CALibration

                Arguments:
                """
                _cmd = "CALibration"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:CALibration:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:QUEStionable:CALibration:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:CALibration:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:QUEStionable:CALibration:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:CALibration:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:QUEStionable:CALibration:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:CALibration:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:QUEStionable:CALibration:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:QUEStionable:CALibration:SUMMary

                    Arguments:
                    """
                    _cmd = "SUMMary"
                    args = []

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:QUEStionable:CALibration:SUMMary:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:QUEStionable:CALibration:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()
                """
                STATus:QUEStionable:CALibration:SUMMary

                Arguments:
                """

            CALibration = CALibration()
            """
            STATus:QUEStionable:CALibration

            Arguments:
            """

            class CONDition(SCPINode, SCPIQuery):
                """
                STATus:QUEStionable:CONDition

                Arguments:
                """
                _cmd = "CONDition"
                args = []

            CONDition = CONDition()
            """
            STATus:QUEStionable:CONDition

            Arguments:
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:ENABle

                Arguments: 1
                """
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()
            """
            STATus:QUEStionable:ENABle

            Arguments: 1
            """

            class EVENt(SCPINode, SCPIQuery):
                """
                STATus:QUEStionable:EVENt

                Arguments:
                """
                _cmd = "EVENt"
                args = []

            EVENt = EVENt()
            """
            STATus:QUEStionable:EVENt

            Arguments:
            """

            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:NTRansition

                Arguments: 1
                """
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()
            """
            STATus:QUEStionable:NTRansition

            Arguments: 1
            """

            class POWer(SCPINode):
                """
                STATus:QUEStionable:POWer

                Arguments:
                """
                _cmd = "POWer"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:POWer:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:QUEStionable:POWer:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:POWer:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:QUEStionable:POWer:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:POWer:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:QUEStionable:POWer:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:POWer:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:QUEStionable:POWer:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:QUEStionable:POWer:SUMMary

                    Arguments:
                    """
                    _cmd = "SUMMary"
                    args = []

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:QUEStionable:POWer:SUMMary:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:QUEStionable:POWer:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()
                """
                STATus:QUEStionable:POWer:SUMMary

                Arguments:
                """

            POWer = POWer()
            """
            STATus:QUEStionable:POWer

            Arguments:
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:PTRansition

                Arguments: 1
                """
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()
            """
            STATus:QUEStionable:PTRansition

            Arguments: 1
            """

            class WINDow(SCPINode):
                """
                STATus:QUEStionable:WINDow

                Arguments:
                """
                _cmd = "WINDow"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:WINDow:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:QUEStionable:WINDow:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:WINDow:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:QUEStionable:WINDow:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:WINDow:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:QUEStionable:WINDow:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:WINDow:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:QUEStionable:WINDow:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:QUEStionable:WINDow:SUMMary

                    Arguments:
                    """
                    _cmd = "SUMMary"
                    args = []

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:QUEStionable:WINDow:SUMMary:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:QUEStionable:WINDow:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()
                """
                STATus:QUEStionable:WINDow:SUMMary

                Arguments:
                """

            WINDow = WINDow()
            """
            STATus:QUEStionable:WINDow

            Arguments:
            """

        QUEStionable = QUEStionable()
        """
        STATus:QUEStionable

        Arguments:
        """

        class QUEue(SCPINode):
            """
            STATus:QUEue

            Arguments:
            """
            _cmd = "QUEue"
            args = []

            class NEXT(SCPINode, SCPIQuery):
                """
                STATus:QUEue:NEXT

                Arguments:
                """
                _cmd = "NEXT"
                args = []

            NEXT = NEXT()
            """
            STATus:QUEue:NEXT

            Arguments:
            """

        QUEue = QUEue()
        """
        STATus:QUEue

        Arguments:
        """

    STATus = STATus()
    """
    STATus

    Arguments:
    """

    class SYSTem(SCPINode):
        """
        SYSTem

        Arguments:
        """
        _cmd = "SYSTem"
        args = []

        class CLOCk(SCPINode):
            """
            SYSTem:CLOCk

            Arguments:
            """
            _cmd = "CLOCk"
            args = []

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:CLOCk:SOURce

                Arguments: EXTernal, INTernal
                """
                _cmd = "SOURce"
                args = ["EXTernal", "INTernal"]

            SOURce = SOURce()
            """
            SYSTem:CLOCk:SOURce

            Arguments: EXTernal, INTernal
            """

        CLOCk = CLOCk()
        """
        SYSTem:CLOCk

        Arguments:
        """

        class COMMunicate(SCPINode):
            """
            SYSTem:COMMunicate

            Arguments:
            """
            _cmd = "COMMunicate"
            args = []

            class NETWork(SCPINode):
                """
                SYSTem:COMMunicate:NETWork

                Arguments:
                """
                _cmd = "NETWork"
                args = []

                class COMMon(SCPINode):
                    """
                    SYSTem:COMMunicate:NETWork:COMMon

                    Arguments:
                    """
                    _cmd = "COMMon"
                    args = []

                    class DOMain(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:NETWork:COMMon:DOMain

                        Arguments: 'string'
                        """
                        _cmd = "DOMain"
                        args = ["'string'"]

                    DOMain = DOMain()
                    """
                    SYSTem:COMMunicate:NETWork:COMMon:DOMain

                    Arguments: 'string'
                    """

                    class HOSTname(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:NETWork:COMMon:HOSTname

                        Arguments: 'string'
                        """
                        _cmd = "HOSTname"
                        args = ["'string'"]

                    HOSTname = HOSTname()
                    """
                    SYSTem:COMMunicate:NETWork:COMMon:HOSTname

                    Arguments: 'string'
                    """

                COMMon = COMMon()
                """
                SYSTem:COMMunicate:NETWork:COMMon

                Arguments:
                """

                class IPADdress(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress

                    Arguments: 'string'
                    """
                    _cmd = "IPADdress"
                    args = ["'string'"]

                    class GATeway(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:GATeway

                        Arguments: 'string'
                        """
                        _cmd = "GATeway"
                        args = ["'string'"]

                    GATeway = GATeway()
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress:GATeway

                    Arguments: 'string'
                    """

                    class INFO(SCPINode, SCPIQuery):
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:INFO

                        Arguments:
                        """
                        _cmd = "INFO"
                        args = []

                    INFO = INFO()
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress:INFO

                    Arguments:
                    """

                    class MODE(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:MODE

                        Arguments: AUTO, STATic
                        """
                        _cmd = "MODE"
                        args = ["AUTO", "STATic"]

                    MODE = MODE()
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress:MODE

                    Arguments: AUTO, STATic
                    """

                    class SUBNet(SCPINode):
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:SUBNet

                        Arguments:
                        """
                        _cmd = "SUBNet"
                        args = []

                        class MASK(SCPINode, SCPIQuery, SCPISet):
                            """
                            SYSTem:COMMunicate:NETWork:IPADdress:SUBNet:MASK

                            Arguments: 'string'
                            """
                            _cmd = "MASK"
                            args = ["'string'"]

                        MASK = MASK()
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:SUBNet:MASK

                        Arguments: 'string'
                        """

                    SUBNet = SUBNet()
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress:SUBNet

                    Arguments:
                    """

                IPADdress = IPADdress()
                """
                SYSTem:COMMunicate:NETWork:IPADdress

                Arguments: 'string'
                """

                class RESTart(SCPINode, SCPISet):
                    """
                    SYSTem:COMMunicate:NETWork:RESTart

                    Arguments:
                    """
                    _cmd = "RESTart"
                    args = []

                RESTart = RESTart()
                """
                SYSTem:COMMunicate:NETWork:RESTart

                Arguments:
                """

                class RESet(SCPINode, SCPISet):
                    """
                    SYSTem:COMMunicate:NETWork:RESet

                    Arguments:
                    """
                    _cmd = "RESet"
                    args = []

                RESet = RESet()
                """
                SYSTem:COMMunicate:NETWork:RESet

                Arguments:
                """

                class STATus(SCPINode, SCPIQuery):
                    """
                    SYSTem:COMMunicate:NETWork:STATus

                    Arguments:
                    """
                    _cmd = "STATus"
                    args = []

                STATus = STATus()
                """
                SYSTem:COMMunicate:NETWork:STATus

                Arguments:
                """

            NETWork = NETWork()
            """
            SYSTem:COMMunicate:NETWork

            Arguments:
            """

        COMMunicate = COMMunicate()
        """
        SYSTem:COMMunicate

        Arguments:
        """

        class DFPRint(SCPINode, SCPIQuery):
            """
            SYSTem:DFPRint

            Arguments:
            """
            _cmd = "DFPRint"
            args = []

        DFPRint = DFPRint()
        """
        SYSTem:DFPRint

        Arguments:
        """

        class ERRor(SCPINode):
            """
            SYSTem:ERRor

            Arguments:
            """
            _cmd = "ERRor"
            args = []

            class ALL(SCPINode, SCPIQuery):
                """
                SYSTem:ERRor:ALL

                Arguments:
                """
                _cmd = "ALL"
                args = []

            ALL = ALL()
            """
            SYSTem:ERRor:ALL

            Arguments:
            """

            class CODE(SCPINode):
                """
                SYSTem:ERRor:CODE

                Arguments:
                """
                _cmd = "CODE"
                args = []

                class ALL(SCPINode, SCPIQuery):
                    """
                    SYSTem:ERRor:CODE:ALL

                    Arguments:
                    """
                    _cmd = "ALL"
                    args = []

                ALL = ALL()
                """
                SYSTem:ERRor:CODE:ALL

                Arguments:
                """

                class NEXT(SCPINode, SCPIQuery):
                    """
                    SYSTem:ERRor:CODE:NEXT

                    Arguments:
                    """
                    _cmd = "NEXT"
                    args = []

                NEXT = NEXT()
                """
                SYSTem:ERRor:CODE:NEXT

                Arguments:
                """

            CODE = CODE()
            """
            SYSTem:ERRor:CODE

            Arguments:
            """

            class COUNt(SCPINode, SCPIQuery):
                """
                SYSTem:ERRor:COUNt

                Arguments:
                """
                _cmd = "COUNt"
                args = []

            COUNt = COUNt()
            """
            SYSTem:ERRor:COUNt

            Arguments:
            """

            class NEXT(SCPINode, SCPIQuery):
                """
                SYSTem:ERRor:NEXT

                Arguments:
                """
                _cmd = "NEXT"
                args = []

            NEXT = NEXT()
            """
            SYSTem:ERRor:NEXT

            Arguments:
            """

        ERRor = ERRor()
        """
        SYSTem:ERRor

        Arguments:
        """

        class FEATures(SCPINode, SCPIQuery):
            """
            SYSTem:FEATures

            Arguments: 1
            """
            _cmd = "FEATures"
            args = ["1"]

        FEATures = FEATures()
        """
        SYSTem:FEATures

        Arguments: 1
        """

        class FWUPdate(SCPINode, SCPISet):
            """
            SYSTem:FWUPdate

            Arguments: <block_data>
            """
            _cmd = "FWUPdate"
            args = ["<block_data>"]

            class STATus(SCPINode, SCPIQuery):
                """
                SYSTem:FWUPdate:STATus

                Arguments:
                """
                _cmd = "STATus"
                args = []

            STATus = STATus()
            """
            SYSTem:FWUPdate:STATus

            Arguments:
            """

        FWUPdate = FWUPdate()
        """
        SYSTem:FWUPdate

        Arguments: <block_data>
        """

        class HELP(SCPINode):
            """
            SYSTem:HELP

            Arguments:
            """
            _cmd = "HELP"
            args = []

            class HEADers(SCPINode, SCPIQuery):
                """
                SYSTem:HELP:HEADers

                Arguments:
                """
                _cmd = "HEADers"
                args = []

            HEADers = HEADers()
            """
            SYSTem:HELP:HEADers

            Arguments:
            """

            class SYNTax(SCPINode, SCPIQuery):
                """
                SYSTem:HELP:SYNTax

                Arguments: 'string'
                """
                _cmd = "SYNTax"
                args = ["'string'"]

                class ALL(SCPINode, SCPIQuery):
                    """
                    SYSTem:HELP:SYNTax:ALL

                    Arguments:
                    """
                    _cmd = "ALL"
                    args = []

                ALL = ALL()
                """
                SYSTem:HELP:SYNTax:ALL

                Arguments:
                """

            SYNTax = SYNTax()
            """
            SYSTem:HELP:SYNTax

            Arguments: 'string'
            """

        HELP = HELP()
        """
        SYSTem:HELP

        Arguments:
        """

        class INFO(SCPINode, SCPIQuery):
            """
            SYSTem:INFO

            Arguments: 'string'
            """
            _cmd = "INFO"
            args = ["'string'"]

        INFO = INFO()
        """
        SYSTem:INFO

        Arguments: 'string'
        """

        class INITialize(SCPINode, SCPISet):
            """
            SYSTem:INITialize

            Arguments:
            """
            _cmd = "INITialize"
            args = []

        INITialize = INITialize()
        """
        SYSTem:INITialize

        Arguments:
        """

        class LANGuage(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:LANGuage

            Arguments: SCPI
            """
            _cmd = "LANGuage"
            args = ["SCPI"]

        LANGuage = LANGuage()
        """
        SYSTem:LANGuage

        Arguments: SCPI
        """

        class LED(SCPINode):
            """
            SYSTem:LED

            Arguments:
            """
            _cmd = "LED"
            args = []

            class COLor(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:LED:COLor

                Arguments: 1
                """
                _cmd = "COLor"
                args = ["1"]

            COLor = COLor()
            """
            SYSTem:LED:COLor

            Arguments: 1
            """

            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:LED:MODE

                Arguments: SENSor, USER
                """
                _cmd = "MODE"
                args = ["SENSor", "USER"]

            MODE = MODE()
            """
            SYSTem:LED:MODE

            Arguments: SENSor, USER
            """

        LED = LED()
        """
        SYSTem:LED

        Arguments:
        """

        class LIMits(SCPINode, SCPIQuery):
            """
            SYSTem:LIMits

            Arguments: 1
            """
            _cmd = "LIMits"
            args = ["1"]

        LIMits = LIMits()
        """
        SYSTem:LIMits

        Arguments: 1
        """

        class MINPower(SCPINode, SCPIQuery):
            """
            SYSTem:MINPower

            Arguments:
            """
            _cmd = "MINPower"
            args = []

        MINPower = MINPower()
        """
        SYSTem:MINPower

        Arguments:
        """

        class PRESet(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:PRESet

            Arguments:
            """
            _cmd = "PRESet"
            args = []

        PRESet = PRESet()
        """
        SYSTem:PRESet

        Arguments:
        """

        class REBoot(SCPINode, SCPISet):
            """
            SYSTem:REBoot

            Arguments:
            """
            _cmd = "REBoot"
            args = []

        REBoot = REBoot()
        """
        SYSTem:REBoot

        Arguments:
        """

        class RUTime(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:RUTime

            Arguments: 1
            """
            _cmd = "RUTime"
            args = ["1"]

        RUTime = RUTime()
        """
        SYSTem:RUTime

        Arguments: 1
        """

        class SENSor(SCPINode):
            """
            SYSTem:SENSor

            Arguments:
            """
            _cmd = "SENSor"
            args = []

            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:SENSor:NAME

                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]

            NAME = NAME()
            """
            SYSTem:SENSor:NAME

            Arguments: 'string'
            """

        SENSor = SENSor()
        """
        SYSTem:SENSor

        Arguments:
        """

        class SERRor(SCPINode, SCPIQuery):
            """
            SYSTem:SERRor

            Arguments:
            """
            _cmd = "SERRor"
            args = []

            class LIST(SCPINode):
                """
                SYSTem:SERRor:LIST

                Arguments:
                """
                _cmd = "LIST"
                args = []

                class ALL(SCPINode, SCPIQuery):
                    """
                    SYSTem:SERRor:LIST:ALL

                    Arguments:
                    """
                    _cmd = "ALL"
                    args = []

                ALL = ALL()
                """
                SYSTem:SERRor:LIST:ALL

                Arguments:
                """

                class NEXT(SCPINode, SCPIQuery):
                    """
                    SYSTem:SERRor:LIST:NEXT

                    Arguments:
                    """
                    _cmd = "NEXT"
                    args = []

                NEXT = NEXT()
                """
                SYSTem:SERRor:LIST:NEXT

                Arguments:
                """

            LIST = LIST()
            """
            SYSTem:SERRor:LIST

            Arguments:
            """

        SERRor = SERRor()
        """
        SYSTem:SERRor

        Arguments:
        """

        class SUTime(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:SUTime

            Arguments: 1
            """
            _cmd = "SUTime"
            args = ["1"]

        SUTime = SUTime()
        """
        SYSTem:SUTime

        Arguments: 1
        """

        class TLEVels(SCPINode, SCPIQuery):
            """
            SYSTem:TLEVels

            Arguments:
            """
            _cmd = "TLEVels"
            args = []

        TLEVels = TLEVels()
        """
        SYSTem:TLEVels

        Arguments:
        """

        class TRANsaction(SCPINode):
            """
            SYSTem:TRANsaction

            Arguments:
            """
            _cmd = "TRANsaction"
            args = []

            class BEGin(SCPINode, SCPISet):
                """
                SYSTem:TRANsaction:BEGin

                Arguments:
                """
                _cmd = "BEGin"
                args = []

            BEGin = BEGin()
            """
            SYSTem:TRANsaction:BEGin

            Arguments:
            """

            class END(SCPINode, SCPISet):
                """
                SYSTem:TRANsaction:END

                Arguments:
                """
                _cmd = "END"
                args = []

            END = END()
            """
            SYSTem:TRANsaction:END

            Arguments:
            """

        TRANsaction = TRANsaction()
        """
        SYSTem:TRANsaction

        Arguments:
        """

        class VERSion(SCPINode, SCPIQuery):
            """
            SYSTem:VERSion

            Arguments:
            """
            _cmd = "VERSion"
            args = []

        VERSion = VERSion()
        """
        SYSTem:VERSion

        Arguments:
        """

    SYSTem = SYSTem()
    """
    SYSTem

    Arguments:
    """

    class TEST(SCPINode):
        """
        TEST

        Arguments:
        """
        _cmd = "TEST"
        args = []

        class SENSor(SCPINode, SCPIQuery):
            """
            TEST:SENSor

            Arguments: 'string'
            """
            _cmd = "SENSor"
            args = ["'string'"]

        SENSor = SENSor()
        """
        TEST:SENSor

        Arguments: 'string'
        """

    TEST = TEST()
    """
    TEST

    Arguments:
    """

    class TRIGger(SCPINode):
        """
        TRIGger

        Arguments:
        """
        _cmd = "TRIGger"
        args = []

        class ATRigger(SCPINode):
            """
            TRIGger:ATRigger

            Arguments:
            """
            _cmd = "ATRigger"
            args = []

            class DELay(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:ATRigger:DELay

                Arguments: 1
                """
                _cmd = "DELay"
                args = ["1"]

            DELay = DELay()
            """
            TRIGger:ATRigger:DELay

            Arguments: 1
            """

            class EXECuted(SCPINode, SCPIQuery):
                """
                TRIGger:ATRigger:EXECuted

                Arguments:
                """
                _cmd = "EXECuted"
                args = []

            EXECuted = EXECuted()
            """
            TRIGger:ATRigger:EXECuted

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                TRIGger:ATRigger:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            TRIGger:ATRigger:STATe

            Arguments: 1, ON, OFF
            """

        ATRigger = ATRigger()
        """
        TRIGger:ATRigger

        Arguments:
        """

        class COUNt(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:COUNt

            Arguments: 1
            """
            _cmd = "COUNt"
            args = ["1"]

        COUNt = COUNt()
        """
        TRIGger:COUNt

        Arguments: 1
        """

        class DELay(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:DELay

            Arguments: 1
            """
            _cmd = "DELay"
            args = ["1"]

            class AUTO(SCPINode, SCPIBool):
                """
                TRIGger:DELay:AUTO

                Arguments: 1, ON, OFF
                """
                _cmd = "AUTO"
                args = ["1", "ON", "OFF"]

            AUTO = AUTO()
            """
            TRIGger:DELay:AUTO

            Arguments: 1, ON, OFF
            """

        DELay = DELay()
        """
        TRIGger:DELay

        Arguments: 1
        """

        class DTIMe(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:DTIMe

            Arguments: 1
            """
            _cmd = "DTIMe"
            args = ["1"]

        DTIMe = DTIMe()
        """
        TRIGger:DTIMe

        Arguments: 1
        """

        class EXTernal(SCPINodeN):
            """
            TRIGger:EXTernal

            Arguments:
            """
            _cmd = "EXTernal"
            args = []

            class IMPedance(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:EXTernal:IMPedance

                Arguments: HIGH, LOW
                """
                _cmd = "IMPedance"
                args = ["HIGH", "LOW"]

            IMPedance = IMPedance()
            """
            TRIGger:EXTernal:IMPedance

            Arguments: HIGH, LOW
            """

        EXTernal = EXTernal()
        """
        TRIGger:EXTernal

        Arguments:
        """

        class HOLDoff(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:HOLDoff

            Arguments: 1
            """
            _cmd = "HOLDoff"
            args = ["1"]

        HOLDoff = HOLDoff()
        """
        TRIGger:HOLDoff

        Arguments: 1
        """

        class HYSTeresis(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:HYSTeresis

            Arguments: 1
            """
            _cmd = "HYSTeresis"
            args = ["1"]

        HYSTeresis = HYSTeresis()
        """
        TRIGger:HYSTeresis

        Arguments: 1
        """

        class IMMediate(SCPINode, SCPISet):
            """
            TRIGger:IMMediate

            Arguments:
            """
            _cmd = "IMMediate"
            args = []

        IMMediate = IMMediate()
        """
        TRIGger:IMMediate

        Arguments:
        """

        class LEVel(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:LEVel

            Arguments: 1
            """
            _cmd = "LEVel"
            args = ["1"]

        LEVel = LEVel()
        """
        TRIGger:LEVel

        Arguments: 1
        """

        class MASTer(SCPINode):
            """
            TRIGger:MASTer

            Arguments:
            """
            _cmd = "MASTer"
            args = []

            class PORT(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:MASTer:PORT

                Arguments: EXT1, EXT2, EXTernal1, EXTernal2
                """
                _cmd = "PORT"
                args = ["EXT1", "EXT2", "EXTernal1", "EXTernal2"]

            PORT = PORT()
            """
            TRIGger:MASTer:PORT

            Arguments: EXT1, EXT2, EXTernal1, EXTernal2
            """

            class STATe(SCPINode, SCPIBool):
                """
                TRIGger:MASTer:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            TRIGger:MASTer:STATe

            Arguments: 1, ON, OFF
            """

        MASTer = MASTer()
        """
        TRIGger:MASTer

        Arguments:
        """

        class SLOPe(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:SLOPe

            Arguments: NEGative, POSitive
            """
            _cmd = "SLOPe"
            args = ["NEGative", "POSitive"]

        SLOPe = SLOPe()
        """
        TRIGger:SLOPe

        Arguments: NEGative, POSitive
        """

        class SOURce(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:SOURce

            Arguments: BUS, EXT1, EXT2, EXTernal, EXTernal1, EXTernal2, HOLD, IMMediate, INTernal
            """
            _cmd = "SOURce"
            args = ["BUS", "EXT1", "EXT2", "EXTernal", "EXTernal1", "EXTernal2", "HOLD", "IMMediate", "INTernal"]

        SOURce = SOURce()
        """
        TRIGger:SOURce

        Arguments: BUS, EXT1, EXT2, EXTernal, EXTernal1, EXTernal2, HOLD, IMMediate, INTernal
        """

        class SYNC(SCPINode):
            """
            TRIGger:SYNC

            Arguments:
            """
            _cmd = "SYNC"
            args = []

            class PORT(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:SYNC:PORT

                Arguments: EXT1, EXT2, EXTernal1, EXTernal2
                """
                _cmd = "PORT"
                args = ["EXT1", "EXT2", "EXTernal1", "EXTernal2"]

            PORT = PORT()
            """
            TRIGger:SYNC:PORT

            Arguments: EXT1, EXT2, EXTernal1, EXTernal2
            """

            class STATe(SCPINode, SCPIBool):
                """
                TRIGger:SYNC:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            TRIGger:SYNC:STATe

            Arguments: 1, ON, OFF
            """

        SYNC = SYNC()
        """
        TRIGger:SYNC

        Arguments:
        """

    TRIGger = TRIGger()
    """
    TRIGger

    Arguments:
    """

    class UNIT(SCPINode):
        """
        UNIT

        Arguments:
        """
        _cmd = "UNIT"
        args = []

        class POWer(SCPINode, SCPIQuery, SCPISet):
            """
            UNIT:POWer

            Arguments: DBM, DBUV, W
            """
            _cmd = "POWer"
            args = ["DBM", "DBUV", "W"]

        POWer = POWer()
        """
        UNIT:POWer

        Arguments: DBM, DBUV, W
        """

    UNIT = UNIT()
    """
    UNIT

    Arguments:
    """

    # END OF NRPxxSN_gen
