# -*- coding: utf-8 -*-
# Generated from SMA100B_syntax.txt on 2017-08-02 19:04
from RSSscpi.SCPI_gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool
from RSSscpi.Instrument import Instrument


class SMA100B_gen(Instrument):
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

    class LLO(SCPINode, SCPISet):
        """
        &LLO

        Arguments:
        """
        _cmd = "&LLO"
        args = []

    LLO = LLO()
    """
    &LLO

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

    class STB(SCPINode, SCPISet):
        """
        &STB

        Arguments:
        """
        _cmd = "&STB"
        args = []

    STB = STB()
    """
    &STB

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

        Arguments: <numeric_value>
        """
        _cmd = "*DEV"
        args = ["<numeric_value>"]

    DEV = DEV()
    """
    *DEV

    Arguments: <numeric_value>
    """

    class DMC(SCPINode, SCPIQuery, SCPISet):
        """
        *DMC

        Arguments: <string>,<block_data>|<string>
        """
        _cmd = "*DMC"
        args = ["<string>,<block_data>|<string>"]

    DMC = DMC()
    """
    *DMC

    Arguments: <string>,<block_data>|<string>
    """

    class EMC(SCPINode, SCPIQuery, SCPISet):
        """
        *EMC

        Arguments: <boolean>
        """
        _cmd = "*EMC"
        args = ["<boolean>"]

    EMC = EMC()
    """
    *EMC

    Arguments: <boolean>
    """

    class ESE(SCPINode, SCPIQuery, SCPISet):
        """
        *ESE

        Arguments: <numeric_value>
        """
        _cmd = "*ESE"
        args = ["<numeric_value>"]

    ESE = ESE()
    """
    *ESE

    Arguments: <numeric_value>
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

        Arguments: <string>
        """
        _cmd = "*GMC"
        args = ["<string>"]

    GMC = GMC()
    """
    *GMC

    Arguments: <string>
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

        Arguments: <numeric_value>
        """
        _cmd = "*PRE"
        args = ["<numeric_value>"]

    PRE = PRE()
    """
    *PRE

    Arguments: <numeric_value>
    """

    class PSC(SCPINode, SCPIQuery, SCPISet):
        """
        *PSC

        Arguments: <boolean>
        """
        _cmd = "*PSC"
        args = ["<boolean>"]

    PSC = PSC()
    """
    *PSC

    Arguments: <boolean>
    """

    class RCL(SCPINode, SCPISet):
        """
        *RCL

        Arguments: <numeric_value>
        """
        _cmd = "*RCL"
        args = ["<numeric_value>"]

    RCL = RCL()
    """
    *RCL

    Arguments: <numeric_value>
    """

    class RMC(SCPINode, SCPISet):
        """
        *RMC

        Arguments: <string>
        """
        _cmd = "*RMC"
        args = ["<string>"]

    RMC = RMC()
    """
    *RMC

    Arguments: <string>
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

        Arguments: <numeric_value>
        """
        _cmd = "*SAV"
        args = ["<numeric_value>"]

    SAV = SAV()
    """
    *SAV

    Arguments: <numeric_value>
    """

    class SRE(SCPINode, SCPIQuery, SCPISet):
        """
        *SRE

        Arguments: <numeric_value>
        """
        _cmd = "*SRE"
        args = ["<numeric_value>"]

    SRE = SRE()
    """
    *SRE

    Arguments: <numeric_value>
    """

    class SRQ(SCPINode, SCPIQuery):
        """
        *SRQ

        Arguments: <integer>|DOWN|MAXimum|MINimum|UP
        """
        _cmd = "*SRQ"
        args = ["<integer>|DOWN|MAXimum|MINimum|UP"]

    SRQ = SRQ()
    """
    *SRQ

    Arguments: <integer>|DOWN|MAXimum|MINimum|UP
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
            MMEMory:CATalog

            Arguments: <string>,ALL|WTIMe
            """
            _cmd = "CATalog"
            args = ["<string>,ALL|WTIMe"]

            class LENGth(SCPINode, SCPIQuery):
                """
                MMEMory:CATalog:LENGth

                Arguments: <string>
                """
                _cmd = "LENGth"
                args = ["<string>"]

            LENGth = LENGth()
            """
            MMEMory:CATalog:LENGth

            Arguments: <string>
            """

        CATalog = CATalog()
        """
        MMEMory:CATalog

        Arguments: <string>,ALL|WTIMe
        """

        class CDIRectory(SCPINode, SCPIQuery, SCPISet):
            """
            MMEMory:CDIRectory

            Arguments: <string>
            """
            _cmd = "CDIRectory"
            args = ["<string>"]

        CDIRectory = CDIRectory()
        """
        MMEMory:CDIRectory

        Arguments: <string>
        """

        class COPY(SCPINode, SCPISet):
            """
            MMEMory:COPY

            Arguments: <string>,<string>
            """
            _cmd = "COPY"
            args = ["<string>,<string>"]

        COPY = COPY()
        """
        MMEMory:COPY

        Arguments: <string>,<string>
        """

        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            MMEMory:DATA

            Arguments: <string>,<block_data>,APPend
            """
            _cmd = "DATA"
            args = ["<string>,<block_data>,APPend"]

        DATA = DATA()
        """
        MMEMory:DATA

        Arguments: <string>,<block_data>,APPend
        """

        class DCATalog(SCPINode, SCPIQuery):
            """
            MMEMory:DCATalog

            Arguments: <string>
            """
            _cmd = "DCATalog"
            args = ["<string>"]

            class LENGth(SCPINode, SCPIQuery):
                """
                MMEMory:DCATalog:LENGth

                Arguments: <string>
                """
                _cmd = "LENGth"
                args = ["<string>"]

            LENGth = LENGth()
            """
            MMEMory:DCATalog:LENGth

            Arguments: <string>
            """

        DCATalog = DCATalog()
        """
        MMEMory:DCATalog

        Arguments: <string>
        """

        class DELete(SCPINode, SCPISet):
            """
            MMEMory:DELete

            Arguments: <string>
            """
            _cmd = "DELete"
            args = ["<string>"]

        DELete = DELete()
        """
        MMEMory:DELete

        Arguments: <string>
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

        class LOAD(SCPINode):
            """
            MMEMory:LOAD

            Arguments:
            """
            _cmd = "LOAD"
            args = []

            class ITEM(SCPINode, SCPISet):
                """
                MMEMory:LOAD:ITEM

                Arguments: <string>,<string>
                """
                _cmd = "ITEM"
                args = ["<string>,<string>"]

            ITEM = ITEM()
            """
            MMEMory:LOAD:ITEM

            Arguments: <string>,<string>
            """

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
                MMEMory:LOAD:STATe

                Arguments: <numeric_value>,<string>,<string>
                """
                _cmd = "STATe"
                args = ["<numeric_value>,<string>,<string>"]

            STATe = STATe()
            """
            MMEMory:LOAD:STATe

            Arguments: <numeric_value>,<string>,<string>
            """

        LOAD = LOAD()
        """
        MMEMory:LOAD

        Arguments:
        """

        class MDIRectory(SCPINode, SCPISet):
            """
            MMEMory:MDIRectory

            Arguments: <string>
            """
            _cmd = "MDIRectory"
            args = ["<string>"]

        MDIRectory = MDIRectory()
        """
        MMEMory:MDIRectory

        Arguments: <string>
        """

        class MOVE(SCPINode, SCPISet):
            """
            MMEMory:MOVE

            Arguments: <string>,<string>
            """
            _cmd = "MOVE"
            args = ["<string>,<string>"]

        MOVE = MOVE()
        """
        MMEMory:MOVE

        Arguments: <string>,<string>
        """

        class MSIS(SCPINode, SCPIQuery, SCPISet):
            """
            MMEMory:MSIS

            Arguments: <string>
            """
            _cmd = "MSIS"
            args = ["<string>"]

        MSIS = MSIS()
        """
        MMEMory:MSIS

        Arguments: <string>
        """

        class RCL(SCPINode, SCPISet):
            """
            MMEMory:RCL

            Arguments: <string>,<string>
            """
            _cmd = "RCL"
            args = ["<string>,<string>"]

        RCL = RCL()
        """
        MMEMory:RCL

        Arguments: <string>,<string>
        """

        class RDIRectory(SCPINode, SCPISet):
            """
            MMEMory:RDIRectory

            Arguments: <string>
            """
            _cmd = "RDIRectory"
            args = ["<string>"]

        RDIRectory = RDIRectory()
        """
        MMEMory:RDIRectory

        Arguments: <string>
        """

        class SAV(SCPINode, SCPISet):
            """
            MMEMory:SAV

            Arguments: <string>,<string>
            """
            _cmd = "SAV"
            args = ["<string>,<string>"]

        SAV = SAV()
        """
        MMEMory:SAV

        Arguments: <string>,<string>
        """

        class STORe(SCPINode):
            """
            MMEMory:STORe

            Arguments:
            """
            _cmd = "STORe"
            args = []

            class ITEM(SCPINode, SCPISet):
                """
                MMEMory:STORe:ITEM

                Arguments: <string>,<string>
                """
                _cmd = "ITEM"
                args = ["<string>,<string>"]

            ITEM = ITEM()
            """
            MMEMory:STORe:ITEM

            Arguments: <string>,<string>
            """

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
                MMEMory:STORe:STATe

                Arguments: <integer>,<string>,<string>
                """
                _cmd = "STATe"
                args = ["<integer>,<string>,<string>"]

            STATe = STATe()
            """
            MMEMory:STORe:STATe

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

    class STATus(SCPINode):
        """
        STATus

        Arguments:
        """
        _cmd = "STATus"
        args = []

        class OPERation(SCPINode):
            """
            STATus:OPERation

            Arguments:
            """
            _cmd = "OPERation"
            args = []

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

                    Arguments: <numeric_value>
                    """
                    _cmd = "ENABle"
                    args = ["<numeric_value>"]

                ENABle = ENABle()
                """
                STATus:OPERation:BIT:ENABle

                Arguments: <numeric_value>
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

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BIT:NTRansition

                    Arguments: <boolean>
                    """
                    _cmd = "NTRansition"
                    args = ["<boolean>"]

                NTRansition = NTRansition()
                """
                STATus:OPERation:BIT:NTRansition

                Arguments: <boolean>
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:OPERation:BIT:PTRansition

                    Arguments: <boolean>
                    """
                    _cmd = "PTRansition"
                    args = ["<boolean>"]

                PTRansition = PTRansition()
                """
                STATus:OPERation:BIT:PTRansition

                Arguments: <boolean>
                """

            BIT = BIT()
            """
            STATus:OPERation:BIT

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

                Arguments: <integer>
                """
                _cmd = "ENABle"
                args = ["<integer>"]

            ENABle = ENABle()
            """
            STATus:OPERation:ENABle

            Arguments: <integer>
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

                Arguments: <integer>
                """
                _cmd = "NTRansition"
                args = ["<integer>"]

            NTRansition = NTRansition()
            """
            STATus:OPERation:NTRansition

            Arguments: <integer>
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:PTRansition

                Arguments: <integer>
                """
                _cmd = "PTRansition"
                args = ["<integer>"]

            PTRansition = PTRansition()
            """
            STATus:OPERation:PTRansition

            Arguments: <integer>
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

                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:BIT:ENABle

                    Arguments: <boolean>
                    """
                    _cmd = "ENABle"
                    args = ["<boolean>"]

                ENABle = ENABle()
                """
                STATus:QUEStionable:BIT:ENABle

                Arguments: <boolean>
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

                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:BIT:NTRansition

                    Arguments: <boolean>
                    """
                    _cmd = "NTRansition"
                    args = ["<boolean>"]

                NTRansition = NTRansition()
                """
                STATus:QUEStionable:BIT:NTRansition

                Arguments: <boolean>
                """

                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:BIT:PTRansition

                    Arguments: <boolean>
                    """
                    _cmd = "PTRansition"
                    args = ["<boolean>"]

                PTRansition = PTRansition()
                """
                STATus:QUEStionable:BIT:PTRansition

                Arguments: <boolean>
                """

            BIT = BIT()
            """
            STATus:QUEStionable:BIT

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

                Arguments: <integer>
                """
                _cmd = "ENABle"
                args = ["<integer>"]

            ENABle = ENABle()
            """
            STATus:QUEStionable:ENABle

            Arguments: <integer>
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

                Arguments: <integer>
                """
                _cmd = "NTRansition"
                args = ["<integer>"]

            NTRansition = NTRansition()
            """
            STATus:QUEStionable:NTRansition

            Arguments: <integer>
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:PTRansition

                Arguments: <integer>
                """
                _cmd = "PTRansition"
                args = ["<integer>"]

            PTRansition = PTRansition()
            """
            STATus:QUEStionable:PTRansition

            Arguments: <integer>
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

        class DATE(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:DATE

            Arguments: <integer>,<integer>,<integer>
            """
            _cmd = "DATE"
            args = ["<integer>,<integer>,<integer>"]

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

            class UTC(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:DATE:UTC

                Arguments: <integer>,<integer>,<integer>
                """
                _cmd = "UTC"
                args = ["<integer>,<integer>,<integer>"]

            UTC = UTC()
            """
            SYSTem:DATE:UTC

            Arguments: <integer>,<integer>,<integer>
            """

        DATE = DATE()
        """
        SYSTem:DATE

        Arguments: <integer>,<integer>,<integer>
        """

        class DEVice(SCPINode):
            """
            SYSTem:DEVice

            Arguments:
            """
            _cmd = "DEVice"
            args = []

            class ID(SCPINode, SCPIQuery):
                """
                SYSTem:DEVice:ID

                Arguments:
                """
                _cmd = "ID"
                args = []

            ID = ID()
            """
            SYSTem:DEVice:ID

            Arguments:
            """

        DEVice = DEVice()
        """
        SYSTem:DEVice

        Arguments:
        """

        class DFPRint(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:DFPRint

            Arguments: <string>
            """
            _cmd = "DFPRint"
            args = ["<string>"]

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

                    Arguments: <integer>
                    """
                    _cmd = "ENTRy"
                    args = ["<integer>"]

                ENTRy = ENTRy()
                """
                SYSTem:DFPRint:HISTory:ENTRy

                Arguments: <integer>
                """

            HISTory = HISTory()
            """
            SYSTem:DFPRint:HISTory

            Arguments:
            """

        DFPRint = DFPRint()
        """
        SYSTem:DFPRint

        Arguments: <string>
        """

        class DID(SCPINode, SCPIQuery):
            """
            SYSTem:DID

            Arguments:
            """
            _cmd = "DID"
            args = []

        DID = DID()
        """
        SYSTem:DID

        Arguments:
        """

        class DISPlay(SCPINode):
            """
            SYSTem:DISPlay

            Arguments:
            """
            _cmd = "DISPlay"
            args = []

            class UPDate(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:DISPlay:UPDate

                Arguments: <boolean>
                """
                _cmd = "UPDate"
                args = ["<boolean>"]

            UPDate = UPDate()
            """
            SYSTem:DISPlay:UPDate

            Arguments: <boolean>
            """

        DISPlay = DISPlay()
        """
        SYSTem:DISPlay

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

                Arguments: <string>
                """
                _cmd = "HEADers"
                args = ["<string>"]

            HEADers = HEADers()
            """
            SYSTem:HELP:HEADers

            Arguments: <string>
            """

            class SYNTax(SCPINode, SCPIQuery):
                """
                SYSTem:HELP:SYNTax

                Arguments: <string>
                """
                _cmd = "SYNTax"
                args = ["<string>"]

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

            Arguments: <string>
            """

        HELP = HELP()
        """
        SYSTem:HELP

        Arguments:
        """

        class KLOCk(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:KLOCk

            Arguments: <boolean>
            """
            _cmd = "KLOCk"
            args = ["<boolean>"]

        KLOCk = KLOCk()
        """
        SYSTem:KLOCk

        Arguments: <boolean>
        """

        class LOCK(SCPINode):
            """
            SYSTem:LOCK

            Arguments:
            """
            _cmd = "LOCK"
            args = []

            class NAME(SCPINode, SCPIQuery):
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

                class ALL(SCPINode, SCPISet):
                    """
                    SYSTem:LOCK:RELease:ALL

                    Arguments:
                    """
                    _cmd = "ALL"
                    args = []

                ALL = ALL()
                """
                SYSTem:LOCK:RELease:ALL

                Arguments:
                """

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

                    Arguments: <integer>|INFinite
                    """
                    _cmd = "EXCLusive"
                    args = ["<integer>|INFinite"]

                EXCLusive = EXCLusive()
                """
                SYSTem:LOCK:REQuest:EXCLusive

                Arguments: <integer>|INFinite
                """

                class SHARed(SCPINode, SCPIQuery):
                    """
                    SYSTem:LOCK:REQuest:SHARed

                    Arguments: <string>,<integer>|INFinite
                    """
                    _cmd = "SHARed"
                    args = ["<string>,<integer>|INFinite"]

                SHARed = SHARed()
                """
                SYSTem:LOCK:REQuest:SHARed

                Arguments: <string>,<integer>|INFinite
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

                Arguments: <integer>|INFinite
                """
                _cmd = "TIMeout"
                args = ["<integer>|INFinite"]

            TIMeout = TIMeout()
            """
            SYSTem:LOCK:TIMeout

            Arguments: <integer>|INFinite
            """

        LOCK = LOCK()
        """
        SYSTem:LOCK

        Arguments:
        """

        class PRESet(SCPINode, SCPISet):
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

        class TIME(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:TIME

            Arguments: <integer>,<integer>,<integer>
            """
            _cmd = "TIME"
            args = ["<integer>,<integer>,<integer>"]

            class DSTime(SCPINode):
                """
                SYSTem:TIME:DSTime

                Arguments:
                """
                _cmd = "DSTime"
                args = []

                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:TIME:DSTime:MODE

                    Arguments: <boolean>
                    """
                    _cmd = "MODE"
                    args = ["<boolean>"]

                MODE = MODE()
                """
                SYSTem:TIME:DSTime:MODE

                Arguments: <boolean>
                """

                class RULE(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:TIME:DSTime:RULE

                    Arguments: <string>
                    """
                    _cmd = "RULE"
                    args = ["<string>"]

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

                Arguments: <string>
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

                    Arguments: <numeric_value>
                    """
                    _cmd = "ABSolute"
                    args = ["<numeric_value>"]

                    class SET(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:TIME:HRTimer:ABSolute:SET

                        Arguments:
                        """
                        _cmd = "SET"
                        args = []

                    SET = SET()
                    """
                    SYSTem:TIME:HRTimer:ABSolute:SET

                    Arguments:
                    """

                ABSolute = ABSolute()
                """
                SYSTem:TIME:HRTimer:ABSolute

                Arguments: <numeric_value>
                """

                class RELative(SCPINode, SCPISet):
                    """
                    SYSTem:TIME:HRTimer:RELative

                    Arguments: <integer>
                    """
                    _cmd = "RELative"
                    args = ["<integer>"]

                RELative = RELative()
                """
                SYSTem:TIME:HRTimer:RELative

                Arguments: <integer>
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

            class UTC(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:TIME:UTC

                Arguments: <integer>,<integer>,<integer>
                """
                _cmd = "UTC"
                args = ["<integer>,<integer>,<integer>"]

            UTC = UTC()
            """
            SYSTem:TIME:UTC

            Arguments: <integer>,<integer>,<integer>
            """

        TIME = TIME()
        """
        SYSTem:TIME

        Arguments: <integer>,<integer>,<integer>
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

    # END OF SMA100B_gen
