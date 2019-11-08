# -*- coding: utf-8 -*-
# Generated from NRPxxSN_syntax.txt on 2019-10-18 15:03
from typing import List
from ..scpi.gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool


class NRPxxSN_gen(SCPINode):
    _cmd = ""

    class CLS(SCPINode, SCPISet):
        """
        *CLS

        Arguments:
        """
        __slots__ = ()
        _cmd = "*CLS"
        args = []  # type: List[str]

    CLS = CLS()  # type: ignore
    """
    *CLS

    Arguments:
    """

    class ESE(SCPINode, SCPIQuery, SCPISet):
        """
        *ESE

        Arguments: 1
        """
        __slots__ = ()
        _cmd = "*ESE"
        args = ["1"]

    ESE = ESE()  # type: ignore
    """
    *ESE

    Arguments: 1
    """

    class ESR(SCPINode, SCPIQuery):
        """
        *ESR

        Arguments:
        """
        __slots__ = ()
        _cmd = "*ESR"
        args = []  # type: List[str]

    ESR = ESR()  # type: ignore
    """
    *ESR

    Arguments:
    """

    class IDN(SCPINode, SCPIQuery):
        """
        *IDN

        Arguments:
        """
        __slots__ = ()
        _cmd = "*IDN"
        args = []  # type: List[str]

    IDN = IDN()  # type: ignore
    """
    *IDN

    Arguments:
    """

    class IST(SCPINode, SCPIQuery):
        """
        *IST

        Arguments:
        """
        __slots__ = ()
        _cmd = "*IST"
        args = []  # type: List[str]

    IST = IST()  # type: ignore
    """
    *IST

    Arguments:
    """

    class OPC(SCPINode, SCPIQuery, SCPISet):
        """
        *OPC

        Arguments:
        """
        __slots__ = ()
        _cmd = "*OPC"
        args = []  # type: List[str]

    OPC = OPC()  # type: ignore
    """
    *OPC

    Arguments:
    """

    class OPT(SCPINode, SCPIQuery):
        """
        *OPT

        Arguments:
        """
        __slots__ = ()
        _cmd = "*OPT"
        args = []  # type: List[str]

    OPT = OPT()  # type: ignore
    """
    *OPT

    Arguments:
    """

    class PRE(SCPINode, SCPIQuery, SCPISet):
        """
        *PRE

        Arguments: 1
        """
        __slots__ = ()
        _cmd = "*PRE"
        args = ["1"]

    PRE = PRE()  # type: ignore
    """
    *PRE

    Arguments: 1
    """

    class RCL(SCPINode, SCPISet):
        """
        *RCL

        Arguments: 1
        """
        __slots__ = ()
        _cmd = "*RCL"
        args = ["1"]

    RCL = RCL()  # type: ignore
    """
    *RCL

    Arguments: 1
    """

    class RST(SCPINode, SCPISet):
        """
        *RST

        Arguments:
        """
        __slots__ = ()
        _cmd = "*RST"
        args = []  # type: List[str]

    RST = RST()  # type: ignore
    """
    *RST

    Arguments:
    """

    class SAV(SCPINode, SCPISet):
        """
        *SAV

        Arguments: 1
        """
        __slots__ = ()
        _cmd = "*SAV"
        args = ["1"]

    SAV = SAV()  # type: ignore
    """
    *SAV

    Arguments: 1
    """

    class SRE(SCPINode, SCPIQuery, SCPISet):
        """
        *SRE

        Arguments: 1
        """
        __slots__ = ()
        _cmd = "*SRE"
        args = ["1"]

    SRE = SRE()  # type: ignore
    """
    *SRE

    Arguments: 1
    """

    class STB(SCPINode, SCPIQuery):
        """
        *STB

        Arguments:
        """
        __slots__ = ()
        _cmd = "*STB"
        args = []  # type: List[str]

    STB = STB()  # type: ignore
    """
    *STB

    Arguments:
    """

    class TRG(SCPINode, SCPISet):
        """
        *TRG

        Arguments:
        """
        __slots__ = ()
        _cmd = "*TRG"
        args = []  # type: List[str]

    TRG = TRG()  # type: ignore
    """
    *TRG

    Arguments:
    """

    class TST(SCPINode, SCPIQuery):
        """
        *TST

        Arguments:
        """
        __slots__ = ()
        _cmd = "*TST"
        args = []  # type: List[str]

    TST = TST()  # type: ignore
    """
    *TST

    Arguments:
    """

    class WAI(SCPINode, SCPISet):
        """
        *WAI

        Arguments:
        """
        __slots__ = ()
        _cmd = "*WAI"
        args = []  # type: List[str]

    WAI = WAI()  # type: ignore
    """
    *WAI

    Arguments:
    """

    class ABORt(SCPINode, SCPISet):
        """
        ABORt

        Arguments:
        """
        __slots__ = ()
        _cmd = "ABORt"
        args = []  # type: List[str]

    ABORt = ABORt()  # type: ignore
    """
    ABORt

    Arguments:
    """

    class CALCulate(SCPINode):
        """
        CALCulate

        Arguments:
        """
        __slots__ = ()
        _cmd = "CALCulate"
        args = []  # type: List[str]

        class FEED(SCPINode, SCPIQuery, SCPISet):
            """
            CALCulate:FEED

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "FEED"
            args = ["'string'"]

        FEED = FEED()  # type: ignore
        """
        CALCulate:FEED

        Arguments: 'string'
        """

    CALCulate = CALCulate()  # type: ignore
    """
    CALCulate

    Arguments:
    """

    class CALibration(SCPINode):
        """
        CALibration

        Arguments:
        """
        __slots__ = ()
        _cmd = "CALibration"
        args = []  # type: List[str]

        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            CALibration:DATA

            Arguments: <block_data>
            """
            __slots__ = ()
            _cmd = "DATA"
            args = ["<block_data>"]

            class LENGth(SCPINode, SCPIQuery):
                """
                CALibration:DATA:LENGth

                Arguments:
                """
                __slots__ = ()
                _cmd = "LENGth"
                args = []  # type: List[str]

            LENGth = LENGth()  # type: ignore
            """
            CALibration:DATA:LENGth

            Arguments:
            """

        DATA = DATA()  # type: ignore
        """
        CALibration:DATA

        Arguments: <block_data>
        """

        class USER(SCPINode):
            """
            CALibration:USER

            Arguments:
            """
            __slots__ = ()
            _cmd = "USER"
            args = []  # type: List[str]

            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                CALibration:USER:DATA

                Arguments: <block_data>
                """
                __slots__ = ()
                _cmd = "DATA"
                args = ["<block_data>"]

                class LENGth(SCPINode, SCPIQuery):
                    """
                    CALibration:USER:DATA:LENGth

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "LENGth"
                    args = []  # type: List[str]

                LENGth = LENGth()  # type: ignore
                """
                CALibration:USER:DATA:LENGth

                Arguments:
                """

            DATA = DATA()  # type: ignore
            """
            CALibration:USER:DATA

            Arguments: <block_data>
            """

        USER = USER()  # type: ignore
        """
        CALibration:USER

        Arguments:
        """

        class ZERO(SCPINode):
            """
            CALibration:ZERO

            Arguments:
            """
            __slots__ = ()
            _cmd = "ZERO"
            args = []  # type: List[str]

            class AUTO(SCPINode, SCPIQuery, SCPISet):
                """
                CALibration:ZERO:AUTO

                Arguments: ONCE
                """
                __slots__ = ()
                _cmd = "AUTO"
                args = ["ONCE"]

            AUTO = AUTO()  # type: ignore
            """
            CALibration:ZERO:AUTO

            Arguments: ONCE
            """

        ZERO = ZERO()  # type: ignore
        """
        CALibration:ZERO

        Arguments:
        """

    CALibration = CALibration()  # type: ignore
    """
    CALibration

    Arguments:
    """

    class FETCh(SCPINodeN, SCPIQuery):
        """
        FETCh

        Arguments:
        """
        __slots__ = ()
        _cmd = "FETCh"
        args = []  # type: List[str]

        class ARRay(SCPINode):
            """
            FETCh:ARRay

            Arguments:
            """
            __slots__ = ()
            _cmd = "ARRay"
            args = []  # type: List[str]

            class POWer(SCPINode):
                """
                FETCh:ARRay:POWer

                Arguments:
                """
                __slots__ = ()
                _cmd = "POWer"
                args = []  # type: List[str]

                class AVG(SCPINode, SCPIQuery):
                    """
                    FETCh:ARRay:POWer:AVG

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "AVG"
                    args = []  # type: List[str]

                AVG = AVG()  # type: ignore
                """
                FETCh:ARRay:POWer:AVG

                Arguments:
                """

            POWer = POWer()  # type: ignore
            """
            FETCh:ARRay:POWer

            Arguments:
            """

        ARRay = ARRay()  # type: ignore
        """
        FETCh:ARRay

        Arguments:
        """

        class SCALar(SCPINode):
            """
            FETCh:SCALar

            Arguments:
            """
            __slots__ = ()
            _cmd = "SCALar"
            args = []  # type: List[str]

            class POWer(SCPINode):
                """
                FETCh:SCALar:POWer

                Arguments:
                """
                __slots__ = ()
                _cmd = "POWer"
                args = []  # type: List[str]

                class AVG(SCPINode, SCPIQuery):
                    """
                    FETCh:SCALar:POWer:AVG

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "AVG"
                    args = []  # type: List[str]

                AVG = AVG()  # type: ignore
                """
                FETCh:SCALar:POWer:AVG

                Arguments:
                """

                class BURSt(SCPINode, SCPIQuery):
                    """
                    FETCh:SCALar:POWer:BURSt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "BURSt"
                    args = []  # type: List[str]

                BURSt = BURSt()  # type: ignore
                """
                FETCh:SCALar:POWer:BURSt

                Arguments:
                """

                class TSLot(SCPINode, SCPIQuery):
                    """
                    FETCh:SCALar:POWer:TSLot

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "TSLot"
                    args = []  # type: List[str]

                TSLot = TSLot()  # type: ignore
                """
                FETCh:SCALar:POWer:TSLot

                Arguments:
                """

            POWer = POWer()  # type: ignore
            """
            FETCh:SCALar:POWer

            Arguments:
            """

        SCALar = SCALar()  # type: ignore
        """
        FETCh:SCALar

        Arguments:
        """

    FETCh = FETCh()  # type: ignore
    """
    FETCh

    Arguments:
    """

    class FORMat(SCPINode):
        """
        FORMat

        Arguments:
        """
        __slots__ = ()
        _cmd = "FORMat"
        args = []  # type: List[str]

        class BORDer(SCPINode, SCPIQuery, SCPISet):
            """
            FORMat:BORDer

            Arguments: NORMal, SWAPped
            """
            __slots__ = ()
            _cmd = "BORDer"
            args = ["NORMal", "SWAPped"]

        BORDer = BORDer()  # type: ignore
        """
        FORMat:BORDer

        Arguments: NORMal, SWAPped
        """

        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            FORMat:DATA

            Arguments: ASCii, REAL
            """
            __slots__ = ()
            _cmd = "DATA"
            args = ["ASCii", "REAL"]

        DATA = DATA()  # type: ignore
        """
        FORMat:DATA

        Arguments: ASCii, REAL
        """

        class SREGister(SCPINode, SCPIQuery, SCPISet):
            """
            FORMat:SREGister

            Arguments: ASCii, BINary, HEXadecimal, OCTal
            """
            __slots__ = ()
            _cmd = "SREGister"
            args = ["ASCii", "BINary", "HEXadecimal", "OCTal"]

        SREGister = SREGister()  # type: ignore
        """
        FORMat:SREGister

        Arguments: ASCii, BINary, HEXadecimal, OCTal
        """

    FORMat = FORMat()  # type: ignore
    """
    FORMat

    Arguments:
    """

    class INITiate(SCPINode):
        """
        INITiate

        Arguments:
        """
        __slots__ = ()
        _cmd = "INITiate"
        args = []  # type: List[str]

        class ALL(SCPINode, SCPISet):
            """
            INITiate:ALL

            Arguments:
            """
            __slots__ = ()
            _cmd = "ALL"
            args = []  # type: List[str]

        ALL = ALL()  # type: ignore
        """
        INITiate:ALL

        Arguments:
        """

        class CONTinuous(SCPINode, SCPIBool):
            """
            INITiate:CONTinuous

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "CONTinuous"
            args = ["1", "ON", "OFF"]

        CONTinuous = CONTinuous()  # type: ignore
        """
        INITiate:CONTinuous

        Arguments: 1, ON, OFF
        """

        class IMMediate(SCPINode, SCPISet):
            """
            INITiate:IMMediate

            Arguments:
            """
            __slots__ = ()
            _cmd = "IMMediate"
            args = []  # type: List[str]

        IMMediate = IMMediate()  # type: ignore
        """
        INITiate:IMMediate

        Arguments:
        """

    INITiate = INITiate()  # type: ignore
    """
    INITiate

    Arguments:
    """

    class READ(SCPINodeN):
        """
        READ

        Arguments:
        """
        __slots__ = ()
        _cmd = "READ"
        args = []  # type: List[str]

        class ARRay(SCPINode):
            """
            READ:ARRay

            Arguments:
            """
            __slots__ = ()
            _cmd = "ARRay"
            args = []  # type: List[str]

            class POWer(SCPINode):
                """
                READ:ARRay:POWer

                Arguments:
                """
                __slots__ = ()
                _cmd = "POWer"
                args = []  # type: List[str]

                class AVG(SCPINode, SCPIQuery):
                    """
                    READ:ARRay:POWer:AVG

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "AVG"
                    args = []  # type: List[str]

                AVG = AVG()  # type: ignore
                """
                READ:ARRay:POWer:AVG

                Arguments:
                """

            POWer = POWer()  # type: ignore
            """
            READ:ARRay:POWer

            Arguments:
            """

        ARRay = ARRay()  # type: ignore
        """
        READ:ARRay

        Arguments:
        """

        class SCALar(SCPINode):
            """
            READ:SCALar

            Arguments:
            """
            __slots__ = ()
            _cmd = "SCALar"
            args = []  # type: List[str]

            class POWer(SCPINode):
                """
                READ:SCALar:POWer

                Arguments:
                """
                __slots__ = ()
                _cmd = "POWer"
                args = []  # type: List[str]

                class AVG(SCPINode, SCPIQuery):
                    """
                    READ:SCALar:POWer:AVG

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "AVG"
                    args = []  # type: List[str]

                AVG = AVG()  # type: ignore
                """
                READ:SCALar:POWer:AVG

                Arguments:
                """

                class BURSt(SCPINode, SCPIQuery):
                    """
                    READ:SCALar:POWer:BURSt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "BURSt"
                    args = []  # type: List[str]

                BURSt = BURSt()  # type: ignore
                """
                READ:SCALar:POWer:BURSt

                Arguments:
                """

                class TSLot(SCPINode, SCPIQuery):
                    """
                    READ:SCALar:POWer:TSLot

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "TSLot"
                    args = []  # type: List[str]

                TSLot = TSLot()  # type: ignore
                """
                READ:SCALar:POWer:TSLot

                Arguments:
                """

            POWer = POWer()  # type: ignore
            """
            READ:SCALar:POWer

            Arguments:
            """

        SCALar = SCALar()  # type: ignore
        """
        READ:SCALar

        Arguments:
        """

        class XTIMe(SCPINode):
            """
            READ:XTIMe

            Arguments:
            """
            __slots__ = ()
            _cmd = "XTIMe"
            args = []  # type: List[str]

            class POWer(SCPINode, SCPIQuery):
                """
                READ:XTIMe:POWer

                Arguments:
                """
                __slots__ = ()
                _cmd = "POWer"
                args = []  # type: List[str]

            POWer = POWer()  # type: ignore
            """
            READ:XTIMe:POWer

            Arguments:
            """

        XTIMe = XTIMe()  # type: ignore
        """
        READ:XTIMe

        Arguments:
        """

    READ = READ()  # type: ignore
    """
    READ

    Arguments:
    """

    class SENSe(SCPINodeN):
        """
        SENSe

        Arguments:
        """
        __slots__ = ()
        _cmd = "SENSe"
        args = []  # type: List[str]

        class AUXiliary(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:AUXiliary

            Arguments: MINMax, NONE, RNDMax
            """
            __slots__ = ()
            _cmd = "AUXiliary"
            args = ["MINMax", "NONE", "RNDMax"]

        AUXiliary = AUXiliary()  # type: ignore
        """
        SENSe:AUXiliary

        Arguments: MINMax, NONE, RNDMax
        """

        class AVERage(SCPINode):
            """
            SENSe:AVERage

            Arguments:
            """
            __slots__ = ()
            _cmd = "AVERage"
            args = []  # type: List[str]

            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:AVERage:COUNt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "COUNt"
                args = ["1"]

                class AUTO(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:AVERage:COUNt:AUTO

                    Arguments: <boolean>, ONCE
                    """
                    __slots__ = ()
                    _cmd = "AUTO"
                    args = ["<boolean>", "ONCE"]

                    class MTIMe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:AVERage:COUNt:AUTO:MTIMe

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "MTIMe"
                        args = ["1"]

                    MTIMe = MTIMe()  # type: ignore
                    """
                    SENSe:AVERage:COUNt:AUTO:MTIMe

                    Arguments: 1
                    """

                    class NSRatio(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:AVERage:COUNt:AUTO:NSRatio

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "NSRatio"
                        args = ["1"]

                    NSRatio = NSRatio()  # type: ignore
                    """
                    SENSe:AVERage:COUNt:AUTO:NSRatio

                    Arguments: 1
                    """

                    class RESolution(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:AVERage:COUNt:AUTO:RESolution

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "RESolution"
                        args = ["1"]

                    RESolution = RESolution()  # type: ignore
                    """
                    SENSe:AVERage:COUNt:AUTO:RESolution

                    Arguments: 1
                    """

                    class SLOT(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:AVERage:COUNt:AUTO:SLOT

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "SLOT"
                        args = ["1"]

                    SLOT = SLOT()  # type: ignore
                    """
                    SENSe:AVERage:COUNt:AUTO:SLOT

                    Arguments: 1
                    """

                    class TYPE(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:AVERage:COUNt:AUTO:TYPE

                        Arguments: NSRatio, RESolution
                        """
                        __slots__ = ()
                        _cmd = "TYPE"
                        args = ["NSRatio", "RESolution"]

                    TYPE = TYPE()  # type: ignore
                    """
                    SENSe:AVERage:COUNt:AUTO:TYPE

                    Arguments: NSRatio, RESolution
                    """

                AUTO = AUTO()  # type: ignore
                """
                SENSe:AVERage:COUNt:AUTO

                Arguments: <boolean>, ONCE
                """

            COUNt = COUNt()  # type: ignore
            """
            SENSe:AVERage:COUNt

            Arguments: 1
            """

            class RESet(SCPINode, SCPISet):
                """
                SENSe:AVERage:RESet

                Arguments:
                """
                __slots__ = ()
                _cmd = "RESet"
                args = []  # type: List[str]

            RESet = RESet()  # type: ignore
            """
            SENSe:AVERage:RESet

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                SENSe:AVERage:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SENSe:AVERage:STATe

            Arguments: 1, ON, OFF
            """

            class TCONtrol(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:AVERage:TCONtrol

                Arguments: MOVing, REPeat
                """
                __slots__ = ()
                _cmd = "TCONtrol"
                args = ["MOVing", "REPeat"]

            TCONtrol = TCONtrol()  # type: ignore
            """
            SENSe:AVERage:TCONtrol

            Arguments: MOVing, REPeat
            """

        AVERage = AVERage()  # type: ignore
        """
        SENSe:AVERage

        Arguments:
        """

        class CORRection(SCPINode):
            """
            SENSe:CORRection

            Arguments:
            """
            __slots__ = ()
            _cmd = "CORRection"
            args = []  # type: List[str]

            class DCYCle(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:DCYCle

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DCYCle"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SENSe:CORRection:DCYCle:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SENSe:CORRection:DCYCle:STATe

                Arguments: 1, ON, OFF
                """

            DCYCle = DCYCle()  # type: ignore
            """
            SENSe:CORRection:DCYCle

            Arguments: 1
            """

            class OFFSet(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:OFFSet

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "OFFSet"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SENSe:CORRection:OFFSet:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SENSe:CORRection:OFFSet:STATe

                Arguments: 1, ON, OFF
                """

            OFFSet = OFFSet()  # type: ignore
            """
            SENSe:CORRection:OFFSet

            Arguments: 1
            """

            class SPDevice(SCPINode):
                """
                SENSe:CORRection:SPDevice

                Arguments:
                """
                __slots__ = ()
                _cmd = "SPDevice"
                args = []  # type: List[str]

                class LIST(SCPINode, SCPIQuery):
                    """
                    SENSe:CORRection:SPDevice:LIST

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "LIST"
                    args = []  # type: List[str]

                LIST = LIST()  # type: ignore
                """
                SENSe:CORRection:SPDevice:LIST

                Arguments:
                """

                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:SPDevice:SELect

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "SELect"
                    args = ["1"]

                SELect = SELect()  # type: ignore
                """
                SENSe:CORRection:SPDevice:SELect

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SENSe:CORRection:SPDevice:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SENSe:CORRection:SPDevice:STATe

                Arguments: 1, ON, OFF
                """

            SPDevice = SPDevice()  # type: ignore
            """
            SENSe:CORRection:SPDevice

            Arguments:
            """

        CORRection = CORRection()  # type: ignore
        """
        SENSe:CORRection

        Arguments:
        """

        class FREQuency(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:FREQuency

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "FREQuency"
            args = ["1"]

        FREQuency = FREQuency()  # type: ignore
        """
        SENSe:FREQuency

        Arguments: 1
        """

        class FUNCtion(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:FUNCtion

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "FUNCtion"
            args = ["'string'"]

        FUNCtion = FUNCtion()  # type: ignore
        """
        SENSe:FUNCtion

        Arguments: 'string'
        """

        class POWer(SCPINode):
            """
            SENSe:POWer

            Arguments:
            """
            __slots__ = ()
            _cmd = "POWer"
            args = []  # type: List[str]

            class AVG(SCPINode):
                """
                SENSe:POWer:AVG

                Arguments:
                """
                __slots__ = ()
                _cmd = "AVG"
                args = []  # type: List[str]

                class APERture(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:POWer:AVG:APERture

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "APERture"
                    args = ["1"]

                APERture = APERture()  # type: ignore
                """
                SENSe:POWer:AVG:APERture

                Arguments: 1
                """

                class BUFFer(SCPINode):
                    """
                    SENSe:POWer:AVG:BUFFer

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "BUFFer"
                    args = []  # type: List[str]

                    class CLEar(SCPINode, SCPISet):
                        """
                        SENSe:POWer:AVG:BUFFer:CLEar

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "CLEar"
                        args = []  # type: List[str]

                    CLEar = CLEar()  # type: ignore
                    """
                    SENSe:POWer:AVG:BUFFer:CLEar

                    Arguments:
                    """

                    class COUNt(SCPINode, SCPIQuery):
                        """
                        SENSe:POWer:AVG:BUFFer:COUNt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "COUNt"
                        args = []  # type: List[str]

                    COUNt = COUNt()  # type: ignore
                    """
                    SENSe:POWer:AVG:BUFFer:COUNt

                    Arguments:
                    """

                    class DATA(SCPINode, SCPIQuery):
                        """
                        SENSe:POWer:AVG:BUFFer:DATA

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "DATA"
                        args = []  # type: List[str]

                    DATA = DATA()  # type: ignore
                    """
                    SENSe:POWer:AVG:BUFFer:DATA

                    Arguments:
                    """

                    class INFO(SCPINode, SCPIQuery):
                        """
                        SENSe:POWer:AVG:BUFFer:INFO

                        Arguments: 'string'
                        """
                        __slots__ = ()
                        _cmd = "INFO"
                        args = ["'string'"]

                    INFO = INFO()  # type: ignore
                    """
                    SENSe:POWer:AVG:BUFFer:INFO

                    Arguments: 'string'
                    """

                    class SIZE(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:POWer:AVG:BUFFer:SIZE

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "SIZE"
                        args = ["1"]

                    SIZE = SIZE()  # type: ignore
                    """
                    SENSe:POWer:AVG:BUFFer:SIZE

                    Arguments: 1
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SENSe:POWer:AVG:BUFFer:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SENSe:POWer:AVG:BUFFer:STATe

                    Arguments: 1, ON, OFF
                    """

                BUFFer = BUFFer()  # type: ignore
                """
                SENSe:POWer:AVG:BUFFer

                Arguments:
                """

                class FAST(SCPINode, SCPIBool):
                    """
                    SENSe:POWer:AVG:FAST

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "FAST"
                    args = ["1", "ON", "OFF"]

                FAST = FAST()  # type: ignore
                """
                SENSe:POWer:AVG:FAST

                Arguments: 1, ON, OFF
                """

                class SMOothing(SCPINode):
                    """
                    SENSe:POWer:AVG:SMOothing

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SMOothing"
                    args = []  # type: List[str]

                    class STATe(SCPINode, SCPIBool):
                        """
                        SENSe:POWer:AVG:SMOothing:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SENSe:POWer:AVG:SMOothing:STATe

                    Arguments: 1, ON, OFF
                    """

                SMOothing = SMOothing()  # type: ignore
                """
                SENSe:POWer:AVG:SMOothing

                Arguments:
                """

            AVG = AVG()  # type: ignore
            """
            SENSe:POWer:AVG

            Arguments:
            """

            class BURSt(SCPINode):
                """
                SENSe:POWer:BURSt

                Arguments:
                """
                __slots__ = ()
                _cmd = "BURSt"
                args = []  # type: List[str]

                class DTOLerance(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:POWer:BURSt:DTOLerance

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DTOLerance"
                    args = ["1"]

                DTOLerance = DTOLerance()  # type: ignore
                """
                SENSe:POWer:BURSt:DTOLerance

                Arguments: 1
                """

                class LENGth(SCPINode, SCPIQuery):
                    """
                    SENSe:POWer:BURSt:LENGth

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "LENGth"
                    args = []  # type: List[str]

                LENGth = LENGth()  # type: ignore
                """
                SENSe:POWer:BURSt:LENGth

                Arguments:
                """

            BURSt = BURSt()  # type: ignore
            """
            SENSe:POWer:BURSt

            Arguments:
            """

            class TSLot(SCPINode):
                """
                SENSe:POWer:TSLot

                Arguments:
                """
                __slots__ = ()
                _cmd = "TSLot"
                args = []  # type: List[str]

                class AVG(SCPINode):
                    """
                    SENSe:POWer:TSLot:AVG

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "AVG"
                    args = []  # type: List[str]

                    class COUNt(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:POWer:TSLot:AVG:COUNt

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "COUNt"
                        args = ["1"]

                    COUNt = COUNt()  # type: ignore
                    """
                    SENSe:POWer:TSLot:AVG:COUNt

                    Arguments: 1
                    """

                    class EXCLude(SCPINode):
                        """
                        SENSe:POWer:TSLot:AVG:EXCLude

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EXCLude"
                        args = []  # type: List[str]

                        class MID(SCPINode):
                            """
                            SENSe:POWer:TSLot:AVG:EXCLude:MID

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "MID"
                            args = []  # type: List[str]

                            class OFFSet(SCPINode):
                                """
                                SENSe:POWer:TSLot:AVG:EXCLude:MID:OFFSet

                                Arguments:
                                """
                                __slots__ = ()
                                _cmd = "OFFSet"
                                args = []  # type: List[str]

                                class TIME(SCPINode, SCPIQuery, SCPISet):
                                    """
                                    SENSe:POWer:TSLot:AVG:EXCLude:MID:OFFSet:TIME

                                    Arguments: 1
                                    """
                                    __slots__ = ()
                                    _cmd = "TIME"
                                    args = ["1"]

                                TIME = TIME()  # type: ignore
                                """
                                SENSe:POWer:TSLot:AVG:EXCLude:MID:OFFSet:TIME

                                Arguments: 1
                                """

                            OFFSet = OFFSet()  # type: ignore
                            """
                            SENSe:POWer:TSLot:AVG:EXCLude:MID:OFFSet

                            Arguments:
                            """

                            class STATe(SCPINode, SCPIBool):
                                """
                                SENSe:POWer:TSLot:AVG:EXCLude:MID:STATe

                                Arguments: 1, ON, OFF
                                """
                                __slots__ = ()
                                _cmd = "STATe"
                                args = ["1", "ON", "OFF"]

                            STATe = STATe()  # type: ignore
                            """
                            SENSe:POWer:TSLot:AVG:EXCLude:MID:STATe

                            Arguments: 1, ON, OFF
                            """

                            class TIME(SCPINode, SCPIQuery, SCPISet):
                                """
                                SENSe:POWer:TSLot:AVG:EXCLude:MID:TIME

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "TIME"
                                args = ["1"]

                            TIME = TIME()  # type: ignore
                            """
                            SENSe:POWer:TSLot:AVG:EXCLude:MID:TIME

                            Arguments: 1
                            """

                        MID = MID()  # type: ignore
                        """
                        SENSe:POWer:TSLot:AVG:EXCLude:MID

                        Arguments:
                        """

                    EXCLude = EXCLude()  # type: ignore
                    """
                    SENSe:POWer:TSLot:AVG:EXCLude

                    Arguments:
                    """

                    class WIDTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:POWer:TSLot:AVG:WIDTh

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "WIDTh"
                        args = ["1"]

                    WIDTh = WIDTh()  # type: ignore
                    """
                    SENSe:POWer:TSLot:AVG:WIDTh

                    Arguments: 1
                    """

                AVG = AVG()  # type: ignore
                """
                SENSe:POWer:TSLot:AVG

                Arguments:
                """

            TSLot = TSLot()  # type: ignore
            """
            SENSe:POWer:TSLot

            Arguments:
            """

        POWer = POWer()  # type: ignore
        """
        SENSe:POWer

        Arguments:
        """

        class RANGe(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:RANGe

            Arguments: 0, 1, 2
            """
            __slots__ = ()
            _cmd = "RANGe"
            args = ["0", "1", "2"]

            class AUTO(SCPINode, SCPIBool):
                """
                SENSe:RANGe:AUTO

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "AUTO"
                args = ["1", "ON", "OFF"]

            AUTO = AUTO()  # type: ignore
            """
            SENSe:RANGe:AUTO

            Arguments: 1, ON, OFF
            """

            class CLEVel(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:RANGe:CLEVel

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "CLEVel"
                args = ["1"]

            CLEVel = CLEVel()  # type: ignore
            """
            SENSe:RANGe:CLEVel

            Arguments: 1
            """

        RANGe = RANGe()  # type: ignore
        """
        SENSe:RANGe

        Arguments: 0, 1, 2
        """

        class SAMPling(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:SAMPling

            Arguments: FREQ1
            """
            __slots__ = ()
            _cmd = "SAMPling"
            args = ["FREQ1"]

        SAMPling = SAMPling()  # type: ignore
        """
        SENSe:SAMPling

        Arguments: FREQ1
        """

        class SGAMma(SCPINode):
            """
            SENSe:SGAMma

            Arguments:
            """
            __slots__ = ()
            _cmd = "SGAMma"
            args = []  # type: List[str]

            class CORRection(SCPINode):
                """
                SENSe:SGAMma:CORRection

                Arguments:
                """
                __slots__ = ()
                _cmd = "CORRection"
                args = []  # type: List[str]

                class STATe(SCPINode, SCPIBool):
                    """
                    SENSe:SGAMma:CORRection:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SENSe:SGAMma:CORRection:STATe

                Arguments: 1, ON, OFF
                """

            CORRection = CORRection()  # type: ignore
            """
            SENSe:SGAMma:CORRection

            Arguments:
            """

            class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SGAMma:MAGNitude

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "MAGNitude"
                args = ["1"]

            MAGNitude = MAGNitude()  # type: ignore
            """
            SENSe:SGAMma:MAGNitude

            Arguments: 1
            """

            class PHASe(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SGAMma:PHASe

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PHASe"
                args = ["1"]

            PHASe = PHASe()  # type: ignore
            """
            SENSe:SGAMma:PHASe

            Arguments: 1
            """

        SGAMma = SGAMma()  # type: ignore
        """
        SENSe:SGAMma

        Arguments:
        """

        class TIMing(SCPINode):
            """
            SENSe:TIMing

            Arguments:
            """
            __slots__ = ()
            _cmd = "TIMing"
            args = []  # type: List[str]

            class EXCLude(SCPINode):
                """
                SENSe:TIMing:EXCLude

                Arguments:
                """
                __slots__ = ()
                _cmd = "EXCLude"
                args = []  # type: List[str]

                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TIMing:EXCLude:STARt

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "STARt"
                    args = ["1"]

                STARt = STARt()  # type: ignore
                """
                SENSe:TIMing:EXCLude:STARt

                Arguments: 1
                """

                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TIMing:EXCLude:STOP

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "STOP"
                    args = ["1"]

                STOP = STOP()  # type: ignore
                """
                SENSe:TIMing:EXCLude:STOP

                Arguments: 1
                """

            EXCLude = EXCLude()  # type: ignore
            """
            SENSe:TIMing:EXCLude

            Arguments:
            """

        TIMing = TIMing()  # type: ignore
        """
        SENSe:TIMing

        Arguments:
        """

        class TRACe(SCPINode):
            """
            SENSe:TRACe

            Arguments:
            """
            __slots__ = ()
            _cmd = "TRACe"
            args = []  # type: List[str]

            class AVERage(SCPINode):
                """
                SENSe:TRACe:AVERage

                Arguments:
                """
                __slots__ = ()
                _cmd = "AVERage"
                args = []  # type: List[str]

                class COUNt(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TRACe:AVERage:COUNt

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "COUNt"
                    args = ["1"]

                COUNt = COUNt()  # type: ignore
                """
                SENSe:TRACe:AVERage:COUNt

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SENSe:TRACe:AVERage:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SENSe:TRACe:AVERage:STATe

                Arguments: 1, ON, OFF
                """

                class TCONtrol(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TRACe:AVERage:TCONtrol

                    Arguments: MOVing, REPeat
                    """
                    __slots__ = ()
                    _cmd = "TCONtrol"
                    args = ["MOVing", "REPeat"]

                TCONtrol = TCONtrol()  # type: ignore
                """
                SENSe:TRACe:AVERage:TCONtrol

                Arguments: MOVing, REPeat
                """

            AVERage = AVERage()  # type: ignore
            """
            SENSe:TRACe:AVERage

            Arguments:
            """

            class DATA(SCPINode, SCPIQuery):
                """
                SENSe:TRACe:DATA

                Arguments:
                """
                __slots__ = ()
                _cmd = "DATA"
                args = []  # type: List[str]

            DATA = DATA()  # type: ignore
            """
            SENSe:TRACe:DATA

            Arguments:
            """

            class MPWidth(SCPINode, SCPIQuery):
                """
                SENSe:TRACe:MPWidth

                Arguments:
                """
                __slots__ = ()
                _cmd = "MPWidth"
                args = []  # type: List[str]

            MPWidth = MPWidth()  # type: ignore
            """
            SENSe:TRACe:MPWidth

            Arguments:
            """

            class OFFSet(SCPINode):
                """
                SENSe:TRACe:OFFSet

                Arguments:
                """
                __slots__ = ()
                _cmd = "OFFSet"
                args = []  # type: List[str]

                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:TRACe:OFFSet:TIME

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "TIME"
                    args = ["1"]

                TIME = TIME()  # type: ignore
                """
                SENSe:TRACe:OFFSet:TIME

                Arguments: 1
                """

            OFFSet = OFFSet()  # type: ignore
            """
            SENSe:TRACe:OFFSet

            Arguments:
            """

            class POINts(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:TRACe:POINts

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "POINts"
                args = ["1"]

            POINts = POINts()  # type: ignore
            """
            SENSe:TRACe:POINts

            Arguments: 1
            """

            class REALtime(SCPINode, SCPIBool):
                """
                SENSe:TRACe:REALtime

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "REALtime"
                args = ["1", "ON", "OFF"]

            REALtime = REALtime()  # type: ignore
            """
            SENSe:TRACe:REALtime

            Arguments: 1, ON, OFF
            """

            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:TRACe:TIME

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "TIME"
                args = ["1"]

            TIME = TIME()  # type: ignore
            """
            SENSe:TRACe:TIME

            Arguments: 1
            """

        TRACe = TRACe()  # type: ignore
        """
        SENSe:TRACe

        Arguments:
        """

    SENSe = SENSe()  # type: ignore
    """
    SENSe

    Arguments:
    """

    class STATus(SCPINode):
        """
        STATus

        Arguments:
        """
        __slots__ = ()
        _cmd = "STATus"
        args = []  # type: List[str]

        class DEVice(SCPINode):
            """
            STATus:DEVice

            Arguments:
            """
            __slots__ = ()
            _cmd = "DEVice"
            args = []  # type: List[str]

            class CONDition(SCPINode, SCPIQuery):
                """
                STATus:DEVice:CONDition

                Arguments:
                """
                __slots__ = ()
                _cmd = "CONDition"
                args = []  # type: List[str]

            CONDition = CONDition()  # type: ignore
            """
            STATus:DEVice:CONDition

            Arguments:
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:DEVice:ENABle

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()  # type: ignore
            """
            STATus:DEVice:ENABle

            Arguments: 1
            """

            class EVENt(SCPINode, SCPIQuery):
                """
                STATus:DEVice:EVENt

                Arguments:
                """
                __slots__ = ()
                _cmd = "EVENt"
                args = []  # type: List[str]

            EVENt = EVENt()  # type: ignore
            """
            STATus:DEVice:EVENt

            Arguments:
            """

            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:DEVice:NTRansition

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()  # type: ignore
            """
            STATus:DEVice:NTRansition

            Arguments: 1
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:DEVice:PTRansition

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()  # type: ignore
            """
            STATus:DEVice:PTRansition

            Arguments: 1
            """

        DEVice = DEVice()  # type: ignore
        """
        STATus:DEVice

        Arguments:
        """

        class OPERation(SCPINode):
            """
            STATus:OPERation

            Arguments:
            """
            __slots__ = ()
            _cmd = "OPERation"
            args = []  # type: List[str]

            class CALibrating(SCPINode):
                """
                STATus:OPERation:CALibrating

                Arguments:
                """
                __slots__ = ()
                _cmd = "CALibrating"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:CALibrating:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:OPERation:CALibrating:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:CALibrating:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:OPERation:CALibrating:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:CALibrating:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:OPERation:CALibrating:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:CALibrating:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:OPERation:CALibrating:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:CALibrating:SUMMary

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SUMMary"
                    args = []  # type: List[str]

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:CALibrating:SUMMary:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:OPERation:CALibrating:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()  # type: ignore
                """
                STATus:OPERation:CALibrating:SUMMary

                Arguments:
                """

            CALibrating = CALibrating()  # type: ignore
            """
            STATus:OPERation:CALibrating

            Arguments:
            """

            class CONDition(SCPINode, SCPIQuery):
                """
                STATus:OPERation:CONDition

                Arguments:
                """
                __slots__ = ()
                _cmd = "CONDition"
                args = []  # type: List[str]

            CONDition = CONDition()  # type: ignore
            """
            STATus:OPERation:CONDition

            Arguments:
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:ENABle

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()  # type: ignore
            """
            STATus:OPERation:ENABle

            Arguments: 1
            """

            class EVENt(SCPINode, SCPIQuery):
                """
                STATus:OPERation:EVENt

                Arguments:
                """
                __slots__ = ()
                _cmd = "EVENt"
                args = []  # type: List[str]

            EVENt = EVENt()  # type: ignore
            """
            STATus:OPERation:EVENt

            Arguments:
            """

            class LLFail(SCPINode):
                """
                STATus:OPERation:LLFail

                Arguments:
                """
                __slots__ = ()
                _cmd = "LLFail"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:LLFail:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:OPERation:LLFail:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:LLFail:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:OPERation:LLFail:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:LLFail:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:OPERation:LLFail:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:LLFail:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:OPERation:LLFail:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:LLFail:SUMMary

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SUMMary"
                    args = []  # type: List[str]

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:LLFail:SUMMary:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:OPERation:LLFail:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()  # type: ignore
                """
                STATus:OPERation:LLFail:SUMMary

                Arguments:
                """

            LLFail = LLFail()  # type: ignore
            """
            STATus:OPERation:LLFail

            Arguments:
            """

            class MEASuring(SCPINode):
                """
                STATus:OPERation:MEASuring

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASuring"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:MEASuring:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:OPERation:MEASuring:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:MEASuring:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:OPERation:MEASuring:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:MEASuring:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:OPERation:MEASuring:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:MEASuring:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:OPERation:MEASuring:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:MEASuring:SUMMary

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SUMMary"
                    args = []  # type: List[str]

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:MEASuring:SUMMary:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:OPERation:MEASuring:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()  # type: ignore
                """
                STATus:OPERation:MEASuring:SUMMary

                Arguments:
                """

            MEASuring = MEASuring()  # type: ignore
            """
            STATus:OPERation:MEASuring

            Arguments:
            """

            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:NTRansition

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()  # type: ignore
            """
            STATus:OPERation:NTRansition

            Arguments: 1
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:PTRansition

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()  # type: ignore
            """
            STATus:OPERation:PTRansition

            Arguments: 1
            """

            class SENSe(SCPINode):
                """
                STATus:OPERation:SENSe

                Arguments:
                """
                __slots__ = ()
                _cmd = "SENSe"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:SENSe:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:OPERation:SENSe:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:SENSe:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:OPERation:SENSe:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:SENSe:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:OPERation:SENSe:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:SENSe:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:OPERation:SENSe:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:SENSe:SUMMary

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SUMMary"
                    args = []  # type: List[str]

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:SENSe:SUMMary:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:OPERation:SENSe:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()  # type: ignore
                """
                STATus:OPERation:SENSe:SUMMary

                Arguments:
                """

            SENSe = SENSe()  # type: ignore
            """
            STATus:OPERation:SENSe

            Arguments:
            """

            class TRIGger(SCPINode):
                """
                STATus:OPERation:TRIGger

                Arguments:
                """
                __slots__ = ()
                _cmd = "TRIGger"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:TRIGger:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:OPERation:TRIGger:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:TRIGger:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:OPERation:TRIGger:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:TRIGger:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:OPERation:TRIGger:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:TRIGger:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:OPERation:TRIGger:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:TRIGger:SUMMary

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SUMMary"
                    args = []  # type: List[str]

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:TRIGger:SUMMary:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:OPERation:TRIGger:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()  # type: ignore
                """
                STATus:OPERation:TRIGger:SUMMary

                Arguments:
                """

            TRIGger = TRIGger()  # type: ignore
            """
            STATus:OPERation:TRIGger

            Arguments:
            """

            class ULFail(SCPINode):
                """
                STATus:OPERation:ULFail

                Arguments:
                """
                __slots__ = ()
                _cmd = "ULFail"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:ULFail:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:OPERation:ULFail:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:ULFail:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:OPERation:ULFail:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:ULFail:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:OPERation:ULFail:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:ULFail:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:OPERation:ULFail:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:OPERation:ULFail:SUMMary

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SUMMary"
                    args = []  # type: List[str]

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:OPERation:ULFail:SUMMary:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:OPERation:ULFail:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()  # type: ignore
                """
                STATus:OPERation:ULFail:SUMMary

                Arguments:
                """

            ULFail = ULFail()  # type: ignore
            """
            STATus:OPERation:ULFail

            Arguments:
            """

        OPERation = OPERation()  # type: ignore
        """
        STATus:OPERation

        Arguments:
        """

        class PRESet(SCPINode, SCPISet):
            """
            STATus:PRESet

            Arguments:
            """
            __slots__ = ()
            _cmd = "PRESet"
            args = []  # type: List[str]

        PRESet = PRESet()  # type: ignore
        """
        STATus:PRESet

        Arguments:
        """

        class QUEStionable(SCPINode):
            """
            STATus:QUEStionable

            Arguments:
            """
            __slots__ = ()
            _cmd = "QUEStionable"
            args = []  # type: List[str]

            class CALibration(SCPINode):
                """
                STATus:QUEStionable:CALibration

                Arguments:
                """
                __slots__ = ()
                _cmd = "CALibration"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:CALibration:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:QUEStionable:CALibration:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:CALibration:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:QUEStionable:CALibration:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:CALibration:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:QUEStionable:CALibration:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:CALibration:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:QUEStionable:CALibration:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:QUEStionable:CALibration:SUMMary

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SUMMary"
                    args = []  # type: List[str]

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:QUEStionable:CALibration:SUMMary:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:QUEStionable:CALibration:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()  # type: ignore
                """
                STATus:QUEStionable:CALibration:SUMMary

                Arguments:
                """

            CALibration = CALibration()  # type: ignore
            """
            STATus:QUEStionable:CALibration

            Arguments:
            """

            class CONDition(SCPINode, SCPIQuery):
                """
                STATus:QUEStionable:CONDition

                Arguments:
                """
                __slots__ = ()
                _cmd = "CONDition"
                args = []  # type: List[str]

            CONDition = CONDition()  # type: ignore
            """
            STATus:QUEStionable:CONDition

            Arguments:
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:ENABle

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()  # type: ignore
            """
            STATus:QUEStionable:ENABle

            Arguments: 1
            """

            class EVENt(SCPINode, SCPIQuery):
                """
                STATus:QUEStionable:EVENt

                Arguments:
                """
                __slots__ = ()
                _cmd = "EVENt"
                args = []  # type: List[str]

            EVENt = EVENt()  # type: ignore
            """
            STATus:QUEStionable:EVENt

            Arguments:
            """

            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:NTRansition

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()  # type: ignore
            """
            STATus:QUEStionable:NTRansition

            Arguments: 1
            """

            class POWer(SCPINode):
                """
                STATus:QUEStionable:POWer

                Arguments:
                """
                __slots__ = ()
                _cmd = "POWer"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:POWer:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:QUEStionable:POWer:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:POWer:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:QUEStionable:POWer:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:POWer:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:QUEStionable:POWer:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:POWer:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:QUEStionable:POWer:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:QUEStionable:POWer:SUMMary

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SUMMary"
                    args = []  # type: List[str]

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:QUEStionable:POWer:SUMMary:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:QUEStionable:POWer:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()  # type: ignore
                """
                STATus:QUEStionable:POWer:SUMMary

                Arguments:
                """

            POWer = POWer()  # type: ignore
            """
            STATus:QUEStionable:POWer

            Arguments:
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:PTRansition

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()  # type: ignore
            """
            STATus:QUEStionable:PTRansition

            Arguments: 1
            """

            class WINDow(SCPINode):
                """
                STATus:QUEStionable:WINDow

                Arguments:
                """
                __slots__ = ()
                _cmd = "WINDow"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:WINDow:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:QUEStionable:WINDow:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:WINDow:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:QUEStionable:WINDow:ENABle

                Arguments: 1
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:WINDow:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:QUEStionable:WINDow:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:WINDow:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:QUEStionable:WINDow:PTRansition

                Arguments: 1
                """

                class SUMMary(SCPINode):
                    """
                    STATus:QUEStionable:WINDow:SUMMary

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SUMMary"
                    args = []  # type: List[str]

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:QUEStionable:WINDow:SUMMary:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:QUEStionable:WINDow:SUMMary:EVENt

                    Arguments:
                    """

                SUMMary = SUMMary()  # type: ignore
                """
                STATus:QUEStionable:WINDow:SUMMary

                Arguments:
                """

            WINDow = WINDow()  # type: ignore
            """
            STATus:QUEStionable:WINDow

            Arguments:
            """

        QUEStionable = QUEStionable()  # type: ignore
        """
        STATus:QUEStionable

        Arguments:
        """

        class QUEue(SCPINode):
            """
            STATus:QUEue

            Arguments:
            """
            __slots__ = ()
            _cmd = "QUEue"
            args = []  # type: List[str]

            class NEXT(SCPINode, SCPIQuery):
                """
                STATus:QUEue:NEXT

                Arguments:
                """
                __slots__ = ()
                _cmd = "NEXT"
                args = []  # type: List[str]

            NEXT = NEXT()  # type: ignore
            """
            STATus:QUEue:NEXT

            Arguments:
            """

        QUEue = QUEue()  # type: ignore
        """
        STATus:QUEue

        Arguments:
        """

    STATus = STATus()  # type: ignore
    """
    STATus

    Arguments:
    """

    class SYSTem(SCPINode):
        """
        SYSTem

        Arguments:
        """
        __slots__ = ()
        _cmd = "SYSTem"
        args = []  # type: List[str]

        class CLOCk(SCPINode):
            """
            SYSTem:CLOCk

            Arguments:
            """
            __slots__ = ()
            _cmd = "CLOCk"
            args = []  # type: List[str]

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:CLOCk:SOURce

                Arguments: EXTernal, INTernal
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["EXTernal", "INTernal"]

            SOURce = SOURce()  # type: ignore
            """
            SYSTem:CLOCk:SOURce

            Arguments: EXTernal, INTernal
            """

        CLOCk = CLOCk()  # type: ignore
        """
        SYSTem:CLOCk

        Arguments:
        """

        class COMMunicate(SCPINode):
            """
            SYSTem:COMMunicate

            Arguments:
            """
            __slots__ = ()
            _cmd = "COMMunicate"
            args = []  # type: List[str]

            class NETWork(SCPINode):
                """
                SYSTem:COMMunicate:NETWork

                Arguments:
                """
                __slots__ = ()
                _cmd = "NETWork"
                args = []  # type: List[str]

                class COMMon(SCPINode):
                    """
                    SYSTem:COMMunicate:NETWork:COMMon

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "COMMon"
                    args = []  # type: List[str]

                    class DOMain(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:NETWork:COMMon:DOMain

                        Arguments: 'string'
                        """
                        __slots__ = ()
                        _cmd = "DOMain"
                        args = ["'string'"]

                    DOMain = DOMain()  # type: ignore
                    """
                    SYSTem:COMMunicate:NETWork:COMMon:DOMain

                    Arguments: 'string'
                    """

                    class HOSTname(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:NETWork:COMMon:HOSTname

                        Arguments: 'string'
                        """
                        __slots__ = ()
                        _cmd = "HOSTname"
                        args = ["'string'"]

                    HOSTname = HOSTname()  # type: ignore
                    """
                    SYSTem:COMMunicate:NETWork:COMMon:HOSTname

                    Arguments: 'string'
                    """

                COMMon = COMMon()  # type: ignore
                """
                SYSTem:COMMunicate:NETWork:COMMon

                Arguments:
                """

                class IPADdress(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress

                    Arguments: 'string'
                    """
                    __slots__ = ()
                    _cmd = "IPADdress"
                    args = ["'string'"]

                    class GATeway(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:GATeway

                        Arguments: 'string'
                        """
                        __slots__ = ()
                        _cmd = "GATeway"
                        args = ["'string'"]

                    GATeway = GATeway()  # type: ignore
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress:GATeway

                    Arguments: 'string'
                    """

                    class INFO(SCPINode, SCPIQuery):
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:INFO

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "INFO"
                        args = []  # type: List[str]

                    INFO = INFO()  # type: ignore
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress:INFO

                    Arguments:
                    """

                    class MODE(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:MODE

                        Arguments: AUTO, STATic
                        """
                        __slots__ = ()
                        _cmd = "MODE"
                        args = ["AUTO", "STATic"]

                    MODE = MODE()  # type: ignore
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress:MODE

                    Arguments: AUTO, STATic
                    """

                    class SUBNet(SCPINode):
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:SUBNet

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "SUBNet"
                        args = []  # type: List[str]

                        class MASK(SCPINode, SCPIQuery, SCPISet):
                            """
                            SYSTem:COMMunicate:NETWork:IPADdress:SUBNet:MASK

                            Arguments: 'string'
                            """
                            __slots__ = ()
                            _cmd = "MASK"
                            args = ["'string'"]

                        MASK = MASK()  # type: ignore
                        """
                        SYSTem:COMMunicate:NETWork:IPADdress:SUBNet:MASK

                        Arguments: 'string'
                        """

                    SUBNet = SUBNet()  # type: ignore
                    """
                    SYSTem:COMMunicate:NETWork:IPADdress:SUBNet

                    Arguments:
                    """

                IPADdress = IPADdress()  # type: ignore
                """
                SYSTem:COMMunicate:NETWork:IPADdress

                Arguments: 'string'
                """

                class RESTart(SCPINode, SCPISet):
                    """
                    SYSTem:COMMunicate:NETWork:RESTart

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "RESTart"
                    args = []  # type: List[str]

                RESTart = RESTart()  # type: ignore
                """
                SYSTem:COMMunicate:NETWork:RESTart

                Arguments:
                """

                class RESet(SCPINode, SCPISet):
                    """
                    SYSTem:COMMunicate:NETWork:RESet

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "RESet"
                    args = []  # type: List[str]

                RESet = RESet()  # type: ignore
                """
                SYSTem:COMMunicate:NETWork:RESet

                Arguments:
                """

                class STATus(SCPINode, SCPIQuery):
                    """
                    SYSTem:COMMunicate:NETWork:STATus

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STATus"
                    args = []  # type: List[str]

                STATus = STATus()  # type: ignore
                """
                SYSTem:COMMunicate:NETWork:STATus

                Arguments:
                """

            NETWork = NETWork()  # type: ignore
            """
            SYSTem:COMMunicate:NETWork

            Arguments:
            """

        COMMunicate = COMMunicate()  # type: ignore
        """
        SYSTem:COMMunicate

        Arguments:
        """

        class DFPRint(SCPINode, SCPIQuery):
            """
            SYSTem:DFPRint

            Arguments:
            """
            __slots__ = ()
            _cmd = "DFPRint"
            args = []  # type: List[str]

        DFPRint = DFPRint()  # type: ignore
        """
        SYSTem:DFPRint

        Arguments:
        """

        class ERRor(SCPINode):
            """
            SYSTem:ERRor

            Arguments:
            """
            __slots__ = ()
            _cmd = "ERRor"
            args = []  # type: List[str]

            class ALL(SCPINode, SCPIQuery):
                """
                SYSTem:ERRor:ALL

                Arguments:
                """
                __slots__ = ()
                _cmd = "ALL"
                args = []  # type: List[str]

            ALL = ALL()  # type: ignore
            """
            SYSTem:ERRor:ALL

            Arguments:
            """

            class CODE(SCPINode):
                """
                SYSTem:ERRor:CODE

                Arguments:
                """
                __slots__ = ()
                _cmd = "CODE"
                args = []  # type: List[str]

                class ALL(SCPINode, SCPIQuery):
                    """
                    SYSTem:ERRor:CODE:ALL

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ALL"
                    args = []  # type: List[str]

                ALL = ALL()  # type: ignore
                """
                SYSTem:ERRor:CODE:ALL

                Arguments:
                """

                class NEXT(SCPINode, SCPIQuery):
                    """
                    SYSTem:ERRor:CODE:NEXT

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "NEXT"
                    args = []  # type: List[str]

                NEXT = NEXT()  # type: ignore
                """
                SYSTem:ERRor:CODE:NEXT

                Arguments:
                """

            CODE = CODE()  # type: ignore
            """
            SYSTem:ERRor:CODE

            Arguments:
            """

            class COUNt(SCPINode, SCPIQuery):
                """
                SYSTem:ERRor:COUNt

                Arguments:
                """
                __slots__ = ()
                _cmd = "COUNt"
                args = []  # type: List[str]

            COUNt = COUNt()  # type: ignore
            """
            SYSTem:ERRor:COUNt

            Arguments:
            """

            class NEXT(SCPINode, SCPIQuery):
                """
                SYSTem:ERRor:NEXT

                Arguments:
                """
                __slots__ = ()
                _cmd = "NEXT"
                args = []  # type: List[str]

            NEXT = NEXT()  # type: ignore
            """
            SYSTem:ERRor:NEXT

            Arguments:
            """

        ERRor = ERRor()  # type: ignore
        """
        SYSTem:ERRor

        Arguments:
        """

        class FEATures(SCPINode, SCPIQuery):
            """
            SYSTem:FEATures

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "FEATures"
            args = ["1"]

        FEATures = FEATures()  # type: ignore
        """
        SYSTem:FEATures

        Arguments: 1
        """

        class FWUPdate(SCPINode, SCPISet):
            """
            SYSTem:FWUPdate

            Arguments: <block_data>
            """
            __slots__ = ()
            _cmd = "FWUPdate"
            args = ["<block_data>"]

            class STATus(SCPINode, SCPIQuery):
                """
                SYSTem:FWUPdate:STATus

                Arguments:
                """
                __slots__ = ()
                _cmd = "STATus"
                args = []  # type: List[str]

            STATus = STATus()  # type: ignore
            """
            SYSTem:FWUPdate:STATus

            Arguments:
            """

        FWUPdate = FWUPdate()  # type: ignore
        """
        SYSTem:FWUPdate

        Arguments: <block_data>
        """

        class HELP(SCPINode):
            """
            SYSTem:HELP

            Arguments:
            """
            __slots__ = ()
            _cmd = "HELP"
            args = []  # type: List[str]

            class HEADers(SCPINode, SCPIQuery):
                """
                SYSTem:HELP:HEADers

                Arguments:
                """
                __slots__ = ()
                _cmd = "HEADers"
                args = []  # type: List[str]

            HEADers = HEADers()  # type: ignore
            """
            SYSTem:HELP:HEADers

            Arguments:
            """

            class SYNTax(SCPINode, SCPIQuery):
                """
                SYSTem:HELP:SYNTax

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "SYNTax"
                args = ["'string'"]

                class ALL(SCPINode, SCPIQuery):
                    """
                    SYSTem:HELP:SYNTax:ALL

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ALL"
                    args = []  # type: List[str]

                ALL = ALL()  # type: ignore
                """
                SYSTem:HELP:SYNTax:ALL

                Arguments:
                """

            SYNTax = SYNTax()  # type: ignore
            """
            SYSTem:HELP:SYNTax

            Arguments: 'string'
            """

        HELP = HELP()  # type: ignore
        """
        SYSTem:HELP

        Arguments:
        """

        class INFO(SCPINode, SCPIQuery):
            """
            SYSTem:INFO

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "INFO"
            args = ["'string'"]

        INFO = INFO()  # type: ignore
        """
        SYSTem:INFO

        Arguments: 'string'
        """

        class INITialize(SCPINode, SCPISet):
            """
            SYSTem:INITialize

            Arguments:
            """
            __slots__ = ()
            _cmd = "INITialize"
            args = []  # type: List[str]

        INITialize = INITialize()  # type: ignore
        """
        SYSTem:INITialize

        Arguments:
        """

        class LANGuage(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:LANGuage

            Arguments: SCPI
            """
            __slots__ = ()
            _cmd = "LANGuage"
            args = ["SCPI"]

        LANGuage = LANGuage()  # type: ignore
        """
        SYSTem:LANGuage

        Arguments: SCPI
        """

        class LED(SCPINode):
            """
            SYSTem:LED

            Arguments:
            """
            __slots__ = ()
            _cmd = "LED"
            args = []  # type: List[str]

            class COLor(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:LED:COLor

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "COLor"
                args = ["1"]

            COLor = COLor()  # type: ignore
            """
            SYSTem:LED:COLor

            Arguments: 1
            """

            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:LED:MODE

                Arguments: SENSor, USER
                """
                __slots__ = ()
                _cmd = "MODE"
                args = ["SENSor", "USER"]

            MODE = MODE()  # type: ignore
            """
            SYSTem:LED:MODE

            Arguments: SENSor, USER
            """

        LED = LED()  # type: ignore
        """
        SYSTem:LED

        Arguments:
        """

        class LIMits(SCPINode, SCPIQuery):
            """
            SYSTem:LIMits

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "LIMits"
            args = ["1"]

        LIMits = LIMits()  # type: ignore
        """
        SYSTem:LIMits

        Arguments: 1
        """

        class MINPower(SCPINode, SCPIQuery):
            """
            SYSTem:MINPower

            Arguments:
            """
            __slots__ = ()
            _cmd = "MINPower"
            args = []  # type: List[str]

        MINPower = MINPower()  # type: ignore
        """
        SYSTem:MINPower

        Arguments:
        """

        class PRESet(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:PRESet

            Arguments:
            """
            __slots__ = ()
            _cmd = "PRESet"
            args = []  # type: List[str]

        PRESet = PRESet()  # type: ignore
        """
        SYSTem:PRESet

        Arguments:
        """

        class REBoot(SCPINode, SCPISet):
            """
            SYSTem:REBoot

            Arguments:
            """
            __slots__ = ()
            _cmd = "REBoot"
            args = []  # type: List[str]

        REBoot = REBoot()  # type: ignore
        """
        SYSTem:REBoot

        Arguments:
        """

        class RUTime(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:RUTime

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "RUTime"
            args = ["1"]

        RUTime = RUTime()  # type: ignore
        """
        SYSTem:RUTime

        Arguments: 1
        """

        class SENSor(SCPINode):
            """
            SYSTem:SENSor

            Arguments:
            """
            __slots__ = ()
            _cmd = "SENSor"
            args = []  # type: List[str]

            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:SENSor:NAME

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "NAME"
                args = ["'string'"]

            NAME = NAME()  # type: ignore
            """
            SYSTem:SENSor:NAME

            Arguments: 'string'
            """

        SENSor = SENSor()  # type: ignore
        """
        SYSTem:SENSor

        Arguments:
        """

        class SERRor(SCPINode, SCPIQuery):
            """
            SYSTem:SERRor

            Arguments:
            """
            __slots__ = ()
            _cmd = "SERRor"
            args = []  # type: List[str]

            class LIST(SCPINode):
                """
                SYSTem:SERRor:LIST

                Arguments:
                """
                __slots__ = ()
                _cmd = "LIST"
                args = []  # type: List[str]

                class ALL(SCPINode, SCPIQuery):
                    """
                    SYSTem:SERRor:LIST:ALL

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ALL"
                    args = []  # type: List[str]

                ALL = ALL()  # type: ignore
                """
                SYSTem:SERRor:LIST:ALL

                Arguments:
                """

                class NEXT(SCPINode, SCPIQuery):
                    """
                    SYSTem:SERRor:LIST:NEXT

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "NEXT"
                    args = []  # type: List[str]

                NEXT = NEXT()  # type: ignore
                """
                SYSTem:SERRor:LIST:NEXT

                Arguments:
                """

            LIST = LIST()  # type: ignore
            """
            SYSTem:SERRor:LIST

            Arguments:
            """

        SERRor = SERRor()  # type: ignore
        """
        SYSTem:SERRor

        Arguments:
        """

        class SUTime(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:SUTime

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "SUTime"
            args = ["1"]

        SUTime = SUTime()  # type: ignore
        """
        SYSTem:SUTime

        Arguments: 1
        """

        class TLEVels(SCPINode, SCPIQuery):
            """
            SYSTem:TLEVels

            Arguments:
            """
            __slots__ = ()
            _cmd = "TLEVels"
            args = []  # type: List[str]

        TLEVels = TLEVels()  # type: ignore
        """
        SYSTem:TLEVels

        Arguments:
        """

        class TRANsaction(SCPINode):
            """
            SYSTem:TRANsaction

            Arguments:
            """
            __slots__ = ()
            _cmd = "TRANsaction"
            args = []  # type: List[str]

            class BEGin(SCPINode, SCPISet):
                """
                SYSTem:TRANsaction:BEGin

                Arguments:
                """
                __slots__ = ()
                _cmd = "BEGin"
                args = []  # type: List[str]

            BEGin = BEGin()  # type: ignore
            """
            SYSTem:TRANsaction:BEGin

            Arguments:
            """

            class END(SCPINode, SCPISet):
                """
                SYSTem:TRANsaction:END

                Arguments:
                """
                __slots__ = ()
                _cmd = "END"
                args = []  # type: List[str]

            END = END()  # type: ignore
            """
            SYSTem:TRANsaction:END

            Arguments:
            """

        TRANsaction = TRANsaction()  # type: ignore
        """
        SYSTem:TRANsaction

        Arguments:
        """

        class VERSion(SCPINode, SCPIQuery):
            """
            SYSTem:VERSion

            Arguments:
            """
            __slots__ = ()
            _cmd = "VERSion"
            args = []  # type: List[str]

        VERSion = VERSion()  # type: ignore
        """
        SYSTem:VERSion

        Arguments:
        """

    SYSTem = SYSTem()  # type: ignore
    """
    SYSTem

    Arguments:
    """

    class TEST(SCPINode):
        """
        TEST

        Arguments:
        """
        __slots__ = ()
        _cmd = "TEST"
        args = []  # type: List[str]

        class SENSor(SCPINode, SCPIQuery):
            """
            TEST:SENSor

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "SENSor"
            args = ["'string'"]

        SENSor = SENSor()  # type: ignore
        """
        TEST:SENSor

        Arguments: 'string'
        """

    TEST = TEST()  # type: ignore
    """
    TEST

    Arguments:
    """

    class TRIGger(SCPINode):
        """
        TRIGger

        Arguments:
        """
        __slots__ = ()
        _cmd = "TRIGger"
        args = []  # type: List[str]

        class ATRigger(SCPINode):
            """
            TRIGger:ATRigger

            Arguments:
            """
            __slots__ = ()
            _cmd = "ATRigger"
            args = []  # type: List[str]

            class DELay(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:ATRigger:DELay

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DELay"
                args = ["1"]

            DELay = DELay()  # type: ignore
            """
            TRIGger:ATRigger:DELay

            Arguments: 1
            """

            class EXECuted(SCPINode, SCPIQuery):
                """
                TRIGger:ATRigger:EXECuted

                Arguments:
                """
                __slots__ = ()
                _cmd = "EXECuted"
                args = []  # type: List[str]

            EXECuted = EXECuted()  # type: ignore
            """
            TRIGger:ATRigger:EXECuted

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                TRIGger:ATRigger:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            TRIGger:ATRigger:STATe

            Arguments: 1, ON, OFF
            """

        ATRigger = ATRigger()  # type: ignore
        """
        TRIGger:ATRigger

        Arguments:
        """

        class COUNt(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:COUNt

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "COUNt"
            args = ["1"]

        COUNt = COUNt()  # type: ignore
        """
        TRIGger:COUNt

        Arguments: 1
        """

        class DELay(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:DELay

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "DELay"
            args = ["1"]

            class AUTO(SCPINode, SCPIBool):
                """
                TRIGger:DELay:AUTO

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "AUTO"
                args = ["1", "ON", "OFF"]

            AUTO = AUTO()  # type: ignore
            """
            TRIGger:DELay:AUTO

            Arguments: 1, ON, OFF
            """

        DELay = DELay()  # type: ignore
        """
        TRIGger:DELay

        Arguments: 1
        """

        class DTIMe(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:DTIMe

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "DTIMe"
            args = ["1"]

        DTIMe = DTIMe()  # type: ignore
        """
        TRIGger:DTIMe

        Arguments: 1
        """

        class EXTernal(SCPINodeN):
            """
            TRIGger:EXTernal

            Arguments:
            """
            __slots__ = ()
            _cmd = "EXTernal"
            args = []  # type: List[str]

            class IMPedance(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:EXTernal:IMPedance

                Arguments: HIGH, LOW
                """
                __slots__ = ()
                _cmd = "IMPedance"
                args = ["HIGH", "LOW"]

            IMPedance = IMPedance()  # type: ignore
            """
            TRIGger:EXTernal:IMPedance

            Arguments: HIGH, LOW
            """

        EXTernal = EXTernal()  # type: ignore
        """
        TRIGger:EXTernal

        Arguments:
        """

        class HOLDoff(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:HOLDoff

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "HOLDoff"
            args = ["1"]

        HOLDoff = HOLDoff()  # type: ignore
        """
        TRIGger:HOLDoff

        Arguments: 1
        """

        class HYSTeresis(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:HYSTeresis

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "HYSTeresis"
            args = ["1"]

        HYSTeresis = HYSTeresis()  # type: ignore
        """
        TRIGger:HYSTeresis

        Arguments: 1
        """

        class IMMediate(SCPINode, SCPISet):
            """
            TRIGger:IMMediate

            Arguments:
            """
            __slots__ = ()
            _cmd = "IMMediate"
            args = []  # type: List[str]

        IMMediate = IMMediate()  # type: ignore
        """
        TRIGger:IMMediate

        Arguments:
        """

        class LEVel(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:LEVel

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "LEVel"
            args = ["1"]

        LEVel = LEVel()  # type: ignore
        """
        TRIGger:LEVel

        Arguments: 1
        """

        class MASTer(SCPINode):
            """
            TRIGger:MASTer

            Arguments:
            """
            __slots__ = ()
            _cmd = "MASTer"
            args = []  # type: List[str]

            class PORT(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:MASTer:PORT

                Arguments: EXT1, EXT2, EXTernal1, EXTernal2
                """
                __slots__ = ()
                _cmd = "PORT"
                args = ["EXT1", "EXT2", "EXTernal1", "EXTernal2"]

            PORT = PORT()  # type: ignore
            """
            TRIGger:MASTer:PORT

            Arguments: EXT1, EXT2, EXTernal1, EXTernal2
            """

            class STATe(SCPINode, SCPIBool):
                """
                TRIGger:MASTer:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            TRIGger:MASTer:STATe

            Arguments: 1, ON, OFF
            """

        MASTer = MASTer()  # type: ignore
        """
        TRIGger:MASTer

        Arguments:
        """

        class SLOPe(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:SLOPe

            Arguments: NEGative, POSitive
            """
            __slots__ = ()
            _cmd = "SLOPe"
            args = ["NEGative", "POSitive"]

        SLOPe = SLOPe()  # type: ignore
        """
        TRIGger:SLOPe

        Arguments: NEGative, POSitive
        """

        class SOURce(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:SOURce

            Arguments: BUS, EXT1, EXT2, EXTernal, EXTernal1, EXTernal2, HOLD, IMMediate, INTernal
            """
            __slots__ = ()
            _cmd = "SOURce"
            args = ["BUS", "EXT1", "EXT2", "EXTernal", "EXTernal1", "EXTernal2", "HOLD", "IMMediate", "INTernal"]

        SOURce = SOURce()  # type: ignore
        """
        TRIGger:SOURce

        Arguments: BUS, EXT1, EXT2, EXTernal, EXTernal1, EXTernal2, HOLD, IMMediate, INTernal
        """

        class SYNC(SCPINode):
            """
            TRIGger:SYNC

            Arguments:
            """
            __slots__ = ()
            _cmd = "SYNC"
            args = []  # type: List[str]

            class PORT(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:SYNC:PORT

                Arguments: EXT1, EXT2, EXTernal1, EXTernal2
                """
                __slots__ = ()
                _cmd = "PORT"
                args = ["EXT1", "EXT2", "EXTernal1", "EXTernal2"]

            PORT = PORT()  # type: ignore
            """
            TRIGger:SYNC:PORT

            Arguments: EXT1, EXT2, EXTernal1, EXTernal2
            """

            class STATe(SCPINode, SCPIBool):
                """
                TRIGger:SYNC:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            TRIGger:SYNC:STATe

            Arguments: 1, ON, OFF
            """

        SYNC = SYNC()  # type: ignore
        """
        TRIGger:SYNC

        Arguments:
        """

    TRIGger = TRIGger()  # type: ignore
    """
    TRIGger

    Arguments:
    """

    class UNIT(SCPINode):
        """
        UNIT

        Arguments:
        """
        __slots__ = ()
        _cmd = "UNIT"
        args = []  # type: List[str]

        class POWer(SCPINode, SCPIQuery, SCPISet):
            """
            UNIT:POWer

            Arguments: DBM, DBUV, W
            """
            __slots__ = ()
            _cmd = "POWer"
            args = ["DBM", "DBUV", "W"]

        POWer = POWer()  # type: ignore
        """
        UNIT:POWer

        Arguments: DBM, DBUV, W
        """

    UNIT = UNIT()  # type: ignore
    """
    UNIT

    Arguments:
    """


NRPxxSN_gen._SCPI_class = NRPxxSN_gen
# END OF NRPxxSN_gen
