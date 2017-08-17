# -*- coding: utf-8 -*-
# Generated from SMB100A_syntax.txt on 2017-08-17 11:20
from RSSscpi.SCPI_gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool
from RSSscpi.Instrument import Instrument


class SMB100A_gen(Instrument):
    class ABO(SCPINode, SCPISet):
        """
        &ABO

        Arguments:
        """
        _cmd = "&ABO"
        args = []

    ABO = ABO()
    """
    &ABO

    Arguments:
    """

    class BRK(SCPINode, SCPISet):
        """
        &BRK

        Arguments:
        """
        _cmd = "&BRK"
        args = []

    BRK = BRK()
    """
    &BRK

    Arguments:
    """

    class DCL(SCPINode, SCPISet):
        """
        &DCL

        Arguments:
        """
        _cmd = "&DCL"
        args = []

    DCL = DCL()
    """
    &DCL

    Arguments:
    """

    class DFC(SCPINode, SCPISet):
        """
        &DFC

        Arguments:
        """
        _cmd = "&DFC"
        args = []

    DFC = DFC()
    """
    &DFC

    Arguments:
    """

    class GET(SCPINode, SCPISet):
        """
        &GET

        Arguments:
        """
        _cmd = "&GET"
        args = []

    GET = GET()
    """
    &GET

    Arguments:
    """

    class GTL(SCPINode, SCPISet):
        """
        &GTL

        Arguments:
        """
        _cmd = "&GTL"
        args = []

    GTL = GTL()
    """
    &GTL

    Arguments:
    """

    class GTM(SCPINode, SCPISet):
        """
        &GTM

        Arguments:
        """
        _cmd = "&GTM"
        args = []

    GTM = GTM()
    """
    &GTM

    Arguments:
    """

    class GTR(SCPINode, SCPISet):
        """
        &GTR

        Arguments:
        """
        _cmd = "&GTR"
        args = []

    GTR = GTR()
    """
    &GTR

    Arguments:
    """

    class HFC(SCPINode, SCPISet):
        """
        &HFC

        Arguments:
        """
        _cmd = "&HFC"
        args = []

    HFC = HFC()
    """
    &HFC

    Arguments:
    """

    class NREN(SCPINode, SCPISet):
        """
        &NREN

        Arguments:
        """
        _cmd = "&NREN"
        args = []

    NREN = NREN()
    """
    &NREN

    Arguments:
    """

    class POL(SCPINode, SCPISet):
        """
        &POL

        Arguments:
        """
        _cmd = "&POL"
        args = []

    POL = POL()
    """
    &POL

    Arguments:
    """

    class RLSD(SCPINode, SCPISet):
        """
        &RLSD

        Arguments:
        """
        _cmd = "&RLSD"
        args = []

    RLSD = RLSD()
    """
    &RLSD

    Arguments:
    """

    class SFC(SCPINode, SCPISet):
        """
        &SFC

        Arguments:
        """
        _cmd = "&SFC"
        args = []

    SFC = SFC()
    """
    &SFC

    Arguments:
    """

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

    class DEV(SCPINode, SCPIQuery, SCPISet):
        """
        *DEV

        Arguments: 1
        """
        _cmd = "*DEV"
        args = ["1"]

    DEV = DEV()
    """
    *DEV

    Arguments: 1
    """

    class DMC(SCPINode, SCPIQuery, SCPISet):
        """
        *DMC

        Arguments: <string>,<string>
        """
        _cmd = "*DMC"
        args = ["<string>,<string>"]

    DMC = DMC()
    """
    *DMC

    Arguments: <string>,<string>
    """

    class EMC(SCPINode, SCPIBool):
        """
        *EMC

        Arguments: 1, ON, OFF
        """
        _cmd = "*EMC"
        args = ["1", "ON", "OFF"]

    EMC = EMC()
    """
    *EMC

    Arguments: 1, ON, OFF
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

    class GCLS(SCPINode, SCPISet):
        """
        *GCLS

        Arguments:
        """
        _cmd = "*GCLS"
        args = []

    GCLS = GCLS()
    """
    *GCLS

    Arguments:
    """

    class GMC(SCPINode, SCPIQuery):
        """
        *GMC

        Arguments: 'string'
        """
        _cmd = "*GMC"
        args = ["'string'"]

    GMC = GMC()
    """
    *GMC

    Arguments: 'string'
    """

    class GOPC(SCPINode, SCPIQuery):
        """
        *GOPC

        Arguments:
        """
        _cmd = "*GOPC"
        args = []

    GOPC = GOPC()
    """
    *GOPC

    Arguments:
    """

    class GWAI(SCPINode, SCPISet):
        """
        *GWAI

        Arguments:
        """
        _cmd = "*GWAI"
        args = []

    GWAI = GWAI()
    """
    *GWAI

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

    class LMC(SCPINode, SCPIQuery):
        """
        *LMC

        Arguments:
        """
        _cmd = "*LMC"
        args = []

    LMC = LMC()
    """
    *LMC

    Arguments:
    """

    class LRN(SCPINode, SCPIQuery):
        """
        *LRN

        Arguments:
        """
        _cmd = "*LRN"
        args = []

    LRN = LRN()
    """
    *LRN

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

    class PMC(SCPINode, SCPISet):
        """
        *PMC

        Arguments:
        """
        _cmd = "*PMC"
        args = []

    PMC = PMC()
    """
    *PMC

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

    class PSC(SCPINode, SCPIBool):
        """
        *PSC

        Arguments: 1, ON, OFF
        """
        _cmd = "*PSC"
        args = ["1", "ON", "OFF"]

    PSC = PSC()
    """
    *PSC

    Arguments: 1, ON, OFF
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

    class RMC(SCPINode, SCPISet):
        """
        *RMC

        Arguments: 'string'
        """
        _cmd = "*RMC"
        args = ["'string'"]

    RMC = RMC()
    """
    *RMC

    Arguments: 'string'
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

    class SRQ(SCPINode, SCPIQuery):
        """
        *SRQ

        Arguments: <integer>, DOWN, MAXimum, MINimum, UP
        """
        _cmd = "*SRQ"
        args = ["<integer>", "DOWN", "MAXimum", "MINimum", "UP"]

    SRQ = SRQ()
    """
    *SRQ

    Arguments: <integer>, DOWN, MAXimum, MINimum, UP
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

    class XESE(SCPINode, SCPIQuery, SCPISet):
        """
        *XESE

        Arguments: <expression>
        """
        _cmd = "*XESE"
        args = ["<expression>"]

    XESE = XESE()
    """
    *XESE

    Arguments: <expression>
    """

    class XESR(SCPINode, SCPIQuery):
        """
        *XESR

        Arguments:
        """
        _cmd = "*XESR"
        args = []

    XESR = XESR()
    """
    *XESR

    Arguments:
    """

    class XPRE(SCPINode, SCPIQuery, SCPISet):
        """
        *XPRE

        Arguments: <expression>
        """
        _cmd = "*XPRE"
        args = ["<expression>"]

    XPRE = XPRE()
    """
    *XPRE

    Arguments: <expression>
    """

    class XSRE(SCPINode, SCPIQuery, SCPISet):
        """
        *XSRE

        Arguments: <expression>
        """
        _cmd = "*XSRE"
        args = ["<expression>"]

    XSRE = XSRE()
    """
    *XSRE

    Arguments: <expression>
    """

    class XSTB(SCPINode, SCPIQuery):
        """
        *XSTB

        Arguments:
        """
        _cmd = "*XSTB"
        args = []

    XSTB = XSTB()
    """
    *XSTB

    Arguments:
    """

    class LLO(SCPINode, SCPISet):
        """
        @LLO

        Arguments:
        """
        _cmd = "@LLO"
        args = []

    LLO = LLO()
    """
    @LLO

    Arguments:
    """

    class LOC(SCPINode, SCPISet):
        """
        @LOC

        Arguments:
        """
        _cmd = "@LOC"
        args = []

    LOC = LOC()
    """
    @LOC

    Arguments:
    """

    class ABORt(SCPINode, SCPISet):
        """
        ABORt

        Arguments:
        """
        _cmd = "ABORt"
        args = []

        class MSEQuence(SCPINode, SCPISet):
            """
            ABORt:MSEQuence

            Arguments:
            """
            _cmd = "MSEQuence"
            args = []

        MSEQuence = MSEQuence()
        """
        ABORt:MSEQuence

        Arguments:
        """

        class SWEep(SCPINode, SCPISet):
            """
            ABORt:SWEep

            Arguments:
            """
            _cmd = "SWEep"
            args = []

        SWEep = SWEep()
        """
        ABORt:SWEep

        Arguments:
        """

    ABORt = ABORt()
    """
    ABORt

    Arguments:
    """

    class AMPLitude(SCPINode):
        """
        AMPLitude

        Arguments:
        """
        _cmd = "AMPLitude"
        args = []

        class OUT(SCPINode):
            """
            AMPLitude:OUT

            Arguments:
            """
            _cmd = "OUT"
            args = []

            class ALC(SCPINode):
                """
                AMPLitude:OUT:ALC

                Arguments:
                """
                _cmd = "ALC"
                args = []

                class BANDwidth(SCPINode, SCPISet):
                    """
                    AMPLitude:OUT:ALC:BANDwidth

                    Arguments:
                    """
                    _cmd = "BANDwidth"
                    args = []

                BANDwidth = BANDwidth()
                """
                AMPLitude:OUT:ALC:BANDwidth

                Arguments:
                """

            ALC = ALC()
            """
            AMPLitude:OUT:ALC

            Arguments:
            """

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:OUT:ATTenuation

                Arguments: 1
                """
                _cmd = "ATTenuation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    AMPLitude:OUT:ATTenuation:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        AMPLitude:OUT:ATTenuation:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    AMPLitude:OUT:ATTenuation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                AMPLitude:OUT:ATTenuation:STEP

                Arguments:
                """

            ATTenuation = ATTenuation()
            """
            AMPLitude:OUT:ATTenuation

            Arguments: 1
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:OUT:LEVel

                Arguments: 1
                """
                _cmd = "LEVel"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    AMPLitude:OUT:LEVel:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        AMPLitude:OUT:LEVel:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    AMPLitude:OUT:LEVel:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                AMPLitude:OUT:LEVel:STEP

                Arguments:
                """

            LEVel = LEVel()
            """
            AMPLitude:OUT:LEVel

            Arguments: 1
            """

            class MUTing(SCPINode, SCPIBool):
                """
                AMPLitude:OUT:MUTing

                Arguments: 1, ON, OFF
                """
                _cmd = "MUTing"
                args = ["1", "ON", "OFF"]

            MUTing = MUTing()
            """
            AMPLitude:OUT:MUTing

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                AMPLitude:OUT:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            AMPLitude:OUT:STATe

            Arguments: 1, ON, OFF
            """

            class ULIMit(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:OUT:ULIMit

                Arguments: 1
                """
                _cmd = "ULIMit"
                args = ["1"]

            ULIMit = ULIMit()
            """
            AMPLitude:OUT:ULIMit

            Arguments: 1
            """

        OUT = OUT()
        """
        AMPLitude:OUT

        Arguments:
        """

        class SOURce(SCPINode):
            """
            AMPLitude:SOURce

            Arguments:
            """
            _cmd = "SOURce"
            args = []

            class ALC(SCPINode):
                """
                AMPLitude:SOURce:ALC

                Arguments:
                """
                _cmd = "ALC"
                args = []

                class BANDwidth(SCPINode, SCPISet):
                    """
                    AMPLitude:SOURce:ALC:BANDwidth

                    Arguments:
                    """
                    _cmd = "BANDwidth"
                    args = []

                BANDwidth = BANDwidth()
                """
                AMPLitude:SOURce:ALC:BANDwidth

                Arguments:
                """

            ALC = ALC()
            """
            AMPLitude:SOURce:ALC

            Arguments:
            """

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:SOURce:ATTenuation

                Arguments: 1
                """
                _cmd = "ATTenuation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    AMPLitude:SOURce:ATTenuation:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        AMPLitude:SOURce:ATTenuation:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    AMPLitude:SOURce:ATTenuation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                AMPLitude:SOURce:ATTenuation:STEP

                Arguments:
                """

            ATTenuation = ATTenuation()
            """
            AMPLitude:SOURce:ATTenuation

            Arguments: 1
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:SOURce:LEVel

                Arguments: 1
                """
                _cmd = "LEVel"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    AMPLitude:SOURce:LEVel:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        AMPLitude:SOURce:LEVel:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    AMPLitude:SOURce:LEVel:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                AMPLitude:SOURce:LEVel:STEP

                Arguments:
                """

            LEVel = LEVel()
            """
            AMPLitude:SOURce:LEVel

            Arguments: 1
            """

            class MUTing(SCPINode, SCPIBool):
                """
                AMPLitude:SOURce:MUTing

                Arguments: 1, ON, OFF
                """
                _cmd = "MUTing"
                args = ["1", "ON", "OFF"]

            MUTing = MUTing()
            """
            AMPLitude:SOURce:MUTing

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                AMPLitude:SOURce:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            AMPLitude:SOURce:STATe

            Arguments: 1, ON, OFF
            """

            class ULIMit(SCPINode, SCPIQuery, SCPISet):
                """
                AMPLitude:SOURce:ULIMit

                Arguments: 1
                """
                _cmd = "ULIMit"
                args = ["1"]

            ULIMit = ULIMit()
            """
            AMPLitude:SOURce:ULIMit

            Arguments: 1
            """

        SOURce = SOURce()
        """
        AMPLitude:SOURce

        Arguments:
        """

    AMPLitude = AMPLitude()
    """
    AMPLitude

    Arguments:
    """

    class ATT0(SCPINodeN, SCPIQuery, SCPISet):
        """
        ATT0

        Arguments:
        """
        _cmd = "ATT0"
        args = []

    ATT0 = ATT0()
    """
    ATT0

    Arguments:
    """

    class ATT1(SCPINodeN, SCPIQuery, SCPISet):
        """
        ATT1

        Arguments:
        """
        _cmd = "ATT1"
        args = []

    ATT1 = ATT1()
    """
    ATT1

    Arguments:
    """

    class ATTen(SCPINode, SCPIQuery):
        """
        ATTen

        Arguments:
        """
        _cmd = "ATTen"
        args = []

        class UNLock(SCPINode, SCPISet):
            """
            ATTen:UNLock

            Arguments:
            """
            _cmd = "UNLock"
            args = []

        UNLock = UNLock()
        """
        ATTen:UNLock

        Arguments:
        """

    ATTen = ATTen()
    """
    ATTen

    Arguments:
    """

    class ATtenuator(SCPINode, SCPIQuery):
        """
        ATtenuator

        Arguments:
        """
        _cmd = "ATtenuator"
        args = []

        class Cont(SCPINode, SCPIQuery):
            """
            ATtenuator:Cont

            Arguments:
            """
            _cmd = "Cont"
            args = []

        Cont = Cont()
        """
        ATtenuator:Cont

        Arguments:
        """

        class Fixed(SCPINode, SCPISet):
            """
            ATtenuator:Fixed

            Arguments:
            """
            _cmd = "Fixed"
            args = []

        Fixed = Fixed()
        """
        ATtenuator:Fixed

        Arguments:
        """

        class Normal(SCPINode, SCPISet):
            """
            ATtenuator:Normal

            Arguments:
            """
            _cmd = "Normal"
            args = []

        Normal = Normal()
        """
        ATtenuator:Normal

        Arguments:
        """

    ATtenuator = ATtenuator()
    """
    ATtenuator

    Arguments:
    """

    class BLANk(SCPINode, SCPIQuery, SCPISet):
        """
        BLANk

        Arguments: 1
        """
        _cmd = "BLANk"
        args = ["1"]

    BLANk = BLANk()
    """
    BLANk

    Arguments: 1
    """

    class Blank(SCPINode, SCPIQuery):
        """
        Blank

        Arguments:
        """
        _cmd = "Blank"
        args = []

        class Inverted(SCPINode, SCPISet):
            """
            Blank:Inverted

            Arguments:
            """
            _cmd = "Inverted"
            args = []

        Inverted = Inverted()
        """
        Blank:Inverted

        Arguments:
        """

        class Normal(SCPINode, SCPISet):
            """
            Blank:Normal

            Arguments:
            """
            _cmd = "Normal"
            args = []

        Normal = Normal()
        """
        Blank:Normal

        Arguments:
        """

    Blank = Blank()
    """
    Blank

    Arguments:
    """

    class CALibration(SCPINode, SCPISet):
        """
        CALibration

        Arguments:
        """
        _cmd = "CALibration"
        args = []

        class AMPLitude(SCPINode, SCPISet):
            """
            CALibration:AMPLitude

            Arguments:
            """
            _cmd = "AMPLitude"
            args = []

            class STATe(SCPINode, SCPIBool):
                """
                CALibration:AMPLitude:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            CALibration:AMPLitude:STATe

            Arguments: 1, ON, OFF
            """

        AMPLitude = AMPLitude()
        """
        CALibration:AMPLitude

        Arguments:
        """

        class ATTenuator(SCPINode):
            """
            CALibration:ATTenuator

            Arguments:
            """
            _cmd = "ATTenuator"
            args = []

            class STATe(SCPINode, SCPIBool):
                """
                CALibration:ATTenuator:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            CALibration:ATTenuator:STATe

            Arguments: 1, ON, OFF
            """

        ATTenuator = ATTenuator()
        """
        CALibration:ATTenuator

        Arguments:
        """

        class FM(SCPINode):
            """
            CALibration:FM

            Arguments:
            """
            _cmd = "FM"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:FM:MEASure

                Arguments:
                """
                _cmd = "MEASure"
                args = []

            MEASure = MEASure()
            """
            CALibration:FM:MEASure

            Arguments:
            """

            class OFFSet(SCPINode, SCPIQuery):
                """
                CALibration:FM:OFFSet

                Arguments:
                """
                _cmd = "OFFSet"
                args = []

            OFFSet = OFFSet()
            """
            CALibration:FM:OFFSet

            Arguments:
            """

        FM = FM()
        """
        CALibration:FM

        Arguments:
        """

        class FMOFfset(SCPINode):
            """
            CALibration:FMOFfset

            Arguments:
            """
            _cmd = "FMOFfset"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                `CALibration:FMOFfset:MEASure
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/11b75bf573884132.htm#ID_b719b8434e4cb5ae0a00206a008f2019-9245ed064e4cb5ae0a00206a0024546d-en-US>`_

                Arguments:
                """
                _cmd = "MEASure"
                args = []

            MEASure = MEASure()
            """
            `CALibration:FMOFfset:MEASure
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/11b75bf573884132.htm#ID_b719b8434e4cb5ae0a00206a008f2019-9245ed064e4cb5ae0a00206a0024546d-en-US>`_

            Arguments:
            """

        FMOFfset = FMOFfset()
        """
        CALibration:FMOFfset

        Arguments:
        """

        class HARMfilter(SCPINode):
            """
            CALibration:HARMfilter

            Arguments:
            """
            _cmd = "HARMfilter"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:HARMfilter:MEASure

                Arguments:
                """
                _cmd = "MEASure"
                args = []

            MEASure = MEASure()
            """
            CALibration:HARMfilter:MEASure

            Arguments:
            """

        HARMfilter = HARMfilter()
        """
        CALibration:HARMfilter

        Arguments:
        """

        class IFFilter(SCPINode):
            """
            CALibration:IFFilter

            Arguments:
            """
            _cmd = "IFFilter"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:IFFilter:MEASure

                Arguments:
                """
                _cmd = "MEASure"
                args = []

            MEASure = MEASure()
            """
            CALibration:IFFilter:MEASure

            Arguments:
            """

        IFFilter = IFFilter()
        """
        CALibration:IFFilter

        Arguments:
        """

        class IQ(SCPINode):
            """
            CALibration:IQ

            Arguments:
            """
            _cmd = "IQ"
            args = []

            class DEFault(SCPINode, SCPISet):
                """
                CALibration:IQ:DEFault

                Arguments:
                """
                _cmd = "DEFault"
                args = []

            DEFault = DEFault()
            """
            CALibration:IQ:DEFault

            Arguments:
            """

            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                CALibration:IQ:STARt

                Arguments: 1
                """
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()
            """
            CALibration:IQ:STARt

            Arguments: 1
            """

        IQ = IQ()
        """
        CALibration:IQ

        Arguments:
        """

        class LEVel(SCPINode, SCPISet):
            """
            CALibration:LEVel

            Arguments:
            """
            _cmd = "LEVel"
            args = []

            class FRANge(SCPINode, SCPIQuery, SCPISet):
                """
                CALibration:LEVel:FRANge

                Arguments: MIXer, NORMal
                """
                _cmd = "FRANge"
                args = ["MIXer", "NORMal"]

            FRANge = FRANge()
            """
            CALibration:LEVel:FRANge

            Arguments: MIXer, NORMal
            """

            class PMODulator(SCPINode, SCPIBool):
                """
                CALibration:LEVel:PMODulator

                Arguments: 1, ON, OFF
                """
                _cmd = "PMODulator"
                args = ["1", "ON", "OFF"]

            PMODulator = PMODulator()
            """
            CALibration:LEVel:PMODulator

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                CALibration:LEVel:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            CALibration:LEVel:STATe

            Arguments: 1, ON, OFF
            """

        LEVel = LEVel()
        """
        CALibration:LEVel

        Arguments:
        """

        class LFGenlevel(SCPINode):
            """
            CALibration:LFGenlevel

            Arguments:
            """
            _cmd = "LFGenlevel"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:LFGenlevel:MEASure

                Arguments:
                """
                _cmd = "MEASure"
                args = []

            MEASure = MEASure()
            """
            CALibration:LFGenlevel:MEASure

            Arguments:
            """

        LFGenlevel = LFGenlevel()
        """
        CALibration:LFGenlevel

        Arguments:
        """

        class LFReset(SCPINode):
            """
            CALibration:LFReset

            Arguments:
            """
            _cmd = "LFReset"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:LFReset:MEASure

                Arguments:
                """
                _cmd = "MEASure"
                args = []

            MEASure = MEASure()
            """
            CALibration:LFReset:MEASure

            Arguments:
            """

        LFReset = LFReset()
        """
        CALibration:LFReset

        Arguments:
        """

        class MAINloop(SCPINode):
            """
            CALibration:MAINloop

            Arguments:
            """
            _cmd = "MAINloop"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:MAINloop:MEASure

                Arguments:
                """
                _cmd = "MEASure"
                args = []

            MEASure = MEASure()
            """
            CALibration:MAINloop:MEASure

            Arguments:
            """

        MAINloop = MAINloop()
        """
        CALibration:MAINloop

        Arguments:
        """

        class MULTfilter(SCPINode):
            """
            CALibration:MULTfilter

            Arguments:
            """
            _cmd = "MULTfilter"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:MULTfilter:MEASure

                Arguments:
                """
                _cmd = "MEASure"
                args = []

            MEASure = MEASure()
            """
            CALibration:MULTfilter:MEASure

            Arguments:
            """

        MULTfilter = MULTfilter()
        """
        CALibration:MULTfilter

        Arguments:
        """

        class PULSe(SCPINode):
            """
            CALibration:PULSe

            Arguments:
            """
            _cmd = "PULSe"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:PULSe:MEASure

                Arguments:
                """
                _cmd = "MEASure"
                args = []

            MEASure = MEASure()
            """
            CALibration:PULSe:MEASure

            Arguments:
            """

        PULSe = PULSe()
        """
        CALibration:PULSe

        Arguments:
        """

        class QPSK(SCPINode):
            """
            CALibration:QPSK

            Arguments:
            """
            _cmd = "QPSK"
            args = []

            class STORe(SCPINode, SCPISet):
                """
                CALibration:QPSK:STORe

                Arguments:
                """
                _cmd = "STORe"
                args = []

            STORe = STORe()
            """
            CALibration:QPSK:STORe

            Arguments:
            """

        QPSK = QPSK()
        """
        CALibration:QPSK

        Arguments:
        """

        class ROSCillator(SCPINode):
            """
            CALibration:ROSCillator

            Arguments:
            """
            _cmd = "ROSCillator"
            args = []

            class STORe(SCPINode, SCPISet):
                """
                CALibration:ROSCillator:STORe

                Arguments:
                """
                _cmd = "STORe"
                args = []

            STORe = STORe()
            """
            CALibration:ROSCillator:STORe

            Arguments:
            """

        ROSCillator = ROSCillator()
        """
        CALibration:ROSCillator

        Arguments:
        """

        class VMODulation(SCPINode):
            """
            CALibration:VMODulation

            Arguments:
            """
            _cmd = "VMODulation"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:VMODulation:MEASure

                Arguments: ONCE
                """
                _cmd = "MEASure"
                args = ["ONCE"]

            MEASure = MEASure()
            """
            CALibration:VMODulation:MEASure

            Arguments: ONCE
            """

        VMODulation = VMODulation()
        """
        CALibration:VMODulation

        Arguments:
        """

        class VSUMmation(SCPINode):
            """
            CALibration:VSUMmation

            Arguments:
            """
            _cmd = "VSUMmation"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:VSUMmation:MEASure

                Arguments:
                """
                _cmd = "MEASure"
                args = []

            MEASure = MEASure()
            """
            CALibration:VSUMmation:MEASure

            Arguments:
            """

            class OFFSet(SCPINode, SCPIQuery):
                """
                CALibration:VSUMmation:OFFSet

                Arguments:
                """
                _cmd = "OFFSet"
                args = []

            OFFSet = OFFSet()
            """
            CALibration:VSUMmation:OFFSet

            Arguments:
            """

        VSUMmation = VSUMmation()
        """
        CALibration:VSUMmation

        Arguments:
        """

        class VSYNthesis(SCPINode):
            """
            CALibration:VSYNthesis

            Arguments:
            """
            _cmd = "VSYNthesis"
            args = []

            class MEASure(SCPINode, SCPIQuery):
                """
                CALibration:VSYNthesis:MEASure

                Arguments:
                """
                _cmd = "MEASure"
                args = []

            MEASure = MEASure()
            """
            CALibration:VSYNthesis:MEASure

            Arguments:
            """

        VSYNthesis = VSYNthesis()
        """
        CALibration:VSYNthesis

        Arguments:
        """

    CALibration = CALibration()
    """
    CALibration

    Arguments:
    """

    class CAlibration(SCPINode, SCPISet):
        """
        CAlibration

        Arguments:
        """
        _cmd = "CAlibration"
        args = []

    CAlibration = CAlibration()
    """
    CAlibration

    Arguments:
    """

    class CONTrast(SCPINode, SCPIQuery, SCPISet):
        """
        CONTrast

        Arguments: 1
        """
        _cmd = "CONTrast"
        args = ["1"]

    CONTrast = CONTrast()
    """
    CONTrast

    Arguments: 1
    """

    class CONTrol(SCPINode, SCPISet):
        """
        CONTrol

        Arguments:
        """
        _cmd = "CONTrol"
        args = []

        class BLANking(SCPINode, SCPISet):
            """
            CONTrol:BLANking

            Arguments:
            """
            _cmd = "BLANking"
            args = []

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:BLANking:POLarity

                Arguments: INVerted, NORMal
                """
                _cmd = "POLarity"
                args = ["INVerted", "NORMal"]

            POLarity = POLarity()
            """
            CONTrol:BLANking:POLarity

            Arguments: INVerted, NORMal
            """

        BLANking = BLANking()
        """
        CONTrol:BLANking

        Arguments:
        """

        class PENLift(SCPINode, SCPISet):
            """
            CONTrol:PENLift

            Arguments:
            """
            _cmd = "PENLift"
            args = []

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:PENLift:POLarity

                Arguments: INVerted, NORMal
                """
                _cmd = "POLarity"
                args = ["INVerted", "NORMal"]

            POLarity = POLarity()
            """
            CONTrol:PENLift:POLarity

            Arguments: INVerted, NORMal
            """

        PENLift = PENLift()
        """
        CONTrol:PENLift

        Arguments:
        """

        class RAMP(SCPINode):
            """
            CONTrol:RAMP

            Arguments:
            """
            _cmd = "RAMP"
            args = []

            class STATe(SCPINode, SCPIBool):
                """
                CONTrol:RAMP:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            CONTrol:RAMP:STATe

            Arguments: 1, ON, OFF
            """

        RAMP = RAMP()
        """
        CONTrol:RAMP

        Arguments:
        """

    CONTrol = CONTrol()
    """
    CONTrol

    Arguments:
    """

    class DCFMnl(SCPINode, SCPISet):
        """
        DCFMnl

        Arguments:
        """
        _cmd = "DCFMnl"
        args = []

    DCFMnl = DCFMnl()
    """
    DCFMnl

    Arguments:
    """

    class DEVTrg(SCPINode, SCPISet):
        """
        DEVTrg

        Arguments: FLSWp, SEQT, SSSWp, VOID
        """
        _cmd = "DEVTrg"
        args = ["FLSWp", "SEQT", "SSSWp", "VOID"]

    DEVTrg = DEVTrg()
    """
    DEVTrg

    Arguments: FLSWp, SEQT, SSSWp, VOID
    """

    class DEcrement(SCPINode, SCPISet):
        """
        DEcrement

        Arguments:
        """
        _cmd = "DEcrement"
        args = []

        class PHAse(SCPINode, SCPISet):
            """
            DEcrement:PHAse

            Arguments:
            """
            _cmd = "PHAse"
            args = []

        PHAse = PHAse()
        """
        DEcrement:PHAse

        Arguments:
        """

        class Swp(SCPINode, SCPISet):
            """
            DEcrement:Swp

            Arguments:
            """
            _cmd = "Swp"
            args = []

        Swp = Swp()
        """
        DEcrement:Swp

        Arguments:
        """

    DEcrement = DEcrement()
    """
    DEcrement

    Arguments:
    """

    class DIAGnostic(SCPINode, SCPISet):
        """
        DIAGnostic

        Arguments:
        """
        _cmd = "DIAGnostic"
        args = []

        class CPU(SCPINode):
            """
            DIAGnostic:CPU

            Arguments:
            """
            _cmd = "CPU"
            args = []

            class INFormation(SCPINode, SCPISet):
                """
                DIAGnostic:CPU:INFormation

                Arguments:
                """
                _cmd = "INFormation"
                args = []

                class BOARds(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:CPU:INFormation:BOARds

                    Arguments:
                    """
                    _cmd = "BOARds"
                    args = []

                BOARds = BOARds()
                """
                DIAGnostic:CPU:INFormation:BOARds

                Arguments:
                """

                class CCOunt(SCPINode, SCPISet):
                    """
                    DIAGnostic:CPU:INFormation:CCOunt

                    Arguments:
                    """
                    _cmd = "CCOunt"
                    args = []

                    class ATTenuator(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:CCOunt:ATTenuator

                        Arguments:
                        """
                        _cmd = "ATTenuator"
                        args = []

                    ATTenuator = ATTenuator()
                    """
                    DIAGnostic:CPU:INFormation:CCOunt:ATTenuator

                    Arguments:
                    """

                    class PROTection(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:CCOunt:PROTection

                        Arguments:
                        """
                        _cmd = "PROTection"
                        args = []

                    PROTection = PROTection()
                    """
                    DIAGnostic:CPU:INFormation:CCOunt:PROTection

                    Arguments:
                    """

                CCOunt = CCOunt()
                """
                DIAGnostic:CPU:INFormation:CCOunt

                Arguments:
                """

                class DISPlay(SCPINode, SCPISet):
                    """
                    DIAGnostic:CPU:INFormation:DISPlay

                    Arguments:
                    """
                    _cmd = "DISPlay"
                    args = []

                    class OTIMe(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:DISPlay:OTIMe

                        Arguments:
                        """
                        _cmd = "OTIMe"
                        args = []

                    OTIMe = OTIMe()
                    """
                    DIAGnostic:CPU:INFormation:DISPlay:OTIMe

                    Arguments:
                    """

                DISPlay = DISPlay()
                """
                DIAGnostic:CPU:INFormation:DISPlay

                Arguments:
                """

                class LICense(SCPINode, SCPISet):
                    """
                    DIAGnostic:CPU:INFormation:LICense

                    Arguments:
                    """
                    _cmd = "LICense"
                    args = []

                    class AUXiliary(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:LICense:AUXiliary

                        Arguments:
                        """
                        _cmd = "AUXiliary"
                        args = []

                    AUXiliary = AUXiliary()
                    """
                    DIAGnostic:CPU:INFormation:LICense:AUXiliary

                    Arguments:
                    """

                    class WAVeform(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:LICense:WAVeform

                        Arguments:
                        """
                        _cmd = "WAVeform"
                        args = []

                    WAVeform = WAVeform()
                    """
                    DIAGnostic:CPU:INFormation:LICense:WAVeform

                    Arguments:
                    """

                LICense = LICense()
                """
                DIAGnostic:CPU:INFormation:LICense

                Arguments:
                """

                class OPTions(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:CPU:INFormation:OPTions

                    Arguments:
                    """
                    _cmd = "OPTions"
                    args = []

                    class DETail(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:OPTions:DETail

                        Arguments:
                        """
                        _cmd = "DETail"
                        args = []

                    DETail = DETail()
                    """
                    DIAGnostic:CPU:INFormation:OPTions:DETail

                    Arguments:
                    """

                OPTions = OPTions()
                """
                DIAGnostic:CPU:INFormation:OPTions

                Arguments:
                """

                class OTIMe(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:CPU:INFormation:OTIMe

                    Arguments:
                    """
                    _cmd = "OTIMe"
                    args = []

                OTIMe = OTIMe()
                """
                DIAGnostic:CPU:INFormation:OTIMe

                Arguments:
                """

                class REVision(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:CPU:INFormation:REVision

                    Arguments:
                    """
                    _cmd = "REVision"
                    args = []

                REVision = REVision()
                """
                DIAGnostic:CPU:INFormation:REVision

                Arguments:
                """

                class SDATe(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:CPU:INFormation:SDATe

                    Arguments:
                    """
                    _cmd = "SDATe"
                    args = []

                SDATe = SDATe()
                """
                DIAGnostic:CPU:INFormation:SDATe

                Arguments:
                """

                class WLICence(SCPINode):
                    """
                    DIAGnostic:CPU:INFormation:WLICence

                    Arguments:
                    """
                    _cmd = "WLICence"
                    args = []

                    class VALue(SCPINode, SCPIQuery):
                        """
                        DIAGnostic:CPU:INFormation:WLICence:VALue

                        Arguments: 1
                        """
                        _cmd = "VALue"
                        args = ["1"]

                    VALue = VALue()
                    """
                    DIAGnostic:CPU:INFormation:WLICence:VALue

                    Arguments: 1
                    """

                WLICence = WLICence()
                """
                DIAGnostic:CPU:INFormation:WLICence

                Arguments:
                """

            INFormation = INFormation()
            """
            DIAGnostic:CPU:INFormation

            Arguments:
            """

        CPU = CPU()
        """
        DIAGnostic:CPU

        Arguments:
        """

        class INFO(SCPINode):
            """
            DIAGnostic:INFO

            Arguments:
            """
            _cmd = "INFO"
            args = []

            class CCOunt(SCPINode):
                """
                DIAGnostic:INFO:CCOunt

                Arguments:
                """
                _cmd = "CCOunt"
                args = []

                class ATTenuator(SCPINodeN, SCPIQuery):
                    """
                    DIAGnostic:INFO:CCOunt:ATTenuator

                    Arguments:
                    """
                    _cmd = "ATTenuator"
                    args = []

                ATTenuator = ATTenuator()
                """
                DIAGnostic:INFO:CCOunt:ATTenuator

                Arguments:
                """

                class POWer(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:INFO:CCOunt:POWer

                    Arguments:
                    """
                    _cmd = "POWer"
                    args = []

                POWer = POWer()
                """
                DIAGnostic:INFO:CCOunt:POWer

                Arguments:
                """

            CCOunt = CCOunt()
            """
            DIAGnostic:INFO:CCOunt

            Arguments:
            """

            class MODules(SCPINode, SCPIQuery):
                """
                DIAGnostic:INFO:MODules

                Arguments:
                """
                _cmd = "MODules"
                args = []

            MODules = MODules()
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
                _cmd = "OTIMe"
                args = []

            OTIMe = OTIMe()
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
                _cmd = "SDATe"
                args = []

            SDATe = SDATe()
            """
            DIAGnostic:INFO:SDATe

            Arguments:
            """

            class SERialno(SCPINode, SCPIQuery):
                """
                DIAGnostic:INFO:SERialno

                Arguments:
                """
                _cmd = "SERialno"
                args = []

            SERialno = SERialno()
            """
            DIAGnostic:INFO:SERialno

            Arguments:
            """

            class SVERsion(SCPINode, SCPIQuery):
                """
                DIAGnostic:INFO:SVERsion

                Arguments:
                """
                _cmd = "SVERsion"
                args = []

            SVERsion = SVERsion()
            """
            DIAGnostic:INFO:SVERsion

            Arguments:
            """

        INFO = INFO()
        """
        DIAGnostic:INFO

        Arguments:
        """

        class MEASure(SCPINode):
            """
            DIAGnostic:MEASure

            Arguments:
            """
            _cmd = "MEASure"
            args = []

            class POINt(SCPINode, SCPIQuery):
                """
                DIAGnostic:MEASure:POINt

                Arguments: 1
                """
                _cmd = "POINt"
                args = ["1"]

            POINt = POINt()
            """
            DIAGnostic:MEASure:POINt

            Arguments: 1
            """

        MEASure = MEASure()
        """
        DIAGnostic:MEASure

        Arguments:
        """

        class XMEM(SCPINode):
            """
            DIAGnostic:XMEM

            Arguments:
            """
            _cmd = "XMEM"
            args = []

            class CHECksum(SCPINode):
                """
                DIAGnostic:XMEM:CHECksum

                Arguments:
                """
                _cmd = "CHECksum"
                args = []

                class ATTenuate(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:XMEM:CHECksum:ATTenuate

                    Arguments:
                    """
                    _cmd = "ATTenuate"
                    args = []

                ATTenuate = ATTenuate()
                """
                DIAGnostic:XMEM:CHECksum:ATTenuate

                Arguments:
                """

                class BURSt(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:XMEM:CHECksum:BURSt

                    Arguments:
                    """
                    _cmd = "BURSt"
                    args = []

                BURSt = BURSt()
                """
                DIAGnostic:XMEM:CHECksum:BURSt

                Arguments:
                """

                class CALCulate(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:XMEM:CHECksum:CALCulate

                    Arguments:
                    """
                    _cmd = "CALCulate"
                    args = []

                CALCulate = CALCulate()
                """
                DIAGnostic:XMEM:CHECksum:CALCulate

                Arguments:
                """

                class TOTal(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:XMEM:CHECksum:TOTal

                    Arguments:
                    """
                    _cmd = "TOTal"
                    args = []

                TOTal = TOTal()
                """
                DIAGnostic:XMEM:CHECksum:TOTal

                Arguments:
                """

            CHECksum = CHECksum()
            """
            DIAGnostic:XMEM:CHECksum

            Arguments:
            """

        XMEM = XMEM()
        """
        DIAGnostic:XMEM

        Arguments:
        """

    DIAGnostic = DIAGnostic()
    """
    DIAGnostic

    Arguments:
    """

    class DIGital(SCPINode, SCPIQuery):
        """
        DIGital

        Arguments:
        """
        _cmd = "DIGital"
        args = []

        class CONFig(SCPINode, SCPIQuery):
            """
            DIGital:CONFig

            Arguments:
            """
            _cmd = "CONFig"
            args = []

            class MIXer(SCPINode, SCPISet):
                """
                DIGital:CONFig:MIXer

                Arguments: EXTernal, INTernal
                """
                _cmd = "MIXer"
                args = ["EXTernal", "INTernal"]

            MIXer = MIXer()
            """
            DIGital:CONFig:MIXer

            Arguments: EXTernal, INTernal
            """

            class PULSe(SCPINode, SCPISet):
                """
                DIGital:CONFig:PULSe

                Arguments: DISabled, ENABled
                """
                _cmd = "PULSe"
                args = ["DISabled", "ENABled"]

            PULSe = PULSe()
            """
            DIGital:CONFig:PULSe

            Arguments: DISabled, ENABled
            """

        CONFig = CONFig()
        """
        DIGital:CONFig

        Arguments:
        """

        class ERRor(SCPINode, SCPIQuery):
            """
            DIGital:ERRor

            Arguments:
            """
            _cmd = "ERRor"
            args = []

            class DISable(SCPINode, SCPISet):
                """
                DIGital:ERRor:DISable

                Arguments:
                """
                _cmd = "DISable"
                args = []

            DISable = DISable()
            """
            DIGital:ERRor:DISable

            Arguments:
            """

            class ENABle(SCPINode, SCPISet):
                """
                DIGital:ERRor:ENABle

                Arguments:
                """
                _cmd = "ENABle"
                args = []

            ENABle = ENABle()
            """
            DIGital:ERRor:ENABle

            Arguments:
            """

        ERRor = ERRor()
        """
        DIGital:ERRor

        Arguments:
        """

        class EXT_par(SCPINode, SCPISet):
            """
            DIGital:EXT_par

            Arguments:
            """
            _cmd = "EXT_par"
            args = []

            class DATapol(SCPINode, SCPISet):
                """
                DIGital:EXT_par:DATapol

                Arguments: INVerse, NORMal
                """
                _cmd = "DATapol"
                args = ["INVerse", "NORMal"]

            DATapol = DATapol()
            """
            DIGital:EXT_par:DATapol

            Arguments: INVerse, NORMal
            """

            class SYMPol(SCPINode, SCPISet):
                """
                DIGital:EXT_par:SYMPol

                Arguments: NEG_edge, POS_edge
                """
                _cmd = "SYMPol"
                args = ["NEG_edge", "POS_edge"]

            SYMPol = SYMPol()
            """
            DIGital:EXT_par:SYMPol

            Arguments: NEG_edge, POS_edge
            """

            class SYMStat(SCPINode, SCPISet):
                """
                DIGital:EXT_par:SYMStat

                Arguments: EXTernal, INTernal
                """
                _cmd = "SYMStat"
                args = ["EXTernal", "INTernal"]

            SYMStat = SYMStat()
            """
            DIGital:EXT_par:SYMStat

            Arguments: EXTernal, INTernal
            """

        EXT_par = EXT_par()
        """
        DIGital:EXT_par

        Arguments:
        """

        class EXT_ser(SCPINode, SCPISet):
            """
            DIGital:EXT_ser

            Arguments:
            """
            _cmd = "EXT_ser"
            args = []

            class BITPol(SCPINode, SCPISet):
                """
                DIGital:EXT_ser:BITPol

                Arguments: NEG_edge, POS_edge
                """
                _cmd = "BITPol"
                args = ["NEG_edge", "POS_edge"]

            BITPol = BITPol()
            """
            DIGital:EXT_ser:BITPol

            Arguments: NEG_edge, POS_edge
            """

            class BITStat(SCPINode, SCPISet):
                """
                DIGital:EXT_ser:BITStat

                Arguments: EXTernal, INTernal
                """
                _cmd = "BITStat"
                args = ["EXTernal", "INTernal"]

            BITStat = BITStat()
            """
            DIGital:EXT_ser:BITStat

            Arguments: EXTernal, INTernal
            """

            class DATapol(SCPINode, SCPISet):
                """
                DIGital:EXT_ser:DATapol

                Arguments: INVerse, NORMal
                """
                _cmd = "DATapol"
                args = ["INVerse", "NORMal"]

            DATapol = DATapol()
            """
            DIGital:EXT_ser:DATapol

            Arguments: INVerse, NORMal
            """

            class SYMPol(SCPINode, SCPISet):
                """
                DIGital:EXT_ser:SYMPol

                Arguments: NEG_edge, POS_edge
                """
                _cmd = "SYMPol"
                args = ["NEG_edge", "POS_edge"]

            SYMPol = SYMPol()
            """
            DIGital:EXT_ser:SYMPol

            Arguments: NEG_edge, POS_edge
            """

            class SYMStat(SCPINode, SCPISet):
                """
                DIGital:EXT_ser:SYMStat

                Arguments: EXTernal, INTernal
                """
                _cmd = "SYMStat"
                args = ["EXTernal", "INTernal"]

            SYMStat = SYMStat()
            """
            DIGital:EXT_ser:SYMStat

            Arguments: EXTernal, INTernal
            """

        EXT_ser = EXT_ser()
        """
        DIGital:EXT_ser

        Arguments:
        """

        class FADing(SCPINode, SCPIQuery):
            """
            DIGital:FADing

            Arguments:
            """
            _cmd = "FADing"
            args = []

            class DIR_dopp(SCPINode, SCPISet):
                """
                DIGital:FADing:DIR_dopp

                Arguments: 1
                """
                _cmd = "DIR_dopp"
                args = ["1"]

            DIR_dopp = DIR_dopp()
            """
            DIGital:FADing:DIR_dopp

            Arguments: 1
            """

            class RATio(SCPINode, SCPISet):
                """
                DIGital:FADing:RATio

                Arguments: 1
                """
                _cmd = "RATio"
                args = ["1"]

            RATio = RATio()
            """
            DIGital:FADing:RATio

            Arguments: 1
            """

            class SPEed(SCPINode, SCPISet):
                """
                DIGital:FADing:SPEed

                Arguments: 1
                """
                _cmd = "SPEed"
                args = ["1"]

            SPEed = SPEed()
            """
            DIGital:FADing:SPEed

            Arguments: 1
            """

        FADing = FADing()
        """
        DIGital:FADing

        Arguments:
        """

        class GAIN(SCPINode):
            """
            DIGital:GAIN

            Arguments:
            """
            _cmd = "GAIN"
            args = []

            class VALue(SCPINode, SCPISet):
                """
                DIGital:GAIN:VALue

                Arguments: 1
                """
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()
            """
            DIGital:GAIN:VALue

            Arguments: 1
            """

        GAIN = GAIN()
        """
        DIGital:GAIN

        Arguments:
        """

        class INT_0s(SCPINode, SCPISet):
            """
            DIGital:INT_0s

            Arguments:
            """
            _cmd = "INT_0s"
            args = []

            class CLOCk(SCPINode, SCPISet):
                """
                DIGital:INT_0s:CLOCk

                Arguments: EXT_bit, EXT_sym, INT_sym
                """
                _cmd = "CLOCk"
                args = ["EXT_bit", "EXT_sym", "INT_sym"]

            CLOCk = CLOCk()
            """
            DIGital:INT_0s:CLOCk

            Arguments: EXT_bit, EXT_sym, INT_sym
            """

            class CLOCkpol(SCPINode, SCPISet):
                """
                DIGital:INT_0s:CLOCkpol

                Arguments: NEG_edge, POS_edge
                """
                _cmd = "CLOCkpol"
                args = ["NEG_edge", "POS_edge"]

            CLOCkpol = CLOCkpol()
            """
            DIGital:INT_0s:CLOCkpol

            Arguments: NEG_edge, POS_edge
            """

            class DATapol(SCPINode, SCPISet):
                """
                DIGital:INT_0s:DATapol

                Arguments: INVerse, NORMal
                """
                _cmd = "DATapol"
                args = ["INVerse", "NORMal"]

            DATapol = DATapol()
            """
            DIGital:INT_0s:DATapol

            Arguments: INVerse, NORMal
            """

        INT_0s = INT_0s()
        """
        DIGital:INT_0s

        Arguments:
        """

        class INT_1s(SCPINode, SCPISet):
            """
            DIGital:INT_1s

            Arguments:
            """
            _cmd = "INT_1s"
            args = []

            class CLOCk(SCPINode, SCPISet):
                """
                DIGital:INT_1s:CLOCk

                Arguments: EXT_bit, EXT_sym, INT_sym
                """
                _cmd = "CLOCk"
                args = ["EXT_bit", "EXT_sym", "INT_sym"]

            CLOCk = CLOCk()
            """
            DIGital:INT_1s:CLOCk

            Arguments: EXT_bit, EXT_sym, INT_sym
            """

            class CLOCkpol(SCPINode, SCPISet):
                """
                DIGital:INT_1s:CLOCkpol

                Arguments: NEG_edge, POS_edge
                """
                _cmd = "CLOCkpol"
                args = ["NEG_edge", "POS_edge"]

            CLOCkpol = CLOCkpol()
            """
            DIGital:INT_1s:CLOCkpol

            Arguments: NEG_edge, POS_edge
            """

            class DATapol(SCPINode, SCPISet):
                """
                DIGital:INT_1s:DATapol

                Arguments: INVerse, NORMal
                """
                _cmd = "DATapol"
                args = ["INVerse", "NORMal"]

            DATapol = DATapol()
            """
            DIGital:INT_1s:DATapol

            Arguments: INVerse, NORMal
            """

        INT_1s = INT_1s()
        """
        DIGital:INT_1s

        Arguments:
        """

        class LEAK(SCPINode):
            """
            DIGital:LEAK

            Arguments:
            """
            _cmd = "LEAK"
            args = []

            class VALue(SCPINode, SCPISet):
                """
                DIGital:LEAK:VALue

                Arguments: 1
                """
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()
            """
            DIGital:LEAK:VALue

            Arguments: 1
            """

        LEAK = LEAK()
        """
        DIGital:LEAK

        Arguments:
        """

        class MODopt(SCPINode, SCPIQuery):
            """
            DIGital:MODopt

            Arguments:
            """
            _cmd = "MODopt"
            args = []

            class ENVelope(SCPINode, SCPISet):
                """
                DIGital:MODopt:ENVelope

                Arguments: DISabled, ENABled
                """
                _cmd = "ENVelope"
                args = ["DISabled", "ENABled"]

            ENVelope = ENVelope()
            """
            DIGital:MODopt:ENVelope

            Arguments: DISabled, ENABled
            """

            class MODPol(SCPINode, SCPISet):
                """
                DIGital:MODopt:MODPol

                Arguments: INVerse, NORMal
                """
                _cmd = "MODPol"
                args = ["INVerse", "NORMal"]

            MODPol = MODPol()
            """
            DIGital:MODopt:MODPol

            Arguments: INVerse, NORMal
            """

            class SBANd(SCPINode, SCPISet):
                """
                DIGital:MODopt:SBANd

                Arguments: AUTO, LOWer, UPPer
                """
                _cmd = "SBANd"
                args = ["AUTO", "LOWer", "UPPer"]

            SBANd = SBANd()
            """
            DIGital:MODopt:SBANd

            Arguments: AUTO, LOWer, UPPer
            """

        MODopt = MODopt()
        """
        DIGital:MODopt

        Arguments:
        """

        class PRBS(SCPINode):
            """
            DIGital:PRBS

            Arguments:
            """
            _cmd = "PRBS"
            args = []

            class CLOCk(SCPINode, SCPISet):
                """
                DIGital:PRBS:CLOCk

                Arguments: EXT_bit, EXT_sym, INT_sym
                """
                _cmd = "CLOCk"
                args = ["EXT_bit", "EXT_sym", "INT_sym"]

            CLOCk = CLOCk()
            """
            DIGital:PRBS:CLOCk

            Arguments: EXT_bit, EXT_sym, INT_sym
            """

            class CLOCkpol(SCPINode, SCPISet):
                """
                DIGital:PRBS:CLOCkpol

                Arguments: NEG_edge, POS_edge
                """
                _cmd = "CLOCkpol"
                args = ["NEG_edge", "POS_edge"]

            CLOCkpol = CLOCkpol()
            """
            DIGital:PRBS:CLOCkpol

            Arguments: NEG_edge, POS_edge
            """

            class DATapol(SCPINode, SCPISet):
                """
                DIGital:PRBS:DATapol

                Arguments: INVerse, NORMal
                """
                _cmd = "DATapol"
                args = ["INVerse", "NORMal"]

            DATapol = DATapol()
            """
            DIGital:PRBS:DATapol

            Arguments: INVerse, NORMal
            """

            class VALue(SCPINode, SCPISet):
                """
                DIGital:PRBS:VALue

                Arguments: 1
                """
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()
            """
            DIGital:PRBS:VALue

            Arguments: 1
            """

        PRBS = PRBS()
        """
        DIGital:PRBS

        Arguments:
        """

        class SKEW(SCPINode):
            """
            DIGital:SKEW

            Arguments:
            """
            _cmd = "SKEW"
            args = []

            class VALue(SCPINode, SCPISet):
                """
                DIGital:SKEW:VALue

                Arguments: 1
                """
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()
            """
            DIGital:SKEW:VALue

            Arguments: 1
            """

        SKEW = SKEW()
        """
        DIGital:SKEW

        Arguments:
        """

        class SYSTem(SCPINode, SCPIQuery):
            """
            DIGital:SYSTem

            Arguments:
            """
            _cmd = "SYSTem"
            args = []

            class ALPHa(SCPINode, SCPISet):
                """
                DIGital:SYSTem:ALPHa

                Arguments: 1
                """
                _cmd = "ALPHa"
                args = ["1"]

            ALPHa = ALPHa()
            """
            DIGital:SYSTem:ALPHa

            Arguments: 1
            """

            class FILTer(SCPINode, SCPISet):
                """
                DIGital:SYSTem:FILTer

                Arguments: GAUSs, R_Cos, R_R_cos
                """
                _cmd = "FILTer"
                args = ["GAUSs", "R_Cos", "R_R_cos"]

            FILTer = FILTer()
            """
            DIGital:SYSTem:FILTer

            Arguments: GAUSs, R_Cos, R_R_cos
            """

            class FORMat(SCPINode, SCPISet):
                """
                DIGital:SYSTem:FORMat

                Arguments: BPSK, D_BPsk, D_PSk8, D_QPsk, FSK2, FSK4, GMSK, O_BPsk, O_PSk8, O_QPsk, PSK8, QAM16, QAM256, QAM4, QAM64, QPSK, TOQPsk, T_Tones
                """
                _cmd = "FORMat"
                args = ["BPSK", "D_BPsk", "D_PSk8", "D_QPsk", "FSK2", "FSK4", "GMSK", "O_BPsk", "O_PSk8", "O_QPsk", "PSK8", "QAM16", "QAM256", "QAM4", "QAM64", "QPSK", "TOQPsk", "T_Tones"]

            FORMat = FORMat()
            """
            DIGital:SYSTem:FORMat

            Arguments: BPSK, D_BPsk, D_PSk8, D_QPsk, FSK2, FSK4, GMSK, O_BPsk, O_PSk8, O_QPsk, PSK8, QAM16, QAM256, QAM4, QAM64, QPSK, TOQPsk, T_Tones
            """

            class SELect(SCPINode, SCPISet):
                """
                DIGital:SYSTem:SELect

                Arguments: CDPD, CITY1200, CITY2400, CITY4800, CITY512, DSRR16, DSRR4, ERMes, GSM, INMar_m, MC9, MD100w, MD120w, MD160n, MD192w, MD24n, MD24w, MD36n, MD36w, MD48n, MD48w, MD80n, MD80w, MD96n, MD96w, MOBitex, NADC, PDC, POC1200, POC2400, POC4800, POC512, Q_APco25, TETRa, TFTS, USER1, USER2, USER3, USER4, USER5, VDR
                """
                _cmd = "SELect"
                args = ["CDPD", "CITY1200", "CITY2400", "CITY4800", "CITY512", "DSRR16", "DSRR4", "ERMes", "GSM", "INMar_m", "MC9", "MD100w", "MD120w", "MD160n", "MD192w", "MD24n", "MD24w", "MD36n", "MD36w", "MD48n", "MD48w", "MD80n", "MD80w", "MD96n", "MD96w", "MOBitex", "NADC", "PDC", "POC1200", "POC2400", "POC4800", "POC512", "Q_APco25", "TETRa", "TFTS", "USER1", "USER2", "USER3", "USER4", "USER5", "VDR"]

            SELect = SELect()
            """
            DIGital:SYSTem:SELect

            Arguments: CDPD, CITY1200, CITY2400, CITY4800, CITY512, DSRR16, DSRR4, ERMes, GSM, INMar_m, MC9, MD100w, MD120w, MD160n, MD192w, MD24n, MD24w, MD36n, MD36w, MD48n, MD48w, MD80n, MD80w, MD96n, MD96w, MOBitex, NADC, PDC, POC1200, POC2400, POC4800, POC512, Q_APco25, TETRa, TFTS, USER1, USER2, USER3, USER4, USER5, VDR
            """

            class SYM_rate(SCPINode, SCPISet):
                """
                DIGital:SYSTem:SYM_rate

                Arguments: 1
                """
                _cmd = "SYM_rate"
                args = ["1"]

            SYM_rate = SYM_rate()
            """
            DIGital:SYSTem:SYM_rate

            Arguments: 1
            """

            class THRee_db(SCPINode, SCPISet):
                """
                DIGital:SYSTem:THRee_db

                Arguments: 1
                """
                _cmd = "THRee_db"
                args = ["1"]

            THRee_db = THRee_db()
            """
            DIGital:SYSTem:THRee_db

            Arguments: 1
            """

        SYSTem = SYSTem()
        """
        DIGital:SYSTem

        Arguments:
        """

        class T_Tones(SCPINode, SCPISet):
            """
            DIGital:T_Tones

            Arguments:
            """
            _cmd = "T_Tones"
            args = []

            class ANGLe(SCPINode, SCPIQuery, SCPISet):
                """
                DIGital:T_Tones:ANGLe

                Arguments: 1
                """
                _cmd = "ANGLe"
                args = ["1"]

            ANGLe = ANGLe()
            """
            DIGital:T_Tones:ANGLe

            Arguments: 1
            """

            class I_AMp(SCPINode, SCPIQuery, SCPISet):
                """
                DIGital:T_Tones:I_AMp

                Arguments: 1
                """
                _cmd = "I_AMp"
                args = ["1"]

            I_AMp = I_AMp()
            """
            DIGital:T_Tones:I_AMp

            Arguments: 1
            """

            class Q_AMp(SCPINode, SCPIQuery, SCPISet):
                """
                DIGital:T_Tones:Q_AMp

                Arguments: 1
                """
                _cmd = "Q_AMp"
                args = ["1"]

            Q_AMp = Q_AMp()
            """
            DIGital:T_Tones:Q_AMp

            Arguments: 1
            """

        T_Tones = T_Tones()
        """
        DIGital:T_Tones

        Arguments:
        """

    DIGital = DIGital()
    """
    DIGital

    Arguments:
    """

    class DIRect(SCPINode, SCPIQuery, SCPISet):
        """
        DIRect

        Arguments: <block_data>
        """
        _cmd = "DIRect"
        args = ["<block_data>"]

    DIRect = DIRect()
    """
    DIRect

    Arguments: <block_data>
    """

    class DISPlay(SCPINode, SCPISet):
        """
        DISPlay

        Arguments:
        """
        _cmd = "DISPlay"
        args = []

        class ANNotation(SCPINode, SCPISet):
            """
            DISPlay:ANNotation

            Arguments:
            """
            _cmd = "ANNotation"
            args = []

            class AMPLitude(SCPINode, SCPIBool):
                """
                `DISPlay:ANNotation:AMPLitude
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7164bc3c1b68452b.htm#ID_49b6f4592f69259f0a00206a0029f4d5-67bb427e2f691da00a00206a00636f5b-en-US>`_

                Arguments: 1, ON, OFF
                """
                _cmd = "AMPLitude"
                args = ["1", "ON", "OFF"]

                class STATe(SCPINode, SCPIBool):
                    """
                    DISPlay:ANNotation:AMPLitude:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                DISPlay:ANNotation:AMPLitude:STATe

                Arguments: 1, ON, OFF
                """

            AMPLitude = AMPLitude()
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
                _cmd = "CLOCk"
                args = []

                class DATE(SCPINode):
                    """
                    DISPlay:ANNotation:CLOCk:DATE

                    Arguments:
                    """
                    _cmd = "DATE"
                    args = []

                    class FORMat(SCPINode, SCPIQuery, SCPISet):
                        """
                        DISPlay:ANNotation:CLOCk:DATE:FORMat

                        Arguments: DMY, MDY
                        """
                        _cmd = "FORMat"
                        args = ["DMY", "MDY"]

                    FORMat = FORMat()
                    """
                    DISPlay:ANNotation:CLOCk:DATE:FORMat

                    Arguments: DMY, MDY
                    """

                DATE = DATE()
                """
                DISPlay:ANNotation:CLOCk:DATE

                Arguments:
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    DISPlay:ANNotation:CLOCk:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                DISPlay:ANNotation:CLOCk:STATe

                Arguments: 1, ON, OFF
                """

            CLOCk = CLOCk()
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
                _cmd = "FREQuency"
                args = ["1", "ON", "OFF"]

                class STATe(SCPINode, SCPIBool):
                    """
                    DISPlay:ANNotation:FREQuency:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                DISPlay:ANNotation:FREQuency:STATe

                Arguments: 1, ON, OFF
                """

            FREQuency = FREQuency()
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
                _cmd = "LFSource"
                args = ["1", "ON", "OFF"]

            LFSource = LFSource()
            """
            DISPlay:ANNotation:LFSource

            Arguments: 1, ON, OFF
            """

            class MODulation(SCPINode, SCPIBool):
                """
                DISPlay:ANNotation:MODulation

                Arguments: 1, ON, OFF
                """
                _cmd = "MODulation"
                args = ["1", "ON", "OFF"]

            MODulation = MODulation()
            """
            DISPlay:ANNotation:MODulation

            Arguments: 1, ON, OFF
            """

        ANNotation = ANNotation()
        """
        DISPlay:ANNotation

        Arguments:
        """

        class BRIGhtness(SCPINode, SCPIQuery, SCPISet):
            """
            DISPlay:BRIGhtness

            Arguments: 1
            """
            _cmd = "BRIGhtness"
            args = ["1"]

        BRIGhtness = BRIGhtness()
        """
        DISPlay:BRIGhtness

        Arguments: 1
        """

        class CAPTure(SCPINode, SCPISet):
            """
            DISPlay:CAPTure

            Arguments:
            """
            _cmd = "CAPTure"
            args = []

        CAPTure = CAPTure()
        """
        DISPlay:CAPTure

        Arguments:
        """

        class CONTrast(SCPINode, SCPIQuery, SCPISet):
            """
            DISPlay:CONTrast

            Arguments: 1
            """
            _cmd = "CONTrast"
            args = ["1"]

        CONTrast = CONTrast()
        """
        DISPlay:CONTrast

        Arguments: 1
        """

        class INVerse(SCPINode, SCPIBool):
            """
            DISPlay:INVerse

            Arguments: 1, ON, OFF
            """
            _cmd = "INVerse"
            args = ["1", "ON", "OFF"]

        INVerse = INVerse()
        """
        DISPlay:INVerse

        Arguments: 1, ON, OFF
        """

        class RADix(SCPINode, SCPIQuery, SCPISet):
            """
            DISPlay:RADix

            Arguments: EURopean, US
            """
            _cmd = "RADix"
            args = ["EURopean", "US"]

        RADix = RADix()
        """
        DISPlay:RADix

        Arguments: EURopean, US
        """

        class REMote(SCPINode, SCPIBool):
            """
            DISPlay:REMote

            Arguments: 1, ON, OFF
            """
            _cmd = "REMote"
            args = ["1", "ON", "OFF"]

        REMote = REMote()
        """
        DISPlay:REMote

        Arguments: 1, ON, OFF
        """

        class STATe(SCPINode, SCPIBool):
            """
            DISPlay:STATe

            Arguments: 1, ON, OFF
            """
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()
        """
        DISPlay:STATe

        Arguments: 1, ON, OFF
        """

        class WINDow(SCPINode, SCPISet):
            """
            DISPlay:WINDow

            Arguments:
            """
            _cmd = "WINDow"
            args = []

            class STATe(SCPINode, SCPIBool):
                """
                DISPlay:WINDow:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            DISPlay:WINDow:STATe

            Arguments: 1, ON, OFF
            """

            class TEXT(SCPINode):
                """
                DISPlay:WINDow:TEXT

                Arguments:
                """
                _cmd = "TEXT"
                args = []

                class STATe(SCPINode, SCPIBool):
                    """
                    DISPlay:WINDow:TEXT:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                DISPlay:WINDow:TEXT:STATe

                Arguments: 1, ON, OFF
                """

            TEXT = TEXT()
            """
            DISPlay:WINDow:TEXT

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

    class DISplay(SCPINode, SCPISet):
        """
        DISplay

        Arguments:
        """
        _cmd = "DISplay"
        args = []

    DISplay = DISplay()
    """
    DISplay

    Arguments:
    """

    class ELAPsed(SCPINode, SCPIQuery):
        """
        ELAPsed

        Arguments:
        """
        _cmd = "ELAPsed"
        args = []

        class RESet(SCPINode, SCPISet):
            """
            ELAPsed:RESet

            Arguments:
            """
            _cmd = "RESet"
            args = []

        RESet = RESet()
        """
        ELAPsed:RESet

        Arguments:
        """

    ELAPsed = ELAPsed()
    """
    ELAPsed

    Arguments:
    """

    class ERASe(SCPINode, SCPISet):
        """
        ERASe

        Arguments:
        """
        _cmd = "ERASe"
        args = []

        class SWEep(SCPINode, SCPISet):
            """
            ERASe:SWEep

            Arguments:
            """
            _cmd = "SWEep"
            args = []

        SWEep = SWEep()
        """
        ERASe:SWEep

        Arguments:
        """

    ERASe = ERASe()
    """
    ERASe

    Arguments:
    """

    class ERRor(SCPINode, SCPIQuery):
        """
        ERRor

        Arguments:
        """
        _cmd = "ERRor"
        args = []

    ERRor = ERRor()
    """
    ERRor

    Arguments:
    """

    class ERrors(SCPINode, SCPIQuery):
        """
        ERrors

        Arguments:
        """
        _cmd = "ERrors"
        args = []

    ERrors = ERrors()
    """
    ERrors

    Arguments:
    """

    class EXTTrg(SCPINode, SCPISet):
        """
        EXTTrg

        Arguments: FLSWp, MEMDn, MEMup, SEQT, SSSWp, VOID
        """
        _cmd = "EXTTrg"
        args = ["FLSWp", "MEMDn", "MEMup", "SEQT", "SSSWp", "VOID"]

    EXTTrg = EXTTrg()
    """
    EXTTrg

    Arguments: FLSWp, MEMDn, MEMup, SEQT, SSSWp, VOID
    """

    class EXecution_mode(SCPINode, SCPIQuery, SCPISet):
        """
        EXecution_mode

        Arguments:
        """
        _cmd = "EXecution_mode"
        args = []

        class Normal(SCPINode, SCPISet):
            """
            EXecution_mode:Normal

            Arguments:
            """
            _cmd = "Normal"
            args = []

        Normal = Normal()
        """
        EXecution_mode:Normal

        Arguments:
        """

        class Triggered(SCPINode, SCPISet):
            """
            EXecution_mode:Triggered

            Arguments:
            """
            _cmd = "Triggered"
            args = []

        Triggered = Triggered()
        """
        EXecution_mode:Triggered

        Arguments:
        """

    EXecution_mode = EXecution_mode()
    """
    EXecution_mode

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
            `FORMat:BORDer
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/59b73d990b8d4acf.htm#ID_729c2ba54e7ed3070a00206a001affe3-8402e7834e7ed3070a00206a0024546d-en-US>`_

            Arguments: NORMal, SWAPped
            """
            _cmd = "BORDer"
            args = ["NORMal", "SWAPped"]

        BORDer = BORDer()
        """
        `FORMat:BORDer
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/59b73d990b8d4acf.htm#ID_729c2ba54e7ed3070a00206a001affe3-8402e7834e7ed3070a00206a0024546d-en-US>`_

        Arguments: NORMal, SWAPped
        """

    FORMat = FORMat()
    """
    FORMat

    Arguments:
    """

    class FREQuency(SCPINode):
        """
        FREQuency

        Arguments:
        """
        _cmd = "FREQuency"
        args = []

        class CENTer(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:CENTer

            Arguments: 1
            """
            _cmd = "CENTer"
            args = ["1"]

            class STEP(SCPINode):
                """
                FREQuency:CENTer:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    FREQuency:CENTer:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                FREQuency:CENTer:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            FREQuency:CENTer:STEP

            Arguments:
            """

        CENTer = CENTer()
        """
        FREQuency:CENTer

        Arguments: 1
        """

        class CW(SCPINode):
            """
            FREQuency:CW

            Arguments:
            """
            _cmd = "CW"
            args = []

            class STEP(SCPINode):
                """
                FREQuency:CW:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    FREQuency:CW:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                FREQuency:CW:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            FREQuency:CW:STEP

            Arguments:
            """

        CW = CW()
        """
        FREQuency:CW

        Arguments:
        """

        class INSTantaneous(SCPINode, SCPIQuery):
            """
            FREQuency:INSTantaneous

            Arguments:
            """
            _cmd = "INSTantaneous"
            args = []

        INSTantaneous = INSTantaneous()
        """
        FREQuency:INSTantaneous

        Arguments:
        """

        class MANual(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:MANual

            Arguments: 1
            """
            _cmd = "MANual"
            args = ["1"]

        MANual = MANual()
        """
        FREQuency:MANual

        Arguments: 1
        """

        class MULTiplier(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:MULTiplier

            Arguments: 1
            """
            _cmd = "MULTiplier"
            args = ["1"]

        MULTiplier = MULTiplier()
        """
        FREQuency:MULTiplier

        Arguments: 1
        """

        class OFFSet(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:OFFSet

            Arguments: 1
            """
            _cmd = "OFFSet"
            args = ["1"]

        OFFSet = OFFSet()
        """
        FREQuency:OFFSet

        Arguments: 1
        """

        class SPAN(SCPINode):
            """
            FREQuency:SPAN

            Arguments:
            """
            _cmd = "SPAN"
            args = []

            class STEP(SCPINode):
                """
                FREQuency:SPAN:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    FREQuency:SPAN:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                FREQuency:SPAN:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            FREQuency:SPAN:STEP

            Arguments:
            """

        SPAN = SPAN()
        """
        FREQuency:SPAN

        Arguments:
        """

        class STARt(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:STARt

            Arguments: 1
            """
            _cmd = "STARt"
            args = ["1"]

            class STEP(SCPINode):
                """
                FREQuency:STARt:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    FREQuency:STARt:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                FREQuency:STARt:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            FREQuency:STARt:STEP

            Arguments:
            """

        STARt = STARt()
        """
        FREQuency:STARt

        Arguments: 1
        """

        class STOP(SCPINode):
            """
            FREQuency:STOP

            Arguments:
            """
            _cmd = "STOP"
            args = []

            class STEP(SCPINode):
                """
                FREQuency:STOP:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    FREQuency:STOP:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                FREQuency:STOP:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            FREQuency:STOP:STEP

            Arguments:
            """

        STOP = STOP()
        """
        FREQuency:STOP

        Arguments:
        """

        class SYNThesis(SCPINode, SCPIQuery, SCPISet):
            """
            FREQuency:SYNThesis

            Arguments: 1
            """
            _cmd = "SYNThesis"
            args = ["1"]

        SYNThesis = SYNThesis()
        """
        FREQuency:SYNThesis

        Arguments: 1
        """

    FREQuency = FREQuency()
    """
    FREQuency

    Arguments:
    """

    class HEAder(SCPINode, SCPISet):
        """
        HEAder

        Arguments:
        """
        _cmd = "HEAder"
        args = []

    HEAder = HEAder()
    """
    HEAder

    Arguments:
    """

    class HET_band(SCPINode, SCPISet):
        """
        HET_band

        Arguments:
        """
        _cmd = "HET_band"
        args = []

        class High(SCPINode, SCPISet):
            """
            HET_band:High

            Arguments:
            """
            _cmd = "High"
            args = []

        High = High()
        """
        HET_band:High

        Arguments:
        """

        class Low(SCPINode, SCPISet):
            """
            HET_band:Low

            Arguments:
            """
            _cmd = "Low"
            args = []

        Low = Low()
        """
        HET_band:Low

        Arguments:
        """

    HET_band = HET_band()
    """
    HET_band

    Arguments:
    """

    class HOPSeq(SCPINode, SCPIQuery, SCPISet):
        """
        HOPSeq

        Arguments: <numeric_value>,<numeric_value>
        """
        _cmd = "HOPSeq"
        args = ["<numeric_value>,<numeric_value>"]

    HOPSeq = HOPSeq()
    """
    HOPSeq

    Arguments: <numeric_value>,<numeric_value>
    """

    class IMODe(SCPINode, SCPISet):
        """
        IMODe

        Arguments: NORMal, SWEeper
        """
        _cmd = "IMODe"
        args = ["NORMal", "SWEeper"]

    IMODe = IMODe()
    """
    IMODe

    Arguments: NORMal, SWEeper
    """

    class IMPedance(SCPINode, SCPIQuery, SCPISet):
        """
        IMPedance

        Arguments: Z50R, Z75R
        """
        _cmd = "IMPedance"
        args = ["Z50R", "Z75R"]

    IMPedance = IMPedance()
    """
    IMPedance

    Arguments: Z50R, Z75R
    """

    class INITialize(SCPINode):
        """
        INITialize

        Arguments:
        """
        _cmd = "INITialize"
        args = []

        class ABORt(SCPINode, SCPISet):
            """
            INITialize:ABORt

            Arguments:
            """
            _cmd = "ABORt"
            args = []

        ABORt = ABORt()
        """
        INITialize:ABORt

        Arguments:
        """

        class CONTinuous(SCPINode, SCPIBool):
            """
            INITialize:CONTinuous

            Arguments: 1, ON, OFF
            """
            _cmd = "CONTinuous"
            args = ["1", "ON", "OFF"]

        CONTinuous = CONTinuous()
        """
        INITialize:CONTinuous

        Arguments: 1, ON, OFF
        """

        class IMMediate(SCPINode, SCPISet):
            """
            INITialize:IMMediate

            Arguments:
            """
            _cmd = "IMMediate"
            args = []

        IMMediate = IMMediate()
        """
        INITialize:IMMediate

        Arguments:
        """

        class STATe(SCPINode, SCPIQuery, SCPISet):
            """
            INITialize:STATe

            Arguments: PAUSe, RUN
            """
            _cmd = "STATe"
            args = ["PAUSe", "RUN"]

        STATe = STATe()
        """
        INITialize:STATe

        Arguments: PAUSe, RUN
        """

    INITialize = INITialize()
    """
    INITialize

    Arguments:
    """

    class INITiate(SCPINode, SCPISet):
        """
        INITiate

        Arguments:
        """
        _cmd = "INITiate"
        args = []

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

    class INPut(SCPINode):
        """
        INPut

        Arguments:
        """
        _cmd = "INPut"
        args = []

        class IF(SCPINode):
            """
            INPut:IF

            Arguments:
            """
            _cmd = "IF"
            args = []

            class STATe(SCPINode, SCPIBool):
                """
                INPut:IF:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            INPut:IF:STATe

            Arguments: 1, ON, OFF
            """

        IF = IF()
        """
        INPut:IF

        Arguments:
        """

        class POLarity(SCPINode, SCPIQuery, SCPISet):
            """
            INPut:POLarity

            Arguments: INVerted, NORMal
            """
            _cmd = "POLarity"
            args = ["INVerted", "NORMal"]

        POLarity = POLarity()
        """
        INPut:POLarity

        Arguments: INVerted, NORMal
        """

    INPut = INPut()
    """
    INPut

    Arguments:
    """

    class Increment(SCPINode, SCPISet):
        """
        Increment

        Arguments:
        """
        _cmd = "Increment"
        args = []

        class PHAse(SCPINode, SCPISet):
            """
            Increment:PHAse

            Arguments:
            """
            _cmd = "PHAse"
            args = []

        PHAse = PHAse()
        """
        Increment:PHAse

        Arguments:
        """

        class Swp(SCPINode, SCPISet):
            """
            Increment:Swp

            Arguments:
            """
            _cmd = "Swp"
            args = []

        Swp = Swp()
        """
        Increment:Swp

        Arguments:
        """

    Increment = Increment()
    """
    Increment

    Arguments:
    """

    class KLOCk(SCPINode, SCPISet):
        """
        KLOCk

        Arguments:
        """
        _cmd = "KLOCk"
        args = []

    KLOCk = KLOCk()
    """
    KLOCk

    Arguments:
    """

    class KUNLock(SCPINode, SCPISet):
        """
        KUNLock

        Arguments:
        """
        _cmd = "KUNLock"
        args = []

    KUNLock = KUNLock()
    """
    KUNLock

    Arguments:
    """

    class LFSource(SCPINodeN):
        """
        LFSource

        Arguments:
        """
        _cmd = "LFSource"
        args = []

        class AM(SCPINode):
            """
            LFSource:AM

            Arguments:
            """
            _cmd = "AM"
            args = []

            class DEPTh(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:AM:DEPTh

                Arguments: 1
                """
                _cmd = "DEPTh"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:AM:DEPTh:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:AM:DEPTh:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    LFSource:AM:DEPTh:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                LFSource:AM:DEPTh:STEP

                Arguments:
                """

            DEPTh = DEPTh()
            """
            LFSource:AM:DEPTh

            Arguments: 1
            """

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:AM:FREQuency

                Arguments: 1
                """
                _cmd = "FREQuency"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:AM:FREQuency:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:AM:FREQuency:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    LFSource:AM:FREQuency:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                LFSource:AM:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()
            """
            LFSource:AM:FREQuency

            Arguments: 1
            """

            class PHASe(SCPINode):
                """
                LFSource:AM:PHASe

                Arguments:
                """
                _cmd = "PHASe"
                args = []

                class ADJust(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:AM:PHASe:ADJust

                    Arguments: 1
                    """
                    _cmd = "ADJust"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        LFSource:AM:PHASe:ADJust:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            LFSource:AM:PHASe:ADJust:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        LFSource:AM:PHASe:ADJust:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    LFSource:AM:PHASe:ADJust:STEP

                    Arguments:
                    """

                ADJust = ADJust()
                """
                LFSource:AM:PHASe:ADJust

                Arguments: 1
                """

            PHASe = PHASe()
            """
            LFSource:AM:PHASe

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                LFSource:AM:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            LFSource:AM:STATe

            Arguments: 1, ON, OFF
            """

            class WAVeform(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:AM:WAVeform

                Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
                """
                _cmd = "WAVeform"
                args = ["SAWTooth", "SINE", "SQUare", "TRIangle", "WGNoise"]

            WAVeform = WAVeform()
            """
            LFSource:AM:WAVeform

            Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
            """

        AM = AM()
        """
        LFSource:AM

        Arguments:
        """

        class AVIonics(SCPINode):
            """
            LFSource:AVIonics

            Arguments:
            """
            _cmd = "AVIonics"
            args = []

            class SETup(SCPINode):
                """
                LFSource:AVIonics:SETup

                Arguments:
                """
                _cmd = "SETup"
                args = []

                class GSLope(SCPINode, SCPISet):
                    """
                    LFSource:AVIonics:SETup:GSLope

                    Arguments:
                    """
                    _cmd = "GSLope"
                    args = []

                GSLope = GSLope()
                """
                LFSource:AVIonics:SETup:GSLope

                Arguments:
                """

                class IMBeacon(SCPINode, SCPISet):
                    """
                    LFSource:AVIonics:SETup:IMBeacon

                    Arguments:
                    """
                    _cmd = "IMBeacon"
                    args = []

                IMBeacon = IMBeacon()
                """
                LFSource:AVIonics:SETup:IMBeacon

                Arguments:
                """

                class LOCalizer(SCPINode, SCPISet):
                    """
                    LFSource:AVIonics:SETup:LOCalizer

                    Arguments:
                    """
                    _cmd = "LOCalizer"
                    args = []

                LOCalizer = LOCalizer()
                """
                LFSource:AVIonics:SETup:LOCalizer

                Arguments:
                """

                class MMBeacon(SCPINode, SCPISet):
                    """
                    LFSource:AVIonics:SETup:MMBeacon

                    Arguments:
                    """
                    _cmd = "MMBeacon"
                    args = []

                MMBeacon = MMBeacon()
                """
                LFSource:AVIonics:SETup:MMBeacon

                Arguments:
                """

                class OMBeacon(SCPINode, SCPISet):
                    """
                    LFSource:AVIonics:SETup:OMBeacon

                    Arguments:
                    """
                    _cmd = "OMBeacon"
                    args = []

                OMBeacon = OMBeacon()
                """
                LFSource:AVIonics:SETup:OMBeacon

                Arguments:
                """

            SETup = SETup()
            """
            LFSource:AVIonics:SETup

            Arguments:
            """

        AVIonics = AVIonics()
        """
        LFSource:AVIonics

        Arguments:
        """

        class FM(SCPINode):
            """
            LFSource:FM

            Arguments:
            """
            _cmd = "FM"
            args = []

            class DEViation(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:FM:DEViation

                Arguments: 1
                """
                _cmd = "DEViation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:FM:DEViation:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:FM:DEViation:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    LFSource:FM:DEViation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                LFSource:FM:DEViation:STEP

                Arguments:
                """

            DEViation = DEViation()
            """
            LFSource:FM:DEViation

            Arguments: 1
            """

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:FM:FREQuency

                Arguments: 1
                """
                _cmd = "FREQuency"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:FM:FREQuency:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:FM:FREQuency:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    LFSource:FM:FREQuency:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                LFSource:FM:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()
            """
            LFSource:FM:FREQuency

            Arguments: 1
            """

            class PHASe(SCPINode):
                """
                LFSource:FM:PHASe

                Arguments:
                """
                _cmd = "PHASe"
                args = []

                class ADJust(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:FM:PHASe:ADJust

                    Arguments: 1
                    """
                    _cmd = "ADJust"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        LFSource:FM:PHASe:ADJust:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            LFSource:FM:PHASe:ADJust:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        LFSource:FM:PHASe:ADJust:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    LFSource:FM:PHASe:ADJust:STEP

                    Arguments:
                    """

                ADJust = ADJust()
                """
                LFSource:FM:PHASe:ADJust

                Arguments: 1
                """

            PHASe = PHASe()
            """
            LFSource:FM:PHASe

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                LFSource:FM:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            LFSource:FM:STATe

            Arguments: 1, ON, OFF
            """

            class WAVeform(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:FM:WAVeform

                Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
                """
                _cmd = "WAVeform"
                args = ["SAWTooth", "SINE", "SQUare", "TRIangle", "WGNoise"]

            WAVeform = WAVeform()
            """
            LFSource:FM:WAVeform

            Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
            """

        FM = FM()
        """
        LFSource:FM

        Arguments:
        """

        class FREQuency(SCPINodeN, SCPIQuery, SCPISet):
            """
            LFSource:FREQuency

            Arguments: 1
            """
            _cmd = "FREQuency"
            args = ["1"]

            class STEP(SCPINode):
                """
                LFSource:FREQuency:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:FREQuency:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                LFSource:FREQuency:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            LFSource:FREQuency:STEP

            Arguments:
            """

        FREQuency = FREQuency()
        """
        LFSource:FREQuency

        Arguments: 1
        """

        class LEVel(SCPINodeN, SCPIQuery, SCPISet):
            """
            LFSource:LEVel

            Arguments: 1
            """
            _cmd = "LEVel"
            args = ["1"]

            class STEP(SCPINode):
                """
                LFSource:LEVel:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:LEVel:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                LFSource:LEVel:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            LFSource:LEVel:STEP

            Arguments:
            """

        LEVel = LEVel()
        """
        LFSource:LEVel

        Arguments: 1
        """

        class PHASe(SCPINodeN):
            """
            LFSource:PHASe

            Arguments:
            """
            _cmd = "PHASe"
            args = []

            class ADJust(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:PHASe:ADJust

                Arguments: 1
                """
                _cmd = "ADJust"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:PHASe:ADJust:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:PHASe:ADJust:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    LFSource:PHASe:ADJust:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                LFSource:PHASe:ADJust:STEP

                Arguments:
                """

            ADJust = ADJust()
            """
            LFSource:PHASe:ADJust

            Arguments: 1
            """

        PHASe = PHASe()
        """
        LFSource:PHASe

        Arguments:
        """

        class PM(SCPINode):
            """
            LFSource:PM

            Arguments:
            """
            _cmd = "PM"
            args = []

            class DEViation(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:PM:DEViation

                Arguments: 1
                """
                _cmd = "DEViation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:PM:DEViation:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:PM:DEViation:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    LFSource:PM:DEViation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                LFSource:PM:DEViation:STEP

                Arguments:
                """

            DEViation = DEViation()
            """
            LFSource:PM:DEViation

            Arguments: 1
            """

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:PM:FREQuency

                Arguments: 1
                """
                _cmd = "FREQuency"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:PM:FREQuency:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:PM:FREQuency:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    LFSource:PM:FREQuency:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                LFSource:PM:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()
            """
            LFSource:PM:FREQuency

            Arguments: 1
            """

            class PHASe(SCPINode):
                """
                LFSource:PM:PHASe

                Arguments:
                """
                _cmd = "PHASe"
                args = []

                class ADJust(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:PM:PHASe:ADJust

                    Arguments: 1
                    """
                    _cmd = "ADJust"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        LFSource:PM:PHASe:ADJust:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            LFSource:PM:PHASe:ADJust:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        LFSource:PM:PHASe:ADJust:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    LFSource:PM:PHASe:ADJust:STEP

                    Arguments:
                    """

                ADJust = ADJust()
                """
                LFSource:PM:PHASe:ADJust

                Arguments: 1
                """

            PHASe = PHASe()
            """
            LFSource:PM:PHASe

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                LFSource:PM:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            LFSource:PM:STATe

            Arguments: 1, ON, OFF
            """

            class WAVeform(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:PM:WAVeform

                Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
                """
                _cmd = "WAVeform"
                args = ["SAWTooth", "SINE", "SQUare", "TRIangle", "WGNoise"]

            WAVeform = WAVeform()
            """
            LFSource:PM:WAVeform

            Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
            """

        PM = PM()
        """
        LFSource:PM

        Arguments:
        """

        class PULSe(SCPINode):
            """
            LFSource:PULSe

            Arguments:
            """
            _cmd = "PULSe"
            args = []

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:PULSe:FREQuency

                Arguments: 1
                """
                _cmd = "FREQuency"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    LFSource:PULSe:FREQuency:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        LFSource:PULSe:FREQuency:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    LFSource:PULSe:FREQuency:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                LFSource:PULSe:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()
            """
            LFSource:PULSe:FREQuency

            Arguments: 1
            """

            class PHASe(SCPINode):
                """
                LFSource:PULSe:PHASe

                Arguments:
                """
                _cmd = "PHASe"
                args = []

                class ADJust(SCPINode, SCPIQuery, SCPISet):
                    """
                    LFSource:PULSe:PHASe:ADJust

                    Arguments: 1
                    """
                    _cmd = "ADJust"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        LFSource:PULSe:PHASe:ADJust:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            LFSource:PULSe:PHASe:ADJust:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        LFSource:PULSe:PHASe:ADJust:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    LFSource:PULSe:PHASe:ADJust:STEP

                    Arguments:
                    """

                ADJust = ADJust()
                """
                LFSource:PULSe:PHASe:ADJust

                Arguments: 1
                """

            PHASe = PHASe()
            """
            LFSource:PULSe:PHASe

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                LFSource:PULSe:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            LFSource:PULSe:STATe

            Arguments: 1, ON, OFF
            """

        PULSe = PULSe()
        """
        LFSource:PULSe

        Arguments:
        """

        class STATe(SCPINodeN, SCPIBool):
            """
            LFSource:STATe

            Arguments: 1, ON, OFF
            """
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()
        """
        LFSource:STATe

        Arguments: 1, ON, OFF
        """

        class TRIGger(SCPINode):
            """
            LFSource:TRIGger

            Arguments:
            """
            _cmd = "TRIGger"
            args = []

            class IMMediate(SCPINode, SCPISet):
                """
                LFSource:TRIGger:IMMediate

                Arguments:
                """
                _cmd = "IMMediate"
                args = []

            IMMediate = IMMediate()
            """
            LFSource:TRIGger:IMMediate

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                LFSource:TRIGger:SOURce

                Arguments: CONTinuous, EXTernal
                """
                _cmd = "SOURce"
                args = ["CONTinuous", "EXTernal"]

            SOURce = SOURce()
            """
            LFSource:TRIGger:SOURce

            Arguments: CONTinuous, EXTernal
            """

        TRIGger = TRIGger()
        """
        LFSource:TRIGger

        Arguments:
        """

        class WAVeform(SCPINodeN, SCPIQuery, SCPISet):
            """
            LFSource:WAVeform

            Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
            """
            _cmd = "WAVeform"
            args = ["SAWTooth", "SINE", "SQUare", "TRIangle", "WGNoise"]

        WAVeform = WAVeform()
        """
        LFSource:WAVeform

        Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
        """

    LFSource = LFSource()
    """
    LFSource

    Arguments:
    """

    class Level(SCPINode):
        """
        Level

        Arguments:
        """
        _cmd = "Level"
        args = []

        class AF(SCPINode):
            """
            Level:AF

            Arguments:
            """
            _cmd = "AF"
            args = []

            class Var_step(SCPINode, SCPIQuery, SCPISet):
                """
                Level:AF:Var_step

                Arguments: 1
                """
                _cmd = "Var_step"
                args = ["1"]

            Var_step = Var_step()
            """
            Level:AF:Var_step

            Arguments: 1
            """

        AF = AF()
        """
        Level:AF

        Arguments:
        """

        class RF(SCPINode):
            """
            Level:RF

            Arguments:
            """
            _cmd = "RF"
            args = []

            class CONtrol(SCPINode, SCPISet):
                """
                Level:RF:CONtrol

                Arguments:
                """
                _cmd = "CONtrol"
                args = []

                class Calibration(SCPINode, SCPISet):
                    """
                    Level:RF:CONtrol:Calibration

                    Arguments:
                    """
                    _cmd = "Calibration"
                    args = []

                Calibration = Calibration()
                """
                Level:RF:CONtrol:Calibration

                Arguments:
                """

                class Lookup(SCPINode, SCPISet):
                    """
                    Level:RF:CONtrol:Lookup

                    Arguments:
                    """
                    _cmd = "Lookup"
                    args = []

                Lookup = Lookup()
                """
                Level:RF:CONtrol:Lookup

                Arguments:
                """

            CONtrol = CONtrol()
            """
            Level:RF:CONtrol

            Arguments:
            """

            class CORRECT_Index(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:CORRECT_Index

                Arguments: 1
                """
                _cmd = "CORRECT_Index"
                args = ["1"]

            CORRECT_Index = CORRECT_Index()
            """
            Level:RF:CORRECT_Index

            Arguments: 1
            """

            class Emf(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:Emf

                Arguments: 1
                """
                _cmd = "Emf"
                args = ["1"]

            Emf = Emf()
            """
            Level:RF:Emf

            Arguments: 1
            """

            class Marker(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:Marker

                Arguments: 1
                """
                _cmd = "Marker"
                args = ["1"]

            Marker = Marker()
            """
            Level:RF:Marker

            Arguments: 1
            """

            class OFFSet(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:OFFSet

                Arguments: 1
                """
                _cmd = "OFFSet"
                args = ["1"]

            OFFSet = OFFSet()
            """
            Level:RF:OFFSet

            Arguments: 1
            """

            class STArt(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:STArt

                Arguments: 1
                """
                _cmd = "STArt"
                args = ["1"]

            STArt = STArt()
            """
            Level:RF:STArt

            Arguments: 1
            """

            class STEp(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:STEp

                Arguments: 1
                """
                _cmd = "STEp"
                args = ["1"]

            STEp = STEp()
            """
            Level:RF:STEp

            Arguments: 1
            """

            class STOp(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:STOp

                Arguments: 1
                """
                _cmd = "STOp"
                args = ["1"]

            STOp = STOp()
            """
            Level:RF:STOp

            Arguments: 1
            """

            class Var_step(SCPINode, SCPIQuery, SCPISet):
                """
                Level:RF:Var_step

                Arguments: 1
                """
                _cmd = "Var_step"
                args = ["1"]

            Var_step = Var_step()
            """
            Level:RF:Var_step

            Arguments: 1
            """

        RF = RF()
        """
        Level:RF

        Arguments:
        """

    Level = Level()
    """
    Level

    Arguments:
    """

    class MARKer(SCPINodeN):
        """
        MARKer

        Arguments:
        """
        _cmd = "MARKer"
        args = []

        class FREQuency(SCPINode, SCPIQuery, SCPISet):
            """
            MARKer:FREQuency

            Arguments: 1
            """
            _cmd = "FREQuency"
            args = ["1"]

            class STEP(SCPINode):
                """
                MARKer:FREQuency:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    MARKer:FREQuency:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                MARKer:FREQuency:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            MARKer:FREQuency:STEP

            Arguments:
            """

        FREQuency = FREQuency()
        """
        MARKer:FREQuency

        Arguments: 1
        """

        class STATe(SCPINode, SCPIBool):
            """
            MARKer:STATe

            Arguments: 1, ON, OFF
            """
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()
        """
        MARKer:STATe

        Arguments: 1, ON, OFF
        """

    MARKer = MARKer()
    """
    MARKer

    Arguments:
    """

    class MEMory(SCPINode, SCPISet):
        """
        MEMory

        Arguments:
        """
        _cmd = "MEMory"
        args = []

        class CATalog(SCPINode):
            """
            MEMory:CATalog

            Arguments:
            """
            _cmd = "CATalog"
            args = []

            class BINary(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:BINary

                Arguments:
                """
                _cmd = "BINary"
                args = []

            BINary = BINary()
            """
            MEMory:CATalog:BINary

            Arguments:
            """

            class DWCDma(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:DWCDma

                Arguments:
                """
                _cmd = "DWCDma"
                args = []

            DWCDma = DWCDma()
            """
            MEMory:CATalog:DWCDma

            Arguments:
            """

            class FCDMa(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:FCDMa

                Arguments:
                """
                _cmd = "FCDMa"
                args = []

            FCDMa = FCDMa()
            """
            MEMory:CATalog:FCDMa

            Arguments:
            """

            class MCDMa(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:MCDMa

                Arguments:
                """
                _cmd = "MCDMa"
                args = []

            MCDMa = MCDMa()
            """
            MEMory:CATalog:MCDMa

            Arguments:
            """

            class MDMod(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:MDMod

                Arguments:
                """
                _cmd = "MDMod"
                args = []

            MDMod = MDMod()
            """
            MEMory:CATalog:MDMod

            Arguments:
            """

            class MDWCdma(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:MDWCdma

                Arguments:
                """
                _cmd = "MDWCdma"
                args = []

            MDWCdma = MDWCdma()
            """
            MEMory:CATalog:MDWCdma

            Arguments:
            """

            class MFCDma(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:MFCDma

                Arguments:
                """
                _cmd = "MFCDma"
                args = []

            MFCDma = MFCDma()
            """
            MEMory:CATalog:MFCDma

            Arguments:
            """

            class MTONe(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:MTONe

                Arguments:
                """
                _cmd = "MTONe"
                args = []

            MTONe = MTONe()
            """
            MEMory:CATalog:MTONe

            Arguments:
            """

            class RCDMa(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:RCDMa

                Arguments:
                """
                _cmd = "RCDMa"
                args = []

            RCDMa = RCDMa()
            """
            MEMory:CATalog:RCDMa

            Arguments:
            """

            class SHAPe(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:SHAPe

                Arguments:
                """
                _cmd = "SHAPe"
                args = []

            SHAPe = SHAPe()
            """
            MEMory:CATalog:SHAPe

            Arguments:
            """

            class STATe(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:STATe

                Arguments:
                """
                _cmd = "STATe"
                args = []

            STATe = STATe()
            """
            MEMory:CATalog:STATe

            Arguments:
            """

            class TABLe(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:TABLe

                Arguments:
                """
                _cmd = "TABLe"
                args = []

            TABLe = TABLe()
            """
            MEMory:CATalog:TABLe

            Arguments:
            """

            class UWCDma(SCPINode, SCPIQuery):
                """
                MEMory:CATalog:UWCDma

                Arguments:
                """
                _cmd = "UWCDma"
                args = []

            UWCDma = UWCDma()
            """
            MEMory:CATalog:UWCDma

            Arguments:
            """

        CATalog = CATalog()
        """
        MEMory:CATalog

        Arguments:
        """

        class DATA(SCPINode):
            """
            MEMory:DATA

            Arguments:
            """
            _cmd = "DATA"
            args = []

            class APPend(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:DATA:APPend

                Arguments: <string>,<block_data>
                """
                _cmd = "APPend"
                args = ["<string>,<block_data>"]

            APPend = APPend()
            """
            MEMory:DATA:APPend

            Arguments: <string>,<block_data>
            """

            class PRAM(SCPINode):
                """
                MEMory:DATA:PRAM

                Arguments:
                """
                _cmd = "PRAM"
                args = []

                class FILE(SCPINode):
                    """
                    MEMory:DATA:PRAM:FILE

                    Arguments:
                    """
                    _cmd = "FILE"
                    args = []

                    class BLOCk(SCPINode, SCPIQuery, SCPISet):
                        """
                        MEMory:DATA:PRAM:FILE:BLOCk

                        Arguments: <string>,<block_data>
                        """
                        _cmd = "BLOCk"
                        args = ["<string>,<block_data>"]

                    BLOCk = BLOCk()
                    """
                    MEMory:DATA:PRAM:FILE:BLOCk

                    Arguments: <string>,<block_data>
                    """

                FILE = FILE()
                """
                MEMory:DATA:PRAM:FILE

                Arguments:
                """

            PRAM = PRAM()
            """
            MEMory:DATA:PRAM

            Arguments:
            """

            class SHAPe(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:DATA:SHAPe

                Arguments: <string>,<numeric_value>,<numeric_value>
                """
                _cmd = "SHAPe"
                args = ["<string>,<numeric_value>,<numeric_value>"]

            SHAPe = SHAPe()
            """
            MEMory:DATA:SHAPe

            Arguments: <string>,<numeric_value>,<numeric_value>
            """

            class UNPRotected(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:DATA:UNPRotected

                Arguments: <string>,<block_data>
                """
                _cmd = "UNPRotected"
                args = ["<string>,<block_data>"]

            UNPRotected = UNPRotected()
            """
            MEMory:DATA:UNPRotected

            Arguments: <string>,<block_data>
            """

        DATA = DATA()
        """
        MEMory:DATA

        Arguments:
        """

        class DELete(SCPINode):
            """
            MEMory:DELete

            Arguments:
            """
            _cmd = "DELete"
            args = []

            class BINary(SCPINode, SCPISet):
                """
                MEMory:DELete:BINary

                Arguments:
                """
                _cmd = "BINary"
                args = []

            BINary = BINary()
            """
            MEMory:DELete:BINary

            Arguments:
            """

            class DWCDma(SCPINode, SCPISet):
                """
                MEMory:DELete:DWCDma

                Arguments:
                """
                _cmd = "DWCDma"
                args = []

            DWCDma = DWCDma()
            """
            MEMory:DELete:DWCDma

            Arguments:
            """

            class FCDMa(SCPINode, SCPISet):
                """
                MEMory:DELete:FCDMa

                Arguments:
                """
                _cmd = "FCDMa"
                args = []

            FCDMa = FCDMa()
            """
            MEMory:DELete:FCDMa

            Arguments:
            """

            class MCDMa(SCPINode, SCPISet):
                """
                MEMory:DELete:MCDMa

                Arguments:
                """
                _cmd = "MCDMa"
                args = []

            MCDMa = MCDMa()
            """
            MEMory:DELete:MCDMa

            Arguments:
            """

            class MDMod(SCPINode, SCPISet):
                """
                MEMory:DELete:MDMod

                Arguments:
                """
                _cmd = "MDMod"
                args = []

            MDMod = MDMod()
            """
            MEMory:DELete:MDMod

            Arguments:
            """

            class MDWCdma(SCPINode, SCPISet):
                """
                MEMory:DELete:MDWCdma

                Arguments:
                """
                _cmd = "MDWCdma"
                args = []

            MDWCdma = MDWCdma()
            """
            MEMory:DELete:MDWCdma

            Arguments:
            """

            class MFCDma(SCPINode, SCPISet):
                """
                MEMory:DELete:MFCDma

                Arguments:
                """
                _cmd = "MFCDma"
                args = []

            MFCDma = MFCDma()
            """
            MEMory:DELete:MFCDma

            Arguments:
            """

            class MTONe(SCPINode, SCPISet):
                """
                MEMory:DELete:MTONe

                Arguments:
                """
                _cmd = "MTONe"
                args = []

            MTONe = MTONe()
            """
            MEMory:DELete:MTONe

            Arguments:
            """

            class RCDMa(SCPINode, SCPISet):
                """
                MEMory:DELete:RCDMa

                Arguments:
                """
                _cmd = "RCDMa"
                args = []

            RCDMa = RCDMa()
            """
            MEMory:DELete:RCDMa

            Arguments:
            """

            class SHAPe(SCPINode, SCPISet):
                """
                MEMory:DELete:SHAPe

                Arguments:
                """
                _cmd = "SHAPe"
                args = []

            SHAPe = SHAPe()
            """
            MEMory:DELete:SHAPe

            Arguments:
            """

            class STATe(SCPINode, SCPISet):
                """
                MEMory:DELete:STATe

                Arguments:
                """
                _cmd = "STATe"
                args = []

            STATe = STATe()
            """
            MEMory:DELete:STATe

            Arguments:
            """

            class UWCDma(SCPINode, SCPISet):
                """
                MEMory:DELete:UWCDma

                Arguments:
                """
                _cmd = "UWCDma"
                args = []

            UWCDma = UWCDma()
            """
            MEMory:DELete:UWCDma

            Arguments:
            """

        DELete = DELete()
        """
        MEMory:DELete

        Arguments:
        """

        class FREE(SCPINode):
            """
            MEMory:FREE

            Arguments:
            """
            _cmd = "FREE"
            args = []

            class MACRo(SCPINode, SCPIQuery):
                """
                MEMory:FREE:MACRo

                Arguments:
                """
                _cmd = "MACRo"
                args = []

            MACRo = MACRo()
            """
            MEMory:FREE:MACRo

            Arguments:
            """

        FREE = FREE()
        """
        MEMory:FREE

        Arguments:
        """

        class NSTates(SCPINode, SCPIQuery):
            """
            MEMory:NSTates

            Arguments:
            """
            _cmd = "NSTates"
            args = []

        NSTates = NSTates()
        """
        MEMory:NSTates

        Arguments:
        """

        class STATe(SCPINode, SCPISet):
            """
            MEMory:STATe

            Arguments:
            """
            _cmd = "STATe"
            args = []

            class COMMent(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:STATe:COMMent

                Arguments: <numeric_value>,<numeric_value>,<string>
                """
                _cmd = "COMMent"
                args = ["<numeric_value>,<numeric_value>,<string>"]

            COMMent = COMMent()
            """
            MEMory:STATe:COMMent

            Arguments: <numeric_value>,<numeric_value>,<string>
            """

        STATe = STATe()
        """
        MEMory:STATe

        Arguments:
        """

        class STORe(SCPINode, SCPISet):
            """
            MEMory:STORe

            Arguments:
            """
            _cmd = "STORe"
            args = []

        STORe = STORe()
        """
        MEMory:STORe

        Arguments:
        """

        class TABLe(SCPINode):
            """
            MEMory:TABLe

            Arguments:
            """
            _cmd = "TABLe"
            args = []

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:TABLe:FREQuency

                Arguments: <numeric_value>[AHZ, FHZ, PHZ, NHZ, UHZ, HZ, KHZ, MHZ, GHZ, THZ, PEHZ, EXHZ],<numeric_value>
                """
                _cmd = "FREQuency"
                args = ["<numeric_value>[AHZ", "FHZ", "PHZ", "NHZ", "UHZ", "HZ", "KHZ", "MHZ", "GHZ", "THZ", "PEHZ", "EXHZ],<numeric_value>"]

                class POINts(SCPINode, SCPIQuery):
                    """
                    MEMory:TABLe:FREQuency:POINts

                    Arguments: 1
                    """
                    _cmd = "POINts"
                    args = ["1"]

                POINts = POINts()
                """
                MEMory:TABLe:FREQuency:POINts

                Arguments: 1
                """

            FREQuency = FREQuency()
            """
            MEMory:TABLe:FREQuency

            Arguments: <numeric_value>[AHZ, FHZ, PHZ, NHZ, UHZ, HZ, KHZ, MHZ, GHZ, THZ, PEHZ, EXHZ],<numeric_value>
            """

            class LOSS(SCPINode):
                """
                MEMory:TABLe:LOSS

                Arguments:
                """
                _cmd = "LOSS"
                args = []

                class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    MEMory:TABLe:LOSS:MAGNitude

                    Arguments: <numeric_value>[DB],<numeric_value>
                    """
                    _cmd = "MAGNitude"
                    args = ["<numeric_value>[DB],<numeric_value>"]

                    class POINts(SCPINode, SCPIQuery):
                        """
                        MEMory:TABLe:LOSS:MAGNitude:POINts

                        Arguments: 1
                        """
                        _cmd = "POINts"
                        args = ["1"]

                    POINts = POINts()
                    """
                    MEMory:TABLe:LOSS:MAGNitude:POINts

                    Arguments: 1
                    """

                MAGNitude = MAGNitude()
                """
                MEMory:TABLe:LOSS:MAGNitude

                Arguments: <numeric_value>[DB],<numeric_value>
                """

            LOSS = LOSS()
            """
            MEMory:TABLe:LOSS

            Arguments:
            """

            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                MEMory:TABLe:SELect

                Arguments: FDAT1, FDAT2, FDAT3, FDAT4
                """
                _cmd = "SELect"
                args = ["FDAT1", "FDAT2", "FDAT3", "FDAT4"]

            SELect = SELect()
            """
            MEMory:TABLe:SELect

            Arguments: FDAT1, FDAT2, FDAT3, FDAT4
            """

        TABLe = TABLe()
        """
        MEMory:TABLe

        Arguments:
        """

    MEMory = MEMory()
    """
    MEMory

    Arguments:
    """

    class MEmory(SCPINode):
        """
        MEmory

        Arguments:
        """
        _cmd = "MEmory"
        args = []

        class Fast(SCPINode, SCPISet):
            """
            MEmory:Fast

            Arguments:
            """
            _cmd = "Fast"
            args = []

            class STArt(SCPINode, SCPIQuery, SCPISet):
                """
                MEmory:Fast:STArt

                Arguments: 1
                """
                _cmd = "STArt"
                args = ["1"]

            STArt = STArt()
            """
            MEmory:Fast:STArt

            Arguments: 1
            """

            class STOp(SCPINode, SCPIQuery, SCPISet):
                """
                MEmory:Fast:STOp

                Arguments: 1
                """
                _cmd = "STOp"
                args = ["1"]

            STOp = STOp()
            """
            MEmory:Fast:STOp

            Arguments: 1
            """

        Fast = Fast()
        """
        MEmory:Fast

        Arguments:
        """

        class STArt(SCPINode, SCPIQuery, SCPISet):
            """
            MEmory:STArt

            Arguments: 1
            """
            _cmd = "STArt"
            args = ["1"]

        STArt = STArt()
        """
        MEmory:STArt

        Arguments: 1
        """

        class STOp(SCPINode, SCPIQuery, SCPISet):
            """
            MEmory:STOp

            Arguments: 1
            """
            _cmd = "STOp"
            args = ["1"]

        STOp = STOp()
        """
        MEmory:STOp

        Arguments: 1
        """

    MEmory = MEmory()
    """
    MEmory

    Arguments:
    """

    class MMEMory(SCPINode):
        """
        MMEMory

        Arguments:
        """
        _cmd = "MMEMory"
        args = []

        class ALIases(SCPINode, SCPIQuery):
            """
            MMEMory:ALIases

            Arguments:
            """
            _cmd = "ALIases"
            args = []

        ALIases = ALIases()
        """
        MMEMory:ALIases

        Arguments:
        """

        class ATTRibute(SCPINode, SCPIQuery, SCPISet):
            """
            MMEMory:ATTRibute

            Arguments: <string>,<string>
            """
            _cmd = "ATTRibute"
            args = ["<string>,<string>"]

        ATTRibute = ATTRibute()
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
            _cmd = "CATalog"
            args = ["'string'"]

            class LENGth(SCPINode, SCPIQuery):
                """
                `MMEMory:CATalog:LENGth
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f52dbc720a0a48f9.htm#ID_de3b183c900f4f0f0a00206a0011b22f-adb17661900f4f0f0a00206a01eae7a4-en-US>`_

                Arguments: 'string'
                """
                _cmd = "LENGth"
                args = ["'string'"]

            LENGth = LENGth()
            """
            `MMEMory:CATalog:LENGth
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f52dbc720a0a48f9.htm#ID_de3b183c900f4f0f0a00206a0011b22f-adb17661900f4f0f0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """

        CATalog = CATalog()
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
            _cmd = "CDIRectory"
            args = ["'string'"]

        CDIRectory = CDIRectory()
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
            _cmd = "DCATalog"
            args = ["'string'"]

            class LENGth(SCPINode, SCPIQuery):
                """
                `MMEMory:DCATalog:LENGth
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a083db692d2a43f1.htm#ID_4e070651900ef70b0a00206a016f7a85-a0f33d76900ef70b0a00206a01eae7a4-en-US>`_

                Arguments: 'string'
                """
                _cmd = "LENGth"
                args = ["'string'"]

            LENGth = LENGth()
            """
            `MMEMory:DCATalog:LENGth
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a083db692d2a43f1.htm#ID_4e070651900ef70b0a00206a016f7a85-a0f33d76900ef70b0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """

        DCATalog = DCATalog()
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
            _cmd = "DELete"
            args = ["'string'"]

            class NVWFm(SCPINode, SCPISet):
                """
                MMEMory:DELete:NVWFm

                Arguments:
                """
                _cmd = "NVWFm"
                args = []

            NVWFm = NVWFm()
            """
            MMEMory:DELete:NVWFm

            Arguments:
            """

            class WFM(SCPINodeN, SCPISet):
                """
                MMEMory:DELete:WFM

                Arguments:
                """
                _cmd = "WFM"
                args = []

            WFM = WFM()
            """
            MMEMory:DELete:WFM

            Arguments:
            """

        DELete = DELete()
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
            _cmd = "DRIVes"
            args = []

        DRIVes = DRIVes()
        """
        MMEMory:DRIVes

        Arguments:
        """

        class HEADer(SCPINode, SCPISet):
            """
            MMEMory:HEADer

            Arguments:
            """
            _cmd = "HEADer"
            args = []

            class CLEar(SCPINode, SCPISet):
                """
                MMEMory:HEADer:CLEar

                Arguments: 'string'
                """
                _cmd = "CLEar"
                args = ["'string'"]

            CLEar = CLEar()
            """
            MMEMory:HEADer:CLEar

            Arguments: 'string'
            """

            class DESCription(SCPINode, SCPISet):
                """
                MMEMory:HEADer:DESCription

                Arguments: <string>,<string>
                """
                _cmd = "DESCription"
                args = ["<string>,<string>"]

            DESCription = DESCription()
            """
            MMEMory:HEADer:DESCription

            Arguments: <string>,<string>
            """

        HEADer = HEADer()
        """
        MMEMory:HEADer

        Arguments:
        """

        class LOAD(SCPINode):
            """
            MMEMory:LOAD

            Arguments:
            """
            _cmd = "LOAD"
            args = []

            class MACRo(SCPINode, SCPISet):
                """
                MMEMory:LOAD:MACRo

                Arguments: <string>,<string>,<string>
                """
                _cmd = "MACRo"
                args = ["<string>,<string>,<string>"]

            MACRo = MACRo()
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
                _cmd = "STATe"
                args = ["<numeric_value>,<string>,<string>"]

            STATe = STATe()
            """
            `MMEMory:LOAD:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/9de91cebcfaf4dfb.htm#ID_e4b148b6b16d7e450a00206a00d7d85c-f2c489ebb16d7e450a00206a002cfbf4-en-US>`_

            Arguments: <numeric_value>,<string>,<string>
            """

        LOAD = LOAD()
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
            _cmd = "MDIRectory"
            args = ["'string'"]

        MDIRectory = MDIRectory()
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
            _cmd = "RDIRectory"
            args = ["'string'"]

        RDIRectory = RDIRectory()
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
            _cmd = "STORe"
            args = []

            class MACRo(SCPINode, SCPISet):
                """
                MMEMory:STORe:MACRo

                Arguments: <string>,<string>,<string>
                """
                _cmd = "MACRo"
                args = ["<string>,<string>,<string>"]

            MACRo = MACRo()
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
                _cmd = "STATe"
                args = ["<integer>,<string>,<string>"]

            STATe = STATe()
            """
            `MMEMory:STORe:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a5614cb446644ab0.htm#ID_45c41292b170604d0a00206a0129c63d-053ce38db170604d0a00206a01567e4b-en-US>`_

            Arguments: <integer>,<string>,<string>
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

    class MODulation(SCPINode):
        """
        MODulation

        Arguments:
        """
        _cmd = "MODulation"
        args = []

        class STATe(SCPINode, SCPIBool):
            """
            MODulation:STATe

            Arguments: 1, ON, OFF
            """
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()
        """
        MODulation:STATe

        Arguments: 1, ON, OFF
        """

    MODulation = MODulation()
    """
    MODulation

    Arguments:
    """

    class MOdulation(SCPINode, SCPIQuery):
        """
        MOdulation

        Arguments:
        """
        _cmd = "MOdulation"
        args = []

        class Normal(SCPINode, SCPISet):
            """
            MOdulation:Normal

            Arguments:
            """
            _cmd = "Normal"
            args = []

        Normal = Normal()
        """
        MOdulation:Normal

        Arguments:
        """

        class Reduced(SCPINode, SCPISet):
            """
            MOdulation:Reduced

            Arguments:
            """
            _cmd = "Reduced"
            args = []

        Reduced = Reduced()
        """
        MOdulation:Reduced

        Arguments:
        """

    MOdulation = MOdulation()
    """
    MOdulation

    Arguments:
    """

    class MPRot(SCPINode, SCPIQuery):
        """
        MPRot

        Arguments:
        """
        _cmd = "MPRot"
        args = []

        class STARt(SCPINode, SCPISet):
            """
            MPRot:STARt

            Arguments: 1
            """
            _cmd = "STARt"
            args = ["1"]

        STARt = STARt()
        """
        MPRot:STARt

        Arguments: 1
        """

    MPRot = MPRot()
    """
    MPRot

    Arguments:
    """

    class MTRig(SCPINode, SCPIQuery):
        """
        MTRig

        Arguments:
        """
        _cmd = "MTRig"
        args = []

    MTRig = MTRig()
    """
    MTRig

    Arguments:
    """

    class OUTPut(SCPINode, SCPIQuery, SCPISet):
        """
        OUTPut

        Arguments:
        """
        _cmd = "OUTPut"
        args = []

        class AFIXed(SCPINode):
            """
            OUTPut:AFIXed

            Arguments:
            """
            _cmd = "AFIXed"
            args = []

            class RANGe(SCPINode):
                """
                OUTPut:AFIXed:RANGe

                Arguments:
                """
                _cmd = "RANGe"
                args = []

                class LOWer(SCPINode, SCPIQuery):
                    """
                    `OUTPut:AFIXed:RANGe:LOWer
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/357ac8f3e4244a47.htm#ID_e38f0e814e64057e0a00206a0013b470-127480ee4e64057e0a00206a0024546d-en-US>`_

                    Arguments:
                    """
                    _cmd = "LOWer"
                    args = []

                LOWer = LOWer()
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
                    _cmd = "UPPer"
                    args = []

                UPPer = UPPer()
                """
                `OUTPut:AFIXed:RANGe:UPPer
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/41e4a70f35a54cde.htm#ID_a55c89064e640b1d0a00206a01925c56-3ee9d9c74e640b1d0a00206a0024546d-en-US>`_

                Arguments:
                """

            RANGe = RANGe()
            """
            OUTPut:AFIXed:RANGe

            Arguments:
            """

        AFIXed = AFIXed()
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
            _cmd = "AMODe"
            args = ["AUTO", "FIXed"]

        AMODe = AMODe()
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
            _cmd = "ATTenuation"
            args = ["1"]

        ATTenuation = ATTenuation()
        """
        OUTPut:ATTenuation

        Arguments: 1
        """

        class BLANk(SCPINode):
            """
            OUTPut:BLANk

            Arguments:
            """
            _cmd = "BLANk"
            args = []

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                OUTPut:BLANk:POLarity

                Arguments: INVerted, NORMal
                """
                _cmd = "POLarity"
                args = ["INVerted", "NORMal"]

            POLarity = POLarity()
            """
            OUTPut:BLANk:POLarity

            Arguments: INVerted, NORMal
            """

        BLANk = BLANk()
        """
        OUTPut:BLANk

        Arguments:
        """

        class BLANking(SCPINode):
            """
            OUTPut:BLANking

            Arguments:
            """
            _cmd = "BLANking"
            args = []

            class STATe(SCPINode, SCPIBool):
                """
                OUTPut:BLANking:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            OUTPut:BLANking:STATe

            Arguments: 1, ON, OFF
            """

        BLANking = BLANking()
        """
        OUTPut:BLANking

        Arguments:
        """

        class DISable(SCPINode, SCPISet):
            """
            OUTPut:DISable

            Arguments:
            """
            _cmd = "DISable"
            args = []

        DISable = DISable()
        """
        OUTPut:DISable

        Arguments:
        """

        class ENABle(SCPINode, SCPISet):
            """
            OUTPut:ENABle

            Arguments:
            """
            _cmd = "ENABle"
            args = []

        ENABle = ENABle()
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
            _cmd = "IMPedance"
            args = ["1"]

        IMPedance = IMPedance()
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
            _cmd = "LIBLanking"
            args = ["NORMal", "OFF"]

        LIBLanking = LIBLanking()
        """
        OUTPut:LIBLanking

        Arguments: NORMal, OFF
        """

        class MODulation(SCPINode):
            """
            OUTPut:MODulation

            Arguments:
            """
            _cmd = "MODulation"
            args = []

            class STATe(SCPINode, SCPIBool):
                """
                OUTPut:MODulation:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            OUTPut:MODulation:STATe

            Arguments: 1, ON, OFF
            """

        MODulation = MODulation()
        """
        OUTPut:MODulation

        Arguments:
        """

        class POLarity(SCPINode):
            """
            OUTPut:POLarity

            Arguments:
            """
            _cmd = "POLarity"
            args = []

            class PULSe(SCPINode, SCPIQuery, SCPISet):
                """
                OUTPut:POLarity:PULSe

                Arguments: INVerted, NORMal
                """
                _cmd = "PULSe"
                args = ["INVerted", "NORMal"]

            PULSe = PULSe()
            """
            OUTPut:POLarity:PULSe

            Arguments: INVerted, NORMal
            """

        POLarity = POLarity()
        """
        OUTPut:POLarity

        Arguments:
        """

        class PROTection(SCPINode, SCPIBool):
            """
            OUTPut:PROTection

            Arguments: 1, ON, OFF
            """
            _cmd = "PROTection"
            args = ["1", "ON", "OFF"]

            class CLEar(SCPINode, SCPISet):
                """
                `OUTPut:PROTection:CLEar
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/312a93269b474916.htm#ID_ff19e8ab4e64109c0a00206a01e0ace3-ddc4d9a54e64109c0a00206a0024546d-en-US>`_

                Arguments:
                """
                _cmd = "CLEar"
                args = []

            CLEar = CLEar()
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
                _cmd = "RETRace"
                args = ["1", "ON", "OFF"]

            RETRace = RETRace()
            """
            OUTPut:PROTection:RETRace

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                OUTPut:PROTection:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
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
                _cmd = "TRIPped"
                args = []

            TRIPped = TRIPped()
            """
            `OUTPut:PROTection:TRIPped
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/8c639762430041c7.htm#ID_37db314d4e64161b0a00206a005d0255-2d47945b4e64161b0a00206a0024546d-en-US>`_

            Arguments:
            """

        PROTection = PROTection()
        """
        OUTPut:PROTection

        Arguments: 1, ON, OFF
        """

        class RFBLanking(SCPINode, SCPIQuery, SCPISet):
            """
            OUTPut:RFBLanking

            Arguments: <boolean>, AUTO
            """
            _cmd = "RFBLanking"
            args = ["<boolean>", "AUTO"]

        RFBLanking = RFBLanking()
        """
        OUTPut:RFBLanking

        Arguments: <boolean>, AUTO
        """

        class SCALe(SCPINode, SCPIQuery, SCPISet):
            """
            OUTPut:SCALe

            Arguments: 1
            """
            _cmd = "SCALe"
            args = ["1"]

        SCALe = SCALe()
        """
        OUTPut:SCALe

        Arguments: 1
        """

        class SOURce(SCPINode, SCPIQuery, SCPISet):
            """
            OUTPut:SOURce

            Arguments: 1
            """
            _cmd = "SOURce"
            args = ["1"]

            class STEReo(SCPINode, SCPIQuery, SCPISet):
                """
                OUTPut:SOURce:STEReo

                Arguments: MPX, PILot
                """
                _cmd = "STEReo"
                args = ["MPX", "PILot"]

            STEReo = STEReo()
            """
            OUTPut:SOURce:STEReo

            Arguments: MPX, PILot
            """

        SOURce = SOURce()
        """
        OUTPut:SOURce

        Arguments: 1
        """

        class STANdby(SCPINode):
            """
            OUTPut:STANdby

            Arguments:
            """
            _cmd = "STANdby"
            args = []

            class STATe(SCPINode, SCPIBool):
                """
                OUTPut:STANdby:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            OUTPut:STANdby:STATe

            Arguments: 1, ON, OFF
            """

        STANdby = STANdby()
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
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

            class BACKup(SCPINode, SCPIBool):
                """
                OUTPut:STATe:BACKup

                Arguments: 1, ON, OFF
                """
                _cmd = "BACKup"
                args = ["1", "ON", "OFF"]

            BACKup = BACKup()
            """
            OUTPut:STATe:BACKup

            Arguments: 1, ON, OFF
            """

        STATe = STATe()
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
            _cmd = "VOLTage"
            args = ["1"]

        VOLTage = VOLTage()
        """
        OUTPut:VOLTage

        Arguments: 1
        """

    OUTPut = OUTPut()
    """
    OUTPut

    Arguments:
    """

    class PHASe(SCPINode):
        """
        PHASe

        Arguments:
        """
        _cmd = "PHASe"
        args = []

        class ADJust(SCPINode, SCPIQuery, SCPISet):
            """
            PHASe:ADJust

            Arguments: 1
            """
            _cmd = "ADJust"
            args = ["1"]

            class STEP(SCPINode):
                """
                PHASe:ADJust:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    PHASe:ADJust:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                PHASe:ADJust:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            PHASe:ADJust:STEP

            Arguments:
            """

        ADJust = ADJust()
        """
        PHASe:ADJust

        Arguments: 1
        """

        class REFerence(SCPINode, SCPISet):
            """
            PHASe:REFerence

            Arguments:
            """
            _cmd = "REFerence"
            args = []

        REFerence = REFerence()
        """
        PHASe:REFerence

        Arguments:
        """

    PHASe = PHASe()
    """
    PHASe

    Arguments:
    """

    class PHAse(SCPINode, SCPIQuery, SCPISet):
        """
        PHAse

        Arguments: 1
        """
        _cmd = "PHAse"
        args = ["1"]

        class Internal(SCPINode, SCPISet):
            """
            PHAse:Internal

            Arguments: 1
            """
            _cmd = "Internal"
            args = ["1"]

        Internal = Internal()
        """
        PHAse:Internal

        Arguments: 1
        """

        class Var_step(SCPINode, SCPIQuery, SCPISet):
            """
            PHAse:Var_step

            Arguments: 1
            """
            _cmd = "Var_step"
            args = ["1"]

        Var_step = Var_step()
        """
        PHAse:Var_step

        Arguments: 1
        """

    PHAse = PHAse()
    """
    PHAse

    Arguments: 1
    """

    class PMETer(SCPINode):
        """
        PMETer

        Arguments:
        """
        _cmd = "PMETer"
        args = []

        class POWer(SCPINode, SCPIQuery):
            """
            PMETer:POWer

            Arguments: 1
            """
            _cmd = "POWer"
            args = ["1"]

        POWer = POWer()
        """
        PMETer:POWer

        Arguments: 1
        """

    PMETer = PMETer()
    """
    PMETer

    Arguments:
    """

    class POWer(SCPINode):
        """
        POWer

        Arguments:
        """
        _cmd = "POWer"
        args = []

        class OUT(SCPINode):
            """
            POWer:OUT

            Arguments:
            """
            _cmd = "OUT"
            args = []

            class ALC(SCPINode):
                """
                POWer:OUT:ALC

                Arguments:
                """
                _cmd = "ALC"
                args = []

                class BANDwidth(SCPINode, SCPISet):
                    """
                    POWer:OUT:ALC:BANDwidth

                    Arguments:
                    """
                    _cmd = "BANDwidth"
                    args = []

                BANDwidth = BANDwidth()
                """
                POWer:OUT:ALC:BANDwidth

                Arguments:
                """

            ALC = ALC()
            """
            POWer:OUT:ALC

            Arguments:
            """

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:OUT:ATTenuation

                Arguments: 1
                """
                _cmd = "ATTenuation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    POWer:OUT:ATTenuation:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        POWer:OUT:ATTenuation:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    POWer:OUT:ATTenuation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                POWer:OUT:ATTenuation:STEP

                Arguments:
                """

            ATTenuation = ATTenuation()
            """
            POWer:OUT:ATTenuation

            Arguments: 1
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:OUT:LEVel

                Arguments: 1
                """
                _cmd = "LEVel"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    POWer:OUT:LEVel:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        POWer:OUT:LEVel:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    POWer:OUT:LEVel:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                POWer:OUT:LEVel:STEP

                Arguments:
                """

            LEVel = LEVel()
            """
            POWer:OUT:LEVel

            Arguments: 1
            """

            class MUTing(SCPINode, SCPIBool):
                """
                POWer:OUT:MUTing

                Arguments: 1, ON, OFF
                """
                _cmd = "MUTing"
                args = ["1", "ON", "OFF"]

            MUTing = MUTing()
            """
            POWer:OUT:MUTing

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                POWer:OUT:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            POWer:OUT:STATe

            Arguments: 1, ON, OFF
            """

            class ULIMit(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:OUT:ULIMit

                Arguments: 1
                """
                _cmd = "ULIMit"
                args = ["1"]

            ULIMit = ULIMit()
            """
            POWer:OUT:ULIMit

            Arguments: 1
            """

        OUT = OUT()
        """
        POWer:OUT

        Arguments:
        """

        class SOURce(SCPINode):
            """
            POWer:SOURce

            Arguments:
            """
            _cmd = "SOURce"
            args = []

            class ALC(SCPINode):
                """
                POWer:SOURce:ALC

                Arguments:
                """
                _cmd = "ALC"
                args = []

                class BANDwidth(SCPINode, SCPISet):
                    """
                    POWer:SOURce:ALC:BANDwidth

                    Arguments:
                    """
                    _cmd = "BANDwidth"
                    args = []

                BANDwidth = BANDwidth()
                """
                POWer:SOURce:ALC:BANDwidth

                Arguments:
                """

            ALC = ALC()
            """
            POWer:SOURce:ALC

            Arguments:
            """

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:SOURce:ATTenuation

                Arguments: 1
                """
                _cmd = "ATTenuation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    POWer:SOURce:ATTenuation:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        POWer:SOURce:ATTenuation:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    POWer:SOURce:ATTenuation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                POWer:SOURce:ATTenuation:STEP

                Arguments:
                """

            ATTenuation = ATTenuation()
            """
            POWer:SOURce:ATTenuation

            Arguments: 1
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:SOURce:LEVel

                Arguments: 1
                """
                _cmd = "LEVel"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    POWer:SOURce:LEVel:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        POWer:SOURce:LEVel:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    POWer:SOURce:LEVel:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                POWer:SOURce:LEVel:STEP

                Arguments:
                """

            LEVel = LEVel()
            """
            POWer:SOURce:LEVel

            Arguments: 1
            """

            class MUTing(SCPINode, SCPIBool):
                """
                POWer:SOURce:MUTing

                Arguments: 1, ON, OFF
                """
                _cmd = "MUTing"
                args = ["1", "ON", "OFF"]

            MUTing = MUTing()
            """
            POWer:SOURce:MUTing

            Arguments: 1, ON, OFF
            """

            class STATe(SCPINode, SCPIBool):
                """
                POWer:SOURce:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            POWer:SOURce:STATe

            Arguments: 1, ON, OFF
            """

            class ULIMit(SCPINode, SCPIQuery, SCPISet):
                """
                POWer:SOURce:ULIMit

                Arguments: 1
                """
                _cmd = "ULIMit"
                args = ["1"]

            ULIMit = ULIMit()
            """
            POWer:SOURce:ULIMit

            Arguments: 1
            """

        SOURce = SOURce()
        """
        POWer:SOURce

        Arguments:
        """

    POWer = POWer()
    """
    POWer

    Arguments:
    """

    class POWup(SCPINode, SCPIQuery):
        """
        POWup

        Arguments:
        """
        _cmd = "POWup"
        args = []

    POWup = POWup()
    """
    POWup

    Arguments:
    """

    class PReset(SCPINode, SCPISet):
        """
        PReset

        Arguments:
        """
        _cmd = "PReset"
        args = []

    PReset = PReset()
    """
    PReset

    Arguments:
    """

    class PULSe(SCPINode, SCPIQuery):
        """
        PULSe

        Arguments:
        """
        _cmd = "PULSe"
        args = []

        class CAL(SCPINode):
            """
            PULSe:CAL

            Arguments:
            """
            _cmd = "CAL"
            args = []

            class DISable(SCPINode, SCPISet):
                """
                PULSe:CAL:DISable

                Arguments:
                """
                _cmd = "DISable"
                args = []

            DISable = DISable()
            """
            PULSe:CAL:DISable

            Arguments:
            """

            class ENABle(SCPINode, SCPISet):
                """
                PULSe:CAL:ENABle

                Arguments:
                """
                _cmd = "ENABle"
                args = []

            ENABle = ENABle()
            """
            PULSe:CAL:ENABle

            Arguments:
            """

        CAL = CAL()
        """
        PULSe:CAL

        Arguments:
        """

        class CONDitioning(SCPINode, SCPIBool):
            """
            PULSe:CONDitioning

            Arguments: 1, ON, OFF
            """
            _cmd = "CONDitioning"
            args = ["1", "ON", "OFF"]

        CONDitioning = CONDitioning()
        """
        PULSe:CONDitioning

        Arguments: 1, ON, OFF
        """

        class DELay(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:DELay

            Arguments: 1
            """
            _cmd = "DELay"
            args = ["1"]

            class STEP(SCPINode):
                """
                PULSe:DELay:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    PULSe:DELay:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                PULSe:DELay:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            PULSe:DELay:STEP

            Arguments:
            """

        DELay = DELay()
        """
        PULSe:DELay

        Arguments: 1
        """

        class FREQuency(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:FREQuency

            Arguments: 1
            """
            _cmd = "FREQuency"
            args = ["1"]

            class STEP(SCPINode):
                """
                PULSe:FREQuency:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    PULSe:FREQuency:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                PULSe:FREQuency:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            PULSe:FREQuency:STEP

            Arguments:
            """

        FREQuency = FREQuency()
        """
        PULSe:FREQuency

        Arguments: 1
        """

        class IMPedance(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:IMPedance

            Arguments: 1
            """
            _cmd = "IMPedance"
            args = ["1"]

        IMPedance = IMPedance()
        """
        PULSe:IMPedance

        Arguments: 1
        """

        class MODF(SCPINode):
            """
            PULSe:MODF

            Arguments:
            """
            _cmd = "MODF"
            args = []

            class VALue(SCPINode, SCPISet):
                """
                PULSe:MODF:VALue

                Arguments: 1
                """
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()
            """
            PULSe:MODF:VALue

            Arguments: 1
            """

        MODF = MODF()
        """
        PULSe:MODF

        Arguments:
        """

        class SLOPe(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:SLOPe

            Arguments: BOTH, NEGative, POSitive
            """
            _cmd = "SLOPe"
            args = ["BOTH", "NEGative", "POSitive"]

        SLOPe = SLOPe()
        """
        PULSe:SLOPe

        Arguments: BOTH, NEGative, POSitive
        """

        class SOURce(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:SOURce

            Arguments: EXTernal, INTernal,EXTernal, INTernal
            """
            _cmd = "SOURce"
            args = ["EXTernal", "INTernal,EXTernal", "INTernal"]

        SOURce = SOURce()
        """
        PULSe:SOURce

        Arguments: EXTernal, INTernal,EXTernal, INTernal
        """

        class STATe(SCPINode, SCPIBool):
            """
            PULSe:STATe

            Arguments: 1, ON, OFF
            """
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()
        """
        PULSe:STATe

        Arguments: 1, ON, OFF
        """

        class WIDTh(SCPINode, SCPIQuery, SCPISet):
            """
            PULSe:WIDTh

            Arguments: 1
            """
            _cmd = "WIDTh"
            args = ["1"]

            class STEP(SCPINode):
                """
                PULSe:WIDTh:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    PULSe:WIDTh:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                PULSe:WIDTh:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            PULSe:WIDTh:STEP

            Arguments:
            """

        WIDTh = WIDTh()
        """
        PULSe:WIDTh

        Arguments: 1
        """

    PULSe = PULSe()
    """
    PULSe

    Arguments:
    """

    class PUlse(SCPINode, SCPIQuery, SCPISet):
        """
        PUlse

        Arguments:
        """
        _cmd = "PUlse"
        args = []

        class Inverted(SCPINode, SCPISet):
            """
            PUlse:Inverted

            Arguments:
            """
            _cmd = "Inverted"
            args = []

        Inverted = Inverted()
        """
        PUlse:Inverted

        Arguments:
        """

        class Normal(SCPINode, SCPISet):
            """
            PUlse:Normal

            Arguments:
            """
            _cmd = "Normal"
            args = []

        Normal = Normal()
        """
        PUlse:Normal

        Arguments:
        """

    PUlse = PUlse()
    """
    PUlse

    Arguments:
    """

    class REFerence_oscil(SCPINode, SCPIQuery, SCPISet):
        """
        REFerence_oscil

        Arguments:
        """
        _cmd = "REFerence_oscil"
        args = []

        class CORrection(SCPINode, SCPISet):
            """
            REFerence_oscil:CORrection

            Arguments: 1
            """
            _cmd = "CORrection"
            args = ["1"]

            class STOre(SCPINode, SCPISet):
                """
                REFerence_oscil:CORrection:STOre

                Arguments:
                """
                _cmd = "STOre"
                args = []

            STOre = STOre()
            """
            REFerence_oscil:CORrection:STOre

            Arguments:
            """

        CORrection = CORrection()
        """
        REFerence_oscil:CORrection

        Arguments: 1
        """

        class External(SCPINode, SCPISet):
            """
            REFerence_oscil:External

            Arguments:
            """
            _cmd = "External"
            args = []

        External = External()
        """
        REFerence_oscil:External

        Arguments:
        """

        class High(SCPINode, SCPISet):
            """
            REFerence_oscil:High

            Arguments:
            """
            _cmd = "High"
            args = []

        High = High()
        """
        REFerence_oscil:High

        Arguments:
        """

        class Internal(SCPINode, SCPISet):
            """
            REFerence_oscil:Internal

            Arguments:
            """
            _cmd = "Internal"
            args = []

        Internal = Internal()
        """
        REFerence_oscil:Internal

        Arguments:
        """

        class Low(SCPINode, SCPISet):
            """
            REFerence_oscil:Low

            Arguments:
            """
            _cmd = "Low"
            args = []

        Low = Low()
        """
        REFerence_oscil:Low

        Arguments:
        """

    REFerence_oscil = REFerence_oscil()
    """
    REFerence_oscil

    Arguments:
    """

    class REcall(SCPINode, SCPISet):
        """
        REcall

        Arguments: 1
        """
        _cmd = "REcall"
        args = ["1"]

    REcall = REcall()
    """
    REcall

    Arguments: 1
    """

    class ROSCillator(SCPINode, SCPISet):
        """
        ROSCillator

        Arguments:
        """
        _cmd = "ROSCillator"
        args = []

        class CALibration(SCPINode, SCPIQuery, SCPISet):
            """
            ROSCillator:CALibration

            Arguments: 1
            """
            _cmd = "CALibration"
            args = ["1"]

            class STEP(SCPINode):
                """
                ROSCillator:CALibration:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery):
                    """
                    ROSCillator:CALibration:STEP:INCRement

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                ROSCillator:CALibration:STEP:INCRement

                Arguments: 1
                """

            STEP = STEP()
            """
            ROSCillator:CALibration:STEP

            Arguments:
            """

        CALibration = CALibration()
        """
        ROSCillator:CALibration

        Arguments: 1
        """

        class SOURce(SCPINode, SCPIQuery, SCPISet):
            """
            ROSCillator:SOURce

            Arguments: EXTernal, INTernal
            """
            _cmd = "SOURce"
            args = ["EXTernal", "INTernal"]

        SOURce = SOURce()
        """
        ROSCillator:SOURce

        Arguments: EXTernal, INTernal
        """

    ROSCillator = ROSCillator()
    """
    ROSCillator

    Arguments:
    """

    class SEQuence(SCPINode):
        """
        SEQuence

        Arguments:
        """
        _cmd = "SEQuence"
        args = []

        class IMMediate(SCPINode, SCPISet):
            """
            SEQuence:IMMediate

            Arguments:
            """
            _cmd = "IMMediate"
            args = []

        IMMediate = IMMediate()
        """
        SEQuence:IMMediate

        Arguments:
        """

        class REGister(SCPINode, SCPIQuery, SCPISet):
            """
            SEQuence:REGister

            Arguments: <numeric_value>,<numeric_value>
            """
            _cmd = "REGister"
            args = ["<numeric_value>,<numeric_value>"]

        REGister = REGister()
        """
        SEQuence:REGister

        Arguments: <numeric_value>,<numeric_value>
        """

        class STATe(SCPINode, SCPIBool):
            """
            SEQuence:STATe

            Arguments: 1, ON, OFF
            """
            _cmd = "STATe"
            args = ["1", "ON", "OFF"]

        STATe = STATe()
        """
        SEQuence:STATe

        Arguments: 1, ON, OFF
        """

    SEQuence = SEQuence()
    """
    SEQuence

    Arguments:
    """

    class SERVice(SCPINode, SCPISet):
        """
        SERVice

        Arguments:
        """
        _cmd = "SERVice"
        args = []

        class DIRect(SCPINode, SCPISet):
            """
            SERVice:DIRect

            Arguments:
            """
            _cmd = "DIRect"
            args = []

            class COMMand(SCPINode, SCPIQuery, SCPISet):
                """
                SERVice:DIRect:COMMand

                Arguments: 'string'
                """
                _cmd = "COMMand"
                args = ["'string'"]

            COMMand = COMMand()
            """
            SERVice:DIRect:COMMand

            Arguments: 'string'
            """

        DIRect = DIRect()
        """
        SERVice:DIRect

        Arguments:
        """

        class HCOPy(SCPINode):
            """
            SERVice:HCOPy

            Arguments:
            """
            _cmd = "HCOPy"
            args = []

            class EXECute(SCPINode, SCPIQuery, SCPISet):
                """
                SERVice:HCOPy:EXECute

                Arguments:
                """
                _cmd = "EXECute"
                args = []

            EXECute = EXECute()
            """
            SERVice:HCOPy:EXECute

            Arguments:
            """

            class IMAGe(SCPINode):
                """
                SERVice:HCOPy:IMAGe

                Arguments:
                """
                _cmd = "IMAGe"
                args = []

                class FORMat(SCPINode, SCPIQuery, SCPISet):
                    """
                    SERVice:HCOPy:IMAGe:FORMat

                    Arguments: BMP, JPG, PNG, XPM
                    """
                    _cmd = "FORMat"
                    args = ["BMP", "JPG", "PNG", "XPM"]

                FORMat = FORMat()
                """
                SERVice:HCOPy:IMAGe:FORMat

                Arguments: BMP, JPG, PNG, XPM
                """

            IMAGe = IMAGe()
            """
            SERVice:HCOPy:IMAGe

            Arguments:
            """

        HCOPy = HCOPy()
        """
        SERVice:HCOPy

        Arguments:
        """

        class SEQuence(SCPINode, SCPISet):
            """
            SERVice:SEQuence

            Arguments:
            """
            _cmd = "SEQuence"
            args = []

        SEQuence = SEQuence()
        """
        SERVice:SEQuence

        Arguments:
        """

        class SPECial(SCPINode):
            """
            SERVice:SPECial

            Arguments:
            """
            _cmd = "SPECial"
            args = []

            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                SERVice:SPECial:FUNCtion

                Arguments: AA, AB, AM, AP, FA, FB, FM, FR, MF, ML, NONE, PL, PM, ST
                """
                _cmd = "FUNCtion"
                args = ["AA", "AB", "AM", "AP", "FA", "FB", "FM", "FR", "MF", "ML", "NONE", "PL", "PM", "ST"]

            FUNCtion = FUNCtion()
            """
            SERVice:SPECial:FUNCtion

            Arguments: AA, AB, AM, AP, FA, FB, FM, FR, MF, ML, NONE, PL, PM, ST
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SERVice:SPECial:SOURce

                Arguments: NONE, S1, S2, S3
                """
                _cmd = "SOURce"
                args = ["NONE", "S1", "S2", "S3"]

            SOURce = SOURce()
            """
            SERVice:SPECial:SOURce

            Arguments: NONE, S1, S2, S3
            """

        SPECial = SPECial()
        """
        SERVice:SPECial

        Arguments:
        """

        class TALKer(SCPINode, SCPISet):
            """
            SERVice:TALKer

            Arguments:
            """
            _cmd = "TALKer"
            args = []

        TALKer = TALKer()
        """
        SERVice:TALKer

        Arguments:
        """

    SERVice = SERVice()
    """
    SERVice

    Arguments:
    """

    class SEquence(SCPINode, SCPISet):
        """
        SEquence

        Arguments:
        """
        _cmd = "SEquence"
        args = []

    SEquence = SEquence()
    """
    SEquence

    Arguments:
    """

    class SHA2(SCPINodeN, SCPISet):
        """
        SHA2

        Arguments:
        """
        _cmd = "SHA2"
        args = []

    SHA2 = SHA2()
    """
    SHA2

    Arguments:
    """

    class SHS1(SCPINodeN, SCPISet):
        """
        SHS1

        Arguments:
        """
        _cmd = "SHS1"
        args = []

    SHS1 = SHS1()
    """
    SHS1

    Arguments:
    """

    class SHT2(SCPINodeN, SCPISet):
        """
        SHT2

        Arguments:
        """
        _cmd = "SHT2"
        args = []

    SHT2 = SHT2()
    """
    SHT2

    Arguments:
    """

    class SOURce(SCPINode, SCPISet):
        """
        SOURce

        Arguments:
        """
        _cmd = "SOURce"
        args = []

        class AM(SCPINode):
            """
            SOURce:AM

            Arguments:
            """
            _cmd = "AM"
            args = []

            class DEPTh(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:AM:DEPTh

                Arguments: 1
                """
                _cmd = "DEPTh"
                args = ["1"]

                class EXPonential(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:AM:DEPTh:EXPonential
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/39eff2936fd04783.htm#ID_856cf6c5fb4c2e620a00206a0128eeb6-0735468cfb4c20f50a00206a002979ad-en-US>`_

                    Arguments: 1
                    """
                    _cmd = "EXPonential"
                    args = ["1"]

                EXPonential = EXPonential()
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
                    _cmd = "LINear"
                    args = ["1"]

                    class TRACk(SCPINode, SCPIBool):
                        """
                        SOURce:AM:DEPTh:LINear:TRACk

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "TRACk"
                        args = ["1", "ON", "OFF"]

                    TRACk = TRACk()
                    """
                    SOURce:AM:DEPTh:LINear:TRACk

                    Arguments: 1, ON, OFF
                    """

                LINear = LINear()
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
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:AM:DEPTh:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:AM:DEPTh:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:AM:DEPTh:STEP

                Arguments:
                """

            DEPTh = DEPTh()
            """
            SOURce:AM:DEPTh

            Arguments: 1
            """

            class EXTernal(SCPINode, SCPISet):
                """
                SOURce:AM:EXTernal

                Arguments:
                """
                _cmd = "EXTernal"
                args = []

                class COUPling(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:AM:EXTernal:COUPling
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7c57efbe68294ef5.htm#ID_5bcc30cf4d678f970a00206a00fe69d4-c60d3ff74d678f970a00206a0024546d-en-US>`_

                    Arguments: AC, DC
                    """
                    _cmd = "COUPling"
                    args = ["AC", "DC"]

                COUPling = COUPling()
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
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()
                """
                SOURce:AM:EXTernal:IMPedance

                Arguments: 1
                """

            EXTernal = EXTernal()
            """
            SOURce:AM:EXTernal

            Arguments:
            """

            class INTernal(SCPINode, SCPISet):
                """
                SOURce:AM:INTernal

                Arguments:
                """
                _cmd = "INTernal"
                args = []

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:AM:INTernal:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                    class ALTernate(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:AM:INTernal:FREQuency:ALTernate

                        Arguments: 1
                        """
                        _cmd = "ALTernate"
                        args = ["1"]

                        class AMPLitude(SCPINode, SCPISet):
                            """
                            SOURce:AM:INTernal:FREQuency:ALTernate:AMPLitude

                            Arguments:
                            """
                            _cmd = "AMPLitude"
                            args = []

                            class PERCent(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:AM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                                Arguments: 1
                                """
                                _cmd = "PERCent"
                                args = ["1"]

                            PERCent = PERCent()
                            """
                            SOURce:AM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                            Arguments: 1
                            """

                        AMPLitude = AMPLitude()
                        """
                        SOURce:AM:INTernal:FREQuency:ALTernate:AMPLitude

                        Arguments:
                        """

                    ALTernate = ALTernate()
                    """
                    SOURce:AM:INTernal:FREQuency:ALTernate

                    Arguments: 1
                    """

                    class STEP(SCPINode):
                        """
                        SOURce:AM:INTernal:FREQuency:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:AM:INTernal:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:AM:INTernal:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:AM:INTernal:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()
                """
                SOURce:AM:INTernal:FREQuency

                Arguments: 1
                """

                class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:AM:INTernal:FUNCtion

                    Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                    """
                    _cmd = "FUNCtion"
                    args = ["GAUSsian", "NOISe", "RAMP", "SINusoid", "SQUare", "TRIangle", "UNIForm"]

                    class NOISe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:AM:INTernal:FUNCtion:NOISe

                        Arguments: GAUSsian, UNIForm
                        """
                        _cmd = "NOISe"
                        args = ["GAUSsian", "UNIForm"]

                    NOISe = NOISe()
                    """
                    SOURce:AM:INTernal:FUNCtion:NOISe

                    Arguments: GAUSsian, UNIForm
                    """

                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:AM:INTernal:FUNCtion:SHAPe

                        Arguments: SINE, SQUare
                        """
                        _cmd = "SHAPe"
                        args = ["SINE", "SQUare"]

                    SHAPe = SHAPe()
                    """
                    SOURce:AM:INTernal:FUNCtion:SHAPe

                    Arguments: SINE, SQUare
                    """

                FUNCtion = FUNCtion()
                """
                SOURce:AM:INTernal:FUNCtion

                Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                """

                class SWEep(SCPINode, SCPISet):
                    """
                    SOURce:AM:INTernal:SWEep

                    Arguments:
                    """
                    _cmd = "SWEep"
                    args = []

                    class TRIGger(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:AM:INTernal:SWEep:TRIGger

                        Arguments: BUS, EXTernal, IMMediate, KEY
                        """
                        _cmd = "TRIGger"
                        args = ["BUS", "EXTernal", "IMMediate", "KEY"]

                    TRIGger = TRIGger()
                    """
                    SOURce:AM:INTernal:SWEep:TRIGger

                    Arguments: BUS, EXTernal, IMMediate, KEY
                    """

                SWEep = SWEep()
                """
                SOURce:AM:INTernal:SWEep

                Arguments:
                """

            INTernal = INTernal()
            """
            SOURce:AM:INTernal

            Arguments:
            """

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:AM:POLarity

                Arguments: INVerted, NORMal
                """
                _cmd = "POLarity"
                args = ["INVerted", "NORMal"]

            POLarity = POLarity()
            """
            SOURce:AM:POLarity

            Arguments: INVerted, NORMal
            """

            class SCAN(SCPINode):
                """
                SOURce:AM:SCAN

                Arguments:
                """
                _cmd = "SCAN"
                args = []

                class SENSitivity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:AM:SCAN:SENSitivity

                    Arguments: 1
                    """
                    _cmd = "SENSitivity"
                    args = ["1"]

                SENSitivity = SENSitivity()
                """
                SOURce:AM:SCAN:SENSitivity

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:AM:SCAN:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:AM:SCAN:STATe

                Arguments: 1, ON, OFF
                """

            SCAN = SCAN()
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
                _cmd = "SENSitivity"
                args = ["1"]

            SENSitivity = SENSitivity()
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
                _cmd = "SOURce"
                args = ["EXTernal", "INT1", "INT2", "INTernal", "INTernal1", "INTernal2,EXTernal", "INT1", "INTernal", "INTernal1"]

            SOURce = SOURce()
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
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

                class EMULation(SCPINode, SCPIBool):
                    """
                    SOURce:AM:STATe:EMULation

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "EMULation"
                    args = ["1", "ON", "OFF"]

                EMULation = EMULation()
                """
                SOURce:AM:STATe:EMULation

                Arguments: 1, ON, OFF
                """

            STATe = STATe()
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
                _cmd = "WIDeband"
                args = []

                class SENSitivity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:AM:WIDeband:SENSitivity

                    Arguments: 1
                    """
                    _cmd = "SENSitivity"
                    args = ["1"]

                SENSitivity = SENSitivity()
                """
                SOURce:AM:WIDeband:SENSitivity

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:AM:WIDeband:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:AM:WIDeband:STATe

                Arguments: 1, ON, OFF
                """

            WIDeband = WIDeband()
            """
            SOURce:AM:WIDeband

            Arguments:
            """

        AM = AM()
        """
        SOURce:AM

        Arguments:
        """

        class BURSt(SCPINode, SCPISet):
            """
            SOURce:BURSt

            Arguments:
            """
            _cmd = "BURSt"
            args = []

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:BURSt:SOURce

                Arguments: EXTernal, EXTernal1, INTernal, INTernal1
                """
                _cmd = "SOURce"
                args = ["EXTernal", "EXTernal1", "INTernal", "INTernal1"]

            SOURce = SOURce()
            """
            SOURce:BURSt:SOURce

            Arguments: EXTernal, EXTernal1, INTernal, INTernal1
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:BURSt:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SOURce:BURSt:STATe

            Arguments: 1, ON, OFF
            """

        BURSt = BURSt()
        """
        SOURce:BURSt

        Arguments:
        """

        class CORRection(SCPINode):
            """
            SOURce:CORRection

            Arguments:
            """
            _cmd = "CORRection"
            args = []

            class CSET(SCPINode):
                """
                SOURce:CORRection:CSET

                Arguments:
                """
                _cmd = "CSET"
                args = []

                class CATalog(SCPINode, SCPIQuery):
                    """
                    `SOURce:CORRection:CSET:CATalog
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/12dc5f6ae5524347.htm#ID_689cd4137c48ac3e0a00206a018986af-f5c35cc47c48ac3e0a00206a012bc823-en-US>`_

                    Arguments:
                    """
                    _cmd = "CATalog"
                    args = []

                CATalog = CATalog()
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
                    _cmd = "DATA"
                    args = []

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:CORRection:CSET:DATA:FREQuency
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2dda9edb61694671.htm#ID_86873f407c48b1ac0a00206a004443cb-400402547c48b1bc0a00206a012bc823-en-US>`_

                        Arguments: <numeric_value>[HZ, KHZ, MHZ, GHZ],<numeric_value>
                        """
                        _cmd = "FREQuency"
                        args = ["<numeric_value>[HZ", "KHZ", "MHZ", "GHZ],<numeric_value>"]

                        class POINts(SCPINode, SCPIQuery):
                            """
                            `SOURce:CORRection:CSET:DATA:FREQuency:POINts
                            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/4370c89124cc46f2.htm#ID_c0348a7c7c48b72b0a00206a014355d0-7dcc67e17c48b72b0a00206a012bc823-en-US>`_

                            Arguments:
                            """
                            _cmd = "POINts"
                            args = []

                        POINts = POINts()
                        """
                        `SOURce:CORRection:CSET:DATA:FREQuency:POINts
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/4370c89124cc46f2.htm#ID_c0348a7c7c48b72b0a00206a014355d0-7dcc67e17c48b72b0a00206a012bc823-en-US>`_

                        Arguments:
                        """

                    FREQuency = FREQuency()
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
                        _cmd = "POWer"
                        args = ["<numeric_value>[DB],<numeric_value>"]

                        class POINts(SCPINode, SCPIQuery):
                            """
                            `SOURce:CORRection:CSET:DATA:POWer:POINts
                            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3f3849f7fd204e75.htm#ID_2516a43f7c48e2ce0a00206a00fc3ca9-c939d22e7c48e2ce0a00206a012bc823-en-US>`_

                            Arguments:
                            """
                            _cmd = "POINts"
                            args = []

                        POINts = POINts()
                        """
                        `SOURce:CORRection:CSET:DATA:POWer:POINts
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3f3849f7fd204e75.htm#ID_2516a43f7c48e2ce0a00206a00fc3ca9-c939d22e7c48e2ce0a00206a012bc823-en-US>`_

                        Arguments:
                        """

                    POWer = POWer()
                    """
                    `SOURce:CORRection:CSET:DATA:POWer
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/a6ceacf6151845d4.htm#ID_ff0722e77c48bc990a00206a002f7094-dc7cab557c48bc990a00206a012bc823-en-US>`_

                    Arguments: <numeric_value>[DB],<numeric_value>
                    """

                DATA = DATA()
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
                    _cmd = "DELete"
                    args = ["'string'"]

                DELete = DELete()
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
                    _cmd = "SELect"
                    args = ["NONE", "USER1", "USER2", "USER3", "USER4", "USER5"]

                SELect = SELect()
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
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:CORRection:CSET:STATe

                Arguments: 1, ON, OFF
                """

            CSET = CSET()
            """
            SOURce:CORRection:CSET

            Arguments:
            """

            class FLATness(SCPINode):
                """
                SOURce:CORRection:FLATness

                Arguments:
                """
                _cmd = "FLATness"
                args = []

                class POINts(SCPINode, SCPIQuery):
                    """
                    SOURce:CORRection:FLATness:POINts

                    Arguments: 1
                    """
                    _cmd = "POINts"
                    args = ["1"]

                POINts = POINts()
                """
                SOURce:CORRection:FLATness:POINts

                Arguments: 1
                """

                class PRESet(SCPINode, SCPISet):
                    """
                    SOURce:CORRection:FLATness:PRESet

                    Arguments:
                    """
                    _cmd = "PRESet"
                    args = []

                PRESet = PRESet()
                """
                SOURce:CORRection:FLATness:PRESet

                Arguments:
                """

                class STORe(SCPINode, SCPISet):
                    """
                    SOURce:CORRection:FLATness:STORe

                    Arguments: 'string'
                    """
                    _cmd = "STORe"
                    args = ["'string'"]

                STORe = STORe()
                """
                SOURce:CORRection:FLATness:STORe

                Arguments: 'string'
                """

            FLATness = FLATness()
            """
            SOURce:CORRection:FLATness

            Arguments:
            """

            class SOURce(SCPINodeN, SCPIQuery, SCPISet):
                """
                SOURce:CORRection:SOURce

                Arguments: ARRay, FLATness
                """
                _cmd = "SOURce"
                args = ["ARRay", "FLATness"]

            SOURce = SOURce()
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
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            `SOURce:CORRection:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f493e8cd5b304030.htm#ID_bfaa6443312d91020a00206a014d3fc5-07f8da5e312d91020a00206a00c4603c-en-US>`_

            Arguments: 1, ON, OFF
            """

        CORRection = CORRection()
        """
        SOURce:CORRection

        Arguments:
        """

        class DM(SCPINode):
            """
            SOURce:DM

            Arguments:
            """
            _cmd = "DM"
            args = []

            class ASK(SCPINode):
                """
                SOURce:DM:ASK

                Arguments:
                """
                _cmd = "ASK"
                args = []

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:ASK:DEPTh

                    Arguments: 1
                    """
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()
                """
                SOURce:DM:ASK:DEPTh

                Arguments: 1
                """

                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:ASK:POLarity

                    Arguments: INVerted, NORMal
                    """
                    _cmd = "POLarity"
                    args = ["INVerted", "NORMal"]

                POLarity = POLarity()
                """
                SOURce:DM:ASK:POLarity

                Arguments: INVerted, NORMal
                """

            ASK = ASK()
            """
            SOURce:DM:ASK

            Arguments:
            """

            class BBFilter(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:DM:BBFilter

                Arguments: 1
                """
                _cmd = "BBFilter"
                args = ["1"]

            BBFilter = BBFilter()
            """
            SOURce:DM:BBFilter

            Arguments: 1
            """

            class EXTernal(SCPINode, SCPISet):
                """
                SOURce:DM:EXTernal

                Arguments:
                """
                _cmd = "EXTernal"
                args = []

                class ALC(SCPINode):
                    """
                    SOURce:DM:EXTernal:ALC

                    Arguments:
                    """
                    _cmd = "ALC"
                    args = []

                    class BANDwidth(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:EXTernal:ALC:BANDwidth

                        Arguments: <numeric_value>, NARRow, NORMal
                        """
                        _cmd = "BANDwidth"
                        args = ["<numeric_value>", "NARRow", "NORMal"]

                    BANDwidth = BANDwidth()
                    """
                    SOURce:DM:EXTernal:ALC:BANDwidth

                    Arguments: <numeric_value>, NARRow, NORMal
                    """

                    class BWIDth(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:EXTernal:ALC:BWIDth

                        Arguments: <numeric_value>, NARRow, NORMal
                        """
                        _cmd = "BWIDth"
                        args = ["<numeric_value>", "NARRow", "NORMal"]

                    BWIDth = BWIDth()
                    """
                    SOURce:DM:EXTernal:ALC:BWIDth

                    Arguments: <numeric_value>, NARRow, NORMal
                    """

                ALC = ALC()
                """
                SOURce:DM:EXTernal:ALC

                Arguments:
                """

                class FILTer(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:EXTernal:FILTer

                    Arguments: 1
                    """
                    _cmd = "FILTer"
                    args = ["1"]

                FILTer = FILTer()
                """
                SOURce:DM:EXTernal:FILTer

                Arguments: 1
                """

                class HCRest(SCPINode):
                    """
                    SOURce:DM:EXTernal:HCRest

                    Arguments:
                    """
                    _cmd = "HCRest"
                    args = []

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:DM:EXTernal:HCRest:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SOURce:DM:EXTernal:HCRest:STATe

                    Arguments: 1, ON, OFF
                    """

                HCRest = HCRest()
                """
                SOURce:DM:EXTernal:HCRest

                Arguments:
                """

                class HICRest(SCPINode):
                    """
                    SOURce:DM:EXTernal:HICRest

                    Arguments:
                    """
                    _cmd = "HICRest"
                    args = []

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:DM:EXTernal:HICRest:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SOURce:DM:EXTernal:HICRest:STATe

                    Arguments: 1, ON, OFF
                    """

                HICRest = HICRest()
                """
                SOURce:DM:EXTernal:HICRest

                Arguments:
                """

                class IMPedance(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:EXTernal:IMPedance

                    Arguments: 1
                    """
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()
                """
                SOURce:DM:EXTernal:IMPedance

                Arguments: 1
                """

                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:EXTernal:POLarity

                    Arguments: INVert, NORMal
                    """
                    _cmd = "POLarity"
                    args = ["INVert", "NORMal"]

                POLarity = POLarity()
                """
                SOURce:DM:EXTernal:POLarity

                Arguments: INVert, NORMal
                """

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:EXTernal:SOURce

                    Arguments: BBG1, EXT600, EXTernal, INTernal, OFF, SUM
                    """
                    _cmd = "SOURce"
                    args = ["BBG1", "EXT600", "EXTernal", "INTernal", "OFF", "SUM"]

                SOURce = SOURce()
                """
                SOURce:DM:EXTernal:SOURce

                Arguments: BBG1, EXT600, EXTernal, INTernal, OFF, SUM
                """

            EXTernal = EXTernal()
            """
            SOURce:DM:EXTernal

            Arguments:
            """

            class FSK(SCPINode):
                """
                SOURce:DM:FSK

                Arguments:
                """
                _cmd = "FSK"
                args = []

                class DEViation(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:FSK:DEViation

                    Arguments: 1
                    """
                    _cmd = "DEViation"
                    args = ["1"]

                DEViation = DEViation()
                """
                SOURce:DM:FSK:DEViation

                Arguments: 1
                """

                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:FSK:POLarity

                    Arguments: INVerted, NORMal
                    """
                    _cmd = "POLarity"
                    args = ["INVerted", "NORMal"]

                POLarity = POLarity()
                """
                SOURce:DM:FSK:POLarity

                Arguments: INVerted, NORMal
                """

            FSK = FSK()
            """
            SOURce:DM:FSK

            Arguments:
            """

            class IMPairment(SCPINode):
                """
                SOURce:DM:IMPairment

                Arguments:
                """
                _cmd = "IMPairment"
                args = []

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:DM:IMPairment:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:DM:IMPairment:STATe

                Arguments: 1, ON, OFF
                """

            IMPairment = IMPairment()
            """
            SOURce:DM:IMPairment

            Arguments:
            """

            class IQ(SCPINode):
                """
                SOURce:DM:IQ

                Arguments:
                """
                _cmd = "IQ"
                args = []

                class CREStfactor(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQ:CREStfactor

                    Arguments: 1
                    """
                    _cmd = "CREStfactor"
                    args = ["1"]

                CREStfactor = CREStfactor()
                """
                SOURce:DM:IQ:CREStfactor

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:DM:IQ:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:DM:IQ:STATe

                Arguments: 1, ON, OFF
                """

            IQ = IQ()
            """
            SOURce:DM:IQ

            Arguments:
            """

            class IQADjustment(SCPINode):
                """
                SOURce:DM:IQADjustment

                Arguments:
                """
                _cmd = "IQADjustment"
                args = []

                class BBG(SCPINode):
                    """
                    SOURce:DM:IQADjustment:BBG

                    Arguments:
                    """
                    _cmd = "BBG"
                    args = []

                    class QSKew(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:BBG:QSKew

                        Arguments: 1
                        """
                        _cmd = "QSKew"
                        args = ["1"]

                    QSKew = QSKew()
                    """
                    SOURce:DM:IQADjustment:BBG:QSKew

                    Arguments: 1
                    """

                BBG = BBG()
                """
                SOURce:DM:IQADjustment:BBG

                Arguments:
                """

                class DELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQADjustment:DELay

                    Arguments: 1
                    """
                    _cmd = "DELay"
                    args = ["1"]

                DELay = DELay()
                """
                SOURce:DM:IQADjustment:DELay

                Arguments: 1
                """

                class EXTernal(SCPINode, SCPISet):
                    """
                    SOURce:DM:IQADjustment:EXTernal

                    Arguments:
                    """
                    _cmd = "EXTernal"
                    args = []

                    class COFFset(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:COFFset

                        Arguments: 1
                        """
                        _cmd = "COFFset"
                        args = ["1"]

                    COFFset = COFFset()
                    """
                    SOURce:DM:IQADjustment:EXTernal:COFFset

                    Arguments: 1
                    """

                    class DIOFfset(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:DIOFfset

                        Arguments: 1
                        """
                        _cmd = "DIOFfset"
                        args = ["1"]

                    DIOFfset = DIOFfset()
                    """
                    SOURce:DM:IQADjustment:EXTernal:DIOFfset

                    Arguments: 1
                    """

                    class DQOFfset(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:DQOFfset

                        Arguments: 1
                        """
                        _cmd = "DQOFfset"
                        args = ["1"]

                    DQOFfset = DQOFfset()
                    """
                    SOURce:DM:IQADjustment:EXTernal:DQOFfset

                    Arguments: 1
                    """

                    class IOFFset(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:IOFFset

                        Arguments: 1
                        """
                        _cmd = "IOFFset"
                        args = ["1"]

                    IOFFset = IOFFset()
                    """
                    SOURce:DM:IQADjustment:EXTernal:IOFFset

                    Arguments: 1
                    """

                    class IQATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:IQATten

                        Arguments: 1
                        """
                        _cmd = "IQATten"
                        args = ["1"]

                    IQATten = IQATten()
                    """
                    SOURce:DM:IQADjustment:EXTernal:IQATten

                    Arguments: 1
                    """

                    class QOFFset(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:EXTernal:QOFFset

                        Arguments: 1
                        """
                        _cmd = "QOFFset"
                        args = ["1"]

                    QOFFset = QOFFset()
                    """
                    SOURce:DM:IQADjustment:EXTernal:QOFFset

                    Arguments: 1
                    """

                EXTernal = EXTernal()
                """
                SOURce:DM:IQADjustment:EXTernal

                Arguments:
                """

                class IOFFset(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQADjustment:IOFFset

                    Arguments: 1
                    """
                    _cmd = "IOFFset"
                    args = ["1"]

                IOFFset = IOFFset()
                """
                SOURce:DM:IQADjustment:IOFFset

                Arguments: 1
                """

                class QOFFset(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQADjustment:QOFFset

                    Arguments: 1
                    """
                    _cmd = "QOFFset"
                    args = ["1"]

                QOFFset = QOFFset()
                """
                SOURce:DM:IQADjustment:QOFFset

                Arguments: 1
                """

                class QSKew(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQADjustment:QSKew

                    Arguments: 1
                    """
                    _cmd = "QSKew"
                    args = ["1"]

                QSKew = QSKew()
                """
                SOURce:DM:IQADjustment:QSKew

                Arguments: 1
                """

                class SKEW(SCPINode):
                    """
                    SOURce:DM:IQADjustment:SKEW

                    Arguments:
                    """
                    _cmd = "SKEW"
                    args = []

                    class DELay(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:DM:IQADjustment:SKEW:DELay

                        Arguments: 1
                        """
                        _cmd = "DELay"
                        args = ["1"]

                    DELay = DELay()
                    """
                    SOURce:DM:IQADjustment:SKEW:DELay

                    Arguments: 1
                    """

                SKEW = SKEW()
                """
                SOURce:DM:IQADjustment:SKEW

                Arguments:
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:DM:IQADjustment:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:DM:IQADjustment:STATe

                Arguments: 1, ON, OFF
                """

            IQADjustment = IQADjustment()
            """
            SOURce:DM:IQADjustment

            Arguments:
            """

            class IQRatio(SCPINode):
                """
                SOURce:DM:IQRatio

                Arguments:
                """
                _cmd = "IQRatio"
                args = []

                class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:IQRatio:MAGNitude

                    Arguments: 1
                    """
                    _cmd = "MAGNitude"
                    args = ["1"]

                MAGNitude = MAGNitude()
                """
                SOURce:DM:IQRatio:MAGNitude

                Arguments: 1
                """

            IQRatio = IQRatio()
            """
            SOURce:DM:IQRatio

            Arguments:
            """

            class IQSWap(SCPINode):
                """
                SOURce:DM:IQSWap

                Arguments:
                """
                _cmd = "IQSWap"
                args = []

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:DM:IQSWap:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:DM:IQSWap:STATe

                Arguments: 1, ON, OFF
                """

            IQSWap = IQSWap()
            """
            SOURce:DM:IQSWap

            Arguments:
            """

            class LEAKage(SCPINode):
                """
                SOURce:DM:LEAKage

                Arguments:
                """
                _cmd = "LEAKage"
                args = []

                class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:LEAKage:MAGNitude

                    Arguments: 1
                    """
                    _cmd = "MAGNitude"
                    args = ["1"]

                MAGNitude = MAGNitude()
                """
                SOURce:DM:LEAKage:MAGNitude

                Arguments: 1
                """

            LEAKage = LEAKage()
            """
            SOURce:DM:LEAKage

            Arguments:
            """

            class MODulation(SCPINode, SCPISet):
                """
                SOURce:DM:MODulation

                Arguments:
                """
                _cmd = "MODulation"
                args = []

                class ATTen(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:MODulation:ATTen

                    Arguments: 1
                    """
                    _cmd = "ATTen"
                    args = ["1"]

                ATTen = ATTen()
                """
                SOURce:DM:MODulation:ATTen

                Arguments: 1
                """

                class FILTer(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:MODulation:FILTer

                    Arguments: 1
                    """
                    _cmd = "FILTer"
                    args = ["1"]

                FILTer = FILTer()
                """
                SOURce:DM:MODulation:FILTer

                Arguments: 1
                """

            MODulation = MODulation()
            """
            SOURce:DM:MODulation

            Arguments:
            """

            class QUADrature(SCPINode):
                """
                SOURce:DM:QUADrature

                Arguments:
                """
                _cmd = "QUADrature"
                args = []

                class ANGLe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:DM:QUADrature:ANGLe

                    Arguments: 1
                    """
                    _cmd = "ANGLe"
                    args = ["1"]

                ANGLe = ANGLe()
                """
                SOURce:DM:QUADrature:ANGLe

                Arguments: 1
                """

            QUADrature = QUADrature()
            """
            SOURce:DM:QUADrature

            Arguments:
            """

            class SKEW(SCPINode):
                """
                SOURce:DM:SKEW

                Arguments:
                """
                _cmd = "SKEW"
                args = []

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:DM:SKEW:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:DM:SKEW:STATe

                Arguments: 1, ON, OFF
                """

            SKEW = SKEW()
            """
            SOURce:DM:SKEW

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:DM:SOURce

                Arguments: EXTernal, INTernal, SUM
                """
                _cmd = "SOURce"
                args = ["EXTernal", "INTernal", "SUM"]

            SOURce = SOURce()
            """
            SOURce:DM:SOURce

            Arguments: EXTernal, INTernal, SUM
            """

            class SRATio(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:DM:SRATio

                Arguments: 1
                """
                _cmd = "SRATio"
                args = ["1"]

            SRATio = SRATio()
            """
            SOURce:DM:SRATio

            Arguments: 1
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:DM:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SOURce:DM:STATe

            Arguments: 1, ON, OFF
            """

        DM = DM()
        """
        SOURce:DM

        Arguments:
        """

        class FM(SCPINode):
            """
            SOURce:FM

            Arguments:
            """
            _cmd = "FM"
            args = []

            class BANDwidth(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FM:BANDwidth

                Arguments: STANdard, WIDE
                """
                _cmd = "BANDwidth"
                args = ["STANdard", "WIDE"]

            BANDwidth = BANDwidth()
            """
            SOURce:FM:BANDwidth

            Arguments: STANdard, WIDE
            """

            class COUPling(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FM:COUPling

                Arguments: AC, DC
                """
                _cmd = "COUPling"
                args = ["AC", "DC"]

            COUPling = COUPling()
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
                _cmd = "DEViation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:FM:DEViation:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FM:DEViation:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:FM:DEViation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:FM:DEViation:STEP

                Arguments:
                """

                class TRACk(SCPINode, SCPIBool):
                    """
                    SOURce:FM:DEViation:TRACk

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "TRACk"
                    args = ["1", "ON", "OFF"]

                TRACk = TRACk()
                """
                SOURce:FM:DEViation:TRACk

                Arguments: 1, ON, OFF
                """

            DEViation = DEViation()
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
                _cmd = "EXTernal"
                args = []

                class COUPling(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:FM:EXTernal:COUPling
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/713237eac8644509.htm#ID_4fe894544d707f4e0a00206a01cec433-d1c7c3df4d707f4e0a00206a0024546d-en-US>`_

                    Arguments: AC, DC
                    """
                    _cmd = "COUPling"
                    args = ["AC", "DC"]

                COUPling = COUPling()
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
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()
                """
                SOURce:FM:EXTernal:IMPedance

                Arguments: 1
                """

            EXTernal = EXTernal()
            """
            SOURce:FM:EXTernal

            Arguments:
            """

            class FILTer(SCPINode):
                """
                SOURce:FM:FILTer

                Arguments:
                """
                _cmd = "FILTer"
                args = []

                class HPASs(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FM:FILTer:HPASs

                    Arguments: 1
                    """
                    _cmd = "HPASs"
                    args = ["1"]

                HPASs = HPASs()
                """
                SOURce:FM:FILTer:HPASs

                Arguments: 1
                """

            FILTer = FILTer()
            """
            SOURce:FM:FILTer

            Arguments:
            """

            class INTernal(SCPINode, SCPISet):
                """
                SOURce:FM:INTernal

                Arguments:
                """
                _cmd = "INTernal"
                args = []

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FM:INTernal:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                    class ALTernate(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FM:INTernal:FREQuency:ALTernate

                        Arguments: 1
                        """
                        _cmd = "ALTernate"
                        args = ["1"]

                        class AMPLitude(SCPINode, SCPISet):
                            """
                            SOURce:FM:INTernal:FREQuency:ALTernate:AMPLitude

                            Arguments:
                            """
                            _cmd = "AMPLitude"
                            args = []

                            class PERCent(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:FM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                                Arguments: 1
                                """
                                _cmd = "PERCent"
                                args = ["1"]

                            PERCent = PERCent()
                            """
                            SOURce:FM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                            Arguments: 1
                            """

                        AMPLitude = AMPLitude()
                        """
                        SOURce:FM:INTernal:FREQuency:ALTernate:AMPLitude

                        Arguments:
                        """

                    ALTernate = ALTernate()
                    """
                    SOURce:FM:INTernal:FREQuency:ALTernate

                    Arguments: 1
                    """

                    class STEP(SCPINode):
                        """
                        SOURce:FM:INTernal:FREQuency:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:FM:INTernal:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:FM:INTernal:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:FM:INTernal:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()
                """
                SOURce:FM:INTernal:FREQuency

                Arguments: 1
                """

                class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FM:INTernal:FUNCtion

                    Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                    """
                    _cmd = "FUNCtion"
                    args = ["GAUSsian", "NOISe", "RAMP", "SINusoid", "SQUare", "TRIangle", "UNIForm"]

                    class NOISe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FM:INTernal:FUNCtion:NOISe

                        Arguments: GAUSsian, UNIForm
                        """
                        _cmd = "NOISe"
                        args = ["GAUSsian", "UNIForm"]

                    NOISe = NOISe()
                    """
                    SOURce:FM:INTernal:FUNCtion:NOISe

                    Arguments: GAUSsian, UNIForm
                    """

                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FM:INTernal:FUNCtion:SHAPe

                        Arguments: SINE, SQUare
                        """
                        _cmd = "SHAPe"
                        args = ["SINE", "SQUare"]

                    SHAPe = SHAPe()
                    """
                    SOURce:FM:INTernal:FUNCtion:SHAPe

                    Arguments: SINE, SQUare
                    """

                FUNCtion = FUNCtion()
                """
                SOURce:FM:INTernal:FUNCtion

                Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                """

                class SWEep(SCPINode, SCPISet):
                    """
                    SOURce:FM:INTernal:SWEep

                    Arguments:
                    """
                    _cmd = "SWEep"
                    args = []

                    class TRIGger(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FM:INTernal:SWEep:TRIGger

                        Arguments: BUS, EXTernal, IMMediate, KEY
                        """
                        _cmd = "TRIGger"
                        args = ["BUS", "EXTernal", "IMMediate", "KEY"]

                    TRIGger = TRIGger()
                    """
                    SOURce:FM:INTernal:SWEep:TRIGger

                    Arguments: BUS, EXTernal, IMMediate, KEY
                    """

                SWEep = SWEep()
                """
                SOURce:FM:INTernal:SWEep

                Arguments:
                """

            INTernal = INTernal()
            """
            SOURce:FM:INTernal

            Arguments:
            """

            class PREemphasis(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FM:PREemphasis

                Arguments: 1
                """
                _cmd = "PREemphasis"
                args = ["1"]

            PREemphasis = PREemphasis()
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
                _cmd = "SENSitivity"
                args = ["1"]

            SENSitivity = SENSitivity()
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
                _cmd = "SOURce"
                args = ["EXTernal", "INT1", "INT2", "INTernal", "INTernal1", "INTernal2,EXTernal", "INT1", "INTernal", "INTernal1"]

            SOURce = SOURce()
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
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

                class EMULation(SCPINode, SCPIBool):
                    """
                    SOURce:FM:STATe:EMULation

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "EMULation"
                    args = ["1", "ON", "OFF"]

                EMULation = EMULation()
                """
                SOURce:FM:STATe:EMULation

                Arguments: 1, ON, OFF
                """

            STATe = STATe()
            """
            `SOURce:FM:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bfc4735fb97e4afb.htm#ID_56f39a7a4d708c000a00206a00870c91-8d7d16d14d708c000a00206a0024546d-en-US>`_

            Arguments: 1, ON, OFF
            """

        FM = FM()
        """
        SOURce:FM

        Arguments:
        """

        class FREQuency(SCPINode, SCPISet):
            """
            SOURce:FREQuency

            Arguments:
            """
            _cmd = "FREQuency"
            args = []

            class CENTer(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:CENTer
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2cf6c143b3cf4c4b.htm#ID_94b28e8271966ef30a00206a004b06bb-b020ee7271966ef30a00206a012bc823-en-US>`_

                Arguments: 1
                """
                _cmd = "CENTer"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:CENTer:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:CENTer:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:FREQuency:CENTer:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:FREQuency:CENTer:STEP

                Arguments:
                """

            CENTer = CENTer()
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
                _cmd = "CHANnels"
                args = []

                class NUMBer(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FREQuency:CHANnels:NUMBer

                    Arguments: 1
                    """
                    _cmd = "NUMBer"
                    args = ["1"]

                NUMBer = NUMBer()
                """
                SOURce:FREQuency:CHANnels:NUMBer

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:FREQuency:CHANnels:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:FREQuency:CHANnels:STATe

                Arguments: 1, ON, OFF
                """

            CHANnels = CHANnels()
            """
            SOURce:FREQuency:CHANnels

            Arguments:
            """

            class CW(SCPINode):
                """
                SOURce:FREQuency:CW

                Arguments:
                """
                _cmd = "CW"
                args = []

                class BACKup(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FREQuency:CW:BACKup

                    Arguments: 1
                    """
                    _cmd = "BACKup"
                    args = ["1"]

                BACKup = BACKup()
                """
                SOURce:FREQuency:CW:BACKup

                Arguments: 1
                """

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:CW:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:CW:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:FREQuency:CW:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:FREQuency:CW:STEP

                Arguments:
                """

            CW = CW()
            """
            SOURce:FREQuency:CW

            Arguments:
            """

            class ERANge(SCPINode, SCPIBool):
                """
                SOURce:FREQuency:ERANge

                Arguments: 1, ON, OFF
                """
                _cmd = "ERANge"
                args = ["1", "ON", "OFF"]

            ERANge = ERANge()
            """
            SOURce:FREQuency:ERANge

            Arguments: 1, ON, OFF
            """

            class FIXed(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FREQuency:FIXed

                Arguments: 1
                """
                _cmd = "FIXed"
                args = ["1"]

                class BACKup(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:FREQuency:FIXed:BACKup

                    Arguments: 1
                    """
                    _cmd = "BACKup"
                    args = ["1"]

                BACKup = BACKup()
                """
                SOURce:FREQuency:FIXed:BACKup

                Arguments: 1
                """

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:FIXed:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:FIXed:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:FREQuency:FIXed:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:FREQuency:FIXed:STEP

                Arguments:
                """

            FIXed = FIXed()
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
                _cmd = "MANual"
                args = ["1"]

            MANual = MANual()
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
                _cmd = "MULTiplier"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:FREQuency:MULTiplier:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:FREQuency:MULTiplier:STATe

                Arguments: 1, ON, OFF
                """

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:MULTiplier:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:MULTiplier:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:FREQuency:MULTiplier:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:FREQuency:MULTiplier:STEP

                Arguments:
                """

            MULTiplier = MULTiplier()
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
                _cmd = "OFFSet"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:FREQuency:OFFSet:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:FREQuency:OFFSet:STATe

                Arguments: 1, ON, OFF
                """

            OFFSet = OFFSet()
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
                _cmd = "PHASe"
                args = []

                class CONTinuous(SCPINode, SCPISet):
                    """
                    SOURce:FREQuency:PHASe:CONTinuous

                    Arguments:
                    """
                    _cmd = "CONTinuous"
                    args = []

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:FREQuency:PHASe:CONTinuous:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SOURce:FREQuency:PHASe:CONTinuous:STATe

                    Arguments: 1, ON, OFF
                    """

                CONTinuous = CONTinuous()
                """
                SOURce:FREQuency:PHASe:CONTinuous

                Arguments:
                """

            PHASe = PHASe()
            """
            SOURce:FREQuency:PHASe

            Arguments:
            """

            class REFerence(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FREQuency:REFerence

                Arguments: 1
                """
                _cmd = "REFerence"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:FREQuency:REFerence:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:FREQuency:REFerence:STATe

                Arguments: 1, ON, OFF
                """

            REFerence = REFerence()
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
                _cmd = "SPAN"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:SPAN:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:SPAN:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:FREQuency:SPAN:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:FREQuency:SPAN:STEP

                Arguments:
                """

            SPAN = SPAN()
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
                _cmd = "STARt"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:STARt:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:STARt:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:FREQuency:STARt:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:FREQuency:STARt:STEP

                Arguments:
                """

            STARt = STARt()
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
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:FREQuency:STEP:INCRement
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/86e6c5f55e234c7f.htm#ID_89eaa7f5719647a40a00206a01cdb994-b088125d719647a40a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                INCRement = INCRement()
                """
                `SOURce:FREQuency:STEP:INCRement
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/86e6c5f55e234c7f.htm#ID_89eaa7f5719647a40a00206a01cdb994-b088125d719647a40a00206a012bc823-en-US>`_

                Arguments: 1
                """

            STEP = STEP()
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
                _cmd = "STOP"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:FREQuency:STOP:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:STOP:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:FREQuency:STOP:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:FREQuency:STOP:STEP

                Arguments:
                """

            STOP = STOP()
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
                _cmd = "SYNThesis"
                args = ["1"]

            SYNThesis = SYNThesis()
            """
            SOURce:FREQuency:SYNThesis

            Arguments: 1
            """

        FREQuency = FREQuency()
        """
        SOURce:FREQuency

        Arguments:
        """

        class FUNCtion(SCPINode):
            """
            SOURce:FUNCtion

            Arguments:
            """
            _cmd = "FUNCtion"
            args = []

            class SHAPe(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FUNCtion:SHAPe

                Arguments: PRNoise, SAWTooth, SINusoid, SQUare, TRIangle
                """
                _cmd = "SHAPe"
                args = ["PRNoise", "SAWTooth", "SINusoid", "SQUare", "TRIangle"]

            SHAPe = SHAPe()
            """
            SOURce:FUNCtion:SHAPe

            Arguments: PRNoise, SAWTooth, SINusoid, SQUare, TRIangle
            """

        FUNCtion = FUNCtion()
        """
        SOURce:FUNCtion

        Arguments:
        """

        class ILS(SCPINode):
            """
            SOURce:ILS

            Arguments:
            """
            _cmd = "ILS"
            args = []

            class GS(SCPINode):
                """
                SOURce:ILS:GS

                Arguments:
                """
                _cmd = "GS"
                args = []

                class COMid(SCPINode):
                    """
                    SOURce:ILS:GS:COMid

                    Arguments:
                    """
                    _cmd = "COMid"
                    args = []

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:COMid:DEPTh

                        Arguments: 1
                        """
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()
                    """
                    SOURce:ILS:GS:COMid:DEPTh

                    Arguments: 1
                    """

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:COMid:FREQuency

                        Arguments: 1
                        """
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()
                    """
                    SOURce:ILS:GS:COMid:FREQuency

                    Arguments: 1
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:ILS:GS:COMid:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SOURce:ILS:GS:COMid:STATe

                    Arguments: 1, ON, OFF
                    """

                COMid = COMid()
                """
                SOURce:ILS:GS:COMid

                Arguments:
                """

                class DDM(SCPINode):
                    """
                    SOURce:ILS:GS:DDM

                    Arguments:
                    """
                    _cmd = "DDM"
                    args = []

                    class CURRent(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:DDM:CURRent

                        Arguments: 1
                        """
                        _cmd = "CURRent"
                        args = ["1"]

                    CURRent = CURRent()
                    """
                    SOURce:ILS:GS:DDM:CURRent

                    Arguments: 1
                    """

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:DDM:DEPTh

                        Arguments: 1
                        """
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()
                    """
                    SOURce:ILS:GS:DDM:DEPTh

                    Arguments: 1
                    """

                    class DIRection(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:DDM:DIRection

                        Arguments: DOWN, UP
                        """
                        _cmd = "DIRection"
                        args = ["DOWN", "UP"]

                    DIRection = DIRection()
                    """
                    SOURce:ILS:GS:DDM:DIRection

                    Arguments: DOWN, UP
                    """

                    class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:DDM:LOGarithmic

                        Arguments: 1
                        """
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()
                    """
                    SOURce:ILS:GS:DDM:LOGarithmic

                    Arguments: 1
                    """

                DDM = DDM()
                """
                SOURce:ILS:GS:DDM

                Arguments:
                """

                class LLOBe(SCPINode):
                    """
                    SOURce:ILS:GS:LLOBe

                    Arguments:
                    """
                    _cmd = "LLOBe"
                    args = []

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:LLOBe:FREQuency

                        Arguments: 1
                        """
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()
                    """
                    SOURce:ILS:GS:LLOBe:FREQuency

                    Arguments: 1
                    """

                LLOBe = LLOBe()
                """
                SOURce:ILS:GS:LLOBe

                Arguments:
                """

                class PHASe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GS:PHASe

                    Arguments: 1
                    """
                    _cmd = "PHASe"
                    args = ["1"]

                PHASe = PHASe()
                """
                SOURce:ILS:GS:PHASe

                Arguments: 1
                """

                class PRESet(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GS:PRESet

                    Arguments:
                    """
                    _cmd = "PRESet"
                    args = []

                PRESet = PRESet()
                """
                SOURce:ILS:GS:PRESet

                Arguments:
                """

                class SODepth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GS:SODepth

                    Arguments: 1
                    """
                    _cmd = "SODepth"
                    args = ["1"]

                SODepth = SODepth()
                """
                SOURce:ILS:GS:SODepth

                Arguments: 1
                """

                class ULOBe(SCPINode):
                    """
                    SOURce:ILS:GS:ULOBe

                    Arguments:
                    """
                    _cmd = "ULOBe"
                    args = []

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GS:ULOBe:FREQuency

                        Arguments: 1
                        """
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()
                    """
                    SOURce:ILS:GS:ULOBe:FREQuency

                    Arguments: 1
                    """

                ULOBe = ULOBe()
                """
                SOURce:ILS:GS:ULOBe

                Arguments:
                """

            GS = GS()
            """
            SOURce:ILS:GS

            Arguments:
            """

            class GSLope(SCPINode):
                """
                SOURce:ILS:GSLope

                Arguments:
                """
                _cmd = "GSLope"
                args = []

                class COMid(SCPINode):
                    """
                    SOURce:ILS:GSLope:COMid

                    Arguments:
                    """
                    _cmd = "COMid"
                    args = []

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:COMid:DEPTh

                        Arguments: 1
                        """
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()
                    """
                    SOURce:ILS:GSLope:COMid:DEPTh

                    Arguments: 1
                    """

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:COMid:FREQuency

                        Arguments: 1
                        """
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()
                    """
                    SOURce:ILS:GSLope:COMid:FREQuency

                    Arguments: 1
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:ILS:GSLope:COMid:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SOURce:ILS:GSLope:COMid:STATe

                    Arguments: 1, ON, OFF
                    """

                COMid = COMid()
                """
                SOURce:ILS:GSLope:COMid

                Arguments:
                """

                class DDM(SCPINode):
                    """
                    SOURce:ILS:GSLope:DDM

                    Arguments:
                    """
                    _cmd = "DDM"
                    args = []

                    class CURRent(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:DDM:CURRent

                        Arguments: 1
                        """
                        _cmd = "CURRent"
                        args = ["1"]

                    CURRent = CURRent()
                    """
                    SOURce:ILS:GSLope:DDM:CURRent

                    Arguments: 1
                    """

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:DDM:DEPTh

                        Arguments: 1
                        """
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()
                    """
                    SOURce:ILS:GSLope:DDM:DEPTh

                    Arguments: 1
                    """

                    class DIRection(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:DDM:DIRection

                        Arguments: DOWN, UP
                        """
                        _cmd = "DIRection"
                        args = ["DOWN", "UP"]

                    DIRection = DIRection()
                    """
                    SOURce:ILS:GSLope:DDM:DIRection

                    Arguments: DOWN, UP
                    """

                    class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:DDM:LOGarithmic

                        Arguments: 1
                        """
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()
                    """
                    SOURce:ILS:GSLope:DDM:LOGarithmic

                    Arguments: 1
                    """

                DDM = DDM()
                """
                SOURce:ILS:GSLope:DDM

                Arguments:
                """

                class LLOBe(SCPINode):
                    """
                    SOURce:ILS:GSLope:LLOBe

                    Arguments:
                    """
                    _cmd = "LLOBe"
                    args = []

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:LLOBe:FREQuency

                        Arguments: 1
                        """
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()
                    """
                    SOURce:ILS:GSLope:LLOBe:FREQuency

                    Arguments: 1
                    """

                LLOBe = LLOBe()
                """
                SOURce:ILS:GSLope:LLOBe

                Arguments:
                """

                class PHASe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GSLope:PHASe

                    Arguments: 1
                    """
                    _cmd = "PHASe"
                    args = ["1"]

                PHASe = PHASe()
                """
                SOURce:ILS:GSLope:PHASe

                Arguments: 1
                """

                class PRESet(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GSLope:PRESet

                    Arguments:
                    """
                    _cmd = "PRESet"
                    args = []

                PRESet = PRESet()
                """
                SOURce:ILS:GSLope:PRESet

                Arguments:
                """

                class SODepth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:GSLope:SODepth

                    Arguments: 1
                    """
                    _cmd = "SODepth"
                    args = ["1"]

                SODepth = SODepth()
                """
                SOURce:ILS:GSLope:SODepth

                Arguments: 1
                """

                class ULOBe(SCPINode):
                    """
                    SOURce:ILS:GSLope:ULOBe

                    Arguments:
                    """
                    _cmd = "ULOBe"
                    args = []

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:GSLope:ULOBe:FREQuency

                        Arguments: 1
                        """
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()
                    """
                    SOURce:ILS:GSLope:ULOBe:FREQuency

                    Arguments: 1
                    """

                ULOBe = ULOBe()
                """
                SOURce:ILS:GSLope:ULOBe

                Arguments:
                """

            GSLope = GSLope()
            """
            SOURce:ILS:GSLope

            Arguments:
            """

            class LOCalizer(SCPINode):
                """
                SOURce:ILS:LOCalizer

                Arguments:
                """
                _cmd = "LOCalizer"
                args = []

                class COMid(SCPINode):
                    """
                    SOURce:ILS:LOCalizer:COMid

                    Arguments:
                    """
                    _cmd = "COMid"
                    args = []

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:COMid:DEPTh

                        Arguments: 1
                        """
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()
                    """
                    SOURce:ILS:LOCalizer:COMid:DEPTh

                    Arguments: 1
                    """

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:COMid:FREQuency

                        Arguments: 1
                        """
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()
                    """
                    SOURce:ILS:LOCalizer:COMid:FREQuency

                    Arguments: 1
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:ILS:LOCalizer:COMid:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SOURce:ILS:LOCalizer:COMid:STATe

                    Arguments: 1, ON, OFF
                    """

                COMid = COMid()
                """
                SOURce:ILS:LOCalizer:COMid

                Arguments:
                """

                class DDM(SCPINode):
                    """
                    SOURce:ILS:LOCalizer:DDM

                    Arguments:
                    """
                    _cmd = "DDM"
                    args = []

                    class CURRent(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:DDM:CURRent

                        Arguments: 1
                        """
                        _cmd = "CURRent"
                        args = ["1"]

                    CURRent = CURRent()
                    """
                    SOURce:ILS:LOCalizer:DDM:CURRent

                    Arguments: 1
                    """

                    class DEPTh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:DDM:DEPTh

                        Arguments: 1
                        """
                        _cmd = "DEPTh"
                        args = ["1"]

                    DEPTh = DEPTh()
                    """
                    SOURce:ILS:LOCalizer:DDM:DEPTh

                    Arguments: 1
                    """

                    class DIRection(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:DDM:DIRection

                        Arguments: LEFT, RIGHt
                        """
                        _cmd = "DIRection"
                        args = ["LEFT", "RIGHt"]

                    DIRection = DIRection()
                    """
                    SOURce:ILS:LOCalizer:DDM:DIRection

                    Arguments: LEFT, RIGHt
                    """

                    class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:DDM:LOGarithmic

                        Arguments: 1
                        """
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()
                    """
                    SOURce:ILS:LOCalizer:DDM:LOGarithmic

                    Arguments: 1
                    """

                DDM = DDM()
                """
                SOURce:ILS:LOCalizer:DDM

                Arguments:
                """

                class LLOBe(SCPINode):
                    """
                    SOURce:ILS:LOCalizer:LLOBe

                    Arguments:
                    """
                    _cmd = "LLOBe"
                    args = []

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:LLOBe:FREQuency

                        Arguments: 1
                        """
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()
                    """
                    SOURce:ILS:LOCalizer:LLOBe:FREQuency

                    Arguments: 1
                    """

                LLOBe = LLOBe()
                """
                SOURce:ILS:LOCalizer:LLOBe

                Arguments:
                """

                class PHASe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:LOCalizer:PHASe

                    Arguments: 1
                    """
                    _cmd = "PHASe"
                    args = ["1"]

                PHASe = PHASe()
                """
                SOURce:ILS:LOCalizer:PHASe

                Arguments: 1
                """

                class PRESet(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:LOCalizer:PRESet

                    Arguments:
                    """
                    _cmd = "PRESet"
                    args = []

                PRESet = PRESet()
                """
                SOURce:ILS:LOCalizer:PRESet

                Arguments:
                """

                class RLOBe(SCPINode):
                    """
                    SOURce:ILS:LOCalizer:RLOBe

                    Arguments:
                    """
                    _cmd = "RLOBe"
                    args = []

                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:ILS:LOCalizer:RLOBe:FREQuency

                        Arguments: 1
                        """
                        _cmd = "FREQuency"
                        args = ["1"]

                    FREQuency = FREQuency()
                    """
                    SOURce:ILS:LOCalizer:RLOBe:FREQuency

                    Arguments: 1
                    """

                RLOBe = RLOBe()
                """
                SOURce:ILS:LOCalizer:RLOBe

                Arguments:
                """

                class SODepth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ILS:LOCalizer:SODepth

                    Arguments: 1
                    """
                    _cmd = "SODepth"
                    args = ["1"]

                SODepth = SODepth()
                """
                SOURce:ILS:LOCalizer:SODepth

                Arguments: 1
                """

            LOCalizer = LOCalizer()
            """
            SOURce:ILS:LOCalizer

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:ILS:SOURce

                Arguments: INT2, INTernal2,EXTernal
                """
                _cmd = "SOURce"
                args = ["INT2", "INTernal2,EXTernal"]

            SOURce = SOURce()
            """
            SOURce:ILS:SOURce

            Arguments: INT2, INTernal2,EXTernal
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:ILS:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SOURce:ILS:STATe

            Arguments: 1, ON, OFF
            """

        ILS = ILS()
        """
        SOURce:ILS

        Arguments:
        """

        class LFOutput(SCPINode, SCPISet):
            """
            SOURce:LFOutput

            Arguments:
            """
            _cmd = "LFOutput"
            args = []

            class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:LFOutput:AMPLitude

                Arguments: 1
                """
                _cmd = "AMPLitude"
                args = ["1"]

            AMPLitude = AMPLitude()
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
                _cmd = "FREQuency"
                args = ["1"]

            FREQuency = FREQuency()
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
                _cmd = "FUNCtion"
                args = []

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:LFOutput:FUNCtion:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                    class ALTernate(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:LFOutput:FUNCtion:FREQuency:ALTernate

                        Arguments: 1
                        """
                        _cmd = "ALTernate"
                        args = ["1"]

                        class AMPLitude(SCPINode, SCPISet):
                            """
                            SOURce:LFOutput:FUNCtion:FREQuency:ALTernate:AMPLitude

                            Arguments:
                            """
                            _cmd = "AMPLitude"
                            args = []

                            class PERCent(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:LFOutput:FUNCtion:FREQuency:ALTernate:AMPLitude:PERCent

                                Arguments: 1
                                """
                                _cmd = "PERCent"
                                args = ["1"]

                            PERCent = PERCent()
                            """
                            SOURce:LFOutput:FUNCtion:FREQuency:ALTernate:AMPLitude:PERCent

                            Arguments: 1
                            """

                        AMPLitude = AMPLitude()
                        """
                        SOURce:LFOutput:FUNCtion:FREQuency:ALTernate:AMPLitude

                        Arguments:
                        """

                    ALTernate = ALTernate()
                    """
                    SOURce:LFOutput:FUNCtion:FREQuency:ALTernate

                    Arguments: 1
                    """

                    class STEP(SCPINode):
                        """
                        SOURce:LFOutput:FUNCtion:FREQuency:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:LFOutput:FUNCtion:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:LFOutput:FUNCtion:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:LFOutput:FUNCtion:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()
                """
                SOURce:LFOutput:FUNCtion:FREQuency

                Arguments: 1
                """

                class PERiod(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:LFOutput:FUNCtion:PERiod

                    Arguments: 1
                    """
                    _cmd = "PERiod"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:LFOutput:FUNCtion:PERiod:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:LFOutput:FUNCtion:PERiod:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:LFOutput:FUNCtion:PERiod:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:LFOutput:FUNCtion:PERiod:STEP

                    Arguments:
                    """

                PERiod = PERiod()
                """
                SOURce:LFOutput:FUNCtion:PERiod

                Arguments: 1
                """

                class PWIDth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:LFOutput:FUNCtion:PWIDth

                    Arguments: 1
                    """
                    _cmd = "PWIDth"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:LFOutput:FUNCtion:PWIDth:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:LFOutput:FUNCtion:PWIDth:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:LFOutput:FUNCtion:PWIDth:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:LFOutput:FUNCtion:PWIDth:STEP

                    Arguments:
                    """

                PWIDth = PWIDth()
                """
                SOURce:LFOutput:FUNCtion:PWIDth

                Arguments: 1
                """

                class SHAPe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:LFOutput:FUNCtion:SHAPe

                    Arguments: DUALsine, NOISe, RAMP, SINE, SQUare, SWEPtsine, TRIangle
                    """
                    _cmd = "SHAPe"
                    args = ["DUALsine", "NOISe", "RAMP", "SINE", "SQUare", "SWEPtsine", "TRIangle"]

                    class NOISe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:LFOutput:FUNCtion:SHAPe:NOISe

                        Arguments: GAUSsian, UNIForm
                        """
                        _cmd = "NOISe"
                        args = ["GAUSsian", "UNIForm"]

                    NOISe = NOISe()
                    """
                    SOURce:LFOutput:FUNCtion:SHAPe:NOISe

                    Arguments: GAUSsian, UNIForm
                    """

                SHAPe = SHAPe()
                """
                SOURce:LFOutput:FUNCtion:SHAPe

                Arguments: DUALsine, NOISe, RAMP, SINE, SQUare, SWEPtsine, TRIangle
                """

                class SWEep(SCPINode, SCPISet):
                    """
                    SOURce:LFOutput:FUNCtion:SWEep

                    Arguments:
                    """
                    _cmd = "SWEep"
                    args = []

                    class TRIGger(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:LFOutput:FUNCtion:SWEep:TRIGger

                        Arguments: BUS, EXTernal, IMMediate, KEY
                        """
                        _cmd = "TRIGger"
                        args = ["BUS", "EXTernal", "IMMediate", "KEY"]

                    TRIGger = TRIGger()
                    """
                    SOURce:LFOutput:FUNCtion:SWEep:TRIGger

                    Arguments: BUS, EXTernal, IMMediate, KEY
                    """

                SWEep = SWEep()
                """
                SOURce:LFOutput:FUNCtion:SWEep

                Arguments:
                """

            FUNCtion = FUNCtion()
            """
            SOURce:LFOutput:FUNCtion

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:LFOutput:SOURce

                Arguments: FUNC1, FUNC2, FUNCtion1, FUNCtion2, INT1, INT2, INTernal, INTernal1, INTernal2
                """
                _cmd = "SOURce"
                args = ["FUNC1", "FUNC2", "FUNCtion1", "FUNCtion2", "INT1", "INT2", "INTernal", "INTernal1", "INTernal2"]

            SOURce = SOURce()
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
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
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
                _cmd = "VOLTage"
                args = ["1"]

            VOLTage = VOLTage()
            """
            `SOURce:LFOutput:VOLTage
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/30f4a928cfb244ff.htm#ID_0aac7ff171a373a10a00206a0151df63-2edc927371a373a10a00206a012bc823-en-US>`_

            Arguments: 1
            """

        LFOutput = LFOutput()
        """
        SOURce:LFOutput

        Arguments:
        """

        class LIST(SCPINode, SCPISet):
            """
            SOURce:LIST

            Arguments:
            """
            _cmd = "LIST"
            args = []

            class CALCulate(SCPINode, SCPISet):
                """
                SOURce:LIST:CALCulate

                Arguments:
                """
                _cmd = "CALCulate"
                args = []

            CALCulate = CALCulate()
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
                _cmd = "CATalog"
                args = []

            CATalog = CATalog()
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
                _cmd = "CPOint"
                args = []

            CPOint = CPOint()
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
                _cmd = "DELete"
                args = ["'string'"]

            DELete = DELete()
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
                _cmd = "DIRection"
                args = ["DOWN", "UP"]

            DIRection = DIRection()
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
                _cmd = "DWELl"
                args = ["<numeric_value>[S", "MS", "US", "NS],<numeric_value>"]

                class POINts(SCPINode, SCPIQuery):
                    """
                    SOURce:LIST:DWELl:POINts

                    Arguments:
                    """
                    _cmd = "POINts"
                    args = []

                POINts = POINts()
                """
                SOURce:LIST:DWELl:POINts

                Arguments:
                """

            DWELl = DWELl()
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
                _cmd = "FREQuency"
                args = ["<numeric_value>[HZ", "KHZ", "MHZ", "GHZ],<numeric_value>"]

                class POINts(SCPINode, SCPIQuery):
                    """
                    `SOURce:LIST:FREQuency:POINts
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7d65b1dd057049b7.htm#ID_b69a536c7ba3073d0a00206a000d2789-99c66bd67ba3073d0a00206a012bc823-en-US>`_

                    Arguments:
                    """
                    _cmd = "POINts"
                    args = []

                POINts = POINts()
                """
                `SOURce:LIST:FREQuency:POINts
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7d65b1dd057049b7.htm#ID_b69a536c7ba3073d0a00206a000d2789-99c66bd67ba3073d0a00206a012bc823-en-US>`_

                Arguments:
                """

            FREQuency = FREQuency()
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
                _cmd = "INDex"
                args = ["1"]

            INDex = INDex()
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
                _cmd = "LEARn"
                args = []

            LEARn = LEARn()
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
                _cmd = "MANual"
                args = ["1"]

            MANual = MANual()
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
                _cmd = "POWer"
                args = ["<numeric_value>[DB],<numeric_value>"]

                class CORRection(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:LIST:POWer:CORRection

                    Arguments: <numeric_value>[DB],<numeric_value>
                    """
                    _cmd = "CORRection"
                    args = ["<numeric_value>[DB],<numeric_value>"]

                    class POINts(SCPINode, SCPIQuery):
                        """
                        SOURce:LIST:POWer:CORRection:POINts

                        Arguments:
                        """
                        _cmd = "POINts"
                        args = []

                    POINts = POINts()
                    """
                    SOURce:LIST:POWer:CORRection:POINts

                    Arguments:
                    """

                CORRection = CORRection()
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
                    _cmd = "POINts"
                    args = []

                POINts = POINts()
                """
                `SOURce:LIST:POWer:POINts
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f55e6d6622054b99.htm#ID_0ad5bbbe7ba30c8d0a00206a002bb3bd-db2157e07ba30c8d0a00206a012bc823-en-US>`_

                Arguments:
                """

            POWer = POWer()
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
                _cmd = "RETRace"
                args = ["1", "ON", "OFF"]

            RETRace = RETRace()
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
                _cmd = "SELect"
                args = ["'string'"]

            SELect = SELect()
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
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()
            """
            SOURce:LIST:STARt

            Arguments: 1
            """

            class TRIGger(SCPINode, SCPISet):
                """
                SOURce:LIST:TRIGger

                Arguments:
                """
                _cmd = "TRIGger"
                args = []

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:LIST:TRIGger:SOURce
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/c1a4677a84944212.htm#ID_e26ff7bb7ba338dc0a00206a01f83843-c7753eb97ba338dc0a00206a012bc823-en-US>`_

                    Arguments: BUS, EXTernal, IMMediate, KEY
                    """
                    _cmd = "SOURce"
                    args = ["BUS", "EXTernal", "IMMediate", "KEY"]

                SOURce = SOURce()
                """
                `SOURce:LIST:TRIGger:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/c1a4677a84944212.htm#ID_e26ff7bb7ba338dc0a00206a01f83843-c7753eb97ba338dc0a00206a012bc823-en-US>`_

                Arguments: BUS, EXTernal, IMMediate, KEY
                """

            TRIGger = TRIGger()
            """
            SOURce:LIST:TRIGger

            Arguments:
            """

            class TYPE(SCPINode):
                """
                SOURce:LIST:TYPE

                Arguments:
                """
                _cmd = "TYPE"
                args = []

                class LIST(SCPINode):
                    """
                    SOURce:LIST:TYPE:LIST

                    Arguments:
                    """
                    _cmd = "LIST"
                    args = []

                    class INITialize(SCPINode, SCPISet):
                        """
                        SOURce:LIST:TYPE:LIST:INITialize

                        Arguments:
                        """
                        _cmd = "INITialize"
                        args = []

                        class FSTep(SCPINode, SCPISet):
                            """
                            SOURce:LIST:TYPE:LIST:INITialize:FSTep

                            Arguments:
                            """
                            _cmd = "FSTep"
                            args = []

                        FSTep = FSTep()
                        """
                        SOURce:LIST:TYPE:LIST:INITialize:FSTep

                        Arguments:
                        """

                        class PRESet(SCPINode, SCPISet):
                            """
                            SOURce:LIST:TYPE:LIST:INITialize:PRESet

                            Arguments:
                            """
                            _cmd = "PRESet"
                            args = []

                        PRESet = PRESet()
                        """
                        SOURce:LIST:TYPE:LIST:INITialize:PRESet

                        Arguments:
                        """

                    INITialize = INITialize()
                    """
                    SOURce:LIST:TYPE:LIST:INITialize

                    Arguments:
                    """

                LIST = LIST()
                """
                SOURce:LIST:TYPE:LIST

                Arguments:
                """

            TYPE = TYPE()
            """
            SOURce:LIST:TYPE

            Arguments:
            """

        LIST = LIST()
        """
        SOURce:LIST

        Arguments:
        """

        class MARKer(SCPINodeN, SCPISet):
            """
            SOURce:MARKer

            Arguments:
            """
            _cmd = "MARKer"
            args = []

            class AMPLitude(SCPINode):
                """
                SOURce:MARKer:AMPLitude

                Arguments:
                """
                _cmd = "AMPLitude"
                args = []

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:MARKer:AMPLitude:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:MARKer:AMPLitude:STATe

                Arguments: 1, ON, OFF
                """

                class VALue(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MARKer:AMPLitude:VALue

                    Arguments: 1
                    """
                    _cmd = "VALue"
                    args = ["1"]

                VALue = VALue()
                """
                SOURce:MARKer:AMPLitude:VALue

                Arguments: 1
                """

            AMPLitude = AMPLitude()
            """
            SOURce:MARKer:AMPLitude

            Arguments:
            """

            class DELTa(SCPINode, SCPIQuery):
                """
                SOURce:MARKer:DELTa

                Arguments: <numeric_value>,<numeric_value>
                """
                _cmd = "DELTa"
                args = ["<numeric_value>,<numeric_value>"]

            DELTa = DELTa()
            """
            SOURce:MARKer:DELTa

            Arguments: <numeric_value>,<numeric_value>
            """

            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:MARKer:FREQuency

                Arguments: 1
                """
                _cmd = "FREQuency"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:MARKer:FREQuency:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:MARKer:FREQuency:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:MARKer:FREQuency:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:MARKer:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()
            """
            SOURce:MARKer:FREQuency

            Arguments: 1
            """

            class FSWeep(SCPINode):
                """
                SOURce:MARKer:FSWeep

                Arguments:
                """
                _cmd = "FSWeep"
                args = []

                class AMPLitude(SCPINode, SCPIBool):
                    """
                    SOURce:MARKer:FSWeep:AMPLitude

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "AMPLitude"
                    args = ["1", "ON", "OFF"]

                AMPLitude = AMPLitude()
                """
                SOURce:MARKer:FSWeep:AMPLitude

                Arguments: 1, ON, OFF
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MARKer:FSWeep:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()
                """
                SOURce:MARKer:FSWeep:FREQuency

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:MARKer:FSWeep:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:MARKer:FSWeep:STATe

                Arguments: 1, ON, OFF
                """

            FSWeep = FSWeep()
            """
            SOURce:MARKer:FSWeep

            Arguments:
            """

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:MARKer:POLarity

                Arguments: NEGative, POSitive
                """
                _cmd = "POLarity"
                args = ["NEGative", "POSitive"]

            POLarity = POLarity()
            """
            SOURce:MARKer:POLarity

            Arguments: NEGative, POSitive
            """

            class PSWeep(SCPINode):
                """
                SOURce:MARKer:PSWeep

                Arguments:
                """
                _cmd = "PSWeep"
                args = []

                class POWer(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MARKer:PSWeep:POWer

                    Arguments: 1
                    """
                    _cmd = "POWer"
                    args = ["1"]

                POWer = POWer()
                """
                SOURce:MARKer:PSWeep:POWer

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:MARKer:PSWeep:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:MARKer:PSWeep:STATe

                Arguments: 1, ON, OFF
                """

            PSWeep = PSWeep()
            """
            SOURce:MARKer:PSWeep

            Arguments:
            """

            class REFerence(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:MARKer:REFerence

                Arguments: 1
                """
                _cmd = "REFerence"
                args = ["1"]

            REFerence = REFerence()
            """
            SOURce:MARKer:REFerence

            Arguments: 1
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:MARKer:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SOURce:MARKer:STATe

            Arguments: 1, ON, OFF
            """

            class VIDeo(SCPINode, SCPIBool):
                """
                SOURce:MARKer:VIDeo

                Arguments: 1, ON, OFF
                """
                _cmd = "VIDeo"
                args = ["1", "ON", "OFF"]

            VIDeo = VIDeo()
            """
            SOURce:MARKer:VIDeo

            Arguments: 1, ON, OFF
            """

        MARKer = MARKer()
        """
        SOURce:MARKer

        Arguments:
        """

        class MBEacon(SCPINode):
            """
            SOURce:MBEacon

            Arguments:
            """
            _cmd = "MBEacon"
            args = []

            class COMid(SCPINode):
                """
                SOURce:MBEacon:COMid

                Arguments:
                """
                _cmd = "COMid"
                args = []

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MBEacon:COMid:DEPTh

                    Arguments: 1
                    """
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()
                """
                SOURce:MBEacon:COMid:DEPTh

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MBEacon:COMid:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()
                """
                SOURce:MBEacon:COMid:FREQuency

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:MBEacon:COMid:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:MBEacon:COMid:STATe

                Arguments: 1, ON, OFF
                """

            COMid = COMid()
            """
            SOURce:MBEacon:COMid

            Arguments:
            """

            class MARKer(SCPINode):
                """
                SOURce:MBEacon:MARKer

                Arguments:
                """
                _cmd = "MARKer"
                args = []

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MBEacon:MARKer:DEPTh

                    Arguments: 1
                    """
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()
                """
                SOURce:MBEacon:MARKer:DEPTh

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MBEacon:MARKer:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()
                """
                SOURce:MBEacon:MARKer:FREQuency

                Arguments: 1
                """

            MARKer = MARKer()
            """
            SOURce:MBEacon:MARKer

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:MBEacon:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SOURce:MBEacon:STATe

            Arguments: 1, ON, OFF
            """

        MBEacon = MBEacon()
        """
        SOURce:MBEacon

        Arguments:
        """

        class MODulation(SCPINode):
            """
            SOURce:MODulation

            Arguments:
            """
            _cmd = "MODulation"
            args = []

            class ALL(SCPINode):
                """
                SOURce:MODulation:ALL

                Arguments:
                """
                _cmd = "ALL"
                args = []

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:MODulation:ALL:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7b63a3602aec41cd.htm#ID_318e32e54e9063210a00206a019f179a-19a855954e9063210a00206a0024546d-en-US>`_

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                `SOURce:MODulation:ALL:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7b63a3602aec41cd.htm#ID_318e32e54e9063210a00206a019f179a-19a855954e9063210a00206a0024546d-en-US>`_

                Arguments: 1, ON, OFF
                """

            ALL = ALL()
            """
            SOURce:MODulation:ALL

            Arguments:
            """

            class OUTPut(SCPINode):
                """
                SOURce:MODulation:OUTPut

                Arguments:
                """
                _cmd = "OUTPut"
                args = []

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:MODulation:OUTPut:SOURce

                    Arguments: AM, FM, OFF
                    """
                    _cmd = "SOURce"
                    args = ["AM", "FM", "OFF"]

                SOURce = SOURce()
                """
                SOURce:MODulation:OUTPut:SOURce

                Arguments: AM, FM, OFF
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:MODulation:OUTPut:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:MODulation:OUTPut:STATe

                Arguments: 1, ON, OFF
                """

            OUTPut = OUTPut()
            """
            SOURce:MODulation:OUTPut

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:MODulation:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SOURce:MODulation:STATe

            Arguments: 1, ON, OFF
            """

        MODulation = MODulation()
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
            _cmd = "PHASe"
            args = ["1"]

            class ADJust(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PHASe:ADJust

                Arguments: 1
                """
                _cmd = "ADJust"
                args = ["1"]

            ADJust = ADJust()
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
                _cmd = "REFerence"
                args = []

            REFerence = REFerence()
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
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SOURce:PHASe:STATe

            Arguments: 1, ON, OFF
            """

        PHASe = PHASe()
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
            _cmd = "PM"
            args = []

            class BANDwidth(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PM:BANDwidth

                Arguments: HIGH, NORMal
                """
                _cmd = "BANDwidth"
                args = ["HIGH", "NORMal"]

            BANDwidth = BANDwidth()
            """
            SOURce:PM:BANDwidth

            Arguments: HIGH, NORMal
            """

            class BWIDth(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PM:BWIDth

                Arguments: HIGH, NORMal
                """
                _cmd = "BWIDth"
                args = ["HIGH", "NORMal"]

            BWIDth = BWIDth()
            """
            SOURce:PM:BWIDth

            Arguments: HIGH, NORMal
            """

            class COUPling(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PM:COUPling

                Arguments: AC, DC
                """
                _cmd = "COUPling"
                args = ["AC", "DC"]

            COUPling = COUPling()
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
                _cmd = "DEViation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:PM:DEViation:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PM:DEViation:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:PM:DEViation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:PM:DEViation:STEP

                Arguments:
                """

                class TRACk(SCPINode, SCPIBool):
                    """
                    SOURce:PM:DEViation:TRACk

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "TRACk"
                    args = ["1", "ON", "OFF"]

                TRACk = TRACk()
                """
                SOURce:PM:DEViation:TRACk

                Arguments: 1, ON, OFF
                """

            DEViation = DEViation()
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
                _cmd = "EXTernal"
                args = []

                class COUPling(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:PM:EXTernal:COUPling
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/106b9eba3c704c91.htm#ID_2eca06d94dff07b70a00206a00e7db83-29ccec014dff07b70a00206a0024546d-en-US>`_

                    Arguments: AC, DC
                    """
                    _cmd = "COUPling"
                    args = ["AC", "DC"]

                COUPling = COUPling()
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
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()
                """
                SOURce:PM:EXTernal:IMPedance

                Arguments: 1
                """

            EXTernal = EXTernal()
            """
            SOURce:PM:EXTernal

            Arguments:
            """

            class INTernal(SCPINode, SCPISet):
                """
                SOURce:PM:INTernal

                Arguments:
                """
                _cmd = "INTernal"
                args = []

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PM:INTernal:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                    class ALTernate(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PM:INTernal:FREQuency:ALTernate

                        Arguments: 1
                        """
                        _cmd = "ALTernate"
                        args = ["1"]

                        class AMPLitude(SCPINode, SCPISet):
                            """
                            SOURce:PM:INTernal:FREQuency:ALTernate:AMPLitude

                            Arguments:
                            """
                            _cmd = "AMPLitude"
                            args = []

                            class PERCent(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:PM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                                Arguments: 1
                                """
                                _cmd = "PERCent"
                                args = ["1"]

                            PERCent = PERCent()
                            """
                            SOURce:PM:INTernal:FREQuency:ALTernate:AMPLitude:PERCent

                            Arguments: 1
                            """

                        AMPLitude = AMPLitude()
                        """
                        SOURce:PM:INTernal:FREQuency:ALTernate:AMPLitude

                        Arguments:
                        """

                    ALTernate = ALTernate()
                    """
                    SOURce:PM:INTernal:FREQuency:ALTernate

                    Arguments: 1
                    """

                    class STEP(SCPINode):
                        """
                        SOURce:PM:INTernal:FREQuency:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PM:INTernal:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:PM:INTernal:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:PM:INTernal:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()
                """
                SOURce:PM:INTernal:FREQuency

                Arguments: 1
                """

                class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PM:INTernal:FUNCtion

                    Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                    """
                    _cmd = "FUNCtion"
                    args = ["GAUSsian", "NOISe", "RAMP", "SINusoid", "SQUare", "TRIangle", "UNIForm"]

                    class NOISe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PM:INTernal:FUNCtion:NOISe

                        Arguments: GAUSsian, UNIForm
                        """
                        _cmd = "NOISe"
                        args = ["GAUSsian", "UNIForm"]

                    NOISe = NOISe()
                    """
                    SOURce:PM:INTernal:FUNCtion:NOISe

                    Arguments: GAUSsian, UNIForm
                    """

                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PM:INTernal:FUNCtion:SHAPe

                        Arguments: SINE, SQUare
                        """
                        _cmd = "SHAPe"
                        args = ["SINE", "SQUare"]

                    SHAPe = SHAPe()
                    """
                    SOURce:PM:INTernal:FUNCtion:SHAPe

                    Arguments: SINE, SQUare
                    """

                FUNCtion = FUNCtion()
                """
                SOURce:PM:INTernal:FUNCtion

                Arguments: GAUSsian, NOISe, RAMP, SINusoid, SQUare, TRIangle, UNIForm
                """

                class SWEep(SCPINode, SCPISet):
                    """
                    SOURce:PM:INTernal:SWEep

                    Arguments:
                    """
                    _cmd = "SWEep"
                    args = []

                    class TRIGger(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PM:INTernal:SWEep:TRIGger

                        Arguments: BUS, EXTernal, IMMediate, KEY
                        """
                        _cmd = "TRIGger"
                        args = ["BUS", "EXTernal", "IMMediate", "KEY"]

                    TRIGger = TRIGger()
                    """
                    SOURce:PM:INTernal:SWEep:TRIGger

                    Arguments: BUS, EXTernal, IMMediate, KEY
                    """

                SWEep = SWEep()
                """
                SOURce:PM:INTernal:SWEep

                Arguments:
                """

            INTernal = INTernal()
            """
            SOURce:PM:INTernal

            Arguments:
            """

            class RANGe(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PM:RANGe

                Arguments: AUTO, HIGH, LOW
                """
                _cmd = "RANGe"
                args = ["AUTO", "HIGH", "LOW"]

            RANGe = RANGe()
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
                _cmd = "SENSitivity"
                args = ["1"]

            SENSitivity = SENSitivity()
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
                _cmd = "SOURce"
                args = ["EXTernal", "INT1", "INT2", "INTernal", "INTernal1", "INTernal2,EXTernal", "INT1", "INTernal", "INTernal1"]

            SOURce = SOURce()
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
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            `SOURce:PM:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/ae557ed7d4cc4881.htm#ID_26e0edd44dff16ba0a00206a009af85a-2b5c07604dff16ba0a00206a0024546d-en-US>`_

            Arguments: 1, ON, OFF
            """

        PM = PM()
        """
        SOURce:PM

        Arguments:
        """

        class POWer(SCPINode):
            """
            SOURce:POWer

            Arguments:
            """
            _cmd = "POWer"
            args = []

            class ALC(SCPINode):
                """
                SOURce:POWer:ALC

                Arguments:
                """
                _cmd = "ALC"
                args = []

                class BANDwidth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:BANDwidth

                    Arguments: 1
                    """
                    _cmd = "BANDwidth"
                    args = ["1"]

                BANDwidth = BANDwidth()
                """
                SOURce:POWer:ALC:BANDwidth

                Arguments: 1
                """

                class BWIDth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:BWIDth

                    Arguments: 1
                    """
                    _cmd = "BWIDth"
                    args = ["1"]

                BWIDth = BWIDth()
                """
                SOURce:POWer:ALC:BWIDth

                Arguments: 1
                """

                class CFACtor(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:CFACtor

                    Arguments: 1
                    """
                    _cmd = "CFACtor"
                    args = ["1"]

                CFACtor = CFACtor()
                """
                SOURce:POWer:ALC:CFACtor

                Arguments: 1
                """

                class LEVel(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:LEVel

                    Arguments: 1
                    """
                    _cmd = "LEVel"
                    args = ["1"]

                LEVel = LEVel()
                """
                SOURce:POWer:ALC:LEVel

                Arguments: 1
                """

                class PMETer(SCPINode):
                    """
                    SOURce:POWer:ALC:PMETer

                    Arguments:
                    """
                    _cmd = "PMETer"
                    args = []

                    class LEVel(SCPINode):
                        """
                        SOURce:POWer:ALC:PMETer:LEVel

                        Arguments:
                        """
                        _cmd = "LEVel"
                        args = []

                        class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:ALC:PMETer:LEVel:AMPLitude

                            Arguments: 1
                            """
                            _cmd = "AMPLitude"
                            args = ["1"]

                        AMPLitude = AMPLitude()
                        """
                        SOURce:POWer:ALC:PMETer:LEVel:AMPLitude

                        Arguments: 1
                        """

                        class STEP(SCPINode):
                            """
                            SOURce:POWer:ALC:PMETer:LEVel:STEP

                            Arguments:
                            """
                            _cmd = "STEP"
                            args = []

                            class INCRement(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:POWer:ALC:PMETer:LEVel:STEP:INCRement

                                Arguments: 1
                                """
                                _cmd = "INCRement"
                                args = ["1"]

                            INCRement = INCRement()
                            """
                            SOURce:POWer:ALC:PMETer:LEVel:STEP:INCRement

                            Arguments: 1
                            """

                        STEP = STEP()
                        """
                        SOURce:POWer:ALC:PMETer:LEVel:STEP

                        Arguments:
                        """

                    LEVel = LEVel()
                    """
                    SOURce:POWer:ALC:PMETer:LEVel

                    Arguments:
                    """

                PMETer = PMETer()
                """
                SOURce:POWer:ALC:PMETer

                Arguments:
                """

                class REFerence(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:REFerence

                    Arguments: 1
                    """
                    _cmd = "REFerence"
                    args = ["1"]

                REFerence = REFerence()
                """
                SOURce:POWer:ALC:REFerence

                Arguments: 1
                """

                class SEARch(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:SEARch

                    Arguments: <boolean>, ONCE
                    """
                    _cmd = "SEARch"
                    args = ["<boolean>", "ONCE"]

                    class REFerence(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:ALC:SEARch:REFerence

                        Arguments: FIXed, MODulated
                        """
                        _cmd = "REFerence"
                        args = ["FIXed", "MODulated"]

                    REFerence = REFerence()
                    """
                    SOURce:POWer:ALC:SEARch:REFerence

                    Arguments: FIXed, MODulated
                    """

                    class SPAN(SCPINode):
                        """
                        SOURce:POWer:ALC:SEARch:SPAN

                        Arguments:
                        """
                        _cmd = "SPAN"
                        args = []

                        class STARt(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:ALC:SEARch:SPAN:STARt

                            Arguments: 1
                            """
                            _cmd = "STARt"
                            args = ["1"]

                        STARt = STARt()
                        """
                        SOURce:POWer:ALC:SEARch:SPAN:STARt

                        Arguments: 1
                        """

                        class STATe(SCPINode, SCPIBool):
                            """
                            SOURce:POWer:ALC:SEARch:SPAN:STATe

                            Arguments: 1, ON, OFF
                            """
                            _cmd = "STATe"
                            args = ["1", "ON", "OFF"]

                        STATe = STATe()
                        """
                        SOURce:POWer:ALC:SEARch:SPAN:STATe

                        Arguments: 1, ON, OFF
                        """

                    SPAN = SPAN()
                    """
                    SOURce:POWer:ALC:SEARch:SPAN

                    Arguments:
                    """

                SEARch = SEARch()
                """
                SOURce:POWer:ALC:SEARch

                Arguments: <boolean>, ONCE
                """

                class SLOPe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:SLOPe

                    Arguments: FAST, MEDium, SLOW
                    """
                    _cmd = "SLOPe"
                    args = ["FAST", "MEDium", "SLOW"]

                SLOPe = SLOPe()
                """
                SOURce:POWer:ALC:SLOPe

                Arguments: FAST, MEDium, SLOW
                """

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:SOURce

                    Arguments: DIOD1, DIOD2, DIODe, DIODe1, DIODe2, FIXed, INTernal, PMET1, PMET2, PMETer, PMETer1, PMETer2
                    """
                    _cmd = "SOURce"
                    args = ["DIOD1", "DIOD2", "DIODe", "DIODe1", "DIODe2", "FIXed", "INTernal", "PMET1", "PMET2", "PMETer", "PMETer1", "PMETer2"]

                    class EXTernal(SCPINode):
                        """
                        SOURce:POWer:ALC:SOURce:EXTernal

                        Arguments:
                        """
                        _cmd = "EXTernal"
                        args = []

                        class COUPling(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:ALC:SOURce:EXTernal:COUPling

                            Arguments: 1
                            """
                            _cmd = "COUPling"
                            args = ["1"]

                        COUPling = COUPling()
                        """
                        SOURce:POWer:ALC:SOURce:EXTernal:COUPling

                        Arguments: 1
                        """

                    EXTernal = EXTernal()
                    """
                    SOURce:POWer:ALC:SOURce:EXTernal

                    Arguments:
                    """

                    class PMETer(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:ALC:SOURce:PMETer

                        Arguments: HP436a, RS_Nrvs
                        """
                        _cmd = "PMETer"
                        args = ["HP436a", "RS_Nrvs"]

                    PMETer = PMETer()
                    """
                    SOURce:POWer:ALC:SOURce:PMETer

                    Arguments: HP436a, RS_Nrvs
                    """

                SOURce = SOURce()
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
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                `SOURce:POWer:ALC:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/318c26be4c5141e7.htm#ID_42c28bb071aa81480a00206a0127eb9d-881ee75671aa81480a00206a012bc823-en-US>`_

                Arguments: 1, ON, OFF
                """

            ALC = ALC()
            """
            SOURce:POWer:ALC

            Arguments:
            """

            class ALTernate(SCPINode, SCPISet):
                """
                SOURce:POWer:ALTernate

                Arguments:
                """
                _cmd = "ALTernate"
                args = []

                class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALTernate:AMPLitude

                    Arguments: 1
                    """
                    _cmd = "AMPLitude"
                    args = ["1"]

                AMPLitude = AMPLitude()
                """
                SOURce:POWer:ALTernate:AMPLitude

                Arguments: 1
                """

                class MANual(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALTernate:MANual

                    Arguments: DELTa, MAIN
                    """
                    _cmd = "MANual"
                    args = ["DELTa", "MAIN"]

                MANual = MANual()
                """
                SOURce:POWer:ALTernate:MANual

                Arguments: DELTa, MAIN
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:ALTernate:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:POWer:ALTernate:STATe

                Arguments: 1, ON, OFF
                """

                class TRIGger(SCPINode):
                    """
                    SOURce:POWer:ALTernate:TRIGger

                    Arguments:
                    """
                    _cmd = "TRIGger"
                    args = []

                    class SOURce(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:ALTernate:TRIGger:SOURce

                        Arguments: EXTernal, INTernal, MANual
                        """
                        _cmd = "SOURce"
                        args = ["EXTernal", "INTernal", "MANual"]

                    SOURce = SOURce()
                    """
                    SOURce:POWer:ALTernate:TRIGger:SOURce

                    Arguments: EXTernal, INTernal, MANual
                    """

                TRIGger = TRIGger()
                """
                SOURce:POWer:ALTernate:TRIGger

                Arguments:
                """

            ALTernate = ALTernate()
            """
            SOURce:POWer:ALTernate

            Arguments:
            """

            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:ATTenuation

                Arguments: 1
                """
                _cmd = "ATTenuation"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:POWer:ATTenuation:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:ATTenuation:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:POWer:ATTenuation:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:POWer:ATTenuation:STEP

                Arguments:
                """

            ATTenuation = ATTenuation()
            """
            SOURce:POWer:ATTenuation

            Arguments: 1
            """

            class CENTer(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:CENTer

                Arguments: 1
                """
                _cmd = "CENTer"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:POWer:CENTer:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CENTer:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:POWer:CENTer:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:POWer:CENTer:STEP

                Arguments:
                """

            CENTer = CENTer()
            """
            SOURce:POWer:CENTer

            Arguments: 1
            """

            class DISPlay(SCPINode, SCPISet):
                """
                SOURce:POWer:DISPlay

                Arguments:
                """
                _cmd = "DISPlay"
                args = []

                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:DISPlay:OFFSet

                    Arguments: 1
                    """
                    _cmd = "OFFSet"
                    args = ["1"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:POWer:DISPlay:OFFSet:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SOURce:POWer:DISPlay:OFFSet:STATe

                    Arguments: 1, ON, OFF
                    """

                OFFSet = OFFSet()
                """
                SOURce:POWer:DISPlay:OFFSet

                Arguments: 1
                """

            DISPlay = DISPlay()
            """
            SOURce:POWer:DISPlay

            Arguments:
            """

            class EMF(SCPINode):
                """
                SOURce:POWer:EMF

                Arguments:
                """
                _cmd = "EMF"
                args = []

                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:EMF:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5f72d48c013e4e46.htm#ID_6119d3272c6943f20a001ae750554416-95cda6a92c6941fe0a001ae76b46bcda-en-US>`_

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                `SOURce:POWer:EMF:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5f72d48c013e4e46.htm#ID_6119d3272c6943f20a001ae750554416-95cda6a92c6941fe0a001ae76b46bcda-en-US>`_

                Arguments: 1, ON, OFF
                """

            EMF = EMF()
            """
            SOURce:POWer:EMF

            Arguments:
            """

            class LEVel(SCPINode):
                """
                SOURce:POWer:LEVel

                Arguments:
                """
                _cmd = "LEVel"
                args = []

                class ALTernate(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:LEVel:ALTernate

                    Arguments: 1
                    """
                    _cmd = "ALTernate"
                    args = ["1"]

                ALTernate = ALTernate()
                """
                SOURce:POWer:LEVel:ALTernate

                Arguments: 1
                """

                class IMMediate(SCPINode):
                    """
                    SOURce:POWer:LEVel:IMMediate

                    Arguments:
                    """
                    _cmd = "IMMediate"
                    args = []

                    class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:AMPLitude
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bb5bb606cd4d4681.htm#ID_d70bf25871aa63310a00206a00bc8d87-d732685371aa63310a00206a012bc823-en-US>`_

                        Arguments: 1
                        """
                        _cmd = "AMPLitude"
                        args = ["1"]

                        class BACKup(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:LEVel:IMMediate:AMPLitude:BACKup

                            Arguments: 1
                            """
                            _cmd = "BACKup"
                            args = ["1"]

                        BACKup = BACKup()
                        """
                        SOURce:POWer:LEVel:IMMediate:AMPLitude:BACKup

                        Arguments: 1
                        """

                        class STEP(SCPINode):
                            """
                            SOURce:POWer:LEVel:IMMediate:AMPLitude:STEP

                            Arguments:
                            """
                            _cmd = "STEP"
                            args = []

                            class INCRement(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:POWer:LEVel:IMMediate:AMPLitude:STEP:INCRement

                                Arguments: 1
                                """
                                _cmd = "INCRement"
                                args = ["1"]

                            INCRement = INCRement()
                            """
                            SOURce:POWer:LEVel:IMMediate:AMPLitude:STEP:INCRement

                            Arguments: 1
                            """

                        STEP = STEP()
                        """
                        SOURce:POWer:LEVel:IMMediate:AMPLitude:STEP

                        Arguments:
                        """

                    AMPLitude = AMPLitude()
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
                        _cmd = "OFFSet"
                        args = ["1"]

                        class LINear(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:LEVel:IMMediate:OFFSet:LINear

                            Arguments: 1
                            """
                            _cmd = "LINear"
                            args = ["1"]

                        LINear = LINear()
                        """
                        SOURce:POWer:LEVel:IMMediate:OFFSet:LINear

                        Arguments: 1
                        """

                        class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:LEVel:IMMediate:OFFSet:LOGarithmic

                            Arguments: 1
                            """
                            _cmd = "LOGarithmic"
                            args = ["1"]

                        LOGarithmic = LOGarithmic()
                        """
                        SOURce:POWer:LEVel:IMMediate:OFFSet:LOGarithmic

                        Arguments: 1
                        """

                    OFFSet = OFFSet()
                    """
                    `SOURce:POWer:LEVel:IMMediate:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/906418e7a7b84f3c.htm#ID_c493de1471aa6af10a00206a00d83907-a6ae5f2a71aa6af10a00206a012bc823-en-US>`_

                    Arguments: 1
                    """

                IMMediate = IMMediate()
                """
                SOURce:POWer:LEVel:IMMediate

                Arguments:
                """

            LEVel = LEVel()
            """
            SOURce:POWer:LEVel

            Arguments:
            """

            class LIMit(SCPINode):
                """
                SOURce:POWer:LIMit

                Arguments:
                """
                _cmd = "LIMit"
                args = []

                class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:LIMit:AMPLitude
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/de410925c5dd477b.htm#ID_f38a02d771aa72930a00206a017c0246-a1f79d3e71aa72930a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    _cmd = "AMPLitude"
                    args = ["1"]

                AMPLitude = AMPLitude()
                """
                `SOURce:POWer:LIMit:AMPLitude
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/de410925c5dd477b.htm#ID_f38a02d771aa72930a00206a017c0246-a1f79d3e71aa72930a00206a012bc823-en-US>`_

                Arguments: 1
                """

            LIMit = LIMit()
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
                _cmd = "MANual"
                args = ["1"]

            MANual = MANual()
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
                _cmd = "OFFSet"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:OFFSet:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:POWer:OFFSet:STATe

                Arguments: 1, ON, OFF
                """

            OFFSet = OFFSet()
            """
            SOURce:POWer:OFFSet

            Arguments: 1
            """

            class PROTection(SCPINode, SCPIBool):
                """
                SOURce:POWer:PROTection

                Arguments: 1, ON, OFF
                """
                _cmd = "PROTection"
                args = ["1", "ON", "OFF"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:PROTection:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:POWer:PROTection:STATe

                Arguments: 1, ON, OFF
                """

            PROTection = PROTection()
            """
            SOURce:POWer:PROTection

            Arguments: 1, ON, OFF
            """

            class RANGe(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:RANGe

                Arguments: 1
                """
                _cmd = "RANGe"
                args = ["1"]

            RANGe = RANGe()
            """
            SOURce:POWer:RANGe

            Arguments: 1
            """

            class REFerence(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:REFerence

                Arguments: 1
                """
                _cmd = "REFerence"
                args = ["1"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:REFerence:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:POWer:REFerence:STATe

                Arguments: 1, ON, OFF
                """

            REFerence = REFerence()
            """
            SOURce:POWer:REFerence

            Arguments: 1
            """

            class SEARch(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:SEARch

                Arguments: <boolean>, ONCE
                """
                _cmd = "SEARch"
                args = ["<boolean>", "ONCE"]

            SEARch = SEARch()
            """
            SOURce:POWer:SEARch

            Arguments: <boolean>, ONCE
            """

            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:SLOPe

                Arguments: 1
                """
                _cmd = "SLOPe"
                args = ["1"]

                class PIVot(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:SLOPe:PIVot

                    Arguments: 1
                    """
                    _cmd = "PIVot"
                    args = ["1"]

                PIVot = PIVot()
                """
                SOURce:POWer:SLOPe:PIVot

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:SLOPe:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:POWer:SLOPe:STATe

                Arguments: 1, ON, OFF
                """

                class STEP(SCPINode):
                    """
                    SOURce:POWer:SLOPe:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:SLOPe:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:POWer:SLOPe:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:POWer:SLOPe:STEP

                Arguments:
                """

            SLOPe = SLOPe()
            """
            SOURce:POWer:SLOPe

            Arguments: 1
            """

            class SPAN(SCPINode):
                """
                SOURce:POWer:SPAN

                Arguments:
                """
                _cmd = "SPAN"
                args = []

                class STEP(SCPINode):
                    """
                    SOURce:POWer:SPAN:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:SPAN:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:POWer:SPAN:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:POWer:SPAN:STEP

                Arguments:
                """

            SPAN = SPAN()
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
                _cmd = "STARt"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:POWer:STARt:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:STARt:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:POWer:STARt:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:POWer:STARt:STEP

                Arguments:
                """

            STARt = STARt()
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
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SOURce:POWer:STATe

            Arguments: 1, ON, OFF
            """

            class STEP(SCPINode):
                """
                SOURce:POWer:STEP

                Arguments:
                """
                _cmd = "STEP"
                args = []

                class INCRement(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:STEP:INCRement
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3a5b9c83f91a4347.htm#ID_78f8a91f71aa79c60a00206a01d797f3-dccd25e471aa79c60a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    _cmd = "INCRement"
                    args = ["1"]

                    class LINear(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:STEP:INCRement:LINear

                        Arguments: 1
                        """
                        _cmd = "LINear"
                        args = ["1"]

                    LINear = LINear()
                    """
                    SOURce:POWer:STEP:INCRement:LINear

                    Arguments: 1
                    """

                    class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:STEP:INCRement:LOGarithmic

                        Arguments: 1
                        """
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()
                    """
                    SOURce:POWer:STEP:INCRement:LOGarithmic

                    Arguments: 1
                    """

                INCRement = INCRement()
                """
                `SOURce:POWer:STEP:INCRement
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3a5b9c83f91a4347.htm#ID_78f8a91f71aa79c60a00206a01d797f3-dccd25e471aa79c60a00206a012bc823-en-US>`_

                Arguments: 1
                """

            STEP = STEP()
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
                _cmd = "STOP"
                args = []

                class STEP(SCPINode):
                    """
                    SOURce:POWer:STOP:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:STOP:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:POWer:STOP:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:POWer:STOP:STEP

                Arguments:
                """

            STOP = STOP()
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
                _cmd = "USER"
                args = []

                class ENABle(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:USER:ENABle

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "ENABle"
                    args = ["1", "ON", "OFF"]

                ENABle = ENABle()
                """
                SOURce:POWer:USER:ENABle

                Arguments: 1, ON, OFF
                """

                class MAXimum(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:USER:MAXimum

                    Arguments: 1
                    """
                    _cmd = "MAXimum"
                    args = ["1"]

                MAXimum = MAXimum()
                """
                SOURce:POWer:USER:MAXimum

                Arguments: 1
                """

            USER = USER()
            """
            SOURce:POWer:USER

            Arguments:
            """

        POWer = POWer()
        """
        SOURce:POWer

        Arguments:
        """

        class PULM(SCPINode):
            """
            SOURce:PULM

            Arguments:
            """
            _cmd = "PULM"
            args = []

            class EXTernal(SCPINode, SCPISet):
                """
                SOURce:PULM:EXTernal

                Arguments:
                """
                _cmd = "EXTernal"
                args = []

                class DELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:EXTernal:DELay

                    Arguments: 1
                    """
                    _cmd = "DELay"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:EXTernal:DELay:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:EXTernal:DELay:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:PULM:EXTernal:DELay:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:PULM:EXTernal:DELay:STEP

                    Arguments:
                    """

                DELay = DELay()
                """
                SOURce:PULM:EXTernal:DELay

                Arguments: 1
                """

                class IMPedance(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:EXTernal:IMPedance

                    Arguments: 1
                    """
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()
                """
                SOURce:PULM:EXTernal:IMPedance

                Arguments: 1
                """

                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:EXTernal:POLarity

                    Arguments: INVerted, NORMal
                    """
                    _cmd = "POLarity"
                    args = ["INVerted", "NORMal"]

                POLarity = POLarity()
                """
                SOURce:PULM:EXTernal:POLarity

                Arguments: INVerted, NORMal
                """

            EXTernal = EXTernal()
            """
            SOURce:PULM:EXTernal

            Arguments:
            """

            class INTernal(SCPINode, SCPISet):
                """
                SOURce:PULM:INTernal

                Arguments:
                """
                _cmd = "INTernal"
                args = []

                class DELay(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:INTernal:DELay

                    Arguments: 1
                    """
                    _cmd = "DELay"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:INTernal:DELay:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:INTernal:DELay:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:PULM:INTernal:DELay:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:PULM:INTernal:DELay:STEP

                    Arguments:
                    """

                DELay = DELay()
                """
                SOURce:PULM:INTernal:DELay

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:INTernal:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:INTernal:FREQuency:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:INTernal:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:PULM:INTernal:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:PULM:INTernal:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()
                """
                SOURce:PULM:INTernal:FREQuency

                Arguments: 1
                """

                class FUNCtion(SCPINode):
                    """
                    SOURce:PULM:INTernal:FUNCtion

                    Arguments:
                    """
                    _cmd = "FUNCtion"
                    args = []

                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULM:INTernal:FUNCtion:SHAPe

                        Arguments: PULSe, SQUare
                        """
                        _cmd = "SHAPe"
                        args = ["PULSe", "SQUare"]

                    SHAPe = SHAPe()
                    """
                    SOURce:PULM:INTernal:FUNCtion:SHAPe

                    Arguments: PULSe, SQUare
                    """

                FUNCtion = FUNCtion()
                """
                SOURce:PULM:INTernal:FUNCtion

                Arguments:
                """

                class PERiod(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:INTernal:PERiod

                    Arguments: 1
                    """
                    _cmd = "PERiod"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:INTernal:PERiod:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:INTernal:PERiod:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:PULM:INTernal:PERiod:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:PULM:INTernal:PERiod:STEP

                    Arguments:
                    """

                PERiod = PERiod()
                """
                SOURce:PULM:INTernal:PERiod

                Arguments: 1
                """

                class PWIDth(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:INTernal:PWIDth

                    Arguments: 1
                    """
                    _cmd = "PWIDth"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:INTernal:PWIDth:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:INTernal:PWIDth:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:PULM:INTernal:PWIDth:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:PULM:INTernal:PWIDth:STEP

                    Arguments:
                    """

                PWIDth = PWIDth()
                """
                SOURce:PULM:INTernal:PWIDth

                Arguments: 1
                """

                class TRIGger(SCPINode):
                    """
                    SOURce:PULM:INTernal:TRIGger

                    Arguments:
                    """
                    _cmd = "TRIGger"
                    args = []

                    class SOURce(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULM:INTernal:TRIGger:SOURce

                        Arguments: EXTernal, INTernal
                        """
                        _cmd = "SOURce"
                        args = ["EXTernal", "INTernal"]

                    SOURce = SOURce()
                    """
                    SOURce:PULM:INTernal:TRIGger:SOURce

                    Arguments: EXTernal, INTernal
                    """

                TRIGger = TRIGger()
                """
                SOURce:PULM:INTernal:TRIGger

                Arguments:
                """

                class VIDeo(SCPINode, SCPISet):
                    """
                    SOURce:PULM:INTernal:VIDeo

                    Arguments:
                    """
                    _cmd = "VIDeo"
                    args = []

                    class POLarity(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULM:INTernal:VIDeo:POLarity

                        Arguments: INVerted, NORMal
                        """
                        _cmd = "POLarity"
                        args = ["INVerted", "NORMal"]

                    POLarity = POLarity()
                    """
                    SOURce:PULM:INTernal:VIDeo:POLarity

                    Arguments: INVerted, NORMal
                    """

                VIDeo = VIDeo()
                """
                SOURce:PULM:INTernal:VIDeo

                Arguments:
                """

                class WIDTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:INTernal:WIDTh

                    Arguments: 1
                    """
                    _cmd = "WIDTh"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULM:INTernal:WIDTh:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULM:INTernal:WIDTh:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:PULM:INTernal:WIDTh:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:PULM:INTernal:WIDTh:STEP

                    Arguments:
                    """

                WIDTh = WIDTh()
                """
                SOURce:PULM:INTernal:WIDTh

                Arguments: 1
                """

            INTernal = INTernal()
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
                _cmd = "PERiod"
                args = ["1"]

            PERiod = PERiod()
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
                _cmd = "POLarity"
                args = ["INVerted", "NORMal"]

            POLarity = POLarity()
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
                _cmd = "SOURce"
                args = ["EXT1", "EXT2", "EXTernal", "EXTernal1", "EXTernal2", "INTernal"]

                class INTernal(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULM:SOURce:INTernal

                    Arguments: ADOublet, DOUBlet, FRUN, GATed, SQUare, TRIGgered
                    """
                    _cmd = "INTernal"
                    args = ["ADOublet", "DOUBlet", "FRUN", "GATed", "SQUare", "TRIGgered"]

                INTernal = INTernal()
                """
                SOURce:PULM:SOURce:INTernal

                Arguments: ADOublet, DOUBlet, FRUN, GATed, SQUare, TRIGgered
                """

            SOURce = SOURce()
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
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
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
                _cmd = "WIDTh"
                args = ["1"]

            WIDTh = WIDTh()
            """
            `SOURce:PULM:WIDTh
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/737870cd065d45b3.htm#ID_b29b3cb94e355edb0a00206a016f086a-cfb305434e355edb0a00206a0024546d-en-US>`_

            Arguments: 1
            """

        PULM = PULM()
        """
        SOURce:PULM

        Arguments:
        """

        class PULSe(SCPINode):
            """
            SOURce:PULSe

            Arguments:
            """
            _cmd = "PULSe"
            args = []

            class DELay(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PULSe:DELay

                Arguments: 1
                """
                _cmd = "DELay"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:PULSe:DELay:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULSe:DELay:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:PULSe:DELay:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:PULSe:DELay:STEP

                Arguments:
                """

            DELay = DELay()
            """
            SOURce:PULSe:DELay

            Arguments: 1
            """

            class DOUBle(SCPINode):
                """
                SOURce:PULSe:DOUBle

                Arguments:
                """
                _cmd = "DOUBle"
                args = []

                class DELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULSe:DOUBle:DELay

                    Arguments: 1
                    """
                    _cmd = "DELay"
                    args = ["1"]

                DELay = DELay()
                """
                SOURce:PULSe:DOUBle:DELay

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:PULSe:DOUBle:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:PULSe:DOUBle:STATe

                Arguments: 1, ON, OFF
                """

            DOUBle = DOUBle()
            """
            SOURce:PULSe:DOUBle

            Arguments:
            """

            class INTernal(SCPINode):
                """
                SOURce:PULSe:INTernal

                Arguments:
                """
                _cmd = "INTernal"
                args = []

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULSe:INTernal:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                    class STEP(SCPINode):
                        """
                        SOURce:PULSe:INTernal:FREQuency:STEP

                        Arguments:
                        """
                        _cmd = "STEP"
                        args = []

                        class INCRement(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:PULSe:INTernal:FREQuency:STEP:INCRement

                            Arguments: 1
                            """
                            _cmd = "INCRement"
                            args = ["1"]

                        INCRement = INCRement()
                        """
                        SOURce:PULSe:INTernal:FREQuency:STEP:INCRement

                        Arguments: 1
                        """

                    STEP = STEP()
                    """
                    SOURce:PULSe:INTernal:FREQuency:STEP

                    Arguments:
                    """

                FREQuency = FREQuency()
                """
                SOURce:PULSe:INTernal:FREQuency

                Arguments: 1
                """

            INTernal = INTernal()
            """
            SOURce:PULSe:INTernal

            Arguments:
            """

            class PERiod(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PULSe:PERiod

                Arguments: 1
                """
                _cmd = "PERiod"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:PULSe:PERiod:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULSe:PERiod:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:PULSe:PERiod:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:PULSe:PERiod:STEP

                Arguments:
                """

            PERiod = PERiod()
            """
            SOURce:PULSe:PERiod

            Arguments: 1
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PULSe:SOURce

                Arguments: EXTernal, INTernal, SCALar
                """
                _cmd = "SOURce"
                args = ["EXTernal", "INTernal", "SCALar"]

            SOURce = SOURce()
            """
            SOURce:PULSe:SOURce

            Arguments: EXTernal, INTernal, SCALar
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:PULSe:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SOURce:PULSe:STATe

            Arguments: 1, ON, OFF
            """

            class TRANsition(SCPINode):
                """
                SOURce:PULSe:TRANsition

                Arguments:
                """
                _cmd = "TRANsition"
                args = []

                class LEADing(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULSe:TRANsition:LEADing

                    Arguments: FAST, MEDium, SLOW
                    """
                    _cmd = "LEADing"
                    args = ["FAST", "MEDium", "SLOW"]

                LEADing = LEADing()
                """
                SOURce:PULSe:TRANsition:LEADing

                Arguments: FAST, MEDium, SLOW
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:PULSe:TRANsition:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:PULSe:TRANsition:STATe

                Arguments: 1, ON, OFF
                """

                class TRAiling(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:PULSe:TRANsition:TRAiling

                    Arguments: FAST, MEDium, SLOW
                    """
                    _cmd = "TRAiling"
                    args = ["FAST", "MEDium", "SLOW"]

                TRAiling = TRAiling()
                """
                SOURce:PULSe:TRANsition:TRAiling

                Arguments: FAST, MEDium, SLOW
                """

            TRANsition = TRANsition()
            """
            SOURce:PULSe:TRANsition

            Arguments:
            """

            class WIDTh(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:PULSe:WIDTh

                Arguments: 1
                """
                _cmd = "WIDTh"
                args = ["1"]

                class STEP(SCPINode):
                    """
                    SOURce:PULSe:WIDTh:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:PULSe:WIDTh:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SOURce:PULSe:WIDTh:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:PULSe:WIDTh:STEP

                Arguments:
                """

            WIDTh = WIDTh()
            """
            SOURce:PULSe:WIDTh

            Arguments: 1
            """

        PULSe = PULSe()
        """
        SOURce:PULSe

        Arguments:
        """

        class RADio(SCPINode, SCPISet):
            """
            SOURce:RADio

            Arguments:
            """
            _cmd = "RADio"
            args = []

            class ARB(SCPINode):
                """
                SOURce:RADio:ARB

                Arguments:
                """
                _cmd = "ARB"
                args = []

                class CLIPping(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:CLIPping

                    Arguments: <string>,IJQ, IORQ,<numeric_value>,<numeric_value>
                    """
                    _cmd = "CLIPping"
                    args = ["<string>,IJQ", "IORQ,<numeric_value>,<numeric_value>"]

                CLIPping = CLIPping()
                """
                SOURce:RADio:ARB:CLIPping

                Arguments: <string>,IJQ, IORQ,<numeric_value>,<numeric_value>
                """

                class CLOCk(SCPINode):
                    """
                    SOURce:RADio:ARB:CLOCk

                    Arguments:
                    """
                    _cmd = "CLOCk"
                    args = []

                    class REFerence(SCPINode):
                        """
                        SOURce:RADio:ARB:CLOCk:REFerence

                        Arguments:
                        """
                        _cmd = "REFerence"
                        args = []

                        class EXTernal(SCPINode, SCPISet):
                            """
                            SOURce:RADio:ARB:CLOCk:REFerence:EXTernal

                            Arguments:
                            """
                            _cmd = "EXTernal"
                            args = []

                            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:ARB:CLOCk:REFerence:EXTernal:FREQuency

                                Arguments: 1
                                """
                                _cmd = "FREQuency"
                                args = ["1"]

                            FREQuency = FREQuency()
                            """
                            SOURce:RADio:ARB:CLOCk:REFerence:EXTernal:FREQuency

                            Arguments: 1
                            """

                        EXTernal = EXTernal()
                        """
                        SOURce:RADio:ARB:CLOCk:REFerence:EXTernal

                        Arguments:
                        """

                        class SOURce(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:ARB:CLOCk:REFerence:SOURce

                            Arguments: EXTernal, INTernal
                            """
                            _cmd = "SOURce"
                            args = ["EXTernal", "INTernal"]

                        SOURce = SOURce()
                        """
                        SOURce:RADio:ARB:CLOCk:REFerence:SOURce

                        Arguments: EXTernal, INTernal
                        """

                    REFerence = REFerence()
                    """
                    SOURce:RADio:ARB:CLOCk:REFerence

                    Arguments:
                    """

                    class SRATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:CLOCk:SRATe

                        Arguments: 1
                        """
                        _cmd = "SRATe"
                        args = ["1"]

                    SRATe = SRATe()
                    """
                    SOURce:RADio:ARB:CLOCk:SRATe

                    Arguments: 1
                    """

                CLOCk = CLOCk()
                """
                SOURce:RADio:ARB:CLOCk

                Arguments:
                """

                class DACS(SCPINode):
                    """
                    SOURce:RADio:ARB:DACS

                    Arguments:
                    """
                    _cmd = "DACS"
                    args = []

                    class ALIGn(SCPINode, SCPISet):
                        """
                        SOURce:RADio:ARB:DACS:ALIGn

                        Arguments:
                        """
                        _cmd = "ALIGn"
                        args = []

                    ALIGn = ALIGn()
                    """
                    SOURce:RADio:ARB:DACS:ALIGn

                    Arguments:
                    """

                DACS = DACS()
                """
                SOURce:RADio:ARB:DACS

                Arguments:
                """

                class GENerate(SCPINode, SCPISet):
                    """
                    SOURce:RADio:ARB:GENerate

                    Arguments:
                    """
                    _cmd = "GENerate"
                    args = []

                GENerate = GENerate()
                """
                SOURce:RADio:ARB:GENerate

                Arguments:
                """

                class HEADer(SCPINode, SCPISet):
                    """
                    SOURce:RADio:ARB:HEADer

                    Arguments:
                    """
                    _cmd = "HEADer"
                    args = []

                    class CLEar(SCPINode, SCPISet):
                        """
                        SOURce:RADio:ARB:HEADer:CLEar

                        Arguments:
                        """
                        _cmd = "CLEar"
                        args = []

                    CLEar = CLEar()
                    """
                    SOURce:RADio:ARB:HEADer:CLEar

                    Arguments:
                    """

                HEADer = HEADer()
                """
                SOURce:RADio:ARB:HEADer

                Arguments:
                """

                class IQ(SCPINode):
                    """
                    SOURce:RADio:ARB:IQ

                    Arguments:
                    """
                    _cmd = "IQ"
                    args = []

                    class EXTernal(SCPINode, SCPISet):
                        """
                        SOURce:RADio:ARB:IQ:EXTernal

                        Arguments:
                        """
                        _cmd = "EXTernal"
                        args = []

                        class FILTer(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:ARB:IQ:EXTernal:FILTer

                            Arguments: 1
                            """
                            _cmd = "FILTer"
                            args = ["1"]

                        FILTer = FILTer()
                        """
                        SOURce:RADio:ARB:IQ:EXTernal:FILTer

                        Arguments: 1
                        """

                    EXTernal = EXTernal()
                    """
                    SOURce:RADio:ARB:IQ:EXTernal

                    Arguments:
                    """

                    class MODulation(SCPINode, SCPISet):
                        """
                        SOURce:RADio:ARB:IQ:MODulation

                        Arguments:
                        """
                        _cmd = "MODulation"
                        args = []

                        class ATTen(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:ARB:IQ:MODulation:ATTen

                            Arguments: 1
                            """
                            _cmd = "ATTen"
                            args = ["1"]

                        ATTen = ATTen()
                        """
                        SOURce:RADio:ARB:IQ:MODulation:ATTen

                        Arguments: 1
                        """

                        class FILTer(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:ARB:IQ:MODulation:FILTer

                            Arguments: 1
                            """
                            _cmd = "FILTer"
                            args = ["1"]

                        FILTer = FILTer()
                        """
                        SOURce:RADio:ARB:IQ:MODulation:FILTer

                        Arguments: 1
                        """

                    MODulation = MODulation()
                    """
                    SOURce:RADio:ARB:IQ:MODulation

                    Arguments:
                    """

                IQ = IQ()
                """
                SOURce:RADio:ARB:IQ

                Arguments:
                """

                class MARKer(SCPINode):
                    """
                    SOURce:RADio:ARB:MARKer

                    Arguments:
                    """
                    _cmd = "MARKer"
                    args = []

                    class CLEar(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MARKer:CLEar

                        Arguments: <string>,<numeric_value>,<numeric_value>,<numeric_value>
                        """
                        _cmd = "CLEar"
                        args = ["<string>,<numeric_value>,<numeric_value>,<numeric_value>"]

                    CLEar = CLEar()
                    """
                    SOURce:RADio:ARB:MARKer:CLEar

                    Arguments: <string>,<numeric_value>,<numeric_value>,<numeric_value>
                    """

                    class ROTate(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MARKer:ROTate

                        Arguments: <string>,<numeric_value>
                        """
                        _cmd = "ROTate"
                        args = ["<string>,<numeric_value>"]

                    ROTate = ROTate()
                    """
                    SOURce:RADio:ARB:MARKer:ROTate

                    Arguments: <string>,<numeric_value>
                    """

                MARKer = MARKer()
                """
                SOURce:RADio:ARB:MARKer

                Arguments:
                """

                class MDEStination(SCPINode, SCPISet):
                    """
                    SOURce:RADio:ARB:MDEStination

                    Arguments:
                    """
                    _cmd = "MDEStination"
                    args = []

                    class AAMPlitude(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MDEStination:AAMPlitude

                        Arguments: M1, M2, M3, M4, NONE
                        """
                        _cmd = "AAMPlitude"
                        args = ["M1", "M2", "M3", "M4", "NONE"]

                    AAMPlitude = AAMPlitude()
                    """
                    SOURce:RADio:ARB:MDEStination:AAMPlitude

                    Arguments: M1, M2, M3, M4, NONE
                    """

                    class ALCHold(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MDEStination:ALCHold

                        Arguments: M1, M2, M3, M4, NONE
                        """
                        _cmd = "ALCHold"
                        args = ["M1", "M2", "M3", "M4", "NONE"]

                    ALCHold = ALCHold()
                    """
                    SOURce:RADio:ARB:MDEStination:ALCHold

                    Arguments: M1, M2, M3, M4, NONE
                    """

                    class PULSe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MDEStination:PULSe

                        Arguments: M1, M2, M3, M4, NONE
                        """
                        _cmd = "PULSe"
                        args = ["M1", "M2", "M3", "M4", "NONE"]

                    PULSe = PULSe()
                    """
                    SOURce:RADio:ARB:MDEStination:PULSe

                    Arguments: M1, M2, M3, M4, NONE
                    """

                MDEStination = MDEStination()
                """
                SOURce:RADio:ARB:MDEStination

                Arguments:
                """

                class MPOLarity(SCPINode, SCPISet):
                    """
                    SOURce:RADio:ARB:MPOLarity

                    Arguments:
                    """
                    _cmd = "MPOLarity"
                    args = []

                    class MARKer(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:MPOLarity:MARKer

                        Arguments: NEGative, POSitive
                        """
                        _cmd = "MARKer"
                        args = ["NEGative", "POSitive"]

                    MARKer = MARKer()
                    """
                    SOURce:RADio:ARB:MPOLarity:MARKer

                    Arguments: NEGative, POSitive
                    """

                MPOLarity = MPOLarity()
                """
                SOURce:RADio:ARB:MPOLarity

                Arguments:
                """

                class NOISe(SCPINode):
                    """
                    SOURce:RADio:ARB:NOISe

                    Arguments:
                    """
                    _cmd = "NOISe"
                    args = []

                    class BFACtor(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:NOISe:BFACtor

                        Arguments: 1
                        """
                        _cmd = "BFACtor"
                        args = ["1"]

                    BFACtor = BFACtor()
                    """
                    SOURce:RADio:ARB:NOISe:BFACtor

                    Arguments: 1
                    """

                    class CBWidth(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:NOISe:CBWidth

                        Arguments: 1
                        """
                        _cmd = "CBWidth"
                        args = ["1"]

                    CBWidth = CBWidth()
                    """
                    SOURce:RADio:ARB:NOISe:CBWidth

                    Arguments: 1
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:RADio:ARB:NOISe:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SOURce:RADio:ARB:NOISe:STATe

                    Arguments: 1, ON, OFF
                    """

                NOISe = NOISe()
                """
                SOURce:RADio:ARB:NOISe

                Arguments:
                """

                class REFerence(SCPINode):
                    """
                    SOURce:RADio:ARB:REFerence

                    Arguments:
                    """
                    _cmd = "REFerence"
                    args = []

                    class EXTernal(SCPINode, SCPISet):
                        """
                        SOURce:RADio:ARB:REFerence:EXTernal

                        Arguments:
                        """
                        _cmd = "EXTernal"
                        args = []

                        class FREQuency(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:ARB:REFerence:EXTernal:FREQuency

                            Arguments: 1
                            """
                            _cmd = "FREQuency"
                            args = ["1"]

                        FREQuency = FREQuency()
                        """
                        SOURce:RADio:ARB:REFerence:EXTernal:FREQuency

                        Arguments: 1
                        """

                    EXTernal = EXTernal()
                    """
                    SOURce:RADio:ARB:REFerence:EXTernal

                    Arguments:
                    """

                    class SOURce(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:REFerence:SOURce

                        Arguments: EXTernal, INTernal
                        """
                        _cmd = "SOURce"
                        args = ["EXTernal", "INTernal"]

                    SOURce = SOURce()
                    """
                    SOURce:RADio:ARB:REFerence:SOURce

                    Arguments: EXTernal, INTernal
                    """

                REFerence = REFerence()
                """
                SOURce:RADio:ARB:REFerence

                Arguments:
                """

                class RETRigger(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:RETRigger

                    Arguments: <boolean>, IMMediate
                    """
                    _cmd = "RETRigger"
                    args = ["<boolean>", "IMMediate"]

                RETRigger = RETRigger()
                """
                SOURce:RADio:ARB:RETRigger

                Arguments: <boolean>, IMMediate
                """

                class RFILter(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:RFILter

                    Arguments: 1
                    """
                    _cmd = "RFILter"
                    args = ["1"]

                RFILter = RFILter()
                """
                SOURce:RADio:ARB:RFILter

                Arguments: 1
                """

                class RSCaling(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:RSCaling

                    Arguments: 1
                    """
                    _cmd = "RSCaling"
                    args = ["1"]

                RSCaling = RSCaling()
                """
                SOURce:RADio:ARB:RSCaling

                Arguments: 1
                """

                class SCALing(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:SCALing

                    Arguments: <string>,<numeric_value>
                    """
                    _cmd = "SCALing"
                    args = ["<string>,<numeric_value>"]

                SCALing = SCALing()
                """
                SOURce:RADio:ARB:SCALing

                Arguments: <string>,<numeric_value>
                """

                class SCLock(SCPINode, SCPISet):
                    """
                    SOURce:RADio:ARB:SCLock

                    Arguments:
                    """
                    _cmd = "SCLock"
                    args = []

                SCLock = SCLock()
                """
                SOURce:RADio:ARB:SCLock

                Arguments:
                """

                class SEQuence(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:SEQuence

                    Arguments: 'string'
                    """
                    _cmd = "SEQuence"
                    args = ["'string'"]

                SEQuence = SEQuence()
                """
                SOURce:RADio:ARB:SEQuence

                Arguments: 'string'
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:RADio:ARB:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:RADio:ARB:STATe

                Arguments: 1, ON, OFF
                """

                class TRIGger(SCPINode):
                    """
                    SOURce:RADio:ARB:TRIGger

                    Arguments:
                    """
                    _cmd = "TRIGger"
                    args = []

                    class SOURce(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:TRIGger:SOURce

                        Arguments: BUS, EXTernal, KEY
                        """
                        _cmd = "SOURce"
                        args = ["BUS", "EXTernal", "KEY"]

                        class EXTernal(SCPINode):
                            """
                            SOURce:RADio:ARB:TRIGger:SOURce:EXTernal

                            Arguments:
                            """
                            _cmd = "EXTernal"
                            args = []

                            class DELay(SCPINode):
                                """
                                SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay

                                Arguments:
                                """
                                _cmd = "DELay"
                                args = []

                                class SAMPles(SCPINode, SCPIQuery, SCPISet):
                                    """
                                    SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay:SAMPles

                                    Arguments: 1
                                    """
                                    _cmd = "SAMPles"
                                    args = ["1"]

                                SAMPles = SAMPles()
                                """
                                SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay:SAMPles

                                Arguments: 1
                                """

                                class STATe(SCPINode, SCPIBool):
                                    """
                                    SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay:STATe

                                    Arguments: 1, ON, OFF
                                    """
                                    _cmd = "STATe"
                                    args = ["1", "ON", "OFF"]

                                STATe = STATe()
                                """
                                SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay:STATe

                                Arguments: 1, ON, OFF
                                """

                            DELay = DELay()
                            """
                            SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:DELay

                            Arguments:
                            """

                            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:SLOPe

                                Arguments: NEGative, POSitive
                                """
                                _cmd = "SLOPe"
                                args = ["NEGative", "POSitive"]

                            SLOPe = SLOPe()
                            """
                            SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:SLOPe

                            Arguments: NEGative, POSitive
                            """

                            class SOURce(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:SOURce

                                Arguments: EPT1, EPT2, EPTRigger1, EPTRigger2
                                """
                                _cmd = "SOURce"
                                args = ["EPT1", "EPT2", "EPTRigger1", "EPTRigger2"]

                            SOURce = SOURce()
                            """
                            SOURce:RADio:ARB:TRIGger:SOURce:EXTernal:SOURce

                            Arguments: EPT1, EPT2, EPTRigger1, EPTRigger2
                            """

                        EXTernal = EXTernal()
                        """
                        SOURce:RADio:ARB:TRIGger:SOURce:EXTernal

                        Arguments:
                        """

                    SOURce = SOURce()
                    """
                    SOURce:RADio:ARB:TRIGger:SOURce

                    Arguments: BUS, EXTernal, KEY
                    """

                    class TYPE(SCPINode):
                        """
                        SOURce:RADio:ARB:TRIGger:TYPE

                        Arguments:
                        """
                        _cmd = "TYPE"
                        args = []

                        class GATE(SCPINode):
                            """
                            SOURce:RADio:ARB:TRIGger:TYPE:GATE

                            Arguments:
                            """
                            _cmd = "GATE"
                            args = []

                            class ACTive(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:ARB:TRIGger:TYPE:GATE:ACTive

                                Arguments: HIGH, LOW
                                """
                                _cmd = "ACTive"
                                args = ["HIGH", "LOW"]

                            ACTive = ACTive()
                            """
                            SOURce:RADio:ARB:TRIGger:TYPE:GATE:ACTive

                            Arguments: HIGH, LOW
                            """

                        GATE = GATE()
                        """
                        SOURce:RADio:ARB:TRIGger:TYPE:GATE

                        Arguments:
                        """

                    TYPE = TYPE()
                    """
                    SOURce:RADio:ARB:TRIGger:TYPE

                    Arguments:
                    """

                TRIGger = TRIGger()
                """
                SOURce:RADio:ARB:TRIGger

                Arguments:
                """

                class VCO(SCPINode):
                    """
                    SOURce:RADio:ARB:VCO

                    Arguments:
                    """
                    _cmd = "VCO"
                    args = []

                    class CLOCk(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:VCO:CLOCk

                        Arguments: EXTernal, INTernal
                        """
                        _cmd = "CLOCk"
                        args = ["EXTernal", "INTernal"]

                    CLOCk = CLOCk()
                    """
                    SOURce:RADio:ARB:VCO:CLOCk

                    Arguments: EXTernal, INTernal
                    """

                VCO = VCO()
                """
                SOURce:RADio:ARB:VCO

                Arguments:
                """

                class WAVeform(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:RADio:ARB:WAVeform

                    Arguments: 'string'
                    """
                    _cmd = "WAVeform"
                    args = ["'string'"]

                    class NHEaders(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:ARB:WAVeform:NHEaders

                        Arguments: 'string'
                        """
                        _cmd = "NHEaders"
                        args = ["'string'"]

                    NHEaders = NHEaders()
                    """
                    SOURce:RADio:ARB:WAVeform:NHEaders

                    Arguments: 'string'
                    """

                WAVeform = WAVeform()
                """
                SOURce:RADio:ARB:WAVeform

                Arguments: 'string'
                """

            ARB = ARB()
            """
            SOURce:RADio:ARB

            Arguments:
            """

            class AWGN(SCPINode):
                """
                SOURce:RADio:AWGN

                Arguments:
                """
                _cmd = "AWGN"
                args = []

                class ARB(SCPINode):
                    """
                    SOURce:RADio:AWGN:ARB

                    Arguments:
                    """
                    _cmd = "ARB"
                    args = []

                    class BWIDth(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:AWGN:ARB:BWIDth

                        Arguments: 1
                        """
                        _cmd = "BWIDth"
                        args = ["1"]

                    BWIDth = BWIDth()
                    """
                    SOURce:RADio:AWGN:ARB:BWIDth

                    Arguments: 1
                    """

                    class HEADer(SCPINode, SCPISet):
                        """
                        SOURce:RADio:AWGN:ARB:HEADer

                        Arguments:
                        """
                        _cmd = "HEADer"
                        args = []

                        class CLEar(SCPINode, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:HEADer:CLEar

                            Arguments:
                            """
                            _cmd = "CLEar"
                            args = []

                        CLEar = CLEar()
                        """
                        SOURce:RADio:AWGN:ARB:HEADer:CLEar

                        Arguments:
                        """

                    HEADer = HEADer()
                    """
                    SOURce:RADio:AWGN:ARB:HEADer

                    Arguments:
                    """

                    class IQ(SCPINode):
                        """
                        SOURce:RADio:AWGN:ARB:IQ

                        Arguments:
                        """
                        _cmd = "IQ"
                        args = []

                        class EXTernal(SCPINode, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:IQ:EXTernal

                            Arguments:
                            """
                            _cmd = "EXTernal"
                            args = []

                            class FILTer(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:AWGN:ARB:IQ:EXTernal:FILTer

                                Arguments: <numeric_value>, THRough
                                """
                                _cmd = "FILTer"
                                args = ["<numeric_value>", "THRough"]

                            FILTer = FILTer()
                            """
                            SOURce:RADio:AWGN:ARB:IQ:EXTernal:FILTer

                            Arguments: <numeric_value>, THRough
                            """

                        EXTernal = EXTernal()
                        """
                        SOURce:RADio:AWGN:ARB:IQ:EXTernal

                        Arguments:
                        """

                        class MODulation(SCPINode, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:IQ:MODulation

                            Arguments:
                            """
                            _cmd = "MODulation"
                            args = []

                            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:AWGN:ARB:IQ:MODulation:ATTenuation

                                Arguments: 1
                                """
                                _cmd = "ATTenuation"
                                args = ["1"]

                            ATTenuation = ATTenuation()
                            """
                            SOURce:RADio:AWGN:ARB:IQ:MODulation:ATTenuation

                            Arguments: 1
                            """

                            class FILTer(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:AWGN:ARB:IQ:MODulation:FILTer

                                Arguments: <numeric_value>, THRough
                                """
                                _cmd = "FILTer"
                                args = ["<numeric_value>", "THRough"]

                            FILTer = FILTer()
                            """
                            SOURce:RADio:AWGN:ARB:IQ:MODulation:FILTer

                            Arguments: <numeric_value>, THRough
                            """

                        MODulation = MODulation()
                        """
                        SOURce:RADio:AWGN:ARB:IQ:MODulation

                        Arguments:
                        """

                    IQ = IQ()
                    """
                    SOURce:RADio:AWGN:ARB:IQ

                    Arguments:
                    """

                    class LENGth(SCPINode, SCPIQuery):
                        """
                        SOURce:RADio:AWGN:ARB:LENGth

                        Arguments:
                        """
                        _cmd = "LENGth"
                        args = []

                    LENGth = LENGth()
                    """
                    SOURce:RADio:AWGN:ARB:LENGth

                    Arguments:
                    """

                    class MDEStination(SCPINode, SCPISet):
                        """
                        SOURce:RADio:AWGN:ARB:MDEStination

                        Arguments:
                        """
                        _cmd = "MDEStination"
                        args = []

                        class AAMPlitude(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:MDEStination:AAMPlitude

                            Arguments: M1, M2, M3, M4, NONE
                            """
                            _cmd = "AAMPlitude"
                            args = ["M1", "M2", "M3", "M4", "NONE"]

                        AAMPlitude = AAMPlitude()
                        """
                        SOURce:RADio:AWGN:ARB:MDEStination:AAMPlitude

                        Arguments: M1, M2, M3, M4, NONE
                        """

                        class ALCHold(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:MDEStination:ALCHold

                            Arguments: M1, M2, M3, M4, NONE
                            """
                            _cmd = "ALCHold"
                            args = ["M1", "M2", "M3", "M4", "NONE"]

                        ALCHold = ALCHold()
                        """
                        SOURce:RADio:AWGN:ARB:MDEStination:ALCHold

                        Arguments: M1, M2, M3, M4, NONE
                        """

                        class PULSe(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:MDEStination:PULSe

                            Arguments: M1, M2, M3, M4, NONE
                            """
                            _cmd = "PULSe"
                            args = ["M1", "M2", "M3", "M4", "NONE"]

                        PULSe = PULSe()
                        """
                        SOURce:RADio:AWGN:ARB:MDEStination:PULSe

                        Arguments: M1, M2, M3, M4, NONE
                        """

                    MDEStination = MDEStination()
                    """
                    SOURce:RADio:AWGN:ARB:MDEStination

                    Arguments:
                    """

                    class MPOLartity(SCPINode, SCPISet):
                        """
                        SOURce:RADio:AWGN:ARB:MPOLartity

                        Arguments:
                        """
                        _cmd = "MPOLartity"
                        args = []

                        class MARKer(SCPINodeN, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:MPOLartity:MARKer

                            Arguments: NEGative, POSitive
                            """
                            _cmd = "MARKer"
                            args = ["NEGative", "POSitive"]

                        MARKer = MARKer()
                        """
                        SOURce:RADio:AWGN:ARB:MPOLartity:MARKer

                        Arguments: NEGative, POSitive
                        """

                    MPOLartity = MPOLartity()
                    """
                    SOURce:RADio:AWGN:ARB:MPOLartity

                    Arguments:
                    """

                    class REFerence(SCPINode):
                        """
                        SOURce:RADio:AWGN:ARB:REFerence

                        Arguments:
                        """
                        _cmd = "REFerence"
                        args = []

                        class EXTernal(SCPINode, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:REFerence:EXTernal

                            Arguments:
                            """
                            _cmd = "EXTernal"
                            args = []

                            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:AWGN:ARB:REFerence:EXTernal:FREQuency

                                Arguments: 1
                                """
                                _cmd = "FREQuency"
                                args = ["1"]

                            FREQuency = FREQuency()
                            """
                            SOURce:RADio:AWGN:ARB:REFerence:EXTernal:FREQuency

                            Arguments: 1
                            """

                        EXTernal = EXTernal()
                        """
                        SOURce:RADio:AWGN:ARB:REFerence:EXTernal

                        Arguments:
                        """

                        class SOURce(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:ARB:REFerence:SOURce

                            Arguments: EXTernal, INTernal
                            """
                            _cmd = "SOURce"
                            args = ["EXTernal", "INTernal"]

                        SOURce = SOURce()
                        """
                        SOURce:RADio:AWGN:ARB:REFerence:SOURce

                        Arguments: EXTernal, INTernal
                        """

                    REFerence = REFerence()
                    """
                    SOURce:RADio:AWGN:ARB:REFerence

                    Arguments:
                    """

                    class SCLock(SCPINode, SCPISet):
                        """
                        SOURce:RADio:AWGN:ARB:SCLock

                        Arguments:
                        """
                        _cmd = "SCLock"
                        args = []

                    SCLock = SCLock()
                    """
                    SOURce:RADio:AWGN:ARB:SCLock

                    Arguments:
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:RADio:AWGN:ARB:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SOURce:RADio:AWGN:ARB:STATe

                    Arguments: 1, ON, OFF
                    """

                ARB = ARB()
                """
                SOURce:RADio:AWGN:ARB

                Arguments:
                """

                class RT(SCPINode):
                    """
                    SOURce:RADio:AWGN:RT

                    Arguments:
                    """
                    _cmd = "RT"
                    args = []

                    class BWIDth(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:AWGN:RT:BWIDth

                        Arguments: 1
                        """
                        _cmd = "BWIDth"
                        args = ["1"]

                    BWIDth = BWIDth()
                    """
                    SOURce:RADio:AWGN:RT:BWIDth

                    Arguments: 1
                    """

                    class IQ(SCPINode):
                        """
                        SOURce:RADio:AWGN:RT:IQ

                        Arguments:
                        """
                        _cmd = "IQ"
                        args = []

                        class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:AWGN:RT:IQ:ATTenuation

                            Arguments: 1
                            """
                            _cmd = "ATTenuation"
                            args = ["1"]

                        ATTenuation = ATTenuation()
                        """
                        SOURce:RADio:AWGN:RT:IQ:ATTenuation

                        Arguments: 1
                        """

                    IQ = IQ()
                    """
                    SOURce:RADio:AWGN:RT:IQ

                    Arguments:
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:RADio:AWGN:RT:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SOURce:RADio:AWGN:RT:STATe

                    Arguments: 1, ON, OFF
                    """

                RT = RT()
                """
                SOURce:RADio:AWGN:RT

                Arguments:
                """

            AWGN = AWGN()
            """
            SOURce:RADio:AWGN

            Arguments:
            """

            class MTONe(SCPINode):
                """
                SOURce:RADio:MTONe

                Arguments:
                """
                _cmd = "MTONe"
                args = []

                class ARB(SCPINode):
                    """
                    SOURce:RADio:MTONe:ARB

                    Arguments:
                    """
                    _cmd = "ARB"
                    args = []

                    class REFerence(SCPINode):
                        """
                        SOURce:RADio:MTONe:ARB:REFerence

                        Arguments:
                        """
                        _cmd = "REFerence"
                        args = []

                        class EXTernal(SCPINode, SCPISet):
                            """
                            SOURce:RADio:MTONe:ARB:REFerence:EXTernal

                            Arguments:
                            """
                            _cmd = "EXTernal"
                            args = []

                            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:MTONe:ARB:REFerence:EXTernal:FREQuency

                                Arguments: 1
                                """
                                _cmd = "FREQuency"
                                args = ["1"]

                            FREQuency = FREQuency()
                            """
                            SOURce:RADio:MTONe:ARB:REFerence:EXTernal:FREQuency

                            Arguments: 1
                            """

                        EXTernal = EXTernal()
                        """
                        SOURce:RADio:MTONe:ARB:REFerence:EXTernal

                        Arguments:
                        """

                        class SOURce(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:MTONe:ARB:REFerence:SOURce

                            Arguments: EXTernal, INTernal
                            """
                            _cmd = "SOURce"
                            args = ["EXTernal", "INTernal"]

                        SOURce = SOURce()
                        """
                        SOURce:RADio:MTONe:ARB:REFerence:SOURce

                        Arguments: EXTernal, INTernal
                        """

                    REFerence = REFerence()
                    """
                    SOURce:RADio:MTONe:ARB:REFerence

                    Arguments:
                    """

                    class SCLock(SCPINode, SCPISet):
                        """
                        SOURce:RADio:MTONe:ARB:SCLock

                        Arguments:
                        """
                        _cmd = "SCLock"
                        args = []

                    SCLock = SCLock()
                    """
                    SOURce:RADio:MTONe:ARB:SCLock

                    Arguments:
                    """

                    class SETup(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:RADio:MTONe:ARB:SETup

                        Arguments: 'string'
                        """
                        _cmd = "SETup"
                        args = ["'string'"]

                        class STORe(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:MTONe:ARB:SETup:STORe

                            Arguments: 'string'
                            """
                            _cmd = "STORe"
                            args = ["'string'"]

                        STORe = STORe()
                        """
                        SOURce:RADio:MTONe:ARB:SETup:STORe

                        Arguments: 'string'
                        """

                        class TABLe(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:RADio:MTONe:ARB:SETup:TABLe

                            Arguments: <numeric_value>,<numeric_value>,FIXed, RANDom,<boolean>
                            """
                            _cmd = "TABLe"
                            args = ["<numeric_value>,<numeric_value>,FIXed", "RANDom,<boolean>"]

                            class FSPacing(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:MTONe:ARB:SETup:TABLe:FSPacing

                                Arguments: 1
                                """
                                _cmd = "FSPacing"
                                args = ["1"]

                            FSPacing = FSPacing()
                            """
                            SOURce:RADio:MTONe:ARB:SETup:TABLe:FSPacing

                            Arguments: 1
                            """

                            class NTONes(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:RADio:MTONe:ARB:SETup:TABLe:NTONes

                                Arguments: 1
                                """
                                _cmd = "NTONes"
                                args = ["1"]

                            NTONes = NTONes()
                            """
                            SOURce:RADio:MTONe:ARB:SETup:TABLe:NTONes

                            Arguments: 1
                            """

                            class PHASe(SCPINode):
                                """
                                SOURce:RADio:MTONe:ARB:SETup:TABLe:PHASe

                                Arguments:
                                """
                                _cmd = "PHASe"
                                args = []

                                class INITialize(SCPINode, SCPIQuery, SCPISet):
                                    """
                                    SOURce:RADio:MTONe:ARB:SETup:TABLe:PHASe:INITialize

                                    Arguments: FIXed, RANDom
                                    """
                                    _cmd = "INITialize"
                                    args = ["FIXed", "RANDom"]

                                INITialize = INITialize()
                                """
                                SOURce:RADio:MTONe:ARB:SETup:TABLe:PHASe:INITialize

                                Arguments: FIXed, RANDom
                                """

                            PHASe = PHASe()
                            """
                            SOURce:RADio:MTONe:ARB:SETup:TABLe:PHASe

                            Arguments:
                            """

                        TABLe = TABLe()
                        """
                        SOURce:RADio:MTONe:ARB:SETup:TABLe

                        Arguments: <numeric_value>,<numeric_value>,FIXed, RANDom,<boolean>
                        """

                    SETup = SETup()
                    """
                    SOURce:RADio:MTONe:ARB:SETup

                    Arguments: 'string'
                    """

                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:RADio:MTONe:ARB:STATe

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    SOURce:RADio:MTONe:ARB:STATe

                    Arguments: 1, ON, OFF
                    """

                ARB = ARB()
                """
                SOURce:RADio:MTONe:ARB

                Arguments:
                """

            MTONe = MTONe()
            """
            SOURce:RADio:MTONe

            Arguments:
            """

        RADio = RADio()
        """
        SOURce:RADio

        Arguments:
        """

        class ROSCillator(SCPINode, SCPISet):
            """
            SOURce:ROSCillator

            Arguments:
            """
            _cmd = "ROSCillator"
            args = []

            class EXTernal(SCPINode):
                """
                SOURce:ROSCillator:EXTernal

                Arguments:
                """
                _cmd = "EXTernal"
                args = []

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:ROSCillator:EXTernal:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/17d3920a3880443f.htm#ID_4f9594624e4ad9290a00206a017105ad-77092b4a4e4acb8d0a00206a00a0c7ed-en-US>`_

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()
                """
                `SOURce:ROSCillator:EXTernal:FREQuency
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/17d3920a3880443f.htm#ID_4f9594624e4ad9290a00206a017105ad-77092b4a4e4acb8d0a00206a00a0c7ed-en-US>`_

                Arguments: 1
                """

            EXTernal = EXTernal()
            """
            SOURce:ROSCillator:EXTernal

            Arguments:
            """

            class FREQuency(SCPINode):
                """
                SOURce:ROSCillator:FREQuency

                Arguments:
                """
                _cmd = "FREQuency"
                args = []

                class EXTernal(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ROSCillator:FREQuency:EXTernal

                    Arguments: 1
                    """
                    _cmd = "EXTernal"
                    args = ["1"]

                EXTernal = EXTernal()
                """
                SOURce:ROSCillator:FREQuency:EXTernal

                Arguments: 1
                """

            FREQuency = FREQuency()
            """
            SOURce:ROSCillator:FREQuency

            Arguments:
            """

            class INTernal(SCPINode):
                """
                SOURce:ROSCillator:INTernal

                Arguments:
                """
                _cmd = "INTernal"
                args = []

                class ADJust(SCPINode):
                    """
                    SOURce:ROSCillator:INTernal:ADJust

                    Arguments:
                    """
                    _cmd = "ADJust"
                    args = []

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:ROSCillator:INTernal:ADJust:STATe
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b90515af7a4f4c94.htm#ID_d64368ec5700fce10a00206a014cb621-3792892e5700fce10a00206a0024546d-en-US>`_

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
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
                        _cmd = "VALue"
                        args = ["1"]

                    VALue = VALue()
                    """
                    `SOURce:ROSCillator:INTernal:ADJust:VALue
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/77691a4f94ac4ffc.htm#ID_a0023e065701029d0a00206a00d2b42c-b2019cd95701029d0a00206a0024546d-en-US>`_

                    Arguments: 1
                    """

                ADJust = ADJust()
                """
                SOURce:ROSCillator:INTernal:ADJust

                Arguments:
                """

                class RLOop(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:ROSCillator:INTernal:RLOop

                    Arguments: NARRow, NORMal
                    """
                    _cmd = "RLOop"
                    args = ["NARRow", "NORMal"]

                RLOop = RLOop()
                """
                SOURce:ROSCillator:INTernal:RLOop

                Arguments: NARRow, NORMal
                """

            INTernal = INTernal()
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
                _cmd = "SOURce"
                args = ["<numeric_value>,EXTernal"]

            SOURce = SOURce()
            """
            `SOURce:ROSCillator:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7e935bcba7104491.htm#ID_f861c84a5700f7140a00206a01a37e10-f799abd25700f7140a00206a0024546d-en-US>`_

            Arguments: <numeric_value>,EXTernal
            """

        ROSCillator = ROSCillator()
        """
        SOURce:ROSCillator

        Arguments:
        """

        class STEReo(SCPINode):
            """
            SOURce:STEReo

            Arguments:
            """
            _cmd = "STEReo"
            args = []

            class ARI(SCPINode):
                """
                SOURce:STEReo:ARI

                Arguments:
                """
                _cmd = "ARI"
                args = []

                class DEViation(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:ARI:DEViation
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/282a6e62f9164949.htm#ID_67dca7c4dc5bae370a00206a01e854e0-3da4a2e5dc5ba6c50a00206a01e40e15-en-US>`_

                    Arguments: 1
                    """
                    _cmd = "DEViation"
                    args = ["1"]

                DEViation = DEViation()
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
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
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
                    _cmd = "TYPE"
                    args = []

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:STEReo:ARI:TYPE:STATe
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/756911e513c34c67.htm#ID_c14f788bdc5c68bd0a00206a01bbc148-6c884fb2dc5c61d70a00206a01e40e15-en-US>`_

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    `SOURce:STEReo:ARI:TYPE:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/756911e513c34c67.htm#ID_c14f788bdc5c68bd0a00206a01bbc148-6c884fb2dc5c61d70a00206a01e40e15-en-US>`_

                    Arguments: 1, ON, OFF
                    """

                TYPE = TYPE()
                """
                `SOURce:STEReo:ARI:TYPE
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/5f0c571ed0204179.htm#ID_37f62275dc5bb6840a00206a00c7669c-3f459759dc5bb0a80a00206a01e40e15-en-US>`_

                Arguments:
                """

            ARI = ARI()
            """
            SOURce:STEReo:ARI

            Arguments:
            """

            class AUDio(SCPINode):
                """
                SOURce:STEReo:AUDio

                Arguments:
                """
                _cmd = "AUDio"
                args = []

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:AUDio:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b27b0233d15c4e70.htm#ID_7cfbf44adc5bdd070a00206a00bdbc74-df188684dc5bd76a0a00206a01e40e15-en-US>`_

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()
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
                    _cmd = "PREemphasis"
                    args = ["1"]

                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:STEReo:AUDio:PREemphasis:STATe
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/cc35ff90b52c4122.htm#ID_de10a50cdc5c02ee0a00206a0029bde5-ece51530dc5bfd510a00206a01e40e15-en-US>`_

                        Arguments: 1, ON, OFF
                        """
                        _cmd = "STATe"
                        args = ["1", "ON", "OFF"]

                    STATe = STATe()
                    """
                    `SOURce:STEReo:AUDio:PREemphasis:STATe
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/cc35ff90b52c4122.htm#ID_de10a50cdc5c02ee0a00206a0029bde5-ece51530dc5bfd510a00206a01e40e15-en-US>`_

                    Arguments: 1, ON, OFF
                    """

                PREemphasis = PREemphasis()
                """
                `SOURce:STEReo:AUDio:PREemphasis
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/652eea05e2f24016.htm#ID_5566f910dc5c399e0a00206a00781b8b-d08a4926dc5c33c20a00206a01e40e15-en-US>`_

                Arguments: 1
                """

            AUDio = AUDio()
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
                _cmd = "DEViation"
                args = ["1"]

            DEViation = DEViation()
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
                _cmd = "DIRect"
                args = ["'string'"]

            DIRect = DIRect()
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
                _cmd = "EXTernal"
                args = []

                class IMPedance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:EXTernal:IMPedance
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bf3bd3cb1b6149d7.htm#ID_ed166f71dc5bd5470a00206a00084298-5934d87ddc5bcfc90a00206a01e40e15-en-US>`_

                    Arguments: 1
                    """
                    _cmd = "IMPedance"
                    args = ["1"]

                IMPedance = IMPedance()
                """
                `SOURce:STEReo:EXTernal:IMPedance
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/bf3bd3cb1b6149d7.htm#ID_ed166f71dc5bd5470a00206a00084298-5934d87ddc5bcfc90a00206a01e40e15-en-US>`_

                Arguments: 1
                """

            EXTernal = EXTernal()
            """
            SOURce:STEReo:EXTernal

            Arguments:
            """

            class PILot(SCPINode):
                """
                SOURce:STEReo:PILot

                Arguments:
                """
                _cmd = "PILot"
                args = []

                class DEViation(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:PILot:DEViation
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/9109ab9c9a614b96.htm#ID_a3761f9bdc5bec4a0a00206a00716dbf-840e2c0cdc5be6ac0a00206a01e40e15-en-US>`_

                    Arguments: 1
                    """
                    _cmd = "DEViation"
                    args = ["1"]

                DEViation = DEViation()
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
                    _cmd = "PHASe"
                    args = ["1"]

                PHASe = PHASe()
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
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                `SOURce:STEReo:PILot:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/068535fbf91146eb.htm#ID_31ee9df8dc5bfb7c0a00206a0160f2b2-1b5f0342dc5bf5cf0a00206a01e40e15-en-US>`_

                Arguments: 1, ON, OFF
                """

            PILot = PILot()
            """
            SOURce:STEReo:PILot

            Arguments:
            """

            class RDS(SCPINode):
                """
                SOURce:STEReo:RDS

                Arguments:
                """
                _cmd = "RDS"
                args = []

                class DATaset(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:STEReo:RDS:DATaset
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/b0c13bb102454957.htm#ID_fd8383cedc5c0a700a00206a01b75b79-fe5583efdc5c04f20a00206a01e40e15-en-US>`_

                    Arguments: DS1, DS2, DS3, DS4, DS5
                    """
                    _cmd = "DATaset"
                    args = ["DS1", "DS2", "DS3", "DS4", "DS5"]

                DATaset = DATaset()
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
                    _cmd = "DEViation"
                    args = ["1"]

                DEViation = DEViation()
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
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
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
                    _cmd = "TRAFfic"
                    args = []

                    class ANNouncement(SCPINode):
                        """
                        SOURce:STEReo:RDS:TRAFfic:ANNouncement

                        Arguments:
                        """
                        _cmd = "ANNouncement"
                        args = []

                        class STATe(SCPINode, SCPIBool):
                            """
                            `SOURce:STEReo:RDS:TRAFfic:ANNouncement:STATe
                            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f5a48f2b2e614615.htm#ID_c2dea175dc5c29df0a00206a002c754e-e0bb6433dc5c24030a00206a01e40e15-en-US>`_

                            Arguments: 1, ON, OFF
                            """
                            _cmd = "STATe"
                            args = ["1", "ON", "OFF"]

                        STATe = STATe()
                        """
                        `SOURce:STEReo:RDS:TRAFfic:ANNouncement:STATe
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f5a48f2b2e614615.htm#ID_c2dea175dc5c29df0a00206a002c754e-e0bb6433dc5c24030a00206a01e40e15-en-US>`_

                        Arguments: 1, ON, OFF
                        """

                    ANNouncement = ANNouncement()
                    """
                    SOURce:STEReo:RDS:TRAFfic:ANNouncement

                    Arguments:
                    """

                    class PROGram(SCPINode):
                        """
                        SOURce:STEReo:RDS:TRAFfic:PROGram

                        Arguments:
                        """
                        _cmd = "PROGram"
                        args = []

                        class STATe(SCPINode, SCPIBool):
                            """
                            `SOURce:STEReo:RDS:TRAFfic:PROGram:STATe
                            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/6ba7f2ecc27b414b.htm#ID_2d18a912dc5c20d70a00206a00bd6c38-6bbab9b0dc5c1b580a00206a01e40e15-en-US>`_

                            Arguments: 1, ON, OFF
                            """
                            _cmd = "STATe"
                            args = ["1", "ON", "OFF"]

                        STATe = STATe()
                        """
                        `SOURce:STEReo:RDS:TRAFfic:PROGram:STATe
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/6ba7f2ecc27b414b.htm#ID_2d18a912dc5c20d70a00206a00bd6c38-6bbab9b0dc5c1b580a00206a01e40e15-en-US>`_

                        Arguments: 1, ON, OFF
                        """

                    PROGram = PROGram()
                    """
                    SOURce:STEReo:RDS:TRAFfic:PROGram

                    Arguments:
                    """

                TRAFfic = TRAFfic()
                """
                SOURce:STEReo:RDS:TRAFfic

                Arguments:
                """

            RDS = RDS()
            """
            SOURce:STEReo:RDS

            Arguments:
            """

            class SIGNal(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:STEReo:SIGNal

                Arguments: ARI, AUDio
                """
                _cmd = "SIGNal"
                args = ["ARI", "AUDio"]

            SIGNal = SIGNal()
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
                _cmd = "SOURce"
                args = ["LFGen", "LREXt", "SPEXt"]

            SOURce = SOURce()
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
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            `SOURce:STEReo:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/1e7f50df80754d97.htm#ID_755ff102dc5c48920a00206a00d7b608-7df2c8b4dc5c42f50a00206a01e40e15-en-US>`_

            Arguments: 1, ON, OFF
            """

        STEReo = STEReo()
        """
        SOURce:STEReo

        Arguments:
        """

        class SWEep(SCPINode, SCPISet):
            """
            SOURce:SWEep

            Arguments:
            """
            _cmd = "SWEep"
            args = []

            class BTIMe(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:BTIMe

                Arguments: LONG, NORMal
                """
                _cmd = "BTIMe"
                args = ["LONG", "NORMal"]

            BTIMe = BTIMe()
            """
            SOURce:SWEep:BTIMe

            Arguments: LONG, NORMal
            """

            class CONTrol(SCPINode, SCPISet):
                """
                SOURce:SWEep:CONTrol

                Arguments:
                """
                _cmd = "CONTrol"
                args = []

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:SWEep:CONTrol:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:SWEep:CONTrol:STATe

                Arguments: 1, ON, OFF
                """

            CONTrol = CONTrol()
            """
            SOURce:SWEep:CONTrol

            Arguments:
            """

            class CPOint(SCPINode, SCPIQuery):
                """
                SOURce:SWEep:CPOint

                Arguments:
                """
                _cmd = "CPOint"
                args = []

            CPOint = CPOint()
            """
            SOURce:SWEep:CPOint

            Arguments:
            """

            class DIRection(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:DIRection

                Arguments: DOWN, UP
                """
                _cmd = "DIRection"
                args = ["DOWN", "UP"]

            DIRection = DIRection()
            """
            SOURce:SWEep:DIRection

            Arguments: DOWN, UP
            """

            class DWELl(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:DWELl

                Arguments: 1
                """
                _cmd = "DWELl"
                args = ["1"]

            DWELl = DWELl()
            """
            SOURce:SWEep:DWELl

            Arguments: 1
            """

            class FREQuency(SCPINode, SCPISet):
                """
                SOURce:SWEep:FREQuency

                Arguments:
                """
                _cmd = "FREQuency"
                args = []

                class DWELl(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:SWEep:FREQuency:DWELl
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/422723d8553c40b3.htm#ID_22f1352871b719430a00206a01ebbac9-df858e4171b719430a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    _cmd = "DWELl"
                    args = ["1"]

                DWELl = DWELl()
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
                    _cmd = "POINts"
                    args = ["1"]

                POINts = POINts()
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
                    _cmd = "RUNNing"
                    args = []

                RUNNing = RUNNing()
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
                    _cmd = "SPACing"
                    args = ["LINear", "LOGarithmic"]

                SPACing = SPACing()
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
                    _cmd = "STEP"
                    args = []

                    class LINear(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:SWEep:FREQuency:STEP:LINear
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/6eeae32a24f148ac.htm#ID_019e085071b6fe580a00206a0078468a-5813ce6a71b6fe580a00206a012bc823-en-US>`_

                        Arguments: 1
                        """
                        _cmd = "LINear"
                        args = ["1"]

                    LINear = LINear()
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
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()
                    """
                    `SOURce:SWEep:FREQuency:STEP:LOGarithmic
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/ccbae2d831df45b5.htm#ID_b055cff771b704e00a00206a0023865a-f2478ac071b704e00a00206a012bc823-en-US>`_

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:SWEep:FREQuency:STEP

                Arguments:
                """

            FREQuency = FREQuency()
            """
            SOURce:SWEep:FREQuency

            Arguments:
            """

            class GENeration(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:GENeration

                Arguments: ANALog, STEPped
                """
                _cmd = "GENeration"
                args = ["ANALog", "STEPped"]

            GENeration = GENeration()
            """
            SOURce:SWEep:GENeration

            Arguments: ANALog, STEPped
            """

            class MANual(SCPINode):
                """
                SOURce:SWEep:MANual

                Arguments:
                """
                _cmd = "MANual"
                args = []

                class POINt(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:SWEep:MANual:POINt

                    Arguments: 1
                    """
                    _cmd = "POINt"
                    args = ["1"]

                POINt = POINt()
                """
                SOURce:SWEep:MANual:POINt

                Arguments: 1
                """

                class RELative(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:SWEep:MANual:RELative

                    Arguments: 1
                    """
                    _cmd = "RELative"
                    args = ["1"]

                RELative = RELative()
                """
                SOURce:SWEep:MANual:RELative

                Arguments: 1
                """

            MANual = MANual()
            """
            SOURce:SWEep:MANual

            Arguments:
            """

            class MARKer(SCPINode):
                """
                SOURce:SWEep:MARKer

                Arguments:
                """
                _cmd = "MARKer"
                args = []

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:SWEep:MARKer:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:SWEep:MARKer:STATe

                Arguments: 1, ON, OFF
                """

            MARKer = MARKer()
            """
            SOURce:SWEep:MARKer

            Arguments:
            """

            class POINts(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:POINts

                Arguments: 1
                """
                _cmd = "POINts"
                args = ["1"]

            POINts = POINts()
            """
            SOURce:SWEep:POINts

            Arguments: 1
            """

            class POWer(SCPINode, SCPISet):
                """
                SOURce:SWEep:POWer

                Arguments:
                """
                _cmd = "POWer"
                args = []

                class DWELl(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:SWEep:POWer:DWELl
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e0f78d0fb5574909.htm#ID_551ad14d71b750700a00206a0188e9b1-eacf1f4671b750700a00206a012bc823-en-US>`_

                    Arguments: 1
                    """
                    _cmd = "DWELl"
                    args = ["1"]

                DWELl = DWELl()
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
                    _cmd = "POINts"
                    args = ["1"]

                POINts = POINts()
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
                    _cmd = "RUNNing"
                    args = []

                RUNNing = RUNNing()
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
                    _cmd = "SPACing"
                    args = ["LOGarithmic"]

                SPACing = SPACing()
                """
                SOURce:SWEep:POWer:SPACing

                Arguments: LOGarithmic
                """

                class STEP(SCPINode):
                    """
                    SOURce:SWEep:POWer:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class LOGarithmic(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:SWEep:POWer:STEP:LOGarithmic
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7a028d77a0e64432.htm#ID_42b6782c71b757170a00206a01b31ca4-4dd4e73f71b757170a00206a012bc823-en-US>`_

                        Arguments: 1
                        """
                        _cmd = "LOGarithmic"
                        args = ["1"]

                    LOGarithmic = LOGarithmic()
                    """
                    `SOURce:SWEep:POWer:STEP:LOGarithmic
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/7a028d77a0e64432.htm#ID_42b6782c71b757170a00206a01b31ca4-4dd4e73f71b757170a00206a012bc823-en-US>`_

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SOURce:SWEep:POWer:STEP

                Arguments:
                """

            POWer = POWer()
            """
            SOURce:SWEep:POWer

            Arguments:
            """

            class SPACing(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:SWEep:SPACing

                Arguments: LINear, LOGarithmic
                """
                _cmd = "SPACing"
                args = ["LINear", "LOGarithmic"]

            SPACing = SPACing()
            """
            SOURce:SWEep:SPACing

            Arguments: LINear, LOGarithmic
            """

            class TIME(SCPINode):
                """
                SOURce:SWEep:TIME

                Arguments:
                """
                _cmd = "TIME"
                args = []

                class LLIMit(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:SWEep:TIME:LLIMit

                    Arguments: 1
                    """
                    _cmd = "LLIMit"
                    args = ["1"]

                LLIMit = LLIMit()
                """
                SOURce:SWEep:TIME:LLIMit

                Arguments: 1
                """

            TIME = TIME()
            """
            SOURce:SWEep:TIME

            Arguments:
            """

            class TRIGger(SCPINode):
                """
                SOURce:SWEep:TRIGger

                Arguments:
                """
                _cmd = "TRIGger"
                args = []

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:SWEep:TRIGger:SOURce

                    Arguments: BUS, EXTernal, IMMediate
                    """
                    _cmd = "SOURce"
                    args = ["BUS", "EXTernal", "IMMediate"]

                SOURce = SOURce()
                """
                SOURce:SWEep:TRIGger:SOURce

                Arguments: BUS, EXTernal, IMMediate
                """

            TRIGger = TRIGger()
            """
            SOURce:SWEep:TRIGger

            Arguments:
            """

        SWEep = SWEep()
        """
        SOURce:SWEep

        Arguments:
        """

        class TSWeep(SCPINode, SCPISet):
            """
            SOURce:TSWeep

            Arguments:
            """
            _cmd = "TSWeep"
            args = []

        TSWeep = TSWeep()
        """
        SOURce:TSWeep

        Arguments:
        """

        class VOR(SCPINode):
            """
            SOURce:VOR

            Arguments:
            """
            _cmd = "VOR"
            args = []

            class BANGle(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:VOR:BANGle

                Arguments: 1
                """
                _cmd = "BANGle"
                args = ["1"]

                class DIRection(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:BANGle:DIRection

                    Arguments: FROM, TO
                    """
                    _cmd = "DIRection"
                    args = ["FROM", "TO"]

                DIRection = DIRection()
                """
                SOURce:VOR:BANGle:DIRection

                Arguments: FROM, TO
                """

            BANGle = BANGle()
            """
            SOURce:VOR:BANGle

            Arguments: 1
            """

            class COMid(SCPINode):
                """
                SOURce:VOR:COMid

                Arguments:
                """
                _cmd = "COMid"
                args = []

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:COMid:DEPTh

                    Arguments: 1
                    """
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()
                """
                SOURce:VOR:COMid:DEPTh

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:COMid:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()
                """
                SOURce:VOR:COMid:FREQuency

                Arguments: 1
                """

                class STATe(SCPINode, SCPIBool):
                    """
                    SOURce:VOR:COMid:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SOURce:VOR:COMid:STATe

                Arguments: 1, ON, OFF
                """

            COMid = COMid()
            """
            SOURce:VOR:COMid

            Arguments:
            """

            class PRESet(SCPINode, SCPISet):
                """
                SOURce:VOR:PRESet

                Arguments:
                """
                _cmd = "PRESet"
                args = []

            PRESet = PRESet()
            """
            SOURce:VOR:PRESet

            Arguments:
            """

            class REFerence(SCPINode):
                """
                SOURce:VOR:REFerence

                Arguments:
                """
                _cmd = "REFerence"
                args = []

                class DEViation(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:REFerence:DEViation

                    Arguments: 1
                    """
                    _cmd = "DEViation"
                    args = ["1"]

                DEViation = DEViation()
                """
                SOURce:VOR:REFerence:DEViation

                Arguments: 1
                """

            REFerence = REFerence()
            """
            SOURce:VOR:REFerence

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:VOR:SOURce

                Arguments: INT2, INTernal2,EXTernal
                """
                _cmd = "SOURce"
                args = ["INT2", "INTernal2,EXTernal"]

            SOURce = SOURce()
            """
            SOURce:VOR:SOURce

            Arguments: INT2, INTernal2,EXTernal
            """

            class STATe(SCPINode, SCPIBool):
                """
                SOURce:VOR:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SOURce:VOR:STATe

            Arguments: 1, ON, OFF
            """

            class SUBCarrier(SCPINode):
                """
                SOURce:VOR:SUBCarrier

                Arguments:
                """
                _cmd = "SUBCarrier"
                args = []

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:SUBCarrier:DEPTh

                    Arguments: 1
                    """
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()
                """
                SOURce:VOR:SUBCarrier:DEPTh

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:SUBCarrier:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()
                """
                SOURce:VOR:SUBCarrier:FREQuency

                Arguments: 1
                """

            SUBCarrier = SUBCarrier()
            """
            SOURce:VOR:SUBCarrier

            Arguments:
            """

            class VAR(SCPINode):
                """
                SOURce:VOR:VAR

                Arguments:
                """
                _cmd = "VAR"
                args = []

                class DEPTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:VAR:DEPTh

                    Arguments: 1
                    """
                    _cmd = "DEPTh"
                    args = ["1"]

                DEPTh = DEPTh()
                """
                SOURce:VOR:VAR:DEPTh

                Arguments: 1
                """

                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:VOR:VAR:FREQuency

                    Arguments: 1
                    """
                    _cmd = "FREQuency"
                    args = ["1"]

                FREQuency = FREQuency()
                """
                SOURce:VOR:VAR:FREQuency

                Arguments: 1
                """

            VAR = VAR()
            """
            SOURce:VOR:VAR

            Arguments:
            """

        VOR = VOR()
        """
        SOURce:VOR

        Arguments:
        """

    SOURce = SOURce()
    """
    SOURce

    Arguments:
    """

    class SPecial_functio(SCPINode, SCPIQuery, SCPISet):
        """
        SPecial_functio

        Arguments: <numeric_value>,<numeric_value>
        """
        _cmd = "SPecial_functio"
        args = ["<numeric_value>,<numeric_value>"]

    SPecial_functio = SPecial_functio()
    """
    SPecial_functio

    Arguments: <numeric_value>,<numeric_value>
    """

    class STATus(SCPINode, SCPISet):
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

            class DQUestionable(SCPINode):
                """
                STATus:DEVice:DQUestionable

                Arguments:
                """
                _cmd = "DQUestionable"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:DQUestionable:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:DEVice:DQUestionable:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:DEVice:DQUestionable:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:DEVice:DQUestionable:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:DQUestionable:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:DEVice:DQUestionable:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:DQUestionable:NTRansition

                    Arguments:
                    """
                    _cmd = "NTRansition"
                    args = []

                NTRansition = NTRansition()
                """
                STATus:DEVice:DQUestionable:NTRansition

                Arguments:
                """

                class PTRansition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:DQUestionable:PTRansition

                    Arguments:
                    """
                    _cmd = "PTRansition"
                    args = []

                PTRansition = PTRansition()
                """
                STATus:DEVice:DQUestionable:PTRansition

                Arguments:
                """

            DQUestionable = DQUestionable()
            """
            STATus:DEVice:DQUestionable

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

            class NTRansition(SCPINode, SCPIQuery):
                """
                STATus:DEVice:NTRansition

                Arguments:
                """
                _cmd = "NTRansition"
                args = []

            NTRansition = NTRansition()
            """
            STATus:DEVice:NTRansition

            Arguments:
            """

            class PTRansition(SCPINode, SCPIQuery):
                """
                STATus:DEVice:PTRansition

                Arguments:
                """
                _cmd = "PTRansition"
                args = []

            PTRansition = PTRansition()
            """
            STATus:DEVice:PTRansition

            Arguments:
            """

            class SINTegrity(SCPINode):
                """
                STATus:DEVice:SINTegrity

                Arguments:
                """
                _cmd = "SINTegrity"
                args = []

                class AMPLitude(SCPINode):
                    """
                    STATus:DEVice:SINTegrity:AMPLitude

                    Arguments:
                    """
                    _cmd = "AMPLitude"
                    args = []

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:AMPLitude:CONDition

                        Arguments:
                        """
                        _cmd = "CONDition"
                        args = []

                    CONDition = CONDition()
                    """
                    STATus:DEVice:SINTegrity:AMPLitude:CONDition

                    Arguments:
                    """

                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        STATus:DEVice:SINTegrity:AMPLitude:ENABle

                        Arguments: 1
                        """
                        _cmd = "ENABle"
                        args = ["1"]

                    ENABle = ENABle()
                    """
                    STATus:DEVice:SINTegrity:AMPLitude:ENABle

                    Arguments: 1
                    """

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:AMPLitude:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:DEVice:SINTegrity:AMPLitude:EVENt

                    Arguments:
                    """

                    class NTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:AMPLitude:NTRansition

                        Arguments:
                        """
                        _cmd = "NTRansition"
                        args = []

                    NTRansition = NTRansition()
                    """
                    STATus:DEVice:SINTegrity:AMPLitude:NTRansition

                    Arguments:
                    """

                    class PTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:AMPLitude:PTRansition

                        Arguments:
                        """
                        _cmd = "PTRansition"
                        args = []

                    PTRansition = PTRansition()
                    """
                    STATus:DEVice:SINTegrity:AMPLitude:PTRansition

                    Arguments:
                    """

                AMPLitude = AMPLitude()
                """
                STATus:DEVice:SINTegrity:AMPLitude

                Arguments:
                """

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:SINTegrity:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:DEVice:SINTegrity:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:DEVice:SINTegrity:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:DEVice:SINTegrity:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:SINTegrity:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:DEVice:SINTegrity:EVENt

                Arguments:
                """

                class FREQuency(SCPINode):
                    """
                    STATus:DEVice:SINTegrity:FREQuency

                    Arguments:
                    """
                    _cmd = "FREQuency"
                    args = []

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:FREQuency:CONDition

                        Arguments:
                        """
                        _cmd = "CONDition"
                        args = []

                    CONDition = CONDition()
                    """
                    STATus:DEVice:SINTegrity:FREQuency:CONDition

                    Arguments:
                    """

                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        STATus:DEVice:SINTegrity:FREQuency:ENABle

                        Arguments: 1
                        """
                        _cmd = "ENABle"
                        args = ["1"]

                    ENABle = ENABle()
                    """
                    STATus:DEVice:SINTegrity:FREQuency:ENABle

                    Arguments: 1
                    """

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:FREQuency:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:DEVice:SINTegrity:FREQuency:EVENt

                    Arguments:
                    """

                    class NTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:FREQuency:NTRansition

                        Arguments:
                        """
                        _cmd = "NTRansition"
                        args = []

                    NTRansition = NTRansition()
                    """
                    STATus:DEVice:SINTegrity:FREQuency:NTRansition

                    Arguments:
                    """

                    class PTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:FREQuency:PTRansition

                        Arguments:
                        """
                        _cmd = "PTRansition"
                        args = []

                    PTRansition = PTRansition()
                    """
                    STATus:DEVice:SINTegrity:FREQuency:PTRansition

                    Arguments:
                    """

                FREQuency = FREQuency()
                """
                STATus:DEVice:SINTegrity:FREQuency

                Arguments:
                """

                class HARDware(SCPINode):
                    """
                    STATus:DEVice:SINTegrity:HARDware

                    Arguments:
                    """
                    _cmd = "HARDware"
                    args = []

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:HARDware:CONDition

                        Arguments:
                        """
                        _cmd = "CONDition"
                        args = []

                    CONDition = CONDition()
                    """
                    STATus:DEVice:SINTegrity:HARDware:CONDition

                    Arguments:
                    """

                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        STATus:DEVice:SINTegrity:HARDware:ENABle

                        Arguments: 1
                        """
                        _cmd = "ENABle"
                        args = ["1"]

                    ENABle = ENABle()
                    """
                    STATus:DEVice:SINTegrity:HARDware:ENABle

                    Arguments: 1
                    """

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:HARDware:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:DEVice:SINTegrity:HARDware:EVENt

                    Arguments:
                    """

                    class NTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:HARDware:NTRansition

                        Arguments:
                        """
                        _cmd = "NTRansition"
                        args = []

                    NTRansition = NTRansition()
                    """
                    STATus:DEVice:SINTegrity:HARDware:NTRansition

                    Arguments:
                    """

                    class PTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:HARDware:PTRansition

                        Arguments:
                        """
                        _cmd = "PTRansition"
                        args = []

                    PTRansition = PTRansition()
                    """
                    STATus:DEVice:SINTegrity:HARDware:PTRansition

                    Arguments:
                    """

                HARDware = HARDware()
                """
                STATus:DEVice:SINTegrity:HARDware

                Arguments:
                """

                class MODulation(SCPINode):
                    """
                    STATus:DEVice:SINTegrity:MODulation

                    Arguments:
                    """
                    _cmd = "MODulation"
                    args = []

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:MODulation:CONDition

                        Arguments:
                        """
                        _cmd = "CONDition"
                        args = []

                    CONDition = CONDition()
                    """
                    STATus:DEVice:SINTegrity:MODulation:CONDition

                    Arguments:
                    """

                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        STATus:DEVice:SINTegrity:MODulation:ENABle

                        Arguments: 1
                        """
                        _cmd = "ENABle"
                        args = ["1"]

                    ENABle = ENABle()
                    """
                    STATus:DEVice:SINTegrity:MODulation:ENABle

                    Arguments: 1
                    """

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:MODulation:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:DEVice:SINTegrity:MODulation:EVENt

                    Arguments:
                    """

                    class NTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:MODulation:NTRansition

                        Arguments:
                        """
                        _cmd = "NTRansition"
                        args = []

                    NTRansition = NTRansition()
                    """
                    STATus:DEVice:SINTegrity:MODulation:NTRansition

                    Arguments:
                    """

                    class PTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:MODulation:PTRansition

                        Arguments:
                        """
                        _cmd = "PTRansition"
                        args = []

                    PTRansition = PTRansition()
                    """
                    STATus:DEVice:SINTegrity:MODulation:PTRansition

                    Arguments:
                    """

                MODulation = MODulation()
                """
                STATus:DEVice:SINTegrity:MODulation

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:SINTegrity:NTRansition

                    Arguments:
                    """
                    _cmd = "NTRansition"
                    args = []

                NTRansition = NTRansition()
                """
                STATus:DEVice:SINTegrity:NTRansition

                Arguments:
                """

                class PTRansition(SCPINode, SCPIQuery):
                    """
                    STATus:DEVice:SINTegrity:PTRansition

                    Arguments:
                    """
                    _cmd = "PTRansition"
                    args = []

                PTRansition = PTRansition()
                """
                STATus:DEVice:SINTegrity:PTRansition

                Arguments:
                """

                class REFerence(SCPINode):
                    """
                    STATus:DEVice:SINTegrity:REFerence

                    Arguments:
                    """
                    _cmd = "REFerence"
                    args = []

                    class CONDition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:REFerence:CONDition

                        Arguments:
                        """
                        _cmd = "CONDition"
                        args = []

                    CONDition = CONDition()
                    """
                    STATus:DEVice:SINTegrity:REFerence:CONDition

                    Arguments:
                    """

                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        STATus:DEVice:SINTegrity:REFerence:ENABle

                        Arguments: 1
                        """
                        _cmd = "ENABle"
                        args = ["1"]

                    ENABle = ENABle()
                    """
                    STATus:DEVice:SINTegrity:REFerence:ENABle

                    Arguments: 1
                    """

                    class EVENt(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:REFerence:EVENt

                        Arguments:
                        """
                        _cmd = "EVENt"
                        args = []

                    EVENt = EVENt()
                    """
                    STATus:DEVice:SINTegrity:REFerence:EVENt

                    Arguments:
                    """

                    class NTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:REFerence:NTRansition

                        Arguments:
                        """
                        _cmd = "NTRansition"
                        args = []

                    NTRansition = NTRansition()
                    """
                    STATus:DEVice:SINTegrity:REFerence:NTRansition

                    Arguments:
                    """

                    class PTRansition(SCPINode, SCPIQuery):
                        """
                        STATus:DEVice:SINTegrity:REFerence:PTRansition

                        Arguments:
                        """
                        _cmd = "PTRansition"
                        args = []

                    PTRansition = PTRansition()
                    """
                    STATus:DEVice:SINTegrity:REFerence:PTRansition

                    Arguments:
                    """

                REFerence = REFerence()
                """
                STATus:DEVice:SINTegrity:REFerence

                Arguments:
                """

            SINTegrity = SINTegrity()
            """
            STATus:DEVice:SINTegrity

            Arguments:
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

            class BASeband(SCPINode):
                """
                STATus:OPERation:BASeband

                Arguments:
                """
                _cmd = "BASeband"
                args = []

                class CONDition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BASeband:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:OPERation:BASeband:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BASeband:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:OPERation:BASeband:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:BASeband:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:OPERation:BASeband:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BASeband:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:OPERation:BASeband:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BASeband:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:OPERation:BASeband:PTRansition

                Arguments: 1
                """

            BASeband = BASeband()
            """
            STATus:OPERation:BASeband

            Arguments:
            """

            class BIT(SCPINodeN):
                """
                STATus:OPERation:BIT

                Arguments:
                """
                _cmd = "BIT"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:BIT:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:OPERation:BIT:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BIT:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:OPERation:BIT:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:OPERation:BIT:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:OPERation:BIT:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIBool):
                    """
                    STATus:OPERation:BIT:NTRansition

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "NTRansition"
                    args = ["1", "ON", "OFF"]

                NTRansition = NTRansition()
                """
                STATus:OPERation:BIT:NTRansition

                Arguments: 1, ON, OFF
                """

                class PTRansition(SCPINode, SCPIBool):
                    """
                    STATus:OPERation:BIT:PTRansition

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "PTRansition"
                    args = ["1", "ON", "OFF"]

                PTRansition = PTRansition()
                """
                STATus:OPERation:BIT:PTRansition

                Arguments: 1, ON, OFF
                """

            BIT = BIT()
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
                _cmd = "CONDition"
                args = ["1"]

            CONDition = CONDition()
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
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()
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
                _cmd = "EVENt"
                args = []

            EVENt = EVENt()
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
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()
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
                _cmd = "NTRanstition"
                args = ["1"]

            NTRanstition = NTRanstition()
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
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()
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
                _cmd = "PTRanstition"
                args = ["1"]

            PTRanstition = PTRanstition()
            """
            STATus:OPERation:PTRanstition

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
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/790fdbfc3c41487f.htm#ID_e484e63b71e7fde70a00206a00a80b3f-98d3fe7771e7fde70a00206a012bc823-en-US>`_

            Arguments:
            """
            _cmd = "PRESet"
            args = []

        PRESet = PRESet()
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
            _cmd = "QUEStionable"
            args = []

            class BERT(SCPINode):
                """
                STATus:QUEStionable:BERT

                Arguments:
                """
                _cmd = "BERT"
                args = []

                class CONDition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:BERT:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:QUEStionable:BERT:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:BERT:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:QUEStionable:BERT:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:BERT:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:QUEStionable:BERT:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:BERT:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:QUEStionable:BERT:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:BERT:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:QUEStionable:BERT:PTRansition

                Arguments: 1
                """

            BERT = BERT()
            """
            STATus:QUEStionable:BERT

            Arguments:
            """

            class BIT(SCPINodeN):
                """
                STATus:QUEStionable:BIT

                Arguments:
                """
                _cmd = "BIT"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:BIT:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:QUEStionable:BIT:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIBool):
                    """
                    STATus:QUEStionable:BIT:ENABle

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "ENABle"
                    args = ["1", "ON", "OFF"]

                ENABle = ENABle()
                """
                STATus:QUEStionable:BIT:ENABle

                Arguments: 1, ON, OFF
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:BIT:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:QUEStionable:BIT:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIBool):
                    """
                    STATus:QUEStionable:BIT:NTRansition

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "NTRansition"
                    args = ["1", "ON", "OFF"]

                NTRansition = NTRansition()
                """
                STATus:QUEStionable:BIT:NTRansition

                Arguments: 1, ON, OFF
                """

                class PTRansition(SCPINode, SCPIBool):
                    """
                    STATus:QUEStionable:BIT:PTRansition

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "PTRansition"
                    args = ["1", "ON", "OFF"]

                PTRansition = PTRansition()
                """
                STATus:QUEStionable:BIT:PTRansition

                Arguments: 1, ON, OFF
                """

            BIT = BIT()
            """
            STATus:QUEStionable:BIT

            Arguments:
            """

            class CALibration(SCPINode):
                """
                STATus:QUEStionable:CALibration

                Arguments:
                """
                _cmd = "CALibration"
                args = []

                class CONDition(SCPINode, SCPIQuery, SCPISet):
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

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:CALibration:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:QUEStionable:CALibration:EVENt

                Arguments:
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

            CALibration = CALibration()
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
                _cmd = "CONDition"
                args = ["1"]

            CONDition = CONDition()
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
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()
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
                _cmd = "EVENt"
                args = []

            EVENt = EVENt()
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
                _cmd = "FREQuency"
                args = []

                class CONDition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:FREQuency:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:QUEStionable:FREQuency:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:FREQuency:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:QUEStionable:FREQuency:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:FREQuency:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:QUEStionable:FREQuency:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:FREQuency:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:QUEStionable:FREQuency:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:FREQuency:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:QUEStionable:FREQuency:PTRansition

                Arguments: 1
                """

            FREQuency = FREQuency()
            """
            STATus:QUEStionable:FREQuency

            Arguments:
            """

            class MODulation(SCPINode):
                """
                STATus:QUEStionable:MODulation

                Arguments:
                """
                _cmd = "MODulation"
                args = []

                class CONDition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:MODulation:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:QUEStionable:MODulation:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:MODulation:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:QUEStionable:MODulation:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:MODulation:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:QUEStionable:MODulation:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:MODulation:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:QUEStionable:MODulation:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:MODulation:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:QUEStionable:MODulation:PTRansition

                Arguments: 1
                """

            MODulation = MODulation()
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
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()
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
                _cmd = "NTRanstition"
                args = ["1"]

            NTRanstition = NTRanstition()
            """
            STATus:QUEStionable:NTRanstition

            Arguments: 1
            """

            class PAGing(SCPINode):
                """
                STATus:QUEStionable:PAGing

                Arguments:
                """
                _cmd = "PAGing"
                args = []

                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:PAGing:CONDition

                    Arguments:
                    """
                    _cmd = "CONDition"
                    args = []

                CONDition = CONDition()
                """
                STATus:QUEStionable:PAGing:CONDition

                Arguments:
                """

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:PAGing:ENABle

                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]

                ENABle = ENABle()
                """
                STATus:QUEStionable:PAGing:ENABle

                Arguments: 1
                """

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:PAGing:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:QUEStionable:PAGing:EVENt

                Arguments:
                """

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:PAGing:NTRansition

                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]

                NTRansition = NTRansition()
                """
                STATus:QUEStionable:PAGing:NTRansition

                Arguments: 1
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:PAGing:PTRansition

                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]

                PTRansition = PTRansition()
                """
                STATus:QUEStionable:PAGing:PTRansition

                Arguments: 1
                """

            PAGing = PAGing()
            """
            STATus:QUEStionable:PAGing

            Arguments:
            """

            class POWer(SCPINode):
                """
                STATus:QUEStionable:POWer

                Arguments:
                """
                _cmd = "POWer"
                args = []

                class CONDition(SCPINode, SCPIQuery, SCPISet):
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

                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:POWer:EVENt

                    Arguments:
                    """
                    _cmd = "EVENt"
                    args = []

                EVENt = EVENt()
                """
                STATus:QUEStionable:POWer:EVENt

                Arguments:
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

            POWer = POWer()
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
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()
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
                _cmd = "PTRanstition"
                args = ["1"]

            PTRanstition = PTRanstition()
            """
            STATus:QUEStionable:PTRanstition

            Arguments: 1
            """

        QUEStionable = QUEStionable()
        """
        STATus:QUEStionable

        Arguments:
        """

    STATus = STATus()
    """
    STATus

    Arguments:
    """

    class STore(SCPINode, SCPISet):
        """
        STore

        Arguments: 1
        """
        _cmd = "STore"
        args = ["1"]

        class Fast(SCPINode, SCPISet):
            """
            STore:Fast

            Arguments: 1
            """
            _cmd = "Fast"
            args = ["1"]

        Fast = Fast()
        """
        STore:Fast

        Arguments: 1
        """

    STore = STore()
    """
    STore

    Arguments: 1
    """

    class SWEep(SCPINode, SCPIQuery):
        """
        SWEep

        Arguments:
        """
        _cmd = "SWEep"
        args = []

        class CFRQ(SCPINode):
            """
            SWEep:CFRQ

            Arguments:
            """
            _cmd = "CFRQ"
            args = []

            class LOGinc(SCPINode, SCPISet):
                """
                SWEep:CFRQ:LOGinc

                Arguments: 1
                """
                _cmd = "LOGinc"
                args = ["1"]

            LOGinc = LOGinc()
            """
            SWEep:CFRQ:LOGinc

            Arguments: 1
            """

            class MKRNum(SCPINode, SCPISet):
                """
                SWEep:CFRQ:MKRNum

                Arguments: 1
                """
                _cmd = "MKRNum"
                args = ["1"]

            MKRNum = MKRNum()
            """
            SWEep:CFRQ:MKRNum

            Arguments: 1
            """

            class MKRoff(SCPINode, SCPISet):
                """
                SWEep:CFRQ:MKRoff

                Arguments:
                """
                _cmd = "MKRoff"
                args = []

            MKRoff = MKRoff()
            """
            SWEep:CFRQ:MKRoff

            Arguments:
            """

            class MKRon(SCPINode, SCPISet):
                """
                SWEep:CFRQ:MKRon

                Arguments:
                """
                _cmd = "MKRon"
                args = []

            MKRon = MKRon()
            """
            SWEep:CFRQ:MKRon

            Arguments:
            """

            class STARt(SCPINode, SCPISet):
                """
                SWEep:CFRQ:STARt

                Arguments: 1
                """
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()
            """
            SWEep:CFRQ:STARt

            Arguments: 1
            """

            class VALue(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:CFRQ:VALue

                Arguments: 1
                """
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()
            """
            SWEep:CFRQ:VALue

            Arguments: 1
            """

        CFRQ = CFRQ()
        """
        SWEep:CFRQ

        Arguments:
        """

        class FREQuency(SCPINode, SCPISet):
            """
            SWEep:FREQuency

            Arguments:
            """
            _cmd = "FREQuency"
            args = []

            class GENeration(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:FREQuency:GENeration

                Arguments: ANALog, STEPped
                """
                _cmd = "GENeration"
                args = ["ANALog", "STEPped"]

            GENeration = GENeration()
            """
            SWEep:FREQuency:GENeration

            Arguments: ANALog, STEPped
            """

            class SPACing(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:FREQuency:SPACing

                Arguments: LINear, LOGarithmic
                """
                _cmd = "SPACing"
                args = ["LINear", "LOGarithmic"]

            SPACing = SPACing()
            """
            SWEep:FREQuency:SPACing

            Arguments: LINear, LOGarithmic
            """

            class TIME(SCPINode):
                """
                SWEep:FREQuency:TIME

                Arguments:
                """
                _cmd = "TIME"
                args = []

                class STEP(SCPINode):
                    """
                    SWEep:FREQuency:TIME:STEP

                    Arguments:
                    """
                    _cmd = "STEP"
                    args = []

                    class INCRement(SCPINode, SCPIQuery):
                        """
                        SWEep:FREQuency:TIME:STEP:INCRement

                        Arguments: 1
                        """
                        _cmd = "INCRement"
                        args = ["1"]

                    INCRement = INCRement()
                    """
                    SWEep:FREQuency:TIME:STEP:INCRement

                    Arguments: 1
                    """

                STEP = STEP()
                """
                SWEep:FREQuency:TIME:STEP

                Arguments:
                """

            TIME = TIME()
            """
            SWEep:FREQuency:TIME

            Arguments:
            """

        FREQuency = FREQuency()
        """
        SWEep:FREQuency

        Arguments:
        """

        class INTF(SCPINode):
            """
            SWEep:INTF

            Arguments:
            """
            _cmd = "INTF"
            args = []

            class MKRNum(SCPINode, SCPISet):
                """
                SWEep:INTF:MKRNum

                Arguments: 1
                """
                _cmd = "MKRNum"
                args = ["1"]

            MKRNum = MKRNum()
            """
            SWEep:INTF:MKRNum

            Arguments: 1
            """

            class MKRoff(SCPINode, SCPISet):
                """
                SWEep:INTF:MKRoff

                Arguments:
                """
                _cmd = "MKRoff"
                args = []

            MKRoff = MKRoff()
            """
            SWEep:INTF:MKRoff

            Arguments:
            """

            class MKRon(SCPINode, SCPISet):
                """
                SWEep:INTF:MKRon

                Arguments:
                """
                _cmd = "MKRon"
                args = []

            MKRon = MKRon()
            """
            SWEep:INTF:MKRon

            Arguments:
            """

            class STARt(SCPINode, SCPISet):
                """
                SWEep:INTF:STARt

                Arguments: 1
                """
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()
            """
            SWEep:INTF:STARt

            Arguments: 1
            """

            class VALue(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:INTF:VALue

                Arguments: 1
                """
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()
            """
            SWEep:INTF:VALue

            Arguments: 1
            """

        INTF = INTF()
        """
        SWEep:INTF

        Arguments:
        """

        class LFGF(SCPINode):
            """
            SWEep:LFGF

            Arguments:
            """
            _cmd = "LFGF"
            args = []

            class MKRNum(SCPINode, SCPISet):
                """
                SWEep:LFGF:MKRNum

                Arguments: 1
                """
                _cmd = "MKRNum"
                args = ["1"]

            MKRNum = MKRNum()
            """
            SWEep:LFGF:MKRNum

            Arguments: 1
            """

            class MKRoff(SCPINode, SCPISet):
                """
                SWEep:LFGF:MKRoff

                Arguments:
                """
                _cmd = "MKRoff"
                args = []

            MKRoff = MKRoff()
            """
            SWEep:LFGF:MKRoff

            Arguments:
            """

            class MKRon(SCPINode, SCPISet):
                """
                SWEep:LFGF:MKRon

                Arguments:
                """
                _cmd = "MKRon"
                args = []

            MKRon = MKRon()
            """
            SWEep:LFGF:MKRon

            Arguments:
            """

            class STARt(SCPINode, SCPISet):
                """
                SWEep:LFGF:STARt

                Arguments: 1
                """
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()
            """
            SWEep:LFGF:STARt

            Arguments: 1
            """

            class VALue(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:LFGF:VALue

                Arguments: 1
                """
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()
            """
            SWEep:LFGF:VALue

            Arguments: 1
            """

        LFGF = LFGF()
        """
        SWEep:LFGF

        Arguments:
        """

        class LFGL(SCPINode):
            """
            SWEep:LFGL

            Arguments:
            """
            _cmd = "LFGL"
            args = []

            class MKRNum(SCPINode, SCPISet):
                """
                SWEep:LFGL:MKRNum

                Arguments: 1
                """
                _cmd = "MKRNum"
                args = ["1"]

            MKRNum = MKRNum()
            """
            SWEep:LFGL:MKRNum

            Arguments: 1
            """

            class MKRoff(SCPINode, SCPISet):
                """
                SWEep:LFGL:MKRoff

                Arguments:
                """
                _cmd = "MKRoff"
                args = []

            MKRoff = MKRoff()
            """
            SWEep:LFGL:MKRoff

            Arguments:
            """

            class MKRon(SCPINode, SCPISet):
                """
                SWEep:LFGL:MKRon

                Arguments:
                """
                _cmd = "MKRon"
                args = []

            MKRon = MKRon()
            """
            SWEep:LFGL:MKRon

            Arguments:
            """

            class STARt(SCPINode, SCPISet):
                """
                SWEep:LFGL:STARt

                Arguments: 1
                """
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()
            """
            SWEep:LFGL:STARt

            Arguments: 1
            """

            class VALue(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:LFGL:VALue

                Arguments: 1
                """
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()
            """
            SWEep:LFGL:VALue

            Arguments: 1
            """

        LFGL = LFGL()
        """
        SWEep:LFGL

        Arguments:
        """

        class MKRoff(SCPINode, SCPISet):
            """
            SWEep:MKRoff

            Arguments:
            """
            _cmd = "MKRoff"
            args = []

        MKRoff = MKRoff()
        """
        SWEep:MKRoff

        Arguments:
        """

        class MKRon(SCPINode, SCPISet):
            """
            SWEep:MKRon

            Arguments:
            """
            _cmd = "MKRon"
            args = []

        MKRon = MKRon()
        """
        SWEep:MKRon

        Arguments:
        """

        class RESet(SCPINode, SCPISet):
            """
            SWEep:RESet

            Arguments:
            """
            _cmd = "RESet"
            args = []

        RESet = RESet()
        """
        SWEep:RESet

        Arguments:
        """

        class RFLV(SCPINode):
            """
            SWEep:RFLV

            Arguments:
            """
            _cmd = "RFLV"
            args = []

            class MKRNum(SCPINode, SCPISet):
                """
                SWEep:RFLV:MKRNum

                Arguments: 1
                """
                _cmd = "MKRNum"
                args = ["1"]

            MKRNum = MKRNum()
            """
            SWEep:RFLV:MKRNum

            Arguments: 1
            """

            class MKRoff(SCPINode, SCPISet):
                """
                SWEep:RFLV:MKRoff

                Arguments:
                """
                _cmd = "MKRoff"
                args = []

            MKRoff = MKRoff()
            """
            SWEep:RFLV:MKRoff

            Arguments:
            """

            class MKRon(SCPINode, SCPISet):
                """
                SWEep:RFLV:MKRon

                Arguments:
                """
                _cmd = "MKRon"
                args = []

            MKRon = MKRon()
            """
            SWEep:RFLV:MKRon

            Arguments:
            """

            class STARt(SCPINode, SCPISet):
                """
                SWEep:RFLV:STARt

                Arguments: 1
                """
                _cmd = "STARt"
                args = ["1"]

            STARt = STARt()
            """
            SWEep:RFLV:STARt

            Arguments: 1
            """

            class VALue(SCPINode, SCPIQuery, SCPISet):
                """
                SWEep:RFLV:VALue

                Arguments: 1
                """
                _cmd = "VALue"
                args = ["1"]

            VALue = VALue()
            """
            SWEep:RFLV:VALue

            Arguments: 1
            """

        RFLV = RFLV()
        """
        SWEep:RFLV

        Arguments:
        """

    SWEep = SWEep()
    """
    SWEep

    Arguments:
    """

    class SYSTem(SCPINode, SCPISet):
        """
        SYSTem

        Arguments:
        """
        _cmd = "SYSTem"
        args = []

        class ALTernate(SCPINode):
            """
            SYSTem:ALTernate

            Arguments:
            """
            _cmd = "ALTernate"
            args = []

            class STATe(SCPINode, SCPIBool):
                """
                SYSTem:ALTernate:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SYSTem:ALTernate:STATe

            Arguments: 1, ON, OFF
            """

        ALTernate = ALTernate()
        """
        SYSTem:ALTernate

        Arguments:
        """

        class BEEPer(SCPINode):
            """
            SYSTem:BEEPer

            Arguments:
            """
            _cmd = "BEEPer"
            args = []

            class STATe(SCPINode, SCPIBool):
                """
                SYSTem:BEEPer:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SYSTem:BEEPer:STATe

            Arguments: 1, ON, OFF
            """

        BEEPer = BEEPer()
        """
        SYSTem:BEEPer

        Arguments:
        """

        class CAPability(SCPINode, SCPIQuery):
            """
            SYSTem:CAPability

            Arguments:
            """
            _cmd = "CAPability"
            args = []

        CAPability = CAPability()
        """
        SYSTem:CAPability

        Arguments:
        """

        class COMMunicate(SCPINode, SCPISet):
            """
            SYSTem:COMMunicate

            Arguments:
            """
            _cmd = "COMMunicate"
            args = []

            class GPIB(SCPINode):
                """
                SYSTem:COMMunicate:GPIB

                Arguments:
                """
                _cmd = "GPIB"
                args = []

                class ADDRess(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:GPIB:ADDRess

                    Arguments: 1
                    """
                    _cmd = "ADDRess"
                    args = ["1"]

                ADDRess = ADDRess()
                """
                SYSTem:COMMunicate:GPIB:ADDRess

                Arguments: 1
                """

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
                        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2c2c393234144769.htm#ID_048f099271caf99b0a00206a00d986d1-b9d7e0eb71caf99b0a00206a012bc823-en-US>`_

                        Arguments: 1
                        """
                        _cmd = "ADDRess"
                        args = ["1"]

                    ADDRess = ADDRess()
                    """
                    `SYSTem:COMMunicate:GPIB:SELF:ADDRess
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2c2c393234144769.htm#ID_048f099271caf99b0a00206a00d986d1-b9d7e0eb71caf99b0a00206a012bc823-en-US>`_

                    Arguments: 1
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

            class GTLocal(SCPINode, SCPISet):
                """
                SYSTem:COMMunicate:GTLocal

                Arguments:
                """
                _cmd = "GTLocal"
                args = []

            GTLocal = GTLocal()
            """
            SYSTem:COMMunicate:GTLocal

            Arguments:
            """

            class LAN(SCPINode):
                """
                SYSTem:COMMunicate:LAN

                Arguments:
                """
                _cmd = "LAN"
                args = []

                class CONFig(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:CONFig

                    Arguments: AIP, AUTO, DHCP, MANual
                    """
                    _cmd = "CONFig"
                    args = ["AIP", "AUTO", "DHCP", "MANual"]

                CONFig = CONFig()
                """
                SYSTem:COMMunicate:LAN:CONFig

                Arguments: AIP, AUTO, DHCP, MANual
                """

                class DEFaults(SCPINode, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:DEFaults

                    Arguments:
                    """
                    _cmd = "DEFaults"
                    args = []

                DEFaults = DEFaults()
                """
                SYSTem:COMMunicate:LAN:DEFaults

                Arguments:
                """

                class DOMain(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:DOMain

                    Arguments: 'string'
                    """
                    _cmd = "DOMain"
                    args = ["'string'"]

                DOMain = DOMain()
                """
                SYSTem:COMMunicate:LAN:DOMain

                Arguments: 'string'
                """

                class GATeway(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:GATeway

                    Arguments: 'string'
                    """
                    _cmd = "GATeway"
                    args = ["'string'"]

                GATeway = GATeway()
                """
                SYSTem:COMMunicate:LAN:GATeway

                Arguments: 'string'
                """

                class HOSTname(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:HOSTname

                    Arguments: 'string'
                    """
                    _cmd = "HOSTname"
                    args = ["'string'"]

                HOSTname = HOSTname()
                """
                SYSTem:COMMunicate:LAN:HOSTname

                Arguments: 'string'
                """

                class RESTart(SCPINode, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:RESTart

                    Arguments:
                    """
                    _cmd = "RESTart"
                    args = []

                RESTart = RESTart()
                """
                SYSTem:COMMunicate:LAN:RESTart

                Arguments:
                """

                class SUBNet(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:LAN:SUBNet

                    Arguments: 'string'
                    """
                    _cmd = "SUBNet"
                    args = ["'string'"]

                SUBNet = SUBNet()
                """
                SYSTem:COMMunicate:LAN:SUBNet

                Arguments: 'string'
                """

            LAN = LAN()
            """
            SYSTem:COMMunicate:LAN

            Arguments:
            """

            class PMETer(SCPINode, SCPISet):
                """
                SYSTem:COMMunicate:PMETer

                Arguments:
                """
                _cmd = "PMETer"
                args = []

                class ADDRess(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:PMETer:ADDRess

                    Arguments: 1
                    """
                    _cmd = "ADDRess"
                    args = ["1"]

                ADDRess = ADDRess()
                """
                SYSTem:COMMunicate:PMETer:ADDRess

                Arguments: 1
                """

                class CHANnel(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:PMETer:CHANnel

                    Arguments: A, B
                    """
                    _cmd = "CHANnel"
                    args = ["A", "B"]

                CHANnel = CHANnel()
                """
                SYSTem:COMMunicate:PMETer:CHANnel

                Arguments: A, B
                """

                class TIMeout(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:PMETer:TIMeout

                    Arguments: 1
                    """
                    _cmd = "TIMeout"
                    args = ["1"]

                TIMeout = TIMeout()
                """
                SYSTem:COMMunicate:PMETer:TIMeout

                Arguments: 1
                """

            PMETer = PMETer()
            """
            SYSTem:COMMunicate:PMETer

            Arguments:
            """

            class SERial(SCPINode, SCPISet):
                """
                SYSTem:COMMunicate:SERial

                Arguments:
                """
                _cmd = "SERial"
                args = []

                class PARity(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:COMMunicate:SERial:PARity
                    <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/007a87c5bc084b7e.htm#ID_ed84c7fa71cc127d0a00206a0162bb19-92f11b0771cc127d0a00206a012bc823-en-US>`_

                    Arguments: EVEN, NONE, ODD, ONE, ZERO
                    """
                    _cmd = "PARity"
                    args = ["EVEN", "NONE", "ODD", "ONE", "ZERO"]

                PARity = PARity()
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
                    _cmd = "RESet"
                    args = []

                RESet = RESet()
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
                    _cmd = "SBITs"
                    args = ["1"]

                SBITs = SBITs()
                """
                `SYSTem:COMMunicate:SERial:SBITs
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e6a3b756c8454b50.htm#ID_48a728cc71cc19b10a00206a014314e1-a83e843471cc19b10a00206a012bc823-en-US>`_

                Arguments: 1
                """

            SERial = SERial()
            """
            SYSTem:COMMunicate:SERial

            Arguments:
            """

        COMMunicate = COMMunicate()
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
            _cmd = "DATE"
            args = []

            class LOCal(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:DATE:LOCal

                Arguments: <integer>,<integer>,<integer>
                """
                _cmd = "LOCal"
                args = ["<integer>,<integer>,<integer>"]

            LOCal = LOCal()
            """
            SYSTem:DATE:LOCal

            Arguments: <integer>,<integer>,<integer>
            """

        DATE = DATE()
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
            _cmd = "DFPRint"
            args = ["'string'"]

            class HISTory(SCPINode):
                """
                SYSTem:DFPRint:HISTory

                Arguments:
                """
                _cmd = "HISTory"
                args = []

                class COUNt(SCPINode, SCPIQuery):
                    """
                    SYSTem:DFPRint:HISTory:COUNt

                    Arguments:
                    """
                    _cmd = "COUNt"
                    args = []

                COUNt = COUNt()
                """
                SYSTem:DFPRint:HISTory:COUNt

                Arguments:
                """

                class ENTRy(SCPINode, SCPIQuery):
                    """
                    SYSTem:DFPRint:HISTory:ENTRy

                    Arguments: 1
                    """
                    _cmd = "ENTRy"
                    args = ["1"]

                ENTRy = ENTRy()
                """
                SYSTem:DFPRint:HISTory:ENTRy

                Arguments: 1
                """

            HISTory = HISTory()
            """
            SYSTem:DFPRint:HISTory

            Arguments:
            """

        DFPRint = DFPRint()
        """
        SYSTem:DFPRint

        Arguments: 'string'
        """

        class DISPlay(SCPINode):
            """
            SYSTem:DISPlay

            Arguments:
            """
            _cmd = "DISPlay"
            args = []

            class UPDate(SCPINode, SCPIBool):
                """
                `SYSTem:DISPlay:UPDate
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f101e4cb6c3f422c.htm#ID_dc6f502b71cb0e3c0a00206a0114ff35-1059cab671cb0e3c0a00206a012bc823-en-US>`_

                Arguments: 1, ON, OFF
                """
                _cmd = "UPDate"
                args = ["1", "ON", "OFF"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SYSTem:DISPlay:UPDate:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SYSTem:DISPlay:UPDate:STATe

                Arguments: 1, ON, OFF
                """

            UPDate = UPDate()
            """
            `SYSTem:DISPlay:UPDate
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/f101e4cb6c3f422c.htm#ID_dc6f502b71cb0e3c0a00206a0114ff35-1059cab671cb0e3c0a00206a012bc823-en-US>`_

            Arguments: 1, ON, OFF
            """

        DISPlay = DISPlay()
        """
        SYSTem:DISPlay

        Arguments:
        """

        class DUMP(SCPINode):
            """
            SYSTem:DUMP

            Arguments:
            """
            _cmd = "DUMP"
            args = []

            class ERRor(SCPINode, SCPIQuery):
                """
                SYSTem:DUMP:ERRor

                Arguments:
                """
                _cmd = "ERRor"
                args = []

            ERRor = ERRor()
            """
            SYSTem:DUMP:ERRor

            Arguments:
            """

            class PRINter(SCPINode, SCPIQuery):
                """
                SYSTem:DUMP:PRINter

                Arguments:
                """
                _cmd = "PRINter"
                args = []

            PRINter = PRINter()
            """
            SYSTem:DUMP:PRINter

            Arguments:
            """

        DUMP = DUMP()
        """
        SYSTem:DUMP

        Arguments:
        """

        class ERRor(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:ERRor

            Arguments: NUMeric, STRing
            """
            _cmd = "ERRor"
            args = ["NUMeric", "STRing"]

            class COUNt(SCPINode, SCPIQuery):
                """
                `SYSTem:ERRor:COUNt
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/ba0d0e59bbb0493c.htm#ID_00c603b971d1daa50a00206a0178d1e6-77aa4c6371d1daa50a00206a012bc823-en-US>`_

                Arguments:
                """
                _cmd = "COUNt"
                args = []

            COUNt = COUNt()
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
                _cmd = "SCPI"
                args = []

                class SYNTax(SCPINode, SCPIBool):
                    """
                    SYSTem:ERRor:SCPI:SYNTax

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "SYNTax"
                    args = ["1", "ON", "OFF"]

                SYNTax = SYNTax()
                """
                SYSTem:ERRor:SCPI:SYNTax

                Arguments: 1, ON, OFF
                """

            SCPI = SCPI()
            """
            SYSTem:ERRor:SCPI

            Arguments:
            """

        ERRor = ERRor()
        """
        SYSTem:ERRor

        Arguments: NUMeric, STRing
        """

        class FILesystem(SCPINode):
            """
            SYSTem:FILesystem

            Arguments:
            """
            _cmd = "FILesystem"
            args = []

            class SAFemode(SCPINode, SCPIBool):
                """
                SYSTem:FILesystem:SAFemode

                Arguments: 1, ON, OFF
                """
                _cmd = "SAFemode"
                args = ["1", "ON", "OFF"]

            SAFemode = SAFemode()
            """
            SYSTem:FILesystem:SAFemode

            Arguments: 1, ON, OFF
            """

        FILesystem = FILesystem()
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
            _cmd = "FPReset"
            args = []

        FPReset = FPReset()
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
            _cmd = "HELP"
            args = []

            class HEADers(SCPINode, SCPIQuery):
                """
                SYSTem:HELP:HEADers

                Arguments: 'string'
                """
                _cmd = "HEADers"
                args = ["'string'"]

            HEADers = HEADers()
            """
            SYSTem:HELP:HEADers

            Arguments: 'string'
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

        class KEY(SCPINode):
            """
            SYSTem:KEY

            Arguments:
            """
            _cmd = "KEY"
            args = []

            class ASSign(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:KEY:ASSign

                Arguments: 1
                """
                _cmd = "ASSign"
                args = ["1"]

            ASSign = ASSign()
            """
            SYSTem:KEY:ASSign

            Arguments: 1
            """

            class CLEar(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:KEY:CLEar

                Arguments: 1
                """
                _cmd = "CLEar"
                args = ["1"]

            CLEar = CLEar()
            """
            SYSTem:KEY:CLEar

            Arguments: 1
            """

            class DISable(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:KEY:DISable

                Arguments: SAVE
                """
                _cmd = "DISable"
                args = ["SAVE"]

            DISable = DISable()
            """
            SYSTem:KEY:DISable

            Arguments: SAVE
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:KEY:ENABle

                Arguments: SAVE
                """
                _cmd = "ENABle"
                args = ["SAVE"]

            ENABle = ENABle()
            """
            SYSTem:KEY:ENABle

            Arguments: SAVE
            """

        KEY = KEY()
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
            _cmd = "KLOCk"
            args = ["1", "ON", "OFF"]

        KLOCk = KLOCk()
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
            _cmd = "LANGuage"
            args = ["'string'"]

        LANGuage = LANGuage()
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
            _cmd = "LOCK"
            args = []

            class NAME(SCPINode):
                """
                SYSTem:LOCK:NAME

                Arguments:
                """
                _cmd = "NAME"
                args = []

                class DETailed(SCPINode, SCPIQuery):
                    """
                    SYSTem:LOCK:NAME:DETailed

                    Arguments:
                    """
                    _cmd = "DETailed"
                    args = []

                DETailed = DETailed()
                """
                SYSTem:LOCK:NAME:DETailed

                Arguments:
                """

            NAME = NAME()
            """
            SYSTem:LOCK:NAME

            Arguments:
            """

            class OWNer(SCPINode, SCPIQuery):
                """
                SYSTem:LOCK:OWNer

                Arguments:
                """
                _cmd = "OWNer"
                args = []

                class DETailed(SCPINode, SCPIQuery):
                    """
                    SYSTem:LOCK:OWNer:DETailed

                    Arguments:
                    """
                    _cmd = "DETailed"
                    args = []

                DETailed = DETailed()
                """
                SYSTem:LOCK:OWNer:DETailed

                Arguments:
                """

            OWNer = OWNer()
            """
            SYSTem:LOCK:OWNer

            Arguments:
            """

            class RELease(SCPINode, SCPISet):
                """
                SYSTem:LOCK:RELease

                Arguments:
                """
                _cmd = "RELease"
                args = []

            RELease = RELease()
            """
            SYSTem:LOCK:RELease

            Arguments:
            """

            class REQuest(SCPINode):
                """
                SYSTem:LOCK:REQuest

                Arguments:
                """
                _cmd = "REQuest"
                args = []

                class EXCLusive(SCPINode, SCPIQuery):
                    """
                    SYSTem:LOCK:REQuest:EXCLusive

                    Arguments: <integer>, INFinite
                    """
                    _cmd = "EXCLusive"
                    args = ["<integer>", "INFinite"]

                EXCLusive = EXCLusive()
                """
                SYSTem:LOCK:REQuest:EXCLusive

                Arguments: <integer>, INFinite
                """

                class SHARed(SCPINode, SCPIQuery):
                    """
                    SYSTem:LOCK:REQuest:SHARed

                    Arguments: <string>,<integer>, INFinite
                    """
                    _cmd = "SHARed"
                    args = ["<string>,<integer>", "INFinite"]

                SHARed = SHARed()
                """
                SYSTem:LOCK:REQuest:SHARed

                Arguments: <string>,<integer>, INFinite
                """

            REQuest = REQuest()
            """
            SYSTem:LOCK:REQuest

            Arguments:
            """

            class SHARed(SCPINode):
                """
                SYSTem:LOCK:SHARed

                Arguments:
                """
                _cmd = "SHARed"
                args = []

                class STRing(SCPINode, SCPIQuery):
                    """
                    SYSTem:LOCK:SHARed:STRing

                    Arguments:
                    """
                    _cmd = "STRing"
                    args = []

                STRing = STRing()
                """
                SYSTem:LOCK:SHARed:STRing

                Arguments:
                """

            SHARed = SHARed()
            """
            SYSTem:LOCK:SHARed

            Arguments:
            """

            class TIMeout(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:LOCK:TIMeout

                Arguments: <integer>, INFinite
                """
                _cmd = "TIMeout"
                args = ["<integer>", "INFinite"]

            TIMeout = TIMeout()
            """
            SYSTem:LOCK:TIMeout

            Arguments: <integer>, INFinite
            """

        LOCK = LOCK()
        """
        SYSTem:LOCK

        Arguments:
        """

        class MMHead(SCPINode):
            """
            SYSTem:MMHead

            Arguments:
            """
            _cmd = "MMHead"
            args = []

            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:MMHead:SELect

                Arguments: FRONt, NONE, REAR
                """
                _cmd = "SELect"
                args = ["FRONt", "NONE", "REAR"]

            SELect = SELect()
            """
            SYSTem:MMHead:SELect

            Arguments: FRONt, NONE, REAR
            """

        MMHead = MMHead()
        """
        SYSTem:MMHead

        Arguments:
        """

        class MSEQuence(SCPINode):
            """
            SYSTem:MSEQuence

            Arguments:
            """
            _cmd = "MSEQuence"
            args = []

            class CATalog(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:MSEQuence:CATalog

                Arguments:
                """
                _cmd = "CATalog"
                args = []

            CATalog = CATalog()
            """
            SYSTem:MSEQuence:CATalog

            Arguments:
            """

            class DELete(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:MSEQuence:DELete

                Arguments: 'string'
                """
                _cmd = "DELete"
                args = ["'string'"]

            DELete = DELete()
            """
            SYSTem:MSEQuence:DELete

            Arguments: 'string'
            """

            class DWELl(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:MSEQuence:DWELl

                Arguments: 1
                """
                _cmd = "DWELl"
                args = ["1"]

            DWELl = DWELl()
            """
            SYSTem:MSEQuence:DWELl

            Arguments: 1
            """

            class RCL(SCPINode):
                """
                SYSTem:MSEQuence:RCL

                Arguments:
                """
                _cmd = "RCL"
                args = []

                class POINts(SCPINode, SCPIQuery):
                    """
                    SYSTem:MSEQuence:RCL:POINts

                    Arguments:
                    """
                    _cmd = "POINts"
                    args = []

                POINts = POINts()
                """
                SYSTem:MSEQuence:RCL:POINts

                Arguments:
                """

            RCL = RCL()
            """
            SYSTem:MSEQuence:RCL

            Arguments:
            """

            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:MSEQuence:SELect

                Arguments: 'string'
                """
                _cmd = "SELect"
                args = ["'string'"]

            SELect = SELect()
            """
            SYSTem:MSEQuence:SELect

            Arguments: 'string'
            """

        MSEQuence = MSEQuence()
        """
        SYSTem:MSEQuence

        Arguments:
        """

        class PDOWn(SCPINode, SCPISet):
            """
            SYSTem:PDOWn

            Arguments:
            """
            _cmd = "PDOWn"
            args = []

        PDOWn = PDOWn()
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
            _cmd = "PRESet"
            args = ["'string'"]

            class EXECute(SCPINode, SCPISet):
                """
                SYSTem:PRESet:EXECute

                Arguments:
                """
                _cmd = "EXECute"
                args = []

            EXECute = EXECute()
            """
            SYSTem:PRESet:EXECute

            Arguments:
            """

            class LANGuage(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:PRESet:LANGuage

                Arguments: 'string'
                """
                _cmd = "LANGuage"
                args = ["'string'"]

            LANGuage = LANGuage()
            """
            SYSTem:PRESet:LANGuage

            Arguments: 'string'
            """

            class PERSistent(SCPINode, SCPISet):
                """
                SYSTem:PRESet:PERSistent

                Arguments:
                """
                _cmd = "PERSistent"
                args = []

            PERSistent = PERSistent()
            """
            SYSTem:PRESet:PERSistent

            Arguments:
            """

            class PN(SCPINodeN, SCPIQuery, SCPISet):
                """
                SYSTem:PRESet:PN

                Arguments: NORMal, QUICk
                """
                _cmd = "PN"
                args = ["NORMal", "QUICk"]

            PN = PN()
            """
            SYSTem:PRESet:PN

            Arguments: NORMal, QUICk
            """

        PRESet = PRESet()
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
            _cmd = "PROTect"
            args = []

            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:PROTect:STATe
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2be619d631aa413c.htm#ID_8573e93571caebb10a00206a0185361b-8394d8f471caebb10a00206a012bc823-en-US>`_

                Arguments: <boolean>,<numeric_value>
                """
                _cmd = "STATe"
                args = ["<boolean>,<numeric_value>"]

            STATe = STATe()
            """
            `SYSTem:PROTect:STATe
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/2be619d631aa413c.htm#ID_8573e93571caebb10a00206a0185361b-8394d8f471caebb10a00206a012bc823-en-US>`_

            Arguments: <boolean>,<numeric_value>
            """

        PROTect = PROTect()
        """
        SYSTem:PROTect

        Arguments:
        """

        class RESet(SCPINode, SCPISet):
            """
            SYSTem:RESet

            Arguments: 'string'
            """
            _cmd = "RESet"
            args = ["'string'"]

        RESet = RESet()
        """
        SYSTem:RESet

        Arguments: 'string'
        """

        class SECurity(SCPINode, SCPIBool):
            """
            SYSTem:SECurity

            Arguments: 1, ON, OFF
            """
            _cmd = "SECurity"
            args = ["1", "ON", "OFF"]

            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:SECurity:COUNt

                Arguments: 1
                """
                _cmd = "COUNt"
                args = ["1"]

            COUNt = COUNt()
            """
            SYSTem:SECurity:COUNt

            Arguments: 1
            """

            class DISPlay(SCPINode, SCPIBool):
                """
                SYSTem:SECurity:DISPlay

                Arguments: 1, ON, OFF
                """
                _cmd = "DISPlay"
                args = ["1", "ON", "OFF"]

            DISPlay = DISPlay()
            """
            SYSTem:SECurity:DISPlay

            Arguments: 1, ON, OFF
            """

            class ERASeall(SCPINode, SCPISet):
                """
                SYSTem:SECurity:ERASeall

                Arguments:
                """
                _cmd = "ERASeall"
                args = []

            ERASeall = ERASeall()
            """
            SYSTem:SECurity:ERASeall

            Arguments:
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:SECurity:LEVel

                Arguments: ERASe, NONE, OVERwrite, SANitize
                """
                _cmd = "LEVel"
                args = ["ERASe", "NONE", "OVERwrite", "SANitize"]

                class STATe(SCPINode, SCPIBool):
                    """
                    SYSTem:SECurity:LEVel:STATe

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "STATe"
                    args = ["1", "ON", "OFF"]

                STATe = STATe()
                """
                SYSTem:SECurity:LEVel:STATe

                Arguments: 1, ON, OFF
                """

            LEVel = LEVel()
            """
            SYSTem:SECurity:LEVel

            Arguments: ERASe, NONE, OVERwrite, SANitize
            """

            class OVERwrite(SCPINode, SCPISet):
                """
                SYSTem:SECurity:OVERwrite

                Arguments:
                """
                _cmd = "OVERwrite"
                args = []

            OVERwrite = OVERwrite()
            """
            SYSTem:SECurity:OVERwrite

            Arguments:
            """

            class SANitize(SCPINode, SCPISet):
                """
                SYSTem:SECurity:SANitize

                Arguments:
                """
                _cmd = "SANitize"
                args = []

            SANitize = SANitize()
            """
            SYSTem:SECurity:SANitize

            Arguments:
            """

            class STATe(SCPINode, SCPIBool):
                """
                SYSTem:SECurity:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SYSTem:SECurity:STATe

            Arguments: 1, ON, OFF
            """

        SECurity = SECurity()
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
            _cmd = "SERRor"
            args = []

        SERRor = SERRor()
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
            _cmd = "SSAVer"
            args = []

            class DELay(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:SSAVer:DELay

                Arguments: 1
                """
                _cmd = "DELay"
                args = ["1"]

            DELay = DELay()
            """
            SYSTem:SSAVer:DELay

            Arguments: 1
            """

            class STATe(SCPINode, SCPIBool):
                """
                SYSTem:SSAVer:STATe

                Arguments: 1, ON, OFF
                """
                _cmd = "STATe"
                args = ["1", "ON", "OFF"]

            STATe = STATe()
            """
            SYSTem:SSAVer:STATe

            Arguments: 1, ON, OFF
            """

        SSAVer = SSAVer()
        """
        SYSTem:SSAVer

        Arguments:
        """

        class STATe(SCPINode, SCPISet):
            """
            SYSTem:STATe

            Arguments:
            """
            _cmd = "STATe"
            args = []

        STATe = STATe()
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
            _cmd = "TIME"
            args = []

            class DSTime(SCPINode):
                """
                SYSTem:TIME:DSTime

                Arguments:
                """
                _cmd = "DSTime"
                args = []

                class RULE(SCPINode):
                    """
                    SYSTem:TIME:DSTime:RULE

                    Arguments:
                    """
                    _cmd = "RULE"
                    args = []

                    class CATalog(SCPINode, SCPIQuery):
                        """
                        SYSTem:TIME:DSTime:RULE:CATalog

                        Arguments:
                        """
                        _cmd = "CATalog"
                        args = []

                    CATalog = CATalog()
                    """
                    SYSTem:TIME:DSTime:RULE:CATalog

                    Arguments:
                    """

                RULE = RULE()
                """
                SYSTem:TIME:DSTime:RULE

                Arguments:
                """

            DSTime = DSTime()
            """
            SYSTem:TIME:DSTime

            Arguments:
            """

            class HRTimer(SCPINode):
                """
                SYSTem:TIME:HRTimer

                Arguments:
                """
                _cmd = "HRTimer"
                args = []

                class ABSolute(SCPINode, SCPISet):
                    """
                    SYSTem:TIME:HRTimer:ABSolute

                    Arguments: 1
                    """
                    _cmd = "ABSolute"
                    args = ["1"]

                ABSolute = ABSolute()
                """
                SYSTem:TIME:HRTimer:ABSolute

                Arguments: 1
                """

                class RELative(SCPINode, SCPISet):
                    """
                    SYSTem:TIME:HRTimer:RELative

                    Arguments: 1
                    """
                    _cmd = "RELative"
                    args = ["1"]

                RELative = RELative()
                """
                SYSTem:TIME:HRTimer:RELative

                Arguments: 1
                """

            HRTimer = HRTimer()
            """
            SYSTem:TIME:HRTimer

            Arguments:
            """

            class LOCal(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:TIME:LOCal

                Arguments: <integer>,<integer>,<integer>
                """
                _cmd = "LOCal"
                args = ["<integer>,<integer>,<integer>"]

            LOCal = LOCal()
            """
            SYSTem:TIME:LOCal

            Arguments: <integer>,<integer>,<integer>
            """

        TIME = TIME()
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
            _cmd = "TZONe"
            args = ["<numeric_value>,<numeric_value>"]

        TZONe = TZONe()
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
            _cmd = "VERSion"
            args = []

        VERSion = VERSion()
        """
        `SYSTem:VERSion
        <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/1687c21d3b684121.htm#ID_83b8bf4871d1f0010a00206a01566d1c-c7a8cef471d1f0010a00206a012bc823-en-US>`_

        Arguments:
        """

    SYSTem = SYSTem()
    """
    SYSTem

    Arguments:
    """

    class TAlk_terminator(SCPINode, SCPISet):
        """
        TAlk_terminator

        Arguments:
        """
        _cmd = "TAlk_terminator"
        args = []

        class Cr_nl_end(SCPINode, SCPISet):
            """
            TAlk_terminator:Cr_nl_end

            Arguments:
            """
            _cmd = "Cr_nl_end"
            args = []

        Cr_nl_end = Cr_nl_end()
        """
        TAlk_terminator:Cr_nl_end

        Arguments:
        """

        class Nl_end(SCPINode, SCPISet):
            """
            TAlk_terminator:Nl_end

            Arguments:
            """
            _cmd = "Nl_end"
            args = []

        Nl_end = Nl_end()
        """
        TAlk_terminator:Nl_end

        Arguments:
        """

    TAlk_terminator = TAlk_terminator()
    """
    TAlk_terminator

    Arguments:
    """

    class TEst(SCPINode, SCPISet):
        """
        TEst

        Arguments:
        """
        _cmd = "TEst"
        args = []

        class Point(SCPINode, SCPIQuery, SCPISet):
            """
            TEst:Point

            Arguments: 1
            """
            _cmd = "Point"
            args = ["1"]

        Point = Point()
        """
        TEst:Point

        Arguments: 1
        """

        class Voltage(SCPINode, SCPIQuery, SCPISet):
            """
            TEst:Voltage

            Arguments:
            """
            _cmd = "Voltage"
            args = []

        Voltage = Voltage()
        """
        TEst:Voltage

        Arguments:
        """

    TEst = TEst()
    """
    TEst

    Arguments:
    """

    class TIme(SCPINode):
        """
        TIme

        Arguments:
        """
        _cmd = "TIme"
        args = []

        class AF_swp(SCPINode, SCPIQuery, SCPISet):
            """
            TIme:AF_swp

            Arguments: 1
            """
            _cmd = "AF_swp"
            args = ["1"]

        AF_swp = AF_swp()
        """
        TIme:AF_swp

        Arguments: 1
        """

        class CF_swp(SCPINode, SCPIQuery, SCPISet):
            """
            TIme:CF_swp

            Arguments: 1
            """
            _cmd = "CF_swp"
            args = ["1"]

        CF_swp = CF_swp()
        """
        TIme:CF_swp

        Arguments: 1
        """

        class MEmory_swp(SCPINode, SCPIQuery, SCPISet):
            """
            TIme:MEmory_swp

            Arguments: 1
            """
            _cmd = "MEmory_swp"
            args = ["1"]

            class Fast(SCPINode, SCPIQuery, SCPISet):
                """
                TIme:MEmory_swp:Fast

                Arguments: 1
                """
                _cmd = "Fast"
                args = ["1"]

            Fast = Fast()
            """
            TIme:MEmory_swp:Fast

            Arguments: 1
            """

        MEmory_swp = MEmory_swp()
        """
        TIme:MEmory_swp

        Arguments: 1
        """

        class RF_swp(SCPINode, SCPIQuery, SCPISet):
            """
            TIme:RF_swp

            Arguments: 1
            """
            _cmd = "RF_swp"
            args = ["1"]

        RF_swp = RF_swp()
        """
        TIme:RF_swp

        Arguments: 1
        """

    TIme = TIme()
    """
    TIme

    Arguments:
    """

    class TRIGger(SCPINode, SCPISet):
        """
        TRIGger

        Arguments:
        """
        _cmd = "TRIGger"
        args = []

        class DM(SCPINode):
            """
            TRIGger:DM

            Arguments:
            """
            _cmd = "DM"
            args = []

            class IMMediate(SCPINode, SCPISet):
                """
                TRIGger:DM:IMMediate

                Arguments:
                """
                _cmd = "IMMediate"
                args = []

            IMMediate = IMMediate()
            """
            TRIGger:DM:IMMediate

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:DM:SOURce

                Arguments: AUTO, EXTernal, SINGle
                """
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()
            """
            TRIGger:DM:SOURce

            Arguments: AUTO, EXTernal, SINGle
            """

        DM = DM()
        """
        TRIGger:DM

        Arguments:
        """

        class FSWeep(SCPINode):
            """
            TRIGger:FSWeep

            Arguments:
            """
            _cmd = "FSWeep"
            args = []

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:FSWeep:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/673177c779ae404e.htm#ID_06cb678671bda0350a00206a01b91256-cb80732271bda0350a00206a012bc823-en-US>`_

                Arguments: AUTO, EXTernal, SINGle
                """
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()
            """
            `TRIGger:FSWeep:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/673177c779ae404e.htm#ID_06cb678671bda0350a00206a01b91256-cb80732271bda0350a00206a012bc823-en-US>`_

            Arguments: AUTO, EXTernal, SINGle
            """

        FSWeep = FSWeep()
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
            _cmd = "IMMediate"
            args = []

        IMMediate = IMMediate()
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
            _cmd = "LIST"
            args = []

            class IMMediate(SCPINode, SCPISet):
                """
                TRIGger:LIST:IMMediate

                Arguments:
                """
                _cmd = "IMMediate"
                args = []

            IMMediate = IMMediate()
            """
            TRIGger:LIST:IMMediate

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:LIST:SOURce

                Arguments: AUTO, EXTernal, SINGle
                """
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()
            """
            TRIGger:LIST:SOURce

            Arguments: AUTO, EXTernal, SINGle
            """

        LIST = LIST()
        """
        TRIGger:LIST

        Arguments:
        """

        class MSEQuence(SCPINode):
            """
            TRIGger:MSEQuence

            Arguments:
            """
            _cmd = "MSEQuence"
            args = []

            class IMMediate(SCPINode, SCPISet):
                """
                TRIGger:MSEQuence:IMMediate

                Arguments:
                """
                _cmd = "IMMediate"
                args = []

            IMMediate = IMMediate()
            """
            TRIGger:MSEQuence:IMMediate

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:MSEQuence:SOURce

                Arguments: AUTO, EXTernal, SINGle
                """
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()
            """
            TRIGger:MSEQuence:SOURce

            Arguments: AUTO, EXTernal, SINGle
            """

        MSEQuence = MSEQuence()
        """
        TRIGger:MSEQuence

        Arguments:
        """

        class ODELay(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:ODELay

            Arguments: 1
            """
            _cmd = "ODELay"
            args = ["1"]

        ODELay = ODELay()
        """
        TRIGger:ODELay

        Arguments: 1
        """

        class OUTPut(SCPINode, SCPISet):
            """
            TRIGger:OUTPut

            Arguments:
            """
            _cmd = "OUTPut"
            args = []

            class POLarity(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:OUTPut:POLarity

                Arguments: NEGative, POSitive
                """
                _cmd = "POLarity"
                args = ["NEGative", "POSitive"]

            POLarity = POLarity()
            """
            TRIGger:OUTPut:POLarity

            Arguments: NEGative, POSitive
            """

        OUTPut = OUTPut()
        """
        TRIGger:OUTPut

        Arguments:
        """

        class PSWeep(SCPINode):
            """
            TRIGger:PSWeep

            Arguments:
            """
            _cmd = "PSWeep"
            args = []

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:PSWeep:SOURce
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3bdb2b0d8df44740.htm#ID_77ad610d71bda6ec0a00206a018a2840-7d255c2071bda6ec0a00206a012bc823-en-US>`_

                Arguments: AUTO, EXTernal, SINGle
                """
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()
            """
            `TRIGger:PSWeep:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/3bdb2b0d8df44740.htm#ID_77ad610d71bda6ec0a00206a018a2840-7d255c2071bda6ec0a00206a012bc823-en-US>`_

            Arguments: AUTO, EXTernal, SINGle
            """

        PSWeep = PSWeep()
        """
        TRIGger:PSWeep

        Arguments:
        """

        class PULSe(SCPINode):
            """
            TRIGger:PULSe

            Arguments:
            """
            _cmd = "PULSe"
            args = []

            class EGATed(SCPINode):
                """
                TRIGger:PULSe:EGATed

                Arguments:
                """
                _cmd = "EGATed"
                args = []

                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    TRIGger:PULSe:EGATed:POLarity

                    Arguments: INVerted, NORMal
                    """
                    _cmd = "POLarity"
                    args = ["INVerted", "NORMal"]

                POLarity = POLarity()
                """
                TRIGger:PULSe:EGATed:POLarity

                Arguments: INVerted, NORMal
                """

            EGATed = EGATed()
            """
            TRIGger:PULSe:EGATed

            Arguments:
            """

            class IMMediate(SCPINode, SCPISet):
                """
                TRIGger:PULSe:IMMediate

                Arguments:
                """
                _cmd = "IMMediate"
                args = []

            IMMediate = IMMediate()
            """
            TRIGger:PULSe:IMMediate

            Arguments:
            """

            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:PULSe:LEVel

                Arguments: TTL, V05, VM25
                """
                _cmd = "LEVel"
                args = ["TTL", "V05", "VM25"]

            LEVel = LEVel()
            """
            TRIGger:PULSe:LEVel

            Arguments: TTL, V05, VM25
            """

            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:PULSe:SLOPe

                Arguments: NEGative, POSitive
                """
                _cmd = "SLOPe"
                args = ["NEGative", "POSitive"]

            SLOPe = SLOPe()
            """
            TRIGger:PULSe:SLOPe

            Arguments: NEGative, POSitive
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:PULSe:SOURce

                Arguments: AUTO, EGATed, EXT_gated, EXTern, EXTernal, SINGle
                """
                _cmd = "SOURce"
                args = ["AUTO", "EGATed", "EXT_gated", "EXTern", "EXTernal", "SINGle"]

            SOURce = SOURce()
            """
            TRIGger:PULSe:SOURce

            Arguments: AUTO, EGATed, EXT_gated, EXTern, EXTernal, SINGle
            """

        PULSe = PULSe()
        """
        TRIGger:PULSe

        Arguments:
        """

        class SEQuence(SCPINode):
            """
            TRIGger:SEQuence

            Arguments:
            """
            _cmd = "SEQuence"
            args = []

            class IMMediate(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:SEQuence:IMMediate

                Arguments:
                """
                _cmd = "IMMediate"
                args = []

            IMMediate = IMMediate()
            """
            TRIGger:SEQuence:IMMediate

            Arguments:
            """

            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:SEQuence:SLOPe

                Arguments: NEGative, POSitive
                """
                _cmd = "SLOPe"
                args = ["NEGative", "POSitive"]

            SLOPe = SLOPe()
            """
            TRIGger:SEQuence:SLOPe

            Arguments: NEGative, POSitive
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:SEQuence:SOURce

                Arguments: BUS, EXTernal, HOLD, IMMediate
                """
                _cmd = "SOURce"
                args = ["BUS", "EXTernal", "HOLD", "IMMediate"]

            SOURce = SOURce()
            """
            TRIGger:SEQuence:SOURce

            Arguments: BUS, EXTernal, HOLD, IMMediate
            """

            class STOP(SCPINode):
                """
                TRIGger:SEQuence:STOP

                Arguments:
                """
                _cmd = "STOP"
                args = []

                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    TRIGger:SEQuence:STOP:SOURce

                    Arguments: EXTernal, IMMediate
                    """
                    _cmd = "SOURce"
                    args = ["EXTernal", "IMMediate"]

                SOURce = SOURce()
                """
                TRIGger:SEQuence:STOP:SOURce

                Arguments: EXTernal, IMMediate
                """

            STOP = STOP()
            """
            TRIGger:SEQuence:STOP

            Arguments:
            """

        SEQuence = SEQuence()
        """
        TRIGger:SEQuence

        Arguments:
        """

        class SLOPe(SCPINode, SCPIQuery, SCPISet):
            """
            TRIGger:SLOPe

            Arguments: EITHer, NEGative, POSitive
            """
            _cmd = "SLOPe"
            args = ["EITHer", "NEGative", "POSitive"]

        SLOPe = SLOPe()
        """
        TRIGger:SLOPe

        Arguments: EITHer, NEGative, POSitive
        """

        class STARt(SCPINode):
            """
            TRIGger:STARt

            Arguments:
            """
            _cmd = "STARt"
            args = []

            class IMMediate(SCPINode, SCPISet):
                """
                TRIGger:STARt:IMMediate

                Arguments:
                """
                _cmd = "IMMediate"
                args = []

            IMMediate = IMMediate()
            """
            TRIGger:STARt:IMMediate

            Arguments:
            """

            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                TRIGger:STARt:SOURce

                Arguments: BUS, EXTernal, HOLD, IMMediate
                """
                _cmd = "SOURce"
                args = ["BUS", "EXTernal", "HOLD", "IMMediate"]

            SOURce = SOURce()
            """
            TRIGger:STARt:SOURce

            Arguments: BUS, EXTernal, HOLD, IMMediate
            """

        STARt = STARt()
        """
        TRIGger:STARt

        Arguments:
        """

        class SWEep(SCPINode):
            """
            TRIGger:SWEep

            Arguments:
            """
            _cmd = "SWEep"
            args = []

            class IMMediate(SCPINode, SCPISet):
                """
                `TRIGger:SWEep:IMMediate
                <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/20e5ba8fcf2b4332.htm#ID_88ce59a571bdae100a00206a008814e4-d4d3ebe871bdae100a00206a012bc823-en-US>`_

                Arguments:
                """
                _cmd = "IMMediate"
                args = []

            IMMediate = IMMediate()
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
                _cmd = "SOURce"
                args = ["AUTO", "EXTernal", "SINGle"]

            SOURce = SOURce()
            """
            `TRIGger:SWEep:SOURce
            <http://www.rohde-schwarz.com/webhelp/smb100a_webhelp/Content/e40fc9dd64154e1e.htm#ID_2d45b80571bd99020a00206a015e8a83-7005204271bd99020a00206a012bc823-en-US>`_

            Arguments: AUTO, EXTernal, SINGle
            """

        SWEep = SWEep()
        """
        TRIGger:SWEep

        Arguments:
        """

    TRIGger = TRIGger()
    """
    TRIGger

    Arguments:
    """

    class TSWeep(SCPINode, SCPISet):
        """
        TSWeep

        Arguments:
        """
        _cmd = "TSWeep"
        args = []

    TSWeep = TSWeep()
    """
    TSWeep

    Arguments:
    """

    class VECTor(SCPINode, SCPISet):
        """
        VECTor

        Arguments:
        """
        _cmd = "VECTor"
        args = []

        class CONFig(SCPINode, SCPIQuery):
            """
            VECTor:CONFig

            Arguments:
            """
            _cmd = "CONFig"
            args = []

            class MIXer(SCPINode, SCPISet):
                """
                VECTor:CONFig:MIXer

                Arguments: EXTernal, INTernal
                """
                _cmd = "MIXer"
                args = ["EXTernal", "INTernal"]

            MIXer = MIXer()
            """
            VECTor:CONFig:MIXer

            Arguments: EXTernal, INTernal
            """

            class PULSe(SCPINode, SCPISet):
                """
                VECTor:CONFig:PULSe

                Arguments: DISabled, ENABled
                """
                _cmd = "PULSe"
                args = ["DISabled", "ENABled"]

            PULSe = PULSe()
            """
            VECTor:CONFig:PULSe

            Arguments: DISabled, ENABled
            """

        CONFig = CONFig()
        """
        VECTor:CONFig

        Arguments:
        """

        class FADing(SCPINode, SCPIQuery):
            """
            VECTor:FADing

            Arguments:
            """
            _cmd = "FADing"
            args = []

            class DIR_dopp(SCPINode, SCPISet):
                """
                VECTor:FADing:DIR_dopp

                Arguments: 1
                """
                _cmd = "DIR_dopp"
                args = ["1"]

            DIR_dopp = DIR_dopp()
            """
            VECTor:FADing:DIR_dopp

            Arguments: 1
            """

            class RATio(SCPINode, SCPISet):
                """
                VECTor:FADing:RATio

                Arguments: 1
                """
                _cmd = "RATio"
                args = ["1"]

            RATio = RATio()
            """
            VECTor:FADing:RATio

            Arguments: 1
            """

            class SPEed(SCPINode, SCPISet):
                """
                VECTor:FADing:SPEed

                Arguments: 1
                """
                _cmd = "SPEed"
                args = ["1"]

            SPEed = SPEed()
            """
            VECTor:FADing:SPEed

            Arguments: 1
            """

        FADing = FADing()
        """
        VECTor:FADing

        Arguments:
        """

        class MODopt(SCPINode, SCPIQuery):
            """
            VECTor:MODopt

            Arguments:
            """
            _cmd = "MODopt"
            args = []

            class ENVelope(SCPINode, SCPISet):
                """
                VECTor:MODopt:ENVelope

                Arguments: DISabled, ENABled
                """
                _cmd = "ENVelope"
                args = ["DISabled", "ENABled"]

            ENVelope = ENVelope()
            """
            VECTor:MODopt:ENVelope

            Arguments: DISabled, ENABled
            """

            class MODPol(SCPINode, SCPISet):
                """
                VECTor:MODopt:MODPol

                Arguments: INVerse, NORMal
                """
                _cmd = "MODPol"
                args = ["INVerse", "NORMal"]

            MODPol = MODPol()
            """
            VECTor:MODopt:MODPol

            Arguments: INVerse, NORMal
            """

        MODopt = MODopt()
        """
        VECTor:MODopt

        Arguments:
        """

    VECTor = VECTor()
    """
    VECTor

    Arguments:
    """

    class VMETer(SCPINode):
        """
        VMETer

        Arguments:
        """
        _cmd = "VMETer"
        args = []

        class VOLTage(SCPINode, SCPIQuery):
            """
            VMETer:VOLTage

            Arguments: 1
            """
            _cmd = "VOLTage"
            args = ["1"]

        VOLTage = VOLTage()
        """
        VMETer:VOLTage

        Arguments: 1
        """

    VMETer = VMETer()
    """
    VMETer

    Arguments:
    """

    class WAVeform(SCPINode, SCPIQuery, SCPISet):
        """
        WAVeform

        Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
        """
        _cmd = "WAVeform"
        args = ["SAWTooth", "SINE", "SQUare", "TRIangle", "WGNoise"]

    WAVeform = WAVeform()
    """
    WAVeform

    Arguments: SAWTooth, SINE, SQUare, TRIangle, WGNoise
    """

SMB100A_gen._SCPI_class = SMB100A_gen
# END OF SMB100A_gen
