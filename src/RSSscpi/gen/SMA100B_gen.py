# -*- coding: utf-8 -*-
# Generated from SMA100B_syntax.txt on 2017-08-08 18:48
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

        Arguments: <string>,<block_data>, <string>
        """
        _cmd = "*DMC"
        args = ["<string>,<block_data>", "<string>"]

    DMC = DMC()
    """
    *DMC

    Arguments: <string>,<block_data>, <string>
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
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/81fb5b7cd1124455.htm#ID_d86b0432900f3f010a00206a015692f4-808cf704900f3f010a00206a01eae7a4-en-US>`_

            Arguments: <string>,ALL, WTIMe
            """
            _cmd = "CATalog"
            args = ["<string>,ALL", "WTIMe"]

            class LENGth(SCPINode, SCPIQuery):
                """
                `MMEMory:CATalog:LENGth
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/f52dbc720a0a48f9.htm#ID_de3b183c900f4f0f0a00206a0011b22f-adb17661900f4f0f0a00206a01eae7a4-en-US>`_

                Arguments: 'string'
                """
                _cmd = "LENGth"
                args = ["'string'"]

            LENGth = LENGth()
            """
            `MMEMory:CATalog:LENGth
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/f52dbc720a0a48f9.htm#ID_de3b183c900f4f0f0a00206a0011b22f-adb17661900f4f0f0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """

        CATalog = CATalog()
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
            _cmd = "CDIRectory"
            args = ["'string'"]

        CDIRectory = CDIRectory()
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
            _cmd = "COPY"
            args = ["<string>,<string>"]

        COPY = COPY()
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
            _cmd = "DATA"
            args = ["<string>,<block_data>,APPend"]

        DATA = DATA()
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
            _cmd = "DCATalog"
            args = ["'string'"]

            class LENGth(SCPINode, SCPIQuery):
                """
                `MMEMory:DCATalog:LENGth
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/a083db692d2a43f1.htm#ID_4e070651900ef70b0a00206a016f7a85-a0f33d76900ef70b0a00206a01eae7a4-en-US>`_

                Arguments: 'string'
                """
                _cmd = "LENGth"
                args = ["'string'"]

            LENGth = LENGth()
            """
            `MMEMory:DCATalog:LENGth
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/a083db692d2a43f1.htm#ID_4e070651900ef70b0a00206a016f7a85-a0f33d76900ef70b0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """

        DCATalog = DCATalog()
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
            _cmd = "DELete"
            args = ["'string'"]

        DELete = DELete()
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
                `MMEMory:LOAD:STATe
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/9de91cebcfaf4dfb.htm#ID_e4b148b6b16d7e450a00206a00d7d85c-f2c489ebb16d7e450a00206a002cfbf4-en-US>`_

                Arguments: <numeric_value>,<string>,<string>
                """
                _cmd = "STATe"
                args = ["<numeric_value>,<string>,<string>"]

            STATe = STATe()
            """
            `MMEMory:LOAD:STATe
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/9de91cebcfaf4dfb.htm#ID_e4b148b6b16d7e450a00206a00d7d85c-f2c489ebb16d7e450a00206a002cfbf4-en-US>`_

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
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/78d90e9c1a164918.htm#ID_28e36f85900ad56d0a00206a01580c40-8ea01a92900ad56d0a00206a01eae7a4-en-US>`_

            Arguments: 'string'
            """
            _cmd = "MDIRectory"
            args = ["'string'"]

        MDIRectory = MDIRectory()
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
            _cmd = "MOVE"
            args = ["<string>,<string>"]

        MOVE = MOVE()
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
            _cmd = "MSIS"
            args = ["'string'"]

        MSIS = MSIS()
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
            _cmd = "RCL"
            args = ["<string>,<string>"]

        RCL = RCL()
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
            _cmd = "RDIRectory"
            args = ["'string'"]

        RDIRectory = RDIRectory()
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
                `MMEMory:STORe:STATe
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/a5614cb446644ab0.htm#ID_45c41292b170604d0a00206a0129c63d-053ce38db170604d0a00206a01567e4b-en-US>`_

                Arguments: <integer>,<string>,<string>
                """
                _cmd = "STATe"
                args = ["<integer>,<string>,<string>"]

            STATe = STATe()
            """
            `MMEMory:STORe:STATe
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/a5614cb446644ab0.htm#ID_45c41292b170604d0a00206a0129c63d-053ce38db170604d0a00206a01567e4b-en-US>`_

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

            class CONDition(SCPINode, SCPIQuery):
                """
                `STATus:OPERation:CONDition
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/eb9e616c44d34723.htm#ID_4d81c86771e8195f0a00206a0077942b-79a3ea6771e8195f0a00206a012bc823-en-US>`_

                Arguments:
                """
                _cmd = "CONDition"
                args = []

            CONDition = CONDition()
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
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()
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
                _cmd = "EVENt"
                args = []

            EVENt = EVENt()
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
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()
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
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()
            """
            `STATus:OPERation:PTRansition
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/19ddd521fccc4c10.htm#ID_7baf119671e812690a00206a0185198a-e4673fbb71e812690a00206a012bc823-en-US>`_

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
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/790fdbfc3c41487f.htm#ID_e484e63b71e7fde70a00206a00a80b3f-98d3fe7771e7fde70a00206a012bc823-en-US>`_

            Arguments:
            """
            _cmd = "PRESet"
            args = []

        PRESet = PRESet()
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

            class CONDition(SCPINode, SCPIQuery):
                """
                `STATus:QUEStionable:CONDition
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/f08a3423b9ea496f.htm#ID_e3fc15a371e842430a00206a009728a6-98e12c6f71e842430a00206a012bc823-en-US>`_

                Arguments:
                """
                _cmd = "CONDition"
                args = []

            CONDition = CONDition()
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
                _cmd = "ENABle"
                args = ["1"]

            ENABle = ENABle()
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
                _cmd = "EVENt"
                args = []

            EVENt = EVENt()
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
                _cmd = "NTRansition"
                args = ["1"]

            NTRansition = NTRansition()
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
                _cmd = "PTRansition"
                args = ["1"]

            PTRansition = PTRansition()
            """
            `STATus:QUEStionable:PTRansition
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/13c14e2f83164444.htm#ID_4ed8eafd71e83b5e0a00206a01c2fbb1-c632286d71e83b5e0a00206a012bc823-en-US>`_

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
                `STATus:QUEue:NEXT
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/4a06b365f17842a7.htm#ID_85f56928ee2f7fee0a001ae7261adfe9-813de58aee2f7e670a001ae72bbdbcb4-en-US>`_

                Arguments:
                """
                _cmd = "NEXT"
                args = []

            NEXT = NEXT()
            """
            `STATus:QUEue:NEXT
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/4a06b365f17842a7.htm#ID_85f56928ee2f7fee0a001ae7261adfe9-813de58aee2f7e670a001ae72bbdbcb4-en-US>`_

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
            `SYSTem:DATE
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/779bb1a4775d490c.htm#ID_09e1ebc9a6ab7e490a001ae70d84cfcf-cf76dd7da6ab7d3f0a001ae71f12f61a-en-US>`_

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
        `SYSTem:DATE
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/779bb1a4775d490c.htm#ID_09e1ebc9a6ab7e490a001ae70d84cfcf-cf76dd7da6ab7d3f0a001ae71f12f61a-en-US>`_

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

            class UPDate(SCPINode, SCPIBool):
                """
                SYSTem:DISPlay:UPDate

                Arguments: 1, ON, OFF
                """
                _cmd = "UPDate"
                args = ["1", "ON", "OFF"]

            UPDate = UPDate()
            """
            SYSTem:DISPlay:UPDate

            Arguments: 1, ON, OFF
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
                `SYSTem:ERRor:ALL
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/7b0fb769f8c94c63.htm#ID_01d81ebc71d1c5670a00206a018810ed-c1e0759071d1c5670a00206a012bc823-en-US>`_

                Arguments:
                """
                _cmd = "ALL"
                args = []

            ALL = ALL()
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
                _cmd = "CODE"
                args = []

                class ALL(SCPINode, SCPIQuery):
                    """
                    `SYSTem:ERRor:CODE:ALL
                    <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/ab9328e7820e4ab2.htm#ID_e106118871d1d3610a00206a00df0731-260d42f471d1d3610a00206a012bc823-en-US>`_

                    Arguments:
                    """
                    _cmd = "ALL"
                    args = []

                ALL = ALL()
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
                    _cmd = "NEXT"
                    args = []

                NEXT = NEXT()
                """
                `SYSTem:ERRor:CODE:NEXT
                <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/7327faef63024f01.htm#ID_782a7ff371d1ccaa0a00206a00d211bc-ce97f85471d1ccaa0a00206a012bc823-en-US>`_

                Arguments:
                """

            CODE = CODE()
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
                _cmd = "COUNt"
                args = []

            COUNt = COUNt()
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
                _cmd = "NEXT"
                args = []

            NEXT = NEXT()
            """
            `SYSTem:ERRor:NEXT
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/9041c827635042ae.htm#ID_3ca90d7f71d1f7830a00206a00d63293-4855f86871d1f7830a00206a012bc823-en-US>`_

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

        class KLOCk(SCPINode, SCPIBool):
            """
            `SYSTem:KLOCk
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/cbb799b612914e37.htm#ID_a7f3c503a58e7f280a00201900122e30-4255d8a4a58e7d430a00201901ee4d9f-en-US>`_

            Arguments: 1, ON, OFF
            """
            _cmd = "KLOCk"
            args = ["1", "ON", "OFF"]

        KLOCk = KLOCk()
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

        class PRESet(SCPINode, SCPISet):
            """
            `SYSTem:PRESet
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/fea01e424ecf4cc4.htm#ID_a64c6dbf4ecf62470a00206a0141ec63-ed39c76a4ecf62470a00206a0024546d-en-US>`_

            Arguments:
            """
            _cmd = "PRESet"
            args = []

        PRESet = PRESet()
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
            _cmd = "TIME"
            args = ["<integer>,<integer>,<integer>"]

            class DSTime(SCPINode):
                """
                SYSTem:TIME:DSTime

                Arguments:
                """
                _cmd = "DSTime"
                args = []

                class MODE(SCPINode, SCPIBool):
                    """
                    SYSTem:TIME:DSTime:MODE

                    Arguments: 1, ON, OFF
                    """
                    _cmd = "MODE"
                    args = ["1", "ON", "OFF"]

                MODE = MODE()
                """
                SYSTem:TIME:DSTime:MODE

                Arguments: 1, ON, OFF
                """

                class RULE(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:TIME:DSTime:RULE

                    Arguments: 'string'
                    """
                    _cmd = "RULE"
                    args = ["'string'"]

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

                Arguments: 'string'
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
        `SYSTem:TIME
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/f17cde1b40ba4722.htm#ID_57f998aba6ab7fcf0a001ae73f23664c-f3909540a6ab7ee50a001ae71f12f61a-en-US>`_

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
            `SYSTem:VERSion
            <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/1687c21d3b684121.htm#ID_83b8bf4871d1f0010a00206a01566d1c-c7a8cef471d1f0010a00206a012bc823-en-US>`_

            Arguments:
            """
            _cmd = "VERSion"
            args = []

        VERSion = VERSion()
        """
        `SYSTem:VERSion
        <http://www.rohde-schwarz.com/webhelp/sma100b_html_usermanual_en/Content/1687c21d3b684121.htm#ID_83b8bf4871d1f0010a00206a01566d1c-c7a8cef471d1f0010a00206a012bc823-en-US>`_

        Arguments:
        """

    SYSTem = SYSTem()
    """
    SYSTem

    Arguments:
    """

    # END OF SMA100B_gen
