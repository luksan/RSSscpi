# -*- coding: utf-8 -*-
# Generated from SMA100B_syntax.txt on 2019-10-18 15:03
from typing import List
from RSSscpi.SCPI_gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool
from RSSscpi.Instrument import Instrument


class SMA100B_gen(SCPINode):
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

    class LLO(SCPINode, SCPISet):
        """
        &LLO

        Arguments:
        """
        __slots__ = ()
        _cmd = "&LLO"
        args = []  # type: List[str]

    LLO = LLO()  # type: ignore
    """
    &LLO

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

    class STB(SCPINode, SCPISet):
        """
        &STB

        Arguments:
        """
        __slots__ = ()
        _cmd = "&STB"
        args = []  # type: List[str]

    STB = STB()  # type: ignore
    """
    &STB

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

        Arguments: <string>,<block_data>, <string>
        """
        __slots__ = ()
        _cmd = "*DMC"
        args = ["<string>,<block_data>", "<string>"]

    DMC = DMC()  # type: ignore
    """
    *DMC

    Arguments: <string>,<block_data>, <string>
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
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/81fb5b7cd1124455.htm#ID_d86b0432900f3f010a00206a015692f4-808cf704900f3f010a00206a01eae7a4-en-US>`_

            Arguments: <string>,ALL, WTIMe
            """
            __slots__ = ()
            _cmd = "CATalog"
            args = ["<string>,ALL", "WTIMe"]

            class LENGth(SCPINode, SCPIQuery):
                """
                `MMEMory:CATalog:LENGth
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/f52dbc720a0a48f9.htm#ID_de3b183c900f4f0f0a00206a0011b22f-adb17661900f4f0f0a00206a01eae7a4-en-US>`_

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "LENGth"
                args = ["'string'"]

            LENGth = LENGth()  # type: ignore
            """
            `MMEMory:CATalog:LENGth
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/f52dbc720a0a48f9.htm#ID_de3b183c900f4f0f0a00206a0011b22f-adb17661900f4f0f0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """

        CATalog = CATalog()  # type: ignore
        """
        `MMEMory:CATalog
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/81fb5b7cd1124455.htm#ID_d86b0432900f3f010a00206a015692f4-808cf704900f3f010a00206a01eae7a4-en-US>`_

        Arguments: <string>,ALL, WTIMe
        """

        class CDIRectory(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:CDIRectory
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/884f6bb587664b1f.htm#ID_1b7d70d1900f44510a00206a01aa7e4f-154c448f900f44510a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "CDIRectory"
            args = ["'string'"]

        CDIRectory = CDIRectory()  # type: ignore
        """
        `MMEMory:CDIRectory
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/884f6bb587664b1f.htm#ID_1b7d70d1900f44510a00206a01aa7e4f-154c448f900f44510a00206a01eae7a4-en-US>`_

        Arguments: 'string'
        """

        class COPY(SCPINode, SCPISet):
            """
            `MMEMory:COPY
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/0e2783010cfb4004.htm#ID_7d4d0053900f49a00a00206a019b2e3f-088f7246900f49a00a00206a01eae7a4-en-US>`_

            Arguments: <string>,<string>
            """
            __slots__ = ()
            _cmd = "COPY"
            args = ["<string>,<string>"]

        COPY = COPY()  # type: ignore
        """
        `MMEMory:COPY
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/0e2783010cfb4004.htm#ID_7d4d0053900f49a00a00206a019b2e3f-088f7246900f49a00a00206a01eae7a4-en-US>`_

        Arguments: <string>,<string>
        """

        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:DATA
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/a6f2e81575a74bab.htm#ID_9d80e2ff0a9fe57e0a00201900ac1637-ac44fdb80a9fe3e80a00201900ad6d49-en-US>`_

            Arguments: <string>,<block_data>,APPend
            """
            __slots__ = ()
            _cmd = "DATA"
            args = ["<string>,<block_data>,APPend"]

        DATA = DATA()  # type: ignore
        """
        `MMEMory:DATA
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/a6f2e81575a74bab.htm#ID_9d80e2ff0a9fe57e0a00201900ac1637-ac44fdb80a9fe3e80a00201900ad6d49-en-US>`_

        Arguments: <string>,<block_data>,APPend
        """

        class DCATalog(SCPINode, SCPIQuery):
            """
            `MMEMory:DCATalog
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/9143817b0b724e69.htm#ID_a8aa6937900ef1cc0a00206a010ba9d5-cf37708c900ef1cc0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "DCATalog"
            args = ["'string'"]

            class LENGth(SCPINode, SCPIQuery):
                """
                `MMEMory:DCATalog:LENGth
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/a083db692d2a43f1.htm#ID_4e070651900ef70b0a00206a016f7a85-a0f33d76900ef70b0a00206a01eae7a4-en-US>`_

                Arguments: 'string'
                """
                __slots__ = ()
                _cmd = "LENGth"
                args = ["'string'"]

            LENGth = LENGth()  # type: ignore
            """
            `MMEMory:DCATalog:LENGth
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/a083db692d2a43f1.htm#ID_4e070651900ef70b0a00206a016f7a85-a0f33d76900ef70b0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """

        DCATalog = DCATalog()  # type: ignore
        """
        `MMEMory:DCATalog
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/9143817b0b724e69.htm#ID_a8aa6937900ef1cc0a00206a010ba9d5-cf37708c900ef1cc0a00206a01eae7a4-en-US>`_

        Arguments: 'string'
        """

        class DELete(SCPINode, SCPISet):
            """
            `MMEMory:DELete
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/04c3a6e184634827.htm#ID_48ccd5f3900eec4d0a00206a007d4e66-412debbb900eec4d0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "DELete"
            args = ["'string'"]

        DELete = DELete()  # type: ignore
        """
        `MMEMory:DELete
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/04c3a6e184634827.htm#ID_48ccd5f3900eec4d0a00206a007d4e66-412debbb900eec4d0a00206a01eae7a4-en-US>`_

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

        class LOAD(SCPINode):
            """
            MMEMory:LOAD

            Arguments:
            """
            __slots__ = ()
            _cmd = "LOAD"
            args = []  # type: List[str]

            class ITEM(SCPINode, SCPISet):
                """
                MMEMory:LOAD:ITEM

                Arguments: <string>,<string>
                """
                __slots__ = ()
                _cmd = "ITEM"
                args = ["<string>,<string>"]

            ITEM = ITEM()  # type: ignore
            """
            MMEMory:LOAD:ITEM

            Arguments: <string>,<string>
            """

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
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/9de91cebcfaf4dfb.htm#ID_e4b148b6b16d7e450a00206a00d7d85c-f2c489ebb16d7e450a00206a002cfbf4-en-US>`_

                Arguments: <numeric_value>,<string>,<string>
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["<numeric_value>,<string>,<string>"]

            STATe = STATe()  # type: ignore
            """
            `MMEMory:LOAD:STATe
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/9de91cebcfaf4dfb.htm#ID_e4b148b6b16d7e450a00206a00d7d85c-f2c489ebb16d7e450a00206a002cfbf4-en-US>`_

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
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/78d90e9c1a164918.htm#ID_28e36f85900ad56d0a00206a01580c40-8ea01a92900ad56d0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "MDIRectory"
            args = ["'string'"]

        MDIRectory = MDIRectory()  # type: ignore
        """
        `MMEMory:MDIRectory
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/78d90e9c1a164918.htm#ID_28e36f85900ad56d0a00206a01580c40-8ea01a92900ad56d0a00206a01eae7a4-en-US>`_

        Arguments: 'string'
        """

        class MOVE(SCPINode, SCPISet):
            """
            `MMEMory:MOVE
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/fff605aef2744a3a.htm#ID_0716a486900adacc0a00206a005facc9-a630b5e6900adacc0a00206a01eae7a4-en-US>`_

            Arguments: <string>,<string>
            """
            __slots__ = ()
            _cmd = "MOVE"
            args = ["<string>,<string>"]

        MOVE = MOVE()  # type: ignore
        """
        `MMEMory:MOVE
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/fff605aef2744a3a.htm#ID_0716a486900adacc0a00206a005facc9-a630b5e6900adacc0a00206a01eae7a4-en-US>`_

        Arguments: <string>,<string>
        """

        class MSIS(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:MSIS
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/4b20fae1f5a54f03.htm#ID_a6615653900a4cc50a00206a01813515-cd2889b0900a4cc50a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "MSIS"
            args = ["'string'"]

        MSIS = MSIS()  # type: ignore
        """
        `MMEMory:MSIS
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/4b20fae1f5a54f03.htm#ID_a6615653900a4cc50a00206a01813515-cd2889b0900a4cc50a00206a01eae7a4-en-US>`_

        Arguments: 'string'
        """

        class RCL(SCPINode, SCPISet):
            """
            MMEMory:RCL

            Arguments: <string>,<string>
            """
            __slots__ = ()
            _cmd = "RCL"
            args = ["<string>,<string>"]

        RCL = RCL()  # type: ignore
        """
        MMEMory:RCL

        Arguments: <string>,<string>
        """

        class RDIRectory(SCPINode, SCPISet):
            """
            `MMEMory:RDIRectory
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/0605b8a725804d3f.htm#ID_845b819f9007a0b00a00206a00db9c2f-f178d5259007a0b00a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            __slots__ = ()
            _cmd = "RDIRectory"
            args = ["'string'"]

        RDIRectory = RDIRectory()  # type: ignore
        """
        `MMEMory:RDIRectory
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/0605b8a725804d3f.htm#ID_845b819f9007a0b00a00206a00db9c2f-f178d5259007a0b00a00206a01eae7a4-en-US>`_

        Arguments: 'string'
        """

        class SAV(SCPINode, SCPISet):
            """
            MMEMory:SAV

            Arguments: <string>,<string>
            """
            __slots__ = ()
            _cmd = "SAV"
            args = ["<string>,<string>"]

        SAV = SAV()  # type: ignore
        """
        MMEMory:SAV

        Arguments: <string>,<string>
        """

        class STORe(SCPINode):
            """
            MMEMory:STORe

            Arguments:
            """
            __slots__ = ()
            _cmd = "STORe"
            args = []  # type: List[str]

            class ITEM(SCPINode, SCPISet):
                """
                MMEMory:STORe:ITEM

                Arguments: <string>,<string>
                """
                __slots__ = ()
                _cmd = "ITEM"
                args = ["<string>,<string>"]

            ITEM = ITEM()  # type: ignore
            """
            MMEMory:STORe:ITEM

            Arguments: <string>,<string>
            """

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
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/a5614cb446644ab0.htm#ID_45c41292b170604d0a00206a0129c63d-053ce38db170604d0a00206a01567e4b-en-US>`_

                Arguments: <integer>,<string>,<string>
                """
                __slots__ = ()
                _cmd = "STATe"
                args = ["<integer>,<string>,<string>"]

            STATe = STATe()  # type: ignore
            """
            `MMEMory:STORe:STATe
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/a5614cb446644ab0.htm#ID_45c41292b170604d0a00206a0129c63d-053ce38db170604d0a00206a01567e4b-en-US>`_

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

    class STATus(SCPINode):
        """
        STATus

        Arguments:
        """
        __slots__ = ()
        _cmd = "STATus"
        args = []  # type: List[str]

        class OPERation(SCPINode):
            """
            STATus:OPERation

            Arguments:
            """
            __slots__ = ()
            _cmd = "OPERation"
            args = []  # type: List[str]

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

            class CONDition(SCPINode, SCPIQuery):
                """
                `STATus:OPERation:CONDition
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/eb9e616c44d34723.htm#ID_4d81c86771e8195f0a00206a0077942b-79a3ea6771e8195f0a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "CONDition"
                args = []  # type: List[str]

            CONDition = CONDition()  # type: ignore
            """
            `STATus:OPERation:CONDition
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/eb9e616c44d34723.htm#ID_4d81c86771e8195f0a00206a0077942b-79a3ea6771e8195f0a00206a012bc823-en-US>`_

            Arguments:
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:OPERation:ENABle
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/98bc7031b17e43d1.htm#ID_8a49b59171e820350a00206a00df2aff-e8cb628971e820350a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()  # type: ignore
            """
            `STATus:OPERation:ENABle
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/98bc7031b17e43d1.htm#ID_8a49b59171e820350a00206a00df2aff-e8cb628971e820350a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class EVENt(SCPINode, SCPIQuery):
                """
                `STATus:OPERation:EVENt
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/6adf4ecb81884cba.htm#ID_4526902e71e80ba30a00206a0056f13c-3203e98571e80bb30a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "EVENt"
                args = []  # type: List[str]

            EVENt = EVENt()  # type: ignore
            """
            `STATus:OPERation:EVENt
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/6adf4ecb81884cba.htm#ID_4526902e71e80ba30a00206a0056f13c-3203e98571e80bb30a00206a012bc823-en-US>`_

            Arguments:
            """

            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:OPERation:NTRansition
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/7972c214b7914431.htm#ID_c40b400271e8268e0a00206a01d0b5f6-bab207fb71e8268e0a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()  # type: ignore
            """
            `STATus:OPERation:NTRansition
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/7972c214b7914431.htm#ID_c40b400271e8268e0a00206a01d0b5f6-bab207fb71e8268e0a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:OPERation:PTRansition
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/19ddd521fccc4c10.htm#ID_7baf119671e812690a00206a0185198a-e4673fbb71e812690a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()  # type: ignore
            """
            `STATus:OPERation:PTRansition
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/19ddd521fccc4c10.htm#ID_7baf119671e812690a00206a0185198a-e4673fbb71e812690a00206a012bc823-en-US>`_

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
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/790fdbfc3c41487f.htm#ID_e484e63b71e7fde70a00206a00a80b3f-98d3fe7771e7fde70a00206a012bc823-en-US>`_

            Arguments:
            """
            __slots__ = ()
            _cmd = "PRESet"
            args = []  # type: List[str]

        PRESet = PRESet()  # type: ignore
        """
        `STATus:PRESet
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/790fdbfc3c41487f.htm#ID_e484e63b71e7fde70a00206a00a80b3f-98d3fe7771e7fde70a00206a012bc823-en-US>`_

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

            class CONDition(SCPINode, SCPIQuery):
                """
                `STATus:QUEStionable:CONDition
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/f08a3423b9ea496f.htm#ID_e3fc15a371e842430a00206a009728a6-98e12c6f71e842430a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "CONDition"
                args = []  # type: List[str]

            CONDition = CONDition()  # type: ignore
            """
            `STATus:QUEStionable:CONDition
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/f08a3423b9ea496f.htm#ID_e3fc15a371e842430a00206a009728a6-98e12c6f71e842430a00206a012bc823-en-US>`_

            Arguments:
            """

            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:ENABle
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/08e648cd32434240.htm#ID_d432e5c771e849670a00206a00cb59b5-0bf1cb4571e849670a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()  # type: ignore
            """
            `STATus:QUEStionable:ENABle
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/08e648cd32434240.htm#ID_d432e5c771e849670a00206a00cb59b5-0bf1cb4571e849670a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class EVENt(SCPINode, SCPIQuery):
                """
                `STATus:QUEStionable:EVENt
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/baaaa61d6eeb4c8f.htm#ID_8f72e6de71e834880a00206a01c75738-c55f605671e834880a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "EVENt"
                args = []  # type: List[str]

            EVENt = EVENt()  # type: ignore
            """
            `STATus:QUEStionable:EVENt
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/baaaa61d6eeb4c8f.htm#ID_8f72e6de71e834880a00206a01c75738-c55f605671e834880a00206a012bc823-en-US>`_

            Arguments:
            """

            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:NTRansition
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/792d9ce3f9bf4fdd.htm#ID_3172142271e8509b0a00206a01b3f2a1-b4d8282f71e8509b0a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()  # type: ignore
            """
            `STATus:QUEStionable:NTRansition
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/792d9ce3f9bf4fdd.htm#ID_3172142271e8509b0a00206a01b3f2a1-b4d8282f71e8509b0a00206a012bc823-en-US>`_

            Arguments: 1
            """

            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:PTRansition
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/13c14e2f83164444.htm#ID_4ed8eafd71e83b5e0a00206a01c2fbb1-c632286d71e83b5e0a00206a012bc823-en-US>`_

                Arguments: 1
                """
                __slots__ = ()
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()  # type: ignore
            """
            `STATus:QUEStionable:PTRansition
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/13c14e2f83164444.htm#ID_4ed8eafd71e83b5e0a00206a01c2fbb1-c632286d71e83b5e0a00206a012bc823-en-US>`_

            Arguments: 1
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
                `STATus:QUEue:NEXT
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/4a06b365f17842a7.htm#ID_85f56928ee2f7fee0a001ae7261adfe9-813de58aee2f7e670a001ae72bbdbcb4-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "NEXT"
                args = []  # type: List[str]

            NEXT = NEXT()  # type: ignore
            """
            `STATus:QUEue:NEXT
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/4a06b365f17842a7.htm#ID_85f56928ee2f7fee0a001ae7261adfe9-813de58aee2f7e670a001ae72bbdbcb4-en-US>`_

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

        class DATE(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:DATE
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/779bb1a4775d490c.htm#ID_09e1ebc9a6ab7e490a001ae70d84cfcf-cf76dd7da6ab7d3f0a001ae71f12f61a-en-US>`_

            Arguments: <integer>,<integer>,<integer>
            """
            __slots__ = ()
            _cmd = "DATE"
            args = ["<integer>,<integer>,<integer>"]

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

            class UTC(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:DATE:UTC

                Arguments: <integer>,<integer>,<integer>
                """
                __slots__ = ()
                _cmd = "UTC"
                args = ["<integer>,<integer>,<integer>"]

            UTC = UTC()  # type: ignore
            """
            SYSTem:DATE:UTC

            Arguments: <integer>,<integer>,<integer>
            """

        DATE = DATE()  # type: ignore
        """
        `SYSTem:DATE
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/779bb1a4775d490c.htm#ID_09e1ebc9a6ab7e490a001ae70d84cfcf-cf76dd7da6ab7d3f0a001ae71f12f61a-en-US>`_

        Arguments: <integer>,<integer>,<integer>
        """

        class DEVice(SCPINode):
            """
            SYSTem:DEVice

            Arguments:
            """
            __slots__ = ()
            _cmd = "DEVice"
            args = []  # type: List[str]

            class ID(SCPINode, SCPIQuery):
                """
                SYSTem:DEVice:ID

                Arguments:
                """
                __slots__ = ()
                _cmd = "ID"
                args = []  # type: List[str]

            ID = ID()  # type: ignore
            """
            SYSTem:DEVice:ID

            Arguments:
            """

        DEVice = DEVice()  # type: ignore
        """
        SYSTem:DEVice

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

        class DID(SCPINode, SCPIQuery):
            """
            SYSTem:DID

            Arguments:
            """
            __slots__ = ()
            _cmd = "DID"
            args = []  # type: List[str]

        DID = DID()  # type: ignore
        """
        SYSTem:DID

        Arguments:
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
                SYSTem:DISPlay:UPDate

                Arguments: 1, ON, OFF
                """
                __slots__ = ()
                _cmd = "UPDate"
                args = ["1", "ON", "OFF"]

            UPDate = UPDate()  # type: ignore
            """
            SYSTem:DISPlay:UPDate

            Arguments: 1, ON, OFF
            """

        DISPlay = DISPlay()  # type: ignore
        """
        SYSTem:DISPlay

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
                `SYSTem:ERRor:ALL
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/7b0fb769f8c94c63.htm#ID_01d81ebc71d1c5670a00206a018810ed-c1e0759071d1c5670a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "ALL"
                args = []  # type: List[str]

            ALL = ALL()  # type: ignore
            """
            `SYSTem:ERRor:ALL
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/7b0fb769f8c94c63.htm#ID_01d81ebc71d1c5670a00206a018810ed-c1e0759071d1c5670a00206a012bc823-en-US>`_

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
                    `SYSTem:ERRor:CODE:ALL
                    <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/ab9328e7820e4ab2.htm#ID_e106118871d1d3610a00206a00df0731-260d42f471d1d3610a00206a012bc823-en-US>`_

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ALL"
                    args = []  # type: List[str]

                ALL = ALL()  # type: ignore
                """
                `SYSTem:ERRor:CODE:ALL
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/ab9328e7820e4ab2.htm#ID_e106118871d1d3610a00206a00df0731-260d42f471d1d3610a00206a012bc823-en-US>`_

                Arguments:
                """

                class NEXT(SCPINode, SCPIQuery):
                    """
                    `SYSTem:ERRor:CODE:NEXT
                    <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/7327faef63024f01.htm#ID_782a7ff371d1ccaa0a00206a00d211bc-ce97f85471d1ccaa0a00206a012bc823-en-US>`_

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "NEXT"
                    args = []  # type: List[str]

                NEXT = NEXT()  # type: ignore
                """
                `SYSTem:ERRor:CODE:NEXT
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/7327faef63024f01.htm#ID_782a7ff371d1ccaa0a00206a00d211bc-ce97f85471d1ccaa0a00206a012bc823-en-US>`_

                Arguments:
                """

            CODE = CODE()  # type: ignore
            """
            SYSTem:ERRor:CODE

            Arguments:
            """

            class COUNt(SCPINode, SCPIQuery):
                """
                `SYSTem:ERRor:COUNt
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/ba0d0e59bbb0493c.htm#ID_00c603b971d1daa50a00206a0178d1e6-77aa4c6371d1daa50a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "COUNt"
                args = []  # type: List[str]

            COUNt = COUNt()  # type: ignore
            """
            `SYSTem:ERRor:COUNt
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/ba0d0e59bbb0493c.htm#ID_00c603b971d1daa50a00206a0178d1e6-77aa4c6371d1daa50a00206a012bc823-en-US>`_

            Arguments:
            """

            class NEXT(SCPINode, SCPIQuery):
                """
                `SYSTem:ERRor:NEXT
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/9041c827635042ae.htm#ID_3ca90d7f71d1f7830a00206a00d63293-4855f86871d1f7830a00206a012bc823-en-US>`_

                Arguments:
                """
                __slots__ = ()
                _cmd = "NEXT"
                args = []  # type: List[str]

            NEXT = NEXT()  # type: ignore
            """
            `SYSTem:ERRor:NEXT
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/9041c827635042ae.htm#ID_3ca90d7f71d1f7830a00206a00d63293-4855f86871d1f7830a00206a012bc823-en-US>`_

            Arguments:
            """

        ERRor = ERRor()  # type: ignore
        """
        SYSTem:ERRor

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

        class KLOCk(SCPINode, SCPIBool):
            """
            `SYSTem:KLOCk
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/cbb799b612914e37.htm#ID_a7f3c503a58e7f280a00201900122e30-4255d8a4a58e7d430a00201901ee4d9f-en-US>`_

            Arguments: 1, ON, OFF
            """
            __slots__ = ()
            _cmd = "KLOCk"
            args = ["1", "ON", "OFF"]

        KLOCk = KLOCk()  # type: ignore
        """
        `SYSTem:KLOCk
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/cbb799b612914e37.htm#ID_a7f3c503a58e7f280a00201900122e30-4255d8a4a58e7d430a00201901ee4d9f-en-US>`_

        Arguments: 1, ON, OFF
        """

        class LOCK(SCPINode):
            """
            SYSTem:LOCK

            Arguments:
            """
            __slots__ = ()
            _cmd = "LOCK"
            args = []  # type: List[str]

            class NAME(SCPINode, SCPIQuery):
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

                class ALL(SCPINode, SCPISet):
                    """
                    SYSTem:LOCK:RELease:ALL

                    Arguments:
                    """
                    __slots__ = ()
                    _cmd = "ALL"
                    args = []  # type: List[str]

                ALL = ALL()  # type: ignore
                """
                SYSTem:LOCK:RELease:ALL

                Arguments:
                """

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

        class PRESet(SCPINode, SCPISet):
            """
            `SYSTem:PRESet
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/fea01e424ecf4cc4.htm#ID_a64c6dbf4ecf62470a00206a0141ec63-ed39c76a4ecf62470a00206a0024546d-en-US>`_

            Arguments:
            """
            __slots__ = ()
            _cmd = "PRESet"
            args = []  # type: List[str]

        PRESet = PRESet()  # type: ignore
        """
        `SYSTem:PRESet
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/fea01e424ecf4cc4.htm#ID_a64c6dbf4ecf62470a00206a0141ec63-ed39c76a4ecf62470a00206a0024546d-en-US>`_

        Arguments:
        """

        class TIME(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:TIME
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/f17cde1b40ba4722.htm#ID_57f998aba6ab7fcf0a001ae73f23664c-f3909540a6ab7ee50a001ae71f12f61a-en-US>`_

            Arguments: <integer>,<integer>,<integer>
            """
            __slots__ = ()
            _cmd = "TIME"
            args = ["<integer>,<integer>,<integer>"]

            class DSTime(SCPINode):
                """
                SYSTem:TIME:DSTime

                Arguments:
                """
                __slots__ = ()
                _cmd = "DSTime"
                args = []  # type: List[str]

                class MODE(SCPINode, SCPIBool):
                    """
                    SYSTem:TIME:DSTime:MODE

                    Arguments: 1, ON, OFF
                    """
                    __slots__ = ()
                    _cmd = "MODE"
                    args = ["1", "ON", "OFF"]

                MODE = MODE()  # type: ignore
                """
                SYSTem:TIME:DSTime:MODE

                Arguments: 1, ON, OFF
                """

                class RULE(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:TIME:DSTime:RULE

                    Arguments: 'string'
                    """
                    __slots__ = ()
                    _cmd = "RULE"
                    args = ["'string'"]

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

                Arguments: 'string'
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

                    class SET(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:TIME:HRTimer:ABSolute:SET

                        Arguments:
                        """
                        __slots__ = ()
                        _cmd = "SET"
                        args = []  # type: List[str]

                    SET = SET()  # type: ignore
                    """
                    SYSTem:TIME:HRTimer:ABSolute:SET

                    Arguments:
                    """

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

            class UTC(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:TIME:UTC

                Arguments: <integer>,<integer>,<integer>
                """
                __slots__ = ()
                _cmd = "UTC"
                args = ["<integer>,<integer>,<integer>"]

            UTC = UTC()  # type: ignore
            """
            SYSTem:TIME:UTC

            Arguments: <integer>,<integer>,<integer>
            """

        TIME = TIME()  # type: ignore
        """
        `SYSTem:TIME
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/f17cde1b40ba4722.htm#ID_57f998aba6ab7fcf0a001ae73f23664c-f3909540a6ab7ee50a001ae71f12f61a-en-US>`_

        Arguments: <integer>,<integer>,<integer>
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
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/1687c21d3b684121.htm#ID_83b8bf4871d1f0010a00206a01566d1c-c7a8cef471d1f0010a00206a012bc823-en-US>`_

            Arguments:
            """
            __slots__ = ()
            _cmd = "VERSion"
            args = []  # type: List[str]

        VERSion = VERSion()  # type: ignore
        """
        `SYSTem:VERSion
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/1687c21d3b684121.htm#ID_83b8bf4871d1f0010a00206a01566d1c-c7a8cef471d1f0010a00206a012bc823-en-US>`_

        Arguments:
        """

    SYSTem = SYSTem()  # type: ignore
    """
    SYSTem

    Arguments:
    """


SMA100B_gen._SCPI_class = SMA100B_gen
# END OF SMA100B_gen
