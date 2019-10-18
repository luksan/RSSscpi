# -*- coding: utf-8 -*-
# Generated from SMB100A_syntax.txt on 2019-10-18 15:03
from typing import List
from RSSscpi.SCPI_gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool
from RSSscpi.Instrument import Instrument


class SMB100A_gen(SCPINode):
    _cmd = ""

    class ABO(SCPINode, SCPISet):
        """
        &ABO

        Arguments:
        """
        __slots__ = ()
        _cmd = "&ABO"
        args = []  # type: List[str]

    ABO = ABO()  # type: ignore
    """
    &ABO

    Arguments:
    """

    class BRK(SCPINode, SCPISet):
        """
        &BRK

        Arguments:
        """
        __slots__ = ()
        _cmd = "&BRK"
        args = []  # type: List[str]

    BRK = BRK()  # type: ignore
    """
    &BRK

    Arguments:
    """

    class DCL(SCPINode, SCPISet):
        """
        &DCL

        Arguments:
        """
        __slots__ = ()
        _cmd = "&DCL"
        args = []  # type: List[str]

    DCL = DCL()  # type: ignore
    """
    &DCL

    Arguments:
    """

    class DFC(SCPINode, SCPISet):
        """
        &DFC

        Arguments:
        """
        __slots__ = ()
        _cmd = "&DFC"
        args = []  # type: List[str]

    DFC = DFC()  # type: ignore
    """
    &DFC

    Arguments:
    """

    class GET(SCPINode, SCPISet):
        """
        &GET

        Arguments:
        """
        __slots__ = ()
        _cmd = "&GET"
        args = []  # type: List[str]

    GET = GET()  # type: ignore
    """
    &GET

    Arguments:
    """

    class GTL(SCPINode, SCPISet):
        """
        &GTL

        Arguments:
        """
        __slots__ = ()
        _cmd = "&GTL"
        args = []  # type: List[str]

    GTL = GTL()  # type: ignore
    """
    &GTL

    Arguments:
    """

    class GTM(SCPINode, SCPISet):
        """
        &GTM

        Arguments:
        """
        __slots__ = ()
        _cmd = "&GTM"
        args = []  # type: List[str]

    GTM = GTM()  # type: ignore
    """
    &GTM

    Arguments:
    """

    class GTR(SCPINode, SCPISet):
        """
        &GTR

        Arguments:
        """
        __slots__ = ()
        _cmd = "&GTR"
        args = []  # type: List[str]

    GTR = GTR()  # type: ignore
    """
    &GTR

    Arguments:
    """

    class HFC(SCPINode, SCPISet):
        """
        &HFC

        Arguments:
        """
        __slots__ = ()
        _cmd = "&HFC"
        args = []  # type: List[str]

    HFC = HFC()  # type: ignore
    """
    &HFC

    Arguments:
    """

    class NREN(SCPINode, SCPISet):
        """
        &NREN

        Arguments:
        """
        __slots__ = ()
        _cmd = "&NREN"
        args = []  # type: List[str]

    NREN = NREN()  # type: ignore
    """
    &NREN

    Arguments:
    """

    class POL(SCPINode, SCPISet):
        """
        &POL

        Arguments:
        """
        __slots__ = ()
        _cmd = "&POL"
        args = []  # type: List[str]

    POL = POL()  # type: ignore
    """
    &POL

    Arguments:
    """

    class RLSD(SCPINode, SCPISet):
        """
        &RLSD

        Arguments:
        """
        __slots__ = ()
        _cmd = "&RLSD"
        args = []  # type: List[str]

    RLSD = RLSD()  # type: ignore
    """
    &RLSD

    Arguments:
    """

    class SFC(SCPINode, SCPISet):
        """
        &SFC

        Arguments:
        """
        __slots__ = ()
        _cmd = "&SFC"
        args = []  # type: List[str]

    SFC = SFC()  # type: ignore
    """
    &SFC

    Arguments:
    """

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

    class DEV(SCPINode, SCPIQuery, SCPISet):
        """
        *DEV

        Arguments: 1
        """
        __slots__ = ()
        _cmd = "*DEV"
        args = ["1"]

    DEV = DEV()  # type: ignore
    """
    *DEV

    Arguments: 1
    """

    class DMC(SCPINode, SCPIQuery, SCPISet):
        """
        *DMC

        Arguments: <string>,<string>
        """
        __slots__ = ()
        _cmd = "*DMC"
        args = ["<string>,<string>"]

    DMC = DMC()  # type: ignore
    """
    *DMC

    Arguments: <string>,<string>
    """

    class EMC(SCPINode, SCPIBool):
        """
        *EMC

        Arguments: 1, ON, OFF
        """
        __slots__ = ()
        _cmd = "*EMC"
        args = ["1", "ON", "OFF"]

    EMC = EMC()  # type: ignore
    """
    *EMC

    Arguments: 1, ON, OFF
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

    class GCLS(SCPINode, SCPISet):
        """
        *GCLS

        Arguments:
        """
        __slots__ = ()
        _cmd = "*GCLS"
        args = []  # type: List[str]

    GCLS = GCLS()  # type: ignore
    """
    *GCLS

    Arguments:
    """

    class GMC(SCPINode, SCPIQuery):
        """
        *GMC

        Arguments: 'string'
        """
        __slots__ = ()
        _cmd = "*GMC"
        args = ["'string'"]

    GMC = GMC()  # type: ignore
    """
    *GMC

    Arguments: 'string'
    """

    class GOPC(SCPINode, SCPIQuery):
        """
        *GOPC

        Arguments:
        """
        __slots__ = ()
        _cmd = "*GOPC"
        args = []  # type: List[str]

    GOPC = GOPC()  # type: ignore
    """
    *GOPC

    Arguments:
    """

    class GWAI(SCPINode, SCPISet):
        """
        *GWAI

        Arguments:
        """
        __slots__ = ()
        _cmd = "*GWAI"
        args = []  # type: List[str]

    GWAI = GWAI()  # type: ignore
    """
    *GWAI

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

    class LMC(SCPINode, SCPIQuery):
        """
        *LMC

        Arguments:
        """
        __slots__ = ()
        _cmd = "*LMC"
        args = []  # type: List[str]

    LMC = LMC()  # type: ignore
    """
    *LMC

    Arguments:
    """

    class LRN(SCPINode, SCPIQuery):
        """
        *LRN

        Arguments:
        """
        __slots__ = ()
        _cmd = "*LRN"
        args = []  # type: List[str]

    LRN = LRN()  # type: ignore
    """
    *LRN

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

    class PMC(SCPINode, SCPISet):
        """
        *PMC

        Arguments:
        """
        __slots__ = ()
        _cmd = "*PMC"
        args = []  # type: List[str]

    PMC = PMC()  # type: ignore
    """
    *PMC

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

    class PSC(SCPINode, SCPIBool):
        """
        *PSC

        Arguments: 1, ON, OFF
        """
        __slots__ = ()
        _cmd = "*PSC"
        args = ["1", "ON", "OFF"]

    PSC = PSC()  # type: ignore
    """
    *PSC

    Arguments: 1, ON, OFF
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

    class RMC(SCPINode, SCPISet):
        """
        *RMC

        Arguments: 'string'
        """
        __slots__ = ()
        _cmd = "*RMC"
        args = ["'string'"]

    RMC = RMC()  # type: ignore
    """
    *RMC

    Arguments: 'string'
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

    class SRQ(SCPINode, SCPIQuery):
        """
        *SRQ

        Arguments: <integer>, DOWN, MAXimum, MINimum, UP
        """
        __slots__ = ()
        _cmd = "*SRQ"
        args = ["<integer>", "DOWN", "MAXimum", "MINimum", "UP"]

    SRQ = SRQ()  # type: ignore
    """
    *SRQ

    Arguments: <integer>, DOWN, MAXimum, MINimum, UP
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

    class XESE(SCPINode, SCPIQuery, SCPISet):
        """
        *XESE

        Arguments: <expression>
        """
        __slots__ = ()
        _cmd = "*XESE"
        args = ["<expression>"]

    XESE = XESE()  # type: ignore
    """
    *XESE

    Arguments: <expression>
    """

    class XESR(SCPINode, SCPIQuery):
        """
        *XESR

        Arguments:
        """
        __slots__ = ()
        _cmd = "*XESR"
        args = []  # type: List[str]

    XESR = XESR()  # type: ignore
    """
    *XESR

    Arguments:
    """

    class XPRE(SCPINode, SCPIQuery, SCPISet):
        """
        *XPRE

        Arguments: <expression>
        """
        __slots__ = ()
        _cmd = "*XPRE"
        args = ["<expression>"]

    XPRE = XPRE()  # type: ignore
    """
    *XPRE

    Arguments: <expression>
    """

    class XSRE(SCPINode, SCPIQuery, SCPISet):
        """
        *XSRE

        Arguments: <expression>
        """
        __slots__ = ()
        _cmd = "*XSRE"
        args = ["<expression>"]

    XSRE = XSRE()  # type: ignore
    """
    *XSRE

    Arguments: <expression>
    """

    class XSTB(SCPINode, SCPIQuery):
        """
        *XSTB

        Arguments:
        """
        __slots__ = ()
        _cmd = "*XSTB"
        args = []  # type: List[str]

    XSTB = XSTB()  # type: ignore
    """
    *XSTB

    Arguments:
    """

    class LLO(SCPINode, SCPISet):
        """
        @LLO

        Arguments:
        """
        __slots__ = ()
        _cmd = "@LLO"
        args = []  # type: List[str]

    LLO = LLO()  # type: ignore
    """
    @LLO

    Arguments:
    """

    class LOC(SCPINode, SCPISet):
        """
        @LOC

        Arguments:
        """
        __slots__ = ()
        _cmd = "@LOC"
        args = []  # type: List[str]

    LOC = LOC()  # type: ignore
    """
    @LOC

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

        class MSEQuence(SCPINode, SCPISet):
            """
            ABORt:MSEQuence

            Arguments:
            """
            __slots__ = ()
            _cmd = "MSEQuence"
            args = []  # type: List[str]

        MSEQuence = MSEQuence()  # type: ignore
        """
        ABORt:MSEQuence

        Arguments:
        """

        class SWEep(SCPINode, SCPISet):
            """
            ABORt:SWEep

            Arguments:
            """
            __slots__ = ()
            _cmd = "SWEep"
            args = []  # type: List[str]

        SWEep = SWEep()  # type: ignore
        """
        ABORt:SWEep

        Arguments:
        """

    ABORt = ABORt()  # type: ignore
    """
    ABORt

    Arguments:
    """

    class AMPLitude(SCPINode):
        """
        AMPLitude

        Arguments:
        """
        __slots__ = ()
        _cmd = "AMPLitude"
        args = []  # type: List[str]

        class OUT(SCPINode):
            """
            AMPLitude:OUT

            Arguments:
            """
            __slots__ = ()
            _cmd = "OUT"
            args = []  # type: List[str]

            class ALC(SCPINode):
                """
                AMPLitude:OUT:ALC

                Arguments:
                """
                __slots__ = ()
                _cmd = "ALC"
                args = []  # type: List[str]

                class BANDwidth(SCPINode, SCPISet):
                    """
                    AMPLitude:OUT:ALC:BANDwidth

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "BANDwidth"
                    args = []  # type: List[str]

                BANDwidth = BANDwidth()  # type: ignore
                """
                AMPLitude:OUT:ALC:BANDwidth

                Arguments:
                """

            ALC = ALC()  # type: ignore
            """
            AMPLitude:OUT:ALC

            Arguments:
            """

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:OUT:ATTenuation

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ATTenuation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    AMPLitude:OUT:ATTenuation:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        AMPLitude:OUT:ATTenuation:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    AMPLitude:OUT:ATTenuation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                AMPLitude:OUT:ATTenuation:STEP

                Arguments:
                """

            ATTenuation = ATTenuation()  # type: ignore
            """
            AMPLitude:OUT:ATTenuation

            Arguments: 1
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:OUT:LEVel

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "LEVel"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    AMPLitude:OUT:LEVel:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        AMPLitude:OUT:LEVel:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    AMPLitude:OUT:LEVel:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                AMPLitude:OUT:LEVel:STEP

                Arguments:
                """

            LEVel = LEVel()  # type: ignore
            """
            AMPLitude:OUT:LEVel

            Arguments: 1
            """

            class MUTing(SCPINode, SCPIBool):
                """
                AMPLitude:OUT:MUTing

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "MUTing"
                args = ["1", "ON", "OFF"]

            MUTing = MUTing()  # type: ignore
            """
            AMPLitude:OUT:MUTing

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                AMPLitude:OUT:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            AMPLitude:OUT:STATe

            Arguments: 1, ON, OFF
            """

            class ULIMit(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:OUT:ULIMit

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ULIMit"
                args = ["1"]

            ULIMit = ULIMit()  # type: ignore
            """
            AMPLitude:OUT:ULIMit

            Arguments: 1
            """

        OUT = OUT()  # type: ignore
        """
        AMPLitude:OUT

        Arguments:
        """

        class SOURce(SCPINode):
            """
            AMPLitude:SOURce

            Arguments:
            """
            __slots__ = ()
            _cmd = "SOURce"
            args = []  # type: List[str]

            class ALC(SCPINode):
                """
                AMPLitude:SOURce:ALC

                Arguments:
                """
                __slots__ = ()
                _cmd = "ALC"
                args = []  # type: List[str]

                class BANDwidth(SCPINode, SCPISet):
                    """
                    AMPLitude:SOURce:ALC:BANDwidth

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "BANDwidth"
                    args = []  # type: List[str]

                BANDwidth = BANDwidth()  # type: ignore
                """
                AMPLitude:SOURce:ALC:BANDwidth

                Arguments:
                """

            ALC = ALC()  # type: ignore
            """
            AMPLitude:SOURce:ALC

            Arguments:
            """

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:SOURce:ATTenuation

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ATTenuation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    AMPLitude:SOURce:ATTenuation:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        AMPLitude:SOURce:ATTenuation:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    AMPLitude:SOURce:ATTenuation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                AMPLitude:SOURce:ATTenuation:STEP

                Arguments:
                """

            ATTenuation = ATTenuation()  # type: ignore
            """
            AMPLitude:SOURce:ATTenuation

            Arguments: 1
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:SOURce:LEVel

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "LEVel"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    AMPLitude:SOURce:LEVel:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        AMPLitude:SOURce:LEVel:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    AMPLitude:SOURce:LEVel:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                AMPLitude:SOURce:LEVel:STEP

                Arguments:
                """

            LEVel = LEVel()  # type: ignore
            """
            AMPLitude:SOURce:LEVel

            Arguments: 1
            """

            class MUTing(SCPINode, SCPIBool):
                """
                AMPLitude:SOURce:MUTing

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "MUTing"
                args = ["1", "ON", "OFF"]

            MUTing = MUTing()  # type: ignore
            """
            AMPLitude:SOURce:MUTing

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                AMPLitude:SOURce:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            AMPLitude:SOURce:STATe

            Arguments: 1, ON, OFF
            """

            class ULIMit(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:SOURce:ULIMit

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ULIMit"
                args = ["1"]

            ULIMit = ULIMit()  # type: ignore
            """
            AMPLitude:SOURce:ULIMit

            Arguments: 1
            """

        SOURce = SOURce()  # type: ignore
        """
        AMPLitude:SOURce

        Arguments:
        """

    AMPLitude = AMPLitude()  # type: ignore
    """
    AMPLitude

    Arguments:
    """

    class ATT0(SCPINodeN, SCPIQuery, SCPISet):
        """
        ATT0

        Arguments:
        """
        __slots__ = ()
        _cmd = "ATT0"
        args = []  # type: List[str]

    ATT0 = ATT0()  # type: ignore
    """
    ATT0

    Arguments:
    """

    class ATT1(SCPINodeN, SCPIQuery, SCPISet):
        """
        ATT1

        Arguments:
        """
        __slots__ = ()
        _cmd = "ATT1"
        args = []  # type: List[str]

    ATT1 = ATT1()  # type: ignore
    """
    ATT1

    Arguments:
    """

    class ATTen(SCPINode, SCPIQuery):
        """
        ATTen

        Arguments:
        """
        __slots__ = ()
        _cmd = "ATTen"
        args = []  # type: List[str]

        class UNLock(SCPINode, SCPISet):
            """
            ATTen:UNLock

            Arguments:
            """
            __slots__ = ()
            _cmd = "UNLock"
            args = []  # type: List[str]

        UNLock = UNLock()  # type: ignore
        """
        ATTen:UNLock

        Arguments:
        """

    ATTen = ATTen()  # type: ignore
    """
    ATTen

    Arguments:
    """

    class ATtenuator(SCPINode, SCPIQuery):
        """
        ATtenuator

        Arguments:
        """
        __slots__ = ()
        _cmd = "ATtenuator"
        args = []  # type: List[str]

        class Cont(SCPINode, SCPIQuery):
            """
            ATtenuator:Cont

            Arguments:
            """
            __slots__ = ()
            _cmd = "Cont"
            args = []  # type: List[str]

        Cont = Cont()  # type: ignore
        """
        ATtenuator:Cont

        Arguments:
        """

        class Fixed(SCPINode, SCPISet):
            """
            ATtenuator:Fixed

            Arguments:
            """
            __slots__ = ()
            _cmd = "Fixed"
            args = []  # type: List[str]

        Fixed = Fixed()  # type: ignore
        """
        ATtenuator:Fixed

        Arguments:
        """

        class Normal(SCPINode, SCPISet):
            """
            ATtenuator:Normal

            Arguments:
            """
            __slots__ = ()
            _cmd = "Normal"
            args = []  # type: List[str]

        Normal = Normal()  # type: ignore
        """
        ATtenuator:Normal

        Arguments:
        """

    ATtenuator = ATtenuator()  # type: ignore
    """
    ATtenuator

    Arguments:
    """

    class BLANk(SCPINode, SCPIQuery, SCPISet):
        """
        BLANk

        Arguments: 1
        """
        __slots__ = ()
        _cmd = "BLANk"
        args = ["1"]

    BLANk = BLANk()  # type: ignore
    """
    BLANk

    Arguments: 1
    """

    class Blank(SCPINode, SCPIQuery):
        """
        Blank

        Arguments:
        """
        __slots__ = ()
        _cmd = "Blank"
        args = []  # type: List[str]

        class Inverted(SCPINode, SCPISet):
            """
            Blank:Inverted

            Arguments:
            """
            __slots__ = ()
            _cmd = "Inverted"
            args = []  # type: List[str]

        Inverted = Inverted()  # type: ignore
        """
        Blank:Inverted

        Arguments:
        """

        class Normal(SCPINode, SCPISet):
            """
            Blank:Normal

            Arguments:
            """
            __slots__ = ()
            _cmd = "Normal"
            args = []  # type: List[str]

        Normal = Normal()  # type: ignore
        """
        Blank:Normal

        Arguments:
        """

    Blank = Blank()  # type: ignore
    """
    Blank

    Arguments:
    """

    class CALibration(SCPINode, SCPISet):
        """
        CALibration

        Arguments:
        """
        __slots__ = ()
        _cmd = "CALibration"
        args = []  # type: List[str]

        class AMPLitude(SCPINode, SCPISet):
            """
            CALibration:AMPLitude

            Arguments:
            """
            __slots__ = ()
            _cmd = "AMPLitude"
            args = []  # type: List[str]

            class STATe(SCPINode, SCPIBool):
                """
                CALibration:AMPLitude:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            CALibration:AMPLitude:STATe

            Arguments: 1, ON, OFF
            """

        AMPLitude = AMPLitude()  # type: ignore
        """
        CALibration:AMPLitude

        Arguments:
        """

        class ATTenuator(SCPINode):
            """
            CALibration:ATTenuator

            Arguments:
            """
            __slots__ = ()
            _cmd = "ATTenuator"
            args = []  # type: List[str]

            class STATe(SCPINode, SCPIBool):
                """
                CALibration:ATTenuator:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            CALibration:ATTenuator:STATe

            Arguments: 1, ON, OFF
            """

        ATTenuator = ATTenuator()  # type: ignore
        """
        CALibration:ATTenuator

        Arguments:
        """

        class FM(SCPINode):
            """
            CALibration:FM

            Arguments:
            """
            __slots__ = ()
            _cmd = "FM"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:FM:MEASure

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = []  # type: List[str]

            MEASure = MEASure()  # type: ignore
            """
            CALibration:FM:MEASure

            Arguments:
            """

            class OFFSet(SCPINode, SCPIQuery):
                """
                CALibration:FM:OFFSet

                Arguments:
                """
                __slots__ = ()
                _cmd = "OFFSet"
                args = []  # type: List[str]

            OFFSet = OFFSet()  # type: ignore
            """
            CALibration:FM:OFFSet

            Arguments:
            """

        FM = FM()  # type: ignore
        """
        CALibration:FM

        Arguments:
        """

        class FMOFfset(SCPINode):
            """
            CALibration:FMOFfset

            Arguments:
            """
            __slots__ = ()
            _cmd = "FMOFfset"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                `CALibration:FMOFfset:MEASure
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/11b75bf573884132.htm#ID_b719b8434e4cb5ae0a00206a008f2019-9245ed064e4cb5ae0a00206a0024546d-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = []  # type: List[str]

            MEASure = MEASure()  # type: ignore
            """
            `CALibration:FMOFfset:MEASure
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/11b75bf573884132.htm#ID_b719b8434e4cb5ae0a00206a008f2019-9245ed064e4cb5ae0a00206a0024546d-en-US>`_

            Arguments:
            """

        FMOFfset = FMOFfset()  # type: ignore
        """
        CALibration:FMOFfset

        Arguments:
        """

        class HARMfilter(SCPINode):
            """
            CALibration:HARMfilter

            Arguments:
            """
            __slots__ = ()
            _cmd = "HARMfilter"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:HARMfilter:MEASure

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = []  # type: List[str]

            MEASure = MEASure()  # type: ignore
            """
            CALibration:HARMfilter:MEASure

            Arguments:
            """

        HARMfilter = HARMfilter()  # type: ignore
        """
        CALibration:HARMfilter

        Arguments:
        """

        class IFFilter(SCPINode):
            """
            CALibration:IFFilter

            Arguments:
            """
            __slots__ = ()
            _cmd = "IFFilter"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:IFFilter:MEASure

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = []  # type: List[str]

            MEASure = MEASure()  # type: ignore
            """
            CALibration:IFFilter:MEASure

            Arguments:
            """

        IFFilter = IFFilter()  # type: ignore
        """
        CALibration:IFFilter

        Arguments:
        """

        class IQ(SCPINode):
            """
            CALibration:IQ

            Arguments:
            """
            __slots__ = ()
            _cmd = "IQ"
            args = []  # type: List[str]

            class DEFault(SCPINode, SCPISet):
                """
                CALibration:IQ:DEFault

                Arguments:
                """
                __slots__ = ()
                _cmd = "DEFault"
                args = []  # type: List[str]

            DEFault = DEFault()  # type: ignore
            """
            CALibration:IQ:DEFault

            Arguments:
            """

            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                CALibration:IQ:STARt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()  # type: ignore
            """
            CALibration:IQ:STARt

            Arguments: 1
            """

        IQ = IQ()  # type: ignore
        """
        CALibration:IQ

        Arguments:
        """

        class LEVel(SCPINode, SCPISet):
            """
            CALibration:LEVel

            Arguments:
            """
            __slots__ = ()
            _cmd = "LEVel"
            args = []  # type: List[str]

            class FRANge(SCPINode, SCPIQuery, SCPISet):
                """
                CALibration:LEVel:FRANge

                Arguments: MIXer, NORMal
                """
                __slots__ = ()
                _cmd = "FRANge"
                args = ["MIXer", "NORMal"]

            FRANge = FRANge()  # type: ignore
            """
            CALibration:LEVel:FRANge

            Arguments: MIXer, NORMal
            """

            class PMODulator(SCPINode, SCPIBool):
                """
                CALibration:LEVel:PMODulator

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "PMODulator"
                args = ["1", "ON", "OFF"]

            PMODulator = PMODulator()  # type: ignore
            """
            CALibration:LEVel:PMODulator

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                CALibration:LEVel:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            CALibration:LEVel:STATe

            Arguments: 1, ON, OFF
            """

        LEVel = LEVel()  # type: ignore
        """
        CALibration:LEVel

        Arguments:
        """

        class LFGenlevel(SCPINode):
            """
            CALibration:LFGenlevel

            Arguments:
            """
            __slots__ = ()
            _cmd = "LFGenlevel"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:LFGenlevel:MEASure

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = []  # type: List[str]

            MEASure = MEASure()  # type: ignore
            """
            CALibration:LFGenlevel:MEASure

            Arguments:
            """

        LFGenlevel = LFGenlevel()  # type: ignore
        """
        CALibration:LFGenlevel

        Arguments:
        """

        class LFReset(SCPINode):
            """
            CALibration:LFReset

            Arguments:
            """
            __slots__ = ()
            _cmd = "LFReset"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:LFReset:MEASure

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = []  # type: List[str]

            MEASure = MEASure()  # type: ignore
            """
            CALibration:LFReset:MEASure

            Arguments:
            """

        LFReset = LFReset()  # type: ignore
        """
        CALibration:LFReset

        Arguments:
        """

        class MAINloop(SCPINode):
            """
            CALibration:MAINloop

            Arguments:
            """
            __slots__ = ()
            _cmd = "MAINloop"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:MAINloop:MEASure

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = []  # type: List[str]

            MEASure = MEASure()  # type: ignore
            """
            CALibration:MAINloop:MEASure

            Arguments:
            """

        MAINloop = MAINloop()  # type: ignore
        """
        CALibration:MAINloop

        Arguments:
        """

        class MULTfilter(SCPINode):
            """
            CALibration:MULTfilter

            Arguments:
            """
            __slots__ = ()
            _cmd = "MULTfilter"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:MULTfilter:MEASure

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = []  # type: List[str]

            MEASure = MEASure()  # type: ignore
            """
            CALibration:MULTfilter:MEASure

            Arguments:
            """

        MULTfilter = MULTfilter()  # type: ignore
        """
        CALibration:MULTfilter

        Arguments:
        """

        class PULSe(SCPINode):
            """
            CALibration:PULSe

            Arguments:
            """
            __slots__ = ()
            _cmd = "PULSe"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:PULSe:MEASure

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = []  # type: List[str]

            MEASure = MEASure()  # type: ignore
            """
            CALibration:PULSe:MEASure

            Arguments:
            """

        PULSe = PULSe()  # type: ignore
        """
        CALibration:PULSe

        Arguments:
        """

        class QPSK(SCPINode):
            """
            CALibration:QPSK

            Arguments:
            """
            __slots__ = ()
            _cmd = "QPSK"
            args = []  # type: List[str]

            class STORe(SCPINode, SCPISet):
                """
                CALibration:QPSK:STORe

                Arguments:
                """
                __slots__ = ()
                _cmd = "STORe"
                args = []  # type: List[str]

            STORe = STORe()  # type: ignore
            """
            CALibration:QPSK:STORe

            Arguments:
            """

        QPSK = QPSK()  # type: ignore
        """
        CALibration:QPSK

        Arguments:
        """

        class ROSCillator(SCPINode):
            """
            CALibration:ROSCillator

            Arguments:
            """
            __slots__ = ()
            _cmd = "ROSCillator"
            args = []  # type: List[str]

            class STORe(SCPINode, SCPISet):
                """
                CALibration:ROSCillator:STORe

                Arguments:
                """
                __slots__ = ()
                _cmd = "STORe"
                args = []  # type: List[str]

            STORe = STORe()  # type: ignore
            """
            CALibration:ROSCillator:STORe

            Arguments:
            """

        ROSCillator = ROSCillator()  # type: ignore
        """
        CALibration:ROSCillator

        Arguments:
        """

        class VMODulation(SCPINode):
            """
            CALibration:VMODulation

            Arguments:
            """
            __slots__ = ()
            _cmd = "VMODulation"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:VMODulation:MEASure

                Arguments: ONCE
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = ["ONCE"]

            MEASure = MEASure()  # type: ignore
            """
            CALibration:VMODulation:MEASure

            Arguments: ONCE
            """

        VMODulation = VMODulation()  # type: ignore
        """
        CALibration:VMODulation

        Arguments:
        """

        class VSUMmation(SCPINode):
            """
            CALibration:VSUMmation

            Arguments:
            """
            __slots__ = ()
            _cmd = "VSUMmation"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:VSUMmation:MEASure

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = []  # type: List[str]

            MEASure = MEASure()  # type: ignore
            """
            CALibration:VSUMmation:MEASure

            Arguments:
            """

            class OFFSet(SCPINode, SCPIQuery):
                """
                CALibration:VSUMmation:OFFSet

                Arguments:
                """
                __slots__ = ()
                _cmd = "OFFSet"
                args = []  # type: List[str]

            OFFSet = OFFSet()  # type: ignore
            """
            CALibration:VSUMmation:OFFSet

            Arguments:
            """

        VSUMmation = VSUMmation()  # type: ignore
        """
        CALibration:VSUMmation

        Arguments:
        """

        class VSYNthesis(SCPINode):
            """
            CALibration:VSYNthesis

            Arguments:
            """
            __slots__ = ()
            _cmd = "VSYNthesis"
            args = []  # type: List[str]

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:VSYNthesis:MEASure

                Arguments:
                """
                __slots__ = ()
                _cmd = "MEASure"
                args = []  # type: List[str]

            MEASure = MEASure()  # type: ignore
            """
            CALibration:VSYNthesis:MEASure

            Arguments:
            """

        VSYNthesis = VSYNthesis()  # type: ignore
        """
        CALibration:VSYNthesis

        Arguments:
        """

    CALibration = CALibration()  # type: ignore
    """
    CALibration

    Arguments:
    """

    class CAlibration(SCPINode, SCPISet):
        """
        CAlibration

        Arguments:
        """
        __slots__ = ()
        _cmd = "CAlibration"
        args = []  # type: List[str]

    CAlibration = CAlibration()  # type: ignore
    """
    CAlibration

    Arguments:
    """

    class CONTrast(SCPINode, SCPIQuery, SCPISet):
        """
        CONTrast

        Arguments: 1
        """
        __slots__ = ()
        _cmd = "CONTrast"
        args = ["1"]

    CONTrast = CONTrast()  # type: ignore
    """
    CONTrast

    Arguments: 1
    """

    class CONTrol(SCPINode, SCPISet):
        """
        CONTrol

        Arguments:
        """
        __slots__ = ()
        _cmd = "CONTrol"
        args = []  # type: List[str]

        class BLANking(SCPINode, SCPISet):
            """
            CONTrol:BLANking

            Arguments:
            """
            __slots__ = ()
            _cmd = "BLANking"
            args = []  # type: List[str]

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:BLANking:POLarity

                Arguments: INVerted, NORMal
                """
                __slots__ = ()
                _cmd = "POLarity"
                args = ["INVerted", "NORMal"]

            POLarity = POLarity()  # type: ignore
            """
            CONTrol:BLANking:POLarity

            Arguments: INVerted, NORMal
            """

        BLANking = BLANking()  # type: ignore
        """
        CONTrol:BLANking

        Arguments:
        """

        class PENLift(SCPINode, SCPISet):
            """
            CONTrol:PENLift

            Arguments:
            """
            __slots__ = ()
            _cmd = "PENLift"
            args = []  # type: List[str]

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:PENLift:POLarity

                Arguments: INVerted, NORMal
                """
                __slots__ = ()
                _cmd = "POLarity"
                args = ["INVerted", "NORMal"]

            POLarity = POLarity()  # type: ignore
            """
            CONTrol:PENLift:POLarity

            Arguments: INVerted, NORMal
            """

        PENLift = PENLift()  # type: ignore
        """
        CONTrol:PENLift

        Arguments:
        """

        class RAMP(SCPINode):
            """
            CONTrol:RAMP

            Arguments:
            """
            __slots__ = ()
            _cmd = "RAMP"
            args = []  # type: List[str]

            class STATe(SCPINode, SCPIBool):
                """
                CONTrol:RAMP:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            CONTrol:RAMP:STATe

            Arguments: 1, ON, OFF
            """

        RAMP = RAMP()  # type: ignore
        """
        CONTrol:RAMP

        Arguments:
        """

    CONTrol = CONTrol()  # type: ignore
    """
    CONTrol

    Arguments:
    """

    class DCFMnl(SCPINode, SCPISet):
        """
        DCFMnl

        Arguments:
        """
        __slots__ = ()
        _cmd = "DCFMnl"
        args = []  # type: List[str]

    DCFMnl = DCFMnl()  # type: ignore
    """
    DCFMnl

    Arguments:
    """

    class DEVTrg(SCPINode, SCPISet):
        """
        DEVTrg

        Arguments: FLSWp, SEQT, SSSWp, VOID
        """
        __slots__ = ()
        _cmd = "DEVTrg"
        args = ["FLSWp", "SEQT", "SSSWp", "VOID"]

    DEVTrg = DEVTrg()  # type: ignore
    """
    DEVTrg

    Arguments: FLSWp, SEQT, SSSWp, VOID
    """

    class DEcrement(SCPINode, SCPISet):
        """
        DEcrement

        Arguments:
        """
        __slots__ = ()
        _cmd = "DEcrement"
        args = []  # type: List[str]

        class PHAse(SCPINode, SCPISet):
            """
            DEcrement:PHAse

            Arguments:
            """
            __slots__ = ()
            _cmd = "PHAse"
            args = []  # type: List[str]

        PHAse = PHAse()  # type: ignore
        """
        DEcrement:PHAse

        Arguments:
        """

        class Swp(SCPINode, SCPISet):
            """
            DEcrement:Swp

            Arguments:
            """
            __slots__ = ()
            _cmd = "Swp"
            args = []  # type: List[str]

        Swp = Swp()  # type: ignore
        """
        DEcrement:Swp

        Arguments:
        """

    DEcrement = DEcrement()  # type: ignore
    """
    DEcrement

    Arguments:
    """

    class DIAGnostic(SCPINode, SCPISet):
        """
        DIAGnostic

        Arguments:
        """
        __slots__ = ()
        _cmd = "DIAGnostic"
        args = []  # type: List[str]

        class CPU(SCPINode):
            """
            DIAGnostic:CPU

            Arguments:
            """
            __slots__ = ()
            _cmd = "CPU"
            args = []  # type: List[str]

            class INFormation(SCPINode, SCPISet):
                """
                DIAGnostic:CPU:INFormation

                Arguments:
                """
                __slots__ = ()
                _cmd = "INFormation"
                args = []  # type: List[str]

                class BOARds(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:CPU:INFormation:BOARds

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "BOARds"
                    args = []  # type: List[str]

                BOARds = BOARds()  # type: ignore
                """
                DIAGnostic:CPU:INFormation:BOARds

                Arguments:
                """

                class CCOunt(SCPINode, SCPISet):
                    """
                    DIAGnostic:CPU:INFormation:CCOunt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CCOunt"
                    args = []  # type: List[str]

                    class ATTenuator(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:CCOunt:ATTenuator

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "ATTenuator"
                        args = []  # type: List[str]

                    ATTenuator = ATTenuator()  # type: ignore
                    """
                    DIAGnostic:CPU:INFormation:CCOunt:ATTenuator

                    Arguments:
                    """

                    class PROTection(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:CCOunt:PROTection

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "PROTection"
                        args = []  # type: List[str]

                    PROTection = PROTection()  # type: ignore
                    """
                    DIAGnostic:CPU:INFormation:CCOunt:PROTection

                    Arguments:
                    """

                CCOunt = CCOunt()  # type: ignore
                """
                DIAGnostic:CPU:INFormation:CCOunt

                Arguments:
                """

                class DISPlay(SCPINode, SCPISet):
                    """
                    DIAGnostic:CPU:INFormation:DISPlay

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "DISPlay"
                    args = []  # type: List[str]

                    class OTIMe(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:DISPlay:OTIMe

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "OTIMe"
                        args = []  # type: List[str]

                    OTIMe = OTIMe()  # type: ignore
                    """
                    DIAGnostic:CPU:INFormation:DISPlay:OTIMe

                    Arguments:
                    """

                DISPlay = DISPlay()  # type: ignore
                """
                DIAGnostic:CPU:INFormation:DISPlay

                Arguments:
                """

                class LICense(SCPINode, SCPISet):
                    """
                    DIAGnostic:CPU:INFormation:LICense

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "LICense"
                    args = []  # type: List[str]

                    class AUXiliary(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:LICense:AUXiliary

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "AUXiliary"
                        args = []  # type: List[str]

                    AUXiliary = AUXiliary()  # type: ignore
                    """
                    DIAGnostic:CPU:INFormation:LICense:AUXiliary

                    Arguments:
                    """

                    class WAVeform(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:LICense:WAVeform

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "WAVeform"
                        args = []  # type: List[str]

                    WAVeform = WAVeform()  # type: ignore
                    """
                    DIAGnostic:CPU:INFormation:LICense:WAVeform

                    Arguments:
                    """

                LICense = LICense()  # type: ignore
                """
                DIAGnostic:CPU:INFormation:LICense

                Arguments:
                """

                class OPTions(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:CPU:INFormation:OPTions

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "OPTions"
                    args = []  # type: List[str]

                    class DETail(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:OPTions:DETail

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "DETail"
                        args = []  # type: List[str]

                    DETail = DETail()  # type: ignore
                    """
                    DIAGnostic:CPU:INFormation:OPTions:DETail

                    Arguments:
                    """

                OPTions = OPTions()  # type: ignore
                """
                DIAGnostic:CPU:INFormation:OPTions

                Arguments:
                """

                class OTIMe(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:CPU:INFormation:OTIMe

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "OTIMe"
                    args = []  # type: List[str]

                OTIMe = OTIMe()  # type: ignore
                """
                DIAGnostic:CPU:INFormation:OTIMe

                Arguments:
                """

                class REVision(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:CPU:INFormation:REVision

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "REVision"
                    args = []  # type: List[str]

                REVision = REVision()  # type: ignore
                """
                DIAGnostic:CPU:INFormation:REVision

                Arguments:
                """

                class SDATe(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:CPU:INFormation:SDATe

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SDATe"
                    args = []  # type: List[str]

                SDATe = SDATe()  # type: ignore
                """
                DIAGnostic:CPU:INFormation:SDATe

                Arguments:
                """

                class WLICence(SCPINode):
                    """
                    DIAGnostic:CPU:INFormation:WLICence

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "WLICence"
                    args = []  # type: List[str]

                    class VALue(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:WLICence:VALue

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "VALue"
                        args = ["1"]

                    VALue = VALue()  # type: ignore
                    """
                    DIAGnostic:CPU:INFormation:WLICence:VALue

                    Arguments: 1
                    """

                WLICence = WLICence()  # type: ignore
                """
                DIAGnostic:CPU:INFormation:WLICence

                Arguments:
                """

            INFormation = INFormation()  # type: ignore
            """
            DIAGnostic:CPU:INFormation

            Arguments:
            """

        CPU = CPU()  # type: ignore
        """
        DIAGnostic:CPU

        Arguments:
        """

        class INFO(SCPINode):
            """
            DIAGnostic:INFO

            Arguments:
            """
            __slots__ = ()
            _cmd = "INFO"
            args = []  # type: List[str]

            class CCOunt(SCPINode):
                """
                DIAGnostic:INFO:CCOunt

                Arguments:
                """
                __slots__ = ()
                _cmd = "CCOunt"
                args = []  # type: List[str]

                class ATTenuator(SCPINodeN, SCPIQuery):
                    """
                    DIAGnostic:INFO:CCOunt:ATTenuator

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ATTenuator"
                    args = []  # type: List[str]

                ATTenuator = ATTenuator()  # type: ignore
                """
                DIAGnostic:INFO:CCOunt:ATTenuator

                Arguments:
                """

                class POWer(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:INFO:CCOunt:POWer

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "POWer"
                    args = []  # type: List[str]

                POWer = POWer()  # type: ignore
                """
                DIAGnostic:INFO:CCOunt:POWer

                Arguments:
                """

            CCOunt = CCOunt()  # type: ignore
            """
            DIAGnostic:INFO:CCOunt

            Arguments:
            """

            class MODules(SCPINode, SCPIQuery):
                """
                DIAGnostic:INFO:MODules

                Arguments:
                """
                __slots__ = ()
                _cmd = "MODules"
                args = []  # type: List[str]

            MODules = MODules()  # type: ignore
            """
            DIAGnostic:INFO:MODules

            Arguments:
            """

            class OTIMe(SCPINode, SCPIQuery):
                """
                `DIAGnostic:INFO:OTIMe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e90e50c315c247d4.htm#ID_f15aa7634e8152f70a00206a00abf390-2654fb124e8152f70a00206a0024546d-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "OTIMe"
                args = []  # type: List[str]

            OTIMe = OTIMe()  # type: ignore
            """
            `DIAGnostic:INFO:OTIMe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e90e50c315c247d4.htm#ID_f15aa7634e8152f70a00206a00abf390-2654fb124e8152f70a00206a0024546d-en-US>`_

            Arguments:
            """

            class SDATe(SCPINode, SCPIQuery):
                """
                DIAGnostic:INFO:SDATe

                Arguments:
                """
                __slots__ = ()
                _cmd = "SDATe"
                args = []  # type: List[str]

            SDATe = SDATe()  # type: ignore
            """
            DIAGnostic:INFO:SDATe

            Arguments:
            """

            class SERialno(SCPINode, SCPIQuery):
                """
                DIAGnostic:INFO:SERialno

                Arguments:
                """
                __slots__ = ()
                _cmd = "SERialno"
                args = []  # type: List[str]

            SERialno = SERialno()  # type: ignore
            """
            DIAGnostic:INFO:SERialno

            Arguments:
            """

            class SVERsion(SCPINode, SCPIQuery):
                """
                DIAGnostic:INFO:SVERsion

                Arguments:
                """
                __slots__ = ()
                _cmd = "SVERsion"
                args = []  # type: List[str]

            SVERsion = SVERsion()  # type: ignore
            """
            DIAGnostic:INFO:SVERsion

            Arguments:
            """

        INFO = INFO()  # type: ignore
        """
        DIAGnostic:INFO

        Arguments:
        """

        class MEASure(SCPINode):
            """
            DIAGnostic:MEASure

            Arguments:
            """
            __slots__ = ()
            _cmd = "MEASure"
            args = []  # type: List[str]

            class POINt(SCPINode, SCPIQuery):
                """
                DIAGnostic:MEASure:POINt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "POINt"
                args = ["1"]

            POINt = POINt()  # type: ignore
            """
            DIAGnostic:MEASure:POINt

            Arguments: 1
            """

        MEASure = MEASure()  # type: ignore
        """
        DIAGnostic:MEASure

        Arguments:
        """

        class XMEM(SCPINode):
            """
            DIAGnostic:XMEM

            Arguments:
            """
            __slots__ = ()
            _cmd = "XMEM"
            args = []  # type: List[str]

            class CHECksum(SCPINode):
                """
                DIAGnostic:XMEM:CHECksum

                Arguments:
                """
                __slots__ = ()
                _cmd = "CHECksum"
                args = []  # type: List[str]

                class ATTenuate(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:XMEM:CHECksum:ATTenuate

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ATTenuate"
                    args = []  # type: List[str]

                ATTenuate = ATTenuate()  # type: ignore
                """
                DIAGnostic:XMEM:CHECksum:ATTenuate

                Arguments:
                """

                class BURSt(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:XMEM:CHECksum:BURSt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "BURSt"
                    args = []  # type: List[str]

                BURSt = BURSt()  # type: ignore
                """
                DIAGnostic:XMEM:CHECksum:BURSt

                Arguments:
                """

                class CALCulate(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:XMEM:CHECksum:CALCulate

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CALCulate"
                    args = []  # type: List[str]

                CALCulate = CALCulate()  # type: ignore
                """
                DIAGnostic:XMEM:CHECksum:CALCulate

                Arguments:
                """

                class TOTal(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:XMEM:CHECksum:TOTal

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "TOTal"
                    args = []  # type: List[str]

                TOTal = TOTal()  # type: ignore
                """
                DIAGnostic:XMEM:CHECksum:TOTal

                Arguments:
                """

            CHECksum = CHECksum()  # type: ignore
            """
            DIAGnostic:XMEM:CHECksum

            Arguments:
            """

        XMEM = XMEM()  # type: ignore
        """
        DIAGnostic:XMEM

        Arguments:
        """

    DIAGnostic = DIAGnostic()  # type: ignore
    """
    DIAGnostic

    Arguments:
    """

    class DIGital(SCPINode, SCPIQuery):
        """
        DIGital

        Arguments:
        """
        __slots__ = ()
        _cmd = "DIGital"
        args = []  # type: List[str]

        class CONFig(SCPINode, SCPIQuery):
            """
            DIGital:CONFig

            Arguments:
            """
            __slots__ = ()
            _cmd = "CONFig"
            args = []  # type: List[str]

            class MIXer(SCPINode, SCPISet):
                """
                DIGital:CONFig:MIXer

                Arguments: EXTernal, INTernal
                """
                __slots__ = ()
                _cmd = "MIXer"
                args = ["EXTernal", "INTernal"]

            MIXer = MIXer()  # type: ignore
            """
            DIGital:CONFig:MIXer

            Arguments: EXTernal, INTernal
            """

            class PULSe(SCPINode, SCPISet):
                """
                DIGital:CONFig:PULSe

                Arguments: DISabled, ENABled
                """
                __slots__ = ()
                _cmd = "PULSe"
                args = ["DISabled", "ENABled"]

            PULSe = PULSe()  # type: ignore
            """
            DIGital:CONFig:PULSe

            Arguments: DISabled, ENABled
            """

        CONFig = CONFig()  # type: ignore
        """
        DIGital:CONFig

        Arguments:
        """

        class ERRor(SCPINode, SCPIQuery):
            """
            DIGital:ERRor

            Arguments:
            """
            __slots__ = ()
            _cmd = "ERRor"
            args = []  # type: List[str]

            class DISable(SCPINode, SCPISet):
                """
                DIGital:ERRor:DISable

                Arguments:
                """
                __slots__ = ()
                _cmd = "DISable"
                args = []  # type: List[str]

            DISable = DISable()  # type: ignore
            """
            DIGital:ERRor:DISable

            Arguments:
            """

            class ENABle(SCPINode, SCPISet):
                """
                DIGital:ERRor:ENABle

                Arguments:
                """
                __slots__ = ()
                _cmd = "ENABle"
                args = []  # type: List[str]

            ENABle = ENABle()  # type: ignore
            """
            DIGital:ERRor:ENABle

            Arguments:
            """

        ERRor = ERRor()  # type: ignore
        """
        DIGital:ERRor

        Arguments:
        """

        class EXT_par(SCPINode, SCPISet):
            """
            DIGital:EXT_par

            Arguments:
            """
            __slots__ = ()
            _cmd = "EXT_par"
            args = []  # type: List[str]

            class DATapol(SCPINode, SCPISet):
                """
                DIGital:EXT_par:DATapol

                Arguments: INVerse, NORMal
                """
                __slots__ = ()
                _cmd = "DATapol"
                args = ["INVerse", "NORMal"]

            DATapol = DATapol()  # type: ignore
            """
            DIGital:EXT_par:DATapol

            Arguments: INVerse, NORMal
            """

            class SYMPol(SCPINode, SCPISet):
                """
                DIGital:EXT_par:SYMPol

                Arguments: NEG_edge, POS_edge
                """
                __slots__ = ()
                _cmd = "SYMPol"
                args = ["NEG_edge", "POS_edge"]

            SYMPol = SYMPol()  # type: ignore
            """
            DIGital:EXT_par:SYMPol

            Arguments: NEG_edge, POS_edge
            """

            class SYMStat(SCPINode, SCPISet):
                """
                DIGital:EXT_par:SYMStat

                Arguments: EXTernal, INTernal
                """
                __slots__ = ()
                _cmd = "SYMStat"
                args = ["EXTernal", "INTernal"]

            SYMStat = SYMStat()  # type: ignore
            """
            DIGital:EXT_par:SYMStat

            Arguments: EXTernal, INTernal
            """

        EXT_par = EXT_par()  # type: ignore
        """
        DIGital:EXT_par

        Arguments:
        """

        class EXT_ser(SCPINode, SCPISet):
            """
            DIGital:EXT_ser

            Arguments:
            """
            __slots__ = ()
            _cmd = "EXT_ser"
            args = []  # type: List[str]

            class BITPol(SCPINode, SCPISet):
                """
                DIGital:EXT_ser:BITPol

                Arguments: NEG_edge, POS_edge
                """
                __slots__ = ()
                _cmd = "BITPol"
                args = ["NEG_edge", "POS_edge"]

            BITPol = BITPol()  # type: ignore
            """
            DIGital:EXT_ser:BITPol

            Arguments: NEG_edge, POS_edge
            """

            class BITStat(SCPINode, SCPISet):
                """
                DIGital:EXT_ser:BITStat

                Arguments: EXTernal, INTernal
                """
                __slots__ = ()
                _cmd = "BITStat"
                args = ["EXTernal", "INTernal"]

            BITStat = BITStat()  # type: ignore
            """
            DIGital:EXT_ser:BITStat

            Arguments: EXTernal, INTernal
            """

            class DATapol(SCPINode, SCPISet):
                """
                DIGital:EXT_ser:DATapol

                Arguments: INVerse, NORMal
                """
                __slots__ = ()
                _cmd = "DATapol"
                args = ["INVerse", "NORMal"]

            DATapol = DATapol()  # type: ignore
            """
            DIGital:EXT_ser:DATapol

            Arguments: INVerse, NORMal
            """

            class SYMPol(SCPINode, SCPISet):
                """
                DIGital:EXT_ser:SYMPol

                Arguments: NEG_edge, POS_edge
                """
                __slots__ = ()
                _cmd = "SYMPol"
                args = ["NEG_edge", "POS_edge"]

            SYMPol = SYMPol()  # type: ignore
            """
            DIGital:EXT_ser:SYMPol

            Arguments: NEG_edge, POS_edge
            """

            class SYMStat(SCPINode, SCPISet):
                """
                DIGital:EXT_ser:SYMStat

                Arguments: EXTernal, INTernal
                """
                __slots__ = ()
                _cmd = "SYMStat"
                args = ["EXTernal", "INTernal"]

            SYMStat = SYMStat()  # type: ignore
            """
            DIGital:EXT_ser:SYMStat

            Arguments: EXTernal, INTernal
            """

        EXT_ser = EXT_ser()  # type: ignore
        """
        DIGital:EXT_ser

        Arguments:
        """

        class FADing(SCPINode, SCPIQuery):
            """
            DIGital:FADing

            Arguments:
            """
            __slots__ = ()
            _cmd = "FADing"
            args = []  # type: List[str]

            class DIR_dopp(SCPINode, SCPISet):
                """
                DIGital:FADing:DIR_dopp

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DIR_dopp"
                args = ["1"]

            DIR_dopp = DIR_dopp()  # type: ignore
            """
            DIGital:FADing:DIR_dopp

            Arguments: 1
            """

            class RATio(SCPINode, SCPISet):
                """
                DIGital:FADing:RATio

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "RATio"
                args = ["1"]

            RATio = RATio()  # type: ignore
            """
            DIGital:FADing:RATio

            Arguments: 1
            """

            class SPEed(SCPINode, SCPISet):
                """
                DIGital:FADing:SPEed

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "SPEed"
                args = ["1"]

            SPEed = SPEed()  # type: ignore
            """
            DIGital:FADing:SPEed

            Arguments: 1
            """

        FADing = FADing()  # type: ignore
        """
        DIGital:FADing

        Arguments:
        """

        class GAIN(SCPINode):
            """
            DIGital:GAIN

            Arguments:
            """
            __slots__ = ()
            _cmd = "GAIN"
            args = []  # type: List[str]

            class VALue(SCPINode, SCPISet):
                """
                DIGital:GAIN:VALue

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()  # type: ignore
            """
            DIGital:GAIN:VALue

            Arguments: 1
            """

        GAIN = GAIN()  # type: ignore
        """
        DIGital:GAIN

        Arguments:
        """

        class INT_0s(SCPINode, SCPISet):
            """
            DIGital:INT_0s

            Arguments:
            """
            __slots__ = ()
            _cmd = "INT_0s"
            args = []  # type: List[str]

            class CLOCk(SCPINode, SCPISet):
                """
                DIGital:INT_0s:CLOCk

                Arguments: EXT_bit, EXT_sym, INT_sym
                """
                __slots__ = ()
                _cmd = "CLOCk"
                args = ["EXT_bit", "EXT_sym", "INT_sym"]

            CLOCk = CLOCk()  # type: ignore
            """
            DIGital:INT_0s:CLOCk

            Arguments: EXT_bit, EXT_sym, INT_sym
            """

            class CLOCkpol(SCPINode, SCPISet):
                """
                DIGital:INT_0s:CLOCkpol

                Arguments: NEG_edge, POS_edge
                """
                __slots__ = ()
                _cmd = "CLOCkpol"
                args = ["NEG_edge", "POS_edge"]

            CLOCkpol = CLOCkpol()  # type: ignore
            """
            DIGital:INT_0s:CLOCkpol

            Arguments: NEG_edge, POS_edge
            """

            class DATapol(SCPINode, SCPISet):
                """
                DIGital:INT_0s:DATapol

                Arguments: INVerse, NORMal
                """
                __slots__ = ()
                _cmd = "DATapol"
                args = ["INVerse", "NORMal"]

            DATapol = DATapol()  # type: ignore
            """
            DIGital:INT_0s:DATapol

            Arguments: INVerse, NORMal
            """

        INT_0s = INT_0s()  # type: ignore
        """
        DIGital:INT_0s

        Arguments:
        """

        class INT_1s(SCPINode, SCPISet):
            """
            DIGital:INT_1s

            Arguments:
            """
            __slots__ = ()
            _cmd = "INT_1s"
            args = []  # type: List[str]

            class CLOCk(SCPINode, SCPISet):
                """
                DIGital:INT_1s:CLOCk

                Arguments: EXT_bit, EXT_sym, INT_sym
                """
                __slots__ = ()
                _cmd = "CLOCk"
                args = ["EXT_bit", "EXT_sym", "INT_sym"]

            CLOCk = CLOCk()  # type: ignore
            """
            DIGital:INT_1s:CLOCk

            Arguments: EXT_bit, EXT_sym, INT_sym
            """

            class CLOCkpol(SCPINode, SCPISet):
                """
                DIGital:INT_1s:CLOCkpol

                Arguments: NEG_edge, POS_edge
                """
                __slots__ = ()
                _cmd = "CLOCkpol"
                args = ["NEG_edge", "POS_edge"]

            CLOCkpol = CLOCkpol()  # type: ignore
            """
            DIGital:INT_1s:CLOCkpol

            Arguments: NEG_edge, POS_edge
            """

            class DATapol(SCPINode, SCPISet):
                """
                DIGital:INT_1s:DATapol

                Arguments: INVerse, NORMal
                """
                __slots__ = ()
                _cmd = "DATapol"
                args = ["INVerse", "NORMal"]

            DATapol = DATapol()  # type: ignore
            """
            DIGital:INT_1s:DATapol

            Arguments: INVerse, NORMal
            """

        INT_1s = INT_1s()  # type: ignore
        """
        DIGital:INT_1s

        Arguments:
        """

        class LEAK(SCPINode):
            """
            DIGital:LEAK

            Arguments:
            """
            __slots__ = ()
            _cmd = "LEAK"
            args = []  # type: List[str]

            class VALue(SCPINode, SCPISet):
                """
                DIGital:LEAK:VALue

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()  # type: ignore
            """
            DIGital:LEAK:VALue

            Arguments: 1
            """

        LEAK = LEAK()  # type: ignore
        """
        DIGital:LEAK

        Arguments:
        """

        class MODopt(SCPINode, SCPIQuery):
            """
            DIGital:MODopt

            Arguments:
            """
            __slots__ = ()
            _cmd = "MODopt"
            args = []  # type: List[str]

            class ENVelope(SCPINode, SCPISet):
                """
                DIGital:MODopt:ENVelope

                Arguments: DISabled, ENABled
                """
                __slots__ = ()
                _cmd = "ENVelope"
                args = ["DISabled", "ENABled"]

            ENVelope = ENVelope()  # type: ignore
            """
            DIGital:MODopt:ENVelope

            Arguments: DISabled, ENABled
            """

            class MODPol(SCPINode, SCPISet):
                """
                DIGital:MODopt:MODPol

                Arguments: INVerse, NORMal
                """
                __slots__ = ()
                _cmd = "MODPol"
                args = ["INVerse", "NORMal"]

            MODPol = MODPol()  # type: ignore
            """
            DIGital:MODopt:MODPol

            Arguments: INVerse, NORMal
            """

            class SBANd(SCPINode, SCPISet):
                """
                DIGital:MODopt:SBANd

                Arguments: AUTO, LOWer, UPPer
                """
                __slots__ = ()
                _cmd = "SBANd"
                args = ["AUTO", "LOWer", "UPPer"]

            SBANd = SBANd()  # type: ignore
            """
            DIGital:MODopt:SBANd

            Arguments: AUTO, LOWer, UPPer
            """

        MODopt = MODopt()  # type: ignore
        """
        DIGital:MODopt

        Arguments:
        """

        class PRBS(SCPINode):
            """
            DIGital:PRBS

            Arguments:
            """
            __slots__ = ()
            _cmd = "PRBS"
            args = []  # type: List[str]

            class CLOCk(SCPINode, SCPISet):
                """
                DIGital:PRBS:CLOCk

                Arguments: EXT_bit, EXT_sym, INT_sym
                """
                __slots__ = ()
                _cmd = "CLOCk"
                args = ["EXT_bit", "EXT_sym", "INT_sym"]

            CLOCk = CLOCk()  # type: ignore
            """
            DIGital:PRBS:CLOCk

            Arguments: EXT_bit, EXT_sym, INT_sym
            """

            class CLOCkpol(SCPINode, SCPISet):
                """
                DIGital:PRBS:CLOCkpol

                Arguments: NEG_edge, POS_edge
                """
                __slots__ = ()
                _cmd = "CLOCkpol"
                args = ["NEG_edge", "POS_edge"]

            CLOCkpol = CLOCkpol()  # type: ignore
            """
            DIGital:PRBS:CLOCkpol

            Arguments: NEG_edge, POS_edge
            """

            class DATapol(SCPINode, SCPISet):
                """
                DIGital:PRBS:DATapol

                Arguments: INVerse, NORMal
                """
                __slots__ = ()
                _cmd = "DATapol"
                args = ["INVerse", "NORMal"]

            DATapol = DATapol()  # type: ignore
            """
            DIGital:PRBS:DATapol

            Arguments: INVerse, NORMal
            """

            class VALue(SCPINode, SCPISet):
                """
                DIGital:PRBS:VALue

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()  # type: ignore
            """
            DIGital:PRBS:VALue

            Arguments: 1
            """

        PRBS = PRBS()  # type: ignore
        """
        DIGital:PRBS

        Arguments:
        """

        class SKEW(SCPINode):
            """
            DIGital:SKEW

            Arguments:
            """
            __slots__ = ()
            _cmd = "SKEW"
            args = []  # type: List[str]

            class VALue(SCPINode, SCPISet):
                """
                DIGital:SKEW:VALue

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()  # type: ignore
            """
            DIGital:SKEW:VALue

            Arguments: 1
            """

        SKEW = SKEW()  # type: ignore
        """
        DIGital:SKEW

        Arguments:
        """

        class SYSTem(SCPINode, SCPIQuery):
            """
            DIGital:SYSTem

            Arguments:
            """
            __slots__ = ()
            _cmd = "SYSTem"
            args = []  # type: List[str]

            class ALPHa(SCPINode, SCPISet):
                """
                DIGital:SYSTem:ALPHa

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ALPHa"
                args = ["1"]

            ALPHa = ALPHa()  # type: ignore
            """
            DIGital:SYSTem:ALPHa

            Arguments: 1
            """

            class FILTer(SCPINode, SCPISet):
                """
                DIGital:SYSTem:FILTer

                Arguments: GAUSs, R_Cos, R_R_cos
                """
                __slots__ = ()
                _cmd = "FILTer"
                args = ["GAUSs", "R_Cos", "R_R_cos"]

            FILTer = FILTer()  # type: ignore
            """
            DIGital:SYSTem:FILTer

            Arguments: GAUSs, R_Cos, R_R_cos
            """

            class FORMat(SCPINode, SCPISet):
                """
                DIGital:SYSTem:FORMat

                Arguments: BPSK, D_BPsk, D_PSk8, D_QPsk, FSK2, FSK4, GMSK, O_BPsk, O_PSk8, O_QPsk, PSK8, QAM16, QAM256, QAM4, QAM64, QPSK, TOQPsk, T_Tones
                """
                __slots__ = ()
                _cmd = "FORMat"
                args = ["BPSK", "D_BPsk", "D_PSk8", "D_QPsk", "FSK2", "FSK4", "GMSK", "O_BPsk", "O_PSk8", "O_QPsk", "PSK8", "QAM16", "QAM256", "QAM4", "QAM64", "QPSK", "TOQPsk", "T_Tones"]

            FORMat = FORMat()  # type: ignore
            """
            DIGital:SYSTem:FORMat

            Arguments: BPSK, D_BPsk, D_PSk8, D_QPsk, FSK2, FSK4, GMSK, O_BPsk, O_PSk8, O_QPsk, PSK8, QAM16, QAM256, QAM4, QAM64, QPSK, TOQPsk, T_Tones
            """

            class SELect(SCPINode, SCPISet):
                """
                DIGital:SYSTem:SELect

                Arguments: CDPD, CITY1200, CITY2400, CITY4800, CITY512, DSRR16, DSRR4, ERMes, GSM, INMar_m, MC9, MD100w, MD120w, MD160n, MD192w, MD24n, MD24w, MD36n, MD36w, MD48n, MD48w, MD80n, MD80w, MD96n, MD96w, MOBitex, NADC, PDC, POC1200, POC2400, POC4800, POC512, Q_APco25, TETRa, TFTS, USER1, USER2, USER3, USER4, USER5, VDR
                """
                __slots__ = ()
                _cmd = "SELect"
                args = ["CDPD", "CITY1200", "CITY2400", "CITY4800", "CITY512", "DSRR16", "DSRR4", "ERMes", "GSM", "INMar_m", "MC9", "MD100w", "MD120w", "MD160n", "MD192w", "MD24n", "MD24w", "MD36n", "MD36w", "MD48n", "MD48w", "MD80n", "MD80w", "MD96n", "MD96w", "MOBitex", "NADC", "PDC", "POC1200", "POC2400", "POC4800", "POC512", "Q_APco25", "TETRa", "TFTS", "USER1", "USER2", "USER3", "USER4", "USER5", "VDR"]

            SELect = SELect()  # type: ignore
            """
            DIGital:SYSTem:SELect

            Arguments: CDPD, CITY1200, CITY2400, CITY4800, CITY512, DSRR16, DSRR4, ERMes, GSM, INMar_m, MC9, MD100w, MD120w, MD160n, MD192w, MD24n, MD24w, MD36n, MD36w, MD48n, MD48w, MD80n, MD80w, MD96n, MD96w, MOBitex, NADC, PDC, POC1200, POC2400, POC4800, POC512, Q_APco25, TETRa, TFTS, USER1, USER2, USER3, USER4, USER5, VDR
            """

            class SYM_rate(SCPINode, SCPISet):
                """
                DIGital:SYSTem:SYM_rate

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "SYM_rate"
                args = ["1"]

            SYM_rate = SYM_rate()  # type: ignore
            """
            DIGital:SYSTem:SYM_rate

            Arguments: 1
            """

            class THRee_db(SCPINode, SCPISet):
                """
                DIGital:SYSTem:THRee_db

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "THRee_db"
                args = ["1"]

            THRee_db = THRee_db()  # type: ignore
            """
            DIGital:SYSTem:THRee_db

            Arguments: 1
            """

        SYSTem = SYSTem()  # type: ignore
        """
        DIGital:SYSTem

        Arguments:
        """

        class T_Tones(SCPINode, SCPISet):
            """
            DIGital:T_Tones

            Arguments:
            """
            __slots__ = ()
            _cmd = "T_Tones"
            args = []  # type: List[str]

            class ANGLe(SCPINode, SCPIQuery, SCPISet):
                """
                DIGital:T_Tones:ANGLe

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ANGLe"
                args = ["1"]

            ANGLe = ANGLe()  # type: ignore
            """
            DIGital:T_Tones:ANGLe

            Arguments: 1
            """

            class I_AMp(SCPINode, SCPIQuery, SCPISet):
                """
                DIGital:T_Tones:I_AMp

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "I_AMp"
                args = ["1"]

            I_AMp = I_AMp()  # type: ignore
            """
            DIGital:T_Tones:I_AMp

            Arguments: 1
            """

            class Q_AMp(SCPINode, SCPIQuery, SCPISet):
                """
                DIGital:T_Tones:Q_AMp

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "Q_AMp"
                args = ["1"]

            Q_AMp = Q_AMp()  # type: ignore
            """
            DIGital:T_Tones:Q_AMp

            Arguments: 1
            """

        T_Tones = T_Tones()  # type: ignore
        """
        DIGital:T_Tones

        Arguments:
        """

    DIGital = DIGital()  # type: ignore
    """
    DIGital

    Arguments:
    """

    class DIRect(SCPINode, SCPIQuery, SCPISet):
        """
        DIRect

        Arguments: <block_data>
        """
        __slots__ = ()
        _cmd = "DIRect"
        args = ["<block_data>"]

    DIRect = DIRect()  # type: ignore
    """
    DIRect

    Arguments: <block_data>
    """

    class DISPlay(SCPINode, SCPISet):
        """
        DISPlay

        Arguments:
        """
        __slots__ = ()
        _cmd = "DISPlay"
        args = []  # type: List[str]

        class ANNotation(SCPINode, SCPISet):
            """
            DISPlay:ANNotation

            Arguments:
            """
            __slots__ = ()
            _cmd = "ANNotation"
            args = []  # type: List[str]

            class AMPLitude(SCPINode, SCPIBool):
                """
                `DISPlay:ANNotation:AMPLitude
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7164bc3c1b68452b.htm#ID_49b6f4592f69259f0a00206a0029f4d5-67bb427e2f691da00a00206a00636f5b-en-US>`_

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "AMPLitude"
                args = ["1", "ON", "OFF"]

                class STATe(SCPINode, SCPIBool):
                    """
                    DISPlay:ANNotation:AMPLitude:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                DISPlay:ANNotation:AMPLitude:STATe

                Arguments: 1, ON, OFF
                """

            AMPLitude = AMPLitude()  # type: ignore
            """
            `DISPlay:ANNotation:AMPLitude
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7164bc3c1b68452b.htm#ID_49b6f4592f69259f0a00206a0029f4d5-67bb427e2f691da00a00206a00636f5b-en-US>`_

            Arguments: 1, ON, OFF
            """

            class CLOCk(SCPINode):
                """
                DISPlay:ANNotation:CLOCk

                Arguments:
                """
                __slots__ = ()
                _cmd = "CLOCk"
                args = []  # type: List[str]

                class DATE(SCPINode):
                    """
                    DISPlay:ANNotation:CLOCk:DATE

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "DATE"
                    args = []  # type: List[str]

                    class FORMat(SCPINode, SCPIQuery, SCPISet):
                        """
                        DISPlay:ANNotation:CLOCk:DATE:FORMat

                        Arguments: DMY, MDY
                        """
                        __slots__ = ()
                        _cmd = "FORMat"
                        args = ["DMY", "MDY"]

                    FORMat = FORMat()  # type: ignore
                    """
                    DISPlay:ANNotation:CLOCk:DATE:FORMat

                    Arguments: DMY, MDY
                    """

                DATE = DATE()  # type: ignore
                """
                DISPlay:ANNotation:CLOCk:DATE

                Arguments:
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    DISPlay:ANNotation:CLOCk:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                DISPlay:ANNotation:CLOCk:STATe

                Arguments: 1, ON, OFF
                """

            CLOCk = CLOCk()  # type: ignore
            """
            DISPlay:ANNotation:CLOCk

            Arguments:
            """

            class FREQuency(SCPINode, SCPIBool):
                """
                `DISPlay:ANNotation:FREQuency
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2e5fcccef60940f9.htm#ID_8b6c05102f691b2f0a00206a011c3f7c-b45c82122f6912650a00206a00636f5b-en-US>`_

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = ["1", "ON", "OFF"]

                class STATe(SCPINode, SCPIBool):
                    """
                    DISPlay:ANNotation:FREQuency:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                DISPlay:ANNotation:FREQuency:STATe

                Arguments: 1, ON, OFF
                """

            FREQuency = FREQuency()  # type: ignore
            """
            `DISPlay:ANNotation:FREQuency
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2e5fcccef60940f9.htm#ID_8b6c05102f691b2f0a00206a011c3f7c-b45c82122f6912650a00206a00636f5b-en-US>`_

            Arguments: 1, ON, OFF
            """

            class LFSource(SCPINode, SCPIBool):
                """
                DISPlay:ANNotation:LFSource

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "LFSource"
                args = ["1", "ON", "OFF"]

            LFSource = LFSource()  # type: ignore
            """
            DISPlay:ANNotation:LFSource

            Arguments: 1, ON, OFF
            """

            class MODulation(SCPINode, SCPIBool):
                """
                DISPlay:ANNotation:MODulation

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "MODulation"
                args = ["1", "ON", "OFF"]

            MODulation = MODulation()  # type: ignore
            """
            DISPlay:ANNotation:MODulation

            Arguments: 1, ON, OFF
            """

        ANNotation = ANNotation()  # type: ignore
        """
        DISPlay:ANNotation

        Arguments:
        """

        class BRIGhtness(SCPINode, SCPIQuery, SCPISet):
            """
            DISPlay:BRIGhtness

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "BRIGhtness"
            args = ["1"]

        BRIGhtness = BRIGhtness()  # type: ignore
        """
        DISPlay:BRIGhtness

        Arguments: 1
        """

        class CAPTure(SCPINode, SCPISet):
            """
            DISPlay:CAPTure

            Arguments:
            """
            __slots__ = ()
            _cmd = "CAPTure"
            args = []  # type: List[str]

        CAPTure = CAPTure()  # type: ignore
        """
        DISPlay:CAPTure

        Arguments:
        """

        class CONTrast(SCPINode, SCPIQuery, SCPISet):
            """
            DISPlay:CONTrast

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "CONTrast"
            args = ["1"]

        CONTrast = CONTrast()  # type: ignore
        """
        DISPlay:CONTrast

        Arguments: 1
        """

        class INVerse(SCPINode, SCPIBool):
            """
            DISPlay:INVerse

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "INVerse"
            args = ["1", "ON", "OFF"]

        INVerse = INVerse()  # type: ignore
        """
        DISPlay:INVerse

        Arguments: 1, ON, OFF
        """

        class RADix(SCPINode, SCPIQuery, SCPISet):
            """
            DISPlay:RADix

            Arguments: EURopean, US
            """
            __slots__ = ()
            _cmd = "RADix"
            args = ["EURopean", "US"]

        RADix = RADix()  # type: ignore
        """
        DISPlay:RADix

        Arguments: EURopean, US
        """

        class REMote(SCPINode, SCPIBool):
            """
            DISPlay:REMote

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "REMote"
            args = ["1", "ON", "OFF"]

        REMote = REMote()  # type: ignore
        """
        DISPlay:REMote

        Arguments: 1, ON, OFF
        """

        class STATe(SCPINode, SCPIBool):
            """
            DISPlay:STATe

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()  # type: ignore
        """
        DISPlay:STATe

        Arguments: 1, ON, OFF
        """

        class WINDow(SCPINode, SCPISet):
            """
            DISPlay:WINDow

            Arguments:
            """
            __slots__ = ()
            _cmd = "WINDow"
            args = []  # type: List[str]

            class STATe(SCPINode, SCPIBool):
                """
                DISPlay:WINDow:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            DISPlay:WINDow:STATe

            Arguments: 1, ON, OFF
            """

            class TEXT(SCPINode):
                """
                DISPlay:WINDow:TEXT

                Arguments:
                """
                __slots__ = ()
                _cmd = "TEXT"
                args = []  # type: List[str]

                class STATe(SCPINode, SCPIBool):
                    """
                    DISPlay:WINDow:TEXT:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                DISPlay:WINDow:TEXT:STATe

                Arguments: 1, ON, OFF
                """

            TEXT = TEXT()  # type: ignore
            """
            DISPlay:WINDow:TEXT

            Arguments:
            """

        WINDow = WINDow()  # type: ignore
        """
        DISPlay:WINDow

        Arguments:
        """

    DISPlay = DISPlay()  # type: ignore
    """
    DISPlay

    Arguments:
    """

    class DISplay(SCPINode, SCPISet):
        """
        DISplay

        Arguments:
        """
        __slots__ = ()
        _cmd = "DISplay"
        args = []  # type: List[str]

    DISplay = DISplay()  # type: ignore
    """
    DISplay

    Arguments:
    """

    class ELAPsed(SCPINode, SCPIQuery):
        """
        ELAPsed

        Arguments:
        """
        __slots__ = ()
        _cmd = "ELAPsed"
        args = []  # type: List[str]

        class RESet(SCPINode, SCPISet):
            """
            ELAPsed:RESet

            Arguments:
            """
            __slots__ = ()
            _cmd = "RESet"
            args = []  # type: List[str]

        RESet = RESet()  # type: ignore
        """
        ELAPsed:RESet

        Arguments:
        """

    ELAPsed = ELAPsed()  # type: ignore
    """
    ELAPsed

    Arguments:
    """

    class ERASe(SCPINode, SCPISet):
        """
        ERASe

        Arguments:
        """
        __slots__ = ()
        _cmd = "ERASe"
        args = []  # type: List[str]

        class SWEep(SCPINode, SCPISet):
            """
            ERASe:SWEep

            Arguments:
            """
            __slots__ = ()
            _cmd = "SWEep"
            args = []  # type: List[str]

        SWEep = SWEep()  # type: ignore
        """
        ERASe:SWEep

        Arguments:
        """

    ERASe = ERASe()  # type: ignore
    """
    ERASe

    Arguments:
    """

    class ERRor(SCPINode, SCPIQuery):
        """
        ERRor

        Arguments:
        """
        __slots__ = ()
        _cmd = "ERRor"
        args = []  # type: List[str]

    ERRor = ERRor()  # type: ignore
    """
    ERRor

    Arguments:
    """

    class ERrors(SCPINode, SCPIQuery):
        """
        ERrors

        Arguments:
        """
        __slots__ = ()
        _cmd = "ERrors"
        args = []  # type: List[str]

    ERrors = ERrors()  # type: ignore
    """
    ERrors

    Arguments:
    """

    class EXTTrg(SCPINode, SCPISet):
        """
        EXTTrg

        Arguments: FLSWp, MEMDn, MEMup, SEQT, SSSWp, VOID
        """
        __slots__ = ()
        _cmd = "EXTTrg"
        args = ["FLSWp", "MEMDn", "MEMup", "SEQT", "SSSWp", "VOID"]

    EXTTrg = EXTTrg()  # type: ignore
    """
    EXTTrg

    Arguments: FLSWp, MEMDn, MEMup, SEQT, SSSWp, VOID
    """

    class EXecution_mode(SCPINode, SCPIQuery, SCPISet):
        """
        EXecution_mode

        Arguments:
        """
        __slots__ = ()
        _cmd = "EXecution_mode"
        args = []  # type: List[str]

        class Normal(SCPINode, SCPISet):
            """
            EXecution_mode:Normal

            Arguments:
            """
            __slots__ = ()
            _cmd = "Normal"
            args = []  # type: List[str]

        Normal = Normal()  # type: ignore
        """
        EXecution_mode:Normal

        Arguments:
        """

        class Triggered(SCPINode, SCPISet):
            """
            EXecution_mode:Triggered

            Arguments:
            """
            __slots__ = ()
            _cmd = "Triggered"
            args = []  # type: List[str]

        Triggered = Triggered()  # type: ignore
        """
        EXecution_mode:Triggered

        Arguments:
        """

    EXecution_mode = EXecution_mode()  # type: ignore
    """
    EXecution_mode

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
            `FORMat:BORDer
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/59b73d990b8d4acf.htm#ID_729c2ba54e7ed3070a00206a001affe3-8402e7834e7ed3070a00206a0024546d-en-US>`_

            Arguments: NORMal, SWAPped
            """
            __slots__ = ()
            _cmd = "BORDer"
            args = ["NORMal", "SWAPped"]

        BORDer = BORDer()  # type: ignore
        """
        `FORMat:BORDer
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/59b73d990b8d4acf.htm#ID_729c2ba54e7ed3070a00206a001affe3-8402e7834e7ed3070a00206a0024546d-en-US>`_

        Arguments: NORMal, SWAPped
        """

    FORMat = FORMat()  # type: ignore
    """
    FORMat

    Arguments:
    """

    class FREQuency(SCPINode):
        """
        FREQuency

        Arguments:
        """
        __slots__ = ()
        _cmd = "FREQuency"
        args = []  # type: List[str]

        class CENTer(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:CENTer

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "CENTer"
            args = ["1"]

            class STEP(SCPINode):
                """
                FREQuency:CENTer:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    FREQuency:CENTer:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                FREQuency:CENTer:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            FREQuency:CENTer:STEP

            Arguments:
            """

        CENTer = CENTer()  # type: ignore
        """
        FREQuency:CENTer

        Arguments: 1
        """

        class CW(SCPINode):
            """
            FREQuency:CW

            Arguments:
            """
            __slots__ = ()
            _cmd = "CW"
            args = []  # type: List[str]

            class STEP(SCPINode):
                """
                FREQuency:CW:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    FREQuency:CW:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                FREQuency:CW:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            FREQuency:CW:STEP

            Arguments:
            """

        CW = CW()  # type: ignore
        """
        FREQuency:CW

        Arguments:
        """

        class INSTantaneous(SCPINode, SCPIQuery):
            """
            FREQuency:INSTantaneous

            Arguments:
            """
            __slots__ = ()
            _cmd = "INSTantaneous"
            args = []  # type: List[str]

        INSTantaneous = INSTantaneous()  # type: ignore
        """
        FREQuency:INSTantaneous

        Arguments:
        """

        class MANual(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:MANual

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "MANual"
            args = ["1"]

        MANual = MANual()  # type: ignore
        """
        FREQuency:MANual

        Arguments: 1
        """

        class MULTiplier(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:MULTiplier

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "MULTiplier"
            args = ["1"]

        MULTiplier = MULTiplier()  # type: ignore
        """
        FREQuency:MULTiplier

        Arguments: 1
        """

        class OFFSet(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:OFFSet

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "OFFSet"
            args = ["1"]

        OFFSet = OFFSet()  # type: ignore
        """
        FREQuency:OFFSet

        Arguments: 1
        """

        class SPAN(SCPINode):
            """
            FREQuency:SPAN

            Arguments:
            """
            __slots__ = ()
            _cmd = "SPAN"
            args = []  # type: List[str]

            class STEP(SCPINode):
                """
                FREQuency:SPAN:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    FREQuency:SPAN:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                FREQuency:SPAN:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            FREQuency:SPAN:STEP

            Arguments:
            """

        SPAN = SPAN()  # type: ignore
        """
        FREQuency:SPAN

        Arguments:
        """

        class STARt(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:STARt

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "STARt"
            args = ["1"]

            class STEP(SCPINode):
                """
                FREQuency:STARt:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    FREQuency:STARt:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                FREQuency:STARt:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            FREQuency:STARt:STEP

            Arguments:
            """

        STARt = STARt()  # type: ignore
        """
        FREQuency:STARt

        Arguments: 1
        """

        class STOP(SCPINode):
            """
            FREQuency:STOP

            Arguments:
            """
            __slots__ = ()
            _cmd = "STOP"
            args = []  # type: List[str]

            class STEP(SCPINode):
                """
                FREQuency:STOP:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    FREQuency:STOP:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                FREQuency:STOP:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            FREQuency:STOP:STEP

            Arguments:
            """

        STOP = STOP()  # type: ignore
        """
        FREQuency:STOP

        Arguments:
        """

        class SYNThesis(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:SYNThesis

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "SYNThesis"
            args = ["1"]

        SYNThesis = SYNThesis()  # type: ignore
        """
        FREQuency:SYNThesis

        Arguments: 1
        """

    FREQuency = FREQuency()  # type: ignore
    """
    FREQuency

    Arguments:
    """

    class HEAder(SCPINode, SCPISet):
        """
        HEAder

        Arguments:
        """
        __slots__ = ()
        _cmd = "HEAder"
        args = []  # type: List[str]

    HEAder = HEAder()  # type: ignore
    """
    HEAder

    Arguments:
    """

    class HET_band(SCPINode, SCPISet):
        """
        HET_band

        Arguments:
        """
        __slots__ = ()
        _cmd = "HET_band"
        args = []  # type: List[str]

        class High(SCPINode, SCPISet):
            """
            HET_band:High

            Arguments:
            """
            __slots__ = ()
            _cmd = "High"
            args = []  # type: List[str]

        High = High()  # type: ignore
        """
        HET_band:High

        Arguments:
        """

        class Low(SCPINode, SCPISet):
            """
            HET_band:Low

            Arguments:
            """
            __slots__ = ()
            _cmd = "Low"
            args = []  # type: List[str]

        Low = Low()  # type: ignore
        """
        HET_band:Low

        Arguments:
        """

    HET_band = HET_band()  # type: ignore
    """
    HET_band

    Arguments:
    """

    class HOPSeq(SCPINode, SCPIQuery, SCPISet):
        """
        HOPSeq

        Arguments: <numeric_value>,<numeric_value>
        """
        __slots__ = ()
        _cmd = "HOPSeq"
        args = ["<numeric_value>,<numeric_value>"]

    HOPSeq = HOPSeq()  # type: ignore
    """
    HOPSeq

    Arguments: <numeric_value>,<numeric_value>
    """

    class IMODe(SCPINode, SCPISet):
        """
        IMODe

        Arguments: NORMal, SWEeper
        """
        __slots__ = ()
        _cmd = "IMODe"
        args = ["NORMal", "SWEeper"]

    IMODe = IMODe()  # type: ignore
    """
    IMODe

    Arguments: NORMal, SWEeper
    """

    class IMPedance(SCPINode, SCPIQuery, SCPISet):
        """
        IMPedance

        Arguments: Z50R, Z75R
        """
        __slots__ = ()
        _cmd = "IMPedance"
        args = ["Z50R", "Z75R"]

    IMPedance = IMPedance()  # type: ignore
    """
    IMPedance

    Arguments: Z50R, Z75R
    """

    class INITialize(SCPINode):
        """
        INITialize

        Arguments:
        """
        __slots__ = ()
        _cmd = "INITialize"
        args = []  # type: List[str]

        class ABORt(SCPINode, SCPISet):
            """
            INITialize:ABORt

            Arguments:
            """
            __slots__ = ()
            _cmd = "ABORt"
            args = []  # type: List[str]

        ABORt = ABORt()  # type: ignore
        """
        INITialize:ABORt

        Arguments:
        """

        class CONTinuous(SCPINode, SCPIBool):
            """
            INITialize:CONTinuous

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "CONTinuous"
            args = ["1", "ON", "OFF"]

        CONTinuous = CONTinuous()  # type: ignore
        """
        INITialize:CONTinuous

        Arguments: 1, ON, OFF
        """

        class IMMediate(SCPINode, SCPISet):
            """
            INITialize:IMMediate

            Arguments:
            """
            __slots__ = ()
            _cmd = "IMMediate"
            args = []  # type: List[str]

        IMMediate = IMMediate()  # type: ignore
        """
        INITialize:IMMediate

        Arguments:
        """

        class STATe(SCPINode, SCPIQuery, SCPISet):
            """
            INITialize:STATe

            Arguments: PAUSe, RUN
            """
            __slots__ = ()
            _cmd = "STATe"
            args = ["PAUSe", "RUN"]

        STATe = STATe()  # type: ignore
        """
        INITialize:STATe

        Arguments: PAUSe, RUN
        """

    INITialize = INITialize()  # type: ignore
    """
    INITialize

    Arguments:
    """

    class INITiate(SCPINode, SCPISet):
        """
        INITiate

        Arguments:
        """
        __slots__ = ()
        _cmd = "INITiate"
        args = []  # type: List[str]

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

    class INPut(SCPINode):
        """
        INPut

        Arguments:
        """
        __slots__ = ()
        _cmd = "INPut"
        args = []  # type: List[str]

        class IF(SCPINode):
            """
            INPut:IF

            Arguments:
            """
            __slots__ = ()
            _cmd = "IF"
            args = []  # type: List[str]

            class STATe(SCPINode, SCPIBool):
                """
                INPut:IF:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            INPut:IF:STATe

            Arguments: 1, ON, OFF
            """

        IF = IF()  # type: ignore
        """
        INPut:IF

        Arguments:
        """

        class POLarity(SCPINode, SCPIQuery, SCPISet):
            """
            INPut:POLarity

            Arguments: INVerted, NORMal
            """
            __slots__ = ()
            _cmd = "POLarity"
            args = ["INVerted", "NORMal"]

        POLarity = POLarity()  # type: ignore
        """
        INPut:POLarity

        Arguments: INVerted, NORMal
        """

    INPut = INPut()  # type: ignore
    """
    INPut

    Arguments:
    """

    class Increment(SCPINode, SCPISet):
        """
        Increment

        Arguments:
        """
        __slots__ = ()
        _cmd = "Increment"
        args = []  # type: List[str]

        class PHAse(SCPINode, SCPISet):
            """
            Increment:PHAse

            Arguments:
            """
            __slots__ = ()
            _cmd = "PHAse"
            args = []  # type: List[str]

        PHAse = PHAse()  # type: ignore
        """
        Increment:PHAse

        Arguments:
        """

        class Swp(SCPINode, SCPISet):
            """
            Increment:Swp

            Arguments:
            """
            __slots__ = ()
            _cmd = "Swp"
            args = []  # type: List[str]

        Swp = Swp()  # type: ignore
        """
        Increment:Swp

        Arguments:
        """

    Increment = Increment()  # type: ignore
    """
    Increment

    Arguments:
    """

    class KLOCk(SCPINode, SCPISet):
        """
        KLOCk

        Arguments:
        """
        __slots__ = ()
        _cmd = "KLOCk"
        args = []  # type: List[str]

    KLOCk = KLOCk()  # type: ignore
    """
    KLOCk

    Arguments:
    """

    class KUNLock(SCPINode, SCPISet):
        """
        KUNLock

        Arguments:
        """
        __slots__ = ()
        _cmd = "KUNLock"
        args = []  # type: List[str]

    KUNLock = KUNLock()  # type: ignore
    """
    KUNLock

    Arguments:
    """

    class LFSource(SCPINodeN):
        """
        LFSource

        Arguments:
        """
        __slots__ = ()
        _cmd = "LFSource"
        args = []  # type: List[str]

        class AM(SCPINode):
            """
            LFSource:AM

            Arguments:
            """
            __slots__ = ()
            _cmd = "AM"
            args = []  # type: List[str]

            class DEPTh(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:AM:DEPTh

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DEPTh"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:AM:DEPTh:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:AM:DEPTh:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    LFSource:AM:DEPTh:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                LFSource:AM:DEPTh:STEP

                Arguments:
                """

            DEPTh = DEPTh()  # type: ignore
            """
            LFSource:AM:DEPTh

            Arguments: 1
            """

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:AM:FREQuency

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:AM:FREQuency:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:AM:FREQuency:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    LFSource:AM:FREQuency:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                LFSource:AM:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()  # type: ignore
            """
            LFSource:AM:FREQuency

            Arguments: 1
            """

            class PHASe(SCPINode):
                """
                LFSource:AM:PHASe

                Arguments:
                """
                __slots__ = ()
                _cmd = "PHASe"
                args = []  # type: List[str]

                class ADJust(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:AM:PHASe:ADJust

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ADJust"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        LFSource:AM:PHASe:ADJust:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            LFSource:AM:PHASe:ADJust:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        LFSource:AM:PHASe:ADJust:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    LFSource:AM:PHASe:ADJust:STEP

                    Arguments:
                    """

                ADJust = ADJust()  # type: ignore
                """
                LFSource:AM:PHASe:ADJust

                Arguments: 1
                """

            PHASe = PHASe()  # type: ignore
            """
            LFSource:AM:PHASe

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                LFSource:AM:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            LFSource:AM:STATe

            Arguments: 1, ON, OFF
            """

            class WAVeform(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:AM:WAVeform

                Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
                """
                __slots__ = ()
                _cmd = "WAVeform"
                args = ["SAWTooth", "SINE", "SQUare", "TRIangle", "WGNoise"]

            WAVeform = WAVeform()  # type: ignore
            """
            LFSource:AM:WAVeform

            Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
            """

        AM = AM()  # type: ignore
        """
        LFSource:AM

        Arguments:
        """

        class AVIonics(SCPINode):
            """
            LFSource:AVIonics

            Arguments:
            """
            __slots__ = ()
            _cmd = "AVIonics"
            args = []  # type: List[str]

            class SETup(SCPINode):
                """
                LFSource:AVIonics:SETup

                Arguments:
                """
                __slots__ = ()
                _cmd = "SETup"
                args = []  # type: List[str]

                class GSLope(SCPINode, SCPISet):
                    """
                    LFSource:AVIonics:SETup:GSLope

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "GSLope"
                    args = []  # type: List[str]

                GSLope = GSLope()  # type: ignore
                """
                LFSource:AVIonics:SETup:GSLope

                Arguments:
                """

                class IMBeacon(SCPINode, SCPISet):
                    """
                    LFSource:AVIonics:SETup:IMBeacon

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "IMBeacon"
                    args = []  # type: List[str]

                IMBeacon = IMBeacon()  # type: ignore
                """
                LFSource:AVIonics:SETup:IMBeacon

                Arguments:
                """

                class LOCalizer(SCPINode, SCPISet):
                    """
                    LFSource:AVIonics:SETup:LOCalizer

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "LOCalizer"
                    args = []  # type: List[str]

                LOCalizer = LOCalizer()  # type: ignore
                """
                LFSource:AVIonics:SETup:LOCalizer

                Arguments:
                """

                class MMBeacon(SCPINode, SCPISet):
                    """
                    LFSource:AVIonics:SETup:MMBeacon

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "MMBeacon"
                    args = []  # type: List[str]

                MMBeacon = MMBeacon()  # type: ignore
                """
                LFSource:AVIonics:SETup:MMBeacon

                Arguments:
                """

                class OMBeacon(SCPINode, SCPISet):
                    """
                    LFSource:AVIonics:SETup:OMBeacon

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "OMBeacon"
                    args = []  # type: List[str]

                OMBeacon = OMBeacon()  # type: ignore
                """
                LFSource:AVIonics:SETup:OMBeacon

                Arguments:
                """

            SETup = SETup()  # type: ignore
            """
            LFSource:AVIonics:SETup

            Arguments:
            """

        AVIonics = AVIonics()  # type: ignore
        """
        LFSource:AVIonics

        Arguments:
        """

        class FM(SCPINode):
            """
            LFSource:FM

            Arguments:
            """
            __slots__ = ()
            _cmd = "FM"
            args = []  # type: List[str]

            class DEViation(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:FM:DEViation

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DEViation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:FM:DEViation:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:FM:DEViation:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    LFSource:FM:DEViation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                LFSource:FM:DEViation:STEP

                Arguments:
                """

            DEViation = DEViation()  # type: ignore
            """
            LFSource:FM:DEViation

            Arguments: 1
            """

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:FM:FREQuency

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:FM:FREQuency:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:FM:FREQuency:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    LFSource:FM:FREQuency:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                LFSource:FM:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()  # type: ignore
            """
            LFSource:FM:FREQuency

            Arguments: 1
            """

            class PHASe(SCPINode):
                """
                LFSource:FM:PHASe

                Arguments:
                """
                __slots__ = ()
                _cmd = "PHASe"
                args = []  # type: List[str]

                class ADJust(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:FM:PHASe:ADJust

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ADJust"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        LFSource:FM:PHASe:ADJust:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            LFSource:FM:PHASe:ADJust:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        LFSource:FM:PHASe:ADJust:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    LFSource:FM:PHASe:ADJust:STEP

                    Arguments:
                    """

                ADJust = ADJust()  # type: ignore
                """
                LFSource:FM:PHASe:ADJust

                Arguments: 1
                """

            PHASe = PHASe()  # type: ignore
            """
            LFSource:FM:PHASe

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                LFSource:FM:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            LFSource:FM:STATe

            Arguments: 1, ON, OFF
            """

            class WAVeform(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:FM:WAVeform

                Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
                """
                __slots__ = ()
                _cmd = "WAVeform"
                args = ["SAWTooth", "SINE", "SQUare", "TRIangle", "WGNoise"]

            WAVeform = WAVeform()  # type: ignore
            """
            LFSource:FM:WAVeform

            Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
            """

        FM = FM()  # type: ignore
        """
        LFSource:FM

        Arguments:
        """

        class FREQuency(SCPINodeN, SCPIQuery, SCPISet):
            """
            LFSource:FREQuency

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "FREQuency"
            args = ["1"]

            class STEP(SCPINode):
                """
                LFSource:FREQuency:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:FREQuency:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                LFSource:FREQuency:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            LFSource:FREQuency:STEP

            Arguments:
            """

        FREQuency = FREQuency()  # type: ignore
        """
        LFSource:FREQuency

        Arguments: 1
        """

        class LEVel(SCPINodeN, SCPIQuery, SCPISet):
            """
            LFSource:LEVel

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "LEVel"
            args = ["1"]

            class STEP(SCPINode):
                """
                LFSource:LEVel:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:LEVel:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                LFSource:LEVel:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            LFSource:LEVel:STEP

            Arguments:
            """

        LEVel = LEVel()  # type: ignore
        """
        LFSource:LEVel

        Arguments: 1
        """

        class PHASe(SCPINodeN):
            """
            LFSource:PHASe

            Arguments:
            """
            __slots__ = ()
            _cmd = "PHASe"
            args = []  # type: List[str]

            class ADJust(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:PHASe:ADJust

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ADJust"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:PHASe:ADJust:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:PHASe:ADJust:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    LFSource:PHASe:ADJust:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                LFSource:PHASe:ADJust:STEP

                Arguments:
                """

            ADJust = ADJust()  # type: ignore
            """
            LFSource:PHASe:ADJust

            Arguments: 1
            """

        PHASe = PHASe()  # type: ignore
        """
        LFSource:PHASe

        Arguments:
        """

        class PM(SCPINode):
            """
            LFSource:PM

            Arguments:
            """
            __slots__ = ()
            _cmd = "PM"
            args = []  # type: List[str]

            class DEViation(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:PM:DEViation

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DEViation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:PM:DEViation:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:PM:DEViation:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    LFSource:PM:DEViation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                LFSource:PM:DEViation:STEP

                Arguments:
                """

            DEViation = DEViation()  # type: ignore
            """
            LFSource:PM:DEViation

            Arguments: 1
            """

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:PM:FREQuency

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:PM:FREQuency:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:PM:FREQuency:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    LFSource:PM:FREQuency:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                LFSource:PM:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()  # type: ignore
            """
            LFSource:PM:FREQuency

            Arguments: 1
            """

            class PHASe(SCPINode):
                """
                LFSource:PM:PHASe

                Arguments:
                """
                __slots__ = ()
                _cmd = "PHASe"
                args = []  # type: List[str]

                class ADJust(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:PM:PHASe:ADJust

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ADJust"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        LFSource:PM:PHASe:ADJust:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            LFSource:PM:PHASe:ADJust:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        LFSource:PM:PHASe:ADJust:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    LFSource:PM:PHASe:ADJust:STEP

                    Arguments:
                    """

                ADJust = ADJust()  # type: ignore
                """
                LFSource:PM:PHASe:ADJust

                Arguments: 1
                """

            PHASe = PHASe()  # type: ignore
            """
            LFSource:PM:PHASe

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                LFSource:PM:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            LFSource:PM:STATe

            Arguments: 1, ON, OFF
            """

            class WAVeform(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:PM:WAVeform

                Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
                """
                __slots__ = ()
                _cmd = "WAVeform"
                args = ["SAWTooth", "SINE", "SQUare", "TRIangle", "WGNoise"]

            WAVeform = WAVeform()  # type: ignore
            """
            LFSource:PM:WAVeform

            Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
            """

        PM = PM()  # type: ignore
        """
        LFSource:PM

        Arguments:
        """

        class PULSe(SCPINode):
            """
            LFSource:PULSe

            Arguments:
            """
            __slots__ = ()
            _cmd = "PULSe"
            args = []  # type: List[str]

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:PULSe:FREQuency

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:PULSe:FREQuency:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:PULSe:FREQuency:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    LFSource:PULSe:FREQuency:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                LFSource:PULSe:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()  # type: ignore
            """
            LFSource:PULSe:FREQuency

            Arguments: 1
            """

            class PHASe(SCPINode):
                """
                LFSource:PULSe:PHASe

                Arguments:
                """
                __slots__ = ()
                _cmd = "PHASe"
                args = []  # type: List[str]

                class ADJust(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:PULSe:PHASe:ADJust

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ADJust"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        LFSource:PULSe:PHASe:ADJust:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            LFSource:PULSe:PHASe:ADJust:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        LFSource:PULSe:PHASe:ADJust:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    LFSource:PULSe:PHASe:ADJust:STEP

                    Arguments:
                    """

                ADJust = ADJust()  # type: ignore
                """
                LFSource:PULSe:PHASe:ADJust

                Arguments: 1
                """

            PHASe = PHASe()  # type: ignore
            """
            LFSource:PULSe:PHASe

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                LFSource:PULSe:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            LFSource:PULSe:STATe

            Arguments: 1, ON, OFF
            """

        PULSe = PULSe()  # type: ignore
        """
        LFSource:PULSe

        Arguments:
        """

        class STATe(SCPINodeN, SCPIBool):
            """
            LFSource:STATe

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()  # type: ignore
        """
        LFSource:STATe

        Arguments: 1, ON, OFF
        """

        class TRIGger(SCPINode):
            """
            LFSource:TRIGger

            Arguments:
            """
            __slots__ = ()
            _cmd = "TRIGger"
            args = []  # type: List[str]

            class IMMediate(SCPINode, SCPISet):
                """
                LFSource:TRIGger:IMMediate

                Arguments:
                """
                __slots__ = ()
                _cmd = "IMMediate"
                args = []  # type: List[str]

            IMMediate = IMMediate()  # type: ignore
            """
            LFSource:TRIGger:IMMediate

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:TRIGger:SOURce

                Arguments: CONTinuous, EXTernal
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["CONTinuous", "EXTernal"]

            SOURce = SOURce()  # type: ignore
            """
            LFSource:TRIGger:SOURce

            Arguments: CONTinuous, EXTernal
            """

        TRIGger = TRIGger()  # type: ignore
        """
        LFSource:TRIGger

        Arguments:
        """

        class WAVeform(SCPINodeN, SCPIQuery, SCPISet):
            """
            LFSource:WAVeform

            Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
            """
            __slots__ = ()
            _cmd = "WAVeform"
            args = ["SAWTooth", "SINE", "SQUare", "TRIangle", "WGNoise"]

        WAVeform = WAVeform()  # type: ignore
        """
        LFSource:WAVeform

        Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
        """

    LFSource = LFSource()  # type: ignore
    """
    LFSource

    Arguments:
    """

    class Level(SCPINode):
        """
        Level

        Arguments:
        """
        __slots__ = ()
        _cmd = "Level"
        args = []  # type: List[str]

        class AF(SCPINode):
            """
            Level:AF

            Arguments:
            """
            __slots__ = ()
            _cmd = "AF"
            args = []  # type: List[str]

            class Var_step(SCPINode, SCPIQuery, SCPISet):
                """
                Level:AF:Var_step

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "Var_step"
                args = ["1"]

            Var_step = Var_step()  # type: ignore
            """
            Level:AF:Var_step

            Arguments: 1
            """

        AF = AF()  # type: ignore
        """
        Level:AF

        Arguments:
        """

        class RF(SCPINode):
            """
            Level:RF

            Arguments:
            """
            __slots__ = ()
            _cmd = "RF"
            args = []  # type: List[str]

            class CONtrol(SCPINode, SCPISet):
                """
                Level:RF:CONtrol

                Arguments:
                """
                __slots__ = ()
                _cmd = "CONtrol"
                args = []  # type: List[str]

                class Calibration(SCPINode, SCPISet):
                    """
                    Level:RF:CONtrol:Calibration

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "Calibration"
                    args = []  # type: List[str]

                Calibration = Calibration()  # type: ignore
                """
                Level:RF:CONtrol:Calibration

                Arguments:
                """

                class Lookup(SCPINode, SCPISet):
                    """
                    Level:RF:CONtrol:Lookup

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "Lookup"
                    args = []  # type: List[str]

                Lookup = Lookup()  # type: ignore
                """
                Level:RF:CONtrol:Lookup

                Arguments:
                """

            CONtrol = CONtrol()  # type: ignore
            """
            Level:RF:CONtrol

            Arguments:
            """

            class CORRECT_Index(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:CORRECT_Index

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "CORRECT_Index"
                args = ["1"]

            CORRECT_Index = CORRECT_Index()  # type: ignore
            """
            Level:RF:CORRECT_Index

            Arguments: 1
            """

            class Emf(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:Emf

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "Emf"
                args = ["1"]

            Emf = Emf()  # type: ignore
            """
            Level:RF:Emf

            Arguments: 1
            """

            class Marker(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:Marker

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "Marker"
                args = ["1"]

            Marker = Marker()  # type: ignore
            """
            Level:RF:Marker

            Arguments: 1
            """

            class OFFSet(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:OFFSet

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "OFFSet"
                args = ["1"]

            OFFSet = OFFSet()  # type: ignore
            """
            Level:RF:OFFSet

            Arguments: 1
            """

            class STArt(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:STArt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STArt"
                args = ["1"]

            STArt = STArt()  # type: ignore
            """
            Level:RF:STArt

            Arguments: 1
            """

            class STEp(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:STEp

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STEp"
                args = ["1"]

            STEp = STEp()  # type: ignore
            """
            Level:RF:STEp

            Arguments: 1
            """

            class STOp(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:STOp

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STOp"
                args = ["1"]

            STOp = STOp()  # type: ignore
            """
            Level:RF:STOp

            Arguments: 1
            """

            class Var_step(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:Var_step

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "Var_step"
                args = ["1"]

            Var_step = Var_step()  # type: ignore
            """
            Level:RF:Var_step

            Arguments: 1
            """

        RF = RF()  # type: ignore
        """
        Level:RF

        Arguments:
        """

    Level = Level()  # type: ignore
    """
    Level

    Arguments:
    """

    class MARKer(SCPINodeN):
        """
        MARKer

        Arguments:
        """
        __slots__ = ()
        _cmd = "MARKer"
        args = []  # type: List[str]

        class FREQuency(SCPINode, SCPIQuery, SCPISet):
            """
            MARKer:FREQuency

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "FREQuency"
            args = ["1"]

            class STEP(SCPINode):
                """
                MARKer:FREQuency:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    MARKer:FREQuency:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                MARKer:FREQuency:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            MARKer:FREQuency:STEP

            Arguments:
            """

        FREQuency = FREQuency()  # type: ignore
        """
        MARKer:FREQuency

        Arguments: 1
        """

        class STATe(SCPINode, SCPIBool):
            """
            MARKer:STATe

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()  # type: ignore
        """
        MARKer:STATe

        Arguments: 1, ON, OFF
        """

    MARKer = MARKer()  # type: ignore
    """
    MARKer

    Arguments:
    """

    class MEMory(SCPINode, SCPISet):
        """
        MEMory

        Arguments:
        """
        __slots__ = ()
        _cmd = "MEMory"
        args = []  # type: List[str]

        class CATalog(SCPINode):
            """
            MEMory:CATalog

            Arguments:
            """
            __slots__ = ()
            _cmd = "CATalog"
            args = []  # type: List[str]

            class BINary(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:BINary

                Arguments:
                """
                __slots__ = ()
                _cmd = "BINary"
                args = []  # type: List[str]

            BINary = BINary()  # type: ignore
            """
            MEMory:CATalog:BINary

            Arguments:
            """

            class DWCDma(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:DWCDma

                Arguments:
                """
                __slots__ = ()
                _cmd = "DWCDma"
                args = []  # type: List[str]

            DWCDma = DWCDma()  # type: ignore
            """
            MEMory:CATalog:DWCDma

            Arguments:
            """

            class FCDMa(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:FCDMa

                Arguments:
                """
                __slots__ = ()
                _cmd = "FCDMa"
                args = []  # type: List[str]

            FCDMa = FCDMa()  # type: ignore
            """
            MEMory:CATalog:FCDMa

            Arguments:
            """

            class MCDMa(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:MCDMa

                Arguments:
                """
                __slots__ = ()
                _cmd = "MCDMa"
                args = []  # type: List[str]

            MCDMa = MCDMa()  # type: ignore
            """
            MEMory:CATalog:MCDMa

            Arguments:
            """

            class MDMod(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:MDMod

                Arguments:
                """
                __slots__ = ()
                _cmd = "MDMod"
                args = []  # type: List[str]

            MDMod = MDMod()  # type: ignore
            """
            MEMory:CATalog:MDMod

            Arguments:
            """

            class MDWCdma(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:MDWCdma

                Arguments:
                """
                __slots__ = ()
                _cmd = "MDWCdma"
                args = []  # type: List[str]

            MDWCdma = MDWCdma()  # type: ignore
            """
            MEMory:CATalog:MDWCdma

            Arguments:
            """

            class MFCDma(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:MFCDma

                Arguments:
                """
                __slots__ = ()
                _cmd = "MFCDma"
                args = []  # type: List[str]

            MFCDma = MFCDma()  # type: ignore
            """
            MEMory:CATalog:MFCDma

            Arguments:
            """

            class MTONe(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:MTONe

                Arguments:
                """
                __slots__ = ()
                _cmd = "MTONe"
                args = []  # type: List[str]

            MTONe = MTONe()  # type: ignore
            """
            MEMory:CATalog:MTONe

            Arguments:
            """

            class RCDMa(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:RCDMa

                Arguments:
                """
                __slots__ = ()
                _cmd = "RCDMa"
                args = []  # type: List[str]

            RCDMa = RCDMa()  # type: ignore
            """
            MEMory:CATalog:RCDMa

            Arguments:
            """

            class SHAPe(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:SHAPe

                Arguments:
                """
                __slots__ = ()
                _cmd = "SHAPe"
                args = []  # type: List[str]

            SHAPe = SHAPe()  # type: ignore
            """
            MEMory:CATalog:SHAPe

            Arguments:
            """

            class STATe(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:STATe

                Arguments:
                """
                __slots__ = ()
                _cmd = "STATe"
                args = []  # type: List[str]

            STATe = STATe()  # type: ignore
            """
            MEMory:CATalog:STATe

            Arguments:
            """

            class TABLe(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:TABLe

                Arguments:
                """
                __slots__ = ()
                _cmd = "TABLe"
                args = []  # type: List[str]

            TABLe = TABLe()  # type: ignore
            """
            MEMory:CATalog:TABLe

            Arguments:
            """

            class UWCDma(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:UWCDma

                Arguments:
                """
                __slots__ = ()
                _cmd = "UWCDma"
                args = []  # type: List[str]

            UWCDma = UWCDma()  # type: ignore
            """
            MEMory:CATalog:UWCDma

            Arguments:
            """

        CATalog = CATalog()  # type: ignore
        """
        MEMory:CATalog

        Arguments:
        """

        class DATA(SCPINode):
            """
            MEMory:DATA

            Arguments:
            """
            __slots__ = ()
            _cmd = "DATA"
            args = []  # type: List[str]

            class APPend(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:DATA:APPend

                Arguments: <string>,<block_data>
                """
                __slots__ = ()
                _cmd = "APPend"
                args = ["<string>,<block_data>"]

            APPend = APPend()  # type: ignore
            """
            MEMory:DATA:APPend

            Arguments: <string>,<block_data>
            """

            class PRAM(SCPINode):
                """
                MEMory:DATA:PRAM

                Arguments:
                """
                __slots__ = ()
                _cmd = "PRAM"
                args = []  # type: List[str]

                class FILE(SCPINode):
                    """
                    MEMory:DATA:PRAM:FILE

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "FILE"
                    args = []  # type: List[str]

                    class BLOCk(SCPINode, SCPIQuery, SCPISet):
                        """
                        MEMory:DATA:PRAM:FILE:BLOCk

                        Arguments: <string>,<block_data>
                        """
                        __slots__ = ()
                        _cmd = "BLOCk"
                        args = ["<string>,<block_data>"]

                    BLOCk = BLOCk()  # type: ignore
                    """
                    MEMory:DATA:PRAM:FILE:BLOCk

                    Arguments: <string>,<block_data>
                    """

                FILE = FILE()  # type: ignore
                """
                MEMory:DATA:PRAM:FILE

                Arguments:
                """

            PRAM = PRAM()  # type: ignore
            """
            MEMory:DATA:PRAM

            Arguments:
            """

            class SHAPe(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:DATA:SHAPe

                Arguments: <string>,<numeric_value>,<numeric_value>
                """
                __slots__ = ()
                _cmd = "SHAPe"
                args = ["<string>,<numeric_value>,<numeric_value>"]

            SHAPe = SHAPe()  # type: ignore
            """
            MEMory:DATA:SHAPe

            Arguments: <string>,<numeric_value>,<numeric_value>
            """

            class UNPRotected(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:DATA:UNPRotected

                Arguments: <string>,<block_data>
                """
                __slots__ = ()
                _cmd = "UNPRotected"
                args = ["<string>,<block_data>"]

            UNPRotected = UNPRotected()  # type: ignore
            """
            MEMory:DATA:UNPRotected

            Arguments: <string>,<block_data>
            """

        DATA = DATA()  # type: ignore
        """
        MEMory:DATA

        Arguments:
        """

        class DELete(SCPINode):
            """
            MEMory:DELete

            Arguments:
            """
            __slots__ = ()
            _cmd = "DELete"
            args = []  # type: List[str]

            class BINary(SCPINode, SCPISet):
                """
                MEMory:DELete:BINary

                Arguments:
                """
                __slots__ = ()
                _cmd = "BINary"
                args = []  # type: List[str]

            BINary = BINary()  # type: ignore
            """
            MEMory:DELete:BINary

            Arguments:
            """

            class DWCDma(SCPINode, SCPISet):
                """
                MEMory:DELete:DWCDma

                Arguments:
                """
                __slots__ = ()
                _cmd = "DWCDma"
                args = []  # type: List[str]

            DWCDma = DWCDma()  # type: ignore
            """
            MEMory:DELete:DWCDma

            Arguments:
            """

            class FCDMa(SCPINode, SCPISet):
                """
                MEMory:DELete:FCDMa

                Arguments:
                """
                __slots__ = ()
                _cmd = "FCDMa"
                args = []  # type: List[str]

            FCDMa = FCDMa()  # type: ignore
            """
            MEMory:DELete:FCDMa

            Arguments:
            """

            class MCDMa(SCPINode, SCPISet):
                """
                MEMory:DELete:MCDMa

                Arguments:
                """
                __slots__ = ()
                _cmd = "MCDMa"
                args = []  # type: List[str]

            MCDMa = MCDMa()  # type: ignore
            """
            MEMory:DELete:MCDMa

            Arguments:
            """

            class MDMod(SCPINode, SCPISet):
                """
                MEMory:DELete:MDMod

                Arguments:
                """
                __slots__ = ()
                _cmd = "MDMod"
                args = []  # type: List[str]

            MDMod = MDMod()  # type: ignore
            """
            MEMory:DELete:MDMod

            Arguments:
            """

            class MDWCdma(SCPINode, SCPISet):
                """
                MEMory:DELete:MDWCdma

                Arguments:
                """
                __slots__ = ()
                _cmd = "MDWCdma"
                args = []  # type: List[str]

            MDWCdma = MDWCdma()  # type: ignore
            """
            MEMory:DELete:MDWCdma

            Arguments:
            """

            class MFCDma(SCPINode, SCPISet):
                """
                MEMory:DELete:MFCDma

                Arguments:
                """
                __slots__ = ()
                _cmd = "MFCDma"
                args = []  # type: List[str]

            MFCDma = MFCDma()  # type: ignore
            """
            MEMory:DELete:MFCDma

            Arguments:
            """

            class MTONe(SCPINode, SCPISet):
                """
                MEMory:DELete:MTONe

                Arguments:
                """
                __slots__ = ()
                _cmd = "MTONe"
                args = []  # type: List[str]

            MTONe = MTONe()  # type: ignore
            """
            MEMory:DELete:MTONe

            Arguments:
            """

            class RCDMa(SCPINode, SCPISet):
                """
                MEMory:DELete:RCDMa

                Arguments:
                """
                __slots__ = ()
                _cmd = "RCDMa"
                args = []  # type: List[str]

            RCDMa = RCDMa()  # type: ignore
            """
            MEMory:DELete:RCDMa

            Arguments:
            """

            class SHAPe(SCPINode, SCPISet):
                """
                MEMory:DELete:SHAPe

                Arguments:
                """
                __slots__ = ()
                _cmd = "SHAPe"
                args = []  # type: List[str]

            SHAPe = SHAPe()  # type: ignore
            """
            MEMory:DELete:SHAPe

            Arguments:
            """

            class STATe(SCPINode, SCPISet):
                """
                MEMory:DELete:STATe

                Arguments:
                """
                __slots__ = ()
                _cmd = "STATe"
                args = []  # type: List[str]

            STATe = STATe()  # type: ignore
            """
            MEMory:DELete:STATe

            Arguments:
            """

            class UWCDma(SCPINode, SCPISet):
                """
                MEMory:DELete:UWCDma

                Arguments:
                """
                __slots__ = ()
                _cmd = "UWCDma"
                args = []  # type: List[str]

            UWCDma = UWCDma()  # type: ignore
            """
            MEMory:DELete:UWCDma

            Arguments:
            """

        DELete = DELete()  # type: ignore
        """
        MEMory:DELete

        Arguments:
        """

        class FREE(SCPINode):
            """
            MEMory:FREE

            Arguments:
            """
            __slots__ = ()
            _cmd = "FREE"
            args = []  # type: List[str]

            class MACRo(SCPINode, SCPIQuery):
                """
                MEMory:FREE:MACRo

                Arguments:
                """
                __slots__ = ()
                _cmd = "MACRo"
                args = []  # type: List[str]

            MACRo = MACRo()  # type: ignore
            """
            MEMory:FREE:MACRo

            Arguments:
            """

        FREE = FREE()  # type: ignore
        """
        MEMory:FREE

        Arguments:
        """

        class NSTates(SCPINode, SCPIQuery):
            """
            MEMory:NSTates

            Arguments:
            """
            __slots__ = ()
            _cmd = "NSTates"
            args = []  # type: List[str]

        NSTates = NSTates()  # type: ignore
        """
        MEMory:NSTates

        Arguments:
        """

        class STATe(SCPINode, SCPISet):
            """
            MEMory:STATe

            Arguments:
            """
            __slots__ = ()
            _cmd = "STATe"
            args = []  # type: List[str]

            class COMMent(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:STATe:COMMent

                Arguments: <numeric_value>,<numeric_value>,<string>
                """
                __slots__ = ()
                _cmd = "COMMent"
                args = ["<numeric_value>,<numeric_value>,<string>"]

            COMMent = COMMent()  # type: ignore
            """
            MEMory:STATe:COMMent

            Arguments: <numeric_value>,<numeric_value>,<string>
            """

        STATe = STATe()  # type: ignore
        """
        MEMory:STATe

        Arguments:
        """

        class STORe(SCPINode, SCPISet):
            """
            MEMory:STORe

            Arguments:
            """
            __slots__ = ()
            _cmd = "STORe"
            args = []  # type: List[str]

        STORe = STORe()  # type: ignore
        """
        MEMory:STORe

        Arguments:
        """

        class TABLe(SCPINode):
            """
            MEMory:TABLe

            Arguments:
            """
            __slots__ = ()
            _cmd = "TABLe"
            args = []  # type: List[str]

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:TABLe:FREQuency

                Arguments: <numeric_value>[AHZ, FHZ, PHZ, NHZ, UHZ, HZ, KHZ, MHZ, GHZ, THZ, PEHZ, EXHZ],<numeric_value>
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = ["<numeric_value>[AHZ", "FHZ", "PHZ", "NHZ", "UHZ", "HZ", "KHZ", "MHZ", "GHZ", "THZ", "PEHZ", "EXHZ],<numeric_value>"]

                class POINts(SCPINode, SCPIQuery):
                    """
                    MEMory:TABLe:FREQuency:POINts

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "POINts"
                    args = ["1"]

                POINts = POINts()  # type: ignore
                """
                MEMory:TABLe:FREQuency:POINts

                Arguments: 1
                """

            FREQuency = FREQuency()  # type: ignore
            """
            MEMory:TABLe:FREQuency

            Arguments: <numeric_value>[AHZ, FHZ, PHZ, NHZ, UHZ, HZ, KHZ, MHZ, GHZ, THZ, PEHZ, EXHZ],<numeric_value>
            """

            class LOSS(SCPINode):
                """
                MEMory:TABLe:LOSS

                Arguments:
                """
                __slots__ = ()
                _cmd = "LOSS"
                args = []  # type: List[str]

                class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    MEMory:TABLe:LOSS:MAGNitude

                    Arguments: <numeric_value>[DB],<numeric_value>
                    """
                    __slots__ = ()
                    _cmd = "MAGNitude"
                    args = ["<numeric_value>[DB],<numeric_value>"]

                    class POINts(SCPINode, SCPIQuery):
                        """
                        MEMory:TABLe:LOSS:MAGNitude:POINts

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "POINts"
                        args = ["1"]

                    POINts = POINts()  # type: ignore
                    """
                    MEMory:TABLe:LOSS:MAGNitude:POINts

                    Arguments: 1
                    """

                MAGNitude = MAGNitude()  # type: ignore
                """
                MEMory:TABLe:LOSS:MAGNitude

                Arguments: <numeric_value>[DB],<numeric_value>
                """

            LOSS = LOSS()  # type: ignore
            """
            MEMory:TABLe:LOSS

            Arguments:
            """

            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:TABLe:SELect

                Arguments: FDAT1, FDAT2, FDAT3, FDAT4
                """
                __slots__ = ()
                _cmd = "SELect"
                args = ["FDAT1", "FDAT2", "FDAT3", "FDAT4"]

            SELect = SELect()  # type: ignore
            """
            MEMory:TABLe:SELect

            Arguments: FDAT1, FDAT2, FDAT3, FDAT4
            """

        TABLe = TABLe()  # type: ignore
        """
        MEMory:TABLe

        Arguments:
        """

    MEMory = MEMory()  # type: ignore
    """
    MEMory

    Arguments:
    """

    class MEmory(SCPINode):
        """
        MEmory

        Arguments:
        """
        __slots__ = ()
        _cmd = "MEmory"
        args = []  # type: List[str]

        class Fast(SCPINode, SCPISet):
            """
            MEmory:Fast

            Arguments:
            """
            __slots__ = ()
            _cmd = "Fast"
            args = []  # type: List[str]

            class STArt(SCPINode, SCPIQuery, SCPISet):
                """
                MEmory:Fast:STArt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STArt"
                args = ["1"]

            STArt = STArt()  # type: ignore
            """
            MEmory:Fast:STArt

            Arguments: 1
            """

            class STOp(SCPINode, SCPIQuery, SCPISet):
                """
                MEmory:Fast:STOp

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STOp"
                args = ["1"]

            STOp = STOp()  # type: ignore
            """
            MEmory:Fast:STOp

            Arguments: 1
            """

        Fast = Fast()  # type: ignore
        """
        MEmory:Fast

        Arguments:
        """

        class STArt(SCPINode, SCPIQuery, SCPISet):
            """
            MEmory:STArt

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "STArt"
            args = ["1"]

        STArt = STArt()  # type: ignore
        """
        MEmory:STArt

        Arguments: 1
        """

        class STOp(SCPINode, SCPIQuery, SCPISet):
            """
            MEmory:STOp

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "STOp"
            args = ["1"]

        STOp = STOp()  # type: ignore
        """
        MEmory:STOp

        Arguments: 1
        """

    MEmory = MEmory()  # type: ignore
    """
    MEmory

    Arguments:
    """

    class MMEMory(SCPINode):
        """
        MMEMory

        Arguments:
        """
        __slots__ = ()
        _cmd = "MMEMory"
        args = []  # type: List[str]

        class ALIases(SCPINode, SCPIQuery):
            """
            MMEMory:ALIases

            Arguments:
            """
            __slots__ = ()
            _cmd = "ALIases"
            args = []  # type: List[str]

        ALIases = ALIases()  # type: ignore
        """
        MMEMory:ALIases

        Arguments:
        """

        class ATTRibute(SCPINode, SCPIQuery, SCPISet):
            """
            MMEMory:ATTRibute

            Arguments: <string>,<string>
            """
            __slots__ = ()
            _cmd = "ATTRibute"
            args = ["<string>,<string>"]

        ATTRibute = ATTRibute()  # type: ignore
        """
        MMEMory:ATTRibute

        Arguments: <string>,<string>
        """

        class CATalog(SCPINode, SCPIQuery):
            """
            `MMEMory:CATalog
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/81fb5b7cd1124455.htm#ID_d86b0432900f3f010a00206a015692f4-808cf704900f3f010a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "CATalog"
            args = ["'string'"]

            class LENGth(SCPINode, SCPIQuery):
                """
                `MMEMory:CATalog:LENGth
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f52dbc720a0a48f9.htm#ID_de3b183c900f4f0f0a00206a0011b22f-adb17661900f4f0f0a00206a01eae7a4-en-US>`_

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "LENGth"
                args = ["'string'"]

            LENGth = LENGth()  # type: ignore
            """
            `MMEMory:CATalog:LENGth
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f52dbc720a0a48f9.htm#ID_de3b183c900f4f0f0a00206a0011b22f-adb17661900f4f0f0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """

        CATalog = CATalog()  # type: ignore
        """
        `MMEMory:CATalog
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/81fb5b7cd1124455.htm#ID_d86b0432900f3f010a00206a015692f4-808cf704900f3f010a00206a01eae7a4-en-US>`_

        Arguments: 'string'
        """

        class CDIRectory(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:CDIRectory
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/884f6bb587664b1f.htm#ID_1b7d70d1900f44510a00206a01aa7e4f-154c448f900f44510a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "CDIRectory"
            args = ["'string'"]

        CDIRectory = CDIRectory()  # type: ignore
        """
        `MMEMory:CDIRectory
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/884f6bb587664b1f.htm#ID_1b7d70d1900f44510a00206a01aa7e4f-154c448f900f44510a00206a01eae7a4-en-US>`_

        Arguments: 'string'
        """

        class DCATalog(SCPINode, SCPIQuery):
            """
            `MMEMory:DCATalog
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/9143817b0b724e69.htm#ID_a8aa6937900ef1cc0a00206a010ba9d5-cf37708c900ef1cc0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "DCATalog"
            args = ["'string'"]

            class LENGth(SCPINode, SCPIQuery):
                """
                `MMEMory:DCATalog:LENGth
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a083db692d2a43f1.htm#ID_4e070651900ef70b0a00206a016f7a85-a0f33d76900ef70b0a00206a01eae7a4-en-US>`_

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "LENGth"
                args = ["'string'"]

            LENGth = LENGth()  # type: ignore
            """
            `MMEMory:DCATalog:LENGth
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a083db692d2a43f1.htm#ID_4e070651900ef70b0a00206a016f7a85-a0f33d76900ef70b0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """

        DCATalog = DCATalog()  # type: ignore
        """
        `MMEMory:DCATalog
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/9143817b0b724e69.htm#ID_a8aa6937900ef1cc0a00206a010ba9d5-cf37708c900ef1cc0a00206a01eae7a4-en-US>`_

        Arguments: 'string'
        """

        class DELete(SCPINode, SCPISet):
            """
            `MMEMory:DELete
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/04c3a6e184634827.htm#ID_48ccd5f3900eec4d0a00206a007d4e66-412debbb900eec4d0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "DELete"
            args = ["'string'"]

            class NVWFm(SCPINode, SCPISet):
                """
                MMEMory:DELete:NVWFm

                Arguments:
                """
                __slots__ = ()
                _cmd = "NVWFm"
                args = []  # type: List[str]

            NVWFm = NVWFm()  # type: ignore
            """
            MMEMory:DELete:NVWFm

            Arguments:
            """

            class WFM(SCPINodeN, SCPISet):
                """
                MMEMory:DELete:WFM

                Arguments:
                """
                __slots__ = ()
                _cmd = "WFM"
                args = []  # type: List[str]

            WFM = WFM()  # type: ignore
            """
            MMEMory:DELete:WFM

            Arguments:
            """

        DELete = DELete()  # type: ignore
        """
        `MMEMory:DELete
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/04c3a6e184634827.htm#ID_48ccd5f3900eec4d0a00206a007d4e66-412debbb900eec4d0a00206a01eae7a4-en-US>`_

        Arguments: 'string'
        """

        class DRIVes(SCPINode, SCPIQuery):
            """
            MMEMory:DRIVes

            Arguments:
            """
            __slots__ = ()
            _cmd = "DRIVes"
            args = []  # type: List[str]

        DRIVes = DRIVes()  # type: ignore
        """
        MMEMory:DRIVes

        Arguments:
        """

        class HEADer(SCPINode, SCPISet):
            """
            MMEMory:HEADer

            Arguments:
            """
            __slots__ = ()
            _cmd = "HEADer"
            args = []  # type: List[str]

            class CLEar(SCPINode, SCPISet):
                """
                MMEMory:HEADer:CLEar

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "CLEar"
                args = ["'string'"]

            CLEar = CLEar()  # type: ignore
            """
            MMEMory:HEADer:CLEar

            Arguments: 'string'
            """

            class DESCription(SCPINode, SCPISet):
                """
                MMEMory:HEADer:DESCription

                Arguments: <string>,<string>
                """
                __slots__ = ()
                _cmd = "DESCription"
                args = ["<string>,<string>"]

            DESCription = DESCription()  # type: ignore
            """
            MMEMory:HEADer:DESCription

            Arguments: <string>,<string>
            """

        HEADer = HEADer()  # type: ignore
        """
        MMEMory:HEADer

        Arguments:
        """

        class LOAD(SCPINode):
            """
            MMEMory:LOAD

            Arguments:
            """
            __slots__ = ()
            _cmd = "LOAD"
            args = []  # type: List[str]

            class MACRo(SCPINode, SCPISet):
                """
                MMEMory:LOAD:MACRo

                Arguments: <string>,<string>,<string>
                """
                __slots__ = ()
                _cmd = "MACRo"
                args = ["<string>,<string>,<string>"]

            MACRo = MACRo()  # type: ignore
            """
            MMEMory:LOAD:MACRo

            Arguments: <string>,<string>,<string>
            """

            class STATe(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/9de91cebcfaf4dfb.htm#ID_e4b148b6b16d7e450a00206a00d7d85c-f2c489ebb16d7e450a00206a002cfbf4-en-US>`_

                Arguments: <numeric_value>,<string>,<string>
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["<numeric_value>,<string>,<string>"]

            STATe = STATe()  # type: ignore
            """
            `MMEMory:LOAD:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/9de91cebcfaf4dfb.htm#ID_e4b148b6b16d7e450a00206a00d7d85c-f2c489ebb16d7e450a00206a002cfbf4-en-US>`_

            Arguments: <numeric_value>,<string>,<string>
            """

        LOAD = LOAD()  # type: ignore
        """
        MMEMory:LOAD

        Arguments:
        """

        class MDIRectory(SCPINode, SCPISet):
            """
            `MMEMory:MDIRectory
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/78d90e9c1a164918.htm#ID_28e36f85900ad56d0a00206a01580c40-8ea01a92900ad56d0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "MDIRectory"
            args = ["'string'"]

        MDIRectory = MDIRectory()  # type: ignore
        """
        `MMEMory:MDIRectory
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/78d90e9c1a164918.htm#ID_28e36f85900ad56d0a00206a01580c40-8ea01a92900ad56d0a00206a01eae7a4-en-US>`_

        Arguments: 'string'
        """

        class RDIRectory(SCPINode, SCPISet):
            """
            `MMEMory:RDIRectory
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0605b8a725804d3f.htm#ID_845b819f9007a0b00a00206a00db9c2f-f178d5259007a0b00a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "RDIRectory"
            args = ["'string'"]

        RDIRectory = RDIRectory()  # type: ignore
        """
        `MMEMory:RDIRectory
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0605b8a725804d3f.htm#ID_845b819f9007a0b00a00206a00db9c2f-f178d5259007a0b00a00206a01eae7a4-en-US>`_

        Arguments: 'string'
        """

        class STORe(SCPINode, SCPISet):
            """
            MMEMory:STORe

            Arguments:
            """
            __slots__ = ()
            _cmd = "STORe"
            args = []  # type: List[str]

            class MACRo(SCPINode, SCPISet):
                """
                MMEMory:STORe:MACRo

                Arguments: <string>,<string>,<string>
                """
                __slots__ = ()
                _cmd = "MACRo"
                args = ["<string>,<string>,<string>"]

            MACRo = MACRo()  # type: ignore
            """
            MMEMory:STORe:MACRo

            Arguments: <string>,<string>,<string>
            """

            class STATe(SCPINode, SCPISet):
                """
                `MMEMory:STORe:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a5614cb446644ab0.htm#ID_45c41292b170604d0a00206a0129c63d-053ce38db170604d0a00206a01567e4b-en-US>`_

                Arguments: <integer>,<string>,<string>
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["<integer>,<string>,<string>"]

            STATe = STATe()  # type: ignore
            """
            `MMEMory:STORe:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a5614cb446644ab0.htm#ID_45c41292b170604d0a00206a0129c63d-053ce38db170604d0a00206a01567e4b-en-US>`_

            Arguments: <integer>,<string>,<string>
            """

        STORe = STORe()  # type: ignore
        """
        MMEMory:STORe

        Arguments:
        """

    MMEMory = MMEMory()  # type: ignore
    """
    MMEMory

    Arguments:
    """

    class MODulation(SCPINode):
        """
        MODulation

        Arguments:
        """
        __slots__ = ()
        _cmd = "MODulation"
        args = []  # type: List[str]

        class STATe(SCPINode, SCPIBool):
            """
            MODulation:STATe

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()  # type: ignore
        """
        MODulation:STATe

        Arguments: 1, ON, OFF
        """

    MODulation = MODulation()  # type: ignore
    """
    MODulation

    Arguments:
    """

    class MOdulation(SCPINode, SCPIQuery):
        """
        MOdulation

        Arguments:
        """
        __slots__ = ()
        _cmd = "MOdulation"
        args = []  # type: List[str]

        class Normal(SCPINode, SCPISet):
            """
            MOdulation:Normal

            Arguments:
            """
            __slots__ = ()
            _cmd = "Normal"
            args = []  # type: List[str]

        Normal = Normal()  # type: ignore
        """
        MOdulation:Normal

        Arguments:
        """

        class Reduced(SCPINode, SCPISet):
            """
            MOdulation:Reduced

            Arguments:
            """
            __slots__ = ()
            _cmd = "Reduced"
            args = []  # type: List[str]

        Reduced = Reduced()  # type: ignore
        """
        MOdulation:Reduced

        Arguments:
        """

    MOdulation = MOdulation()  # type: ignore
    """
    MOdulation

    Arguments:
    """

    class MPRot(SCPINode, SCPIQuery):
        """
        MPRot

        Arguments:
        """
        __slots__ = ()
        _cmd = "MPRot"
        args = []  # type: List[str]

        class STARt(SCPINode, SCPISet):
            """
            MPRot:STARt

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "STARt"
            args = ["1"]

        STARt = STARt()  # type: ignore
        """
        MPRot:STARt

        Arguments: 1
        """

    MPRot = MPRot()  # type: ignore
    """
    MPRot

    Arguments:
    """

    class MTRig(SCPINode, SCPIQuery):
        """
        MTRig

        Arguments:
        """
        __slots__ = ()
        _cmd = "MTRig"
        args = []  # type: List[str]

    MTRig = MTRig()  # type: ignore
    """
    MTRig

    Arguments:
    """

    class OUTPut(SCPINode, SCPIQuery, SCPISet):
        """
        OUTPut

        Arguments:
        """
        __slots__ = ()
        _cmd = "OUTPut"
        args = []  # type: List[str]

        class AFIXed(SCPINode):
            """
            OUTPut:AFIXed

            Arguments:
            """
            __slots__ = ()
            _cmd = "AFIXed"
            args = []  # type: List[str]

            class RANGe(SCPINode):
                """
                OUTPut:AFIXed:RANGe

                Arguments:
                """
                __slots__ = ()
                _cmd = "RANGe"
                args = []  # type: List[str]

                class LOWer(SCPINode, SCPIQuery):
                    """
                    `OUTPut:AFIXed:RANGe:LOWer
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/357ac8f3e4244a47.htm#ID_e38f0e814e64057e0a00206a0013b470-127480ee4e64057e0a00206a0024546d-en-US>`_

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "LOWer"
                    args = []  # type: List[str]

                LOWer = LOWer()  # type: ignore
                """
                `OUTPut:AFIXed:RANGe:LOWer
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/357ac8f3e4244a47.htm#ID_e38f0e814e64057e0a00206a0013b470-127480ee4e64057e0a00206a0024546d-en-US>`_

                Arguments:
                """

                class UPPer(SCPINode, SCPIQuery):
                    """
                    `OUTPut:AFIXed:RANGe:UPPer
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/41e4a70f35a54cde.htm#ID_a55c89064e640b1d0a00206a01925c56-3ee9d9c74e640b1d0a00206a0024546d-en-US>`_

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "UPPer"
                    args = []  # type: List[str]

                UPPer = UPPer()  # type: ignore
                """
                `OUTPut:AFIXed:RANGe:UPPer
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/41e4a70f35a54cde.htm#ID_a55c89064e640b1d0a00206a01925c56-3ee9d9c74e640b1d0a00206a0024546d-en-US>`_

                Arguments:
                """

            RANGe = RANGe()  # type: ignore
            """
            OUTPut:AFIXed:RANGe

            Arguments:
            """

        AFIXed = AFIXed()  # type: ignore
        """
        OUTPut:AFIXed

        Arguments:
        """

        class AMODe(SCPINode, SCPIQuery, SCPISet):
            """
            `OUTPut:AMODe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a7cb436862264377.htm#ID_4c9f7d824e63ffff0a00206a00be3d6b-f716d1094e63ffff0a00206a0024546d-en-US>`_

            Arguments: AUTO, FIXed
            """
            __slots__ = ()
            _cmd = "AMODe"
            args = ["AUTO", "FIXed"]

        AMODe = AMODe()  # type: ignore
        """
        `OUTPut:AMODe
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a7cb436862264377.htm#ID_4c9f7d824e63ffff0a00206a00be3d6b-f716d1094e63ffff0a00206a0024546d-en-US>`_

        Arguments: AUTO, FIXed
        """

        class ATTenuation(SCPINode, SCPIQuery, SCPISet):
            """
            OUTPut:ATTenuation

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "ATTenuation"
            args = ["1"]

        ATTenuation = ATTenuation()  # type: ignore
        """
        OUTPut:ATTenuation

        Arguments: 1
        """

        class BLANk(SCPINode):
            """
            OUTPut:BLANk

            Arguments:
            """
            __slots__ = ()
            _cmd = "BLANk"
            args = []  # type: List[str]

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                OUTPut:BLANk:POLarity

                Arguments: INVerted, NORMal
                """
                __slots__ = ()
                _cmd = "POLarity"
                args = ["INVerted", "NORMal"]

            POLarity = POLarity()  # type: ignore
            """
            OUTPut:BLANk:POLarity

            Arguments: INVerted, NORMal
            """

        BLANk = BLANk()  # type: ignore
        """
        OUTPut:BLANk

        Arguments:
        """

        class BLANking(SCPINode):
            """
            OUTPut:BLANking

            Arguments:
            """
            __slots__ = ()
            _cmd = "BLANking"
            args = []  # type: List[str]

            class STATe(SCPINode, SCPIBool):
                """
                OUTPut:BLANking:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            OUTPut:BLANking:STATe

            Arguments: 1, ON, OFF
            """

        BLANking = BLANking()  # type: ignore
        """
        OUTPut:BLANking

        Arguments:
        """

        class DISable(SCPINode, SCPISet):
            """
            OUTPut:DISable

            Arguments:
            """
            __slots__ = ()
            _cmd = "DISable"
            args = []  # type: List[str]

        DISable = DISable()  # type: ignore
        """
        OUTPut:DISable

        Arguments:
        """

        class ENABle(SCPINode, SCPISet):
            """
            OUTPut:ENABle

            Arguments:
            """
            __slots__ = ()
            _cmd = "ENABle"
            args = []  # type: List[str]

        ENABle = ENABle()  # type: ignore
        """
        OUTPut:ENABle

        Arguments:
        """

        class IMPedance(SCPINode, SCPIQuery):
            """
            `OUTPut:IMPedance
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a47f0290b4ca4b68.htm#ID_8baa6a394e641baa0a00206a00f78a8f-2e642ae14e641baa0a00206a0024546d-en-US>`_

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "IMPedance"
            args = ["1"]

        IMPedance = IMPedance()  # type: ignore
        """
        `OUTPut:IMPedance
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a47f0290b4ca4b68.htm#ID_8baa6a394e641baa0a00206a00f78a8f-2e642ae14e641baa0a00206a0024546d-en-US>`_

        Arguments: 1
        """

        class LIBLanking(SCPINode, SCPIQuery, SCPISet):
            """
            OUTPut:LIBLanking

            Arguments: NORMal, OFF
            """
            __slots__ = ()
            _cmd = "LIBLanking"
            args = ["NORMal", "OFF"]

        LIBLanking = LIBLanking()  # type: ignore
        """
        OUTPut:LIBLanking

        Arguments: NORMal, OFF
        """

        class MODulation(SCPINode):
            """
            OUTPut:MODulation

            Arguments:
            """
            __slots__ = ()
            _cmd = "MODulation"
            args = []  # type: List[str]

            class STATe(SCPINode, SCPIBool):
                """
                OUTPut:MODulation:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            OUTPut:MODulation:STATe

            Arguments: 1, ON, OFF
            """

        MODulation = MODulation()  # type: ignore
        """
        OUTPut:MODulation

        Arguments:
        """

        class POLarity(SCPINode):
            """
            OUTPut:POLarity

            Arguments:
            """
            __slots__ = ()
            _cmd = "POLarity"
            args = []  # type: List[str]

            class PULSe(SCPINode, SCPIQuery, SCPISet):
                """
                OUTPut:POLarity:PULSe

                Arguments: INVerted, NORMal
                """
                __slots__ = ()
                _cmd = "PULSe"
                args = ["INVerted", "NORMal"]

            PULSe = PULSe()  # type: ignore
            """
            OUTPut:POLarity:PULSe

            Arguments: INVerted, NORMal
            """

        POLarity = POLarity()  # type: ignore
        """
        OUTPut:POLarity

        Arguments:
        """

        class PROTection(SCPINode, SCPIBool):
            """
            OUTPut:PROTection

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "PROTection"
            args = ["1", "ON", "OFF"]

            class CLEar(SCPINode, SCPISet):
                """
                `OUTPut:PROTection:CLEar
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/312a93269b474916.htm#ID_ff19e8ab4e64109c0a00206a01e0ace3-ddc4d9a54e64109c0a00206a0024546d-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "CLEar"
                args = []  # type: List[str]

            CLEar = CLEar()  # type: ignore
            """
            `OUTPut:PROTection:CLEar
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/312a93269b474916.htm#ID_ff19e8ab4e64109c0a00206a01e0ace3-ddc4d9a54e64109c0a00206a0024546d-en-US>`_

            Arguments:
            """

            class RETRace(SCPINode, SCPIBool):
                """
                OUTPut:PROTection:RETRace

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "RETRace"
                args = ["1", "ON", "OFF"]

            RETRace = RETRace()  # type: ignore
            """
            OUTPut:PROTection:RETRace

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                OUTPut:PROTection:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            OUTPut:PROTection:STATe

            Arguments: 1, ON, OFF
            """

            class TRIPped(SCPINode, SCPIQuery):
                """
                `OUTPut:PROTection:TRIPped
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/8c639762430041c7.htm#ID_37db314d4e64161b0a00206a005d0255-2d47945b4e64161b0a00206a0024546d-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "TRIPped"
                args = []  # type: List[str]

            TRIPped = TRIPped()  # type: ignore
            """
            `OUTPut:PROTection:TRIPped
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/8c639762430041c7.htm#ID_37db314d4e64161b0a00206a005d0255-2d47945b4e64161b0a00206a0024546d-en-US>`_

            Arguments:
            """

        PROTection = PROTection()  # type: ignore
        """
        OUTPut:PROTection

        Arguments: 1, ON, OFF
        """

        class RFBLanking(SCPINode, SCPIQuery, SCPISet):
            """
            OUTPut:RFBLanking

            Arguments: <boolean>, AUTO
            """
            __slots__ = ()
            _cmd = "RFBLanking"
            args = ["<boolean>", "AUTO"]

        RFBLanking = RFBLanking()  # type: ignore
        """
        OUTPut:RFBLanking

        Arguments: <boolean>, AUTO
        """

        class SCALe(SCPINode, SCPIQuery, SCPISet):
            """
            OUTPut:SCALe

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "SCALe"
            args = ["1"]

        SCALe = SCALe()  # type: ignore
        """
        OUTPut:SCALe

        Arguments: 1
        """

        class SOURce(SCPINode, SCPIQuery, SCPISet):
            """
            OUTPut:SOURce

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "SOURce"
            args = ["1"]

            class STEReo(SCPINode, SCPIQuery, SCPISet):
                """
                OUTPut:SOURce:STEReo

                Arguments: MPX, PILot
                """
                __slots__ = ()
                _cmd = "STEReo"
                args = ["MPX", "PILot"]

            STEReo = STEReo()  # type: ignore
            """
            OUTPut:SOURce:STEReo

            Arguments: MPX, PILot
            """

        SOURce = SOURce()  # type: ignore
        """
        OUTPut:SOURce

        Arguments: 1
        """

        class STANdby(SCPINode):
            """
            OUTPut:STANdby

            Arguments:
            """
            __slots__ = ()
            _cmd = "STANdby"
            args = []  # type: List[str]

            class STATe(SCPINode, SCPIBool):
                """
                OUTPut:STANdby:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            OUTPut:STANdby:STATe

            Arguments: 1, ON, OFF
            """

        STANdby = STANdby()  # type: ignore
        """
        OUTPut:STANdby

        Arguments:
        """

        class STATe(SCPINode, SCPIBool):
            """
            `OUTPut:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/d68157f6ecaf46b2.htm#ID_2943fc164e63f4f10a00206a00231222-a9036df24e63f4f10a00206a0024546d-en-US>`_

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

            class BACKup(SCPINode, SCPIBool):
                """
                OUTPut:STATe:BACKup

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "BACKup"
                args = ["1", "ON", "OFF"]

            BACKup = BACKup()  # type: ignore
            """
            OUTPut:STATe:BACKup

            Arguments: 1, ON, OFF
            """

        STATe = STATe()  # type: ignore
        """
        `OUTPut:STATe
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/d68157f6ecaf46b2.htm#ID_2943fc164e63f4f10a00206a00231222-a9036df24e63f4f10a00206a0024546d-en-US>`_

        Arguments: 1, ON, OFF
        """

        class VOLTage(SCPINode, SCPIQuery, SCPISet):
            """
            OUTPut:VOLTage

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "VOLTage"
            args = ["1"]

        VOLTage = VOLTage()  # type: ignore
        """
        OUTPut:VOLTage

        Arguments: 1
        """

    OUTPut = OUTPut()  # type: ignore
    """
    OUTPut

    Arguments:
    """

    class PHASe(SCPINode):
        """
        PHASe

        Arguments:
        """
        __slots__ = ()
        _cmd = "PHASe"
        args = []  # type: List[str]

        class ADJust(SCPINode, SCPIQuery, SCPISet):
            """
            PHASe:ADJust

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "ADJust"
            args = ["1"]

            class STEP(SCPINode):
                """
                PHASe:ADJust:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    PHASe:ADJust:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                PHASe:ADJust:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            PHASe:ADJust:STEP

            Arguments:
            """

        ADJust = ADJust()  # type: ignore
        """
        PHASe:ADJust

        Arguments: 1
        """

        class REFerence(SCPINode, SCPISet):
            """
            PHASe:REFerence

            Arguments:
            """
            __slots__ = ()
            _cmd = "REFerence"
            args = []  # type: List[str]

        REFerence = REFerence()  # type: ignore
        """
        PHASe:REFerence

        Arguments:
        """

    PHASe = PHASe()  # type: ignore
    """
    PHASe

    Arguments:
    """

    class PHAse(SCPINode, SCPIQuery, SCPISet):
        """
        PHAse

        Arguments: 1
        """
        __slots__ = ()
        _cmd = "PHAse"
        args = ["1"]

        class Internal(SCPINode, SCPISet):
            """
            PHAse:Internal

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "Internal"
            args = ["1"]

        Internal = Internal()  # type: ignore
        """
        PHAse:Internal

        Arguments: 1
        """

        class Var_step(SCPINode, SCPIQuery, SCPISet):
            """
            PHAse:Var_step

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "Var_step"
            args = ["1"]

        Var_step = Var_step()  # type: ignore
        """
        PHAse:Var_step

        Arguments: 1
        """

    PHAse = PHAse()  # type: ignore
    """
    PHAse

    Arguments: 1
    """

    class PMETer(SCPINode):
        """
        PMETer

        Arguments:
        """
        __slots__ = ()
        _cmd = "PMETer"
        args = []  # type: List[str]

        class POWer(SCPINode, SCPIQuery):
            """
            PMETer:POWer

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "POWer"
            args = ["1"]

        POWer = POWer()  # type: ignore
        """
        PMETer:POWer

        Arguments: 1
        """

    PMETer = PMETer()  # type: ignore
    """
    PMETer

    Arguments:
    """

    class POWer(SCPINode):
        """
        POWer

        Arguments:
        """
        __slots__ = ()
        _cmd = "POWer"
        args = []  # type: List[str]

        class OUT(SCPINode):
            """
            POWer:OUT

            Arguments:
            """
            __slots__ = ()
            _cmd = "OUT"
            args = []  # type: List[str]

            class ALC(SCPINode):
                """
                POWer:OUT:ALC

                Arguments:
                """
                __slots__ = ()
                _cmd = "ALC"
                args = []  # type: List[str]

                class BANDwidth(SCPINode, SCPISet):
                    """
                    POWer:OUT:ALC:BANDwidth

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "BANDwidth"
                    args = []  # type: List[str]

                BANDwidth = BANDwidth()  # type: ignore
                """
                POWer:OUT:ALC:BANDwidth

                Arguments:
                """

            ALC = ALC()  # type: ignore
            """
            POWer:OUT:ALC

            Arguments:
            """

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:OUT:ATTenuation

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ATTenuation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    POWer:OUT:ATTenuation:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        POWer:OUT:ATTenuation:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    POWer:OUT:ATTenuation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                POWer:OUT:ATTenuation:STEP

                Arguments:
                """

            ATTenuation = ATTenuation()  # type: ignore
            """
            POWer:OUT:ATTenuation

            Arguments: 1
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:OUT:LEVel

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "LEVel"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    POWer:OUT:LEVel:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        POWer:OUT:LEVel:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    POWer:OUT:LEVel:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                POWer:OUT:LEVel:STEP

                Arguments:
                """

            LEVel = LEVel()  # type: ignore
            """
            POWer:OUT:LEVel

            Arguments: 1
            """

            class MUTing(SCPINode, SCPIBool):
                """
                POWer:OUT:MUTing

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "MUTing"
                args = ["1", "ON", "OFF"]

            MUTing = MUTing()  # type: ignore
            """
            POWer:OUT:MUTing

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                POWer:OUT:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            POWer:OUT:STATe

            Arguments: 1, ON, OFF
            """

            class ULIMit(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:OUT:ULIMit

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ULIMit"
                args = ["1"]

            ULIMit = ULIMit()  # type: ignore
            """
            POWer:OUT:ULIMit

            Arguments: 1
            """

        OUT = OUT()  # type: ignore
        """
        POWer:OUT

        Arguments:
        """

        class SOURce(SCPINode):
            """
            POWer:SOURce

            Arguments:
            """
            __slots__ = ()
            _cmd = "SOURce"
            args = []  # type: List[str]

            class ALC(SCPINode):
                """
                POWer:SOURce:ALC

                Arguments:
                """
                __slots__ = ()
                _cmd = "ALC"
                args = []  # type: List[str]

                class BANDwidth(SCPINode, SCPISet):
                    """
                    POWer:SOURce:ALC:BANDwidth

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "BANDwidth"
                    args = []  # type: List[str]

                BANDwidth = BANDwidth()  # type: ignore
                """
                POWer:SOURce:ALC:BANDwidth

                Arguments:
                """

            ALC = ALC()  # type: ignore
            """
            POWer:SOURce:ALC

            Arguments:
            """

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:SOURce:ATTenuation

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ATTenuation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    POWer:SOURce:ATTenuation:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        POWer:SOURce:ATTenuation:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    POWer:SOURce:ATTenuation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                POWer:SOURce:ATTenuation:STEP

                Arguments:
                """

            ATTenuation = ATTenuation()  # type: ignore
            """
            POWer:SOURce:ATTenuation

            Arguments: 1
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:SOURce:LEVel

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "LEVel"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    POWer:SOURce:LEVel:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        POWer:SOURce:LEVel:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    POWer:SOURce:LEVel:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                POWer:SOURce:LEVel:STEP

                Arguments:
                """

            LEVel = LEVel()  # type: ignore
            """
            POWer:SOURce:LEVel

            Arguments: 1
            """

            class MUTing(SCPINode, SCPIBool):
                """
                POWer:SOURce:MUTing

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "MUTing"
                args = ["1", "ON", "OFF"]

            MUTing = MUTing()  # type: ignore
            """
            POWer:SOURce:MUTing

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                POWer:SOURce:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            POWer:SOURce:STATe

            Arguments: 1, ON, OFF
            """

            class ULIMit(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:SOURce:ULIMit

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ULIMit"
                args = ["1"]

            ULIMit = ULIMit()  # type: ignore
            """
            POWer:SOURce:ULIMit

            Arguments: 1
            """

        SOURce = SOURce()  # type: ignore
        """
        POWer:SOURce

        Arguments:
        """

    POWer = POWer()  # type: ignore
    """
    POWer

    Arguments:
    """

    class POWup(SCPINode, SCPIQuery):
        """
        POWup

        Arguments:
        """
        __slots__ = ()
        _cmd = "POWup"
        args = []  # type: List[str]

    POWup = POWup()  # type: ignore
    """
    POWup

    Arguments:
    """

    class PReset(SCPINode, SCPISet):
        """
        PReset

        Arguments:
        """
        __slots__ = ()
        _cmd = "PReset"
        args = []  # type: List[str]

    PReset = PReset()  # type: ignore
    """
    PReset

    Arguments:
    """

    class PULSe(SCPINode, SCPIQuery):
        """
        PULSe

        Arguments:
        """
        __slots__ = ()
        _cmd = "PULSe"
        args = []  # type: List[str]

        class CAL(SCPINode):
            """
            PULSe:CAL

            Arguments:
            """
            __slots__ = ()
            _cmd = "CAL"
            args = []  # type: List[str]

            class DISable(SCPINode, SCPISet):
                """
                PULSe:CAL:DISable

                Arguments:
                """
                __slots__ = ()
                _cmd = "DISable"
                args = []  # type: List[str]

            DISable = DISable()  # type: ignore
            """
            PULSe:CAL:DISable

            Arguments:
            """

            class ENABle(SCPINode, SCPISet):
                """
                PULSe:CAL:ENABle

                Arguments:
                """
                __slots__ = ()
                _cmd = "ENABle"
                args = []  # type: List[str]

            ENABle = ENABle()  # type: ignore
            """
            PULSe:CAL:ENABle

            Arguments:
            """

        CAL = CAL()  # type: ignore
        """
        PULSe:CAL

        Arguments:
        """

        class CONDitioning(SCPINode, SCPIBool):
            """
            PULSe:CONDitioning

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "CONDitioning"
            args = ["1", "ON", "OFF"]

        CONDitioning = CONDitioning()  # type: ignore
        """
        PULSe:CONDitioning

        Arguments: 1, ON, OFF
        """

        class DELay(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:DELay

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "DELay"
            args = ["1"]

            class STEP(SCPINode):
                """
                PULSe:DELay:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    PULSe:DELay:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                PULSe:DELay:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            PULSe:DELay:STEP

            Arguments:
            """

        DELay = DELay()  # type: ignore
        """
        PULSe:DELay

        Arguments: 1
        """

        class FREQuency(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:FREQuency

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "FREQuency"
            args = ["1"]

            class STEP(SCPINode):
                """
                PULSe:FREQuency:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    PULSe:FREQuency:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                PULSe:FREQuency:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            PULSe:FREQuency:STEP

            Arguments:
            """

        FREQuency = FREQuency()  # type: ignore
        """
        PULSe:FREQuency

        Arguments: 1
        """

        class IMPedance(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:IMPedance

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "IMPedance"
            args = ["1"]

        IMPedance = IMPedance()  # type: ignore
        """
        PULSe:IMPedance

        Arguments: 1
        """

        class MODF(SCPINode):
            """
            PULSe:MODF

            Arguments:
            """
            __slots__ = ()
            _cmd = "MODF"
            args = []  # type: List[str]

            class VALue(SCPINode, SCPISet):
                """
                PULSe:MODF:VALue

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()  # type: ignore
            """
            PULSe:MODF:VALue

            Arguments: 1
            """

        MODF = MODF()  # type: ignore
        """
        PULSe:MODF

        Arguments:
        """

        class SLOPe(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:SLOPe

            Arguments: BOTH, NEGative, POSitive
            """
            __slots__ = ()
            _cmd = "SLOPe"
            args = ["BOTH", "NEGative", "POSitive"]

        SLOPe = SLOPe()  # type: ignore
        """
        PULSe:SLOPe

        Arguments: BOTH, NEGative, POSitive
        """

        class SOURce(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:SOURce

            Arguments: EXTernal, INTernal,EXTernal, INTernal
            """
            __slots__ = ()
            _cmd = "SOURce"
            args = ["EXTernal", "INTernal,EXTernal", "INTernal"]

        SOURce = SOURce()  # type: ignore
        """
        PULSe:SOURce

        Arguments: EXTernal, INTernal,EXTernal, INTernal
        """

        class STATe(SCPINode, SCPIBool):
            """
            PULSe:STATe

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()  # type: ignore
        """
        PULSe:STATe

        Arguments: 1, ON, OFF
        """

        class WIDTh(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:WIDTh

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "WIDTh"
            args = ["1"]

            class STEP(SCPINode):
                """
                PULSe:WIDTh:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    PULSe:WIDTh:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                PULSe:WIDTh:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            PULSe:WIDTh:STEP

            Arguments:
            """

        WIDTh = WIDTh()  # type: ignore
        """
        PULSe:WIDTh

        Arguments: 1
        """

    PULSe = PULSe()  # type: ignore
    """
    PULSe

    Arguments:
    """

    class PUlse(SCPINode, SCPIQuery, SCPISet):
        """
        PUlse

        Arguments:
        """
        __slots__ = ()
        _cmd = "PUlse"
        args = []  # type: List[str]

        class Inverted(SCPINode, SCPISet):
            """
            PUlse:Inverted

            Arguments:
            """
            __slots__ = ()
            _cmd = "Inverted"
            args = []  # type: List[str]

        Inverted = Inverted()  # type: ignore
        """
        PUlse:Inverted

        Arguments:
        """

        class Normal(SCPINode, SCPISet):
            """
            PUlse:Normal

            Arguments:
            """
            __slots__ = ()
            _cmd = "Normal"
            args = []  # type: List[str]

        Normal = Normal()  # type: ignore
        """
        PUlse:Normal

        Arguments:
        """

    PUlse = PUlse()  # type: ignore
    """
    PUlse

    Arguments:
    """

    class REFerence_oscil(SCPINode, SCPIQuery, SCPISet):
        """
        REFerence_oscil

        Arguments:
        """
        __slots__ = ()
        _cmd = "REFerence_oscil"
        args = []  # type: List[str]

        class CORrection(SCPINode, SCPISet):
            """
            REFerence_oscil:CORrection

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "CORrection"
            args = ["1"]

            class STOre(SCPINode, SCPISet):
                """
                REFerence_oscil:CORrection:STOre

                Arguments:
                """
                __slots__ = ()
                _cmd = "STOre"
                args = []  # type: List[str]

            STOre = STOre()  # type: ignore
            """
            REFerence_oscil:CORrection:STOre

            Arguments:
            """

        CORrection = CORrection()  # type: ignore
        """
        REFerence_oscil:CORrection

        Arguments: 1
        """

        class External(SCPINode, SCPISet):
            """
            REFerence_oscil:External

            Arguments:
            """
            __slots__ = ()
            _cmd = "External"
            args = []  # type: List[str]

        External = External()  # type: ignore
        """
        REFerence_oscil:External

        Arguments:
        """

        class High(SCPINode, SCPISet):
            """
            REFerence_oscil:High

            Arguments:
            """
            __slots__ = ()
            _cmd = "High"
            args = []  # type: List[str]

        High = High()  # type: ignore
        """
        REFerence_oscil:High

        Arguments:
        """

        class Internal(SCPINode, SCPISet):
            """
            REFerence_oscil:Internal

            Arguments:
            """
            __slots__ = ()
            _cmd = "Internal"
            args = []  # type: List[str]

        Internal = Internal()  # type: ignore
        """
        REFerence_oscil:Internal

        Arguments:
        """

        class Low(SCPINode, SCPISet):
            """
            REFerence_oscil:Low

            Arguments:
            """
            __slots__ = ()
            _cmd = "Low"
            args = []  # type: List[str]

        Low = Low()  # type: ignore
        """
        REFerence_oscil:Low

        Arguments:
        """

    REFerence_oscil = REFerence_oscil()  # type: ignore
    """
    REFerence_oscil

    Arguments:
    """

    class REcall(SCPINode, SCPISet):
        """
        REcall

        Arguments: 1
        """
        __slots__ = ()
        _cmd = "REcall"
        args = ["1"]

    REcall = REcall()  # type: ignore
    """
    REcall

    Arguments: 1
    """

    class ROSCillator(SCPINode, SCPISet):
        """
        ROSCillator

        Arguments:
        """
        __slots__ = ()
        _cmd = "ROSCillator"
        args = []  # type: List[str]

        class CALibration(SCPINode, SCPIQuery, SCPISet):
            """
            ROSCillator:CALibration

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "CALibration"
            args = ["1"]

            class STEP(SCPINode):
                """
                ROSCillator:CALibration:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery):
                    """
                    ROSCillator:CALibration:STEP:INCRement

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                ROSCillator:CALibration:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            ROSCillator:CALibration:STEP

            Arguments:
            """

        CALibration = CALibration()  # type: ignore
        """
        ROSCillator:CALibration

        Arguments: 1
        """

        class SOURce(SCPINode, SCPIQuery, SCPISet):
            """
            ROSCillator:SOURce

            Arguments: EXTernal, INTernal
            """
            __slots__ = ()
            _cmd = "SOURce"
            args = ["EXTernal", "INTernal"]

        SOURce = SOURce()  # type: ignore
        """
        ROSCillator:SOURce

        Arguments: EXTernal, INTernal
        """

    ROSCillator = ROSCillator()  # type: ignore
    """
    ROSCillator

    Arguments:
    """

    class SEQuence(SCPINode):
        """
        SEQuence

        Arguments:
        """
        __slots__ = ()
        _cmd = "SEQuence"
        args = []  # type: List[str]

        class IMMediate(SCPINode, SCPISet):
            """
            SEQuence:IMMediate

            Arguments:
            """
            __slots__ = ()
            _cmd = "IMMediate"
            args = []  # type: List[str]

        IMMediate = IMMediate()  # type: ignore
        """
        SEQuence:IMMediate

        Arguments:
        """

        class REGister(SCPINode, SCPIQuery, SCPISet):
            """
            SEQuence:REGister

            Arguments: <numeric_value>,<numeric_value>
            """
            __slots__ = ()
            _cmd = "REGister"
            args = ["<numeric_value>,<numeric_value>"]

        REGister = REGister()  # type: ignore
        """
        SEQuence:REGister

        Arguments: <numeric_value>,<numeric_value>
        """

        class STATe(SCPINode, SCPIBool):
            """
            SEQuence:STATe

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()  # type: ignore
        """
        SEQuence:STATe

        Arguments: 1, ON, OFF
        """

    SEQuence = SEQuence()  # type: ignore
    """
    SEQuence

    Arguments:
    """

    class SERVice(SCPINode, SCPISet):
        """
        SERVice

        Arguments:
        """
        __slots__ = ()
        _cmd = "SERVice"
        args = []  # type: List[str]

        class DIRect(SCPINode, SCPISet):
            """
            SERVice:DIRect

            Arguments:
            """
            __slots__ = ()
            _cmd = "DIRect"
            args = []  # type: List[str]

            class COMMand(SCPINode, SCPIQuery, SCPISet):
                """
                SERVice:DIRect:COMMand

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "COMMand"
                args = ["'string'"]

            COMMand = COMMand()  # type: ignore
            """
            SERVice:DIRect:COMMand

            Arguments: 'string'
            """

        DIRect = DIRect()  # type: ignore
        """
        SERVice:DIRect

        Arguments:
        """

        class HCOPy(SCPINode):
            """
            SERVice:HCOPy

            Arguments:
            """
            __slots__ = ()
            _cmd = "HCOPy"
            args = []  # type: List[str]

            class EXECute(SCPINode, SCPIQuery, SCPISet):
                """
                SERVice:HCOPy:EXECute

                Arguments:
                """
                __slots__ = ()
                _cmd = "EXECute"
                args = []  # type: List[str]

            EXECute = EXECute()  # type: ignore
            """
            SERVice:HCOPy:EXECute

            Arguments:
            """

            class IMAGe(SCPINode):
                """
                SERVice:HCOPy:IMAGe

                Arguments:
                """
                __slots__ = ()
                _cmd = "IMAGe"
                args = []  # type: List[str]

                class FORMat(SCPINode, SCPIQuery, SCPISet):
                    """
                    SERVice:HCOPy:IMAGe:FORMat

                    Arguments: BMP, JPG, PNG, XPM
                    """
                    __slots__ = ()
                    _cmd = "FORMat"
                    args = ["BMP", "JPG", "PNG", "XPM"]

                FORMat = FORMat()  # type: ignore
                """
                SERVice:HCOPy:IMAGe:FORMat

                Arguments: BMP, JPG, PNG, XPM
                """

            IMAGe = IMAGe()  # type: ignore
            """
            SERVice:HCOPy:IMAGe

            Arguments:
            """

        HCOPy = HCOPy()  # type: ignore
        """
        SERVice:HCOPy

        Arguments:
        """

        class SEQuence(SCPINode, SCPISet):
            """
            SERVice:SEQuence

            Arguments:
            """
            __slots__ = ()
            _cmd = "SEQuence"
            args = []  # type: List[str]

        SEQuence = SEQuence()  # type: ignore
        """
        SERVice:SEQuence

        Arguments:
        """

        class SPECial(SCPINode):
            """
            SERVice:SPECial

            Arguments:
            """
            __slots__ = ()
            _cmd = "SPECial"
            args = []  # type: List[str]

            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                SERVice:SPECial:FUNCtion

                Arguments: AA, AB, AM, AP, FA, FB, FM, FR, MF, ML, NONE, PL, PM, ST
                """
                __slots__ = ()
                _cmd = "FUNCtion"
                args = ["AA", "AB", "AM", "AP", "FA", "FB", "FM", "FR", "MF", "ML", "NONE", "PL", "PM", "ST"]

            FUNCtion = FUNCtion()  # type: ignore
            """
            SERVice:SPECial:FUNCtion

            Arguments: AA, AB, AM, AP, FA, FB, FM, FR, MF, ML, NONE, PL, PM, ST
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SERVice:SPECial:SOURce

                Arguments: NONE, S1, S2, S3
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["NONE", "S1", "S2", "S3"]

            SOURce = SOURce()  # type: ignore
            """
            SERVice:SPECial:SOURce

            Arguments: NONE, S1, S2, S3
            """

        SPECial = SPECial()  # type: ignore
        """
        SERVice:SPECial

        Arguments:
        """

        class TALKer(SCPINode, SCPISet):
            """
            SERVice:TALKer

            Arguments:
            """
            __slots__ = ()
            _cmd = "TALKer"
            args = []  # type: List[str]

        TALKer = TALKer()  # type: ignore
        """
        SERVice:TALKer

        Arguments:
        """

    SERVice = SERVice()  # type: ignore
    """
    SERVice

    Arguments:
    """

    class SEquence(SCPINode, SCPISet):
        """
        SEquence

        Arguments:
        """
        __slots__ = ()
        _cmd = "SEquence"
        args = []  # type: List[str]

    SEquence = SEquence()  # type: ignore
    """
    SEquence

    Arguments:
    """

    class SHA2(SCPINodeN, SCPISet):
        """
        SHA2

        Arguments:
        """
        __slots__ = ()
        _cmd = "SHA2"
        args = []  # type: List[str]

    SHA2 = SHA2()  # type: ignore
    """
    SHA2

    Arguments:
    """

    class SHS1(SCPINodeN, SCPISet):
        """
        SHS1

        Arguments:
        """
        __slots__ = ()
        _cmd = "SHS1"
        args = []  # type: List[str]

    SHS1 = SHS1()  # type: ignore
    """
    SHS1

    Arguments:
    """

    class SHT2(SCPINodeN, SCPISet):
        """
        SHT2

        Arguments:
        """
        __slots__ = ()
        _cmd = "SHT2"
        args = []  # type: List[str]

    SHT2 = SHT2()  # type: ignore
    """
    SHT2

    Arguments:
    """

    class SOURce(SCPINode, SCPISet):
        """
        SOURce

        Arguments:
        """
        __slots__ = ()
        _cmd = "SOURce"
        args = []  # type: List[str]

        class AM(SCPINode):
            """
            SOURce:AM

            Arguments:
            """
            __slots__ = ()
            _cmd = "AM"
            args = []  # type: List[str]

            class DEPTh(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:AM:DEPTh

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DEPTh"
                args = ["1"]

                class EXPonential(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:AM:DEPTh:EXPonential
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/39eff2936fd04783.htm#ID_856cf6c5fb4c2e620a00206a0128eeb6-0735468cfb4c20f50a00206a002979ad-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "EXPonential"
                    args = ["1"]

                EXPonential = EXPonential()  # type: ignore
                """
                `SOURce:AM:DEPTh:EXPonential
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/39eff2936fd04783.htm#ID_856cf6c5fb4c2e620a00206a0128eeb6-0735468cfb4c20f50a00206a002979ad-en-US>`_

                Arguments: 1
                """

                class LINear(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:AM:DEPTh:LINear
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/8067ab8f7396447a.htm#ID_7adfcbcefb4c1bd40a00206a001d9c20-808a5aebfb4c0cb10a00206a002979ad-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "LINear"
                    args = ["1"]

                    class TRACk(SCPINode, SCPIBool):
                        """
                        SOURce:AM:DEPTh:LINear:TRACk

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "TRACk"
                        args = ["1", "ON", "OFF"]

                    TRACk = TRACk()  # type: ignore
                    """
                    SOURce:AM:DEPTh:LINear:TRACk

                    Arguments: 1, ON, OFF
                    """

                LINear = LINear()  # type: ignore
                """
                `SOURce:AM:DEPTh:LINear
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/8067ab8f7396447a.htm#ID_7adfcbcefb4c1bd40a00206a001d9c20-808a5aebfb4c0cb10a00206a002979ad-en-US>`_

                Arguments: 1
                """

                class STEP(SCPINode):
                    """
                    SOURce:AM:DEPTh:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:AM:DEPTh:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:AM:DEPTh:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:AM:DEPTh:STEP

                Arguments:
                """

            DEPTh = DEPTh()  # type: ignore
            """
            SOURce:AM:DEPTh

            Arguments: 1
            """

            class EXTernal(SCPINode, SCPISet):
                """
                SOURce:AM:EXTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "EXTernal"
                args = []  # type: List[str]

                class COUPling(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:AM:EXTernal:COUPling
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7c57efbe68294ef5.htm#ID_5bcc30cf4d678f970a00206a00fe69d4-c60d3ff74d678f970a00206a0024546d-en-US>`_

                    Arguments: AC, DC
                    """
                    __slots__ = ()
                    _cmd = "COUPling"
                    args = ["AC", "DC"]

                COUPling = COUPling()  # type: ignore
                """
                `SOURce:AM:EXTernal:COUPling
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7c57efbe68294ef5.htm#ID_5bcc30cf4d678f970a00206a00fe69d4-c60d3ff74d678f970a00206a0024546d-en-US>`_

                Arguments: AC, DC
                """

                class IMPedance(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:AM:EXTernal:IMPedance

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()  # type: ignore
                """
                SOURce:AM:EXTernal:IMPedance

                Arguments: 1
                """

            EXTernal = EXTernal()  # type: ignore
            """
            SOURce:AM:EXTernal

            Arguments:
            """

            class INTernal(SCPINode, SCPISet):
                """
                SOURce:AM:INTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "INTernal"
                args = []  # type: List[str]

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:AM:INTernal:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                    class ALTernate(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:AM:INTernal:FREQuency:ALTernate

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "ALTernate"
                        args = ["1"]

                        class AMPLitude(SCPINode, SCPISet):
                            """
                            SOURce:AM:INTernal:FREQuency:ALTernate:AMPLitude

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "AMPLitude"
                            args = []  # type: List[str]

                            class PERCent(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:AM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "PERCent"
                                args = ["1"]

                            PERCent = PERCent()  # type: ignore
                            """
                            SOURce:AM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                            Arguments: 1
                            """

                        AMPLitude = AMPLitude()  # type: ignore
                        """
                        SOURce:AM:INTernal:FREQuency:ALTernate:AMPLitude

                        Arguments:
                        """

                    ALTernate = ALTernate()  # type: ignore
                    """
                    SOURce:AM:INTernal:FREQuency:ALTernate

                    Arguments: 1
                    """

                    class STEP(SCPINode):
                        """
                        SOURce:AM:INTernal:FREQuency:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:AM:INTernal:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:AM:INTernal:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:AM:INTernal:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:AM:INTernal:FREQuency

                Arguments: 1
                """

                class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:AM:INTernal:FUNCtion

                    Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                    """
                    __slots__ = ()
                    _cmd = "FUNCtion"
                    args = ["GAUSsian", "NOISe", "RAMP", "SINusoid", "SQUare", "TRIangle", "UNIForm"]

                    class NOISe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:AM:INTernal:FUNCtion:NOISe

                        Arguments: GAUSsian, UNIForm
                        """
                        __slots__ = ()
                        _cmd = "NOISe"
                        args = ["GAUSsian", "UNIForm"]

                    NOISe = NOISe()  # type: ignore
                    """
                    SOURce:AM:INTernal:FUNCtion:NOISe

                    Arguments: GAUSsian, UNIForm
                    """

                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:AM:INTernal:FUNCtion:SHAPe

                        Arguments: SINE, SQUare
                        """
                        __slots__ = ()
                        _cmd = "SHAPe"
                        args = ["SINE", "SQUare"]

                    SHAPe = SHAPe()  # type: ignore
                    """
                    SOURce:AM:INTernal:FUNCtion:SHAPe

                    Arguments: SINE, SQUare
                    """

                FUNCtion = FUNCtion()  # type: ignore
                """
                SOURce:AM:INTernal:FUNCtion

                Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                """

                class SWEep(SCPINode, SCPISet):
                    """
                    SOURce:AM:INTernal:SWEep

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SWEep"
                    args = []  # type: List[str]

                    class TRIGger(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:AM:INTernal:SWEep:TRIGger

                        Arguments: BUS, EXTernal, IMMediate, KEY
                        """
                        __slots__ = ()
                        _cmd = "TRIGger"
                        args = ["BUS", "EXTernal", "IMMediate", "KEY"]

                    TRIGger = TRIGger()  # type: ignore
                    """
                    SOURce:AM:INTernal:SWEep:TRIGger

                    Arguments: BUS, EXTernal, IMMediate, KEY
                    """

                SWEep = SWEep()  # type: ignore
                """
                SOURce:AM:INTernal:SWEep

                Arguments:
                """

            INTernal = INTernal()  # type: ignore
            """
            SOURce:AM:INTernal

            Arguments:
            """

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:AM:POLarity

                Arguments: INVerted, NORMal
                """
                __slots__ = ()
                _cmd = "POLarity"
                args = ["INVerted", "NORMal"]

            POLarity = POLarity()  # type: ignore
            """
            SOURce:AM:POLarity

            Arguments: INVerted, NORMal
            """

            class SCAN(SCPINode):
                """
                SOURce:AM:SCAN

                Arguments:
                """
                __slots__ = ()
                _cmd = "SCAN"
                args = []  # type: List[str]

                class SENSitivity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:AM:SCAN:SENSitivity

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "SENSitivity"
                    args = ["1"]

                SENSitivity = SENSitivity()  # type: ignore
                """
                SOURce:AM:SCAN:SENSitivity

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:AM:SCAN:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:AM:SCAN:STATe

                Arguments: 1, ON, OFF
                """

            SCAN = SCAN()  # type: ignore
            """
            SOURce:AM:SCAN

            Arguments:
            """

            class SENSitivity(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:AM:SENSitivity
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/6c5790605c444e81.htm#ID_49b9748f4d6795350a00206a01bcd5ca-0c8a2fb54d6795350a00206a0024546d-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "SENSitivity"
                args = ["1"]

            SENSitivity = SENSitivity()  # type: ignore
            """
            `SOURce:AM:SENSitivity
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/6c5790605c444e81.htm#ID_49b9748f4d6795350a00206a01bcd5ca-0c8a2fb54d6795350a00206a0024546d-en-US>`_

            Arguments: 1
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:AM:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/03d65f627a674214.htm#ID_e27ef81b4d679aa50a00206a007718e3-f6f38bbf4d679aa50a00206a0024546d-en-US>`_

                Arguments: EXTernal, INT1, INT2, INTernal, INTernal1, INTernal2,EXTernal, INT1, INTernal, INTernal1
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["EXTernal", "INT1", "INT2", "INTernal", "INTernal1", "INTernal2,EXTernal", "INT1", "INTernal", "INTernal1"]

            SOURce = SOURce()  # type: ignore
            """
            `SOURce:AM:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/03d65f627a674214.htm#ID_e27ef81b4d679aa50a00206a007718e3-f6f38bbf4d679aa50a00206a0024546d-en-US>`_

            Arguments: EXTernal, INT1, INT2, INTernal, INTernal1, INTernal2,EXTernal, INT1, INTernal, INTernal1
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SOURce:AM:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/03a638cb0e924f7c.htm#ID_26d49ccd4d679ff50a00206a0016778c-d761ca934d679ff50a00206a0024546d-en-US>`_

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

                class EMULation(SCPINode, SCPIBool):
                    """
                    SOURce:AM:STATe:EMULation

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "EMULation"
                    args = ["1", "ON", "OFF"]

                EMULation = EMULation()  # type: ignore
                """
                SOURce:AM:STATe:EMULation

                Arguments: 1, ON, OFF
                """

            STATe = STATe()  # type: ignore
            """
            `SOURce:AM:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/03a638cb0e924f7c.htm#ID_26d49ccd4d679ff50a00206a0016778c-d761ca934d679ff50a00206a0024546d-en-US>`_

            Arguments: 1, ON, OFF
            """

            class WIDeband(SCPINode, SCPISet):
                """
                SOURce:AM:WIDeband

                Arguments:
                """
                __slots__ = ()
                _cmd = "WIDeband"
                args = []  # type: List[str]

                class SENSitivity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:AM:WIDeband:SENSitivity

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "SENSitivity"
                    args = ["1"]

                SENSitivity = SENSitivity()  # type: ignore
                """
                SOURce:AM:WIDeband:SENSitivity

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:AM:WIDeband:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:AM:WIDeband:STATe

                Arguments: 1, ON, OFF
                """

            WIDeband = WIDeband()  # type: ignore
            """
            SOURce:AM:WIDeband

            Arguments:
            """

        AM = AM()  # type: ignore
        """
        SOURce:AM

        Arguments:
        """

        class BURSt(SCPINode, SCPISet):
            """
            SOURce:BURSt

            Arguments:
            """
            __slots__ = ()
            _cmd = "BURSt"
            args = []  # type: List[str]

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:BURSt:SOURce

                Arguments: EXTernal, EXTernal1, INTernal, INTernal1
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["EXTernal", "EXTernal1", "INTernal", "INTernal1"]

            SOURce = SOURce()  # type: ignore
            """
            SOURce:BURSt:SOURce

            Arguments: EXTernal, EXTernal1, INTernal, INTernal1
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:BURSt:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SOURce:BURSt:STATe

            Arguments: 1, ON, OFF
            """

        BURSt = BURSt()  # type: ignore
        """
        SOURce:BURSt

        Arguments:
        """

        class CORRection(SCPINode):
            """
            SOURce:CORRection

            Arguments:
            """
            __slots__ = ()
            _cmd = "CORRection"
            args = []  # type: List[str]

            class CSET(SCPINode):
                """
                SOURce:CORRection:CSET

                Arguments:
                """
                __slots__ = ()
                _cmd = "CSET"
                args = []  # type: List[str]

                class CATalog(SCPINode, SCPIQuery):
                    """
                    `SOURce:CORRection:CSET:CATalog
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/12dc5f6ae5524347.htm#ID_689cd4137c48ac3e0a00206a018986af-f5c35cc47c48ac3e0a00206a012bc823-en-US>`_

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CATalog"
                    args = []  # type: List[str]

                CATalog = CATalog()  # type: ignore
                """
                `SOURce:CORRection:CSET:CATalog
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/12dc5f6ae5524347.htm#ID_689cd4137c48ac3e0a00206a018986af-f5c35cc47c48ac3e0a00206a012bc823-en-US>`_

                Arguments:
                """

                class DATA(SCPINode):
                    """
                    SOURce:CORRection:CSET:DATA

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "DATA"
                    args = []  # type: List[str]

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:CORRection:CSET:DATA:FREQuency
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2dda9edb61694671.htm#ID_86873f407c48b1ac0a00206a004443cb-400402547c48b1bc0a00206a012bc823-en-US>`_

                        Arguments: <numeric_value>[HZ, KHZ, MHZ, GHZ],<numeric_value>
                        """
                        __slots__ = ()
                        _cmd = "FREQuency"
                        args = ["<numeric_value>[HZ", "KHZ", "MHZ", "GHZ],<numeric_value>"]

                        class POINts(SCPINode, SCPIQuery):
                            """
                            `SOURce:CORRection:CSET:DATA:FREQuency:POINts
                            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/4370c89124cc46f2.htm#ID_c0348a7c7c48b72b0a00206a014355d0-7dcc67e17c48b72b0a00206a012bc823-en-US>`_

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "POINts"
                            args = []  # type: List[str]

                        POINts = POINts()  # type: ignore
                        """
                        `SOURce:CORRection:CSET:DATA:FREQuency:POINts
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/4370c89124cc46f2.htm#ID_c0348a7c7c48b72b0a00206a014355d0-7dcc67e17c48b72b0a00206a012bc823-en-US>`_

                        Arguments:
                        """

                    FREQuency = FREQuency()  # type: ignore
                    """
                    `SOURce:CORRection:CSET:DATA:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2dda9edb61694671.htm#ID_86873f407c48b1ac0a00206a004443cb-400402547c48b1bc0a00206a012bc823-en-US>`_

                    Arguments: <numeric_value>[HZ, KHZ, MHZ, GHZ],<numeric_value>
                    """

                    class POWer(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:CORRection:CSET:DATA:POWer
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a6ceacf6151845d4.htm#ID_ff0722e77c48bc990a00206a002f7094-dc7cab557c48bc990a00206a012bc823-en-US>`_

                        Arguments: <numeric_value>[DB],<numeric_value>
                        """
                        __slots__ = ()
                        _cmd = "POWer"
                        args = ["<numeric_value>[DB],<numeric_value>"]

                        class POINts(SCPINode, SCPIQuery):
                            """
                            `SOURce:CORRection:CSET:DATA:POWer:POINts
                            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3f3849f7fd204e75.htm#ID_2516a43f7c48e2ce0a00206a00fc3ca9-c939d22e7c48e2ce0a00206a012bc823-en-US>`_

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "POINts"
                            args = []  # type: List[str]

                        POINts = POINts()  # type: ignore
                        """
                        `SOURce:CORRection:CSET:DATA:POWer:POINts
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3f3849f7fd204e75.htm#ID_2516a43f7c48e2ce0a00206a00fc3ca9-c939d22e7c48e2ce0a00206a012bc823-en-US>`_

                        Arguments:
                        """

                    POWer = POWer()  # type: ignore
                    """
                    `SOURce:CORRection:CSET:DATA:POWer
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a6ceacf6151845d4.htm#ID_ff0722e77c48bc990a00206a002f7094-dc7cab557c48bc990a00206a012bc823-en-US>`_

                    Arguments: <numeric_value>[DB],<numeric_value>
                    """

                DATA = DATA()  # type: ignore
                """
                SOURce:CORRection:CSET:DATA

                Arguments:
                """

                class DELete(SCPINode, SCPISet):
                    """
                    `SOURce:CORRection:CSET:DELete
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/8a1cfd4921054bf3.htm#ID_9095a51e7c48f4240a00206a018c3141-1e9571927c48f4240a00206a012bc823-en-US>`_

                    Arguments: 'string'
                    """
                    __slots__ = ()
                    _cmd = "DELete"
                    args = ["'string'"]

                DELete = DELete()  # type: ignore
                """
                `SOURce:CORRection:CSET:DELete
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/8a1cfd4921054bf3.htm#ID_9095a51e7c48f4240a00206a018c3141-1e9571927c48f4240a00206a012bc823-en-US>`_

                Arguments: 'string'
                """

                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:CORRection:CSET:SELect
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0c7e2d4956e34eb6.htm#ID_e15ed3447c488b480a00206a002fedba-f8db389d7c488b480a00206a012bc823-en-US>`_

                    Arguments: NONE, USER1, USER2, USER3, USER4, USER5
                    """
                    __slots__ = ()
                    _cmd = "SELect"
                    args = ["NONE", "USER1", "USER2", "USER3", "USER4", "USER5"]

                SELect = SELect()  # type: ignore
                """
                `SOURce:CORRection:CSET:SELect
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0c7e2d4956e34eb6.htm#ID_e15ed3447c488b480a00206a002fedba-f8db389d7c488b480a00206a012bc823-en-US>`_

                Arguments: NONE, USER1, USER2, USER3, USER4, USER5
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:CORRection:CSET:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:CORRection:CSET:STATe

                Arguments: 1, ON, OFF
                """

            CSET = CSET()  # type: ignore
            """
            SOURce:CORRection:CSET

            Arguments:
            """

            class FLATness(SCPINode):
                """
                SOURce:CORRection:FLATness

                Arguments:
                """
                __slots__ = ()
                _cmd = "FLATness"
                args = []  # type: List[str]

                class POINts(SCPINode, SCPIQuery):
                    """
                    SOURce:CORRection:FLATness:POINts

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "POINts"
                    args = ["1"]

                POINts = POINts()  # type: ignore
                """
                SOURce:CORRection:FLATness:POINts

                Arguments: 1
                """

                class PRESet(SCPINode, SCPISet):
                    """
                    SOURce:CORRection:FLATness:PRESet

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "PRESet"
                    args = []  # type: List[str]

                PRESet = PRESet()  # type: ignore
                """
                SOURce:CORRection:FLATness:PRESet

                Arguments:
                """

                class STORe(SCPINode, SCPISet):
                    """
                    SOURce:CORRection:FLATness:STORe

                    Arguments: 'string'
                    """
                    __slots__ = ()
                    _cmd = "STORe"
                    args = ["'string'"]

                STORe = STORe()  # type: ignore
                """
                SOURce:CORRection:FLATness:STORe

                Arguments: 'string'
                """

            FLATness = FLATness()  # type: ignore
            """
            SOURce:CORRection:FLATness

            Arguments:
            """

            class SOURce(SCPINodeN, SCPIQuery, SCPISet):
                """
                SOURce:CORRection:SOURce

                Arguments: ARRay, FLATness
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["ARRay", "FLATness"]

            SOURce = SOURce()  # type: ignore
            """
            SOURce:CORRection:SOURce

            Arguments: ARRay, FLATness
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SOURce:CORRection:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f493e8cd5b304030.htm#ID_bfaa6443312d91020a00206a014d3fc5-07f8da5e312d91020a00206a00c4603c-en-US>`_

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            `SOURce:CORRection:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f493e8cd5b304030.htm#ID_bfaa6443312d91020a00206a014d3fc5-07f8da5e312d91020a00206a00c4603c-en-US>`_

            Arguments: 1, ON, OFF
            """

        CORRection = CORRection()  # type: ignore
        """
        SOURce:CORRection

        Arguments:
        """

        class DM(SCPINode):
            """
            SOURce:DM

            Arguments:
            """
            __slots__ = ()
            _cmd = "DM"
            args = []  # type: List[str]

            class ASK(SCPINode):
                """
                SOURce:DM:ASK

                Arguments:
                """
                __slots__ = ()
                _cmd = "ASK"
                args = []  # type: List[str]

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:ASK:DEPTh

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()  # type: ignore
                """
                SOURce:DM:ASK:DEPTh

                Arguments: 1
                """

                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:ASK:POLarity

                    Arguments: INVerted, NORMal
                    """
                    __slots__ = ()
                    _cmd = "POLarity"
                    args = ["INVerted", "NORMal"]

                POLarity = POLarity()  # type: ignore
                """
                SOURce:DM:ASK:POLarity

                Arguments: INVerted, NORMal
                """

            ASK = ASK()  # type: ignore
            """
            SOURce:DM:ASK

            Arguments:
            """

            class BBFilter(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:DM:BBFilter

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "BBFilter"
                args = ["1"]

            BBFilter = BBFilter()  # type: ignore
            """
            SOURce:DM:BBFilter

            Arguments: 1
            """

            class EXTernal(SCPINode, SCPISet):
                """
                SOURce:DM:EXTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "EXTernal"
                args = []  # type: List[str]

                class ALC(SCPINode):
                    """
                    SOURce:DM:EXTernal:ALC

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ALC"
                    args = []  # type: List[str]

                    class BANDwidth(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:EXTernal:ALC:BANDwidth

                        Arguments: <numeric_value>, NARRow, NORMal
                        """
                        __slots__ = ()
                        _cmd = "BANDwidth"
                        args = ["<numeric_value>", "NARRow", "NORMal"]

                    BANDwidth = BANDwidth()  # type: ignore
                    """
                    SOURce:DM:EXTernal:ALC:BANDwidth

                    Arguments: <numeric_value>, NARRow, NORMal
                    """

                    class BWIDth(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:EXTernal:ALC:BWIDth

                        Arguments: <numeric_value>, NARRow, NORMal
                        """
                        __slots__ = ()
                        _cmd = "BWIDth"
                        args = ["<numeric_value>", "NARRow", "NORMal"]

                    BWIDth = BWIDth()  # type: ignore
                    """
                    SOURce:DM:EXTernal:ALC:BWIDth

                    Arguments: <numeric_value>, NARRow, NORMal
                    """

                ALC = ALC()  # type: ignore
                """
                SOURce:DM:EXTernal:ALC

                Arguments:
                """

                class FILTer(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:EXTernal:FILTer

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FILTer"
                    args = ["1"]

                FILTer = FILTer()  # type: ignore
                """
                SOURce:DM:EXTernal:FILTer

                Arguments: 1
                """

                class HCRest(SCPINode):
                    """
                    SOURce:DM:EXTernal:HCRest

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "HCRest"
                    args = []  # type: List[str]

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:DM:EXTernal:HCRest:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SOURce:DM:EXTernal:HCRest:STATe

                    Arguments: 1, ON, OFF
                    """

                HCRest = HCRest()  # type: ignore
                """
                SOURce:DM:EXTernal:HCRest

                Arguments:
                """

                class HICRest(SCPINode):
                    """
                    SOURce:DM:EXTernal:HICRest

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "HICRest"
                    args = []  # type: List[str]

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:DM:EXTernal:HICRest:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SOURce:DM:EXTernal:HICRest:STATe

                    Arguments: 1, ON, OFF
                    """

                HICRest = HICRest()  # type: ignore
                """
                SOURce:DM:EXTernal:HICRest

                Arguments:
                """

                class IMPedance(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:EXTernal:IMPedance

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()  # type: ignore
                """
                SOURce:DM:EXTernal:IMPedance

                Arguments: 1
                """

                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:EXTernal:POLarity

                    Arguments: INVert, NORMal
                    """
                    __slots__ = ()
                    _cmd = "POLarity"
                    args = ["INVert", "NORMal"]

                POLarity = POLarity()  # type: ignore
                """
                SOURce:DM:EXTernal:POLarity

                Arguments: INVert, NORMal
                """

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:EXTernal:SOURce

                    Arguments: BBG1, EXT600, EXTernal, INTernal, OFF, SUM
                    """
                    __slots__ = ()
                    _cmd = "SOURce"
                    args = ["BBG1", "EXT600", "EXTernal", "INTernal", "OFF", "SUM"]

                SOURce = SOURce()  # type: ignore
                """
                SOURce:DM:EXTernal:SOURce

                Arguments: BBG1, EXT600, EXTernal, INTernal, OFF, SUM
                """

            EXTernal = EXTernal()  # type: ignore
            """
            SOURce:DM:EXTernal

            Arguments:
            """

            class FSK(SCPINode):
                """
                SOURce:DM:FSK

                Arguments:
                """
                __slots__ = ()
                _cmd = "FSK"
                args = []  # type: List[str]

                class DEViation(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:FSK:DEViation

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DEViation"
                    args = ["1"]

                DEViation = DEViation()  # type: ignore
                """
                SOURce:DM:FSK:DEViation

                Arguments: 1
                """

                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:FSK:POLarity

                    Arguments: INVerted, NORMal
                    """
                    __slots__ = ()
                    _cmd = "POLarity"
                    args = ["INVerted", "NORMal"]

                POLarity = POLarity()  # type: ignore
                """
                SOURce:DM:FSK:POLarity

                Arguments: INVerted, NORMal
                """

            FSK = FSK()  # type: ignore
            """
            SOURce:DM:FSK

            Arguments:
            """

            class IMPairment(SCPINode):
                """
                SOURce:DM:IMPairment

                Arguments:
                """
                __slots__ = ()
                _cmd = "IMPairment"
                args = []  # type: List[str]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:DM:IMPairment:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:DM:IMPairment:STATe

                Arguments: 1, ON, OFF
                """

            IMPairment = IMPairment()  # type: ignore
            """
            SOURce:DM:IMPairment

            Arguments:
            """

            class IQ(SCPINode):
                """
                SOURce:DM:IQ

                Arguments:
                """
                __slots__ = ()
                _cmd = "IQ"
                args = []  # type: List[str]

                class CREStfactor(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQ:CREStfactor

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "CREStfactor"
                    args = ["1"]

                CREStfactor = CREStfactor()  # type: ignore
                """
                SOURce:DM:IQ:CREStfactor

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:DM:IQ:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:DM:IQ:STATe

                Arguments: 1, ON, OFF
                """

            IQ = IQ()  # type: ignore
            """
            SOURce:DM:IQ

            Arguments:
            """

            class IQADjustment(SCPINode):
                """
                SOURce:DM:IQADjustment

                Arguments:
                """
                __slots__ = ()
                _cmd = "IQADjustment"
                args = []  # type: List[str]

                class BBG(SCPINode):
                    """
                    SOURce:DM:IQADjustment:BBG

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "BBG"
                    args = []  # type: List[str]

                    class QSKew(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:BBG:QSKew

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "QSKew"
                        args = ["1"]

                    QSKew = QSKew()  # type: ignore
                    """
                    SOURce:DM:IQADjustment:BBG:QSKew

                    Arguments: 1
                    """

                BBG = BBG()  # type: ignore
                """
                SOURce:DM:IQADjustment:BBG

                Arguments:
                """

                class DELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQADjustment:DELay

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DELay"
                    args = ["1"]

                DELay = DELay()  # type: ignore
                """
                SOURce:DM:IQADjustment:DELay

                Arguments: 1
                """

                class EXTernal(SCPINode, SCPISet):
                    """
                    SOURce:DM:IQADjustment:EXTernal

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EXTernal"
                    args = []  # type: List[str]

                    class COFFset(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:COFFset

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "COFFset"
                        args = ["1"]

                    COFFset = COFFset()  # type: ignore
                    """
                    SOURce:DM:IQADjustment:EXTernal:COFFset

                    Arguments: 1
                    """

                    class DIOFfset(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:DIOFfset

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "DIOFfset"
                        args = ["1"]

                    DIOFfset = DIOFfset()  # type: ignore
                    """
                    SOURce:DM:IQADjustment:EXTernal:DIOFfset

                    Arguments: 1
                    """

                    class DQOFfset(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:DQOFfset

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "DQOFfset"
                        args = ["1"]

                    DQOFfset = DQOFfset()  # type: ignore
                    """
                    SOURce:DM:IQADjustment:EXTernal:DQOFfset

                    Arguments: 1
                    """

                    class IOFFset(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:IOFFset

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "IOFFset"
                        args = ["1"]

                    IOFFset = IOFFset()  # type: ignore
                    """
                    SOURce:DM:IQADjustment:EXTernal:IOFFset

                    Arguments: 1
                    """

                    class IQATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:IQATten

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "IQATten"
                        args = ["1"]

                    IQATten = IQATten()  # type: ignore
                    """
                    SOURce:DM:IQADjustment:EXTernal:IQATten

                    Arguments: 1
                    """

                    class QOFFset(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:QOFFset

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "QOFFset"
                        args = ["1"]

                    QOFFset = QOFFset()  # type: ignore
                    """
                    SOURce:DM:IQADjustment:EXTernal:QOFFset

                    Arguments: 1
                    """

                EXTernal = EXTernal()  # type: ignore
                """
                SOURce:DM:IQADjustment:EXTernal

                Arguments:
                """

                class IOFFset(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQADjustment:IOFFset

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "IOFFset"
                    args = ["1"]

                IOFFset = IOFFset()  # type: ignore
                """
                SOURce:DM:IQADjustment:IOFFset

                Arguments: 1
                """

                class QOFFset(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQADjustment:QOFFset

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "QOFFset"
                    args = ["1"]

                QOFFset = QOFFset()  # type: ignore
                """
                SOURce:DM:IQADjustment:QOFFset

                Arguments: 1
                """

                class QSKew(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQADjustment:QSKew

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "QSKew"
                    args = ["1"]

                QSKew = QSKew()  # type: ignore
                """
                SOURce:DM:IQADjustment:QSKew

                Arguments: 1
                """

                class SKEW(SCPINode):
                    """
                    SOURce:DM:IQADjustment:SKEW

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SKEW"
                    args = []  # type: List[str]

                    class DELay(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:SKEW:DELay

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "DELay"
                        args = ["1"]

                    DELay = DELay()  # type: ignore
                    """
                    SOURce:DM:IQADjustment:SKEW:DELay

                    Arguments: 1
                    """

                SKEW = SKEW()  # type: ignore
                """
                SOURce:DM:IQADjustment:SKEW

                Arguments:
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:DM:IQADjustment:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:DM:IQADjustment:STATe

                Arguments: 1, ON, OFF
                """

            IQADjustment = IQADjustment()  # type: ignore
            """
            SOURce:DM:IQADjustment

            Arguments:
            """

            class IQRatio(SCPINode):
                """
                SOURce:DM:IQRatio

                Arguments:
                """
                __slots__ = ()
                _cmd = "IQRatio"
                args = []  # type: List[str]

                class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQRatio:MAGNitude

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "MAGNitude"
                    args = ["1"]

                MAGNitude = MAGNitude()  # type: ignore
                """
                SOURce:DM:IQRatio:MAGNitude

                Arguments: 1
                """

            IQRatio = IQRatio()  # type: ignore
            """
            SOURce:DM:IQRatio

            Arguments:
            """

            class IQSWap(SCPINode):
                """
                SOURce:DM:IQSWap

                Arguments:
                """
                __slots__ = ()
                _cmd = "IQSWap"
                args = []  # type: List[str]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:DM:IQSWap:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:DM:IQSWap:STATe

                Arguments: 1, ON, OFF
                """

            IQSWap = IQSWap()  # type: ignore
            """
            SOURce:DM:IQSWap

            Arguments:
            """

            class LEAKage(SCPINode):
                """
                SOURce:DM:LEAKage

                Arguments:
                """
                __slots__ = ()
                _cmd = "LEAKage"
                args = []  # type: List[str]

                class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:LEAKage:MAGNitude

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "MAGNitude"
                    args = ["1"]

                MAGNitude = MAGNitude()  # type: ignore
                """
                SOURce:DM:LEAKage:MAGNitude

                Arguments: 1
                """

            LEAKage = LEAKage()  # type: ignore
            """
            SOURce:DM:LEAKage

            Arguments:
            """

            class MODulation(SCPINode, SCPISet):
                """
                SOURce:DM:MODulation

                Arguments:
                """
                __slots__ = ()
                _cmd = "MODulation"
                args = []  # type: List[str]

                class ATTen(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:MODulation:ATTen

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ATTen"
                    args = ["1"]

                ATTen = ATTen()  # type: ignore
                """
                SOURce:DM:MODulation:ATTen

                Arguments: 1
                """

                class FILTer(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:MODulation:FILTer

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FILTer"
                    args = ["1"]

                FILTer = FILTer()  # type: ignore
                """
                SOURce:DM:MODulation:FILTer

                Arguments: 1
                """

            MODulation = MODulation()  # type: ignore
            """
            SOURce:DM:MODulation

            Arguments:
            """

            class QUADrature(SCPINode):
                """
                SOURce:DM:QUADrature

                Arguments:
                """
                __slots__ = ()
                _cmd = "QUADrature"
                args = []  # type: List[str]

                class ANGLe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:QUADrature:ANGLe

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ANGLe"
                    args = ["1"]

                ANGLe = ANGLe()  # type: ignore
                """
                SOURce:DM:QUADrature:ANGLe

                Arguments: 1
                """

            QUADrature = QUADrature()  # type: ignore
            """
            SOURce:DM:QUADrature

            Arguments:
            """

            class SKEW(SCPINode):
                """
                SOURce:DM:SKEW

                Arguments:
                """
                __slots__ = ()
                _cmd = "SKEW"
                args = []  # type: List[str]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:DM:SKEW:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:DM:SKEW:STATe

                Arguments: 1, ON, OFF
                """

            SKEW = SKEW()  # type: ignore
            """
            SOURce:DM:SKEW

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:DM:SOURce

                Arguments: EXTernal, INTernal, SUM
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["EXTernal", "INTernal", "SUM"]

            SOURce = SOURce()  # type: ignore
            """
            SOURce:DM:SOURce

            Arguments: EXTernal, INTernal, SUM
            """

            class SRATio(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:DM:SRATio

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "SRATio"
                args = ["1"]

            SRATio = SRATio()  # type: ignore
            """
            SOURce:DM:SRATio

            Arguments: 1
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:DM:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SOURce:DM:STATe

            Arguments: 1, ON, OFF
            """

        DM = DM()  # type: ignore
        """
        SOURce:DM

        Arguments:
        """

        class FM(SCPINode):
            """
            SOURce:FM

            Arguments:
            """
            __slots__ = ()
            _cmd = "FM"
            args = []  # type: List[str]

            class BANDwidth(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FM:BANDwidth

                Arguments: STANdard, WIDE
                """
                __slots__ = ()
                _cmd = "BANDwidth"
                args = ["STANdard", "WIDE"]

            BANDwidth = BANDwidth()  # type: ignore
            """
            SOURce:FM:BANDwidth

            Arguments: STANdard, WIDE
            """

            class COUPling(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FM:COUPling

                Arguments: AC, DC
                """
                __slots__ = ()
                _cmd = "COUPling"
                args = ["AC", "DC"]

            COUPling = COUPling()  # type: ignore
            """
            SOURce:FM:COUPling

            Arguments: AC, DC
            """

            class DEViation(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FM:DEViation
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/17615211bdc2474d.htm#ID_4adf1663ed64b2010a00201901e52a86-bfbdd369ed64afa00a00201900ba4ad4-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DEViation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:FM:DEViation:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FM:DEViation:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:FM:DEViation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:FM:DEViation:STEP

                Arguments:
                """

                class TRACk(SCPINode, SCPIBool):
                    """
                    SOURce:FM:DEViation:TRACk

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "TRACk"
                    args = ["1", "ON", "OFF"]

                TRACk = TRACk()  # type: ignore
                """
                SOURce:FM:DEViation:TRACk

                Arguments: 1, ON, OFF
                """

            DEViation = DEViation()  # type: ignore
            """
            `SOURce:FM:DEViation
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/17615211bdc2474d.htm#ID_4adf1663ed64b2010a00201901e52a86-bfbdd369ed64afa00a00201900ba4ad4-en-US>`_

            Arguments: 1
            """

            class EXTernal(SCPINode, SCPISet):
                """
                SOURce:FM:EXTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "EXTernal"
                args = []  # type: List[str]

                class COUPling(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:FM:EXTernal:COUPling
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/713237eac8644509.htm#ID_4fe894544d707f4e0a00206a01cec433-d1c7c3df4d707f4e0a00206a0024546d-en-US>`_

                    Arguments: AC, DC
                    """
                    __slots__ = ()
                    _cmd = "COUPling"
                    args = ["AC", "DC"]

                COUPling = COUPling()  # type: ignore
                """
                `SOURce:FM:EXTernal:COUPling
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/713237eac8644509.htm#ID_4fe894544d707f4e0a00206a01cec433-d1c7c3df4d707f4e0a00206a0024546d-en-US>`_

                Arguments: AC, DC
                """

                class IMPedance(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FM:EXTernal:IMPedance

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()  # type: ignore
                """
                SOURce:FM:EXTernal:IMPedance

                Arguments: 1
                """

            EXTernal = EXTernal()  # type: ignore
            """
            SOURce:FM:EXTernal

            Arguments:
            """

            class FILTer(SCPINode):
                """
                SOURce:FM:FILTer

                Arguments:
                """
                __slots__ = ()
                _cmd = "FILTer"
                args = []  # type: List[str]

                class HPASs(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FM:FILTer:HPASs

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "HPASs"
                    args = ["1"]

                HPASs = HPASs()  # type: ignore
                """
                SOURce:FM:FILTer:HPASs

                Arguments: 1
                """

            FILTer = FILTer()  # type: ignore
            """
            SOURce:FM:FILTer

            Arguments:
            """

            class INTernal(SCPINode, SCPISet):
                """
                SOURce:FM:INTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "INTernal"
                args = []  # type: List[str]

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FM:INTernal:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                    class ALTernate(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FM:INTernal:FREQuency:ALTernate

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "ALTernate"
                        args = ["1"]

                        class AMPLitude(SCPINode, SCPISet):
                            """
                            SOURce:FM:INTernal:FREQuency:ALTernate:AMPLitude

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "AMPLitude"
                            args = []  # type: List[str]

                            class PERCent(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:FM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "PERCent"
                                args = ["1"]

                            PERCent = PERCent()  # type: ignore
                            """
                            SOURce:FM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                            Arguments: 1
                            """

                        AMPLitude = AMPLitude()  # type: ignore
                        """
                        SOURce:FM:INTernal:FREQuency:ALTernate:AMPLitude

                        Arguments:
                        """

                    ALTernate = ALTernate()  # type: ignore
                    """
                    SOURce:FM:INTernal:FREQuency:ALTernate

                    Arguments: 1
                    """

                    class STEP(SCPINode):
                        """
                        SOURce:FM:INTernal:FREQuency:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:FM:INTernal:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:FM:INTernal:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:FM:INTernal:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:FM:INTernal:FREQuency

                Arguments: 1
                """

                class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FM:INTernal:FUNCtion

                    Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                    """
                    __slots__ = ()
                    _cmd = "FUNCtion"
                    args = ["GAUSsian", "NOISe", "RAMP", "SINusoid", "SQUare", "TRIangle", "UNIForm"]

                    class NOISe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FM:INTernal:FUNCtion:NOISe

                        Arguments: GAUSsian, UNIForm
                        """
                        __slots__ = ()
                        _cmd = "NOISe"
                        args = ["GAUSsian", "UNIForm"]

                    NOISe = NOISe()  # type: ignore
                    """
                    SOURce:FM:INTernal:FUNCtion:NOISe

                    Arguments: GAUSsian, UNIForm
                    """

                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FM:INTernal:FUNCtion:SHAPe

                        Arguments: SINE, SQUare
                        """
                        __slots__ = ()
                        _cmd = "SHAPe"
                        args = ["SINE", "SQUare"]

                    SHAPe = SHAPe()  # type: ignore
                    """
                    SOURce:FM:INTernal:FUNCtion:SHAPe

                    Arguments: SINE, SQUare
                    """

                FUNCtion = FUNCtion()  # type: ignore
                """
                SOURce:FM:INTernal:FUNCtion

                Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                """

                class SWEep(SCPINode, SCPISet):
                    """
                    SOURce:FM:INTernal:SWEep

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SWEep"
                    args = []  # type: List[str]

                    class TRIGger(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FM:INTernal:SWEep:TRIGger

                        Arguments: BUS, EXTernal, IMMediate, KEY
                        """
                        __slots__ = ()
                        _cmd = "TRIGger"
                        args = ["BUS", "EXTernal", "IMMediate", "KEY"]

                    TRIGger = TRIGger()  # type: ignore
                    """
                    SOURce:FM:INTernal:SWEep:TRIGger

                    Arguments: BUS, EXTernal, IMMediate, KEY
                    """

                SWEep = SWEep()  # type: ignore
                """
                SOURce:FM:INTernal:SWEep

                Arguments:
                """

            INTernal = INTernal()  # type: ignore
            """
            SOURce:FM:INTernal

            Arguments:
            """

            class PREemphasis(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FM:PREemphasis

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PREemphasis"
                args = ["1"]

            PREemphasis = PREemphasis()  # type: ignore
            """
            SOURce:FM:PREemphasis

            Arguments: 1
            """

            class SENSitivity(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FM:SENSitivity
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/d6f8c97d066e4010.htm#ID_3d6e84804d70782a0a00206a0179e300-35b70df44d70782a0a00206a0024546d-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "SENSitivity"
                args = ["1"]

            SENSitivity = SENSitivity()  # type: ignore
            """
            `SOURce:FM:SENSitivity
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/d6f8c97d066e4010.htm#ID_3d6e84804d70782a0a00206a0179e300-35b70df44d70782a0a00206a0024546d-en-US>`_

            Arguments: 1
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FM:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/ddeceb86743c4342.htm#ID_7ce7c1e54d7085a70a00206a0035ad95-7c998c484d7085a70a00206a0024546d-en-US>`_

                Arguments: EXTernal, INT1, INT2, INTernal, INTernal1, INTernal2,EXTernal, INT1, INTernal, INTernal1
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["EXTernal", "INT1", "INT2", "INTernal", "INTernal1", "INTernal2,EXTernal", "INT1", "INTernal", "INTernal1"]

            SOURce = SOURce()  # type: ignore
            """
            `SOURce:FM:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/ddeceb86743c4342.htm#ID_7ce7c1e54d7085a70a00206a0035ad95-7c998c484d7085a70a00206a0024546d-en-US>`_

            Arguments: EXTernal, INT1, INT2, INTernal, INTernal1, INTernal2,EXTernal, INT1, INTernal, INTernal1
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SOURce:FM:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bfc4735fb97e4afb.htm#ID_56f39a7a4d708c000a00206a00870c91-8d7d16d14d708c000a00206a0024546d-en-US>`_

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

                class EMULation(SCPINode, SCPIBool):
                    """
                    SOURce:FM:STATe:EMULation

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "EMULation"
                    args = ["1", "ON", "OFF"]

                EMULation = EMULation()  # type: ignore
                """
                SOURce:FM:STATe:EMULation

                Arguments: 1, ON, OFF
                """

            STATe = STATe()  # type: ignore
            """
            `SOURce:FM:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bfc4735fb97e4afb.htm#ID_56f39a7a4d708c000a00206a00870c91-8d7d16d14d708c000a00206a0024546d-en-US>`_

            Arguments: 1, ON, OFF
            """

        FM = FM()  # type: ignore
        """
        SOURce:FM

        Arguments:
        """

        class FREQuency(SCPINode, SCPISet):
            """
            SOURce:FREQuency

            Arguments:
            """
            __slots__ = ()
            _cmd = "FREQuency"
            args = []  # type: List[str]

            class CENTer(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:CENTer
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2cf6c143b3cf4c4b.htm#ID_94b28e8271966ef30a00206a004b06bb-b020ee7271966ef30a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "CENTer"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:CENTer:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:CENTer:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:FREQuency:CENTer:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:FREQuency:CENTer:STEP

                Arguments:
                """

            CENTer = CENTer()  # type: ignore
            """
            `SOURce:FREQuency:CENTer
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2cf6c143b3cf4c4b.htm#ID_94b28e8271966ef30a00206a004b06bb-b020ee7271966ef30a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class CHANnels(SCPINode):
                """
                SOURce:FREQuency:CHANnels

                Arguments:
                """
                __slots__ = ()
                _cmd = "CHANnels"
                args = []  # type: List[str]

                class NUMBer(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FREQuency:CHANnels:NUMBer

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NUMBer"
                    args = ["1"]

                NUMBer = NUMBer()  # type: ignore
                """
                SOURce:FREQuency:CHANnels:NUMBer

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:FREQuency:CHANnels:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:FREQuency:CHANnels:STATe

                Arguments: 1, ON, OFF
                """

            CHANnels = CHANnels()  # type: ignore
            """
            SOURce:FREQuency:CHANnels

            Arguments:
            """

            class CW(SCPINode):
                """
                SOURce:FREQuency:CW

                Arguments:
                """
                __slots__ = ()
                _cmd = "CW"
                args = []  # type: List[str]

                class BACKup(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FREQuency:CW:BACKup

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "BACKup"
                    args = ["1"]

                BACKup = BACKup()  # type: ignore
                """
                SOURce:FREQuency:CW:BACKup

                Arguments: 1
                """

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:CW:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:CW:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:FREQuency:CW:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:FREQuency:CW:STEP

                Arguments:
                """

            CW = CW()  # type: ignore
            """
            SOURce:FREQuency:CW

            Arguments:
            """

            class ERANge(SCPINode, SCPIBool):
                """
                SOURce:FREQuency:ERANge

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "ERANge"
                args = ["1", "ON", "OFF"]

            ERANge = ERANge()  # type: ignore
            """
            SOURce:FREQuency:ERANge

            Arguments: 1, ON, OFF
            """

            class FIXed(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FREQuency:FIXed

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "FIXed"
                args = ["1"]

                class BACKup(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FREQuency:FIXed:BACKup

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "BACKup"
                    args = ["1"]

                BACKup = BACKup()  # type: ignore
                """
                SOURce:FREQuency:FIXed:BACKup

                Arguments: 1
                """

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:FIXed:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:FIXed:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:FREQuency:FIXed:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:FREQuency:FIXed:STEP

                Arguments:
                """

            FIXed = FIXed()  # type: ignore
            """
            SOURce:FREQuency:FIXed

            Arguments: 1
            """

            class MANual(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:MANual
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b256342b64e54406.htm#ID_c7717ccc71967af90a00206a0175c71f-fcb82bd071967af90a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "MANual"
                args = ["1"]

            MANual = MANual()  # type: ignore
            """
            `SOURce:FREQuency:MANual
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b256342b64e54406.htm#ID_c7717ccc71967af90a00206a0175c71f-fcb82bd071967af90a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class MULTiplier(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:MULTiplier
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a9bd609236c14729.htm#ID_3351c13f7196e80a0a00206a0041112e-e73472347196e80a0a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "MULTiplier"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:FREQuency:MULTiplier:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:FREQuency:MULTiplier:STATe

                Arguments: 1, ON, OFF
                """

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:MULTiplier:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:MULTiplier:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:FREQuency:MULTiplier:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:FREQuency:MULTiplier:STEP

                Arguments:
                """

            MULTiplier = MULTiplier()  # type: ignore
            """
            `SOURce:FREQuency:MULTiplier
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a9bd609236c14729.htm#ID_3351c13f7196e80a0a00206a0041112e-e73472347196e80a0a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class OFFSet(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:OFFSet
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/cb510032520641ae.htm#ID_af38e01f71962fc70a00206a0025f2de-cb72d0b271962fc70a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "OFFSet"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:FREQuency:OFFSet:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:FREQuency:OFFSet:STATe

                Arguments: 1, ON, OFF
                """

            OFFSet = OFFSet()  # type: ignore
            """
            `SOURce:FREQuency:OFFSet
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/cb510032520641ae.htm#ID_af38e01f71962fc70a00206a0025f2de-cb72d0b271962fc70a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class PHASe(SCPINode, SCPISet):
                """
                SOURce:FREQuency:PHASe

                Arguments:
                """
                __slots__ = ()
                _cmd = "PHASe"
                args = []  # type: List[str]

                class CONTinuous(SCPINode, SCPISet):
                    """
                    SOURce:FREQuency:PHASe:CONTinuous

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONTinuous"
                    args = []  # type: List[str]

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:FREQuency:PHASe:CONTinuous:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SOURce:FREQuency:PHASe:CONTinuous:STATe

                    Arguments: 1, ON, OFF
                    """

                CONTinuous = CONTinuous()  # type: ignore
                """
                SOURce:FREQuency:PHASe:CONTinuous

                Arguments:
                """

            PHASe = PHASe()  # type: ignore
            """
            SOURce:FREQuency:PHASe

            Arguments:
            """

            class REFerence(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FREQuency:REFerence

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "REFerence"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:FREQuency:REFerence:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:FREQuency:REFerence:STATe

                Arguments: 1, ON, OFF
                """

            REFerence = REFerence()  # type: ignore
            """
            SOURce:FREQuency:REFerence

            Arguments: 1
            """

            class SPAN(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:SPAN
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/918726699f9a436a.htm#ID_877b9a2d71969db30a00206a01270bed-91afc66471969db30a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "SPAN"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:SPAN:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:SPAN:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:FREQuency:SPAN:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:FREQuency:SPAN:STEP

                Arguments:
                """

            SPAN = SPAN()  # type: ignore
            """
            `SOURce:FREQuency:SPAN
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/918726699f9a436a.htm#ID_877b9a2d71969db30a00206a01270bed-91afc66471969db30a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:STARt
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0f57f1e62e22466d.htm#ID_d6ff21d9719686b10a00206a016817d0-3e9f661a719686b10a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STARt"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:STARt:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:STARt:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:FREQuency:STARt:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:FREQuency:STARt:STEP

                Arguments:
                """

            STARt = STARt()  # type: ignore
            """
            `SOURce:FREQuency:STARt
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0f57f1e62e22466d.htm#ID_d6ff21d9719686b10a00206a016817d0-3e9f661a719686b10a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class STEP(SCPINode):
                """
                SOURce:FREQuency:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:FREQuency:STEP:INCRement
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/86e6c5f55e234c7f.htm#ID_89eaa7f5719647a40a00206a01cdb994-b088125d719647a40a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()  # type: ignore
                """
                `SOURce:FREQuency:STEP:INCRement
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/86e6c5f55e234c7f.htm#ID_89eaa7f5719647a40a00206a01cdb994-b088125d719647a40a00206a012bc823-en-US>`_

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            SOURce:FREQuency:STEP

            Arguments:
            """

            class STOP(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:STOP
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0affa845d399442b.htm#ID_af855a1c7196919e0a00206a00d3c228-eea6068f7196919e0a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STOP"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:STOP:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:STOP:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:FREQuency:STOP:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:FREQuency:STOP:STEP

                Arguments:
                """

            STOP = STOP()  # type: ignore
            """
            `SOURce:FREQuency:STOP
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0affa845d399442b.htm#ID_af855a1c7196919e0a00206a00d3c228-eea6068f7196919e0a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class SYNThesis(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FREQuency:SYNThesis

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "SYNThesis"
                args = ["1"]

            SYNThesis = SYNThesis()  # type: ignore
            """
            SOURce:FREQuency:SYNThesis

            Arguments: 1
            """

        FREQuency = FREQuency()  # type: ignore
        """
        SOURce:FREQuency

        Arguments:
        """

        class FUNCtion(SCPINode):
            """
            SOURce:FUNCtion

            Arguments:
            """
            __slots__ = ()
            _cmd = "FUNCtion"
            args = []  # type: List[str]

            class SHAPe(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FUNCtion:SHAPe

                Arguments: PRNoise, SAWTooth, SINusoid, SQUare, TRIangle
                """
                __slots__ = ()
                _cmd = "SHAPe"
                args = ["PRNoise", "SAWTooth", "SINusoid", "SQUare", "TRIangle"]

            SHAPe = SHAPe()  # type: ignore
            """
            SOURce:FUNCtion:SHAPe

            Arguments: PRNoise, SAWTooth, SINusoid, SQUare, TRIangle
            """

        FUNCtion = FUNCtion()  # type: ignore
        """
        SOURce:FUNCtion

        Arguments:
        """

        class ILS(SCPINode):
            """
            SOURce:ILS

            Arguments:
            """
            __slots__ = ()
            _cmd = "ILS"
            args = []  # type: List[str]

            class GS(SCPINode):
                """
                SOURce:ILS:GS

                Arguments:
                """
                __slots__ = ()
                _cmd = "GS"
                args = []  # type: List[str]

                class COMid(SCPINode):
                    """
                    SOURce:ILS:GS:COMid

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "COMid"
                    args = []  # type: List[str]

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:COMid:DEPTh

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()  # type: ignore
                    """
                    SOURce:ILS:GS:COMid:DEPTh

                    Arguments: 1
                    """

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:COMid:FREQuency

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()  # type: ignore
                    """
                    SOURce:ILS:GS:COMid:FREQuency

                    Arguments: 1
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:ILS:GS:COMid:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SOURce:ILS:GS:COMid:STATe

                    Arguments: 1, ON, OFF
                    """

                COMid = COMid()  # type: ignore
                """
                SOURce:ILS:GS:COMid

                Arguments:
                """

                class DDM(SCPINode):
                    """
                    SOURce:ILS:GS:DDM

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "DDM"
                    args = []  # type: List[str]

                    class CURRent(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:DDM:CURRent

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "CURRent"
                        args = ["1"]

                    CURRent = CURRent()  # type: ignore
                    """
                    SOURce:ILS:GS:DDM:CURRent

                    Arguments: 1
                    """

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:DDM:DEPTh

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()  # type: ignore
                    """
                    SOURce:ILS:GS:DDM:DEPTh

                    Arguments: 1
                    """

                    class DIRection(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:DDM:DIRection

                        Arguments: DOWN, UP
                        """
                        __slots__ = ()
                        _cmd = "DIRection"
                        args = ["DOWN", "UP"]

                    DIRection = DIRection()  # type: ignore
                    """
                    SOURce:ILS:GS:DDM:DIRection

                    Arguments: DOWN, UP
                    """

                    class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:DDM:LOGarithmic

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()  # type: ignore
                    """
                    SOURce:ILS:GS:DDM:LOGarithmic

                    Arguments: 1
                    """

                DDM = DDM()  # type: ignore
                """
                SOURce:ILS:GS:DDM

                Arguments:
                """

                class LLOBe(SCPINode):
                    """
                    SOURce:ILS:GS:LLOBe

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "LLOBe"
                    args = []  # type: List[str]

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:LLOBe:FREQuency

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()  # type: ignore
                    """
                    SOURce:ILS:GS:LLOBe:FREQuency

                    Arguments: 1
                    """

                LLOBe = LLOBe()  # type: ignore
                """
                SOURce:ILS:GS:LLOBe

                Arguments:
                """

                class PHASe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GS:PHASe

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PHASe"
                    args = ["1"]

                PHASe = PHASe()  # type: ignore
                """
                SOURce:ILS:GS:PHASe

                Arguments: 1
                """

                class PRESet(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GS:PRESet

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "PRESet"
                    args = []  # type: List[str]

                PRESet = PRESet()  # type: ignore
                """
                SOURce:ILS:GS:PRESet

                Arguments:
                """

                class SODepth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GS:SODepth

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "SODepth"
                    args = ["1"]

                SODepth = SODepth()  # type: ignore
                """
                SOURce:ILS:GS:SODepth

                Arguments: 1
                """

                class ULOBe(SCPINode):
                    """
                    SOURce:ILS:GS:ULOBe

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ULOBe"
                    args = []  # type: List[str]

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:ULOBe:FREQuency

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()  # type: ignore
                    """
                    SOURce:ILS:GS:ULOBe:FREQuency

                    Arguments: 1
                    """

                ULOBe = ULOBe()  # type: ignore
                """
                SOURce:ILS:GS:ULOBe

                Arguments:
                """

            GS = GS()  # type: ignore
            """
            SOURce:ILS:GS

            Arguments:
            """

            class GSLope(SCPINode):
                """
                SOURce:ILS:GSLope

                Arguments:
                """
                __slots__ = ()
                _cmd = "GSLope"
                args = []  # type: List[str]

                class COMid(SCPINode):
                    """
                    SOURce:ILS:GSLope:COMid

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "COMid"
                    args = []  # type: List[str]

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:COMid:DEPTh

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()  # type: ignore
                    """
                    SOURce:ILS:GSLope:COMid:DEPTh

                    Arguments: 1
                    """

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:COMid:FREQuency

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()  # type: ignore
                    """
                    SOURce:ILS:GSLope:COMid:FREQuency

                    Arguments: 1
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:ILS:GSLope:COMid:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SOURce:ILS:GSLope:COMid:STATe

                    Arguments: 1, ON, OFF
                    """

                COMid = COMid()  # type: ignore
                """
                SOURce:ILS:GSLope:COMid

                Arguments:
                """

                class DDM(SCPINode):
                    """
                    SOURce:ILS:GSLope:DDM

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "DDM"
                    args = []  # type: List[str]

                    class CURRent(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:DDM:CURRent

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "CURRent"
                        args = ["1"]

                    CURRent = CURRent()  # type: ignore
                    """
                    SOURce:ILS:GSLope:DDM:CURRent

                    Arguments: 1
                    """

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:DDM:DEPTh

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()  # type: ignore
                    """
                    SOURce:ILS:GSLope:DDM:DEPTh

                    Arguments: 1
                    """

                    class DIRection(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:DDM:DIRection

                        Arguments: DOWN, UP
                        """
                        __slots__ = ()
                        _cmd = "DIRection"
                        args = ["DOWN", "UP"]

                    DIRection = DIRection()  # type: ignore
                    """
                    SOURce:ILS:GSLope:DDM:DIRection

                    Arguments: DOWN, UP
                    """

                    class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:DDM:LOGarithmic

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()  # type: ignore
                    """
                    SOURce:ILS:GSLope:DDM:LOGarithmic

                    Arguments: 1
                    """

                DDM = DDM()  # type: ignore
                """
                SOURce:ILS:GSLope:DDM

                Arguments:
                """

                class LLOBe(SCPINode):
                    """
                    SOURce:ILS:GSLope:LLOBe

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "LLOBe"
                    args = []  # type: List[str]

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:LLOBe:FREQuency

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()  # type: ignore
                    """
                    SOURce:ILS:GSLope:LLOBe:FREQuency

                    Arguments: 1
                    """

                LLOBe = LLOBe()  # type: ignore
                """
                SOURce:ILS:GSLope:LLOBe

                Arguments:
                """

                class PHASe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GSLope:PHASe

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PHASe"
                    args = ["1"]

                PHASe = PHASe()  # type: ignore
                """
                SOURce:ILS:GSLope:PHASe

                Arguments: 1
                """

                class PRESet(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GSLope:PRESet

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "PRESet"
                    args = []  # type: List[str]

                PRESet = PRESet()  # type: ignore
                """
                SOURce:ILS:GSLope:PRESet

                Arguments:
                """

                class SODepth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GSLope:SODepth

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "SODepth"
                    args = ["1"]

                SODepth = SODepth()  # type: ignore
                """
                SOURce:ILS:GSLope:SODepth

                Arguments: 1
                """

                class ULOBe(SCPINode):
                    """
                    SOURce:ILS:GSLope:ULOBe

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ULOBe"
                    args = []  # type: List[str]

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:ULOBe:FREQuency

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()  # type: ignore
                    """
                    SOURce:ILS:GSLope:ULOBe:FREQuency

                    Arguments: 1
                    """

                ULOBe = ULOBe()  # type: ignore
                """
                SOURce:ILS:GSLope:ULOBe

                Arguments:
                """

            GSLope = GSLope()  # type: ignore
            """
            SOURce:ILS:GSLope

            Arguments:
            """

            class LOCalizer(SCPINode):
                """
                SOURce:ILS:LOCalizer

                Arguments:
                """
                __slots__ = ()
                _cmd = "LOCalizer"
                args = []  # type: List[str]

                class COMid(SCPINode):
                    """
                    SOURce:ILS:LOCalizer:COMid

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "COMid"
                    args = []  # type: List[str]

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:COMid:DEPTh

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()  # type: ignore
                    """
                    SOURce:ILS:LOCalizer:COMid:DEPTh

                    Arguments: 1
                    """

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:COMid:FREQuency

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()  # type: ignore
                    """
                    SOURce:ILS:LOCalizer:COMid:FREQuency

                    Arguments: 1
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:ILS:LOCalizer:COMid:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SOURce:ILS:LOCalizer:COMid:STATe

                    Arguments: 1, ON, OFF
                    """

                COMid = COMid()  # type: ignore
                """
                SOURce:ILS:LOCalizer:COMid

                Arguments:
                """

                class DDM(SCPINode):
                    """
                    SOURce:ILS:LOCalizer:DDM

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "DDM"
                    args = []  # type: List[str]

                    class CURRent(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:DDM:CURRent

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "CURRent"
                        args = ["1"]

                    CURRent = CURRent()  # type: ignore
                    """
                    SOURce:ILS:LOCalizer:DDM:CURRent

                    Arguments: 1
                    """

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:DDM:DEPTh

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()  # type: ignore
                    """
                    SOURce:ILS:LOCalizer:DDM:DEPTh

                    Arguments: 1
                    """

                    class DIRection(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:DDM:DIRection

                        Arguments: LEFT, RIGHt
                        """
                        __slots__ = ()
                        _cmd = "DIRection"
                        args = ["LEFT", "RIGHt"]

                    DIRection = DIRection()  # type: ignore
                    """
                    SOURce:ILS:LOCalizer:DDM:DIRection

                    Arguments: LEFT, RIGHt
                    """

                    class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:DDM:LOGarithmic

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()  # type: ignore
                    """
                    SOURce:ILS:LOCalizer:DDM:LOGarithmic

                    Arguments: 1
                    """

                DDM = DDM()  # type: ignore
                """
                SOURce:ILS:LOCalizer:DDM

                Arguments:
                """

                class LLOBe(SCPINode):
                    """
                    SOURce:ILS:LOCalizer:LLOBe

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "LLOBe"
                    args = []  # type: List[str]

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:LLOBe:FREQuency

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()  # type: ignore
                    """
                    SOURce:ILS:LOCalizer:LLOBe:FREQuency

                    Arguments: 1
                    """

                LLOBe = LLOBe()  # type: ignore
                """
                SOURce:ILS:LOCalizer:LLOBe

                Arguments:
                """

                class PHASe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:LOCalizer:PHASe

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PHASe"
                    args = ["1"]

                PHASe = PHASe()  # type: ignore
                """
                SOURce:ILS:LOCalizer:PHASe

                Arguments: 1
                """

                class PRESet(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:LOCalizer:PRESet

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "PRESet"
                    args = []  # type: List[str]

                PRESet = PRESet()  # type: ignore
                """
                SOURce:ILS:LOCalizer:PRESet

                Arguments:
                """

                class RLOBe(SCPINode):
                    """
                    SOURce:ILS:LOCalizer:RLOBe

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "RLOBe"
                    args = []  # type: List[str]

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:RLOBe:FREQuency

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()  # type: ignore
                    """
                    SOURce:ILS:LOCalizer:RLOBe:FREQuency

                    Arguments: 1
                    """

                RLOBe = RLOBe()  # type: ignore
                """
                SOURce:ILS:LOCalizer:RLOBe

                Arguments:
                """

                class SODepth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:LOCalizer:SODepth

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "SODepth"
                    args = ["1"]

                SODepth = SODepth()  # type: ignore
                """
                SOURce:ILS:LOCalizer:SODepth

                Arguments: 1
                """

            LOCalizer = LOCalizer()  # type: ignore
            """
            SOURce:ILS:LOCalizer

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:ILS:SOURce

                Arguments: INT2, INTernal2,EXTernal
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["INT2", "INTernal2,EXTernal"]

            SOURce = SOURce()  # type: ignore
            """
            SOURce:ILS:SOURce

            Arguments: INT2, INTernal2,EXTernal
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:ILS:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SOURce:ILS:STATe

            Arguments: 1, ON, OFF
            """

        ILS = ILS()  # type: ignore
        """
        SOURce:ILS

        Arguments:
        """

        class LFOutput(SCPINode, SCPISet):
            """
            SOURce:LFOutput

            Arguments:
            """
            __slots__ = ()
            _cmd = "LFOutput"
            args = []  # type: List[str]

            class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:LFOutput:AMPLitude

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "AMPLitude"
                args = ["1"]

            AMPLitude = AMPLitude()  # type: ignore
            """
            SOURce:LFOutput:AMPLitude

            Arguments: 1
            """

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:LFOutput:FREQuency
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/1f6b2dfd7502424e.htm#ID_e2eac03371a347130a00206a013a8948-b48d9b7871a347130a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = ["1"]

            FREQuency = FREQuency()  # type: ignore
            """
            `SOURce:LFOutput:FREQuency
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/1f6b2dfd7502424e.htm#ID_e2eac03371a347130a00206a013a8948-b48d9b7871a347130a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class FUNCtion(SCPINode, SCPISet):
                """
                SOURce:LFOutput:FUNCtion

                Arguments:
                """
                __slots__ = ()
                _cmd = "FUNCtion"
                args = []  # type: List[str]

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:LFOutput:FUNCtion:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                    class ALTernate(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:LFOutput:FUNCtion:FREQuency:ALTernate

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "ALTernate"
                        args = ["1"]

                        class AMPLitude(SCPINode, SCPISet):
                            """
                            SOURce:LFOutput:FUNCtion:FREQuency:ALTernate:AMPLitude

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "AMPLitude"
                            args = []  # type: List[str]

                            class PERCent(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:LFOutput:FUNCtion:FREQuency:ALTernate:AMPLitude:PERCent

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "PERCent"
                                args = ["1"]

                            PERCent = PERCent()  # type: ignore
                            """
                            SOURce:LFOutput:FUNCtion:FREQuency:ALTernate:AMPLitude:PERCent

                            Arguments: 1
                            """

                        AMPLitude = AMPLitude()  # type: ignore
                        """
                        SOURce:LFOutput:FUNCtion:FREQuency:ALTernate:AMPLitude

                        Arguments:
                        """

                    ALTernate = ALTernate()  # type: ignore
                    """
                    SOURce:LFOutput:FUNCtion:FREQuency:ALTernate

                    Arguments: 1
                    """

                    class STEP(SCPINode):
                        """
                        SOURce:LFOutput:FUNCtion:FREQuency:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:LFOutput:FUNCtion:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:LFOutput:FUNCtion:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:LFOutput:FUNCtion:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:LFOutput:FUNCtion:FREQuency

                Arguments: 1
                """

                class PERiod(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:LFOutput:FUNCtion:PERiod

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PERiod"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:LFOutput:FUNCtion:PERiod:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:LFOutput:FUNCtion:PERiod:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:LFOutput:FUNCtion:PERiod:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:LFOutput:FUNCtion:PERiod:STEP

                    Arguments:
                    """

                PERiod = PERiod()  # type: ignore
                """
                SOURce:LFOutput:FUNCtion:PERiod

                Arguments: 1
                """

                class PWIDth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:LFOutput:FUNCtion:PWIDth

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PWIDth"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:LFOutput:FUNCtion:PWIDth:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:LFOutput:FUNCtion:PWIDth:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:LFOutput:FUNCtion:PWIDth:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:LFOutput:FUNCtion:PWIDth:STEP

                    Arguments:
                    """

                PWIDth = PWIDth()  # type: ignore
                """
                SOURce:LFOutput:FUNCtion:PWIDth

                Arguments: 1
                """

                class SHAPe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:LFOutput:FUNCtion:SHAPe

                    Arguments: DUALsine, NOISe, RAMP, SINE, SQUare, SWEPtsine, TRIangle
                    """
                    __slots__ = ()
                    _cmd = "SHAPe"
                    args = ["DUALsine", "NOISe", "RAMP", "SINE", "SQUare", "SWEPtsine", "TRIangle"]

                    class NOISe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:LFOutput:FUNCtion:SHAPe:NOISe

                        Arguments: GAUSsian, UNIForm
                        """
                        __slots__ = ()
                        _cmd = "NOISe"
                        args = ["GAUSsian", "UNIForm"]

                    NOISe = NOISe()  # type: ignore
                    """
                    SOURce:LFOutput:FUNCtion:SHAPe:NOISe

                    Arguments: GAUSsian, UNIForm
                    """

                SHAPe = SHAPe()  # type: ignore
                """
                SOURce:LFOutput:FUNCtion:SHAPe

                Arguments: DUALsine, NOISe, RAMP, SINE, SQUare, SWEPtsine, TRIangle
                """

                class SWEep(SCPINode, SCPISet):
                    """
                    SOURce:LFOutput:FUNCtion:SWEep

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SWEep"
                    args = []  # type: List[str]

                    class TRIGger(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:LFOutput:FUNCtion:SWEep:TRIGger

                        Arguments: BUS, EXTernal, IMMediate, KEY
                        """
                        __slots__ = ()
                        _cmd = "TRIGger"
                        args = ["BUS", "EXTernal", "IMMediate", "KEY"]

                    TRIGger = TRIGger()  # type: ignore
                    """
                    SOURce:LFOutput:FUNCtion:SWEep:TRIGger

                    Arguments: BUS, EXTernal, IMMediate, KEY
                    """

                SWEep = SWEep()  # type: ignore
                """
                SOURce:LFOutput:FUNCtion:SWEep

                Arguments:
                """

            FUNCtion = FUNCtion()  # type: ignore
            """
            SOURce:LFOutput:FUNCtion

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:LFOutput:SOURce

                Arguments: FUNC1, FUNC2, FUNCtion1, FUNCtion2, INT1, INT2, INTernal, INTernal1, INTernal2
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["FUNC1", "FUNC2", "FUNCtion1", "FUNCtion2", "INT1", "INT2", "INTernal", "INTernal1", "INTernal2"]

            SOURce = SOURce()  # type: ignore
            """
            SOURce:LFOutput:SOURce

            Arguments: FUNC1, FUNC2, FUNCtion1, FUNCtion2, INT1, INT2, INTernal, INTernal1, INTernal2
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SOURce:LFOutput:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/9aa195c42bb647c7.htm#ID_5a5d63ab71a330bc0a00206a000cda4d-1617947971a330bc0a00206a012bc823-en-US>`_

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            `SOURce:LFOutput:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/9aa195c42bb647c7.htm#ID_5a5d63ab71a330bc0a00206a000cda4d-1617947971a330bc0a00206a012bc823-en-US>`_

            Arguments: 1, ON, OFF
            """

            class VOLTage(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:LFOutput:VOLTage
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/30f4a928cfb244ff.htm#ID_0aac7ff171a373a10a00206a0151df63-2edc927371a373a10a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "VOLTage"
                args = ["1"]

            VOLTage = VOLTage()  # type: ignore
            """
            `SOURce:LFOutput:VOLTage
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/30f4a928cfb244ff.htm#ID_0aac7ff171a373a10a00206a0151df63-2edc927371a373a10a00206a012bc823-en-US>`_

            Arguments: 1
            """

        LFOutput = LFOutput()  # type: ignore
        """
        SOURce:LFOutput

        Arguments:
        """

        class LIST(SCPINode, SCPISet):
            """
            SOURce:LIST

            Arguments:
            """
            __slots__ = ()
            _cmd = "LIST"
            args = []  # type: List[str]

            class CALCulate(SCPINode, SCPISet):
                """
                SOURce:LIST:CALCulate

                Arguments:
                """
                __slots__ = ()
                _cmd = "CALCulate"
                args = []  # type: List[str]

            CALCulate = CALCulate()  # type: ignore
            """
            SOURce:LIST:CALCulate

            Arguments:
            """

            class CATalog(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:LIST:CATalog
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/16c72e3030b147e1.htm#ID_3069dbd57ba2f03b0a00206a00039550-48dc81507ba2f03b0a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "CATalog"
                args = []  # type: List[str]

            CATalog = CATalog()  # type: ignore
            """
            `SOURce:LIST:CATalog
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/16c72e3030b147e1.htm#ID_3069dbd57ba2f03b0a00206a00039550-48dc81507ba2f03b0a00206a012bc823-en-US>`_

            Arguments:
            """

            class CPOint(SCPINode, SCPIQuery):
                """
                SOURce:LIST:CPOint

                Arguments:
                """
                __slots__ = ()
                _cmd = "CPOint"
                args = []  # type: List[str]

            CPOint = CPOint()  # type: ignore
            """
            SOURce:LIST:CPOint

            Arguments:
            """

            class DELete(SCPINode, SCPISet):
                """
                `SOURce:LIST:DELete
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/478634d2f1c14f74.htm#ID_624d744a7ba2f6c20a00206a00fc6ced-3ec734647ba2f6c20a00206a012bc823-en-US>`_

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "DELete"
                args = ["'string'"]

            DELete = DELete()  # type: ignore
            """
            `SOURce:LIST:DELete
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/478634d2f1c14f74.htm#ID_624d744a7ba2f6c20a00206a00fc6ced-3ec734647ba2f6c20a00206a012bc823-en-US>`_

            Arguments: 'string'
            """

            class DIRection(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:LIST:DIRection

                Arguments: DOWN, UP
                """
                __slots__ = ()
                _cmd = "DIRection"
                args = ["DOWN", "UP"]

            DIRection = DIRection()  # type: ignore
            """
            SOURce:LIST:DIRection

            Arguments: DOWN, UP
            """

            class DWELl(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:LIST:DWELl
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/22311a6bdb404393.htm#ID_517045367ba322280a00206a0147be12-14458ec47ba322280a00206a012bc823-en-US>`_

                Arguments: <numeric_value>[S, MS, US, NS],<numeric_value>
                """
                __slots__ = ()
                _cmd = "DWELl"
                args = ["<numeric_value>[S", "MS", "US", "NS],<numeric_value>"]

                class POINts(SCPINode, SCPIQuery):
                    """
                    SOURce:LIST:DWELl:POINts

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "POINts"
                    args = []  # type: List[str]

                POINts = POINts()  # type: ignore
                """
                SOURce:LIST:DWELl:POINts

                Arguments:
                """

            DWELl = DWELl()  # type: ignore
            """
            `SOURce:LIST:DWELl
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/22311a6bdb404393.htm#ID_517045367ba322280a00206a0147be12-14458ec47ba322280a00206a012bc823-en-US>`_

            Arguments: <numeric_value>[S, MS, US, NS],<numeric_value>
            """

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:LIST:FREQuency
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f90eaa236ece4248.htm#ID_c9bf26237ba301cf0a00206a00e0ce9e-37a02b557ba301cf0a00206a012bc823-en-US>`_

                Arguments: <numeric_value>[HZ, KHZ, MHZ, GHZ],<numeric_value>
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = ["<numeric_value>[HZ", "KHZ", "MHZ", "GHZ],<numeric_value>"]

                class POINts(SCPINode, SCPIQuery):
                    """
                    `SOURce:LIST:FREQuency:POINts
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7d65b1dd057049b7.htm#ID_b69a536c7ba3073d0a00206a000d2789-99c66bd67ba3073d0a00206a012bc823-en-US>`_

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "POINts"
                    args = []  # type: List[str]

                POINts = POINts()  # type: ignore
                """
                `SOURce:LIST:FREQuency:POINts
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7d65b1dd057049b7.htm#ID_b69a536c7ba3073d0a00206a000d2789-99c66bd67ba3073d0a00206a012bc823-en-US>`_

                Arguments:
                """

            FREQuency = FREQuency()  # type: ignore
            """
            `SOURce:LIST:FREQuency
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f90eaa236ece4248.htm#ID_c9bf26237ba301cf0a00206a00e0ce9e-37a02b557ba301cf0a00206a012bc823-en-US>`_

            Arguments: <numeric_value>[HZ, KHZ, MHZ, GHZ],<numeric_value>
            """

            class INDex(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:LIST:INDex
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/868b396a40754ba2.htm#ID_067dfbf58c3062130a00206a00010bd5-6df2da598c3062130a00206a00aff702-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "INDex"
                args = ["1"]

            INDex = INDex()  # type: ignore
            """
            `SOURce:LIST:INDex
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/868b396a40754ba2.htm#ID_067dfbf58c3062130a00206a00010bd5-6df2da598c3062130a00206a00aff702-en-US>`_

            Arguments: 1
            """

            class LEARn(SCPINode, SCPISet):
                """
                `SOURce:LIST:LEARn
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/df51bebecca046fc.htm#ID_7e28763e7ba327a60a00206a019a9399-eebba4977ba327a60a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "LEARn"
                args = []  # type: List[str]

            LEARn = LEARn()  # type: ignore
            """
            `SOURce:LIST:LEARn
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/df51bebecca046fc.htm#ID_7e28763e7ba327a60a00206a019a9399-eebba4977ba327a60a00206a012bc823-en-US>`_

            Arguments:
            """

            class MANual(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:LIST:MANual

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "MANual"
                args = ["1"]

            MANual = MANual()  # type: ignore
            """
            SOURce:LIST:MANual

            Arguments: 1
            """

            class POWer(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:LIST:POWer
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0fb4c8f885b74436.htm#ID_f9c5b80f7ba311fb0a00206a00e2155d-e913c2b67ba311fb0a00206a012bc823-en-US>`_

                Arguments: <numeric_value>[DB],<numeric_value>
                """
                __slots__ = ()
                _cmd = "POWer"
                args = ["<numeric_value>[DB],<numeric_value>"]

                class CORRection(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:LIST:POWer:CORRection

                    Arguments: <numeric_value>[DB],<numeric_value>
                    """
                    __slots__ = ()
                    _cmd = "CORRection"
                    args = ["<numeric_value>[DB],<numeric_value>"]

                    class POINts(SCPINode, SCPIQuery):
                        """
                        SOURce:LIST:POWer:CORRection:POINts

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "POINts"
                        args = []  # type: List[str]

                    POINts = POINts()  # type: ignore
                    """
                    SOURce:LIST:POWer:CORRection:POINts

                    Arguments:
                    """

                CORRection = CORRection()  # type: ignore
                """
                SOURce:LIST:POWer:CORRection

                Arguments: <numeric_value>[DB],<numeric_value>
                """

                class POINts(SCPINode, SCPIQuery):
                    """
                    `SOURce:LIST:POWer:POINts
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f55e6d6622054b99.htm#ID_0ad5bbbe7ba30c8d0a00206a002bb3bd-db2157e07ba30c8d0a00206a012bc823-en-US>`_

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "POINts"
                    args = []  # type: List[str]

                POINts = POINts()  # type: ignore
                """
                `SOURce:LIST:POWer:POINts
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f55e6d6622054b99.htm#ID_0ad5bbbe7ba30c8d0a00206a002bb3bd-db2157e07ba30c8d0a00206a012bc823-en-US>`_

                Arguments:
                """

            POWer = POWer()  # type: ignore
            """
            `SOURce:LIST:POWer
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0fb4c8f885b74436.htm#ID_f9c5b80f7ba311fb0a00206a00e2155d-e913c2b67ba311fb0a00206a012bc823-en-US>`_

            Arguments: <numeric_value>[DB],<numeric_value>
            """

            class RETRace(SCPINode, SCPIBool):
                """
                SOURce:LIST:RETRace

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "RETRace"
                args = ["1", "ON", "OFF"]

            RETRace = RETRace()  # type: ignore
            """
            SOURce:LIST:RETRace

            Arguments: 1, ON, OFF
            """

            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:LIST:SELect
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bb14b349e79e40dc.htm#ID_e5b35aa57ba31ca90a00206a01b8b53b-2962634e7ba31ca90a00206a012bc823-en-US>`_

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "SELect"
                args = ["'string'"]

            SELect = SELect()  # type: ignore
            """
            `SOURce:LIST:SELect
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bb14b349e79e40dc.htm#ID_e5b35aa57ba31ca90a00206a01b8b53b-2962634e7ba31ca90a00206a012bc823-en-US>`_

            Arguments: 'string'
            """

            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:LIST:STARt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()  # type: ignore
            """
            SOURce:LIST:STARt

            Arguments: 1
            """

            class TRIGger(SCPINode, SCPISet):
                """
                SOURce:LIST:TRIGger

                Arguments:
                """
                __slots__ = ()
                _cmd = "TRIGger"
                args = []  # type: List[str]

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:LIST:TRIGger:SOURce
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/c1a4677a84944212.htm#ID_e26ff7bb7ba338dc0a00206a01f83843-c7753eb97ba338dc0a00206a012bc823-en-US>`_

                    Arguments: BUS, EXTernal, IMMediate, KEY
                    """
                    __slots__ = ()
                    _cmd = "SOURce"
                    args = ["BUS", "EXTernal", "IMMediate", "KEY"]

                SOURce = SOURce()  # type: ignore
                """
                `SOURce:LIST:TRIGger:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/c1a4677a84944212.htm#ID_e26ff7bb7ba338dc0a00206a01f83843-c7753eb97ba338dc0a00206a012bc823-en-US>`_

                Arguments: BUS, EXTernal, IMMediate, KEY
                """

            TRIGger = TRIGger()  # type: ignore
            """
            SOURce:LIST:TRIGger

            Arguments:
            """

            class TYPE(SCPINode):
                """
                SOURce:LIST:TYPE

                Arguments:
                """
                __slots__ = ()
                _cmd = "TYPE"
                args = []  # type: List[str]

                class LIST(SCPINode):
                    """
                    SOURce:LIST:TYPE:LIST

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "LIST"
                    args = []  # type: List[str]

                    class INITialize(SCPINode, SCPISet):
                        """
                        SOURce:LIST:TYPE:LIST:INITialize

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "INITialize"
                        args = []  # type: List[str]

                        class FSTep(SCPINode, SCPISet):
                            """
                            SOURce:LIST:TYPE:LIST:INITialize:FSTep

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "FSTep"
                            args = []  # type: List[str]

                        FSTep = FSTep()  # type: ignore
                        """
                        SOURce:LIST:TYPE:LIST:INITialize:FSTep

                        Arguments:
                        """

                        class PRESet(SCPINode, SCPISet):
                            """
                            SOURce:LIST:TYPE:LIST:INITialize:PRESet

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "PRESet"
                            args = []  # type: List[str]

                        PRESet = PRESet()  # type: ignore
                        """
                        SOURce:LIST:TYPE:LIST:INITialize:PRESet

                        Arguments:
                        """

                    INITialize = INITialize()  # type: ignore
                    """
                    SOURce:LIST:TYPE:LIST:INITialize

                    Arguments:
                    """

                LIST = LIST()  # type: ignore
                """
                SOURce:LIST:TYPE:LIST

                Arguments:
                """

            TYPE = TYPE()  # type: ignore
            """
            SOURce:LIST:TYPE

            Arguments:
            """

        LIST = LIST()  # type: ignore
        """
        SOURce:LIST

        Arguments:
        """

        class MARKer(SCPINodeN, SCPISet):
            """
            SOURce:MARKer

            Arguments:
            """
            __slots__ = ()
            _cmd = "MARKer"
            args = []  # type: List[str]

            class AMPLitude(SCPINode):
                """
                SOURce:MARKer:AMPLitude

                Arguments:
                """
                __slots__ = ()
                _cmd = "AMPLitude"
                args = []  # type: List[str]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:MARKer:AMPLitude:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:MARKer:AMPLitude:STATe

                Arguments: 1, ON, OFF
                """

                class VALue(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MARKer:AMPLitude:VALue

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "VALue"
                    args = ["1"]

                VALue = VALue()  # type: ignore
                """
                SOURce:MARKer:AMPLitude:VALue

                Arguments: 1
                """

            AMPLitude = AMPLitude()  # type: ignore
            """
            SOURce:MARKer:AMPLitude

            Arguments:
            """

            class DELTa(SCPINode, SCPIQuery):
                """
                SOURce:MARKer:DELTa

                Arguments: <numeric_value>,<numeric_value>
                """
                __slots__ = ()
                _cmd = "DELTa"
                args = ["<numeric_value>,<numeric_value>"]

            DELTa = DELTa()  # type: ignore
            """
            SOURce:MARKer:DELTa

            Arguments: <numeric_value>,<numeric_value>
            """

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:MARKer:FREQuency

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:MARKer:FREQuency:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:MARKer:FREQuency:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:MARKer:FREQuency:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:MARKer:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()  # type: ignore
            """
            SOURce:MARKer:FREQuency

            Arguments: 1
            """

            class FSWeep(SCPINode):
                """
                SOURce:MARKer:FSWeep

                Arguments:
                """
                __slots__ = ()
                _cmd = "FSWeep"
                args = []  # type: List[str]

                class AMPLitude(SCPINode, SCPIBool):
                    """
                    SOURce:MARKer:FSWeep:AMPLitude

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "AMPLitude"
                    args = ["1", "ON", "OFF"]

                AMPLitude = AMPLitude()  # type: ignore
                """
                SOURce:MARKer:FSWeep:AMPLitude

                Arguments: 1, ON, OFF
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MARKer:FSWeep:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:MARKer:FSWeep:FREQuency

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:MARKer:FSWeep:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:MARKer:FSWeep:STATe

                Arguments: 1, ON, OFF
                """

            FSWeep = FSWeep()  # type: ignore
            """
            SOURce:MARKer:FSWeep

            Arguments:
            """

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:MARKer:POLarity

                Arguments: NEGative, POSitive
                """
                __slots__ = ()
                _cmd = "POLarity"
                args = ["NEGative", "POSitive"]

            POLarity = POLarity()  # type: ignore
            """
            SOURce:MARKer:POLarity

            Arguments: NEGative, POSitive
            """

            class PSWeep(SCPINode):
                """
                SOURce:MARKer:PSWeep

                Arguments:
                """
                __slots__ = ()
                _cmd = "PSWeep"
                args = []  # type: List[str]

                class POWer(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MARKer:PSWeep:POWer

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "POWer"
                    args = ["1"]

                POWer = POWer()  # type: ignore
                """
                SOURce:MARKer:PSWeep:POWer

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:MARKer:PSWeep:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:MARKer:PSWeep:STATe

                Arguments: 1, ON, OFF
                """

            PSWeep = PSWeep()  # type: ignore
            """
            SOURce:MARKer:PSWeep

            Arguments:
            """

            class REFerence(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:MARKer:REFerence

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "REFerence"
                args = ["1"]

            REFerence = REFerence()  # type: ignore
            """
            SOURce:MARKer:REFerence

            Arguments: 1
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:MARKer:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SOURce:MARKer:STATe

            Arguments: 1, ON, OFF
            """

            class VIDeo(SCPINode, SCPIBool):
                """
                SOURce:MARKer:VIDeo

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "VIDeo"
                args = ["1", "ON", "OFF"]

            VIDeo = VIDeo()  # type: ignore
            """
            SOURce:MARKer:VIDeo

            Arguments: 1, ON, OFF
            """

        MARKer = MARKer()  # type: ignore
        """
        SOURce:MARKer

        Arguments:
        """

        class MBEacon(SCPINode):
            """
            SOURce:MBEacon

            Arguments:
            """
            __slots__ = ()
            _cmd = "MBEacon"
            args = []  # type: List[str]

            class COMid(SCPINode):
                """
                SOURce:MBEacon:COMid

                Arguments:
                """
                __slots__ = ()
                _cmd = "COMid"
                args = []  # type: List[str]

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MBEacon:COMid:DEPTh

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()  # type: ignore
                """
                SOURce:MBEacon:COMid:DEPTh

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MBEacon:COMid:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:MBEacon:COMid:FREQuency

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:MBEacon:COMid:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:MBEacon:COMid:STATe

                Arguments: 1, ON, OFF
                """

            COMid = COMid()  # type: ignore
            """
            SOURce:MBEacon:COMid

            Arguments:
            """

            class MARKer(SCPINode):
                """
                SOURce:MBEacon:MARKer

                Arguments:
                """
                __slots__ = ()
                _cmd = "MARKer"
                args = []  # type: List[str]

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MBEacon:MARKer:DEPTh

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()  # type: ignore
                """
                SOURce:MBEacon:MARKer:DEPTh

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MBEacon:MARKer:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:MBEacon:MARKer:FREQuency

                Arguments: 1
                """

            MARKer = MARKer()  # type: ignore
            """
            SOURce:MBEacon:MARKer

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:MBEacon:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SOURce:MBEacon:STATe

            Arguments: 1, ON, OFF
            """

        MBEacon = MBEacon()  # type: ignore
        """
        SOURce:MBEacon

        Arguments:
        """

        class MODulation(SCPINode):
            """
            SOURce:MODulation

            Arguments:
            """
            __slots__ = ()
            _cmd = "MODulation"
            args = []  # type: List[str]

            class ALL(SCPINode):
                """
                SOURce:MODulation:ALL

                Arguments:
                """
                __slots__ = ()
                _cmd = "ALL"
                args = []  # type: List[str]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:MODulation:ALL:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7b63a3602aec41cd.htm#ID_318e32e54e9063210a00206a019f179a-19a855954e9063210a00206a0024546d-en-US>`_

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                `SOURce:MODulation:ALL:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7b63a3602aec41cd.htm#ID_318e32e54e9063210a00206a019f179a-19a855954e9063210a00206a0024546d-en-US>`_

                Arguments: 1, ON, OFF
                """

            ALL = ALL()  # type: ignore
            """
            SOURce:MODulation:ALL

            Arguments:
            """

            class OUTPut(SCPINode):
                """
                SOURce:MODulation:OUTPut

                Arguments:
                """
                __slots__ = ()
                _cmd = "OUTPut"
                args = []  # type: List[str]

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MODulation:OUTPut:SOURce

                    Arguments: AM, FM, OFF
                    """
                    __slots__ = ()
                    _cmd = "SOURce"
                    args = ["AM", "FM", "OFF"]

                SOURce = SOURce()  # type: ignore
                """
                SOURce:MODulation:OUTPut:SOURce

                Arguments: AM, FM, OFF
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:MODulation:OUTPut:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:MODulation:OUTPut:STATe

                Arguments: 1, ON, OFF
                """

            OUTPut = OUTPut()  # type: ignore
            """
            SOURce:MODulation:OUTPut

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:MODulation:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SOURce:MODulation:STATe

            Arguments: 1, ON, OFF
            """

        MODulation = MODulation()  # type: ignore
        """
        SOURce:MODulation

        Arguments:
        """

        class PHASe(SCPINode, SCPIQuery, SCPISet):
            """
            `SOURce:PHASe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7dee4f9b28a5436d.htm#ID_f61f12ac56ece11f0a00206a00640933-b66d0ab556ece11f0a00206a0024546d-en-US>`_

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "PHASe"
            args = ["1"]

            class ADJust(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PHASe:ADJust

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ADJust"
                args = ["1"]

            ADJust = ADJust()  # type: ignore
            """
            SOURce:PHASe:ADJust

            Arguments: 1
            """

            class REFerence(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:PHASe:REFerence
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7c795407019e4fda.htm#ID_1292e34256ece6dc0a00206a016031df-85318c6056ece6dc0a00206a0024546d-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "REFerence"
                args = []  # type: List[str]

            REFerence = REFerence()  # type: ignore
            """
            `SOURce:PHASe:REFerence
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7c795407019e4fda.htm#ID_1292e34256ece6dc0a00206a016031df-85318c6056ece6dc0a00206a0024546d-en-US>`_

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:PHASe:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SOURce:PHASe:STATe

            Arguments: 1, ON, OFF
            """

        PHASe = PHASe()  # type: ignore
        """
        `SOURce:PHASe
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7dee4f9b28a5436d.htm#ID_f61f12ac56ece11f0a00206a00640933-b66d0ab556ece11f0a00206a0024546d-en-US>`_

        Arguments: 1
        """

        class PM(SCPINode):
            """
            SOURce:PM

            Arguments:
            """
            __slots__ = ()
            _cmd = "PM"
            args = []  # type: List[str]

            class BANDwidth(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PM:BANDwidth

                Arguments: HIGH, NORMal
                """
                __slots__ = ()
                _cmd = "BANDwidth"
                args = ["HIGH", "NORMal"]

            BANDwidth = BANDwidth()  # type: ignore
            """
            SOURce:PM:BANDwidth

            Arguments: HIGH, NORMal
            """

            class BWIDth(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PM:BWIDth

                Arguments: HIGH, NORMal
                """
                __slots__ = ()
                _cmd = "BWIDth"
                args = ["HIGH", "NORMal"]

            BWIDth = BWIDth()  # type: ignore
            """
            SOURce:PM:BWIDth

            Arguments: HIGH, NORMal
            """

            class COUPling(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PM:COUPling

                Arguments: AC, DC
                """
                __slots__ = ()
                _cmd = "COUPling"
                args = ["AC", "DC"]

            COUPling = COUPling()  # type: ignore
            """
            SOURce:PM:COUPling

            Arguments: AC, DC
            """

            class DEViation(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:PM:DEViation
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b1129cdf10fc4d18.htm#ID_aac994794dfe968f0a00206a003ca3de-036e27e84dfe968f0a00206a0024546d-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DEViation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:PM:DEViation:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PM:DEViation:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:PM:DEViation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:PM:DEViation:STEP

                Arguments:
                """

                class TRACk(SCPINode, SCPIBool):
                    """
                    SOURce:PM:DEViation:TRACk

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "TRACk"
                    args = ["1", "ON", "OFF"]

                TRACk = TRACk()  # type: ignore
                """
                SOURce:PM:DEViation:TRACk

                Arguments: 1, ON, OFF
                """

            DEViation = DEViation()  # type: ignore
            """
            `SOURce:PM:DEViation
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b1129cdf10fc4d18.htm#ID_aac994794dfe968f0a00206a003ca3de-036e27e84dfe968f0a00206a0024546d-en-US>`_

            Arguments: 1
            """

            class EXTernal(SCPINode, SCPISet):
                """
                SOURce:PM:EXTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "EXTernal"
                args = []  # type: List[str]

                class COUPling(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:PM:EXTernal:COUPling
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/106b9eba3c704c91.htm#ID_2eca06d94dff07b70a00206a00e7db83-29ccec014dff07b70a00206a0024546d-en-US>`_

                    Arguments: AC, DC
                    """
                    __slots__ = ()
                    _cmd = "COUPling"
                    args = ["AC", "DC"]

                COUPling = COUPling()  # type: ignore
                """
                `SOURce:PM:EXTernal:COUPling
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/106b9eba3c704c91.htm#ID_2eca06d94dff07b70a00206a00e7db83-29ccec014dff07b70a00206a0024546d-en-US>`_

                Arguments: AC, DC
                """

                class IMPedance(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PM:EXTernal:IMPedance

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()  # type: ignore
                """
                SOURce:PM:EXTernal:IMPedance

                Arguments: 1
                """

            EXTernal = EXTernal()  # type: ignore
            """
            SOURce:PM:EXTernal

            Arguments:
            """

            class INTernal(SCPINode, SCPISet):
                """
                SOURce:PM:INTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "INTernal"
                args = []  # type: List[str]

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PM:INTernal:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                    class ALTernate(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PM:INTernal:FREQuency:ALTernate

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "ALTernate"
                        args = ["1"]

                        class AMPLitude(SCPINode, SCPISet):
                            """
                            SOURce:PM:INTernal:FREQuency:ALTernate:AMPLitude

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "AMPLitude"
                            args = []  # type: List[str]

                            class PERCent(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:PM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "PERCent"
                                args = ["1"]

                            PERCent = PERCent()  # type: ignore
                            """
                            SOURce:PM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                            Arguments: 1
                            """

                        AMPLitude = AMPLitude()  # type: ignore
                        """
                        SOURce:PM:INTernal:FREQuency:ALTernate:AMPLitude

                        Arguments:
                        """

                    ALTernate = ALTernate()  # type: ignore
                    """
                    SOURce:PM:INTernal:FREQuency:ALTernate

                    Arguments: 1
                    """

                    class STEP(SCPINode):
                        """
                        SOURce:PM:INTernal:FREQuency:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PM:INTernal:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:PM:INTernal:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:PM:INTernal:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:PM:INTernal:FREQuency

                Arguments: 1
                """

                class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PM:INTernal:FUNCtion

                    Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                    """
                    __slots__ = ()
                    _cmd = "FUNCtion"
                    args = ["GAUSsian", "NOISe", "RAMP", "SINusoid", "SQUare", "TRIangle", "UNIForm"]

                    class NOISe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PM:INTernal:FUNCtion:NOISe

                        Arguments: GAUSsian, UNIForm
                        """
                        __slots__ = ()
                        _cmd = "NOISe"
                        args = ["GAUSsian", "UNIForm"]

                    NOISe = NOISe()  # type: ignore
                    """
                    SOURce:PM:INTernal:FUNCtion:NOISe

                    Arguments: GAUSsian, UNIForm
                    """

                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PM:INTernal:FUNCtion:SHAPe

                        Arguments: SINE, SQUare
                        """
                        __slots__ = ()
                        _cmd = "SHAPe"
                        args = ["SINE", "SQUare"]

                    SHAPe = SHAPe()  # type: ignore
                    """
                    SOURce:PM:INTernal:FUNCtion:SHAPe

                    Arguments: SINE, SQUare
                    """

                FUNCtion = FUNCtion()  # type: ignore
                """
                SOURce:PM:INTernal:FUNCtion

                Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                """

                class SWEep(SCPINode, SCPISet):
                    """
                    SOURce:PM:INTernal:SWEep

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SWEep"
                    args = []  # type: List[str]

                    class TRIGger(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PM:INTernal:SWEep:TRIGger

                        Arguments: BUS, EXTernal, IMMediate, KEY
                        """
                        __slots__ = ()
                        _cmd = "TRIGger"
                        args = ["BUS", "EXTernal", "IMMediate", "KEY"]

                    TRIGger = TRIGger()  # type: ignore
                    """
                    SOURce:PM:INTernal:SWEep:TRIGger

                    Arguments: BUS, EXTernal, IMMediate, KEY
                    """

                SWEep = SWEep()  # type: ignore
                """
                SOURce:PM:INTernal:SWEep

                Arguments:
                """

            INTernal = INTernal()  # type: ignore
            """
            SOURce:PM:INTernal

            Arguments:
            """

            class RANGe(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PM:RANGe

                Arguments: AUTO, HIGH, LOW
                """
                __slots__ = ()
                _cmd = "RANGe"
                args = ["AUTO", "HIGH", "LOW"]

            RANGe = RANGe()  # type: ignore
            """
            SOURce:PM:RANGe

            Arguments: AUTO, HIGH, LOW
            """

            class SENSitivity(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:PM:SENSitivity
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5836d526cac145e7.htm#ID_27fa42664dfef8a40a00206a01c64dd3-a9c7bda04dfef8a40a00206a0024546d-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "SENSitivity"
                args = ["1"]

            SENSitivity = SENSitivity()  # type: ignore
            """
            `SOURce:PM:SENSitivity
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5836d526cac145e7.htm#ID_27fa42664dfef8a40a00206a01c64dd3-a9c7bda04dfef8a40a00206a0024546d-en-US>`_

            Arguments: 1
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:PM:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a5eea8bb9ea4432a.htm#ID_a38f265d4dff00540a00206a0075b5cb-63121be24dff00540a00206a0024546d-en-US>`_

                Arguments: EXTernal, INT1, INT2, INTernal, INTernal1, INTernal2,EXTernal, INT1, INTernal, INTernal1
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["EXTernal", "INT1", "INT2", "INTernal", "INTernal1", "INTernal2,EXTernal", "INT1", "INTernal", "INTernal1"]

            SOURce = SOURce()  # type: ignore
            """
            `SOURce:PM:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a5eea8bb9ea4432a.htm#ID_a38f265d4dff00540a00206a0075b5cb-63121be24dff00540a00206a0024546d-en-US>`_

            Arguments: EXTernal, INT1, INT2, INTernal, INTernal1, INTernal2,EXTernal, INT1, INTernal, INTernal1
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SOURce:PM:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/ae557ed7d4cc4881.htm#ID_26e0edd44dff16ba0a00206a009af85a-2b5c07604dff16ba0a00206a0024546d-en-US>`_

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            `SOURce:PM:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/ae557ed7d4cc4881.htm#ID_26e0edd44dff16ba0a00206a009af85a-2b5c07604dff16ba0a00206a0024546d-en-US>`_

            Arguments: 1, ON, OFF
            """

        PM = PM()  # type: ignore
        """
        SOURce:PM

        Arguments:
        """

        class POWer(SCPINode):
            """
            SOURce:POWer

            Arguments:
            """
            __slots__ = ()
            _cmd = "POWer"
            args = []  # type: List[str]

            class ALC(SCPINode):
                """
                SOURce:POWer:ALC

                Arguments:
                """
                __slots__ = ()
                _cmd = "ALC"
                args = []  # type: List[str]

                class BANDwidth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:BANDwidth

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "BANDwidth"
                    args = ["1"]

                BANDwidth = BANDwidth()  # type: ignore
                """
                SOURce:POWer:ALC:BANDwidth

                Arguments: 1
                """

                class BWIDth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:BWIDth

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "BWIDth"
                    args = ["1"]

                BWIDth = BWIDth()  # type: ignore
                """
                SOURce:POWer:ALC:BWIDth

                Arguments: 1
                """

                class CFACtor(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:CFACtor

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "CFACtor"
                    args = ["1"]

                CFACtor = CFACtor()  # type: ignore
                """
                SOURce:POWer:ALC:CFACtor

                Arguments: 1
                """

                class LEVel(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:LEVel

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "LEVel"
                    args = ["1"]

                LEVel = LEVel()  # type: ignore
                """
                SOURce:POWer:ALC:LEVel

                Arguments: 1
                """

                class PMETer(SCPINode):
                    """
                    SOURce:POWer:ALC:PMETer

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "PMETer"
                    args = []  # type: List[str]

                    class LEVel(SCPINode):
                        """
                        SOURce:POWer:ALC:PMETer:LEVel

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "LEVel"
                        args = []  # type: List[str]

                        class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:ALC:PMETer:LEVel:AMPLitude

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "AMPLitude"
                            args = ["1"]

                        AMPLitude = AMPLitude()  # type: ignore
                        """
                        SOURce:POWer:ALC:PMETer:LEVel:AMPLitude

                        Arguments: 1
                        """

                        class STEP(SCPINode):
                            """
                            SOURce:POWer:ALC:PMETer:LEVel:STEP

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "STEP"
                            args = []  # type: List[str]

                            class INCRement(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:POWer:ALC:PMETer:LEVel:STEP:INCRement

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "INCRement"
                                args = ["1"]

                            INCRement = INCRement()  # type: ignore
                            """
                            SOURce:POWer:ALC:PMETer:LEVel:STEP:INCRement

                            Arguments: 1
                            """

                        STEP = STEP()  # type: ignore
                        """
                        SOURce:POWer:ALC:PMETer:LEVel:STEP

                        Arguments:
                        """

                    LEVel = LEVel()  # type: ignore
                    """
                    SOURce:POWer:ALC:PMETer:LEVel

                    Arguments:
                    """

                PMETer = PMETer()  # type: ignore
                """
                SOURce:POWer:ALC:PMETer

                Arguments:
                """

                class REFerence(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:REFerence

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "REFerence"
                    args = ["1"]

                REFerence = REFerence()  # type: ignore
                """
                SOURce:POWer:ALC:REFerence

                Arguments: 1
                """

                class SEARch(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:SEARch

                    Arguments: <boolean>, ONCE
                    """
                    __slots__ = ()
                    _cmd = "SEARch"
                    args = ["<boolean>", "ONCE"]

                    class REFerence(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:ALC:SEARch:REFerence

                        Arguments: FIXed, MODulated
                        """
                        __slots__ = ()
                        _cmd = "REFerence"
                        args = ["FIXed", "MODulated"]

                    REFerence = REFerence()  # type: ignore
                    """
                    SOURce:POWer:ALC:SEARch:REFerence

                    Arguments: FIXed, MODulated
                    """

                    class SPAN(SCPINode):
                        """
                        SOURce:POWer:ALC:SEARch:SPAN

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "SPAN"
                        args = []  # type: List[str]

                        class STARt(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:ALC:SEARch:SPAN:STARt

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "STARt"
                            args = ["1"]

                        STARt = STARt()  # type: ignore
                        """
                        SOURce:POWer:ALC:SEARch:SPAN:STARt

                        Arguments: 1
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            SOURce:POWer:ALC:SEARch:SPAN:STATe

                            Arguments: 1, ON, OFF
                            """
                            __slots__ = ()
                            _cmd = "STATe"
                            args = ["1", "ON", "OFF"]

                        STATe = STATe()  # type: ignore
                        """
                        SOURce:POWer:ALC:SEARch:SPAN:STATe

                        Arguments: 1, ON, OFF
                        """

                    SPAN = SPAN()  # type: ignore
                    """
                    SOURce:POWer:ALC:SEARch:SPAN

                    Arguments:
                    """

                SEARch = SEARch()  # type: ignore
                """
                SOURce:POWer:ALC:SEARch

                Arguments: <boolean>, ONCE
                """

                class SLOPe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:SLOPe

                    Arguments: FAST, MEDium, SLOW
                    """
                    __slots__ = ()
                    _cmd = "SLOPe"
                    args = ["FAST", "MEDium", "SLOW"]

                SLOPe = SLOPe()  # type: ignore
                """
                SOURce:POWer:ALC:SLOPe

                Arguments: FAST, MEDium, SLOW
                """

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:SOURce

                    Arguments: DIOD1, DIOD2, DIODe, DIODe1, DIODe2, FIXed, INTernal, PMET1, PMET2, PMETer, PMETer1, PMETer2
                    """
                    __slots__ = ()
                    _cmd = "SOURce"
                    args = ["DIOD1", "DIOD2", "DIODe", "DIODe1", "DIODe2", "FIXed", "INTernal", "PMET1", "PMET2", "PMETer", "PMETer1", "PMETer2"]

                    class EXTernal(SCPINode):
                        """
                        SOURce:POWer:ALC:SOURce:EXTernal

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EXTernal"
                        args = []  # type: List[str]

                        class COUPling(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:ALC:SOURce:EXTernal:COUPling

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "COUPling"
                            args = ["1"]

                        COUPling = COUPling()  # type: ignore
                        """
                        SOURce:POWer:ALC:SOURce:EXTernal:COUPling

                        Arguments: 1
                        """

                    EXTernal = EXTernal()  # type: ignore
                    """
                    SOURce:POWer:ALC:SOURce:EXTernal

                    Arguments:
                    """

                    class PMETer(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:ALC:SOURce:PMETer

                        Arguments: HP436a, RS_Nrvs
                        """
                        __slots__ = ()
                        _cmd = "PMETer"
                        args = ["HP436a", "RS_Nrvs"]

                    PMETer = PMETer()  # type: ignore
                    """
                    SOURce:POWer:ALC:SOURce:PMETer

                    Arguments: HP436a, RS_Nrvs
                    """

                SOURce = SOURce()  # type: ignore
                """
                SOURce:POWer:ALC:SOURce

                Arguments: DIOD1, DIOD2, DIODe, DIODe1, DIODe2, FIXed, INTernal, PMET1, PMET2, PMETer, PMETer1, PMETer2
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:ALC:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/318c26be4c5141e7.htm#ID_42c28bb071aa81480a00206a0127eb9d-881ee75671aa81480a00206a012bc823-en-US>`_

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                `SOURce:POWer:ALC:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/318c26be4c5141e7.htm#ID_42c28bb071aa81480a00206a0127eb9d-881ee75671aa81480a00206a012bc823-en-US>`_

                Arguments: 1, ON, OFF
                """

            ALC = ALC()  # type: ignore
            """
            SOURce:POWer:ALC

            Arguments:
            """

            class ALTernate(SCPINode, SCPISet):
                """
                SOURce:POWer:ALTernate

                Arguments:
                """
                __slots__ = ()
                _cmd = "ALTernate"
                args = []  # type: List[str]

                class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALTernate:AMPLitude

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "AMPLitude"
                    args = ["1"]

                AMPLitude = AMPLitude()  # type: ignore
                """
                SOURce:POWer:ALTernate:AMPLitude

                Arguments: 1
                """

                class MANual(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALTernate:MANual

                    Arguments: DELTa, MAIN
                    """
                    __slots__ = ()
                    _cmd = "MANual"
                    args = ["DELTa", "MAIN"]

                MANual = MANual()  # type: ignore
                """
                SOURce:POWer:ALTernate:MANual

                Arguments: DELTa, MAIN
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:ALTernate:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:POWer:ALTernate:STATe

                Arguments: 1, ON, OFF
                """

                class TRIGger(SCPINode):
                    """
                    SOURce:POWer:ALTernate:TRIGger

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "TRIGger"
                    args = []  # type: List[str]

                    class SOURce(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:ALTernate:TRIGger:SOURce

                        Arguments: EXTernal, INTernal, MANual
                        """
                        __slots__ = ()
                        _cmd = "SOURce"
                        args = ["EXTernal", "INTernal", "MANual"]

                    SOURce = SOURce()  # type: ignore
                    """
                    SOURce:POWer:ALTernate:TRIGger:SOURce

                    Arguments: EXTernal, INTernal, MANual
                    """

                TRIGger = TRIGger()  # type: ignore
                """
                SOURce:POWer:ALTernate:TRIGger

                Arguments:
                """

            ALTernate = ALTernate()  # type: ignore
            """
            SOURce:POWer:ALTernate

            Arguments:
            """

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:ATTenuation

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ATTenuation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:POWer:ATTenuation:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:ATTenuation:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:POWer:ATTenuation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:POWer:ATTenuation:STEP

                Arguments:
                """

            ATTenuation = ATTenuation()  # type: ignore
            """
            SOURce:POWer:ATTenuation

            Arguments: 1
            """

            class CENTer(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:CENTer

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "CENTer"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:POWer:CENTer:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CENTer:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:POWer:CENTer:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:POWer:CENTer:STEP

                Arguments:
                """

            CENTer = CENTer()  # type: ignore
            """
            SOURce:POWer:CENTer

            Arguments: 1
            """

            class DISPlay(SCPINode, SCPISet):
                """
                SOURce:POWer:DISPlay

                Arguments:
                """
                __slots__ = ()
                _cmd = "DISPlay"
                args = []  # type: List[str]

                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:DISPlay:OFFSet

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "OFFSet"
                    args = ["1"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:POWer:DISPlay:OFFSet:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SOURce:POWer:DISPlay:OFFSet:STATe

                    Arguments: 1, ON, OFF
                    """

                OFFSet = OFFSet()  # type: ignore
                """
                SOURce:POWer:DISPlay:OFFSet

                Arguments: 1
                """

            DISPlay = DISPlay()  # type: ignore
            """
            SOURce:POWer:DISPlay

            Arguments:
            """

            class EMF(SCPINode):
                """
                SOURce:POWer:EMF

                Arguments:
                """
                __slots__ = ()
                _cmd = "EMF"
                args = []  # type: List[str]

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:EMF:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5f72d48c013e4e46.htm#ID_6119d3272c6943f20a001ae750554416-95cda6a92c6941fe0a001ae76b46bcda-en-US>`_

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                `SOURce:POWer:EMF:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5f72d48c013e4e46.htm#ID_6119d3272c6943f20a001ae750554416-95cda6a92c6941fe0a001ae76b46bcda-en-US>`_

                Arguments: 1, ON, OFF
                """

            EMF = EMF()  # type: ignore
            """
            SOURce:POWer:EMF

            Arguments:
            """

            class LEVel(SCPINode):
                """
                SOURce:POWer:LEVel

                Arguments:
                """
                __slots__ = ()
                _cmd = "LEVel"
                args = []  # type: List[str]

                class ALTernate(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:LEVel:ALTernate

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ALTernate"
                    args = ["1"]

                ALTernate = ALTernate()  # type: ignore
                """
                SOURce:POWer:LEVel:ALTernate

                Arguments: 1
                """

                class IMMediate(SCPINode):
                    """
                    SOURce:POWer:LEVel:IMMediate

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "IMMediate"
                    args = []  # type: List[str]

                    class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:AMPLitude
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bb5bb606cd4d4681.htm#ID_d70bf25871aa63310a00206a00bc8d87-d732685371aa63310a00206a012bc823-en-US>`_

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "AMPLitude"
                        args = ["1"]

                        class BACKup(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:LEVel:IMMediate:AMPLitude:BACKup

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "BACKup"
                            args = ["1"]

                        BACKup = BACKup()  # type: ignore
                        """
                        SOURce:POWer:LEVel:IMMediate:AMPLitude:BACKup

                        Arguments: 1
                        """

                        class STEP(SCPINode):
                            """
                            SOURce:POWer:LEVel:IMMediate:AMPLitude:STEP

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "STEP"
                            args = []  # type: List[str]

                            class INCRement(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:POWer:LEVel:IMMediate:AMPLitude:STEP:INCRement

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "INCRement"
                                args = ["1"]

                            INCRement = INCRement()  # type: ignore
                            """
                            SOURce:POWer:LEVel:IMMediate:AMPLitude:STEP:INCRement

                            Arguments: 1
                            """

                        STEP = STEP()  # type: ignore
                        """
                        SOURce:POWer:LEVel:IMMediate:AMPLitude:STEP

                        Arguments:
                        """

                    AMPLitude = AMPLitude()  # type: ignore
                    """
                    `SOURce:POWer:LEVel:IMMediate:AMPLitude
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bb5bb606cd4d4681.htm#ID_d70bf25871aa63310a00206a00bc8d87-d732685371aa63310a00206a012bc823-en-US>`_

                    Arguments: 1
                    """

                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/906418e7a7b84f3c.htm#ID_c493de1471aa6af10a00206a00d83907-a6ae5f2a71aa6af10a00206a012bc823-en-US>`_

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "OFFSet"
                        args = ["1"]

                        class LINear(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:LEVel:IMMediate:OFFSet:LINear

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "LINear"
                            args = ["1"]

                        LINear = LINear()  # type: ignore
                        """
                        SOURce:POWer:LEVel:IMMediate:OFFSet:LINear

                        Arguments: 1
                        """

                        class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:LEVel:IMMediate:OFFSet:LOGarithmic

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "LOGarithmic"
                            args = ["1"]

                        LOGarithmic = LOGarithmic()  # type: ignore
                        """
                        SOURce:POWer:LEVel:IMMediate:OFFSet:LOGarithmic

                        Arguments: 1
                        """

                    OFFSet = OFFSet()  # type: ignore
                    """
                    `SOURce:POWer:LEVel:IMMediate:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/906418e7a7b84f3c.htm#ID_c493de1471aa6af10a00206a00d83907-a6ae5f2a71aa6af10a00206a012bc823-en-US>`_

                    Arguments: 1
                    """

                IMMediate = IMMediate()  # type: ignore
                """
                SOURce:POWer:LEVel:IMMediate

                Arguments:
                """

            LEVel = LEVel()  # type: ignore
            """
            SOURce:POWer:LEVel

            Arguments:
            """

            class LIMit(SCPINode):
                """
                SOURce:POWer:LIMit

                Arguments:
                """
                __slots__ = ()
                _cmd = "LIMit"
                args = []  # type: List[str]

                class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:LIMit:AMPLitude
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/de410925c5dd477b.htm#ID_f38a02d771aa72930a00206a017c0246-a1f79d3e71aa72930a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "AMPLitude"
                    args = ["1"]

                AMPLitude = AMPLitude()  # type: ignore
                """
                `SOURce:POWer:LIMit:AMPLitude
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/de410925c5dd477b.htm#ID_f38a02d771aa72930a00206a017c0246-a1f79d3e71aa72930a00206a012bc823-en-US>`_

                Arguments: 1
                """

            LIMit = LIMit()  # type: ignore
            """
            SOURce:POWer:LIMit

            Arguments:
            """

            class MANual(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:MANual
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b16e4a79adfa47ad.htm#ID_786f132571aaa75e0a00206a003b0637-68a04f6e71aaa75e0a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "MANual"
                args = ["1"]

            MANual = MANual()  # type: ignore
            """
            `SOURce:POWer:MANual
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b16e4a79adfa47ad.htm#ID_786f132571aaa75e0a00206a003b0637-68a04f6e71aaa75e0a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class OFFSet(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:OFFSet

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "OFFSet"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:OFFSet:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:POWer:OFFSet:STATe

                Arguments: 1, ON, OFF
                """

            OFFSet = OFFSet()  # type: ignore
            """
            SOURce:POWer:OFFSet

            Arguments: 1
            """

            class PROTection(SCPINode, SCPIBool):
                """
                SOURce:POWer:PROTection

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "PROTection"
                args = ["1", "ON", "OFF"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:PROTection:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:POWer:PROTection:STATe

                Arguments: 1, ON, OFF
                """

            PROTection = PROTection()  # type: ignore
            """
            SOURce:POWer:PROTection

            Arguments: 1, ON, OFF
            """

            class RANGe(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:RANGe

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "RANGe"
                args = ["1"]

            RANGe = RANGe()  # type: ignore
            """
            SOURce:POWer:RANGe

            Arguments: 1
            """

            class REFerence(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:REFerence

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "REFerence"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:REFerence:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:POWer:REFerence:STATe

                Arguments: 1, ON, OFF
                """

            REFerence = REFerence()  # type: ignore
            """
            SOURce:POWer:REFerence

            Arguments: 1
            """

            class SEARch(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:SEARch

                Arguments: <boolean>, ONCE
                """
                __slots__ = ()
                _cmd = "SEARch"
                args = ["<boolean>", "ONCE"]

            SEARch = SEARch()  # type: ignore
            """
            SOURce:POWer:SEARch

            Arguments: <boolean>, ONCE
            """

            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:SLOPe

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "SLOPe"
                args = ["1"]

                class PIVot(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:SLOPe:PIVot

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PIVot"
                    args = ["1"]

                PIVot = PIVot()  # type: ignore
                """
                SOURce:POWer:SLOPe:PIVot

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:SLOPe:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:POWer:SLOPe:STATe

                Arguments: 1, ON, OFF
                """

                class STEP(SCPINode):
                    """
                    SOURce:POWer:SLOPe:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:SLOPe:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:POWer:SLOPe:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:POWer:SLOPe:STEP

                Arguments:
                """

            SLOPe = SLOPe()  # type: ignore
            """
            SOURce:POWer:SLOPe

            Arguments: 1
            """

            class SPAN(SCPINode):
                """
                SOURce:POWer:SPAN

                Arguments:
                """
                __slots__ = ()
                _cmd = "SPAN"
                args = []  # type: List[str]

                class STEP(SCPINode):
                    """
                    SOURce:POWer:SPAN:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:SPAN:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:POWer:SPAN:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:POWer:SPAN:STEP

                Arguments:
                """

            SPAN = SPAN()  # type: ignore
            """
            SOURce:POWer:SPAN

            Arguments:
            """

            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:STARt
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/75df17de88344e45.htm#ID_bfd022ec71aaaeff0a00206a01dfb254-b40f922e71aaaeff0a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STARt"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:POWer:STARt:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:STARt:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:POWer:STARt:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:POWer:STARt:STEP

                Arguments:
                """

            STARt = STARt()  # type: ignore
            """
            `SOURce:POWer:STARt
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/75df17de88344e45.htm#ID_bfd022ec71aaaeff0a00206a01dfb254-b40f922e71aaaeff0a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:POWer:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SOURce:POWer:STATe

            Arguments: 1, ON, OFF
            """

            class STEP(SCPINode):
                """
                SOURce:POWer:STEP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STEP"
                args = []  # type: List[str]

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:STEP:INCRement
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3a5b9c83f91a4347.htm#ID_78f8a91f71aa79c60a00206a01d797f3-dccd25e471aa79c60a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "INCRement"
                    args = ["1"]

                    class LINear(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:STEP:INCRement:LINear

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "LINear"
                        args = ["1"]

                    LINear = LINear()  # type: ignore
                    """
                    SOURce:POWer:STEP:INCRement:LINear

                    Arguments: 1
                    """

                    class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:STEP:INCRement:LOGarithmic

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()  # type: ignore
                    """
                    SOURce:POWer:STEP:INCRement:LOGarithmic

                    Arguments: 1
                    """

                INCRement = INCRement()  # type: ignore
                """
                `SOURce:POWer:STEP:INCRement
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3a5b9c83f91a4347.htm#ID_78f8a91f71aa79c60a00206a01d797f3-dccd25e471aa79c60a00206a012bc823-en-US>`_

                Arguments: 1
                """

            STEP = STEP()  # type: ignore
            """
            SOURce:POWer:STEP

            Arguments:
            """

            class STOP(SCPINode):
                """
                `SOURce:POWer:STOP
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3e7c17ad63134242.htm#ID_0b3f20dd71aab6620a00206a0036ddee-9ea7ec1a71aab6620a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "STOP"
                args = []  # type: List[str]

                class STEP(SCPINode):
                    """
                    SOURce:POWer:STOP:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:STOP:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:POWer:STOP:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:POWer:STOP:STEP

                Arguments:
                """

            STOP = STOP()  # type: ignore
            """
            `SOURce:POWer:STOP
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3e7c17ad63134242.htm#ID_0b3f20dd71aab6620a00206a0036ddee-9ea7ec1a71aab6620a00206a012bc823-en-US>`_

            Arguments:
            """

            class USER(SCPINode):
                """
                SOURce:POWer:USER

                Arguments:
                """
                __slots__ = ()
                _cmd = "USER"
                args = []  # type: List[str]

                class ENABle(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:USER:ENABle

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1", "ON", "OFF"]

                ENABle = ENABle()  # type: ignore
                """
                SOURce:POWer:USER:ENABle

                Arguments: 1, ON, OFF
                """

                class MAXimum(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:USER:MAXimum

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "MAXimum"
                    args = ["1"]

                MAXimum = MAXimum()  # type: ignore
                """
                SOURce:POWer:USER:MAXimum

                Arguments: 1
                """

            USER = USER()  # type: ignore
            """
            SOURce:POWer:USER

            Arguments:
            """

        POWer = POWer()  # type: ignore
        """
        SOURce:POWer

        Arguments:
        """

        class PULM(SCPINode):
            """
            SOURce:PULM

            Arguments:
            """
            __slots__ = ()
            _cmd = "PULM"
            args = []  # type: List[str]

            class EXTernal(SCPINode, SCPISet):
                """
                SOURce:PULM:EXTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "EXTernal"
                args = []  # type: List[str]

                class DELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:EXTernal:DELay

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DELay"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:EXTernal:DELay:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:EXTernal:DELay:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:PULM:EXTernal:DELay:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:PULM:EXTernal:DELay:STEP

                    Arguments:
                    """

                DELay = DELay()  # type: ignore
                """
                SOURce:PULM:EXTernal:DELay

                Arguments: 1
                """

                class IMPedance(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:EXTernal:IMPedance

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()  # type: ignore
                """
                SOURce:PULM:EXTernal:IMPedance

                Arguments: 1
                """

                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:EXTernal:POLarity

                    Arguments: INVerted, NORMal
                    """
                    __slots__ = ()
                    _cmd = "POLarity"
                    args = ["INVerted", "NORMal"]

                POLarity = POLarity()  # type: ignore
                """
                SOURce:PULM:EXTernal:POLarity

                Arguments: INVerted, NORMal
                """

            EXTernal = EXTernal()  # type: ignore
            """
            SOURce:PULM:EXTernal

            Arguments:
            """

            class INTernal(SCPINode, SCPISet):
                """
                SOURce:PULM:INTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "INTernal"
                args = []  # type: List[str]

                class DELay(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:INTernal:DELay

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DELay"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:INTernal:DELay:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:INTernal:DELay:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:PULM:INTernal:DELay:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:PULM:INTernal:DELay:STEP

                    Arguments:
                    """

                DELay = DELay()  # type: ignore
                """
                SOURce:PULM:INTernal:DELay

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:INTernal:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:INTernal:FREQuency:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:INTernal:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:PULM:INTernal:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:PULM:INTernal:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:PULM:INTernal:FREQuency

                Arguments: 1
                """

                class FUNCtion(SCPINode):
                    """
                    SOURce:PULM:INTernal:FUNCtion

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "FUNCtion"
                    args = []  # type: List[str]

                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULM:INTernal:FUNCtion:SHAPe

                        Arguments: PULSe, SQUare
                        """
                        __slots__ = ()
                        _cmd = "SHAPe"
                        args = ["PULSe", "SQUare"]

                    SHAPe = SHAPe()  # type: ignore
                    """
                    SOURce:PULM:INTernal:FUNCtion:SHAPe

                    Arguments: PULSe, SQUare
                    """

                FUNCtion = FUNCtion()  # type: ignore
                """
                SOURce:PULM:INTernal:FUNCtion

                Arguments:
                """

                class PERiod(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:INTernal:PERiod

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PERiod"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:INTernal:PERiod:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:INTernal:PERiod:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:PULM:INTernal:PERiod:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:PULM:INTernal:PERiod:STEP

                    Arguments:
                    """

                PERiod = PERiod()  # type: ignore
                """
                SOURce:PULM:INTernal:PERiod

                Arguments: 1
                """

                class PWIDth(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:INTernal:PWIDth

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PWIDth"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:INTernal:PWIDth:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:INTernal:PWIDth:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:PULM:INTernal:PWIDth:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:PULM:INTernal:PWIDth:STEP

                    Arguments:
                    """

                PWIDth = PWIDth()  # type: ignore
                """
                SOURce:PULM:INTernal:PWIDth

                Arguments: 1
                """

                class TRIGger(SCPINode):
                    """
                    SOURce:PULM:INTernal:TRIGger

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "TRIGger"
                    args = []  # type: List[str]

                    class SOURce(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULM:INTernal:TRIGger:SOURce

                        Arguments: EXTernal, INTernal
                        """
                        __slots__ = ()
                        _cmd = "SOURce"
                        args = ["EXTernal", "INTernal"]

                    SOURce = SOURce()  # type: ignore
                    """
                    SOURce:PULM:INTernal:TRIGger:SOURce

                    Arguments: EXTernal, INTernal
                    """

                TRIGger = TRIGger()  # type: ignore
                """
                SOURce:PULM:INTernal:TRIGger

                Arguments:
                """

                class VIDeo(SCPINode, SCPISet):
                    """
                    SOURce:PULM:INTernal:VIDeo

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "VIDeo"
                    args = []  # type: List[str]

                    class POLarity(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULM:INTernal:VIDeo:POLarity

                        Arguments: INVerted, NORMal
                        """
                        __slots__ = ()
                        _cmd = "POLarity"
                        args = ["INVerted", "NORMal"]

                    POLarity = POLarity()  # type: ignore
                    """
                    SOURce:PULM:INTernal:VIDeo:POLarity

                    Arguments: INVerted, NORMal
                    """

                VIDeo = VIDeo()  # type: ignore
                """
                SOURce:PULM:INTernal:VIDeo

                Arguments:
                """

                class WIDTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:INTernal:WIDTh

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "WIDTh"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:INTernal:WIDTh:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:INTernal:WIDTh:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:PULM:INTernal:WIDTh:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:PULM:INTernal:WIDTh:STEP

                    Arguments:
                    """

                WIDTh = WIDTh()  # type: ignore
                """
                SOURce:PULM:INTernal:WIDTh

                Arguments: 1
                """

            INTernal = INTernal()  # type: ignore
            """
            SOURce:PULM:INTernal

            Arguments:
            """

            class PERiod(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:PULM:PERiod
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f8fc39f1ea9c40a3.htm#ID_ebe92a974e3555850a00206a0199777d-bd4d581f4e3555850a00206a0024546d-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PERiod"
                args = ["1"]

            PERiod = PERiod()  # type: ignore
            """
            `SOURce:PULM:PERiod
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f8fc39f1ea9c40a3.htm#ID_ebe92a974e3555850a00206a0199777d-bd4d581f4e3555850a00206a0024546d-en-US>`_

            Arguments: 1
            """

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:PULM:POLarity
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/cd47c0071bb149e5.htm#ID_3497059d4e353d690a00206a01ed3f2d-d8fa28904e353d690a00206a0024546d-en-US>`_

                Arguments: INVerted, NORMal
                """
                __slots__ = ()
                _cmd = "POLarity"
                args = ["INVerted", "NORMal"]

            POLarity = POLarity()  # type: ignore
            """
            `SOURce:PULM:POLarity
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/cd47c0071bb149e5.htm#ID_3497059d4e353d690a00206a01ed3f2d-d8fa28904e353d690a00206a0024546d-en-US>`_

            Arguments: INVerted, NORMal
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:PULM:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/d01a62da234944cd.htm#ID_c1f0481e4e3545970a00206a00087ee2-5edf7c2c4e3545970a00206a0024546d-en-US>`_

                Arguments: EXT1, EXT2, EXTernal, EXTernal1, EXTernal2, INTernal
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["EXT1", "EXT2", "EXTernal", "EXTernal1", "EXTernal2", "INTernal"]

                class INTernal(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:SOURce:INTernal

                    Arguments: ADOublet, DOUBlet, FRUN, GATed, SQUare, TRIGgered
                    """
                    __slots__ = ()
                    _cmd = "INTernal"
                    args = ["ADOublet", "DOUBlet", "FRUN", "GATed", "SQUare", "TRIGgered"]

                INTernal = INTernal()  # type: ignore
                """
                SOURce:PULM:SOURce:INTernal

                Arguments: ADOublet, DOUBlet, FRUN, GATed, SQUare, TRIGgered
                """

            SOURce = SOURce()  # type: ignore
            """
            `SOURce:PULM:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/d01a62da234944cd.htm#ID_c1f0481e4e3545970a00206a00087ee2-5edf7c2c4e3545970a00206a0024546d-en-US>`_

            Arguments: EXT1, EXT2, EXTernal, EXTernal1, EXTernal2, INTernal
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SOURce:PULM:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/08c1f6939a514b85.htm#ID_ee977e2b4e352d8b0a00206a018c0222-5a28bd874e352d8b0a00206a0024546d-en-US>`_

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            `SOURce:PULM:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/08c1f6939a514b85.htm#ID_ee977e2b4e352d8b0a00206a018c0222-5a28bd874e352d8b0a00206a0024546d-en-US>`_

            Arguments: 1, ON, OFF
            """

            class WIDTh(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:PULM:WIDTh
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/737870cd065d45b3.htm#ID_b29b3cb94e355edb0a00206a016f086a-cfb305434e355edb0a00206a0024546d-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "WIDTh"
                args = ["1"]

            WIDTh = WIDTh()  # type: ignore
            """
            `SOURce:PULM:WIDTh
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/737870cd065d45b3.htm#ID_b29b3cb94e355edb0a00206a016f086a-cfb305434e355edb0a00206a0024546d-en-US>`_

            Arguments: 1
            """

        PULM = PULM()  # type: ignore
        """
        SOURce:PULM

        Arguments:
        """

        class PULSe(SCPINode):
            """
            SOURce:PULSe

            Arguments:
            """
            __slots__ = ()
            _cmd = "PULSe"
            args = []  # type: List[str]

            class DELay(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PULSe:DELay

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DELay"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:PULSe:DELay:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULSe:DELay:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:PULSe:DELay:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:PULSe:DELay:STEP

                Arguments:
                """

            DELay = DELay()  # type: ignore
            """
            SOURce:PULSe:DELay

            Arguments: 1
            """

            class DOUBle(SCPINode):
                """
                SOURce:PULSe:DOUBle

                Arguments:
                """
                __slots__ = ()
                _cmd = "DOUBle"
                args = []  # type: List[str]

                class DELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULSe:DOUBle:DELay

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DELay"
                    args = ["1"]

                DELay = DELay()  # type: ignore
                """
                SOURce:PULSe:DOUBle:DELay

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:PULSe:DOUBle:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:PULSe:DOUBle:STATe

                Arguments: 1, ON, OFF
                """

            DOUBle = DOUBle()  # type: ignore
            """
            SOURce:PULSe:DOUBle

            Arguments:
            """

            class INTernal(SCPINode):
                """
                SOURce:PULSe:INTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "INTernal"
                args = []  # type: List[str]

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULSe:INTernal:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULSe:INTernal:FREQuency:STEP

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "STEP"
                        args = []  # type: List[str]

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULSe:INTernal:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()  # type: ignore
                        """
                        SOURce:PULSe:INTernal:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()  # type: ignore
                    """
                    SOURce:PULSe:INTernal:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:PULSe:INTernal:FREQuency

                Arguments: 1
                """

            INTernal = INTernal()  # type: ignore
            """
            SOURce:PULSe:INTernal

            Arguments:
            """

            class PERiod(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PULSe:PERiod

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PERiod"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:PULSe:PERiod:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULSe:PERiod:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:PULSe:PERiod:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:PULSe:PERiod:STEP

                Arguments:
                """

            PERiod = PERiod()  # type: ignore
            """
            SOURce:PULSe:PERiod

            Arguments: 1
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PULSe:SOURce

                Arguments: EXTernal, INTernal, SCALar
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["EXTernal", "INTernal", "SCALar"]

            SOURce = SOURce()  # type: ignore
            """
            SOURce:PULSe:SOURce

            Arguments: EXTernal, INTernal, SCALar
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:PULSe:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SOURce:PULSe:STATe

            Arguments: 1, ON, OFF
            """

            class TRANsition(SCPINode):
                """
                SOURce:PULSe:TRANsition

                Arguments:
                """
                __slots__ = ()
                _cmd = "TRANsition"
                args = []  # type: List[str]

                class LEADing(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULSe:TRANsition:LEADing

                    Arguments: FAST, MEDium, SLOW
                    """
                    __slots__ = ()
                    _cmd = "LEADing"
                    args = ["FAST", "MEDium", "SLOW"]

                LEADing = LEADing()  # type: ignore
                """
                SOURce:PULSe:TRANsition:LEADing

                Arguments: FAST, MEDium, SLOW
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:PULSe:TRANsition:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:PULSe:TRANsition:STATe

                Arguments: 1, ON, OFF
                """

                class TRAiling(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULSe:TRANsition:TRAiling

                    Arguments: FAST, MEDium, SLOW
                    """
                    __slots__ = ()
                    _cmd = "TRAiling"
                    args = ["FAST", "MEDium", "SLOW"]

                TRAiling = TRAiling()  # type: ignore
                """
                SOURce:PULSe:TRANsition:TRAiling

                Arguments: FAST, MEDium, SLOW
                """

            TRANsition = TRANsition()  # type: ignore
            """
            SOURce:PULSe:TRANsition

            Arguments:
            """

            class WIDTh(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PULSe:WIDTh

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "WIDTh"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:PULSe:WIDTh:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULSe:WIDTh:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SOURce:PULSe:WIDTh:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:PULSe:WIDTh:STEP

                Arguments:
                """

            WIDTh = WIDTh()  # type: ignore
            """
            SOURce:PULSe:WIDTh

            Arguments: 1
            """

        PULSe = PULSe()  # type: ignore
        """
        SOURce:PULSe

        Arguments:
        """

        class RADio(SCPINode, SCPISet):
            """
            SOURce:RADio

            Arguments:
            """
            __slots__ = ()
            _cmd = "RADio"
            args = []  # type: List[str]

            class ARB(SCPINode):
                """
                SOURce:RADio:ARB

                Arguments:
                """
                __slots__ = ()
                _cmd = "ARB"
                args = []  # type: List[str]

                class CLIPping(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:CLIPping

                    Arguments: <string>,IJQ, IORQ,<numeric_value>,<numeric_value>
                    """
                    __slots__ = ()
                    _cmd = "CLIPping"
                    args = ["<string>,IJQ", "IORQ,<numeric_value>,<numeric_value>"]

                CLIPping = CLIPping()  # type: ignore
                """
                SOURce:RADio:ARB:CLIPping

                Arguments: <string>,IJQ, IORQ,<numeric_value>,<numeric_value>
                """

                class CLOCk(SCPINode):
                    """
                    SOURce:RADio:ARB:CLOCk

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CLOCk"
                    args = []  # type: List[str]

                    class REFerence(SCPINode):
                        """
                        SOURce:RADio:ARB:CLOCk:REFerence

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "REFerence"
                        args = []  # type: List[str]

                        class EXTernal(SCPINode, SCPISet):
                            """
                            SOURce:RADio:ARB:CLOCk:REFerence:EXTernal

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "EXTernal"
                            args = []  # type: List[str]

                            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:ARB:CLOCk:REFerence:EXTernal:FREQuency

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "FREQuency"
                                args = ["1"]

                            FREQuency = FREQuency()  # type: ignore
                            """
                            SOURce:RADio:ARB:CLOCk:REFerence:EXTernal:FREQuency

                            Arguments: 1
                            """

                        EXTernal = EXTernal()  # type: ignore
                        """
                        SOURce:RADio:ARB:CLOCk:REFerence:EXTernal

                        Arguments:
                        """

                        class SOURce(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:ARB:CLOCk:REFerence:SOURce

                            Arguments: EXTernal, INTernal
                            """
                            __slots__ = ()
                            _cmd = "SOURce"
                            args = ["EXTernal", "INTernal"]

                        SOURce = SOURce()  # type: ignore
                        """
                        SOURce:RADio:ARB:CLOCk:REFerence:SOURce

                        Arguments: EXTernal, INTernal
                        """

                    REFerence = REFerence()  # type: ignore
                    """
                    SOURce:RADio:ARB:CLOCk:REFerence

                    Arguments:
                    """

                    class SRATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:CLOCk:SRATe

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "SRATe"
                        args = ["1"]

                    SRATe = SRATe()  # type: ignore
                    """
                    SOURce:RADio:ARB:CLOCk:SRATe

                    Arguments: 1
                    """

                CLOCk = CLOCk()  # type: ignore
                """
                SOURce:RADio:ARB:CLOCk

                Arguments:
                """

                class DACS(SCPINode):
                    """
                    SOURce:RADio:ARB:DACS

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "DACS"
                    args = []  # type: List[str]

                    class ALIGn(SCPINode, SCPISet):
                        """
                        SOURce:RADio:ARB:DACS:ALIGn

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "ALIGn"
                        args = []  # type: List[str]

                    ALIGn = ALIGn()  # type: ignore
                    """
                    SOURce:RADio:ARB:DACS:ALIGn

                    Arguments:
                    """

                DACS = DACS()  # type: ignore
                """
                SOURce:RADio:ARB:DACS

                Arguments:
                """

                class GENerate(SCPINode, SCPISet):
                    """
                    SOURce:RADio:ARB:GENerate

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "GENerate"
                    args = []  # type: List[str]

                GENerate = GENerate()  # type: ignore
                """
                SOURce:RADio:ARB:GENerate

                Arguments:
                """

                class HEADer(SCPINode, SCPISet):
                    """
                    SOURce:RADio:ARB:HEADer

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "HEADer"
                    args = []  # type: List[str]

                    class CLEar(SCPINode, SCPISet):
                        """
                        SOURce:RADio:ARB:HEADer:CLEar

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "CLEar"
                        args = []  # type: List[str]

                    CLEar = CLEar()  # type: ignore
                    """
                    SOURce:RADio:ARB:HEADer:CLEar

                    Arguments:
                    """

                HEADer = HEADer()  # type: ignore
                """
                SOURce:RADio:ARB:HEADer

                Arguments:
                """

                class IQ(SCPINode):
                    """
                    SOURce:RADio:ARB:IQ

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "IQ"
                    args = []  # type: List[str]

                    class EXTernal(SCPINode, SCPISet):
                        """
                        SOURce:RADio:ARB:IQ:EXTernal

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EXTernal"
                        args = []  # type: List[str]

                        class FILTer(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:ARB:IQ:EXTernal:FILTer

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "FILTer"
                            args = ["1"]

                        FILTer = FILTer()  # type: ignore
                        """
                        SOURce:RADio:ARB:IQ:EXTernal:FILTer

                        Arguments: 1
                        """

                    EXTernal = EXTernal()  # type: ignore
                    """
                    SOURce:RADio:ARB:IQ:EXTernal

                    Arguments:
                    """

                    class MODulation(SCPINode, SCPISet):
                        """
                        SOURce:RADio:ARB:IQ:MODulation

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "MODulation"
                        args = []  # type: List[str]

                        class ATTen(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:ARB:IQ:MODulation:ATTen

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "ATTen"
                            args = ["1"]

                        ATTen = ATTen()  # type: ignore
                        """
                        SOURce:RADio:ARB:IQ:MODulation:ATTen

                        Arguments: 1
                        """

                        class FILTer(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:ARB:IQ:MODulation:FILTer

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "FILTer"
                            args = ["1"]

                        FILTer = FILTer()  # type: ignore
                        """
                        SOURce:RADio:ARB:IQ:MODulation:FILTer

                        Arguments: 1
                        """

                    MODulation = MODulation()  # type: ignore
                    """
                    SOURce:RADio:ARB:IQ:MODulation

                    Arguments:
                    """

                IQ = IQ()  # type: ignore
                """
                SOURce:RADio:ARB:IQ

                Arguments:
                """

                class MARKer(SCPINode):
                    """
                    SOURce:RADio:ARB:MARKer

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "MARKer"
                    args = []  # type: List[str]

                    class CLEar(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MARKer:CLEar

                        Arguments: <string>,<numeric_value>,<numeric_value>,<numeric_value>
                        """
                        __slots__ = ()
                        _cmd = "CLEar"
                        args = ["<string>,<numeric_value>,<numeric_value>,<numeric_value>"]

                    CLEar = CLEar()  # type: ignore
                    """
                    SOURce:RADio:ARB:MARKer:CLEar

                    Arguments: <string>,<numeric_value>,<numeric_value>,<numeric_value>
                    """

                    class ROTate(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MARKer:ROTate

                        Arguments: <string>,<numeric_value>
                        """
                        __slots__ = ()
                        _cmd = "ROTate"
                        args = ["<string>,<numeric_value>"]

                    ROTate = ROTate()  # type: ignore
                    """
                    SOURce:RADio:ARB:MARKer:ROTate

                    Arguments: <string>,<numeric_value>
                    """

                MARKer = MARKer()  # type: ignore
                """
                SOURce:RADio:ARB:MARKer

                Arguments:
                """

                class MDEStination(SCPINode, SCPISet):
                    """
                    SOURce:RADio:ARB:MDEStination

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "MDEStination"
                    args = []  # type: List[str]

                    class AAMPlitude(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MDEStination:AAMPlitude

                        Arguments: M1, M2, M3, M4, NONE
                        """
                        __slots__ = ()
                        _cmd = "AAMPlitude"
                        args = ["M1", "M2", "M3", "M4", "NONE"]

                    AAMPlitude = AAMPlitude()  # type: ignore
                    """
                    SOURce:RADio:ARB:MDEStination:AAMPlitude

                    Arguments: M1, M2, M3, M4, NONE
                    """

                    class ALCHold(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MDEStination:ALCHold

                        Arguments: M1, M2, M3, M4, NONE
                        """
                        __slots__ = ()
                        _cmd = "ALCHold"
                        args = ["M1", "M2", "M3", "M4", "NONE"]

                    ALCHold = ALCHold()  # type: ignore
                    """
                    SOURce:RADio:ARB:MDEStination:ALCHold

                    Arguments: M1, M2, M3, M4, NONE
                    """

                    class PULSe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MDEStination:PULSe

                        Arguments: M1, M2, M3, M4, NONE
                        """
                        __slots__ = ()
                        _cmd = "PULSe"
                        args = ["M1", "M2", "M3", "M4", "NONE"]

                    PULSe = PULSe()  # type: ignore
                    """
                    SOURce:RADio:ARB:MDEStination:PULSe

                    Arguments: M1, M2, M3, M4, NONE
                    """

                MDEStination = MDEStination()  # type: ignore
                """
                SOURce:RADio:ARB:MDEStination

                Arguments:
                """

                class MPOLarity(SCPINode, SCPISet):
                    """
                    SOURce:RADio:ARB:MPOLarity

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "MPOLarity"
                    args = []  # type: List[str]

                    class MARKer(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MPOLarity:MARKer

                        Arguments: NEGative, POSitive
                        """
                        __slots__ = ()
                        _cmd = "MARKer"
                        args = ["NEGative", "POSitive"]

                    MARKer = MARKer()  # type: ignore
                    """
                    SOURce:RADio:ARB:MPOLarity:MARKer

                    Arguments: NEGative, POSitive
                    """

                MPOLarity = MPOLarity()  # type: ignore
                """
                SOURce:RADio:ARB:MPOLarity

                Arguments:
                """

                class NOISe(SCPINode):
                    """
                    SOURce:RADio:ARB:NOISe

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "NOISe"
                    args = []  # type: List[str]

                    class BFACtor(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:NOISe:BFACtor

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "BFACtor"
                        args = ["1"]

                    BFACtor = BFACtor()  # type: ignore
                    """
                    SOURce:RADio:ARB:NOISe:BFACtor

                    Arguments: 1
                    """

                    class CBWidth(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:NOISe:CBWidth

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "CBWidth"
                        args = ["1"]

                    CBWidth = CBWidth()  # type: ignore
                    """
                    SOURce:RADio:ARB:NOISe:CBWidth

                    Arguments: 1
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:RADio:ARB:NOISe:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SOURce:RADio:ARB:NOISe:STATe

                    Arguments: 1, ON, OFF
                    """

                NOISe = NOISe()  # type: ignore
                """
                SOURce:RADio:ARB:NOISe

                Arguments:
                """

                class REFerence(SCPINode):
                    """
                    SOURce:RADio:ARB:REFerence

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "REFerence"
                    args = []  # type: List[str]

                    class EXTernal(SCPINode, SCPISet):
                        """
                        SOURce:RADio:ARB:REFerence:EXTernal

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EXTernal"
                        args = []  # type: List[str]

                        class FREQuency(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:ARB:REFerence:EXTernal:FREQuency

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "FREQuency"
                            args = ["1"]

                        FREQuency = FREQuency()  # type: ignore
                        """
                        SOURce:RADio:ARB:REFerence:EXTernal:FREQuency

                        Arguments: 1
                        """

                    EXTernal = EXTernal()  # type: ignore
                    """
                    SOURce:RADio:ARB:REFerence:EXTernal

                    Arguments:
                    """

                    class SOURce(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:REFerence:SOURce

                        Arguments: EXTernal, INTernal
                        """
                        __slots__ = ()
                        _cmd = "SOURce"
                        args = ["EXTernal", "INTernal"]

                    SOURce = SOURce()  # type: ignore
                    """
                    SOURce:RADio:ARB:REFerence:SOURce

                    Arguments: EXTernal, INTernal
                    """

                REFerence = REFerence()  # type: ignore
                """
                SOURce:RADio:ARB:REFerence

                Arguments:
                """

                class RETRigger(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:RETRigger

                    Arguments: <boolean>, IMMediate
                    """
                    __slots__ = ()
                    _cmd = "RETRigger"
                    args = ["<boolean>", "IMMediate"]

                RETRigger = RETRigger()  # type: ignore
                """
                SOURce:RADio:ARB:RETRigger

                Arguments: <boolean>, IMMediate
                """

                class RFILter(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:RFILter

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "RFILter"
                    args = ["1"]

                RFILter = RFILter()  # type: ignore
                """
                SOURce:RADio:ARB:RFILter

                Arguments: 1
                """

                class RSCaling(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:RSCaling

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "RSCaling"
                    args = ["1"]

                RSCaling = RSCaling()  # type: ignore
                """
                SOURce:RADio:ARB:RSCaling

                Arguments: 1
                """

                class SCALing(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:SCALing

                    Arguments: <string>,<numeric_value>
                    """
                    __slots__ = ()
                    _cmd = "SCALing"
                    args = ["<string>,<numeric_value>"]

                SCALing = SCALing()  # type: ignore
                """
                SOURce:RADio:ARB:SCALing

                Arguments: <string>,<numeric_value>
                """

                class SCLock(SCPINode, SCPISet):
                    """
                    SOURce:RADio:ARB:SCLock

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SCLock"
                    args = []  # type: List[str]

                SCLock = SCLock()  # type: ignore
                """
                SOURce:RADio:ARB:SCLock

                Arguments:
                """

                class SEQuence(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:SEQuence

                    Arguments: 'string'
                    """
                    __slots__ = ()
                    _cmd = "SEQuence"
                    args = ["'string'"]

                SEQuence = SEQuence()  # type: ignore
                """
                SOURce:RADio:ARB:SEQuence

                Arguments: 'string'
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:RADio:ARB:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:RADio:ARB:STATe

                Arguments: 1, ON, OFF
                """

                class TRIGger(SCPINode):
                    """
                    SOURce:RADio:ARB:TRIGger

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "TRIGger"
                    args = []  # type: List[str]

                    class SOURce(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:TRIGger:SOURce

                        Arguments: BUS, EXTernal, KEY
                        """
                        __slots__ = ()
                        _cmd = "SOURce"
                        args = ["BUS", "EXTernal", "KEY"]

                        class EXTernal(SCPINode):
                            """
                            SOURce:RADio:ARB:TRIGger:SOURce:EXTernal

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "EXTernal"
                            args = []  # type: List[str]

                            class DELay(SCPINode):
                                """
                                SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay

                                Arguments:
                                """
                                __slots__ = ()
                                _cmd = "DELay"
                                args = []  # type: List[str]

                                class SAMPles(SCPINode, SCPIQuery, SCPISet):
                                    """
                                    SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay:SAMPles

                                    Arguments: 1
                                    """
                                    __slots__ = ()
                                    _cmd = "SAMPles"
                                    args = ["1"]

                                SAMPles = SAMPles()  # type: ignore
                                """
                                SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay:SAMPles

                                Arguments: 1
                                """

                                class STATe(SCPINode, SCPIBool):
                                    """
                                    SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay:STATe

                                    Arguments: 1, ON, OFF
                                    """
                                    __slots__ = ()
                                    _cmd = "STATe"
                                    args = ["1", "ON", "OFF"]

                                STATe = STATe()  # type: ignore
                                """
                                SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay:STATe

                                Arguments: 1, ON, OFF
                                """

                            DELay = DELay()  # type: ignore
                            """
                            SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay

                            Arguments:
                            """

                            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:SLOPe

                                Arguments: NEGative, POSitive
                                """
                                __slots__ = ()
                                _cmd = "SLOPe"
                                args = ["NEGative", "POSitive"]

                            SLOPe = SLOPe()  # type: ignore
                            """
                            SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:SLOPe

                            Arguments: NEGative, POSitive
                            """

                            class SOURce(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:SOURce

                                Arguments: EPT1, EPT2, EPTRigger1, EPTRigger2
                                """
                                __slots__ = ()
                                _cmd = "SOURce"
                                args = ["EPT1", "EPT2", "EPTRigger1", "EPTRigger2"]

                            SOURce = SOURce()  # type: ignore
                            """
                            SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:SOURce

                            Arguments: EPT1, EPT2, EPTRigger1, EPTRigger2
                            """

                        EXTernal = EXTernal()  # type: ignore
                        """
                        SOURce:RADio:ARB:TRIGger:SOURce:EXTernal

                        Arguments:
                        """

                    SOURce = SOURce()  # type: ignore
                    """
                    SOURce:RADio:ARB:TRIGger:SOURce

                    Arguments: BUS, EXTernal, KEY
                    """

                    class TYPE(SCPINode):
                        """
                        SOURce:RADio:ARB:TRIGger:TYPE

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "TYPE"
                        args = []  # type: List[str]

                        class GATE(SCPINode):
                            """
                            SOURce:RADio:ARB:TRIGger:TYPE:GATE

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "GATE"
                            args = []  # type: List[str]

                            class ACTive(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:ARB:TRIGger:TYPE:GATE:ACTive

                                Arguments: HIGH, LOW
                                """
                                __slots__ = ()
                                _cmd = "ACTive"
                                args = ["HIGH", "LOW"]

                            ACTive = ACTive()  # type: ignore
                            """
                            SOURce:RADio:ARB:TRIGger:TYPE:GATE:ACTive

                            Arguments: HIGH, LOW
                            """

                        GATE = GATE()  # type: ignore
                        """
                        SOURce:RADio:ARB:TRIGger:TYPE:GATE

                        Arguments:
                        """

                    TYPE = TYPE()  # type: ignore
                    """
                    SOURce:RADio:ARB:TRIGger:TYPE

                    Arguments:
                    """

                TRIGger = TRIGger()  # type: ignore
                """
                SOURce:RADio:ARB:TRIGger

                Arguments:
                """

                class VCO(SCPINode):
                    """
                    SOURce:RADio:ARB:VCO

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "VCO"
                    args = []  # type: List[str]

                    class CLOCk(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:VCO:CLOCk

                        Arguments: EXTernal, INTernal
                        """
                        __slots__ = ()
                        _cmd = "CLOCk"
                        args = ["EXTernal", "INTernal"]

                    CLOCk = CLOCk()  # type: ignore
                    """
                    SOURce:RADio:ARB:VCO:CLOCk

                    Arguments: EXTernal, INTernal
                    """

                VCO = VCO()  # type: ignore
                """
                SOURce:RADio:ARB:VCO

                Arguments:
                """

                class WAVeform(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:WAVeform

                    Arguments: 'string'
                    """
                    __slots__ = ()
                    _cmd = "WAVeform"
                    args = ["'string'"]

                    class NHEaders(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:WAVeform:NHEaders

                        Arguments: 'string'
                        """
                        __slots__ = ()
                        _cmd = "NHEaders"
                        args = ["'string'"]

                    NHEaders = NHEaders()  # type: ignore
                    """
                    SOURce:RADio:ARB:WAVeform:NHEaders

                    Arguments: 'string'
                    """

                WAVeform = WAVeform()  # type: ignore
                """
                SOURce:RADio:ARB:WAVeform

                Arguments: 'string'
                """

            ARB = ARB()  # type: ignore
            """
            SOURce:RADio:ARB

            Arguments:
            """

            class AWGN(SCPINode):
                """
                SOURce:RADio:AWGN

                Arguments:
                """
                __slots__ = ()
                _cmd = "AWGN"
                args = []  # type: List[str]

                class ARB(SCPINode):
                    """
                    SOURce:RADio:AWGN:ARB

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ARB"
                    args = []  # type: List[str]

                    class BWIDth(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:AWGN:ARB:BWIDth

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "BWIDth"
                        args = ["1"]

                    BWIDth = BWIDth()  # type: ignore
                    """
                    SOURce:RADio:AWGN:ARB:BWIDth

                    Arguments: 1
                    """

                    class HEADer(SCPINode, SCPISet):
                        """
                        SOURce:RADio:AWGN:ARB:HEADer

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "HEADer"
                        args = []  # type: List[str]

                        class CLEar(SCPINode, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:HEADer:CLEar

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "CLEar"
                            args = []  # type: List[str]

                        CLEar = CLEar()  # type: ignore
                        """
                        SOURce:RADio:AWGN:ARB:HEADer:CLEar

                        Arguments:
                        """

                    HEADer = HEADer()  # type: ignore
                    """
                    SOURce:RADio:AWGN:ARB:HEADer

                    Arguments:
                    """

                    class IQ(SCPINode):
                        """
                        SOURce:RADio:AWGN:ARB:IQ

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "IQ"
                        args = []  # type: List[str]

                        class EXTernal(SCPINode, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:IQ:EXTernal

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "EXTernal"
                            args = []  # type: List[str]

                            class FILTer(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:AWGN:ARB:IQ:EXTernal:FILTer

                                Arguments: <numeric_value>, THRough
                                """
                                __slots__ = ()
                                _cmd = "FILTer"
                                args = ["<numeric_value>", "THRough"]

                            FILTer = FILTer()  # type: ignore
                            """
                            SOURce:RADio:AWGN:ARB:IQ:EXTernal:FILTer

                            Arguments: <numeric_value>, THRough
                            """

                        EXTernal = EXTernal()  # type: ignore
                        """
                        SOURce:RADio:AWGN:ARB:IQ:EXTernal

                        Arguments:
                        """

                        class MODulation(SCPINode, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:IQ:MODulation

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "MODulation"
                            args = []  # type: List[str]

                            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:AWGN:ARB:IQ:MODulation:ATTenuation

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "ATTenuation"
                                args = ["1"]

                            ATTenuation = ATTenuation()  # type: ignore
                            """
                            SOURce:RADio:AWGN:ARB:IQ:MODulation:ATTenuation

                            Arguments: 1
                            """

                            class FILTer(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:AWGN:ARB:IQ:MODulation:FILTer

                                Arguments: <numeric_value>, THRough
                                """
                                __slots__ = ()
                                _cmd = "FILTer"
                                args = ["<numeric_value>", "THRough"]

                            FILTer = FILTer()  # type: ignore
                            """
                            SOURce:RADio:AWGN:ARB:IQ:MODulation:FILTer

                            Arguments: <numeric_value>, THRough
                            """

                        MODulation = MODulation()  # type: ignore
                        """
                        SOURce:RADio:AWGN:ARB:IQ:MODulation

                        Arguments:
                        """

                    IQ = IQ()  # type: ignore
                    """
                    SOURce:RADio:AWGN:ARB:IQ

                    Arguments:
                    """

                    class LENGth(SCPINode, SCPIQuery):
                        """
                        SOURce:RADio:AWGN:ARB:LENGth

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "LENGth"
                        args = []  # type: List[str]

                    LENGth = LENGth()  # type: ignore
                    """
                    SOURce:RADio:AWGN:ARB:LENGth

                    Arguments:
                    """

                    class MDEStination(SCPINode, SCPISet):
                        """
                        SOURce:RADio:AWGN:ARB:MDEStination

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "MDEStination"
                        args = []  # type: List[str]

                        class AAMPlitude(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:MDEStination:AAMPlitude

                            Arguments: M1, M2, M3, M4, NONE
                            """
                            __slots__ = ()
                            _cmd = "AAMPlitude"
                            args = ["M1", "M2", "M3", "M4", "NONE"]

                        AAMPlitude = AAMPlitude()  # type: ignore
                        """
                        SOURce:RADio:AWGN:ARB:MDEStination:AAMPlitude

                        Arguments: M1, M2, M3, M4, NONE
                        """

                        class ALCHold(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:MDEStination:ALCHold

                            Arguments: M1, M2, M3, M4, NONE
                            """
                            __slots__ = ()
                            _cmd = "ALCHold"
                            args = ["M1", "M2", "M3", "M4", "NONE"]

                        ALCHold = ALCHold()  # type: ignore
                        """
                        SOURce:RADio:AWGN:ARB:MDEStination:ALCHold

                        Arguments: M1, M2, M3, M4, NONE
                        """

                        class PULSe(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:MDEStination:PULSe

                            Arguments: M1, M2, M3, M4, NONE
                            """
                            __slots__ = ()
                            _cmd = "PULSe"
                            args = ["M1", "M2", "M3", "M4", "NONE"]

                        PULSe = PULSe()  # type: ignore
                        """
                        SOURce:RADio:AWGN:ARB:MDEStination:PULSe

                        Arguments: M1, M2, M3, M4, NONE
                        """

                    MDEStination = MDEStination()  # type: ignore
                    """
                    SOURce:RADio:AWGN:ARB:MDEStination

                    Arguments:
                    """

                    class MPOLartity(SCPINode, SCPISet):
                        """
                        SOURce:RADio:AWGN:ARB:MPOLartity

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "MPOLartity"
                        args = []  # type: List[str]

                        class MARKer(SCPINodeN, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:MPOLartity:MARKer

                            Arguments: NEGative, POSitive
                            """
                            __slots__ = ()
                            _cmd = "MARKer"
                            args = ["NEGative", "POSitive"]

                        MARKer = MARKer()  # type: ignore
                        """
                        SOURce:RADio:AWGN:ARB:MPOLartity:MARKer

                        Arguments: NEGative, POSitive
                        """

                    MPOLartity = MPOLartity()  # type: ignore
                    """
                    SOURce:RADio:AWGN:ARB:MPOLartity

                    Arguments:
                    """

                    class REFerence(SCPINode):
                        """
                        SOURce:RADio:AWGN:ARB:REFerence

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "REFerence"
                        args = []  # type: List[str]

                        class EXTernal(SCPINode, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:REFerence:EXTernal

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "EXTernal"
                            args = []  # type: List[str]

                            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:AWGN:ARB:REFerence:EXTernal:FREQuency

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "FREQuency"
                                args = ["1"]

                            FREQuency = FREQuency()  # type: ignore
                            """
                            SOURce:RADio:AWGN:ARB:REFerence:EXTernal:FREQuency

                            Arguments: 1
                            """

                        EXTernal = EXTernal()  # type: ignore
                        """
                        SOURce:RADio:AWGN:ARB:REFerence:EXTernal

                        Arguments:
                        """

                        class SOURce(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:REFerence:SOURce

                            Arguments: EXTernal, INTernal
                            """
                            __slots__ = ()
                            _cmd = "SOURce"
                            args = ["EXTernal", "INTernal"]

                        SOURce = SOURce()  # type: ignore
                        """
                        SOURce:RADio:AWGN:ARB:REFerence:SOURce

                        Arguments: EXTernal, INTernal
                        """

                    REFerence = REFerence()  # type: ignore
                    """
                    SOURce:RADio:AWGN:ARB:REFerence

                    Arguments:
                    """

                    class SCLock(SCPINode, SCPISet):
                        """
                        SOURce:RADio:AWGN:ARB:SCLock

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "SCLock"
                        args = []  # type: List[str]

                    SCLock = SCLock()  # type: ignore
                    """
                    SOURce:RADio:AWGN:ARB:SCLock

                    Arguments:
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:RADio:AWGN:ARB:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SOURce:RADio:AWGN:ARB:STATe

                    Arguments: 1, ON, OFF
                    """

                ARB = ARB()  # type: ignore
                """
                SOURce:RADio:AWGN:ARB

                Arguments:
                """

                class RT(SCPINode):
                    """
                    SOURce:RADio:AWGN:RT

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "RT"
                    args = []  # type: List[str]

                    class BWIDth(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:AWGN:RT:BWIDth

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "BWIDth"
                        args = ["1"]

                    BWIDth = BWIDth()  # type: ignore
                    """
                    SOURce:RADio:AWGN:RT:BWIDth

                    Arguments: 1
                    """

                    class IQ(SCPINode):
                        """
                        SOURce:RADio:AWGN:RT:IQ

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "IQ"
                        args = []  # type: List[str]

                        class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:RT:IQ:ATTenuation

                            Arguments: 1
                            """
                            __slots__ = ()
                            _cmd = "ATTenuation"
                            args = ["1"]

                        ATTenuation = ATTenuation()  # type: ignore
                        """
                        SOURce:RADio:AWGN:RT:IQ:ATTenuation

                        Arguments: 1
                        """

                    IQ = IQ()  # type: ignore
                    """
                    SOURce:RADio:AWGN:RT:IQ

                    Arguments:
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:RADio:AWGN:RT:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SOURce:RADio:AWGN:RT:STATe

                    Arguments: 1, ON, OFF
                    """

                RT = RT()  # type: ignore
                """
                SOURce:RADio:AWGN:RT

                Arguments:
                """

            AWGN = AWGN()  # type: ignore
            """
            SOURce:RADio:AWGN

            Arguments:
            """

            class MTONe(SCPINode):
                """
                SOURce:RADio:MTONe

                Arguments:
                """
                __slots__ = ()
                _cmd = "MTONe"
                args = []  # type: List[str]

                class ARB(SCPINode):
                    """
                    SOURce:RADio:MTONe:ARB

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ARB"
                    args = []  # type: List[str]

                    class REFerence(SCPINode):
                        """
                        SOURce:RADio:MTONe:ARB:REFerence

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "REFerence"
                        args = []  # type: List[str]

                        class EXTernal(SCPINode, SCPISet):
                            """
                            SOURce:RADio:MTONe:ARB:REFerence:EXTernal

                            Arguments:
                            """
                            __slots__ = ()
                            _cmd = "EXTernal"
                            args = []  # type: List[str]

                            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:MTONe:ARB:REFerence:EXTernal:FREQuency

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "FREQuency"
                                args = ["1"]

                            FREQuency = FREQuency()  # type: ignore
                            """
                            SOURce:RADio:MTONe:ARB:REFerence:EXTernal:FREQuency

                            Arguments: 1
                            """

                        EXTernal = EXTernal()  # type: ignore
                        """
                        SOURce:RADio:MTONe:ARB:REFerence:EXTernal

                        Arguments:
                        """

                        class SOURce(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:MTONe:ARB:REFerence:SOURce

                            Arguments: EXTernal, INTernal
                            """
                            __slots__ = ()
                            _cmd = "SOURce"
                            args = ["EXTernal", "INTernal"]

                        SOURce = SOURce()  # type: ignore
                        """
                        SOURce:RADio:MTONe:ARB:REFerence:SOURce

                        Arguments: EXTernal, INTernal
                        """

                    REFerence = REFerence()  # type: ignore
                    """
                    SOURce:RADio:MTONe:ARB:REFerence

                    Arguments:
                    """

                    class SCLock(SCPINode, SCPISet):
                        """
                        SOURce:RADio:MTONe:ARB:SCLock

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "SCLock"
                        args = []  # type: List[str]

                    SCLock = SCLock()  # type: ignore
                    """
                    SOURce:RADio:MTONe:ARB:SCLock

                    Arguments:
                    """

                    class SETup(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:MTONe:ARB:SETup

                        Arguments: 'string'
                        """
                        __slots__ = ()
                        _cmd = "SETup"
                        args = ["'string'"]

                        class STORe(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:MTONe:ARB:SETup:STORe

                            Arguments: 'string'
                            """
                            __slots__ = ()
                            _cmd = "STORe"
                            args = ["'string'"]

                        STORe = STORe()  # type: ignore
                        """
                        SOURce:RADio:MTONe:ARB:SETup:STORe

                        Arguments: 'string'
                        """

                        class TABLe(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:MTONe:ARB:SETup:TABLe

                            Arguments: <numeric_value>,<numeric_value>,FIXed, RANDom,<boolean>
                            """
                            __slots__ = ()
                            _cmd = "TABLe"
                            args = ["<numeric_value>,<numeric_value>,FIXed", "RANDom,<boolean>"]

                            class FSPacing(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:MTONe:ARB:SETup:TABLe:FSPacing

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "FSPacing"
                                args = ["1"]

                            FSPacing = FSPacing()  # type: ignore
                            """
                            SOURce:RADio:MTONe:ARB:SETup:TABLe:FSPacing

                            Arguments: 1
                            """

                            class NTONes(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:MTONe:ARB:SETup:TABLe:NTONes

                                Arguments: 1
                                """
                                __slots__ = ()
                                _cmd = "NTONes"
                                args = ["1"]

                            NTONes = NTONes()  # type: ignore
                            """
                            SOURce:RADio:MTONe:ARB:SETup:TABLe:NTONes

                            Arguments: 1
                            """

                            class PHASe(SCPINode):
                                """
                                SOURce:RADio:MTONe:ARB:SETup:TABLe:PHASe

                                Arguments:
                                """
                                __slots__ = ()
                                _cmd = "PHASe"
                                args = []  # type: List[str]

                                class INITialize(SCPINode, SCPIQuery, SCPISet):
                                    """
                                    SOURce:RADio:MTONe:ARB:SETup:TABLe:PHASe:INITialize

                                    Arguments: FIXed, RANDom
                                    """
                                    __slots__ = ()
                                    _cmd = "INITialize"
                                    args = ["FIXed", "RANDom"]

                                INITialize = INITialize()  # type: ignore
                                """
                                SOURce:RADio:MTONe:ARB:SETup:TABLe:PHASe:INITialize

                                Arguments: FIXed, RANDom
                                """

                            PHASe = PHASe()  # type: ignore
                            """
                            SOURce:RADio:MTONe:ARB:SETup:TABLe:PHASe

                            Arguments:
                            """

                        TABLe = TABLe()  # type: ignore
                        """
                        SOURce:RADio:MTONe:ARB:SETup:TABLe

                        Arguments: <numeric_value>,<numeric_value>,FIXed, RANDom,<boolean>
                        """

                    SETup = SETup()  # type: ignore
                    """
                    SOURce:RADio:MTONe:ARB:SETup

                    Arguments: 'string'
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:RADio:MTONe:ARB:STATe

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    SOURce:RADio:MTONe:ARB:STATe

                    Arguments: 1, ON, OFF
                    """

                ARB = ARB()  # type: ignore
                """
                SOURce:RADio:MTONe:ARB

                Arguments:
                """

            MTONe = MTONe()  # type: ignore
            """
            SOURce:RADio:MTONe

            Arguments:
            """

        RADio = RADio()  # type: ignore
        """
        SOURce:RADio

        Arguments:
        """

        class ROSCillator(SCPINode, SCPISet):
            """
            SOURce:ROSCillator

            Arguments:
            """
            __slots__ = ()
            _cmd = "ROSCillator"
            args = []  # type: List[str]

            class EXTernal(SCPINode):
                """
                SOURce:ROSCillator:EXTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "EXTernal"
                args = []  # type: List[str]

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:ROSCillator:EXTernal:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/17d3920a3880443f.htm#ID_4f9594624e4ad9290a00206a017105ad-77092b4a4e4acb8d0a00206a00a0c7ed-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()  # type: ignore
                """
                `SOURce:ROSCillator:EXTernal:FREQuency
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/17d3920a3880443f.htm#ID_4f9594624e4ad9290a00206a017105ad-77092b4a4e4acb8d0a00206a00a0c7ed-en-US>`_

                Arguments: 1
                """

            EXTernal = EXTernal()  # type: ignore
            """
            SOURce:ROSCillator:EXTernal

            Arguments:
            """

            class FREQuency(SCPINode):
                """
                SOURce:ROSCillator:FREQuency

                Arguments:
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = []  # type: List[str]

                class EXTernal(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ROSCillator:FREQuency:EXTernal

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "EXTernal"
                    args = ["1"]

                EXTernal = EXTernal()  # type: ignore
                """
                SOURce:ROSCillator:FREQuency:EXTernal

                Arguments: 1
                """

            FREQuency = FREQuency()  # type: ignore
            """
            SOURce:ROSCillator:FREQuency

            Arguments:
            """

            class INTernal(SCPINode):
                """
                SOURce:ROSCillator:INTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "INTernal"
                args = []  # type: List[str]

                class ADJust(SCPINode):
                    """
                    SOURce:ROSCillator:INTernal:ADJust

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ADJust"
                    args = []  # type: List[str]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:ROSCillator:INTernal:ADJust:STATe
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b90515af7a4f4c94.htm#ID_d64368ec5700fce10a00206a014cb621-3792892e5700fce10a00206a0024546d-en-US>`_

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    `SOURce:ROSCillator:INTernal:ADJust:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b90515af7a4f4c94.htm#ID_d64368ec5700fce10a00206a014cb621-3792892e5700fce10a00206a0024546d-en-US>`_

                    Arguments: 1, ON, OFF
                    """

                    class VALue(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:ROSCillator:INTernal:ADJust:VALue
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/77691a4f94ac4ffc.htm#ID_a0023e065701029d0a00206a00d2b42c-b2019cd95701029d0a00206a0024546d-en-US>`_

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "VALue"
                        args = ["1"]

                    VALue = VALue()  # type: ignore
                    """
                    `SOURce:ROSCillator:INTernal:ADJust:VALue
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/77691a4f94ac4ffc.htm#ID_a0023e065701029d0a00206a00d2b42c-b2019cd95701029d0a00206a0024546d-en-US>`_

                    Arguments: 1
                    """

                ADJust = ADJust()  # type: ignore
                """
                SOURce:ROSCillator:INTernal:ADJust

                Arguments:
                """

                class RLOop(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ROSCillator:INTernal:RLOop

                    Arguments: NARRow, NORMal
                    """
                    __slots__ = ()
                    _cmd = "RLOop"
                    args = ["NARRow", "NORMal"]

                RLOop = RLOop()  # type: ignore
                """
                SOURce:ROSCillator:INTernal:RLOop

                Arguments: NARRow, NORMal
                """

            INTernal = INTernal()  # type: ignore
            """
            SOURce:ROSCillator:INTernal

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:ROSCillator:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7e935bcba7104491.htm#ID_f861c84a5700f7140a00206a01a37e10-f799abd25700f7140a00206a0024546d-en-US>`_

                Arguments: <numeric_value>,EXTernal
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["<numeric_value>,EXTernal"]

            SOURce = SOURce()  # type: ignore
            """
            `SOURce:ROSCillator:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7e935bcba7104491.htm#ID_f861c84a5700f7140a00206a01a37e10-f799abd25700f7140a00206a0024546d-en-US>`_

            Arguments: <numeric_value>,EXTernal
            """

        ROSCillator = ROSCillator()  # type: ignore
        """
        SOURce:ROSCillator

        Arguments:
        """

        class STEReo(SCPINode):
            """
            SOURce:STEReo

            Arguments:
            """
            __slots__ = ()
            _cmd = "STEReo"
            args = []  # type: List[str]

            class ARI(SCPINode):
                """
                SOURce:STEReo:ARI

                Arguments:
                """
                __slots__ = ()
                _cmd = "ARI"
                args = []  # type: List[str]

                class DEViation(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:ARI:DEViation
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/282a6e62f9164949.htm#ID_67dca7c4dc5bae370a00206a01e854e0-3da4a2e5dc5ba6c50a00206a01e40e15-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DEViation"
                    args = ["1"]

                DEViation = DEViation()  # type: ignore
                """
                `SOURce:STEReo:ARI:DEViation
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/282a6e62f9164949.htm#ID_67dca7c4dc5bae370a00206a01e854e0-3da4a2e5dc5ba6c50a00206a01e40e15-en-US>`_

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:STEReo:ARI:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/998508dfe46e41f8.htm#ID_b2a4f8bedc5bbe640a00206a0027a4ab-9631aac2dc5bb8970a00206a01e40e15-en-US>`_

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                `SOURce:STEReo:ARI:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/998508dfe46e41f8.htm#ID_b2a4f8bedc5bbe640a00206a0027a4ab-9631aac2dc5bb8970a00206a01e40e15-en-US>`_

                Arguments: 1, ON, OFF
                """

                class TYPE(SCPINode):
                    """
                    `SOURce:STEReo:ARI:TYPE
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5f0c571ed0204179.htm#ID_37f62275dc5bb6840a00206a00c7669c-3f459759dc5bb0a80a00206a01e40e15-en-US>`_

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "TYPE"
                    args = []  # type: List[str]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:STEReo:ARI:TYPE:STATe
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/756911e513c34c67.htm#ID_c14f788bdc5c68bd0a00206a01bbc148-6c884fb2dc5c61d70a00206a01e40e15-en-US>`_

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    `SOURce:STEReo:ARI:TYPE:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/756911e513c34c67.htm#ID_c14f788bdc5c68bd0a00206a01bbc148-6c884fb2dc5c61d70a00206a01e40e15-en-US>`_

                    Arguments: 1, ON, OFF
                    """

                TYPE = TYPE()  # type: ignore
                """
                `SOURce:STEReo:ARI:TYPE
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5f0c571ed0204179.htm#ID_37f62275dc5bb6840a00206a00c7669c-3f459759dc5bb0a80a00206a01e40e15-en-US>`_

                Arguments:
                """

            ARI = ARI()  # type: ignore
            """
            SOURce:STEReo:ARI

            Arguments:
            """

            class AUDio(SCPINode):
                """
                SOURce:STEReo:AUDio

                Arguments:
                """
                __slots__ = ()
                _cmd = "AUDio"
                args = []  # type: List[str]

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:AUDio:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b27b0233d15c4e70.htm#ID_7cfbf44adc5bdd070a00206a00bdbc74-df188684dc5bd76a0a00206a01e40e15-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()  # type: ignore
                """
                `SOURce:STEReo:AUDio:FREQuency
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b27b0233d15c4e70.htm#ID_7cfbf44adc5bdd070a00206a00bdbc74-df188684dc5bd76a0a00206a01e40e15-en-US>`_

                Arguments: 1
                """

                class PREemphasis(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:AUDio:PREemphasis
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/652eea05e2f24016.htm#ID_5566f910dc5c399e0a00206a00781b8b-d08a4926dc5c33c20a00206a01e40e15-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PREemphasis"
                    args = ["1"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:STEReo:AUDio:PREemphasis:STATe
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/cc35ff90b52c4122.htm#ID_de10a50cdc5c02ee0a00206a0029bde5-ece51530dc5bfd510a00206a01e40e15-en-US>`_

                        Arguments: 1, ON, OFF
                        """
                        __slots__ = ()
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()  # type: ignore
                    """
                    `SOURce:STEReo:AUDio:PREemphasis:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/cc35ff90b52c4122.htm#ID_de10a50cdc5c02ee0a00206a0029bde5-ece51530dc5bfd510a00206a01e40e15-en-US>`_

                    Arguments: 1, ON, OFF
                    """

                PREemphasis = PREemphasis()  # type: ignore
                """
                `SOURce:STEReo:AUDio:PREemphasis
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/652eea05e2f24016.htm#ID_5566f910dc5c399e0a00206a00781b8b-d08a4926dc5c33c20a00206a01e40e15-en-US>`_

                Arguments: 1
                """

            AUDio = AUDio()  # type: ignore
            """
            SOURce:STEReo:AUDio

            Arguments:
            """

            class DEViation(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:STEReo:DEViation
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/77bf3680cacd45eb.htm#ID_cc254567dc5bcdd50a00206a00015f03-191cccafdc5bc8470a00206a01e40e15-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DEViation"
                args = ["1"]

            DEViation = DEViation()  # type: ignore
            """
            `SOURce:STEReo:DEViation
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/77bf3680cacd45eb.htm#ID_cc254567dc5bcdd50a00206a00015f03-191cccafdc5bc8470a00206a01e40e15-en-US>`_

            Arguments: 1
            """

            class DIRect(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:STEReo:DIRect
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/8b97704e30ca4cf8.htm#ID_6bdc62a3dc5c50530a00206a007b4a30-09b6e1c4dc5c4a860a00206a01e40e15-en-US>`_

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "DIRect"
                args = ["'string'"]

            DIRect = DIRect()  # type: ignore
            """
            `SOURce:STEReo:DIRect
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/8b97704e30ca4cf8.htm#ID_6bdc62a3dc5c50530a00206a007b4a30-09b6e1c4dc5c4a860a00206a01e40e15-en-US>`_

            Arguments: 'string'
            """

            class EXTernal(SCPINode):
                """
                SOURce:STEReo:EXTernal

                Arguments:
                """
                __slots__ = ()
                _cmd = "EXTernal"
                args = []  # type: List[str]

                class IMPedance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:EXTernal:IMPedance
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bf3bd3cb1b6149d7.htm#ID_ed166f71dc5bd5470a00206a00084298-5934d87ddc5bcfc90a00206a01e40e15-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()  # type: ignore
                """
                `SOURce:STEReo:EXTernal:IMPedance
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bf3bd3cb1b6149d7.htm#ID_ed166f71dc5bd5470a00206a00084298-5934d87ddc5bcfc90a00206a01e40e15-en-US>`_

                Arguments: 1
                """

            EXTernal = EXTernal()  # type: ignore
            """
            SOURce:STEReo:EXTernal

            Arguments:
            """

            class PILot(SCPINode):
                """
                SOURce:STEReo:PILot

                Arguments:
                """
                __slots__ = ()
                _cmd = "PILot"
                args = []  # type: List[str]

                class DEViation(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:PILot:DEViation
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/9109ab9c9a614b96.htm#ID_a3761f9bdc5bec4a0a00206a00716dbf-840e2c0cdc5be6ac0a00206a01e40e15-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DEViation"
                    args = ["1"]

                DEViation = DEViation()  # type: ignore
                """
                `SOURce:STEReo:PILot:DEViation
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/9109ab9c9a614b96.htm#ID_a3761f9bdc5bec4a0a00206a00716dbf-840e2c0cdc5be6ac0a00206a01e40e15-en-US>`_

                Arguments: 1
                """

                class PHASe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:PILot:PHASe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/10f108b19f624a5e.htm#ID_86f8bd04dc5bf3cb0a00206a017fdfc9-c5314867dc5bee1e0a00206a01e40e15-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PHASe"
                    args = ["1"]

                PHASe = PHASe()  # type: ignore
                """
                `SOURce:STEReo:PILot:PHASe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/10f108b19f624a5e.htm#ID_86f8bd04dc5bf3cb0a00206a017fdfc9-c5314867dc5bee1e0a00206a01e40e15-en-US>`_

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:STEReo:PILot:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/068535fbf91146eb.htm#ID_31ee9df8dc5bfb7c0a00206a0160f2b2-1b5f0342dc5bf5cf0a00206a01e40e15-en-US>`_

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                `SOURce:STEReo:PILot:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/068535fbf91146eb.htm#ID_31ee9df8dc5bfb7c0a00206a0160f2b2-1b5f0342dc5bf5cf0a00206a01e40e15-en-US>`_

                Arguments: 1, ON, OFF
                """

            PILot = PILot()  # type: ignore
            """
            SOURce:STEReo:PILot

            Arguments:
            """

            class RDS(SCPINode):
                """
                SOURce:STEReo:RDS

                Arguments:
                """
                __slots__ = ()
                _cmd = "RDS"
                args = []  # type: List[str]

                class DATaset(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:RDS:DATaset
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b0c13bb102454957.htm#ID_fd8383cedc5c0a700a00206a01b75b79-fe5583efdc5c04f20a00206a01e40e15-en-US>`_

                    Arguments: DS1, DS2, DS3, DS4, DS5
                    """
                    __slots__ = ()
                    _cmd = "DATaset"
                    args = ["DS1", "DS2", "DS3", "DS4", "DS5"]

                DATaset = DATaset()  # type: ignore
                """
                `SOURce:STEReo:RDS:DATaset
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b0c13bb102454957.htm#ID_fd8383cedc5c0a700a00206a01b75b79-fe5583efdc5c04f20a00206a01e40e15-en-US>`_

                Arguments: DS1, DS2, DS3, DS4, DS5
                """

                class DEViation(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:RDS:DEViation
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2bf5650ffdc14b35.htm#ID_2974ecc1dc5c11d30a00206a003a95cb-e42b5a1cdc5c0c550a00206a01e40e15-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DEViation"
                    args = ["1"]

                DEViation = DEViation()  # type: ignore
                """
                `SOURce:STEReo:RDS:DEViation
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2bf5650ffdc14b35.htm#ID_2974ecc1dc5c11d30a00206a003a95cb-e42b5a1cdc5c0c550a00206a01e40e15-en-US>`_

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:STEReo:RDS:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/1d512496e30b4ccd.htm#ID_558b5e83dc5c19640a00206a01d4d2e2-38f90b46dc5c13c70a00206a01e40e15-en-US>`_

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                `SOURce:STEReo:RDS:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/1d512496e30b4ccd.htm#ID_558b5e83dc5c19640a00206a01d4d2e2-38f90b46dc5c13c70a00206a01e40e15-en-US>`_

                Arguments: 1, ON, OFF
                """

                class TRAFfic(SCPINode):
                    """
                    SOURce:STEReo:RDS:TRAFfic

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "TRAFfic"
                    args = []  # type: List[str]

                    class ANNouncement(SCPINode):
                        """
                        SOURce:STEReo:RDS:TRAFfic:ANNouncement

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "ANNouncement"
                        args = []  # type: List[str]

                        class STATe(SCPINode, SCPIBool):
                            """
                            `SOURce:STEReo:RDS:TRAFfic:ANNouncement:STATe
                            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f5a48f2b2e614615.htm#ID_c2dea175dc5c29df0a00206a002c754e-e0bb6433dc5c24030a00206a01e40e15-en-US>`_

                            Arguments: 1, ON, OFF
                            """
                            __slots__ = ()
                            _cmd = "STATe"
                            args = ["1", "ON", "OFF"]

                        STATe = STATe()  # type: ignore
                        """
                        `SOURce:STEReo:RDS:TRAFfic:ANNouncement:STATe
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f5a48f2b2e614615.htm#ID_c2dea175dc5c29df0a00206a002c754e-e0bb6433dc5c24030a00206a01e40e15-en-US>`_

                        Arguments: 1, ON, OFF
                        """

                    ANNouncement = ANNouncement()  # type: ignore
                    """
                    SOURce:STEReo:RDS:TRAFfic:ANNouncement

                    Arguments:
                    """

                    class PROGram(SCPINode):
                        """
                        SOURce:STEReo:RDS:TRAFfic:PROGram

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "PROGram"
                        args = []  # type: List[str]

                        class STATe(SCPINode, SCPIBool):
                            """
                            `SOURce:STEReo:RDS:TRAFfic:PROGram:STATe
                            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/6ba7f2ecc27b414b.htm#ID_2d18a912dc5c20d70a00206a00bd6c38-6bbab9b0dc5c1b580a00206a01e40e15-en-US>`_

                            Arguments: 1, ON, OFF
                            """
                            __slots__ = ()
                            _cmd = "STATe"
                            args = ["1", "ON", "OFF"]

                        STATe = STATe()  # type: ignore
                        """
                        `SOURce:STEReo:RDS:TRAFfic:PROGram:STATe
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/6ba7f2ecc27b414b.htm#ID_2d18a912dc5c20d70a00206a00bd6c38-6bbab9b0dc5c1b580a00206a01e40e15-en-US>`_

                        Arguments: 1, ON, OFF
                        """

                    PROGram = PROGram()  # type: ignore
                    """
                    SOURce:STEReo:RDS:TRAFfic:PROGram

                    Arguments:
                    """

                TRAFfic = TRAFfic()  # type: ignore
                """
                SOURce:STEReo:RDS:TRAFfic

                Arguments:
                """

            RDS = RDS()  # type: ignore
            """
            SOURce:STEReo:RDS

            Arguments:
            """

            class SIGNal(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:STEReo:SIGNal

                Arguments: ARI, AUDio
                """
                __slots__ = ()
                _cmd = "SIGNal"
                args = ["ARI", "AUDio"]

            SIGNal = SIGNal()  # type: ignore
            """
            SOURce:STEReo:SIGNal

            Arguments: ARI, AUDio
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:STEReo:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/69d8d93fd9a343d4.htm#ID_e61a5b08dc5c31900a00206a01f29de2-10435111dc5c2bf20a00206a01e40e15-en-US>`_

                Arguments: LFGen, LREXt, SPEXt
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["LFGen", "LREXt", "SPEXt"]

            SOURce = SOURce()  # type: ignore
            """
            `SOURce:STEReo:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/69d8d93fd9a343d4.htm#ID_e61a5b08dc5c31900a00206a01f29de2-10435111dc5c2bf20a00206a01e40e15-en-US>`_

            Arguments: LFGen, LREXt, SPEXt
            """

            class STATe(SCPINode, SCPIBool):
                """
                `SOURce:STEReo:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/1e7f50df80754d97.htm#ID_755ff102dc5c48920a00206a00d7b608-7df2c8b4dc5c42f50a00206a01e40e15-en-US>`_

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            `SOURce:STEReo:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/1e7f50df80754d97.htm#ID_755ff102dc5c48920a00206a00d7b608-7df2c8b4dc5c42f50a00206a01e40e15-en-US>`_

            Arguments: 1, ON, OFF
            """

        STEReo = STEReo()  # type: ignore
        """
        SOURce:STEReo

        Arguments:
        """

        class SWEep(SCPINode, SCPISet):
            """
            SOURce:SWEep

            Arguments:
            """
            __slots__ = ()
            _cmd = "SWEep"
            args = []  # type: List[str]

            class BTIMe(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:BTIMe

                Arguments: LONG, NORMal
                """
                __slots__ = ()
                _cmd = "BTIMe"
                args = ["LONG", "NORMal"]

            BTIMe = BTIMe()  # type: ignore
            """
            SOURce:SWEep:BTIMe

            Arguments: LONG, NORMal
            """

            class CONTrol(SCPINode, SCPISet):
                """
                SOURce:SWEep:CONTrol

                Arguments:
                """
                __slots__ = ()
                _cmd = "CONTrol"
                args = []  # type: List[str]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:SWEep:CONTrol:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:SWEep:CONTrol:STATe

                Arguments: 1, ON, OFF
                """

            CONTrol = CONTrol()  # type: ignore
            """
            SOURce:SWEep:CONTrol

            Arguments:
            """

            class CPOint(SCPINode, SCPIQuery):
                """
                SOURce:SWEep:CPOint

                Arguments:
                """
                __slots__ = ()
                _cmd = "CPOint"
                args = []  # type: List[str]

            CPOint = CPOint()  # type: ignore
            """
            SOURce:SWEep:CPOint

            Arguments:
            """

            class DIRection(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:DIRection

                Arguments: DOWN, UP
                """
                __slots__ = ()
                _cmd = "DIRection"
                args = ["DOWN", "UP"]

            DIRection = DIRection()  # type: ignore
            """
            SOURce:SWEep:DIRection

            Arguments: DOWN, UP
            """

            class DWELl(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:DWELl

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DWELl"
                args = ["1"]

            DWELl = DWELl()  # type: ignore
            """
            SOURce:SWEep:DWELl

            Arguments: 1
            """

            class FREQuency(SCPINode, SCPISet):
                """
                SOURce:SWEep:FREQuency

                Arguments:
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = []  # type: List[str]

                class DWELl(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:SWEep:FREQuency:DWELl
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/422723d8553c40b3.htm#ID_22f1352871b719430a00206a01ebbac9-df858e4171b719430a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DWELl"
                    args = ["1"]

                DWELl = DWELl()  # type: ignore
                """
                `SOURce:SWEep:FREQuency:DWELl
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/422723d8553c40b3.htm#ID_22f1352871b719430a00206a01ebbac9-df858e4171b719430a00206a012bc823-en-US>`_

                Arguments: 1
                """

                class POINts(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:SWEep:FREQuency:POINts
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5c7c5b5057a640f2.htm#ID_c2b0cb6871b70bc50a00206a0181b01c-efb3999b71b70bd50a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "POINts"
                    args = ["1"]

                POINts = POINts()  # type: ignore
                """
                `SOURce:SWEep:FREQuency:POINts
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5c7c5b5057a640f2.htm#ID_c2b0cb6871b70bc50a00206a0181b01c-efb3999b71b70bd50a00206a012bc823-en-US>`_

                Arguments: 1
                """

                class RUNNing(SCPINode, SCPIQuery):
                    """
                    `SOURce:SWEep:FREQuency:RUNNing
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/03da63933dbb4b18.htm#ID_0b005d4bed649e6a0a002019017c48d8-40c7ed4fed649aef0a00201900ba4ad4-en-US>`_

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "RUNNing"
                    args = []  # type: List[str]

                RUNNing = RUNNing()  # type: ignore
                """
                `SOURce:SWEep:FREQuency:RUNNing
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/03da63933dbb4b18.htm#ID_0b005d4bed649e6a0a002019017c48d8-40c7ed4fed649aef0a00201900ba4ad4-en-US>`_

                Arguments:
                """

                class SPACing(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:SWEep:FREQuency:SPACing
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/4cac97cd94264483.htm#ID_8d191a9771b7127c0a00206a01d897a9-0439662f71b7127c0a00206a012bc823-en-US>`_

                    Arguments: LINear, LOGarithmic
                    """
                    __slots__ = ()
                    _cmd = "SPACing"
                    args = ["LINear", "LOGarithmic"]

                SPACing = SPACing()  # type: ignore
                """
                `SOURce:SWEep:FREQuency:SPACing
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/4cac97cd94264483.htm#ID_8d191a9771b7127c0a00206a01d897a9-0439662f71b7127c0a00206a012bc823-en-US>`_

                Arguments: LINear, LOGarithmic
                """

                class STEP(SCPINode):
                    """
                    SOURce:SWEep:FREQuency:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class LINear(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:SWEep:FREQuency:STEP:LINear
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/6eeae32a24f148ac.htm#ID_019e085071b6fe580a00206a0078468a-5813ce6a71b6fe580a00206a012bc823-en-US>`_

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "LINear"
                        args = ["1"]

                    LINear = LINear()  # type: ignore
                    """
                    `SOURce:SWEep:FREQuency:STEP:LINear
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/6eeae32a24f148ac.htm#ID_019e085071b6fe580a00206a0078468a-5813ce6a71b6fe580a00206a012bc823-en-US>`_

                    Arguments: 1
                    """

                    class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:SWEep:FREQuency:STEP:LOGarithmic
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/ccbae2d831df45b5.htm#ID_b055cff771b704e00a00206a0023865a-f2478ac071b704e00a00206a012bc823-en-US>`_

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()  # type: ignore
                    """
                    `SOURce:SWEep:FREQuency:STEP:LOGarithmic
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/ccbae2d831df45b5.htm#ID_b055cff771b704e00a00206a0023865a-f2478ac071b704e00a00206a012bc823-en-US>`_

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:SWEep:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()  # type: ignore
            """
            SOURce:SWEep:FREQuency

            Arguments:
            """

            class GENeration(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:GENeration

                Arguments: ANALog, STEPped
                """
                __slots__ = ()
                _cmd = "GENeration"
                args = ["ANALog", "STEPped"]

            GENeration = GENeration()  # type: ignore
            """
            SOURce:SWEep:GENeration

            Arguments: ANALog, STEPped
            """

            class MANual(SCPINode):
                """
                SOURce:SWEep:MANual

                Arguments:
                """
                __slots__ = ()
                _cmd = "MANual"
                args = []  # type: List[str]

                class POINt(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:SWEep:MANual:POINt

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "POINt"
                    args = ["1"]

                POINt = POINt()  # type: ignore
                """
                SOURce:SWEep:MANual:POINt

                Arguments: 1
                """

                class RELative(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:SWEep:MANual:RELative

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "RELative"
                    args = ["1"]

                RELative = RELative()  # type: ignore
                """
                SOURce:SWEep:MANual:RELative

                Arguments: 1
                """

            MANual = MANual()  # type: ignore
            """
            SOURce:SWEep:MANual

            Arguments:
            """

            class MARKer(SCPINode):
                """
                SOURce:SWEep:MARKer

                Arguments:
                """
                __slots__ = ()
                _cmd = "MARKer"
                args = []  # type: List[str]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:SWEep:MARKer:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:SWEep:MARKer:STATe

                Arguments: 1, ON, OFF
                """

            MARKer = MARKer()  # type: ignore
            """
            SOURce:SWEep:MARKer

            Arguments:
            """

            class POINts(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:POINts

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "POINts"
                args = ["1"]

            POINts = POINts()  # type: ignore
            """
            SOURce:SWEep:POINts

            Arguments: 1
            """

            class POWer(SCPINode, SCPISet):
                """
                SOURce:SWEep:POWer

                Arguments:
                """
                __slots__ = ()
                _cmd = "POWer"
                args = []  # type: List[str]

                class DWELl(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:SWEep:POWer:DWELl
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e0f78d0fb5574909.htm#ID_551ad14d71b750700a00206a0188e9b1-eacf1f4671b750700a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DWELl"
                    args = ["1"]

                DWELl = DWELl()  # type: ignore
                """
                `SOURce:SWEep:POWer:DWELl
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e0f78d0fb5574909.htm#ID_551ad14d71b750700a00206a0188e9b1-eacf1f4671b750700a00206a012bc823-en-US>`_

                Arguments: 1
                """

                class POINts(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:SWEep:POWer:POINts
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/dded827b58e54ae7.htm#ID_eeb8ce0071b7498a0a00206a019e8b48-f33619a371b7498a0a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "POINts"
                    args = ["1"]

                POINts = POINts()  # type: ignore
                """
                `SOURce:SWEep:POWer:POINts
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/dded827b58e54ae7.htm#ID_eeb8ce0071b7498a0a00206a019e8b48-f33619a371b7498a0a00206a012bc823-en-US>`_

                Arguments: 1
                """

                class RUNNing(SCPINode, SCPIQuery):
                    """
                    `SOURce:SWEep:POWer:RUNNing
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/09b06d6b82a34974.htm#ID_6d0752bced643a300a002019019e51e3-74da00c4ed64381d0a00201900ba4ad4-en-US>`_

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "RUNNing"
                    args = []  # type: List[str]

                RUNNing = RUNNing()  # type: ignore
                """
                `SOURce:SWEep:POWer:RUNNing
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/09b06d6b82a34974.htm#ID_6d0752bced643a300a002019019e51e3-74da00c4ed64381d0a00201900ba4ad4-en-US>`_

                Arguments:
                """

                class SPACing(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:SWEep:POWer:SPACing

                    Arguments: LOGarithmic
                    """
                    __slots__ = ()
                    _cmd = "SPACing"
                    args = ["LOGarithmic"]

                SPACing = SPACing()  # type: ignore
                """
                SOURce:SWEep:POWer:SPACing

                Arguments: LOGarithmic
                """

                class STEP(SCPINode):
                    """
                    SOURce:SWEep:POWer:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:SWEep:POWer:STEP:LOGarithmic
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7a028d77a0e64432.htm#ID_42b6782c71b757170a00206a01b31ca4-4dd4e73f71b757170a00206a012bc823-en-US>`_

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()  # type: ignore
                    """
                    `SOURce:SWEep:POWer:STEP:LOGarithmic
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7a028d77a0e64432.htm#ID_42b6782c71b757170a00206a01b31ca4-4dd4e73f71b757170a00206a012bc823-en-US>`_

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SOURce:SWEep:POWer:STEP

                Arguments:
                """

            POWer = POWer()  # type: ignore
            """
            SOURce:SWEep:POWer

            Arguments:
            """

            class SPACing(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:SPACing

                Arguments: LINear, LOGarithmic
                """
                __slots__ = ()
                _cmd = "SPACing"
                args = ["LINear", "LOGarithmic"]

            SPACing = SPACing()  # type: ignore
            """
            SOURce:SWEep:SPACing

            Arguments: LINear, LOGarithmic
            """

            class TIME(SCPINode):
                """
                SOURce:SWEep:TIME

                Arguments:
                """
                __slots__ = ()
                _cmd = "TIME"
                args = []  # type: List[str]

                class LLIMit(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:SWEep:TIME:LLIMit

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "LLIMit"
                    args = ["1"]

                LLIMit = LLIMit()  # type: ignore
                """
                SOURce:SWEep:TIME:LLIMit

                Arguments: 1
                """

            TIME = TIME()  # type: ignore
            """
            SOURce:SWEep:TIME

            Arguments:
            """

            class TRIGger(SCPINode):
                """
                SOURce:SWEep:TRIGger

                Arguments:
                """
                __slots__ = ()
                _cmd = "TRIGger"
                args = []  # type: List[str]

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:SWEep:TRIGger:SOURce

                    Arguments: BUS, EXTernal, IMMediate
                    """
                    __slots__ = ()
                    _cmd = "SOURce"
                    args = ["BUS", "EXTernal", "IMMediate"]

                SOURce = SOURce()  # type: ignore
                """
                SOURce:SWEep:TRIGger:SOURce

                Arguments: BUS, EXTernal, IMMediate
                """

            TRIGger = TRIGger()  # type: ignore
            """
            SOURce:SWEep:TRIGger

            Arguments:
            """

        SWEep = SWEep()  # type: ignore
        """
        SOURce:SWEep

        Arguments:
        """

        class TSWeep(SCPINode, SCPISet):
            """
            SOURce:TSWeep

            Arguments:
            """
            __slots__ = ()
            _cmd = "TSWeep"
            args = []  # type: List[str]

        TSWeep = TSWeep()  # type: ignore
        """
        SOURce:TSWeep

        Arguments:
        """

        class VOR(SCPINode):
            """
            SOURce:VOR

            Arguments:
            """
            __slots__ = ()
            _cmd = "VOR"
            args = []  # type: List[str]

            class BANGle(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:VOR:BANGle

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "BANGle"
                args = ["1"]

                class DIRection(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:BANGle:DIRection

                    Arguments: FROM, TO
                    """
                    __slots__ = ()
                    _cmd = "DIRection"
                    args = ["FROM", "TO"]

                DIRection = DIRection()  # type: ignore
                """
                SOURce:VOR:BANGle:DIRection

                Arguments: FROM, TO
                """

            BANGle = BANGle()  # type: ignore
            """
            SOURce:VOR:BANGle

            Arguments: 1
            """

            class COMid(SCPINode):
                """
                SOURce:VOR:COMid

                Arguments:
                """
                __slots__ = ()
                _cmd = "COMid"
                args = []  # type: List[str]

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:COMid:DEPTh

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()  # type: ignore
                """
                SOURce:VOR:COMid:DEPTh

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:COMid:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:VOR:COMid:FREQuency

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:VOR:COMid:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SOURce:VOR:COMid:STATe

                Arguments: 1, ON, OFF
                """

            COMid = COMid()  # type: ignore
            """
            SOURce:VOR:COMid

            Arguments:
            """

            class PRESet(SCPINode, SCPISet):
                """
                SOURce:VOR:PRESet

                Arguments:
                """
                __slots__ = ()
                _cmd = "PRESet"
                args = []  # type: List[str]

            PRESet = PRESet()  # type: ignore
            """
            SOURce:VOR:PRESet

            Arguments:
            """

            class REFerence(SCPINode):
                """
                SOURce:VOR:REFerence

                Arguments:
                """
                __slots__ = ()
                _cmd = "REFerence"
                args = []  # type: List[str]

                class DEViation(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:REFerence:DEViation

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DEViation"
                    args = ["1"]

                DEViation = DEViation()  # type: ignore
                """
                SOURce:VOR:REFerence:DEViation

                Arguments: 1
                """

            REFerence = REFerence()  # type: ignore
            """
            SOURce:VOR:REFerence

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:VOR:SOURce

                Arguments: INT2, INTernal2,EXTernal
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["INT2", "INTernal2,EXTernal"]

            SOURce = SOURce()  # type: ignore
            """
            SOURce:VOR:SOURce

            Arguments: INT2, INTernal2,EXTernal
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:VOR:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SOURce:VOR:STATe

            Arguments: 1, ON, OFF
            """

            class SUBCarrier(SCPINode):
                """
                SOURce:VOR:SUBCarrier

                Arguments:
                """
                __slots__ = ()
                _cmd = "SUBCarrier"
                args = []  # type: List[str]

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:SUBCarrier:DEPTh

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()  # type: ignore
                """
                SOURce:VOR:SUBCarrier:DEPTh

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:SUBCarrier:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:VOR:SUBCarrier:FREQuency

                Arguments: 1
                """

            SUBCarrier = SUBCarrier()  # type: ignore
            """
            SOURce:VOR:SUBCarrier

            Arguments:
            """

            class VAR(SCPINode):
                """
                SOURce:VOR:VAR

                Arguments:
                """
                __slots__ = ()
                _cmd = "VAR"
                args = []  # type: List[str]

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:VAR:DEPTh

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()  # type: ignore
                """
                SOURce:VOR:VAR:DEPTh

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:VAR:FREQuency

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()  # type: ignore
                """
                SOURce:VOR:VAR:FREQuency

                Arguments: 1
                """

            VAR = VAR()  # type: ignore
            """
            SOURce:VOR:VAR

            Arguments:
            """

        VOR = VOR()  # type: ignore
        """
        SOURce:VOR

        Arguments:
        """

    SOURce = SOURce()  # type: ignore
    """
    SOURce

    Arguments:
    """

    class SPecial_functio(SCPINode, SCPIQuery, SCPISet):
        """
        SPecial_functio

        Arguments: <numeric_value>,<numeric_value>
        """
        __slots__ = ()
        _cmd = "SPecial_functio"
        args = ["<numeric_value>,<numeric_value>"]

    SPecial_functio = SPecial_functio()  # type: ignore
    """
    SPecial_functio

    Arguments: <numeric_value>,<numeric_value>
    """

    class STATus(SCPINode, SCPISet):
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

            class DQUestionable(SCPINode):
                """
                STATus:DEVice:DQUestionable

                Arguments:
                """
                __slots__ = ()
                _cmd = "DQUestionable"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:DQUestionable:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:DEVice:DQUestionable:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:DEVice:DQUestionable:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:DEVice:DQUestionable:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:DQUestionable:EVENt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EVENt"
                    args = []  # type: List[str]

                EVENt = EVENt()  # type: ignore
                """
                STATus:DEVice:DQUestionable:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:DQUestionable:NTRansition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = []  # type: List[str]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:DEVice:DQUestionable:NTRansition

                Arguments:
                """

                class PTRansition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:DQUestionable:PTRansition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = []  # type: List[str]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:DEVice:DQUestionable:PTRansition

                Arguments:
                """

            DQUestionable = DQUestionable()  # type: ignore
            """
            STATus:DEVice:DQUestionable

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

            class NTRansition(SCPINode, SCPIQuery):
                """
                STATus:DEVice:NTRansition

                Arguments:
                """
                __slots__ = ()
                _cmd = "NTRansition"
                args = []  # type: List[str]

            NTRansition = NTRansition()  # type: ignore
            """
            STATus:DEVice:NTRansition

            Arguments:
            """

            class PTRansition(SCPINode, SCPIQuery):
                """
                STATus:DEVice:PTRansition

                Arguments:
                """
                __slots__ = ()
                _cmd = "PTRansition"
                args = []  # type: List[str]

            PTRansition = PTRansition()  # type: ignore
            """
            STATus:DEVice:PTRansition

            Arguments:
            """

            class SINTegrity(SCPINode):
                """
                STATus:DEVice:SINTegrity

                Arguments:
                """
                __slots__ = ()
                _cmd = "SINTegrity"
                args = []  # type: List[str]

                class AMPLitude(SCPINode):
                    """
                    STATus:DEVice:SINTegrity:AMPLitude

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "AMPLitude"
                    args = []  # type: List[str]

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:AMPLitude:CONDition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "CONDition"
                        args = []  # type: List[str]

                    CONDition = CONDition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:AMPLitude:CONDition

                    Arguments:
                    """

                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        STATus:DEVice:SINTegrity:AMPLitude:ENABle

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "ENABle"
                        args = ["1"]

                    ENABle = ENABle()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:AMPLitude:ENABle

                    Arguments: 1
                    """

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:AMPLitude:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:AMPLitude:EVENt

                    Arguments:
                    """

                    class NTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:AMPLitude:NTRansition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "NTRansition"
                        args = []  # type: List[str]

                    NTRansition = NTRansition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:AMPLitude:NTRansition

                    Arguments:
                    """

                    class PTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:AMPLitude:PTRansition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "PTRansition"
                        args = []  # type: List[str]

                    PTRansition = PTRansition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:AMPLitude:PTRansition

                    Arguments:
                    """

                AMPLitude = AMPLitude()  # type: ignore
                """
                STATus:DEVice:SINTegrity:AMPLitude

                Arguments:
                """

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:SINTegrity:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:DEVice:SINTegrity:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:DEVice:SINTegrity:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:DEVice:SINTegrity:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:SINTegrity:EVENt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EVENt"
                    args = []  # type: List[str]

                EVENt = EVENt()  # type: ignore
                """
                STATus:DEVice:SINTegrity:EVENt

                Arguments:
                """

                class FREQuency(SCPINode):
                    """
                    STATus:DEVice:SINTegrity:FREQuency

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "FREQuency"
                    args = []  # type: List[str]

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:FREQuency:CONDition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "CONDition"
                        args = []  # type: List[str]

                    CONDition = CONDition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:FREQuency:CONDition

                    Arguments:
                    """

                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        STATus:DEVice:SINTegrity:FREQuency:ENABle

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "ENABle"
                        args = ["1"]

                    ENABle = ENABle()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:FREQuency:ENABle

                    Arguments: 1
                    """

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:FREQuency:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:FREQuency:EVENt

                    Arguments:
                    """

                    class NTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:FREQuency:NTRansition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "NTRansition"
                        args = []  # type: List[str]

                    NTRansition = NTRansition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:FREQuency:NTRansition

                    Arguments:
                    """

                    class PTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:FREQuency:PTRansition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "PTRansition"
                        args = []  # type: List[str]

                    PTRansition = PTRansition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:FREQuency:PTRansition

                    Arguments:
                    """

                FREQuency = FREQuency()  # type: ignore
                """
                STATus:DEVice:SINTegrity:FREQuency

                Arguments:
                """

                class HARDware(SCPINode):
                    """
                    STATus:DEVice:SINTegrity:HARDware

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "HARDware"
                    args = []  # type: List[str]

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:HARDware:CONDition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "CONDition"
                        args = []  # type: List[str]

                    CONDition = CONDition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:HARDware:CONDition

                    Arguments:
                    """

                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        STATus:DEVice:SINTegrity:HARDware:ENABle

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "ENABle"
                        args = ["1"]

                    ENABle = ENABle()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:HARDware:ENABle

                    Arguments: 1
                    """

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:HARDware:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:HARDware:EVENt

                    Arguments:
                    """

                    class NTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:HARDware:NTRansition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "NTRansition"
                        args = []  # type: List[str]

                    NTRansition = NTRansition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:HARDware:NTRansition

                    Arguments:
                    """

                    class PTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:HARDware:PTRansition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "PTRansition"
                        args = []  # type: List[str]

                    PTRansition = PTRansition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:HARDware:PTRansition

                    Arguments:
                    """

                HARDware = HARDware()  # type: ignore
                """
                STATus:DEVice:SINTegrity:HARDware

                Arguments:
                """

                class MODulation(SCPINode):
                    """
                    STATus:DEVice:SINTegrity:MODulation

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "MODulation"
                    args = []  # type: List[str]

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:MODulation:CONDition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "CONDition"
                        args = []  # type: List[str]

                    CONDition = CONDition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:MODulation:CONDition

                    Arguments:
                    """

                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        STATus:DEVice:SINTegrity:MODulation:ENABle

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "ENABle"
                        args = ["1"]

                    ENABle = ENABle()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:MODulation:ENABle

                    Arguments: 1
                    """

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:MODulation:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:MODulation:EVENt

                    Arguments:
                    """

                    class NTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:MODulation:NTRansition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "NTRansition"
                        args = []  # type: List[str]

                    NTRansition = NTRansition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:MODulation:NTRansition

                    Arguments:
                    """

                    class PTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:MODulation:PTRansition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "PTRansition"
                        args = []  # type: List[str]

                    PTRansition = PTRansition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:MODulation:PTRansition

                    Arguments:
                    """

                MODulation = MODulation()  # type: ignore
                """
                STATus:DEVice:SINTegrity:MODulation

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:SINTegrity:NTRansition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = []  # type: List[str]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:DEVice:SINTegrity:NTRansition

                Arguments:
                """

                class PTRansition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:SINTegrity:PTRansition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = []  # type: List[str]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:DEVice:SINTegrity:PTRansition

                Arguments:
                """

                class REFerence(SCPINode):
                    """
                    STATus:DEVice:SINTegrity:REFerence

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "REFerence"
                    args = []  # type: List[str]

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:REFerence:CONDition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "CONDition"
                        args = []  # type: List[str]

                    CONDition = CONDition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:REFerence:CONDition

                    Arguments:
                    """

                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        STATus:DEVice:SINTegrity:REFerence:ENABle

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "ENABle"
                        args = ["1"]

                    ENABle = ENABle()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:REFerence:ENABle

                    Arguments: 1
                    """

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:REFerence:EVENt

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "EVENt"
                        args = []  # type: List[str]

                    EVENt = EVENt()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:REFerence:EVENt

                    Arguments:
                    """

                    class NTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:REFerence:NTRansition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "NTRansition"
                        args = []  # type: List[str]

                    NTRansition = NTRansition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:REFerence:NTRansition

                    Arguments:
                    """

                    class PTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:REFerence:PTRansition

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "PTRansition"
                        args = []  # type: List[str]

                    PTRansition = PTRansition()  # type: ignore
                    """
                    STATus:DEVice:SINTegrity:REFerence:PTRansition

                    Arguments:
                    """

                REFerence = REFerence()  # type: ignore
                """
                STATus:DEVice:SINTegrity:REFerence

                Arguments:
                """

            SINTegrity = SINTegrity()  # type: ignore
            """
            STATus:DEVice:SINTegrity

            Arguments:
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

            class BASeband(SCPINode):
                """
                STATus:OPERation:BASeband

                Arguments:
                """
                __slots__ = ()
                _cmd = "BASeband"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BASeband:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:OPERation:BASeband:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BASeband:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:OPERation:BASeband:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:BASeband:EVENt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EVENt"
                    args = []  # type: List[str]

                EVENt = EVENt()  # type: ignore
                """
                STATus:OPERation:BASeband:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BASeband:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:OPERation:BASeband:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BASeband:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:OPERation:BASeband:PTRansition

                Arguments: 1
                """

            BASeband = BASeband()  # type: ignore
            """
            STATus:OPERation:BASeband

            Arguments:
            """

            class BIT(SCPINodeN):
                """
                STATus:OPERation:BIT

                Arguments:
                """
                __slots__ = ()
                _cmd = "BIT"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:BIT:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:OPERation:BIT:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BIT:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:OPERation:BIT:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:BIT:EVENt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EVENt"
                    args = []  # type: List[str]

                EVENt = EVENt()  # type: ignore
                """
                STATus:OPERation:BIT:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIBool):
                    """
                    STATus:OPERation:BIT:NTRansition

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1", "ON", "OFF"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:OPERation:BIT:NTRansition

                Arguments: 1, ON, OFF
                """

                class PTRansition(SCPINode, SCPIBool):
                    """
                    STATus:OPERation:BIT:PTRansition

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1", "ON", "OFF"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:OPERation:BIT:PTRansition

                Arguments: 1, ON, OFF
                """

            BIT = BIT()  # type: ignore
            """
            STATus:OPERation:BIT

            Arguments:
            """

            class CONDition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:OPERation:CONDition
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/eb9e616c44d34723.htm#ID_4d81c86771e8195f0a00206a0077942b-79a3ea6771e8195f0a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "CONDition"
                args = ["1"]

            CONDition = CONDition()  # type: ignore
            """
            `STATus:OPERation:CONDition
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/eb9e616c44d34723.htm#ID_4d81c86771e8195f0a00206a0077942b-79a3ea6771e8195f0a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:OPERation:ENABle
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/98bc7031b17e43d1.htm#ID_8a49b59171e820350a00206a00df2aff-e8cb628971e820350a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()  # type: ignore
            """
            `STATus:OPERation:ENABle
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/98bc7031b17e43d1.htm#ID_8a49b59171e820350a00206a00df2aff-e8cb628971e820350a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class EVENt(SCPINode, SCPIQuery):
                """
                `STATus:OPERation:EVENt
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/6adf4ecb81884cba.htm#ID_4526902e71e80ba30a00206a0056f13c-3203e98571e80bb30a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "EVENt"
                args = []  # type: List[str]

            EVENt = EVENt()  # type: ignore
            """
            `STATus:OPERation:EVENt
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/6adf4ecb81884cba.htm#ID_4526902e71e80ba30a00206a0056f13c-3203e98571e80bb30a00206a012bc823-en-US>`_

            Arguments:
            """

            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:OPERation:NTRansition
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7972c214b7914431.htm#ID_c40b400271e8268e0a00206a01d0b5f6-bab207fb71e8268e0a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()  # type: ignore
            """
            `STATus:OPERation:NTRansition
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7972c214b7914431.htm#ID_c40b400271e8268e0a00206a01d0b5f6-bab207fb71e8268e0a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class NTRanstition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:NTRanstition

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "NTRanstition"
                args = ["1"]

            NTRanstition = NTRanstition()  # type: ignore
            """
            STATus:OPERation:NTRanstition

            Arguments: 1
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:OPERation:PTRansition
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/19ddd521fccc4c10.htm#ID_7baf119671e812690a00206a0185198a-e4673fbb71e812690a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()  # type: ignore
            """
            `STATus:OPERation:PTRansition
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/19ddd521fccc4c10.htm#ID_7baf119671e812690a00206a0185198a-e4673fbb71e812690a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class PTRanstition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:PTRanstition

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PTRanstition"
                args = ["1"]

            PTRanstition = PTRanstition()  # type: ignore
            """
            STATus:OPERation:PTRanstition

            Arguments: 1
            """

        OPERation = OPERation()  # type: ignore
        """
        STATus:OPERation

        Arguments:
        """

        class PRESet(SCPINode, SCPISet):
            """
            `STATus:PRESet
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/790fdbfc3c41487f.htm#ID_e484e63b71e7fde70a00206a00a80b3f-98d3fe7771e7fde70a00206a012bc823-en-US>`_

            Arguments:
            """
            __slots__ = ()
            _cmd = "PRESet"
            args = []  # type: List[str]

        PRESet = PRESet()  # type: ignore
        """
        `STATus:PRESet
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/790fdbfc3c41487f.htm#ID_e484e63b71e7fde70a00206a00a80b3f-98d3fe7771e7fde70a00206a012bc823-en-US>`_

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

            class BERT(SCPINode):
                """
                STATus:QUEStionable:BERT

                Arguments:
                """
                __slots__ = ()
                _cmd = "BERT"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:BERT:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:QUEStionable:BERT:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:BERT:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:QUEStionable:BERT:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:BERT:EVENt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EVENt"
                    args = []  # type: List[str]

                EVENt = EVENt()  # type: ignore
                """
                STATus:QUEStionable:BERT:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:BERT:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:QUEStionable:BERT:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:BERT:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:QUEStionable:BERT:PTRansition

                Arguments: 1
                """

            BERT = BERT()  # type: ignore
            """
            STATus:QUEStionable:BERT

            Arguments:
            """

            class BIT(SCPINodeN):
                """
                STATus:QUEStionable:BIT

                Arguments:
                """
                __slots__ = ()
                _cmd = "BIT"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:BIT:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:QUEStionable:BIT:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIBool):
                    """
                    STATus:QUEStionable:BIT:ENABle

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1", "ON", "OFF"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:QUEStionable:BIT:ENABle

                Arguments: 1, ON, OFF
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:BIT:EVENt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EVENt"
                    args = []  # type: List[str]

                EVENt = EVENt()  # type: ignore
                """
                STATus:QUEStionable:BIT:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIBool):
                    """
                    STATus:QUEStionable:BIT:NTRansition

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1", "ON", "OFF"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:QUEStionable:BIT:NTRansition

                Arguments: 1, ON, OFF
                """

                class PTRansition(SCPINode, SCPIBool):
                    """
                    STATus:QUEStionable:BIT:PTRansition

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1", "ON", "OFF"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:QUEStionable:BIT:PTRansition

                Arguments: 1, ON, OFF
                """

            BIT = BIT()  # type: ignore
            """
            STATus:QUEStionable:BIT

            Arguments:
            """

            class CALibration(SCPINode):
                """
                STATus:QUEStionable:CALibration

                Arguments:
                """
                __slots__ = ()
                _cmd = "CALibration"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery, SCPISet):
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

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:CALibration:EVENt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EVENt"
                    args = []  # type: List[str]

                EVENt = EVENt()  # type: ignore
                """
                STATus:QUEStionable:CALibration:EVENt

                Arguments:
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

            CALibration = CALibration()  # type: ignore
            """
            STATus:QUEStionable:CALibration

            Arguments:
            """

            class CONDition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:CONDition
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f08a3423b9ea496f.htm#ID_e3fc15a371e842430a00206a009728a6-98e12c6f71e842430a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "CONDition"
                args = ["1"]

            CONDition = CONDition()  # type: ignore
            """
            `STATus:QUEStionable:CONDition
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f08a3423b9ea496f.htm#ID_e3fc15a371e842430a00206a009728a6-98e12c6f71e842430a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:ENABle
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/08e648cd32434240.htm#ID_d432e5c771e849670a00206a00cb59b5-0bf1cb4571e849670a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()  # type: ignore
            """
            `STATus:QUEStionable:ENABle
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/08e648cd32434240.htm#ID_d432e5c771e849670a00206a00cb59b5-0bf1cb4571e849670a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class EVENt(SCPINode, SCPIQuery):
                """
                `STATus:QUEStionable:EVENt
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/baaaa61d6eeb4c8f.htm#ID_8f72e6de71e834880a00206a01c75738-c55f605671e834880a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "EVENt"
                args = []  # type: List[str]

            EVENt = EVENt()  # type: ignore
            """
            `STATus:QUEStionable:EVENt
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/baaaa61d6eeb4c8f.htm#ID_8f72e6de71e834880a00206a01c75738-c55f605671e834880a00206a012bc823-en-US>`_

            Arguments:
            """

            class FREQuency(SCPINode):
                """
                STATus:QUEStionable:FREQuency

                Arguments:
                """
                __slots__ = ()
                _cmd = "FREQuency"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:FREQuency:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:QUEStionable:FREQuency:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:FREQuency:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:QUEStionable:FREQuency:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:FREQuency:EVENt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EVENt"
                    args = []  # type: List[str]

                EVENt = EVENt()  # type: ignore
                """
                STATus:QUEStionable:FREQuency:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:FREQuency:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:QUEStionable:FREQuency:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:FREQuency:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:QUEStionable:FREQuency:PTRansition

                Arguments: 1
                """

            FREQuency = FREQuency()  # type: ignore
            """
            STATus:QUEStionable:FREQuency

            Arguments:
            """

            class MODulation(SCPINode):
                """
                STATus:QUEStionable:MODulation

                Arguments:
                """
                __slots__ = ()
                _cmd = "MODulation"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:MODulation:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:QUEStionable:MODulation:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:MODulation:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:QUEStionable:MODulation:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:MODulation:EVENt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EVENt"
                    args = []  # type: List[str]

                EVENt = EVENt()  # type: ignore
                """
                STATus:QUEStionable:MODulation:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:MODulation:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:QUEStionable:MODulation:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:MODulation:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:QUEStionable:MODulation:PTRansition

                Arguments: 1
                """

            MODulation = MODulation()  # type: ignore
            """
            STATus:QUEStionable:MODulation

            Arguments:
            """

            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:NTRansition
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/792d9ce3f9bf4fdd.htm#ID_3172142271e8509b0a00206a01b3f2a1-b4d8282f71e8509b0a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()  # type: ignore
            """
            `STATus:QUEStionable:NTRansition
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/792d9ce3f9bf4fdd.htm#ID_3172142271e8509b0a00206a01b3f2a1-b4d8282f71e8509b0a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class NTRanstition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:NTRanstition

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "NTRanstition"
                args = ["1"]

            NTRanstition = NTRanstition()  # type: ignore
            """
            STATus:QUEStionable:NTRanstition

            Arguments: 1
            """

            class PAGing(SCPINode):
                """
                STATus:QUEStionable:PAGing

                Arguments:
                """
                __slots__ = ()
                _cmd = "PAGing"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:PAGing:CONDition

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "CONDition"
                    args = []  # type: List[str]

                CONDition = CONDition()  # type: ignore
                """
                STATus:QUEStionable:PAGing:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:PAGing:ENABle

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()  # type: ignore
                """
                STATus:QUEStionable:PAGing:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:PAGing:EVENt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EVENt"
                    args = []  # type: List[str]

                EVENt = EVENt()  # type: ignore
                """
                STATus:QUEStionable:PAGing:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:PAGing:NTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()  # type: ignore
                """
                STATus:QUEStionable:PAGing:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:PAGing:PTRansition

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()  # type: ignore
                """
                STATus:QUEStionable:PAGing:PTRansition

                Arguments: 1
                """

            PAGing = PAGing()  # type: ignore
            """
            STATus:QUEStionable:PAGing

            Arguments:
            """

            class POWer(SCPINode):
                """
                STATus:QUEStionable:POWer

                Arguments:
                """
                __slots__ = ()
                _cmd = "POWer"
                args = []  # type: List[str]

                class CONDition(SCPINode, SCPIQuery, SCPISet):
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

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:POWer:EVENt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "EVENt"
                    args = []  # type: List[str]

                EVENt = EVENt()  # type: ignore
                """
                STATus:QUEStionable:POWer:EVENt

                Arguments:
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

            POWer = POWer()  # type: ignore
            """
            STATus:QUEStionable:POWer

            Arguments:
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:PTRansition
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/13c14e2f83164444.htm#ID_4ed8eafd71e83b5e0a00206a01c2fbb1-c632286d71e83b5e0a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()  # type: ignore
            """
            `STATus:QUEStionable:PTRansition
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/13c14e2f83164444.htm#ID_4ed8eafd71e83b5e0a00206a01c2fbb1-c632286d71e83b5e0a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class PTRanstition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:PTRanstition

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PTRanstition"
                args = ["1"]

            PTRanstition = PTRanstition()  # type: ignore
            """
            STATus:QUEStionable:PTRanstition

            Arguments: 1
            """

        QUEStionable = QUEStionable()  # type: ignore
        """
        STATus:QUEStionable

        Arguments:
        """

    STATus = STATus()  # type: ignore
    """
    STATus

    Arguments:
    """

    class STore(SCPINode, SCPISet):
        """
        STore

        Arguments: 1
        """
        __slots__ = ()
        _cmd = "STore"
        args = ["1"]

        class Fast(SCPINode, SCPISet):
            """
            STore:Fast

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "Fast"
            args = ["1"]

        Fast = Fast()  # type: ignore
        """
        STore:Fast

        Arguments: 1
        """

    STore = STore()  # type: ignore
    """
    STore

    Arguments: 1
    """

    class SWEep(SCPINode, SCPIQuery):
        """
        SWEep

        Arguments:
        """
        __slots__ = ()
        _cmd = "SWEep"
        args = []  # type: List[str]

        class CFRQ(SCPINode):
            """
            SWEep:CFRQ

            Arguments:
            """
            __slots__ = ()
            _cmd = "CFRQ"
            args = []  # type: List[str]

            class LOGinc(SCPINode, SCPISet):
                """
                SWEep:CFRQ:LOGinc

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "LOGinc"
                args = ["1"]

            LOGinc = LOGinc()  # type: ignore
            """
            SWEep:CFRQ:LOGinc

            Arguments: 1
            """

            class MKRNum(SCPINode, SCPISet):
                """
                SWEep:CFRQ:MKRNum

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "MKRNum"
                args = ["1"]

            MKRNum = MKRNum()  # type: ignore
            """
            SWEep:CFRQ:MKRNum

            Arguments: 1
            """

            class MKRoff(SCPINode, SCPISet):
                """
                SWEep:CFRQ:MKRoff

                Arguments:
                """
                __slots__ = ()
                _cmd = "MKRoff"
                args = []  # type: List[str]

            MKRoff = MKRoff()  # type: ignore
            """
            SWEep:CFRQ:MKRoff

            Arguments:
            """

            class MKRon(SCPINode, SCPISet):
                """
                SWEep:CFRQ:MKRon

                Arguments:
                """
                __slots__ = ()
                _cmd = "MKRon"
                args = []  # type: List[str]

            MKRon = MKRon()  # type: ignore
            """
            SWEep:CFRQ:MKRon

            Arguments:
            """

            class STARt(SCPINode, SCPISet):
                """
                SWEep:CFRQ:STARt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()  # type: ignore
            """
            SWEep:CFRQ:STARt

            Arguments: 1
            """

            class VALue(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:CFRQ:VALue

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()  # type: ignore
            """
            SWEep:CFRQ:VALue

            Arguments: 1
            """

        CFRQ = CFRQ()  # type: ignore
        """
        SWEep:CFRQ

        Arguments:
        """

        class FREQuency(SCPINode, SCPISet):
            """
            SWEep:FREQuency

            Arguments:
            """
            __slots__ = ()
            _cmd = "FREQuency"
            args = []  # type: List[str]

            class GENeration(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:FREQuency:GENeration

                Arguments: ANALog, STEPped
                """
                __slots__ = ()
                _cmd = "GENeration"
                args = ["ANALog", "STEPped"]

            GENeration = GENeration()  # type: ignore
            """
            SWEep:FREQuency:GENeration

            Arguments: ANALog, STEPped
            """

            class SPACing(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:FREQuency:SPACing

                Arguments: LINear, LOGarithmic
                """
                __slots__ = ()
                _cmd = "SPACing"
                args = ["LINear", "LOGarithmic"]

            SPACing = SPACing()  # type: ignore
            """
            SWEep:FREQuency:SPACing

            Arguments: LINear, LOGarithmic
            """

            class TIME(SCPINode):
                """
                SWEep:FREQuency:TIME

                Arguments:
                """
                __slots__ = ()
                _cmd = "TIME"
                args = []  # type: List[str]

                class STEP(SCPINode):
                    """
                    SWEep:FREQuency:TIME:STEP

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STEP"
                    args = []  # type: List[str]

                    class INCRement(SCPINode, SCPIQuery):
                        """
                        SWEep:FREQuency:TIME:STEP:INCRement

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()  # type: ignore
                    """
                    SWEep:FREQuency:TIME:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()  # type: ignore
                """
                SWEep:FREQuency:TIME:STEP

                Arguments:
                """

            TIME = TIME()  # type: ignore
            """
            SWEep:FREQuency:TIME

            Arguments:
            """

        FREQuency = FREQuency()  # type: ignore
        """
        SWEep:FREQuency

        Arguments:
        """

        class INTF(SCPINode):
            """
            SWEep:INTF

            Arguments:
            """
            __slots__ = ()
            _cmd = "INTF"
            args = []  # type: List[str]

            class MKRNum(SCPINode, SCPISet):
                """
                SWEep:INTF:MKRNum

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "MKRNum"
                args = ["1"]

            MKRNum = MKRNum()  # type: ignore
            """
            SWEep:INTF:MKRNum

            Arguments: 1
            """

            class MKRoff(SCPINode, SCPISet):
                """
                SWEep:INTF:MKRoff

                Arguments:
                """
                __slots__ = ()
                _cmd = "MKRoff"
                args = []  # type: List[str]

            MKRoff = MKRoff()  # type: ignore
            """
            SWEep:INTF:MKRoff

            Arguments:
            """

            class MKRon(SCPINode, SCPISet):
                """
                SWEep:INTF:MKRon

                Arguments:
                """
                __slots__ = ()
                _cmd = "MKRon"
                args = []  # type: List[str]

            MKRon = MKRon()  # type: ignore
            """
            SWEep:INTF:MKRon

            Arguments:
            """

            class STARt(SCPINode, SCPISet):
                """
                SWEep:INTF:STARt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()  # type: ignore
            """
            SWEep:INTF:STARt

            Arguments: 1
            """

            class VALue(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:INTF:VALue

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()  # type: ignore
            """
            SWEep:INTF:VALue

            Arguments: 1
            """

        INTF = INTF()  # type: ignore
        """
        SWEep:INTF

        Arguments:
        """

        class LFGF(SCPINode):
            """
            SWEep:LFGF

            Arguments:
            """
            __slots__ = ()
            _cmd = "LFGF"
            args = []  # type: List[str]

            class MKRNum(SCPINode, SCPISet):
                """
                SWEep:LFGF:MKRNum

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "MKRNum"
                args = ["1"]

            MKRNum = MKRNum()  # type: ignore
            """
            SWEep:LFGF:MKRNum

            Arguments: 1
            """

            class MKRoff(SCPINode, SCPISet):
                """
                SWEep:LFGF:MKRoff

                Arguments:
                """
                __slots__ = ()
                _cmd = "MKRoff"
                args = []  # type: List[str]

            MKRoff = MKRoff()  # type: ignore
            """
            SWEep:LFGF:MKRoff

            Arguments:
            """

            class MKRon(SCPINode, SCPISet):
                """
                SWEep:LFGF:MKRon

                Arguments:
                """
                __slots__ = ()
                _cmd = "MKRon"
                args = []  # type: List[str]

            MKRon = MKRon()  # type: ignore
            """
            SWEep:LFGF:MKRon

            Arguments:
            """

            class STARt(SCPINode, SCPISet):
                """
                SWEep:LFGF:STARt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()  # type: ignore
            """
            SWEep:LFGF:STARt

            Arguments: 1
            """

            class VALue(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:LFGF:VALue

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()  # type: ignore
            """
            SWEep:LFGF:VALue

            Arguments: 1
            """

        LFGF = LFGF()  # type: ignore
        """
        SWEep:LFGF

        Arguments:
        """

        class LFGL(SCPINode):
            """
            SWEep:LFGL

            Arguments:
            """
            __slots__ = ()
            _cmd = "LFGL"
            args = []  # type: List[str]

            class MKRNum(SCPINode, SCPISet):
                """
                SWEep:LFGL:MKRNum

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "MKRNum"
                args = ["1"]

            MKRNum = MKRNum()  # type: ignore
            """
            SWEep:LFGL:MKRNum

            Arguments: 1
            """

            class MKRoff(SCPINode, SCPISet):
                """
                SWEep:LFGL:MKRoff

                Arguments:
                """
                __slots__ = ()
                _cmd = "MKRoff"
                args = []  # type: List[str]

            MKRoff = MKRoff()  # type: ignore
            """
            SWEep:LFGL:MKRoff

            Arguments:
            """

            class MKRon(SCPINode, SCPISet):
                """
                SWEep:LFGL:MKRon

                Arguments:
                """
                __slots__ = ()
                _cmd = "MKRon"
                args = []  # type: List[str]

            MKRon = MKRon()  # type: ignore
            """
            SWEep:LFGL:MKRon

            Arguments:
            """

            class STARt(SCPINode, SCPISet):
                """
                SWEep:LFGL:STARt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()  # type: ignore
            """
            SWEep:LFGL:STARt

            Arguments: 1
            """

            class VALue(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:LFGL:VALue

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()  # type: ignore
            """
            SWEep:LFGL:VALue

            Arguments: 1
            """

        LFGL = LFGL()  # type: ignore
        """
        SWEep:LFGL

        Arguments:
        """

        class MKRoff(SCPINode, SCPISet):
            """
            SWEep:MKRoff

            Arguments:
            """
            __slots__ = ()
            _cmd = "MKRoff"
            args = []  # type: List[str]

        MKRoff = MKRoff()  # type: ignore
        """
        SWEep:MKRoff

        Arguments:
        """

        class MKRon(SCPINode, SCPISet):
            """
            SWEep:MKRon

            Arguments:
            """
            __slots__ = ()
            _cmd = "MKRon"
            args = []  # type: List[str]

        MKRon = MKRon()  # type: ignore
        """
        SWEep:MKRon

        Arguments:
        """

        class RESet(SCPINode, SCPISet):
            """
            SWEep:RESet

            Arguments:
            """
            __slots__ = ()
            _cmd = "RESet"
            args = []  # type: List[str]

        RESet = RESet()  # type: ignore
        """
        SWEep:RESet

        Arguments:
        """

        class RFLV(SCPINode):
            """
            SWEep:RFLV

            Arguments:
            """
            __slots__ = ()
            _cmd = "RFLV"
            args = []  # type: List[str]

            class MKRNum(SCPINode, SCPISet):
                """
                SWEep:RFLV:MKRNum

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "MKRNum"
                args = ["1"]

            MKRNum = MKRNum()  # type: ignore
            """
            SWEep:RFLV:MKRNum

            Arguments: 1
            """

            class MKRoff(SCPINode, SCPISet):
                """
                SWEep:RFLV:MKRoff

                Arguments:
                """
                __slots__ = ()
                _cmd = "MKRoff"
                args = []  # type: List[str]

            MKRoff = MKRoff()  # type: ignore
            """
            SWEep:RFLV:MKRoff

            Arguments:
            """

            class MKRon(SCPINode, SCPISet):
                """
                SWEep:RFLV:MKRon

                Arguments:
                """
                __slots__ = ()
                _cmd = "MKRon"
                args = []  # type: List[str]

            MKRon = MKRon()  # type: ignore
            """
            SWEep:RFLV:MKRon

            Arguments:
            """

            class STARt(SCPINode, SCPISet):
                """
                SWEep:RFLV:STARt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()  # type: ignore
            """
            SWEep:RFLV:STARt

            Arguments: 1
            """

            class VALue(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:RFLV:VALue

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()  # type: ignore
            """
            SWEep:RFLV:VALue

            Arguments: 1
            """

        RFLV = RFLV()  # type: ignore
        """
        SWEep:RFLV

        Arguments:
        """

    SWEep = SWEep()  # type: ignore
    """
    SWEep

    Arguments:
    """

    class SYSTem(SCPINode, SCPISet):
        """
        SYSTem

        Arguments:
        """
        __slots__ = ()
        _cmd = "SYSTem"
        args = []  # type: List[str]

        class ALTernate(SCPINode):
            """
            SYSTem:ALTernate

            Arguments:
            """
            __slots__ = ()
            _cmd = "ALTernate"
            args = []  # type: List[str]

            class STATe(SCPINode, SCPIBool):
                """
                SYSTem:ALTernate:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SYSTem:ALTernate:STATe

            Arguments: 1, ON, OFF
            """

        ALTernate = ALTernate()  # type: ignore
        """
        SYSTem:ALTernate

        Arguments:
        """

        class BEEPer(SCPINode):
            """
            SYSTem:BEEPer

            Arguments:
            """
            __slots__ = ()
            _cmd = "BEEPer"
            args = []  # type: List[str]

            class STATe(SCPINode, SCPIBool):
                """
                SYSTem:BEEPer:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SYSTem:BEEPer:STATe

            Arguments: 1, ON, OFF
            """

        BEEPer = BEEPer()  # type: ignore
        """
        SYSTem:BEEPer

        Arguments:
        """

        class CAPability(SCPINode, SCPIQuery):
            """
            SYSTem:CAPability

            Arguments:
            """
            __slots__ = ()
            _cmd = "CAPability"
            args = []  # type: List[str]

        CAPability = CAPability()  # type: ignore
        """
        SYSTem:CAPability

        Arguments:
        """

        class COMMunicate(SCPINode, SCPISet):
            """
            SYSTem:COMMunicate

            Arguments:
            """
            __slots__ = ()
            _cmd = "COMMunicate"
            args = []  # type: List[str]

            class GPIB(SCPINode):
                """
                SYSTem:COMMunicate:GPIB

                Arguments:
                """
                __slots__ = ()
                _cmd = "GPIB"
                args = []  # type: List[str]

                class ADDRess(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:GPIB:ADDRess

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ADDRess"
                    args = ["1"]

                ADDRess = ADDRess()  # type: ignore
                """
                SYSTem:COMMunicate:GPIB:ADDRess

                Arguments: 1
                """

                class SELF(SCPINode):
                    """
                    SYSTem:COMMunicate:GPIB:SELF

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "SELF"
                    args = []  # type: List[str]

                    class ADDRess(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:GPIB:SELF:ADDRess
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2c2c393234144769.htm#ID_048f099271caf99b0a00206a00d986d1-b9d7e0eb71caf99b0a00206a012bc823-en-US>`_

                        Arguments: 1
                        """
                        __slots__ = ()
                        _cmd = "ADDRess"
                        args = ["1"]

                    ADDRess = ADDRess()  # type: ignore
                    """
                    `SYSTem:COMMunicate:GPIB:SELF:ADDRess
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2c2c393234144769.htm#ID_048f099271caf99b0a00206a00d986d1-b9d7e0eb71caf99b0a00206a012bc823-en-US>`_

                    Arguments: 1
                    """

                SELF = SELF()  # type: ignore
                """
                SYSTem:COMMunicate:GPIB:SELF

                Arguments:
                """

            GPIB = GPIB()  # type: ignore
            """
            SYSTem:COMMunicate:GPIB

            Arguments:
            """

            class GTLocal(SCPINode, SCPISet):
                """
                SYSTem:COMMunicate:GTLocal

                Arguments:
                """
                __slots__ = ()
                _cmd = "GTLocal"
                args = []  # type: List[str]

            GTLocal = GTLocal()  # type: ignore
            """
            SYSTem:COMMunicate:GTLocal

            Arguments:
            """

            class LAN(SCPINode):
                """
                SYSTem:COMMunicate:LAN

                Arguments:
                """
                __slots__ = ()
                _cmd = "LAN"
                args = []  # type: List[str]

                class CONFig(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:CONFig

                    Arguments: AIP, AUTO, DHCP, MANual
                    """
                    __slots__ = ()
                    _cmd = "CONFig"
                    args = ["AIP", "AUTO", "DHCP", "MANual"]

                CONFig = CONFig()  # type: ignore
                """
                SYSTem:COMMunicate:LAN:CONFig

                Arguments: AIP, AUTO, DHCP, MANual
                """

                class DEFaults(SCPINode, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:DEFaults

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "DEFaults"
                    args = []  # type: List[str]

                DEFaults = DEFaults()  # type: ignore
                """
                SYSTem:COMMunicate:LAN:DEFaults

                Arguments:
                """

                class DOMain(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:DOMain

                    Arguments: 'string'
                    """
                    __slots__ = ()
                    _cmd = "DOMain"
                    args = ["'string'"]

                DOMain = DOMain()  # type: ignore
                """
                SYSTem:COMMunicate:LAN:DOMain

                Arguments: 'string'
                """

                class GATeway(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:GATeway

                    Arguments: 'string'
                    """
                    __slots__ = ()
                    _cmd = "GATeway"
                    args = ["'string'"]

                GATeway = GATeway()  # type: ignore
                """
                SYSTem:COMMunicate:LAN:GATeway

                Arguments: 'string'
                """

                class HOSTname(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:HOSTname

                    Arguments: 'string'
                    """
                    __slots__ = ()
                    _cmd = "HOSTname"
                    args = ["'string'"]

                HOSTname = HOSTname()  # type: ignore
                """
                SYSTem:COMMunicate:LAN:HOSTname

                Arguments: 'string'
                """

                class RESTart(SCPINode, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:RESTart

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "RESTart"
                    args = []  # type: List[str]

                RESTart = RESTart()  # type: ignore
                """
                SYSTem:COMMunicate:LAN:RESTart

                Arguments:
                """

                class SUBNet(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:SUBNet

                    Arguments: 'string'
                    """
                    __slots__ = ()
                    _cmd = "SUBNet"
                    args = ["'string'"]

                SUBNet = SUBNet()  # type: ignore
                """
                SYSTem:COMMunicate:LAN:SUBNet

                Arguments: 'string'
                """

            LAN = LAN()  # type: ignore
            """
            SYSTem:COMMunicate:LAN

            Arguments:
            """

            class PMETer(SCPINode, SCPISet):
                """
                SYSTem:COMMunicate:PMETer

                Arguments:
                """
                __slots__ = ()
                _cmd = "PMETer"
                args = []  # type: List[str]

                class ADDRess(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:PMETer:ADDRess

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ADDRess"
                    args = ["1"]

                ADDRess = ADDRess()  # type: ignore
                """
                SYSTem:COMMunicate:PMETer:ADDRess

                Arguments: 1
                """

                class CHANnel(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:PMETer:CHANnel

                    Arguments: A, B
                    """
                    __slots__ = ()
                    _cmd = "CHANnel"
                    args = ["A", "B"]

                CHANnel = CHANnel()  # type: ignore
                """
                SYSTem:COMMunicate:PMETer:CHANnel

                Arguments: A, B
                """

                class TIMeout(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:PMETer:TIMeout

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "TIMeout"
                    args = ["1"]

                TIMeout = TIMeout()  # type: ignore
                """
                SYSTem:COMMunicate:PMETer:TIMeout

                Arguments: 1
                """

            PMETer = PMETer()  # type: ignore
            """
            SYSTem:COMMunicate:PMETer

            Arguments:
            """

            class SERial(SCPINode, SCPISet):
                """
                SYSTem:COMMunicate:SERial

                Arguments:
                """
                __slots__ = ()
                _cmd = "SERial"
                args = []  # type: List[str]

                class PARity(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:COMMunicate:SERial:PARity
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/007a87c5bc084b7e.htm#ID_ed84c7fa71cc127d0a00206a0162bb19-92f11b0771cc127d0a00206a012bc823-en-US>`_

                    Arguments: EVEN, NONE, ODD, ONE, ZERO
                    """
                    __slots__ = ()
                    _cmd = "PARity"
                    args = ["EVEN", "NONE", "ODD", "ONE", "ZERO"]

                PARity = PARity()  # type: ignore
                """
                `SYSTem:COMMunicate:SERial:PARity
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/007a87c5bc084b7e.htm#ID_ed84c7fa71cc127d0a00206a0162bb19-92f11b0771cc127d0a00206a012bc823-en-US>`_

                Arguments: EVEN, NONE, ODD, ONE, ZERO
                """

                class RESet(SCPINode, SCPISet):
                    """
                    SYSTem:COMMunicate:SERial:RESet

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "RESet"
                    args = []  # type: List[str]

                RESet = RESet()  # type: ignore
                """
                SYSTem:COMMunicate:SERial:RESet

                Arguments:
                """

                class SBITs(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:COMMunicate:SERial:SBITs
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e6a3b756c8454b50.htm#ID_48a728cc71cc19b10a00206a014314e1-a83e843471cc19b10a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "SBITs"
                    args = ["1"]

                SBITs = SBITs()  # type: ignore
                """
                `SYSTem:COMMunicate:SERial:SBITs
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e6a3b756c8454b50.htm#ID_48a728cc71cc19b10a00206a014314e1-a83e843471cc19b10a00206a012bc823-en-US>`_

                Arguments: 1
                """

            SERial = SERial()  # type: ignore
            """
            SYSTem:COMMunicate:SERial

            Arguments:
            """

        COMMunicate = COMMunicate()  # type: ignore
        """
        SYSTem:COMMunicate

        Arguments:
        """

        class DATE(SCPINode):
            """
            `SYSTem:DATE
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/c85e1a39bfd346a5.htm#ID_4045f3d171cb96480a00206a0187c2e2-1c42171d71cb96480a00206a012bc823-en-US>`_

            Arguments:
            """
            __slots__ = ()
            _cmd = "DATE"
            args = []  # type: List[str]

            class LOCal(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:DATE:LOCal

                Arguments: <integer>,<integer>,<integer>
                """
                __slots__ = ()
                _cmd = "LOCal"
                args = ["<integer>,<integer>,<integer>"]

            LOCal = LOCal()  # type: ignore
            """
            SYSTem:DATE:LOCal

            Arguments: <integer>,<integer>,<integer>
            """

        DATE = DATE()  # type: ignore
        """
        `SYSTem:DATE
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/c85e1a39bfd346a5.htm#ID_4045f3d171cb96480a00206a0187c2e2-1c42171d71cb96480a00206a012bc823-en-US>`_

        Arguments:
        """

        class DFPRint(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:DFPRint

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "DFPRint"
            args = ["'string'"]

            class HISTory(SCPINode):
                """
                SYSTem:DFPRint:HISTory

                Arguments:
                """
                __slots__ = ()
                _cmd = "HISTory"
                args = []  # type: List[str]

                class COUNt(SCPINode, SCPIQuery):
                    """
                    SYSTem:DFPRint:HISTory:COUNt

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "COUNt"
                    args = []  # type: List[str]

                COUNt = COUNt()  # type: ignore
                """
                SYSTem:DFPRint:HISTory:COUNt

                Arguments:
                """

                class ENTRy(SCPINode, SCPIQuery):
                    """
                    SYSTem:DFPRint:HISTory:ENTRy

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ENTRy"
                    args = ["1"]

                ENTRy = ENTRy()  # type: ignore
                """
                SYSTem:DFPRint:HISTory:ENTRy

                Arguments: 1
                """

            HISTory = HISTory()  # type: ignore
            """
            SYSTem:DFPRint:HISTory

            Arguments:
            """

        DFPRint = DFPRint()  # type: ignore
        """
        SYSTem:DFPRint

        Arguments: 'string'
        """

        class DISPlay(SCPINode):
            """
            SYSTem:DISPlay

            Arguments:
            """
            __slots__ = ()
            _cmd = "DISPlay"
            args = []  # type: List[str]

            class UPDate(SCPINode, SCPIBool):
                """
                `SYSTem:DISPlay:UPDate
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f101e4cb6c3f422c.htm#ID_dc6f502b71cb0e3c0a00206a0114ff35-1059cab671cb0e3c0a00206a012bc823-en-US>`_

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "UPDate"
                args = ["1", "ON", "OFF"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SYSTem:DISPlay:UPDate:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SYSTem:DISPlay:UPDate:STATe

                Arguments: 1, ON, OFF
                """

            UPDate = UPDate()  # type: ignore
            """
            `SYSTem:DISPlay:UPDate
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f101e4cb6c3f422c.htm#ID_dc6f502b71cb0e3c0a00206a0114ff35-1059cab671cb0e3c0a00206a012bc823-en-US>`_

            Arguments: 1, ON, OFF
            """

        DISPlay = DISPlay()  # type: ignore
        """
        SYSTem:DISPlay

        Arguments:
        """

        class DUMP(SCPINode):
            """
            SYSTem:DUMP

            Arguments:
            """
            __slots__ = ()
            _cmd = "DUMP"
            args = []  # type: List[str]

            class ERRor(SCPINode, SCPIQuery):
                """
                SYSTem:DUMP:ERRor

                Arguments:
                """
                __slots__ = ()
                _cmd = "ERRor"
                args = []  # type: List[str]

            ERRor = ERRor()  # type: ignore
            """
            SYSTem:DUMP:ERRor

            Arguments:
            """

            class PRINter(SCPINode, SCPIQuery):
                """
                SYSTem:DUMP:PRINter

                Arguments:
                """
                __slots__ = ()
                _cmd = "PRINter"
                args = []  # type: List[str]

            PRINter = PRINter()  # type: ignore
            """
            SYSTem:DUMP:PRINter

            Arguments:
            """

        DUMP = DUMP()  # type: ignore
        """
        SYSTem:DUMP

        Arguments:
        """

        class ERRor(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:ERRor

            Arguments: NUMeric, STRing
            """
            __slots__ = ()
            _cmd = "ERRor"
            args = ["NUMeric", "STRing"]

            class COUNt(SCPINode, SCPIQuery):
                """
                `SYSTem:ERRor:COUNt
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/ba0d0e59bbb0493c.htm#ID_00c603b971d1daa50a00206a0178d1e6-77aa4c6371d1daa50a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "COUNt"
                args = []  # type: List[str]

            COUNt = COUNt()  # type: ignore
            """
            `SYSTem:ERRor:COUNt
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/ba0d0e59bbb0493c.htm#ID_00c603b971d1daa50a00206a0178d1e6-77aa4c6371d1daa50a00206a012bc823-en-US>`_

            Arguments:
            """

            class SCPI(SCPINode):
                """
                SYSTem:ERRor:SCPI

                Arguments:
                """
                __slots__ = ()
                _cmd = "SCPI"
                args = []  # type: List[str]

                class SYNTax(SCPINode, SCPIBool):
                    """
                    SYSTem:ERRor:SCPI:SYNTax

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "SYNTax"
                    args = ["1", "ON", "OFF"]

                SYNTax = SYNTax()  # type: ignore
                """
                SYSTem:ERRor:SCPI:SYNTax

                Arguments: 1, ON, OFF
                """

            SCPI = SCPI()  # type: ignore
            """
            SYSTem:ERRor:SCPI

            Arguments:
            """

        ERRor = ERRor()  # type: ignore
        """
        SYSTem:ERRor

        Arguments: NUMeric, STRing
        """

        class FILesystem(SCPINode):
            """
            SYSTem:FILesystem

            Arguments:
            """
            __slots__ = ()
            _cmd = "FILesystem"
            args = []  # type: List[str]

            class SAFemode(SCPINode, SCPIBool):
                """
                SYSTem:FILesystem:SAFemode

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "SAFemode"
                args = ["1", "ON", "OFF"]

            SAFemode = SAFemode()  # type: ignore
            """
            SYSTem:FILesystem:SAFemode

            Arguments: 1, ON, OFF
            """

        FILesystem = FILesystem()  # type: ignore
        """
        SYSTem:FILesystem

        Arguments:
        """

        class FPReset(SCPINode, SCPISet):
            """
            `SYSTem:FPReset
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a8969674f533414b.htm#ID_7d183de071cbe2940a00206a00c529ef-cb25f8cf71cbe2940a00206a012bc823-en-US>`_

            Arguments:
            """
            __slots__ = ()
            _cmd = "FPReset"
            args = []  # type: List[str]

        FPReset = FPReset()  # type: ignore
        """
        `SYSTem:FPReset
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a8969674f533414b.htm#ID_7d183de071cbe2940a00206a00c529ef-cb25f8cf71cbe2940a00206a012bc823-en-US>`_

        Arguments:
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

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "HEADers"
                args = ["'string'"]

            HEADers = HEADers()  # type: ignore
            """
            SYSTem:HELP:HEADers

            Arguments: 'string'
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

        class KEY(SCPINode):
            """
            SYSTem:KEY

            Arguments:
            """
            __slots__ = ()
            _cmd = "KEY"
            args = []  # type: List[str]

            class ASSign(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:KEY:ASSign

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ASSign"
                args = ["1"]

            ASSign = ASSign()  # type: ignore
            """
            SYSTem:KEY:ASSign

            Arguments: 1
            """

            class CLEar(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:KEY:CLEar

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "CLEar"
                args = ["1"]

            CLEar = CLEar()  # type: ignore
            """
            SYSTem:KEY:CLEar

            Arguments: 1
            """

            class DISable(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:KEY:DISable

                Arguments: SAVE
                """
                __slots__ = ()
                _cmd = "DISable"
                args = ["SAVE"]

            DISable = DISable()  # type: ignore
            """
            SYSTem:KEY:DISable

            Arguments: SAVE
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:KEY:ENABle

                Arguments: SAVE
                """
                __slots__ = ()
                _cmd = "ENABle"
                args = ["SAVE"]

            ENABle = ENABle()  # type: ignore
            """
            SYSTem:KEY:ENABle

            Arguments: SAVE
            """

        KEY = KEY()  # type: ignore
        """
        SYSTem:KEY

        Arguments:
        """

        class KLOCk(SCPINode, SCPIBool):
            """
            `SYSTem:KLOCk
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e57ad6f63f694963.htm#ID_1c2c1ab671cae4100a00206a013aa55f-c059ec8271cae4100a00206a012bc823-en-US>`_

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "KLOCk"
            args = ["1", "ON", "OFF"]

        KLOCk = KLOCk()  # type: ignore
        """
        `SYSTem:KLOCk
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e57ad6f63f694963.htm#ID_1c2c1ab671cae4100a00206a013aa55f-c059ec8271cae4100a00206a012bc823-en-US>`_

        Arguments: 1, ON, OFF
        """

        class LANGuage(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:LANGuage
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e6915ffdd7e64075.htm#ID_1282e19171cbeff10a00206a01b52e61-a5ace65d71cbeff10a00206a012bc823-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "LANGuage"
            args = ["'string'"]

        LANGuage = LANGuage()  # type: ignore
        """
        `SYSTem:LANGuage
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e6915ffdd7e64075.htm#ID_1282e19171cbeff10a00206a01b52e61-a5ace65d71cbeff10a00206a012bc823-en-US>`_

        Arguments: 'string'
        """

        class LOCK(SCPINode):
            """
            SYSTem:LOCK

            Arguments:
            """
            __slots__ = ()
            _cmd = "LOCK"
            args = []  # type: List[str]

            class NAME(SCPINode):
                """
                SYSTem:LOCK:NAME

                Arguments:
                """
                __slots__ = ()
                _cmd = "NAME"
                args = []  # type: List[str]

                class DETailed(SCPINode, SCPIQuery):
                    """
                    SYSTem:LOCK:NAME:DETailed

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "DETailed"
                    args = []  # type: List[str]

                DETailed = DETailed()  # type: ignore
                """
                SYSTem:LOCK:NAME:DETailed

                Arguments:
                """

            NAME = NAME()  # type: ignore
            """
            SYSTem:LOCK:NAME

            Arguments:
            """

            class OWNer(SCPINode, SCPIQuery):
                """
                SYSTem:LOCK:OWNer

                Arguments:
                """
                __slots__ = ()
                _cmd = "OWNer"
                args = []  # type: List[str]

                class DETailed(SCPINode, SCPIQuery):
                    """
                    SYSTem:LOCK:OWNer:DETailed

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "DETailed"
                    args = []  # type: List[str]

                DETailed = DETailed()  # type: ignore
                """
                SYSTem:LOCK:OWNer:DETailed

                Arguments:
                """

            OWNer = OWNer()  # type: ignore
            """
            SYSTem:LOCK:OWNer

            Arguments:
            """

            class RELease(SCPINode, SCPISet):
                """
                SYSTem:LOCK:RELease

                Arguments:
                """
                __slots__ = ()
                _cmd = "RELease"
                args = []  # type: List[str]

            RELease = RELease()  # type: ignore
            """
            SYSTem:LOCK:RELease

            Arguments:
            """

            class REQuest(SCPINode):
                """
                SYSTem:LOCK:REQuest

                Arguments:
                """
                __slots__ = ()
                _cmd = "REQuest"
                args = []  # type: List[str]

                class EXCLusive(SCPINode, SCPIQuery):
                    """
                    SYSTem:LOCK:REQuest:EXCLusive

                    Arguments: <integer>, INFinite
                    """
                    __slots__ = ()
                    _cmd = "EXCLusive"
                    args = ["<integer>", "INFinite"]

                EXCLusive = EXCLusive()  # type: ignore
                """
                SYSTem:LOCK:REQuest:EXCLusive

                Arguments: <integer>, INFinite
                """

                class SHARed(SCPINode, SCPIQuery):
                    """
                    SYSTem:LOCK:REQuest:SHARed

                    Arguments: <string>,<integer>, INFinite
                    """
                    __slots__ = ()
                    _cmd = "SHARed"
                    args = ["<string>,<integer>", "INFinite"]

                SHARed = SHARed()  # type: ignore
                """
                SYSTem:LOCK:REQuest:SHARed

                Arguments: <string>,<integer>, INFinite
                """

            REQuest = REQuest()  # type: ignore
            """
            SYSTem:LOCK:REQuest

            Arguments:
            """

            class SHARed(SCPINode):
                """
                SYSTem:LOCK:SHARed

                Arguments:
                """
                __slots__ = ()
                _cmd = "SHARed"
                args = []  # type: List[str]

                class STRing(SCPINode, SCPIQuery):
                    """
                    SYSTem:LOCK:SHARed:STRing

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "STRing"
                    args = []  # type: List[str]

                STRing = STRing()  # type: ignore
                """
                SYSTem:LOCK:SHARed:STRing

                Arguments:
                """

            SHARed = SHARed()  # type: ignore
            """
            SYSTem:LOCK:SHARed

            Arguments:
            """

            class TIMeout(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:LOCK:TIMeout

                Arguments: <integer>, INFinite
                """
                __slots__ = ()
                _cmd = "TIMeout"
                args = ["<integer>", "INFinite"]

            TIMeout = TIMeout()  # type: ignore
            """
            SYSTem:LOCK:TIMeout

            Arguments: <integer>, INFinite
            """

        LOCK = LOCK()  # type: ignore
        """
        SYSTem:LOCK

        Arguments:
        """

        class MMHead(SCPINode):
            """
            SYSTem:MMHead

            Arguments:
            """
            __slots__ = ()
            _cmd = "MMHead"
            args = []  # type: List[str]

            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:MMHead:SELect

                Arguments: FRONt, NONE, REAR
                """
                __slots__ = ()
                _cmd = "SELect"
                args = ["FRONt", "NONE", "REAR"]

            SELect = SELect()  # type: ignore
            """
            SYSTem:MMHead:SELect

            Arguments: FRONt, NONE, REAR
            """

        MMHead = MMHead()  # type: ignore
        """
        SYSTem:MMHead

        Arguments:
        """

        class MSEQuence(SCPINode):
            """
            SYSTem:MSEQuence

            Arguments:
            """
            __slots__ = ()
            _cmd = "MSEQuence"
            args = []  # type: List[str]

            class CATalog(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:MSEQuence:CATalog

                Arguments:
                """
                __slots__ = ()
                _cmd = "CATalog"
                args = []  # type: List[str]

            CATalog = CATalog()  # type: ignore
            """
            SYSTem:MSEQuence:CATalog

            Arguments:
            """

            class DELete(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:MSEQuence:DELete

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "DELete"
                args = ["'string'"]

            DELete = DELete()  # type: ignore
            """
            SYSTem:MSEQuence:DELete

            Arguments: 'string'
            """

            class DWELl(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:MSEQuence:DWELl

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DWELl"
                args = ["1"]

            DWELl = DWELl()  # type: ignore
            """
            SYSTem:MSEQuence:DWELl

            Arguments: 1
            """

            class RCL(SCPINode):
                """
                SYSTem:MSEQuence:RCL

                Arguments:
                """
                __slots__ = ()
                _cmd = "RCL"
                args = []  # type: List[str]

                class POINts(SCPINode, SCPIQuery):
                    """
                    SYSTem:MSEQuence:RCL:POINts

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "POINts"
                    args = []  # type: List[str]

                POINts = POINts()  # type: ignore
                """
                SYSTem:MSEQuence:RCL:POINts

                Arguments:
                """

            RCL = RCL()  # type: ignore
            """
            SYSTem:MSEQuence:RCL

            Arguments:
            """

            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:MSEQuence:SELect

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "SELect"
                args = ["'string'"]

            SELect = SELect()  # type: ignore
            """
            SYSTem:MSEQuence:SELect

            Arguments: 'string'
            """

        MSEQuence = MSEQuence()  # type: ignore
        """
        SYSTem:MSEQuence

        Arguments:
        """

        class PDOWn(SCPINode, SCPISet):
            """
            SYSTem:PDOWn

            Arguments:
            """
            __slots__ = ()
            _cmd = "PDOWn"
            args = []  # type: List[str]

        PDOWn = PDOWn()  # type: ignore
        """
        SYSTem:PDOWn

        Arguments:
        """

        class PRESet(SCPINode, SCPISet):
            """
            `SYSTem:PRESet
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/fea01e424ecf4cc4.htm#ID_a64c6dbf4ecf62470a00206a0141ec63-ed39c76a4ecf62470a00206a0024546d-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "PRESet"
            args = ["'string'"]

            class EXECute(SCPINode, SCPISet):
                """
                SYSTem:PRESet:EXECute

                Arguments:
                """
                __slots__ = ()
                _cmd = "EXECute"
                args = []  # type: List[str]

            EXECute = EXECute()  # type: ignore
            """
            SYSTem:PRESet:EXECute

            Arguments:
            """

            class LANGuage(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:PRESet:LANGuage

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "LANGuage"
                args = ["'string'"]

            LANGuage = LANGuage()  # type: ignore
            """
            SYSTem:PRESet:LANGuage

            Arguments: 'string'
            """

            class PERSistent(SCPINode, SCPISet):
                """
                SYSTem:PRESet:PERSistent

                Arguments:
                """
                __slots__ = ()
                _cmd = "PERSistent"
                args = []  # type: List[str]

            PERSistent = PERSistent()  # type: ignore
            """
            SYSTem:PRESet:PERSistent

            Arguments:
            """

            class PN(SCPINodeN, SCPIQuery, SCPISet):
                """
                SYSTem:PRESet:PN

                Arguments: NORMal, QUICk
                """
                __slots__ = ()
                _cmd = "PN"
                args = ["NORMal", "QUICk"]

            PN = PN()  # type: ignore
            """
            SYSTem:PRESet:PN

            Arguments: NORMal, QUICk
            """

        PRESet = PRESet()  # type: ignore
        """
        `SYSTem:PRESet
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/fea01e424ecf4cc4.htm#ID_a64c6dbf4ecf62470a00206a0141ec63-ed39c76a4ecf62470a00206a0024546d-en-US>`_

        Arguments: 'string'
        """

        class PROTect(SCPINodeN):
            """
            SYSTem:PROTect

            Arguments:
            """
            __slots__ = ()
            _cmd = "PROTect"
            args = []  # type: List[str]

            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:PROTect:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2be619d631aa413c.htm#ID_8573e93571caebb10a00206a0185361b-8394d8f471caebb10a00206a012bc823-en-US>`_

                Arguments: <boolean>,<numeric_value>
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["<boolean>,<numeric_value>"]

            STATe = STATe()  # type: ignore
            """
            `SYSTem:PROTect:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2be619d631aa413c.htm#ID_8573e93571caebb10a00206a0185361b-8394d8f471caebb10a00206a012bc823-en-US>`_

            Arguments: <boolean>,<numeric_value>
            """

        PROTect = PROTect()  # type: ignore
        """
        SYSTem:PROTect

        Arguments:
        """

        class RESet(SCPINode, SCPISet):
            """
            SYSTem:RESet

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "RESet"
            args = ["'string'"]

        RESet = RESet()  # type: ignore
        """
        SYSTem:RESet

        Arguments: 'string'
        """

        class SECurity(SCPINode, SCPIBool):
            """
            SYSTem:SECurity

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "SECurity"
            args = ["1", "ON", "OFF"]

            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:SECurity:COUNt

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "COUNt"
                args = ["1"]

            COUNt = COUNt()  # type: ignore
            """
            SYSTem:SECurity:COUNt

            Arguments: 1
            """

            class DISPlay(SCPINode, SCPIBool):
                """
                SYSTem:SECurity:DISPlay

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "DISPlay"
                args = ["1", "ON", "OFF"]

            DISPlay = DISPlay()  # type: ignore
            """
            SYSTem:SECurity:DISPlay

            Arguments: 1, ON, OFF
            """

            class ERASeall(SCPINode, SCPISet):
                """
                SYSTem:SECurity:ERASeall

                Arguments:
                """
                __slots__ = ()
                _cmd = "ERASeall"
                args = []  # type: List[str]

            ERASeall = ERASeall()  # type: ignore
            """
            SYSTem:SECurity:ERASeall

            Arguments:
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:SECurity:LEVel

                Arguments: ERASe, NONE, OVERwrite, SANitize
                """
                __slots__ = ()
                _cmd = "LEVel"
                args = ["ERASe", "NONE", "OVERwrite", "SANitize"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SYSTem:SECurity:LEVel:STATe

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()  # type: ignore
                """
                SYSTem:SECurity:LEVel:STATe

                Arguments: 1, ON, OFF
                """

            LEVel = LEVel()  # type: ignore
            """
            SYSTem:SECurity:LEVel

            Arguments: ERASe, NONE, OVERwrite, SANitize
            """

            class OVERwrite(SCPINode, SCPISet):
                """
                SYSTem:SECurity:OVERwrite

                Arguments:
                """
                __slots__ = ()
                _cmd = "OVERwrite"
                args = []  # type: List[str]

            OVERwrite = OVERwrite()  # type: ignore
            """
            SYSTem:SECurity:OVERwrite

            Arguments:
            """

            class SANitize(SCPINode, SCPISet):
                """
                SYSTem:SECurity:SANitize

                Arguments:
                """
                __slots__ = ()
                _cmd = "SANitize"
                args = []  # type: List[str]

            SANitize = SANitize()  # type: ignore
            """
            SYSTem:SECurity:SANitize

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                SYSTem:SECurity:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SYSTem:SECurity:STATe

            Arguments: 1, ON, OFF
            """

        SECurity = SECurity()  # type: ignore
        """
        SYSTem:SECurity

        Arguments: 1, ON, OFF
        """

        class SERRor(SCPINode, SCPIQuery):
            """
            `SYSTem:SERRor
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5399f400e2034c4e.htm#ID_6fc0f364cdeb59d40a00201901c90f84-6ec4330acdeb589c0a00201901e67c3d-en-US>`_

            Arguments:
            """
            __slots__ = ()
            _cmd = "SERRor"
            args = []  # type: List[str]

        SERRor = SERRor()  # type: ignore
        """
        `SYSTem:SERRor
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5399f400e2034c4e.htm#ID_6fc0f364cdeb59d40a00201901c90f84-6ec4330acdeb589c0a00201901e67c3d-en-US>`_

        Arguments:
        """

        class SSAVer(SCPINode, SCPISet):
            """
            SYSTem:SSAVer

            Arguments:
            """
            __slots__ = ()
            _cmd = "SSAVer"
            args = []  # type: List[str]

            class DELay(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:SSAVer:DELay

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DELay"
                args = ["1"]

            DELay = DELay()  # type: ignore
            """
            SYSTem:SSAVer:DELay

            Arguments: 1
            """

            class STATe(SCPINode, SCPIBool):
                """
                SYSTem:SSAVer:STATe

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()  # type: ignore
            """
            SYSTem:SSAVer:STATe

            Arguments: 1, ON, OFF
            """

        SSAVer = SSAVer()  # type: ignore
        """
        SYSTem:SSAVer

        Arguments:
        """

        class STATe(SCPINode, SCPISet):
            """
            SYSTem:STATe

            Arguments:
            """
            __slots__ = ()
            _cmd = "STATe"
            args = []  # type: List[str]

        STATe = STATe()  # type: ignore
        """
        SYSTem:STATe

        Arguments:
        """

        class TIME(SCPINode):
            """
            `SYSTem:TIME
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0ad7e322edac4195.htm#ID_dbb4b4c671cb9ca10a00206a00ebeda8-374d740171cb9ca10a00206a012bc823-en-US>`_

            Arguments:
            """
            __slots__ = ()
            _cmd = "TIME"
            args = []  # type: List[str]

            class DSTime(SCPINode):
                """
                SYSTem:TIME:DSTime

                Arguments:
                """
                __slots__ = ()
                _cmd = "DSTime"
                args = []  # type: List[str]

                class RULE(SCPINode):
                    """
                    SYSTem:TIME:DSTime:RULE

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "RULE"
                    args = []  # type: List[str]

                    class CATalog(SCPINode, SCPIQuery):
                        """
                        SYSTem:TIME:DSTime:RULE:CATalog

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "CATalog"
                        args = []  # type: List[str]

                    CATalog = CATalog()  # type: ignore
                    """
                    SYSTem:TIME:DSTime:RULE:CATalog

                    Arguments:
                    """

                RULE = RULE()  # type: ignore
                """
                SYSTem:TIME:DSTime:RULE

                Arguments:
                """

            DSTime = DSTime()  # type: ignore
            """
            SYSTem:TIME:DSTime

            Arguments:
            """

            class HRTimer(SCPINode):
                """
                SYSTem:TIME:HRTimer

                Arguments:
                """
                __slots__ = ()
                _cmd = "HRTimer"
                args = []  # type: List[str]

                class ABSolute(SCPINode, SCPISet):
                    """
                    SYSTem:TIME:HRTimer:ABSolute

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "ABSolute"
                    args = ["1"]

                ABSolute = ABSolute()  # type: ignore
                """
                SYSTem:TIME:HRTimer:ABSolute

                Arguments: 1
                """

                class RELative(SCPINode, SCPISet):
                    """
                    SYSTem:TIME:HRTimer:RELative

                    Arguments: 1
                    """
                    __slots__ = ()
                    _cmd = "RELative"
                    args = ["1"]

                RELative = RELative()  # type: ignore
                """
                SYSTem:TIME:HRTimer:RELative

                Arguments: 1
                """

            HRTimer = HRTimer()  # type: ignore
            """
            SYSTem:TIME:HRTimer

            Arguments:
            """

            class LOCal(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:TIME:LOCal

                Arguments: <integer>,<integer>,<integer>
                """
                __slots__ = ()
                _cmd = "LOCal"
                args = ["<integer>,<integer>,<integer>"]

            LOCal = LOCal()  # type: ignore
            """
            SYSTem:TIME:LOCal

            Arguments: <integer>,<integer>,<integer>
            """

        TIME = TIME()  # type: ignore
        """
        `SYSTem:TIME
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/0ad7e322edac4195.htm#ID_dbb4b4c671cb9ca10a00206a00ebeda8-374d740171cb9ca10a00206a012bc823-en-US>`_

        Arguments:
        """

        class TZONe(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:TZONe

            Arguments: <numeric_value>,<numeric_value>
            """
            __slots__ = ()
            _cmd = "TZONe"
            args = ["<numeric_value>,<numeric_value>"]

        TZONe = TZONe()  # type: ignore
        """
        SYSTem:TZONe

        Arguments: <numeric_value>,<numeric_value>
        """

        class VERSion(SCPINode, SCPIQuery):
            """
            `SYSTem:VERSion
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/1687c21d3b684121.htm#ID_83b8bf4871d1f0010a00206a01566d1c-c7a8cef471d1f0010a00206a012bc823-en-US>`_

            Arguments:
            """
            __slots__ = ()
            _cmd = "VERSion"
            args = []  # type: List[str]

        VERSion = VERSion()  # type: ignore
        """
        `SYSTem:VERSion
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/1687c21d3b684121.htm#ID_83b8bf4871d1f0010a00206a01566d1c-c7a8cef471d1f0010a00206a012bc823-en-US>`_

        Arguments:
        """

    SYSTem = SYSTem()  # type: ignore
    """
    SYSTem

    Arguments:
    """

    class TAlk_terminator(SCPINode, SCPISet):
        """
        TAlk_terminator

        Arguments:
        """
        __slots__ = ()
        _cmd = "TAlk_terminator"
        args = []  # type: List[str]

        class Cr_nl_end(SCPINode, SCPISet):
            """
            TAlk_terminator:Cr_nl_end

            Arguments:
            """
            __slots__ = ()
            _cmd = "Cr_nl_end"
            args = []  # type: List[str]

        Cr_nl_end = Cr_nl_end()  # type: ignore
        """
        TAlk_terminator:Cr_nl_end

        Arguments:
        """

        class Nl_end(SCPINode, SCPISet):
            """
            TAlk_terminator:Nl_end

            Arguments:
            """
            __slots__ = ()
            _cmd = "Nl_end"
            args = []  # type: List[str]

        Nl_end = Nl_end()  # type: ignore
        """
        TAlk_terminator:Nl_end

        Arguments:
        """

    TAlk_terminator = TAlk_terminator()  # type: ignore
    """
    TAlk_terminator

    Arguments:
    """

    class TEst(SCPINode, SCPISet):
        """
        TEst

        Arguments:
        """
        __slots__ = ()
        _cmd = "TEst"
        args = []  # type: List[str]

        class Point(SCPINode, SCPIQuery, SCPISet):
            """
            TEst:Point

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "Point"
            args = ["1"]

        Point = Point()  # type: ignore
        """
        TEst:Point

        Arguments: 1
        """

        class Voltage(SCPINode, SCPIQuery, SCPISet):
            """
            TEst:Voltage

            Arguments:
            """
            __slots__ = ()
            _cmd = "Voltage"
            args = []  # type: List[str]

        Voltage = Voltage()  # type: ignore
        """
        TEst:Voltage

        Arguments:
        """

    TEst = TEst()  # type: ignore
    """
    TEst

    Arguments:
    """

    class TIme(SCPINode):
        """
        TIme

        Arguments:
        """
        __slots__ = ()
        _cmd = "TIme"
        args = []  # type: List[str]

        class AF_swp(SCPINode, SCPIQuery, SCPISet):
            """
            TIme:AF_swp

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "AF_swp"
            args = ["1"]

        AF_swp = AF_swp()  # type: ignore
        """
        TIme:AF_swp

        Arguments: 1
        """

        class CF_swp(SCPINode, SCPIQuery, SCPISet):
            """
            TIme:CF_swp

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "CF_swp"
            args = ["1"]

        CF_swp = CF_swp()  # type: ignore
        """
        TIme:CF_swp

        Arguments: 1
        """

        class MEmory_swp(SCPINode, SCPIQuery, SCPISet):
            """
            TIme:MEmory_swp

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "MEmory_swp"
            args = ["1"]

            class Fast(SCPINode, SCPIQuery, SCPISet):
                """
                TIme:MEmory_swp:Fast

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "Fast"
                args = ["1"]

            Fast = Fast()  # type: ignore
            """
            TIme:MEmory_swp:Fast

            Arguments: 1
            """

        MEmory_swp = MEmory_swp()  # type: ignore
        """
        TIme:MEmory_swp

        Arguments: 1
        """

        class RF_swp(SCPINode, SCPIQuery, SCPISet):
            """
            TIme:RF_swp

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "RF_swp"
            args = ["1"]

        RF_swp = RF_swp()  # type: ignore
        """
        TIme:RF_swp

        Arguments: 1
        """

    TIme = TIme()  # type: ignore
    """
    TIme

    Arguments:
    """

    class TRIGger(SCPINode, SCPISet):
        """
        TRIGger

        Arguments:
        """
        __slots__ = ()
        _cmd = "TRIGger"
        args = []  # type: List[str]

        class DM(SCPINode):
            """
            TRIGger:DM

            Arguments:
            """
            __slots__ = ()
            _cmd = "DM"
            args = []  # type: List[str]

            class IMMediate(SCPINode, SCPISet):
                """
                TRIGger:DM:IMMediate

                Arguments:
                """
                __slots__ = ()
                _cmd = "IMMediate"
                args = []  # type: List[str]

            IMMediate = IMMediate()  # type: ignore
            """
            TRIGger:DM:IMMediate

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:DM:SOURce

                Arguments: AUTO, EXTernal, SINGle
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()  # type: ignore
            """
            TRIGger:DM:SOURce

            Arguments: AUTO, EXTernal, SINGle
            """

        DM = DM()  # type: ignore
        """
        TRIGger:DM

        Arguments:
        """

        class FSWeep(SCPINode):
            """
            TRIGger:FSWeep

            Arguments:
            """
            __slots__ = ()
            _cmd = "FSWeep"
            args = []  # type: List[str]

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:FSWeep:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/673177c779ae404e.htm#ID_06cb678671bda0350a00206a01b91256-cb80732271bda0350a00206a012bc823-en-US>`_

                Arguments: AUTO, EXTernal, SINGle
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()  # type: ignore
            """
            `TRIGger:FSWeep:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/673177c779ae404e.htm#ID_06cb678671bda0350a00206a01b91256-cb80732271bda0350a00206a012bc823-en-US>`_

            Arguments: AUTO, EXTernal, SINGle
            """

        FSWeep = FSWeep()  # type: ignore
        """
        TRIGger:FSWeep

        Arguments:
        """

        class IMMediate(SCPINode, SCPISet):
            """
            `TRIGger:IMMediate
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/d4ef093297e1451c.htm#ID_4d0a658571bdb5730a00206a006f27c0-2860086d71bdb5730a00206a012bc823-en-US>`_

            Arguments:
            """
            __slots__ = ()
            _cmd = "IMMediate"
            args = []  # type: List[str]

        IMMediate = IMMediate()  # type: ignore
        """
        `TRIGger:IMMediate
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/d4ef093297e1451c.htm#ID_4d0a658571bdb5730a00206a006f27c0-2860086d71bdb5730a00206a012bc823-en-US>`_

        Arguments:
        """

        class LIST(SCPINode):
            """
            TRIGger:LIST

            Arguments:
            """
            __slots__ = ()
            _cmd = "LIST"
            args = []  # type: List[str]

            class IMMediate(SCPINode, SCPISet):
                """
                TRIGger:LIST:IMMediate

                Arguments:
                """
                __slots__ = ()
                _cmd = "IMMediate"
                args = []  # type: List[str]

            IMMediate = IMMediate()  # type: ignore
            """
            TRIGger:LIST:IMMediate

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:LIST:SOURce

                Arguments: AUTO, EXTernal, SINGle
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()  # type: ignore
            """
            TRIGger:LIST:SOURce

            Arguments: AUTO, EXTernal, SINGle
            """

        LIST = LIST()  # type: ignore
        """
        TRIGger:LIST

        Arguments:
        """

        class MSEQuence(SCPINode):
            """
            TRIGger:MSEQuence

            Arguments:
            """
            __slots__ = ()
            _cmd = "MSEQuence"
            args = []  # type: List[str]

            class IMMediate(SCPINode, SCPISet):
                """
                TRIGger:MSEQuence:IMMediate

                Arguments:
                """
                __slots__ = ()
                _cmd = "IMMediate"
                args = []  # type: List[str]

            IMMediate = IMMediate()  # type: ignore
            """
            TRIGger:MSEQuence:IMMediate

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:MSEQuence:SOURce

                Arguments: AUTO, EXTernal, SINGle
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()  # type: ignore
            """
            TRIGger:MSEQuence:SOURce

            Arguments: AUTO, EXTernal, SINGle
            """

        MSEQuence = MSEQuence()  # type: ignore
        """
        TRIGger:MSEQuence

        Arguments:
        """

        class ODELay(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:ODELay

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "ODELay"
            args = ["1"]

        ODELay = ODELay()  # type: ignore
        """
        TRIGger:ODELay

        Arguments: 1
        """

        class OUTPut(SCPINode, SCPISet):
            """
            TRIGger:OUTPut

            Arguments:
            """
            __slots__ = ()
            _cmd = "OUTPut"
            args = []  # type: List[str]

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:OUTPut:POLarity

                Arguments: NEGative, POSitive
                """
                __slots__ = ()
                _cmd = "POLarity"
                args = ["NEGative", "POSitive"]

            POLarity = POLarity()  # type: ignore
            """
            TRIGger:OUTPut:POLarity

            Arguments: NEGative, POSitive
            """

        OUTPut = OUTPut()  # type: ignore
        """
        TRIGger:OUTPut

        Arguments:
        """

        class PSWeep(SCPINode):
            """
            TRIGger:PSWeep

            Arguments:
            """
            __slots__ = ()
            _cmd = "PSWeep"
            args = []  # type: List[str]

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:PSWeep:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3bdb2b0d8df44740.htm#ID_77ad610d71bda6ec0a00206a018a2840-7d255c2071bda6ec0a00206a012bc823-en-US>`_

                Arguments: AUTO, EXTernal, SINGle
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()  # type: ignore
            """
            `TRIGger:PSWeep:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3bdb2b0d8df44740.htm#ID_77ad610d71bda6ec0a00206a018a2840-7d255c2071bda6ec0a00206a012bc823-en-US>`_

            Arguments: AUTO, EXTernal, SINGle
            """

        PSWeep = PSWeep()  # type: ignore
        """
        TRIGger:PSWeep

        Arguments:
        """

        class PULSe(SCPINode):
            """
            TRIGger:PULSe

            Arguments:
            """
            __slots__ = ()
            _cmd = "PULSe"
            args = []  # type: List[str]

            class EGATed(SCPINode):
                """
                TRIGger:PULSe:EGATed

                Arguments:
                """
                __slots__ = ()
                _cmd = "EGATed"
                args = []  # type: List[str]

                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    TRIGger:PULSe:EGATed:POLarity

                    Arguments: INVerted, NORMal
                    """
                    __slots__ = ()
                    _cmd = "POLarity"
                    args = ["INVerted", "NORMal"]

                POLarity = POLarity()  # type: ignore
                """
                TRIGger:PULSe:EGATed:POLarity

                Arguments: INVerted, NORMal
                """

            EGATed = EGATed()  # type: ignore
            """
            TRIGger:PULSe:EGATed

            Arguments:
            """

            class IMMediate(SCPINode, SCPISet):
                """
                TRIGger:PULSe:IMMediate

                Arguments:
                """
                __slots__ = ()
                _cmd = "IMMediate"
                args = []  # type: List[str]

            IMMediate = IMMediate()  # type: ignore
            """
            TRIGger:PULSe:IMMediate

            Arguments:
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:PULSe:LEVel

                Arguments: TTL, V05, VM25
                """
                __slots__ = ()
                _cmd = "LEVel"
                args = ["TTL", "V05", "VM25"]

            LEVel = LEVel()  # type: ignore
            """
            TRIGger:PULSe:LEVel

            Arguments: TTL, V05, VM25
            """

            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:PULSe:SLOPe

                Arguments: NEGative, POSitive
                """
                __slots__ = ()
                _cmd = "SLOPe"
                args = ["NEGative", "POSitive"]

            SLOPe = SLOPe()  # type: ignore
            """
            TRIGger:PULSe:SLOPe

            Arguments: NEGative, POSitive
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:PULSe:SOURce

                Arguments: AUTO, EGATed, EXT_gated, EXTern, EXTernal, SINGle
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["AUTO", "EGATed", "EXT_gated", "EXTern", "EXTernal", "SINGle"]

            SOURce = SOURce()  # type: ignore
            """
            TRIGger:PULSe:SOURce

            Arguments: AUTO, EGATed, EXT_gated, EXTern, EXTernal, SINGle
            """

        PULSe = PULSe()  # type: ignore
        """
        TRIGger:PULSe

        Arguments:
        """

        class SEQuence(SCPINode):
            """
            TRIGger:SEQuence

            Arguments:
            """
            __slots__ = ()
            _cmd = "SEQuence"
            args = []  # type: List[str]

            class IMMediate(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:SEQuence:IMMediate

                Arguments:
                """
                __slots__ = ()
                _cmd = "IMMediate"
                args = []  # type: List[str]

            IMMediate = IMMediate()  # type: ignore
            """
            TRIGger:SEQuence:IMMediate

            Arguments:
            """

            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:SEQuence:SLOPe

                Arguments: NEGative, POSitive
                """
                __slots__ = ()
                _cmd = "SLOPe"
                args = ["NEGative", "POSitive"]

            SLOPe = SLOPe()  # type: ignore
            """
            TRIGger:SEQuence:SLOPe

            Arguments: NEGative, POSitive
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:SEQuence:SOURce

                Arguments: BUS, EXTernal, HOLD, IMMediate
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["BUS", "EXTernal", "HOLD", "IMMediate"]

            SOURce = SOURce()  # type: ignore
            """
            TRIGger:SEQuence:SOURce

            Arguments: BUS, EXTernal, HOLD, IMMediate
            """

            class STOP(SCPINode):
                """
                TRIGger:SEQuence:STOP

                Arguments:
                """
                __slots__ = ()
                _cmd = "STOP"
                args = []  # type: List[str]

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    TRIGger:SEQuence:STOP:SOURce

                    Arguments: EXTernal, IMMediate
                    """
                    __slots__ = ()
                    _cmd = "SOURce"
                    args = ["EXTernal", "IMMediate"]

                SOURce = SOURce()  # type: ignore
                """
                TRIGger:SEQuence:STOP:SOURce

                Arguments: EXTernal, IMMediate
                """

            STOP = STOP()  # type: ignore
            """
            TRIGger:SEQuence:STOP

            Arguments:
            """

        SEQuence = SEQuence()  # type: ignore
        """
        TRIGger:SEQuence

        Arguments:
        """

        class SLOPe(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:SLOPe

            Arguments: EITHer, NEGative, POSitive
            """
            __slots__ = ()
            _cmd = "SLOPe"
            args = ["EITHer", "NEGative", "POSitive"]

        SLOPe = SLOPe()  # type: ignore
        """
        TRIGger:SLOPe

        Arguments: EITHer, NEGative, POSitive
        """

        class STARt(SCPINode):
            """
            TRIGger:STARt

            Arguments:
            """
            __slots__ = ()
            _cmd = "STARt"
            args = []  # type: List[str]

            class IMMediate(SCPINode, SCPISet):
                """
                TRIGger:STARt:IMMediate

                Arguments:
                """
                __slots__ = ()
                _cmd = "IMMediate"
                args = []  # type: List[str]

            IMMediate = IMMediate()  # type: ignore
            """
            TRIGger:STARt:IMMediate

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:STARt:SOURce

                Arguments: BUS, EXTernal, HOLD, IMMediate
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["BUS", "EXTernal", "HOLD", "IMMediate"]

            SOURce = SOURce()  # type: ignore
            """
            TRIGger:STARt:SOURce

            Arguments: BUS, EXTernal, HOLD, IMMediate
            """

        STARt = STARt()  # type: ignore
        """
        TRIGger:STARt

        Arguments:
        """

        class SWEep(SCPINode):
            """
            TRIGger:SWEep

            Arguments:
            """
            __slots__ = ()
            _cmd = "SWEep"
            args = []  # type: List[str]

            class IMMediate(SCPINode, SCPISet):
                """
                `TRIGger:SWEep:IMMediate
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/20e5ba8fcf2b4332.htm#ID_88ce59a571bdae100a00206a008814e4-d4d3ebe871bdae100a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "IMMediate"
                args = []  # type: List[str]

            IMMediate = IMMediate()  # type: ignore
            """
            `TRIGger:SWEep:IMMediate
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/20e5ba8fcf2b4332.htm#ID_88ce59a571bdae100a00206a008814e4-d4d3ebe871bdae100a00206a012bc823-en-US>`_

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SWEep:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e40fc9dd64154e1e.htm#ID_2d45b80571bd99020a00206a015e8a83-7005204271bd99020a00206a012bc823-en-US>`_

                Arguments: AUTO, EXTernal, SINGle
                """
                __slots__ = ()
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()  # type: ignore
            """
            `TRIGger:SWEep:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e40fc9dd64154e1e.htm#ID_2d45b80571bd99020a00206a015e8a83-7005204271bd99020a00206a012bc823-en-US>`_

            Arguments: AUTO, EXTernal, SINGle
            """

        SWEep = SWEep()  # type: ignore
        """
        TRIGger:SWEep

        Arguments:
        """

    TRIGger = TRIGger()  # type: ignore
    """
    TRIGger

    Arguments:
    """

    class TSWeep(SCPINode, SCPISet):
        """
        TSWeep

        Arguments:
        """
        __slots__ = ()
        _cmd = "TSWeep"
        args = []  # type: List[str]

    TSWeep = TSWeep()  # type: ignore
    """
    TSWeep

    Arguments:
    """

    class VECTor(SCPINode, SCPISet):
        """
        VECTor

        Arguments:
        """
        __slots__ = ()
        _cmd = "VECTor"
        args = []  # type: List[str]

        class CONFig(SCPINode, SCPIQuery):
            """
            VECTor:CONFig

            Arguments:
            """
            __slots__ = ()
            _cmd = "CONFig"
            args = []  # type: List[str]

            class MIXer(SCPINode, SCPISet):
                """
                VECTor:CONFig:MIXer

                Arguments: EXTernal, INTernal
                """
                __slots__ = ()
                _cmd = "MIXer"
                args = ["EXTernal", "INTernal"]

            MIXer = MIXer()  # type: ignore
            """
            VECTor:CONFig:MIXer

            Arguments: EXTernal, INTernal
            """

            class PULSe(SCPINode, SCPISet):
                """
                VECTor:CONFig:PULSe

                Arguments: DISabled, ENABled
                """
                __slots__ = ()
                _cmd = "PULSe"
                args = ["DISabled", "ENABled"]

            PULSe = PULSe()  # type: ignore
            """
            VECTor:CONFig:PULSe

            Arguments: DISabled, ENABled
            """

        CONFig = CONFig()  # type: ignore
        """
        VECTor:CONFig

        Arguments:
        """

        class FADing(SCPINode, SCPIQuery):
            """
            VECTor:FADing

            Arguments:
            """
            __slots__ = ()
            _cmd = "FADing"
            args = []  # type: List[str]

            class DIR_dopp(SCPINode, SCPISet):
                """
                VECTor:FADing:DIR_dopp

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "DIR_dopp"
                args = ["1"]

            DIR_dopp = DIR_dopp()  # type: ignore
            """
            VECTor:FADing:DIR_dopp

            Arguments: 1
            """

            class RATio(SCPINode, SCPISet):
                """
                VECTor:FADing:RATio

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "RATio"
                args = ["1"]

            RATio = RATio()  # type: ignore
            """
            VECTor:FADing:RATio

            Arguments: 1
            """

            class SPEed(SCPINode, SCPISet):
                """
                VECTor:FADing:SPEed

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "SPEed"
                args = ["1"]

            SPEed = SPEed()  # type: ignore
            """
            VECTor:FADing:SPEed

            Arguments: 1
            """

        FADing = FADing()  # type: ignore
        """
        VECTor:FADing

        Arguments:
        """

        class MODopt(SCPINode, SCPIQuery):
            """
            VECTor:MODopt

            Arguments:
            """
            __slots__ = ()
            _cmd = "MODopt"
            args = []  # type: List[str]

            class ENVelope(SCPINode, SCPISet):
                """
                VECTor:MODopt:ENVelope

                Arguments: DISabled, ENABled
                """
                __slots__ = ()
                _cmd = "ENVelope"
                args = ["DISabled", "ENABled"]

            ENVelope = ENVelope()  # type: ignore
            """
            VECTor:MODopt:ENVelope

            Arguments: DISabled, ENABled
            """

            class MODPol(SCPINode, SCPISet):
                """
                VECTor:MODopt:MODPol

                Arguments: INVerse, NORMal
                """
                __slots__ = ()
                _cmd = "MODPol"
                args = ["INVerse", "NORMal"]

            MODPol = MODPol()  # type: ignore
            """
            VECTor:MODopt:MODPol

            Arguments: INVerse, NORMal
            """

        MODopt = MODopt()  # type: ignore
        """
        VECTor:MODopt

        Arguments:
        """

    VECTor = VECTor()  # type: ignore
    """
    VECTor

    Arguments:
    """

    class VMETer(SCPINode):
        """
        VMETer

        Arguments:
        """
        __slots__ = ()
        _cmd = "VMETer"
        args = []  # type: List[str]

        class VOLTage(SCPINode, SCPIQuery):
            """
            VMETer:VOLTage

            Arguments: 1
            """
            __slots__ = ()
            _cmd = "VOLTage"
            args = ["1"]

        VOLTage = VOLTage()  # type: ignore
        """
        VMETer:VOLTage

        Arguments: 1
        """

    VMETer = VMETer()  # type: ignore
    """
    VMETer

    Arguments:
    """

    class WAVeform(SCPINode, SCPIQuery, SCPISet):
        """
        WAVeform

        Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
        """
        __slots__ = ()
        _cmd = "WAVeform"
        args = ["SAWTooth", "SINE", "SQUare", "TRIangle", "WGNoise"]

    WAVeform = WAVeform()  # type: ignore
    """
    WAVeform

    Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
    """


SMB100A_gen._SCPI_class = SMB100A_gen
# END OF SMB100A_gen
