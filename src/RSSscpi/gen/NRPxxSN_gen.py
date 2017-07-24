# -*- coding: utf-8 -*-
# Generated from NRPxxSN_rev07.txt on 2017-07-24 19:18
from RSSscpi.SCPI_gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool
from RSSscpi.Instrument import Instrument


class NRPxxSN_gen(Instrument):
    class CLS(SCPINode, SCPIQuery, SCPISet):
        """
        *CLS

        Arguments: 1
        """
        _cmd = "*CLS"
        args = ["1"]

    CLS = CLS()
    """
    *CLS

    Arguments: 1
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

        Arguments: 1
        """
        _cmd = "*OPC"
        args = ["1"]

    OPC = OPC()
    """
    *OPC

    Arguments: 1
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

    class RCL(SCPINode, SCPIQuery, SCPISet):
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

    class RST(SCPINode, SCPIQuery, SCPISet):
        """
        *RST

        Arguments: 1
        """
        _cmd = "*RST"
        args = ["1"]

    RST = RST()
    """
    *RST

    Arguments: 1
    """

    class SAV(SCPINode, SCPIQuery, SCPISet):
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

    class TRG(SCPINode, SCPIQuery, SCPISet):
        """
        *TRG

        Arguments: 1
        """
        _cmd = "*TRG"
        args = ["1"]

    TRG = TRG()
    """
    *TRG

    Arguments: 1
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

    class WAI(SCPINode, SCPIQuery, SCPISet):
        """
        *WAI

        Arguments: 1
        """
        _cmd = "*WAI"
        args = ["1"]

    WAI = WAI()
    """
    *WAI

    Arguments: 1
    """

    class ABORt(SCPINode, SCPIQuery, SCPISet):
        """
        ABORt

        Arguments: 1
        """
        _cmd = "ABORt"
        args = ["1"]

    ABORt = ABORt()
    """
    ABORt

    Arguments: 1
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

            Arguments: 1
            """
            _cmd = "FEED"
            args = ["1"]

        FEED = FEED()
        """
        CALCulate:FEED

        Arguments: 1
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

            Arguments: 1
            """
            _cmd = "DATA"
            args = ["1"]

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

        Arguments: 1
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

                Arguments: 1
                """
                _cmd = "DATA"
                args = ["1"]

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

            Arguments: 1
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

                Arguments: 1
                """
                _cmd = "AUTO"
                args = ["1"]

            AUTO = AUTO()
            """
            CALibration:ZERO:AUTO

            Arguments: 1
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

    class FETCh(SCPINode, SCPIQuery):
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

            Arguments: 1
            """
            _cmd = "BORDer"
            args = ["1"]

        BORDer = BORDer()
        """
        FORMat:BORDer

        Arguments: 1
        """

        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            FORMat:DATA

            Arguments: 1
            """
            _cmd = "DATA"
            args = ["1"]

        DATA = DATA()
        """
        FORMat:DATA

        Arguments: 1
        """

        class SREGister(SCPINode, SCPIQuery, SCPISet):
            """
            FORMat:SREGister

            Arguments: 1
            """
            _cmd = "SREGister"
            args = ["1"]

        SREGister = SREGister()
        """
        FORMat:SREGister

        Arguments: 1
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

        class CONTinuous(SCPINode, SCPIQuery, SCPISet):
            """
            INITiate:CONTinuous

            Arguments: 1
            """
            _cmd = "CONTinuous"
            args = ["1"]

        CONTinuous = CONTinuous()
        """
        INITiate:CONTinuous

        Arguments: 1
        """

        class IMMediate(SCPINode, SCPIQuery, SCPISet):
            """
            INITiate:IMMediate

            Arguments: 1
            """
            _cmd = "IMMediate"
            args = ["1"]

        IMMediate = IMMediate()
        """
        INITiate:IMMediate

        Arguments: 1
        """

    INITiate = INITiate()
    """
    INITiate

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

            Arguments: 1
            """
            _cmd = "AUXiliary"
            args = ["1"]

        AUXiliary = AUXiliary()
        """
        SENSe:AUXiliary

        Arguments: 1
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

                    Arguments: 1
                    """
                    _cmd = "AUTO"
                    args = ["1"]

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

                        Arguments: 1
                        """
                        _cmd = "TYPE"
                        args = ["1"]

                    TYPE = TYPE()
                    """
                    SENSe:AVERage:COUNt:AUTO:TYPE

                    Arguments: 1
                    """

                AUTO = AUTO()
                """
                SENSe:AVERage:COUNt:AUTO

                Arguments: 1
                """

            COUNt = COUNt()
            """
            SENSe:AVERage:COUNt

            Arguments: 1
            """

            class RESet(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:AVERage:RESet

                Arguments: 1
                """
                _cmd = "RESet"
                args = ["1"]

            RESet = RESet()
            """
            SENSe:AVERage:RESet

            Arguments: 1
            """

            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:AVERage:STATe

                Arguments: 1
                """
                _cmd = "STATe"
                args = ["1"]

            STATe = STATe()
            """
            SENSe:AVERage:STATe

            Arguments: 1
            """

            class TCONtrol(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:AVERage:TCONtrol

                Arguments: 1
                """
                _cmd = "TCONtrol"
                args = ["1"]

            TCONtrol = TCONtrol()
            """
            SENSe:AVERage:TCONtrol

            Arguments: 1
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

                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:DCYCle:STATe

                    Arguments: 1
                    """
                    _cmd = "STATe"
                    args = ["1"]

                STATe = STATe()
                """
                SENSe:CORRection:DCYCle:STATe

                Arguments: 1
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

                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:OFFSet:STATe

                    Arguments: 1
                    """
                    _cmd = "STATe"
                    args = ["1"]

                STATe = STATe()
                """
                SENSe:CORRection:OFFSet:STATe

                Arguments: 1
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

                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:SPDevice:STATe

                    Arguments: 1
                    """
                    _cmd = "STATe"
                    args = ["1"]

                STATe = STATe()
                """
                SENSe:CORRection:SPDevice:STATe

                Arguments: 1
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

            Arguments: 1
            """
            _cmd = "FUNCtion"
            args = ["1"]

        FUNCtion = FUNCtion()
        """
        SENSe:FUNCtion

        Arguments: 1
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

                    class CLEar(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:POWer:AVG:BUFFer:CLEar

                        Arguments: 1
                        """
                        _cmd = "CLEar"
                        args = ["1"]

                    CLEar = CLEar()
                    """
                    SENSe:POWer:AVG:BUFFer:CLEar

                    Arguments: 1
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

                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:POWer:AVG:BUFFer:STATe

                        Arguments: 1
                        """
                        _cmd = "STATe"
                        args = ["1"]

                    STATe = STATe()
                    """
                    SENSe:POWer:AVG:BUFFer:STATe

                    Arguments: 1
                    """

                BUFFer = BUFFer()
                """
                SENSe:POWer:AVG:BUFFer

                Arguments:
                """

                class FAST(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:POWer:AVG:FAST

                    Arguments: 1
                    """
                    _cmd = "FAST"
                    args = ["1"]

                FAST = FAST()
                """
                SENSe:POWer:AVG:FAST

                Arguments: 1
                """

                class SMOothing(SCPINode):
                    """
                    SENSe:POWer:AVG:SMOothing

                    Arguments:
                    """
                    _cmd = "SMOothing"
                    args = []

                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:POWer:AVG:SMOothing:STATe

                        Arguments: 1
                        """
                        _cmd = "STATe"
                        args = ["1"]

                    STATe = STATe()
                    """
                    SENSe:POWer:AVG:SMOothing:STATe

                    Arguments: 1
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

                class CHOPper(SCPINode):
                    """
                    SENSe:POWer:BURSt:CHOPper

                    Arguments:
                    """
                    _cmd = "CHOPper"
                    args = []

                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:POWer:BURSt:CHOPper:STATe

                        Arguments: 1
                        """
                        _cmd = "STATe"
                        args = ["1"]

                    STATe = STATe()
                    """
                    SENSe:POWer:BURSt:CHOPper:STATe

                    Arguments: 1
                    """

                CHOPper = CHOPper()
                """
                SENSe:POWer:BURSt:CHOPper

                Arguments:
                """

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

                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                """
                                SENSe:POWer:TSLot:AVG:EXCLude:MID:STATe

                                Arguments: 1
                                """
                                _cmd = "STATe"
                                args = ["1"]

                            STATe = STATe()
                            """
                            SENSe:POWer:TSLot:AVG:EXCLude:MID:STATe

                            Arguments: 1
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

            Arguments: 1
            """
            _cmd = "RANGe"
            args = ["1"]

            class AUTO(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:RANGe:AUTO

                Arguments: 1
                """
                _cmd = "AUTO"
                args = ["1"]

            AUTO = AUTO()
            """
            SENSe:RANGe:AUTO

            Arguments: 1
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

        Arguments: 1
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

                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:SGAMma:CORRection:STATe

                    Arguments: 1
                    """
                    _cmd = "STATe"
                    args = ["1"]

                STATe = STATe()
                """
                SENSe:SGAMma:CORRection:STATe

                Arguments: 1
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

                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TRACe:AVERage:STATe

                    Arguments: 1
                    """
                    _cmd = "STATe"
                    args = ["1"]

                STATe = STATe()
                """
                SENSe:TRACe:AVERage:STATe

                Arguments: 1
                """

                class TCONtrol(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TRACe:AVERage:TCONtrol

                    Arguments: 1
                    """
                    _cmd = "TCONtrol"
                    args = ["1"]

                TCONtrol = TCONtrol()
                """
                SENSe:TRACe:AVERage:TCONtrol

                Arguments: 1
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

            class REALtime(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:TRACe:REALtime

                Arguments: 1
                """
                _cmd = "REALtime"
                args = ["1"]

            REALtime = REALtime()
            """
            SENSe:TRACe:REALtime

            Arguments: 1
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

        class PRESet(SCPINode, SCPIQuery, SCPISet):
            """
            STATus:PRESet

            Arguments: 1
            """
            _cmd = "PRESet"
            args = ["1"]

        PRESet = PRESet()
        """
        STATus:PRESet

        Arguments: 1
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

                        Arguments: 1
                        """
                        _cmd = "DOMain"
                        args = ["1"]

                    DOMain = DOMain()
                    """
                    SYSTem:COMMunicate:NETWork:COMMon:DOMain

                    Arguments: 1
                    """

                    class HOSTname(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:NETWork:COMMon:HOSTname

                        Arguments: 1
                        """
                        _cmd = "HOSTname"
                        args = ["1"]

                    HOSTname = HOSTname()
                    """
                    SYSTem:COMMunicate:NETWork:COMMon:HOSTname

                    Arguments: 1
                    """

                COMMon = COMMon()
                """
                SYSTem:COMMunicate:NETWork:COMMon

                Arguments:
                """

                class IPADdress(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress

                    Arguments: 1
                    """
                    _cmd = "IPADdress"
                    args = ["1"]

                    class GATeway(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:GATeway

                        Arguments: 1
                        """
                        _cmd = "GATeway"
                        args = ["1"]

                    GATeway = GATeway()
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress:GATeway

                    Arguments: 1
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

                        Arguments: 1
                        """
                        _cmd = "MODE"
                        args = ["1"]

                    MODE = MODE()
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress:MODE

                    Arguments: 1
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

                            Arguments: 1
                            """
                            _cmd = "MASK"
                            args = ["1"]

                        MASK = MASK()
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:SUBNet:MASK

                        Arguments: 1
                        """

                    SUBNet = SUBNet()
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress:SUBNet

                    Arguments:
                    """

                IPADdress = IPADdress()
                """
                SYSTem:COMMunicate:NETWork:IPADdress

                Arguments: 1
                """

                class RESTart(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:NETWork:RESTart

                    Arguments: 1
                    """
                    _cmd = "RESTart"
                    args = ["1"]

                RESTart = RESTart()
                """
                SYSTem:COMMunicate:NETWork:RESTart

                Arguments: 1
                """

                class RESet(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:NETWork:RESet

                    Arguments: 1
                    """
                    _cmd = "RESet"
                    args = ["1"]

                RESet = RESet()
                """
                SYSTem:COMMunicate:NETWork:RESet

                Arguments: 1
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

            Arguments:
            """
            _cmd = "FEATures"
            args = []

        FEATures = FEATures()
        """
        SYSTem:FEATures

        Arguments:
        """

        class FWUPdate(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:FWUPdate

            Arguments: 1
            """
            _cmd = "FWUPdate"
            args = ["1"]

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

        Arguments: 1
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

                Arguments:
                """
                _cmd = "SYNTax"
                args = []

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

            Arguments:
            """

        HELP = HELP()
        """
        SYSTem:HELP

        Arguments:
        """

        class INFO(SCPINode, SCPIQuery):
            """
            SYSTem:INFO

            Arguments:
            """
            _cmd = "INFO"
            args = []

        INFO = INFO()
        """
        SYSTem:INFO

        Arguments:
        """

        class INITialize(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:INITialize

            Arguments: 1
            """
            _cmd = "INITialize"
            args = ["1"]

        INITialize = INITialize()
        """
        SYSTem:INITialize

        Arguments: 1
        """

        class LANGuage(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:LANGuage

            Arguments: 1
            """
            _cmd = "LANGuage"
            args = ["1"]

        LANGuage = LANGuage()
        """
        SYSTem:LANGuage

        Arguments: 1
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

                Arguments: 1
                """
                _cmd = "MODE"
                args = ["1"]

            MODE = MODE()
            """
            SYSTem:LED:MODE

            Arguments: 1
            """

        LED = LED()
        """
        SYSTem:LED

        Arguments:
        """

        class LIMits(SCPINode, SCPIQuery):
            """
            SYSTem:LIMits

            Arguments:
            """
            _cmd = "LIMits"
            args = []

        LIMits = LIMits()
        """
        SYSTem:LIMits

        Arguments:
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

            Arguments: 1
            """
            _cmd = "PRESet"
            args = ["1"]

        PRESet = PRESet()
        """
        SYSTem:PRESet

        Arguments: 1
        """

        class REBoot(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:REBoot

            Arguments: 1
            """
            _cmd = "REBoot"
            args = ["1"]

        REBoot = REBoot()
        """
        SYSTem:REBoot

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

                Arguments: 1
                """
                _cmd = "NAME"
                args = ["1"]

            NAME = NAME()
            """
            SYSTem:SENSor:NAME

            Arguments: 1
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

            class BEGin(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:TRANsaction:BEGin

                Arguments: 1
                """
                _cmd = "BEGin"
                args = ["1"]

            BEGin = BEGin()
            """
            SYSTem:TRANsaction:BEGin

            Arguments: 1
            """

            class END(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:TRANsaction:END

                Arguments: 1
                """
                _cmd = "END"
                args = ["1"]

            END = END()
            """
            SYSTem:TRANsaction:END

            Arguments: 1
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

            Arguments:
            """
            _cmd = "SENSor"
            args = []

        SENSor = SENSor()
        """
        TEST:SENSor

        Arguments:
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

            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:ATRigger:STATe

                Arguments: 1
                """
                _cmd = "STATe"
                args = ["1"]

            STATe = STATe()
            """
            TRIGger:ATRigger:STATe

            Arguments: 1
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

            class AUTO(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:DELay:AUTO

                Arguments: 1
                """
                _cmd = "AUTO"
                args = ["1"]

            AUTO = AUTO()
            """
            TRIGger:DELay:AUTO

            Arguments: 1
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

                Arguments: 1
                """
                _cmd = "IMPedance"
                args = ["1"]

            IMPedance = IMPedance()
            """
            TRIGger:EXTernal:IMPedance

            Arguments: 1
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

        class IMMediate(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:IMMediate

            Arguments: 1
            """
            _cmd = "IMMediate"
            args = ["1"]

        IMMediate = IMMediate()
        """
        TRIGger:IMMediate

        Arguments: 1
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

                Arguments: 1
                """
                _cmd = "PORT"
                args = ["1"]

            PORT = PORT()
            """
            TRIGger:MASTer:PORT

            Arguments: 1
            """

            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:MASTer:STATe

                Arguments: 1
                """
                _cmd = "STATe"
                args = ["1"]

            STATe = STATe()
            """
            TRIGger:MASTer:STATe

            Arguments: 1
            """

        MASTer = MASTer()
        """
        TRIGger:MASTer

        Arguments:
        """

        class SLOPe(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:SLOPe

            Arguments: 1
            """
            _cmd = "SLOPe"
            args = ["1"]

        SLOPe = SLOPe()
        """
        TRIGger:SLOPe

        Arguments: 1
        """

        class SOURce(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:SOURce

            Arguments: 1
            """
            _cmd = "SOURce"
            args = ["1"]

        SOURce = SOURce()
        """
        TRIGger:SOURce

        Arguments: 1
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

                Arguments: 1
                """
                _cmd = "PORT"
                args = ["1"]

            PORT = PORT()
            """
            TRIGger:SYNC:PORT

            Arguments: 1
            """

            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:SYNC:STATe

                Arguments: 1
                """
                _cmd = "STATe"
                args = ["1"]

            STATe = STATe()
            """
            TRIGger:SYNC:STATe

            Arguments: 1
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

            Arguments: 1
            """
            _cmd = "POWer"
            args = ["1"]

        POWer = POWer()
        """
        UNIT:POWer

        Arguments: 1
        """

    UNIT = UNIT()
    """
    UNIT

    Arguments:
    """

    # END OF NRPxxSN_gen
