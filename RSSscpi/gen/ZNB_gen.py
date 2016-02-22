# -*- coding: utf-8 -*-
# Generated from ZNB_commands_2_56.inp on 2016-02-22 18:54
from SCPI_gen_support import Instrument, SCPINode, SCPINodeN, SCPIQuery, SCPISet
class ZNB_gen(Instrument):
    class CAL(SCPINode, SCPIQuery):
        """
        `*CAL
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*CAL"
        
    class CLS(SCPINode, SCPISet):
        """
        `*CLS
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*CLS"
        
    class ESE(SCPINode, SCPIQuery, SCPISet):
        """
        `*ESE
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*ESE"
        
    class ESR(SCPINode, SCPIQuery, SCPISet):
        """
        `*ESR
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*ESR"
        
    class IDN(SCPINode, SCPIQuery):
        """
        `*IDN
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*IDN"
        
    class IST(SCPINode, SCPIQuery, SCPISet):
        """
        `*IST
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*IST"
        
    class OPC(SCPINode, SCPIQuery, SCPISet):
        """
        `*OPC
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*OPC"
        
    class OPT(SCPINode, SCPIQuery):
        """
        `*OPT
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*OPT"
        
    class PCB(SCPINode, SCPISet):
        """
        `*PCB
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*PCB"
        
    class PRE(SCPINode, SCPIQuery, SCPISet):
        """
        `*PRE
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*PRE"
        
    class PSC(SCPINode, SCPIQuery, SCPISet):
        """
        `*PSC
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*PSC"
        
    class RST(SCPINode, SCPISet):
        """
        `*RST
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*RST"
        
    class SRE(SCPINode, SCPIQuery, SCPISet):
        """
        `*SRE
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*SRE"
        
    class STB(SCPINode, SCPIQuery):
        """
        `*STB
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*STB"
        
    class TRG(SCPINode, SCPISet):
        """
        `*TRG
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*TRG"
        
    class TST(SCPINode, SCPIQuery):
        """
        `*TST
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*TST"
        
    class WAI(SCPINode, SCPISet):
        """
        `*WAI
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e62515.htm>`_
        """
        _cmd = "*WAI"
        
    class DCL(SCPINode, SCPIQuery, SCPISet):
        """
        `@DCL
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8e04d5566c46494a.htm>`_
        """
        _cmd = "@DCL"
        
    class GET(SCPINode, SCPIQuery, SCPISet):
        """
        `@GET
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8e04d5566c46494a.htm>`_
        """
        _cmd = "@GET"
        
    class LOC(SCPINode, SCPIQuery, SCPISet):
        """
        `@LOC
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8e04d5566c46494a.htm>`_
        """
        _cmd = "@LOC"
        
    class REM(SCPINode, SCPIQuery, SCPISet):
        """
        `@REM
        <https://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8e04d5566c46494a.htm>`_
        """
        _cmd = "@REM"
        
    class ABORt(SCPINode, SCPISet):
        """
        `ABORt
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ea9e0c2ff5474211.htm#ID_dd2ff843031772130a00206a0075bedf-1f9dad2503176c760a00206a011f3527-en-US>`_
        """
        _cmd = "ABORt"
        
    class CALCulate(SCPINodeN):
        """
        CALCulate
        """
        _cmd = "CALCulate"
        
        class CLIMits(SCPINode):
            """
            CALCulate:CLIMits
            """
            _cmd = "CLIMits"
            
            class FAIL(SCPINode, SCPIQuery):
                """
                `CALCulate:CLIMits:FAIL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b5d067ff75ce4bc8.htm#ID_eac6ce9afa8821ae0a00206a008389c0-9a887c81fa881c110a00206a01a6673d-en-US>`_
                """
                _cmd = "FAIL"
                
        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:DATA
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a9ce754f8a7c483a.htm#ID_40c37a8cfa8829400a00206a00988dcb-6469059ffa8823920a00206a01a6673d-en-US>`_
            """
            _cmd = "DATA"
            
            class ALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1a55fa6074b44acc.htm#ID_9bc5567afa8830e10a00206a01031e8d-d6457c53fa882b430a00206a01a6673d-en-US>`_
                """
                _cmd = "ALL"
                
            class CALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:CALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/342c7b12f0c3425b.htm#ID_50a40c98350a4f350a00206a008806a1-19dffcd1350a48200a00206a01f2dc17-en-US>`_
                """
                _cmd = "CALL"
                
                class CATalog(SCPINode, SCPIQuery):
                    """
                    `CALCulate:DATA:CALL:CATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2eb08e30e3664412.htm#ID_de9ddd49350a59e30a00206a0057b3a3-d34e11d1350a51e40a00206a01f2dc17-en-US>`_
                    """
                    _cmd = "CATalog"
                    
            class CHANnel(SCPINode):
                """
                CALCulate:DATA:CHANnel
                """
                _cmd = "CHANnel"
                
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:CHANnel:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/67f03a3329554429.htm#ID_a6de926b5d2e7b7d0a001ae706ea3d2c-01ff1e255d2e79c70a001ae75392d2c4-en-US>`_
                    """
                    _cmd = "ALL"
                    
                class DALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:CHANnel:DALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/791f30dde0864bcc.htm#ID_ab2c40015d2e7d900a001ae75e144a27-d22c946e5d2e7c290a001ae75392d2c4-en-US>`_
                    """
                    _cmd = "DALL"
                    
            class DALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:DALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/44cd9ed2bdc14474.htm#ID_6a89a036fa8838a10a00206a00837657-b47c209efa8832c50a00206a01a6673d-en-US>`_
                """
                _cmd = "DALL"
                
            class NSWeep(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:DATA:NSWeep
                """
                _cmd = "NSWeep"
                
                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CALCulate:DATA:NSWeep:COUNt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/df64f664f7c341d7.htm#ID_675c2f06fa8840610a00206a00f5f114-74a998d4fa883a850a00206a01a6673d-en-US>`_
                    """
                    _cmd = "COUNt"
                    
                class FIRSt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:NSWeep:FIRSt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/db653262bea049c8.htm#ID_6f599dcafa8847e30a00206a01cb4396-4834fe6cfa8842360a00206a01a6673d-en-US>`_
                    """
                    _cmd = "FIRSt"
                    
                class LAST(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:NSWeep:LAST
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/68d77cb0c14a4fb8.htm#ID_79dc4d93fa884f650a00206a0014f820-5e0464d9fa8849b80a00206a01a6673d-en-US>`_
                    """
                    _cmd = "LAST"
                    
            class SGRoup(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:SGRoup
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d70ccd328fe648fb.htm#ID_f487020ffa8857250a00206a0013f6a1-b99c255cfa8851490a00206a01a6673d-en-US>`_
                """
                _cmd = "SGRoup"
                
            class STIMulus(SCPINode, SCPIQuery):
                """
                `CALCulate:DATA:STIMulus
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/038ef1cf7a044e85.htm#ID_c099a65ffa885eb70a00206a01a9364f-47a89778fa88590a0a00206a01a6673d-en-US>`_
                """
                _cmd = "STIMulus"
                
            class TRACe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:TRACe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0ccb336efd194e81.htm#ID_c4253b7991da1d150a00206a01d5c62a-8d7fc8c091da15450a00206a00e9ecac-en-US>`_
                """
                _cmd = "TRACe"
                
        class DLINe(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:DLINe
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/789e52d0d45d4a05.htm#ID_86597917fa8866680a00206a00b6f794-18a084d6fa88608c0a00206a01a6673d-en-US>`_
            """
            _cmd = "DLINe"
            
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DLINe:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/92cd9927bed242fd.htm#ID_a1d23145fa886de90a00206a00dd1777-52a9e9affa88684c0a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
        class FILTer(SCPINode):
            """
            CALCulate:FILTer
            """
            _cmd = "FILTer"
            
            class GATE(SCPINode):
                """
                CALCulate:FILTer:GATE
                """
                _cmd = "GATE"
                
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:FILTer:GATE:TIME
                    """
                    _cmd = "TIME"
                    
                    class AOFFset(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:AOFFset
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/13b7cd6211a64886.htm#ID_76a35f12e2b27f340a00201900691b7c-b24d2b5c9d95c7d60a00201901108bad-en-US>`_
                        """
                        _cmd = "AOFFset"
                        
                    class CENTer(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:CENTer
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/708d0e1a2d574ab4.htm#ID_8939aaaffa88756b0a00206a00804a7d-9e5db8b9fa886fce0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "CENTer"
                        
                    class DCHebyshev(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:DCHebyshev
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/65c43bf8cd18408a.htm#ID_7fba1aeafa887cce0a00206a019b2ba1-e5421c59fa8877500a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DCHebyshev"
                        
                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:SHAPe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/54f92ea1195240bc.htm#ID_031b5b73fa88848e0a00206a00b00ed6-d02bdedbfa887ec20a00206a01a6673d-en-US>`_
                        """
                        _cmd = "SHAPe"
                        
                    class SHOW(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:SHOW
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/df1959e8b0fc4cc4.htm#ID_5bdd49f3fa888c000a00206a0155fee8-5df0b4aafa8886730a00206a01a6673d-en-US>`_
                        """
                        _cmd = "SHOW"
                        
                    class SPAN(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:SPAN
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a9ca210cb08a416a.htm#ID_1f821d5afa8893a20a00206a017ae442-3cf5253bfa888df40a00206a01a6673d-en-US>`_
                        """
                        _cmd = "SPAN"
                        
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/76948f89db62434b.htm#ID_839a66a9fa889b620a00206a0160e4c2-22dadc45fa8895960a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STARt"
                        
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1222ca1a6262411a.htm#ID_8cc9db0bfa88a2c40a00206a007a16ad-6e3bd764fa889d370a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/76948f89db62434b.htm#ID_7956fee9fa88aa560a00206a00a34674-2328ec2afa88a4990a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STOP"
                        
                    class TYPE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:TYPE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7b8b789f4a4148ec.htm#ID_3e6d61d6fa88b9690a00206a0013cd15-cb383adafa88b39d0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "TYPE"
                        
                    class WINDow(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:WINDow
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/aa512b0a1a7341fc.htm#ID_ef3431c2fa88b1c80a00206a003380d7-10ec9575fa88ac2b0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "WINDow"
                        
        class FORMat(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:FORMat
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/132d40cd4d1d43c4.htm#ID_d897b8eafa88c10a0a00206a011a6be4-72cc9cedfa88bb4e0a00206a01a6673d-en-US>`_
            """
            _cmd = "FORMat"
            
            class WQUType(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:FORMat:WQUType
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f59df8170e2e48b1.htm#ID_58fe9ca9134bbdc10a00206a01c60d6d-3d8b7753134bb65e0a00206a0182dc26-en-US>`_
                """
                _cmd = "WQUType"
                
        class GDAPerture(SCPINode):
            """
            CALCulate:GDAPerture
            """
            _cmd = "GDAPerture"
            
            class SCOunt(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:GDAPerture:SCOunt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c736cb18a37c4bcf.htm#ID_71a00580fa88f5e50a00206a0102d135-12afaa0ffa88f0380a00206a01a6673d-en-US>`_
                """
                _cmd = "SCOunt"
                
        class LDEViation(SCPINode):
            """
            CALCulate:LDEViation
            """
            _cmd = "LDEViation"
            
            class AUTO(SCPINode, SCPISet):
                """
                CALCulate:LDEViation:AUTO
                """
                _cmd = "AUTO"
                
            class CONStant(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LDEViation:CONStant
                """
                _cmd = "CONStant"
                
            class ELENgth(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LDEViation:ELENgth
                """
                _cmd = "ELENgth"
                
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LDEViation:MODE
                """
                _cmd = "MODE"
                
            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LDEViation:SLOPe
                """
                _cmd = "SLOPe"
                
        class LIMit(SCPINodeN):
            """
            CALCulate:LIMit
            """
            _cmd = "LIMit"
            
            class CIRCle(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:CIRCle
                """
                _cmd = "CIRCle"
                
                class CLEar(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:CIRCle:CLEar
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1f1b628da0ff4632.htm#ID_0e0cda67e2b28c830a00201900760f22-d4bd05cae2b28b4a0a002019017b841c-en-US>`_
                    """
                    _cmd = "CLEar"
                    
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:CIRCle:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2ed038e078b94e81.htm#ID_00d3a3fdbba6da9f0a002019017a3f54-baaba439bba6d9660a0020190170f726-en-US>`_
                    """
                    _cmd = "DATA"
                    
                class DISPlay(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:LIMit:CIRCle:DISPlay
                    """
                    _cmd = "DISPlay"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:CIRCle:DISPlay:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/95c25e5e1cc049ad.htm#ID_02d43bf1bba6dc440a002019016ba97e-a3f8e06fbba6db0c0a0020190170f726-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class FAIL(SCPINode, SCPIQuery):
                    """
                    `CALCulate:LIMit:CIRCle:FAIL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3a8b018f1c4549aa.htm#ID_6567a18abba6ddfa0a002019019eee1a-7b3fc002bba6dcb20a0020190170f726-en-US>`_
                    """
                    _cmd = "FAIL"
                    
                    class ALL(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:CIRCle:FAIL:ALL
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/07f68e8133af4d34.htm#ID_2ef23be7a1e90cd10a001ae723a88db3-dab4fe52a1e90b690a001ae70a9caa95-en-US>`_
                        """
                        _cmd = "ALL"
                        
                class SOUNd(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:LIMit:CIRCle:SOUNd
                    """
                    _cmd = "SOUNd"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:CIRCle:SOUNd:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/154eb220f88d4f32.htm#ID_bc8304e0bba6dfa00a002019016c88e3-6624d71cbba6de770a0020190170f726-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:CIRCle:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/47c20d06725748a5.htm#ID_a38a567ebba6e1550a00201900cb8393-0af63611bba6dffe0a0020190170f726-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class CLEar(SCPINode, SCPISet):
                """
                `CALCulate:LIMit:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f3d7c761247b47f0.htm#ID_dc89d368e2b28f900a0020190141c352-f1766415e2b28e570a002019017b841c-en-US>`_
                """
                _cmd = "CLEar"
                
            class CONTrol(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:CONTrol
                """
                _cmd = "CONTrol"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7fb73b9082124702.htm#ID_8c0418dcfa89330e0a00206a00138405-43be1e80fa892d600a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DATA"
                    
                class DOMain(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:DOMain
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e8aa35068b694faf.htm#ID_b1c1b996fa8923eb0a00206a00a30cbc-432d059efa891e4d0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DOMain"
                    
                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:SHIFt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c0acf94a1b904577.htm#ID_e02c13f2fa892b5d0a00206a00d97f61-ac43656dfa8925bf0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SHIFt"
                    
            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LIMit:DATA
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e65391.htm#ID_0edb9fe4fa893a8f0a00206a0022bc60-e6fbb4aa4b56d1d50a00206a01a60f5f-en-US>`_
                """
                _cmd = "DATA"
                
            class DELete(SCPINode):
                """
                CALCulate:LIMit:DELete
                """
                _cmd = "DELete"
                
                class ALL(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7653993fc6474b79.htm#ID_8a7de250fa8942020a00206a002374c5-0bf55881fa893c740a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ALL"
                    
            class DISPlay(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:DISPlay
                """
                _cmd = "DISPlay"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:DISPlay:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a620fa8c37b143ad.htm#ID_201695c6fa8949930a00206a0137b8c8-b12eb996fa8943e60a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class FAIL(SCPINode, SCPIQuery):
                """
                `CALCulate:LIMit:FAIL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a70d2fed40134890.htm#ID_f86051f1fa8951150a00206a01cb3196-02514d2afa894b770a00206a01a6673d-en-US>`_
                """
                _cmd = "FAIL"
                
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:FAIL:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/11aaccb278fd4696.htm#ID_847e9896a1e911e10a001ae76a2c60e0-ebef358aa1e910b90a001ae70a9caa95-en-US>`_
                    """
                    _cmd = "ALL"
                    
            class LOWer(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:LOWer
                """
                _cmd = "LOWer"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f170628c1afb430e.htm#ID_ce8edc7ffa896f2c0a00206a00e12ff4-d2a79ea4fa89698e0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DATA"
                    
                class FEED(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:FEED
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/736e608ceccb45ab.htm#ID_0a02e1e6fa8958970a00206a01102a1b-58c77064fa8952ea0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "FEED"
                    
                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:SHIFt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ebe098175c6f4345.htm#ID_42c4bc43fa8960280a00206a0190c6a5-473dcd87fa895a7b0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SHIFt"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b94fb57fc16a4021.htm#ID_5e22d895fa89679a0a00206a0189df49-6c41edc1fa8961fd0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class RDOMain(SCPINode):
                """
                CALCulate:LIMit:RDOMain
                """
                _cmd = "RDOMain"
                
                class COMPlex(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:RDOMain:COMPlex
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/238f51657b44402d.htm#ID_1bfa6dc5fa89770c0a00206a011e3406-6dd1f87bfa89715e0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "COMPlex"
                    
                class FORMat(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:RDOMain:FORMat
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6cac5c97886d4899.htm#ID_d0fa1e97fa897ecc0a00206a00a410e7-fc19fdddfa8978f00a00206a01a6673d-en-US>`_
                    """
                    _cmd = "FORMat"
                    
                class SPACing(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:RDOMain:SPACing
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/fbdd7a3d75284494.htm#ID_d10f581ffa89866d0a00206a01cdc12f-072c5dfcfa8980c00a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SPACing"
                    
            class SEGMent(SCPINodeN):
                """
                CALCulate:LIMit:SEGMent
                """
                _cmd = "SEGMent"
                
                class AMPLitude(SCPINode):
                    """
                    CALCulate:LIMit:SEGMent:AMPLitude
                    """
                    _cmd = "AMPLitude"
                    
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:AMPLitude:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/11b0747d8e944b4b.htm#ID_79d6b03cfa898f560a00206a0037e778-eaa1c80cfa89898a0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STARt"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:AMPLitude:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/11b0747d8e944b4b.htm#ID_82e40f82fa8996d80a00206a019caca5-517eee2dfa89913b0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STOP"
                        
                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CALCulate:LIMit:SEGMent:COUNt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f00309e159e4411c.htm#ID_a4781db3fa899eb80a00206a004cbe94-9a955102fa8998cc0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "COUNt"
                    
                class STIMulus(SCPINode):
                    """
                    CALCulate:LIMit:SEGMent:STIMulus
                    """
                    _cmd = "STIMulus"
                    
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:STIMulus:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d668e7d16044438d.htm#ID_d1275cb9fa89a6590a00206a01db09d6-4a3c58bdfa89a09c0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STARt"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:STIMulus:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d668e7d16044438d.htm#ID_f98528d0fa89adbb0a00206a011164e6-65241391fa89a83d0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STOP"
                        
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:SEGMent:TYPE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2b4cba8b57db4862.htm#ID_b6e64935fa89b55c0a00206a00c5b92a-00be6b1ffa89afa00a00206a01a6673d-en-US>`_
                    """
                    _cmd = "TYPE"
                    
            class SOUNd(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:SOUNd
                """
                _cmd = "SOUNd"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:SOUNd:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/eecfbfbc00724725.htm#ID_8cff667afa89bd0d0a00206a002b9bb9-c7083814fa89b7310a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LIMit:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/41d4ae0c38fe49c4.htm#ID_a2351470fa89c49f0a00206a003ef800-63a4586cfa89bef20a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:STATe:AREA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9d9e42e32fcf45e6.htm#ID_e4bbdf5091dad73d0a00206a015f6524-9e0d80eb91dacdd70a00206a00e9ecac-en-US>`_
                    """
                    _cmd = "AREA"
                    
            class TTLout(SCPINodeN, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:TTLout
                """
                _cmd = "TTLout"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:TTLout:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8c5a247317814d57.htm#ID_cbcffdacfa89ccbd0a00206a00b40a25-4afe7823fa89c6930a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class UPPer(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:UPPer
                """
                _cmd = "UPPer"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f170628c1afb430e.htm#ID_bc7a4fc8fa89ebbe0a00206a0189234d-9a27fa013c961f1f0a00201901e2ea6c-en-US>`_
                    """
                    _cmd = "DATA"
                    
                class FEED(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:FEED
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/736e608ceccb45ab.htm#ID_120c8703fa89d46d0a00206a0192176f-bb730b26fa89cea10a00206a01a6673d-en-US>`_
                    """
                    _cmd = "FEED"
                    
                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:SHIFt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ebe098175c6f4345.htm#ID_4049dd9cfa89dbff0a00206a01134819-274d8fa3fa89d6610a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SHIFt"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b94fb57fc16a4021.htm#ID_63005ebdfa89e3ee0a00206a016ea114-723fb281fa89ddf30a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
        class MARKer(SCPINodeN, SCPIQuery, SCPISet):
            """
            CALCulate:MARKer
            """
            _cmd = "MARKer"
            
            class AOFF(SCPINode, SCPISet):
                """
                `CALCulate:MARKer:AOFF
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/fa000f93fd4f4c5b.htm#ID_c984dcecfa89f38e0a00206a00d27a1c-ca2a1fc1fa89edb20a00206a01a6673d-en-US>`_
                """
                _cmd = "AOFF"
                
            class BWIDth(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:BWIDth
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8db4f4a0d76a456e.htm#ID_c87ace40fa89fb3f0a00206a01891879-b1201654fa89f5820a00206a01a6673d-en-US>`_
                """
                _cmd = "BWIDth"
                
            class COUPled(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MARKer:COUPled
                """
                _cmd = "COUPled"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:COUPled:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1bd62bd7692f4e41.htm#ID_3afb171ffa8a030f0a00206a00a6f15a-8e7bcef9fa89fd230a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class DEFault(SCPINode):
                """
                CALCulate:MARKer:DEFault
                """
                _cmd = "DEFault"
                
                class FORMat(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:DEFault:FORMat
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f47b7220e9a24599.htm#ID_a1916f36353430b80a001ae733a2d25d-cf535f9435342f120a001ae72ac1dc63-en-US>`_
                    """
                    _cmd = "FORMat"
                    
            class DELTa(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MARKer:DELTa
                """
                _cmd = "DELTa"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:DELTa:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9a00eb7a33d84165.htm#ID_2ac31b0bfa8a0aa00a00206a014d68e5-7bbe3cfbfa8a04f30a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class FORMat(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:FORMat
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4c7af5ff6777435b.htm#ID_0c7f97fada30383f0a001ae704ff0606-a607c8b9fa8a0c750a00206a01a6673d-en-US>`_
                """
                _cmd = "FORMat"
                
            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MARKer:FUNCtion
                """
                _cmd = "FUNCtion"
                
                class APEak(SCPINode):
                    """
                    CALCulate:MARKer:FUNCtion:APEak
                    """
                    _cmd = "APEak"
                    
                    class THReshold(SCPINode, SCPIQuery, SCPISet):
                        """
                        CALCulate:MARKer:FUNCtion:APEak:THReshold
                        """
                        _cmd = "THReshold"
                        
                class BWIDth(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:BWIDth
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/18d64e401a3c4d78.htm#ID_e192fb1bfa8a28e60a00206a0079aa26-15468232fa8a23290a00206a01a6673d-en-US>`_
                    """
                    _cmd = "BWIDth"
                    
                    class GMCenter(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:BWIDth:GMCenter
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9ea2897cc2074b65.htm#ID_09cba1695d2e9a7e0a001ae73dea0c2a-40db97d65d2e98f80a001ae75392d2c4-en-US>`_
                        """
                        _cmd = "GMCenter"
                        
                    class MODE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:BWIDth:MODE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0a26f3b8139d4bb4.htm#ID_791788fefa8a30c60a00206a00649e10-787c5f72fa8a2abb0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "MODE"
                        
                class CENTer(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:CENTer
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8c94020d00ed4c26.htm#ID_365edbb4fa8a38960a00206a00bd8439-2a58127bfa8a32ba0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CENTer"
                    
                class DELTa(SCPINode):
                    """
                    CALCulate:MARKer:FUNCtion:DELTa
                    """
                    _cmd = "DELTa"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:DELTa:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6b65d72689764580.htm#ID_1d43c878fa8a40660a00206a011298cf-abb3447cfa8a3a8a0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class DOMain(SCPINode):
                    """
                    CALCulate:MARKer:FUNCtion:DOMain
                    """
                    _cmd = "DOMain"
                    
                    class USER(SCPINode, SCPIQuery, SCPISet):
                        """
                        CALCulate:MARKer:FUNCtion:DOMain:USER
                        """
                        _cmd = "USER"
                        
                        class RANGe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:RANGe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2af2a460e1634e13.htm#ID_ec748740a1e91ec20a001ae73c718e26-cff20544a1e91da90a001ae70a9caa95-en-US>`_
                            """
                            _cmd = "RANGe"
                            
                        class SHOW(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:SHOW
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b996f7d9a11b400a.htm#ID_0bf0909ffa8a4fe60a00206a01917992-7f696627fa8a49dc0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "SHOW"
                            
                        class STARt(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:STARt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6b09f447b71d417a.htm#ID_a5f79d01fa8a57e50a00206a002de6dc-52538baffa8a51ea0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "STARt"
                            
                        class STOP(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:STOP
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6b09f447b71d417a.htm#ID_687ae9d6fa8a60030a00206a007c1291-2f4051c6fa8a59ca0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "STOP"
                            
                class EXECute(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:EXECute
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/600b76c1f17b4625.htm#ID_0f48fc24fa8a67f30a00206a017b7ffd-4761b5f8fa8a61e80a00206a01a6673d-en-US>`_
                    """
                    _cmd = "EXECute"
                    
                class RESult(SCPINode, SCPIQuery):
                    """
                    `CALCulate:MARKer:FUNCtion:RESult
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c4a647dafdef46ee.htm#ID_ca4abd32fa8a6f840a00206a01da7da1-6cf5cdc7fa8a69c70a00206a01a6673d-en-US>`_
                    """
                    _cmd = "RESult"
                    
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c95147813aef4387.htm#ID_28ad0b13fa8a8e860a00206a002e5875-64e78ee7fa8a884c0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SELect"
                    
                class SPAN(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:SPAN
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d16c29d1400f4678.htm#ID_8d68f92e6c02ab810a00206a01c2603f-22bc3ca36c02a4da0a00206a01eade93-en-US>`_
                    """
                    _cmd = "SPAN"
                    
                class STARt(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:STARt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ceab94aa505047d1.htm#ID_c6f90737fa8a77350a00206a00929601-35edf04bfa8a71780a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STARt"
                    
                class STOP(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:STOP
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ceab94aa505047d1.htm#ID_c5b678bdfa8a7ed60a00206a007ab819-384b0a87fa8a790a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STOP"
                    
                class TARGet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:TARGet
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7c2d30605ca841ae.htm#ID_bc960c67fa8a86770a00206a0083f28b-98cf2789fa8a80ab0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "TARGet"
                    
            class MAXimum(SCPINode, SCPISet):
                """
                `CALCulate:MARKer:MAXimum
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dd071845c23d417a.htm#ID_8c34c922fa8a983a0a00206a00c82880-06d37e32fa8a91160a00206a01a6673d-en-US>`_
                """
                _cmd = "MAXimum"
                
            class MINimum(SCPINode, SCPISet):
                """
                `CALCulate:MARKer:MINimum
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dd071845c23d417a.htm#ID_4ad27e65fa8aa1420a00206a0153b85a-e85401f8fa8a9aba0a00206a01a6673d-en-US>`_
                """
                _cmd = "MINimum"
                
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:MODE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4010b689c6bf4ec7.htm#ID_b49e503bfa8aa9af0a00206a01c8eac3-1a6dc12efa8aa3a40a00206a01a6673d-en-US>`_
                """
                _cmd = "MODE"
                
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d956e2c3002e4abd.htm#ID_a680fdc9fa8ab2980a00206a000a65ae-163ea644fa8aaba30a00206a01a6673d-en-US>`_
                """
                _cmd = "NAME"
                
            class REFerence(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MARKer:REFerence
                """
                _cmd = "REFerence"
                
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/44bfec6a89d24ef8.htm#ID_603a1492fa8abac50a00206a0069c536-856117a3fa8ab5180a00206a01a6673d-en-US>`_
                    """
                    _cmd = "MODE"
                    
                class NAME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:NAME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/87ac5dca438a4cdd.htm#ID_999919fdfa8ac2950a00206a01882570-c28c1b05fa8abc9a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "NAME"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6ea0ed2e1ddf4f74.htm#ID_38b890f5fa8b86330a00206a01954afc-5cd7d92dfa8b80760a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:TYPE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7c0f3d498f264e9e.htm#ID_20c235fafa8b6eb30a00206a01dede11-49a0afa4fa8b685a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "TYPE"
                    
                class X(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:X
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/57b141f2e2c44fb9.htm#ID_17e585b9fa8b76b20a00206a002d73ab-c4bf51adfa8b70980a00206a01a6673d-en-US>`_
                    """
                    _cmd = "X"
                    
                class Y(SCPINode, SCPIQuery):
                    """
                    `CALCulate:MARKer:REFerence:Y
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/90520d3afddd4fde.htm#ID_6e8f4665fa8b7e630a00206a01ed19b0-7b490ccffa8b78b60a00206a01a6673d-en-US>`_
                    """
                    _cmd = "Y"
                    
            class SEARch(SCPINode, SCPISet):
                """
                CALCulate:MARKer:SEARch
                """
                _cmd = "SEARch"
                
                class BFILter(SCPINode):
                    """
                    CALCulate:MARKer:SEARch:BFILter
                    """
                    _cmd = "BFILter"
                    
                    class RESult(SCPINode, SCPIQuery, SCPISet):
                        """
                        CALCulate:MARKer:SEARch:BFILter:RESult
                        """
                        _cmd = "RESult"
                        
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:SEARch:BFILter:RESult:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f2d891a03a1d49f9.htm#ID_b0cb39b7fa8b8e410a00206a00d7eda6-57e9f681fa8b88080a00206a01a6673d-en-US>`_
                            """
                            _cmd = "STATe"
                            
                            class AREA(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:MARKer:SEARch:BFILter:RESult:STATe:AREA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e2feccae7432448d.htm#ID_3d27cc9c91db00ce0a00206a01798cde-8853842091daf8230a00206a00e9ecac-en-US>`_
                                """
                                _cmd = "AREA"
                                
                class FORMat(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:FORMat
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d201a42d7ccc45ed.htm#ID_365c6ea35de572610a00201900016e84-655449015de571290a0020190152315a-en-US>`_
                    """
                    _cmd = "FORMat"
                    
                class IMMediate(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:IMMediate
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4a78723c9cff4eef.htm#ID_8220efeafa8bb61c0a00206a002cc9cf-50585b86fa8baff20a00206a01a6673d-en-US>`_
                    """
                    _cmd = "IMMediate"
                    
                class LEFT(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:LEFT
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cdfa7b0040b0418c.htm#ID_8278f555fa8b96210a00206a0146cca2-c96c28e0fa8b90160a00206a01a6673d-en-US>`_
                    """
                    _cmd = "LEFT"
                    
                class NEXT(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:NEXT
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cdfa7b0040b0418c.htm#ID_3ef4139bfa8b9de10a00206a0020e6d6-55733c3dfa8b98150a00206a01a6673d-en-US>`_
                    """
                    _cmd = "NEXT"
                    
                class RIGHt(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:RIGHt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cdfa7b0040b0418c.htm#ID_f8f11fcbfa8ba61f0a00206a00095eea-c2ff6c7afa8ba0330a00206a01a6673d-en-US>`_
                    """
                    _cmd = "RIGHt"
                    
                class TRACking(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:TRACking
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/50067f6406044da9.htm#ID_47207a16fa8bae0e0a00206a008d852a-04f0dca6fa8ba8220a00206a01a6673d-en-US>`_
                    """
                    _cmd = "TRACking"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d0472df6b3cb40c9.htm#ID_e745149dfa8be1340a00206a01305b71-b428f5aefa8bdb380a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:STATe:AREA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/59688d861c344dbc.htm#ID_4bccbbec91db0bda0a00206a01d2f8b1-2b62471a91db04390a00206a00e9ecac-en-US>`_
                    """
                    _cmd = "AREA"
                    
            class TARGet(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:TARGet
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8f93a1eedbcb4346.htm#ID_6773dc66fa8bbe890a00206a01e71f6d-ee358b16fa8bb7f10a00206a01a6673d-en-US>`_
                """
                _cmd = "TARGet"
                
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:TYPE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8740dafec1944a52.htm#ID_6ec07d71fa8bc8aa0a00206a01cd9de5-4689d12efa8bc0ea0a00206a01a6673d-en-US>`_
                """
                _cmd = "TYPE"
                
            class X(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:X
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4ef3e6895bcf42b7.htm#ID_2358db0ffa8bd1840a00206a01e12053-393c91dcfa8bcb690a00206a01a6673d-en-US>`_
                """
                _cmd = "X"
                
            class Y(SCPINode, SCPIQuery):
                """
                `CALCulate:MARKer:Y
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8d8c242cdd7e4572.htm#ID_68d57989fa8bd9540a00206a0034e41b-a588c4c5fa8bd3590a00206a01a6673d-en-US>`_
                """
                _cmd = "Y"
                
        class MATH(SCPINode, SCPIQuery, SCPISet):
            """
            CALCulate:MATH
            """
            _cmd = "MATH"
            
            class EXPRession(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MATH:EXPRession
                """
                _cmd = "EXPRession"
                
                class DEFine(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MATH:EXPRession:DEFine
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/49b93df4d2974c24.htm#ID_8520d66dfa8c11b90a00206a002e410f-5fdc9322fa8c0c0c0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DEFine"
                    
                class SDEFine(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MATH:EXPRession:SDEFine
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7d726687c3514fa3.htm#ID_a2f75c6cfa8c0a370a00206a0145ed97-d61bd978fa8c049a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SDEFine"
                    
            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MATH:FUNCtion
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ffdc5ec43e98489c.htm#ID_39a94accfa8be8b50a00206a00eb9289-d8e4b798fa8be3080a00206a01a6673d-en-US>`_
                """
                _cmd = "FUNCtion"
                
            class MEMorize(SCPINode, SCPISet):
                """
                `CALCulate:MATH:MEMorize
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1bc091561bf04c5d.htm#ID_8c53fd1afa8bf20c0a00206a01fcb1ce-8e069e7efa8beb260a00206a01a6673d-en-US>`_
                """
                _cmd = "MEMorize"
                
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MATH:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5826421b58a046ed.htm#ID_68bf5aa0fa8bfae60a00206a01d8cc25-038f9478fa8bf43e0a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
            class WUNit(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MATH:WUNit
                """
                _cmd = "WUNit"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MATH:WUNit:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9628726622464f1c.htm#ID_020fd1e7fa8c02c50a00206a01046c97-6a5ac2ccfa8bfce90a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
        class PARameter(SCPINode):
            """
            CALCulate:PARameter
            """
            _cmd = "PARameter"
            
            class CATalog(SCPINode, SCPIQuery):
                """
                `CALCulate:PARameter:CATalog
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2ce049f1af684d21.htm#ID_6d0f03abfa8c193b0a00206a003b5f50-8685a90cfa8c13bd0a00206a01a6673d-en-US>`_
                """
                _cmd = "CATalog"
                
                class SENDed(SCPINode, SCPIQuery):
                    """
                    `CALCulate:PARameter:CATalog:SENDed
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4aaff69b21544d46.htm#ID_72b3d670842dc4af0a00201900a9cfc5-ae203438842dc3380a00201901936165-en-US>`_
                    """
                    _cmd = "SENDed"
                    
            class DEFine(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:DEFine
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/85c286e91d1f45c1.htm#ID_c26a23a6fa8c20bd0a00206a01ef3d1b-d5d71622fa8c1b100a00206a01a6673d-en-US>`_
                """
                _cmd = "DEFine"
                
                class SGRoup(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:PARameter:DEFine:SGRoup
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/78a4125ac51a435a.htm#ID_119cf020fa8c283f0a00206a00a5b7f1-6f48d8a2fa8c22920a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SGRoup"
                    
            class DELete(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:DELete
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0763f74d0a2d4d61.htm#ID_8f70dcdefa8c2fe00a00206a003b801c-ee007debfa8c2a330a00206a01a6673d-en-US>`_
                """
                _cmd = "DELete"
                
                class ALL(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e69977.htm#ID_aaf85c1de1568dfc0a00206a01ec5604-135cad8de15685420a00206a00796295-en-US>`_
                    """
                    _cmd = "ALL"
                    
                class CALL(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:CALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8d937272d97244fb.htm#ID_8d9ff76be156a6a50a00206a01182ba4-6f8706dce1569d5e0a00206a00796295-en-US>`_
                    """
                    _cmd = "CALL"
                    
                class CMEMory(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:CMEMory
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cc3d9af74e704b5c.htm#ID_a75b324c4b6a080e0a001ae706c6f2b3-ded67b324b6a04740a001ae708cb241d-en-US>`_
                    """
                    _cmd = "CMEMory"
                    
                class MEMory(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:MEMory
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4613fe70603c4f9d.htm#ID_96a98c814b6a0ce00a001ae76e6a3196-75f503b24b6a09d30a001ae708cb241d-en-US>`_
                    """
                    _cmd = "MEMory"
                    
                class SGRoup(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:SGRoup
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bc5ac4b592724e7a.htm#ID_f2764fe1fa8c37520a00206a01e48f49-65ba2f61fa8c31b50a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SGRoup"
                    
            class MEASure(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:PARameter:MEASure
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/10abfaa35dcf40f3.htm#ID_b2e7e077fa8c3ef30a00206a00c865a1-07a6d833fa8c39460a00206a01a6673d-en-US>`_
                """
                _cmd = "MEASure"
                
                class SENDed(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:PARameter:MEASure:SENDed
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c7009e9c24ab41ca.htm#ID_e36c8c14842dcc210a00201900ce962e-6d066a16842dcac90a00201901936165-en-US>`_
                    """
                    _cmd = "SENDed"
                    
            class SDEFine(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:SDEFine
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e75d49e2a14541c5.htm#ID_e2a5b54afa8c4dd80a00206a00d8bd4a-b73200d6fa8c482b0a00206a01a6673d-en-US>`_
                """
                _cmd = "SDEFine"
                
                class SENDed(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:SDEFine:SENDed
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/87172ee6d3f0486d.htm#ID_22046707842dcee00a002019009c3503-c048e5e3842dcd5a0a00201901936165-en-US>`_
                    """
                    _cmd = "SENDed"
                    
            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:PARameter:SELect
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3c03effa6de64ee5.htm#ID_fa5a7dabfa8c555a0a00206a00a4a885-9edb1c2efa8c4fac0a00206a01a6673d-en-US>`_
                """
                _cmd = "SELect"
                
        class PHOLd(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:PHOLd
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7be6f52751ea485d.htm#ID_98d0d154fa8c5cfb0a00206a01cc0c79-20de90e3fa8c573e0a00206a01a6673d-en-US>`_
            """
            _cmd = "PHOLd"
            
        class RIPPle(SCPINode):
            """
            CALCulate:RIPPle
            """
            _cmd = "RIPPle"
            
            class CLEar(SCPINode, SCPISet):
                """
                `CALCulate:RIPPle:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bc102c309ca64801.htm#ID_30c2583ee2b2b2890a00201901f4a3cf-911a2616e2b2b1600a002019017b841c-en-US>`_
                """
                _cmd = "CLEar"
                
            class CONTrol(SCPINode):
                """
                CALCulate:RIPPle:CONTrol
                """
                _cmd = "CONTrol"
                
                class DOMain(SCPINode, SCPISet):
                    """
                    `CALCulate:RIPPle:CONTrol:DOMain
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/efa433eb0a4a488d.htm#ID_6271dbebfa8c648c0a00206a01bc324d-fe0c5318fa8c5edf0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DOMain"
                    
            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:RIPPle:DATA
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/003f16e0af9744b9.htm#ID_bd72ae33fa8c6bfe0a00206a0156adc6-dec22044fa8c66700a00206a01a6673d-en-US>`_
                """
                _cmd = "DATA"
                
            class DELete(SCPINode):
                """
                CALCulate:RIPPle:DELete
                """
                _cmd = "DELete"
                
                class ALL(SCPINode, SCPISet):
                    """
                    `CALCulate:RIPPle:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/80e7731362314ea3.htm#ID_cb829192fa8c73710a00206a00e729bd-16eb12ddfa8c6de30a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ALL"
                    
            class DISPlay(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:RIPPle:DISPlay
                """
                _cmd = "DISPlay"
                
                class RESult(SCPINode):
                    """
                    CALCulate:RIPPle:DISPlay:RESult
                    """
                    _cmd = "RESult"
                    
                    class ALL(SCPINode, SCPIQuery, SCPISet):
                        """
                        CALCulate:RIPPle:DISPlay:RESult:ALL
                        """
                        _cmd = "ALL"
                        
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:RIPPle:DISPlay:RESult:ALL:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9252124bcddc41e8.htm#ID_283b9afd5d2eb3c30a001ae73e7db882-361816a15d2eb29a0a001ae75392d2c4-en-US>`_
                            """
                            _cmd = "STATe"
                            
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:DISPlay:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/af30ef097a4240bb.htm#ID_eec53853fa8c7af20a00206a017b8a53-82ea5f14fa8c75360a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class FAIL(SCPINode, SCPIQuery):
                """
                `CALCulate:RIPPle:FAIL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a6f184c34daa43c5.htm#ID_2d1b4441fa8c82840a00206a01c73f6d-bcd238bdfa8c7cc70a00206a01a6673d-en-US>`_
                """
                _cmd = "FAIL"
                
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:FAIL:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3ff9874b75fd4b77.htm#ID_982687eba1e9377a0a001ae71d33ac9e-7cc4d3dda1e936130a001ae70a9caa95-en-US>`_
                    """
                    _cmd = "ALL"
                    
            class RDOMain(SCPINode):
                """
                CALCulate:RIPPle:RDOMain
                """
                _cmd = "RDOMain"
                
                class FORMat(SCPINode, SCPISet):
                    """
                    `CALCulate:RIPPle:RDOMain:FORMat
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/96a8405a7acb4768.htm#ID_c02c1b65fa8c89f60a00206a00ef0219-80cbde3efa8c84590a00206a01a6673d-en-US>`_
                    """
                    _cmd = "FORMat"
                    
            class SEGMent(SCPINodeN, SCPIQuery, SCPISet):
                """
                CALCulate:RIPPle:SEGMent
                """
                _cmd = "SEGMent"
                
                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CALCulate:RIPPle:SEGMent:COUNt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f6dd927483bd4b0b.htm#ID_157eedbefa8c91680a00206a01a10a29-76eb58c0fa8c8bda0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "COUNt"
                    
                class LIMit(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:SEGMent:LIMit
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b53e47cd6ee84c63.htm#ID_c0af3f18fa8c98ea0a00206a0153bc80-411a2a59fa8c934d0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "LIMit"
                    
                class RESult(SCPINode, SCPIQuery):
                    """
                    `CALCulate:RIPPle:SEGMent:RESult
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/588bd177edf54661.htm#ID_5ae347ddfa8ca08b0a00206a00280543-d97d0bb0fa8c9acf0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "RESult"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:SEGMent:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/56affa087259447b.htm#ID_a7b1806cfa8cb77e0a00206a017e3363-e5617d47fa8cb1c10a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
                class STIMulus(SCPINode):
                    """
                    CALCulate:RIPPle:SEGMent:STIMulus
                    """
                    _cmd = "STIMulus"
                    
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:RIPPle:SEGMent:STIMulus:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e14be574123e48c9.htm#ID_a5c3ac7ffa8ca83c0a00206a017a8448-adda4ba4fa8ca2600a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STARt"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:RIPPle:SEGMent:STIMulus:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e14be574123e48c9.htm#ID_10f947ddfa8cafed0a00206a0105be95-4d344ccefa8caa200a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STOP"
                        
            class SOUNd(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:RIPPle:SOUNd
                """
                _cmd = "SOUNd"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:SOUNd:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3bf0aae076bc42bc.htm#ID_52557a3ffa8cbf100a00206a01806165-0b45785ffa8cb9530a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:RIPPle:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/fb623ebe7fb54f9b.htm#ID_f43adfc2fa8cc6820a00206a0172e6f5-e09bed1cfa8cc0e40a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:STATe:AREA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4dc1b5a2821a4ae3.htm#ID_34fca1f991db93590a00206a01c30472-e3489bde91db8a700a00206a00e9ecac-en-US>`_
                    """
                    _cmd = "AREA"
                    
        class SMOothing(SCPINode, SCPIQuery, SCPISet):
            """
            CALCulate:SMOothing
            """
            _cmd = "SMOothing"
            
            class APERture(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:SMOothing:APERture
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/529f93d8d2414119.htm#ID_0e07cb25fa8cce420a00206a0171f8ab-81a86b0efa8cc8660a00206a01a6673d-en-US>`_
                """
                _cmd = "APERture"
                
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:SMOothing:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7811d02911894706.htm#ID_671d4593fa8cd6120a00206a0062fcac-cbb8b985fa8cd0270a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
        class STATistics(SCPINode, SCPIQuery, SCPISet):
            """
            CALCulate:STATistics
            """
            _cmd = "STATistics"
            
            class DOMain(SCPINode):
                """
                CALCulate:STATistics:DOMain
                """
                _cmd = "DOMain"
                
                class USER(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:STATistics:DOMain:USER
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a589efe7a4ea4cd2.htm#ID_9f963f50fa8cddb30a00206a005d21da-5aafc2dafa8cd7f70a00206a01a6673d-en-US>`_
                    """
                    _cmd = "USER"
                    
                    class SHOW(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:DOMain:USER:SHOW
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7c04e1dc565f42fe.htm#ID_9b274ca7fa8ce5160a00206a01e534b5-014aff7efa8cdf880a00206a01a6673d-en-US>`_
                        """
                        _cmd = "SHOW"
                        
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:DOMain:USER:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8684a6f4edc14a42.htm#ID_feacdf2cfa8cec880a00206a00658f5d-d35f250cfa8ce6eb0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STARt"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:DOMain:USER:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8684a6f4edc14a42.htm#ID_9e04cc6bfa8cf4390a00206a016f509f-161fec51fa8cee9b0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STOP"
                        
            class EPDelay(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:STATistics:EPDelay
                """
                _cmd = "EPDelay"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:STATistics:EPDelay:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dd777ffb23ef4a85.htm#ID_ddeec772fa8cfbca0a00206a00768219-c4a76b8efa8cf61d0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class FORMat(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:STATistics:FORMat
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5af594af8b3d4ad3.htm#ID_9c03469b97e84b1c0a001ae7788a17fc-113e556897e849e40a001ae760f7f904-en-US>`_
                """
                _cmd = "FORMat"
                
            class MMPTpeak(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:STATistics:MMPTpeak
                """
                _cmd = "MMPTpeak"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:STATistics:MMPTpeak:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dd777ffb23ef4a85.htm#ID_70eaa25efa8d034c0a00206a01b86abd-878c52c8fa8cfdbe0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class MSTDdev(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:STATistics:MSTDdev
                """
                _cmd = "MSTDdev"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:STATistics:MSTDdev:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dd777ffb23ef4a85.htm#ID_68163564fa8d0ace0a00206a006a35c4-9131f9e9fa8d05210a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class NLINear(SCPINode):
                """
                CALCulate:STATistics:NLINear
                """
                _cmd = "NLINear"
                
                class COMP(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:STATistics:NLINear:COMP
                    """
                    _cmd = "COMP"
                    
                    class LEVel(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:NLINear:COMP:LEVel
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5d6c51b169d74dd1.htm#ID_c925aca6fa8d127f0a00206a00d4d7e8-4b0de918fa8d0cc20a00206a01a6673d-en-US>`_
                        """
                        _cmd = "LEVel"
                        
                    class RESult(SCPINode, SCPIQuery):
                        """
                        `CALCulate:STATistics:NLINear:COMP:RESult
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d066840052e34270.htm#ID_877f774dfa8d1a010a00206a000c5799-9a74d1cdfa8d14730a00206a01a6673d-en-US>`_
                        """
                        _cmd = "RESult"
                        
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:NLINear:COMP:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6bb074b56dab4d34.htm#ID_4bc3ff91fa8d21920a00206a00c0450c-b88e3168fa8d1bd50a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
            class RESult(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:STATistics:RESult
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/504c1240aaf84b48.htm#ID_9ad8a052fa8d29240a00206a018e8f49-cc55af54fa8d23670a00206a01a6673d-en-US>`_
                """
                _cmd = "RESult"
                
            class RMS(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:STATistics:RMS
                """
                _cmd = "RMS"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:STATistics:RMS:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5ab4519994e14adf.htm#ID_3614abc9fa8d30860a00206a00131843-d95b7e56fa8d2af80a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class SFLatness(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:STATistics:SFLatness
                """
                _cmd = "SFLatness"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:STATistics:SFLatness:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5ab4519994e14adf.htm#ID_4120133afa8d38180a00206a01da59ef-a95d681dfa8d326b0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:STATistics:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2f7b3f85defe4eb2.htm#ID_a5c56f11fa8d3f8a0a00206a001597a1-2c31185bfa8d39fc0a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:STATistics:STATe:AREA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f48f70d27489445d.htm#ID_97e5221b91dbbcea0a00206a01e4bef3-0cc1fe9b91dbb5680a00206a00e9ecac-en-US>`_
                    """
                    _cmd = "AREA"
                    
        class TRANsform(SCPINode):
            """
            CALCulate:TRANsform
            """
            _cmd = "TRANsform"
            
            class COMPlex(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:TRANsform:COMPlex
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0ddb2fb52f9647b1.htm#ID_6763dcf5fa8d4ebc0a00206a0172615e-fc0db3f8fa8d492f0a00206a01a6673d-en-US>`_
                """
                _cmd = "COMPlex"
                
            class IMPedance(SCPINode):
                """
                CALCulate:TRANsform:IMPedance
                """
                _cmd = "IMPedance"
                
                class RNORmal(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:IMPedance:RNORmal
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/14e821102ae54212.htm#ID_559024ddfa8d563e0a00206a008657c0-5f0233befa8d50a10a00206a01a6673d-en-US>`_
                    """
                    _cmd = "RNORmal"
                    
            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:TRANsform:TIME
                """
                _cmd = "TIME"
                
                class CENTer(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:CENTer
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2d5ae32dc5f84be0.htm#ID_35afe348fa8d5dd00a00206a010edee7-6f4e2e2afa8d58320a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CENTer"
                    
                class DCHebyshev(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:DCHebyshev
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bd1362285dd64cb0.htm#ID_4c77cbdefa8d668a0a00206a012d61e1-ecea3751fa8d60ed0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DCHebyshev"
                    
                class LPASs(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:LPASs
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f526f7ddf2884d92.htm#ID_170ddb9dfa8d6e0c0a00206a0187917f-377f1619fa8d686e0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "LPASs"
                    
                    class DCSParam(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:TRANsform:TIME:LPASs:DCSParam
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/53ce9e90e07e4a51.htm#ID_4a46c475fa8d75cc0a00206a01e0e76f-bd956431fa8d6fe10a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DCSParam"
                        
                        class CONTinuous(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:TIME:LPASs:DCSParam:CONTinuous
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/eb8dd59636a74569.htm#ID_1c2005cafa8d7d4e0a00206a0174e6c4-98d7bc34fa8d77b10a00206a01a6673d-en-US>`_
                            """
                            _cmd = "CONTinuous"
                            
                        class EXTRapolate(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:TIME:LPASs:DCSParam:EXTRapolate
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2dcd2a27ce744b66.htm#ID_675aa806fa8d84c00a00206a01e30f89-cfb2563cfa8d7f230a00206a01a6673d-en-US>`_
                            """
                            _cmd = "EXTRapolate"
                            
                class LPFRequency(SCPINode, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:LPFRequency
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/27b41786fbb64c8c.htm#ID_e86cd025fa8d8c610a00206a00c7bfc0-581fc947fa8d86a50a00206a01a6673d-en-US>`_
                    """
                    _cmd = "LPFRequency"
                    
                class METHod(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:TRANsform:TIME:METHod
                    """
                    _cmd = "METHod"
                    
                class RESolution(SCPINode):
                    """
                    CALCulate:TRANsform:TIME:RESolution
                    """
                    _cmd = "RESolution"
                    
                    class EFACtor(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:TRANsform:TIME:RESolution:EFACtor
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/635fc83aab98475a.htm#ID_ed455756fa8d9b840a00206a01cbf0cc-c0ea7111fa8d95c80a00206a01a6673d-en-US>`_
                        """
                        _cmd = "EFACtor"
                        
                class SPAN(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:SPAN
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1e787fde60e7484a.htm#ID_e25bd601fa8da3060a00206a00fa1352-d688e1b8fa8d9d590a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SPAN"
                    
                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STARt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8ea0328127044ba9.htm#ID_6070a8edfa8daa980a00206a0032a239-a965258ffa8da4fa0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STARt"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/83fed5073fde47ee.htm#ID_024e8732fa8db2480a00206a01f94674-e8c96f45fa8dac7c0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
                class STIMulus(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STIMulus
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0157afe1515d4140.htm#ID_2274ec00fa8db9ea0a00206a01a73a83-47ff8851fa8db41d0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STIMulus"
                    
                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STOP
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4cd73ad6216545c4.htm#ID_c1eb53d4fa8dc18b0a00206a01c01ff2-c6268d0cfa8dbbce0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STOP"
                    
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:TYPE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/baf83ae4b9fc4af4.htm#ID_883048c0fa8dd8200a00206a001376e6-4965ba92fa8dd2920a00206a01a6673d-en-US>`_
                    """
                    _cmd = "TYPE"
                    
                class WINDow(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:WINDow
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/aac0f28b6e3041a6.htm#ID_08a5b679fa8dc92c0a00206a0171d219-eeb23c46fa8dc38e0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "WINDow"
                    
                class XAXis(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:XAXis
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2e1c9ec5c19b4efa.htm#ID_9a53dbaffa8dd0ae0a00206a01f538e4-a3eff330fa8dcb010a00206a01a6673d-en-US>`_
                    """
                    _cmd = "XAXis"
                    
            class VNETworks(SCPINode):
                """
                CALCulate:TRANsform:VNETworks
                """
                _cmd = "VNETworks"
                
                class BALanced(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:BALanced
                    """
                    _cmd = "BALanced"
                    
                    class DEEMbedding(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding
                        """
                        _cmd = "DEEMbedding"
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6f0c9d49615148c7.htm#ID_dd8133a4fa8ddfc10a00206a01185633-3d70b06bfa8dda040a00206a01a6673d-en-US>`_
                                """
                                _cmd = "C"
                                
                            class DATA(SCPINodeN, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:DATA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/59ae1ad9a60e4c58.htm#ID_84293532842de3240a00201901e6e490-deedc1c0842de18d0a00201901936165-en-US>`_
                                """
                                _cmd = "DATA"
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3cb1c25a3e284cac.htm#ID_2b5d169b6f6624690a001ae7153f6596-6c03f7b66f6622f20a001ae727f5f310-en-US>`_
                                """
                                _cmd = "G"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1186eea832df4546.htm#ID_d84a0ce1fa8de7720a00206a00f5bb24-31cd32e7fa8de1a50a00206a01a6673d-en-US>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f2ea1c1f6a88461f.htm#ID_a9c33f0dfa8def320a00206a00518f0d-c5a4cd8ffa8de9560a00206a01a6673d-en-US>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4d9b6ee9116348ce.htm#ID_5172a9c4fa8dfe550a00206a01e07981-787e7537fa8df8980a00206a01a6673d-en-US>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/12448e2e96f04df7.htm#ID_2a7d63bbfa8df6b40a00206a01d43e88-8940a4f2fa8df1160a00206a01a6673d-en-US>`_
                            """
                            _cmd = "TNDefinition"
                            
                    class EMBedding(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        CALCulate:TRANsform:VNETworks:BALanced:EMBedding
                        """
                        _cmd = "EMBedding"
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8ec140379660414a.htm#ID_abf3f1e2fa8e05b80a00206a01a47cb4-e08b0c9ffa8e002a0a00206a01a6673d-en-US>`_
                                """
                                _cmd = "C"
                                
                            class DATA(SCPINodeN, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:DATA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/079e83a8c9584f42.htm#ID_5d9cf2fb842de70c0a00201900076709-7b992475842de5850a00201901936165-en-US>`_
                                """
                                _cmd = "DATA"
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2ccae92408394fe5.htm#ID_7dea03e06f66334e0a001ae707928781-33d95ab56f6631c70a001ae727f5f310-en-US>`_
                                """
                                _cmd = "G"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a81a26b3e8d64942.htm#ID_ad04c1a1fa8e0d780a00206a0035eeba-bf4cbae4fa8e07ac0a00206a01a6673d-en-US>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/45b9a3fe38f24521.htm#ID_f782d205fa8e15290a00206a00731edf-a1857f58fa8e0f6c0a00206a01a6673d-en-US>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0941b76a5f064868.htm#ID_4cee94dffa8e242c0a00206a001fceaf-644e4ad9fa8e1e8f0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2c2c0962a3db4ae5.htm#ID_44ab70c2fa8e1cab0a00206a0136415c-a9f9c620fa8e16fd0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "TNDefinition"
                            
                class DIFFerential(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:DIFFerential
                    """
                    _cmd = "DIFFerential"
                    
                    class EMBedding(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding
                        """
                        _cmd = "EMBedding"
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/80c9a3cffb4f4e17.htm#ID_429e54d35811f7050a001ae7223f1761-c3650e9b5811f5500a001ae75f9ff217-en-US>`_
                                """
                                _cmd = "C"
                                
                            class DATA(SCPINodeN, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters:DATA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ba87af15592944b1.htm#ID_6111424c5811f9d40a001ae752b7f8db-8e717b935811f84d0a001ae75f9ff217-en-US>`_
                                """
                                _cmd = "DATA"
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4b188e3593414a28.htm#ID_0fc049035811fc830a001ae77896ac76-12d2ae9f5811fb0c0a001ae75f9ff217-en-US>`_
                                """
                                _cmd = "G"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1e62e495ff464265.htm#ID_e5653d405811ff140a001ae77606ea04-ba2c9fd65811fd7d0a001ae75f9ff217-en-US>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f95acab1da68435d.htm#ID_ed781559581202110a001ae74e1270a2-65654e575812004c0a001ae75f9ff217-en-US>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/148b0faee7ee405f.htm#ID_54768ad0581204d00a001ae71ebb62bb-6c8d7c8c5812031b0a001ae75f9ff217-en-US>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/fa133c6be7354958.htm#ID_63150e8d581207700a001ae7722d3053-8579f2a0581205ab0a001ae75f9ff217-en-US>`_
                            """
                            _cmd = "TNDefinition"
                            
                class FSIMulator(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:TRANsform:VNETworks:FSIMulator
                    """
                    _cmd = "FSIMulator"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:TRANsform:VNETworks:FSIMulator:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d757c633360247c7.htm#ID_11fd85585d2ecf890a001ae7384a35ab-7de5b54a5d2ecdd30a001ae75392d2c4-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class GLOop(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:GLOop
                    """
                    _cmd = "GLOop"
                    
                    class DEEMbedding(SCPINode, SCPIQuery, SCPISet):
                        """
                        CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding
                        """
                        _cmd = "DEEMbedding"
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/77956e5cf93946b3.htm#ID_81fff10dfa8e2bae0a00206a01a4b72d-5b3e5f86fa8e26110a00206a01a6673d-en-US>`_
                                """
                                _cmd = "C"
                                
                            class G(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/aac6592ce85444e2.htm#ID_f8b2f8696f6642710a001ae710afca50-2f4c4e8c6f6640fa0a001ae727f5f310-en-US>`_
                                """
                                _cmd = "G"
                                
                            class L(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7a422b2f995d4f9a.htm#ID_a8965c72fa8e338e0a00206a0026bd75-609f9708fa8e2d830a00206a01a6673d-en-US>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5a1c1c036d584ff6.htm#ID_c0cffff5fa8e3b1f0a00206a008fe948-51c74c06fa8e35720a00206a01a6673d-en-US>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/97f3857893904d79.htm#ID_159ddfd4fa8e4a330a00206a013b7c49-dc269bc4fa8e44a50a00206a01a6673d-en-US>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/799259b2b62f4149.htm#ID_2f36ab34fa8e42c00a00206a01fc84f3-043babf2fa8e3d040a00206a01a6673d-en-US>`_
                            """
                            _cmd = "TNDefinition"
                            
                    class EMBedding(SCPINode, SCPIQuery, SCPISet):
                        """
                        CALCulate:TRANsform:VNETworks:GLOop:EMBedding
                        """
                        _cmd = "EMBedding"
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5ea6451ed3a94d89.htm#ID_37668013fa8e51d40a00206a00c15700-894bed2efa8e4c360a00206a01a6673d-en-US>`_
                                """
                                _cmd = "C"
                                
                            class G(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/53607605721e41d0.htm#ID_dc37fee66f664fb00a001ae766fe6587-ed213d396f664dfa0a001ae727f5f310-en-US>`_
                                """
                                _cmd = "G"
                                
                            class L(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6c564130695147b8.htm#ID_b2cd795dfa8e59840a00206a01453521-97ac064cfa8e53b80a00206a01a6673d-en-US>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dbd85ab533b642e6.htm#ID_ed15dbb6fa8e61640a00206a01db511f-4a7a9660fa8e5b690a00206a01a6673d-en-US>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f05d33e191e54ad2.htm#ID_337b7158fa8e70970a00206a01e3e1bf-ad84cdf0fa8e6ada0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/99b65e02d497406d.htm#ID_756d6eb0fa8e68e60a00206a008cf339-f9a8da34fa8e63390a00206a01a6673d-en-US>`_
                            """
                            _cmd = "TNDefinition"
                            
                class PPAir(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:PPAir
                    """
                    _cmd = "PPAir"
                    
                    class DEEMbedding(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding
                        """
                        _cmd = "DEEMbedding"
                        
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:DEFine
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e8becb0a3078421b.htm#ID_3ba674b458120daa0a001ae715a0e5be-c703d9d69646cc8e0a001ae72394529b-en-US>`_
                            """
                            _cmd = "DEFine"
                            
                        class DELete(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:DELete
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/43d0e6d7b4144b08.htm#ID_1722509658120fbd0a001ae75e11b532-0381552758120e750a001ae75f9ff217-en-US>`_
                            """
                            _cmd = "DELete"
                            
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:C
                                """
                                _cmd = "C"
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:G
                                """
                                _cmd = "G"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:L
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:R
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/46b480af07bb407f.htm#ID_4b3324f7581218d60a001ae751738823-c02afe855812176e0a001ae75f9ff217-en-US>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/35ec3220c32e4f80.htm#ID_3c16a3b758121b560a001ae77271577c-a49e9fde581219ef0a001ae75f9ff217-en-US>`_
                            """
                            _cmd = "TNDefinition"
                            
                    class EMBedding(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        CALCulate:TRANsform:VNETworks:PPAir:EMBedding
                        """
                        _cmd = "EMBedding"
                        
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:DEFine
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e400839544a94301.htm#ID_e83fd23258121d790a001ae73123507a-8e751156970d6a920a001ae74f7a64ee-en-US>`_
                            """
                            _cmd = "DEFine"
                            
                        class DELete(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:DELete
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6c61769117054661.htm#ID_6ae62e5b58121ffa0a001ae712441e42-cabb03ec58121e540a001ae75f9ff217-en-US>`_
                            """
                            _cmd = "DELete"
                            
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:C
                                """
                                _cmd = "C"
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:G
                                """
                                _cmd = "G"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:L
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:R
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/db97017adcc64a9d.htm#ID_d3a37976581229510a001ae71520611c-bfc8ef34581227ca0a001ae75f9ff217-en-US>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f4fd86459812485c.htm#ID_85b0b37258122b930a001ae750c1f98b-d10f3fff58122a0c0a001ae75f9ff217-en-US>`_
                            """
                            _cmd = "TNDefinition"
                            
                class PSET(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:PSET
                    """
                    _cmd = "PSET"
                    
                    class DEEMbedding(SCPINodeN):
                        """
                        CALCulate:TRANsform:VNETworks:PSET:DEEMbedding
                        """
                        _cmd = "DEEMbedding"
                        
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PSET:DEEMbedding:DEFine
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/481a0c5b67654aaf.htm#ID_a38b0ffd97e86de70a001ae7390e6333-de29757a97e86c8f0a001ae760f7f904-en-US>`_
                            """
                            _cmd = "DEFine"
                            
                    class EMBedding(SCPINodeN):
                        """
                        CALCulate:TRANsform:VNETworks:PSET:EMBedding
                        """
                        _cmd = "EMBedding"
                        
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PSET:EMBedding:DEFine
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f6b188400f7d4c8e.htm#ID_2cfc1d2497e86fbb0a001ae70cbfb36f-5d787a8997e86e830a001ae760f7f904-en-US>`_
                            """
                            _cmd = "DEFine"
                            
                class SENDed(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:SENDed
                    """
                    _cmd = "SENDed"
                    
                    class DEEMbedding(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding
                        """
                        _cmd = "DEEMbedding"
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8f37b1c2acee44bf.htm#ID_5ef9469cfa8e78470a00206a003fb9da-e1c64a86fa8e727b0a00206a01a6673d-en-US>`_
                                """
                                _cmd = "C"
                                
                            class DATA(SCPINodeN, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:DATA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9fd3cb7e82ed444d.htm#ID_367ed7c5842dee7e0a0020190086f675-49915501842decb90a00201901936165-en-US>`_
                                """
                                _cmd = "DATA"
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c51043739b194e65.htm#ID_7cd42ef3aac442490a00201901b51a4b-b2bda20baac440650a002019014405dd-en-US>`_
                                """
                                _cmd = "G"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ee2ffa524efe4143.htm#ID_ae17b162fa8e7fe80a00206a01b10570-63778782fa8e7a3b0a00206a01a6673d-en-US>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/fd7eabf9c9fe4f75.htm#ID_65259074fa8e877a0a00206a01c1d949-59bdb169fa8e81cd0a00206a01a6673d-en-US>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/099a019b9af84e28.htm#ID_4425e038fa8e96ad0a00206a00a9bdd8-133ea7b3fa8e90ff0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/adbe16aed5bc4ba6.htm#ID_193f4b02fa8e8f2b0a00206a01d1a2a2-594a30cefa8e895e0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "TNDefinition"
                            
                    class EMBedding(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        CALCulate:TRANsform:VNETworks:SENDed:EMBedding
                        """
                        _cmd = "EMBedding"
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9b3802e99dd04934.htm#ID_47ea57dcfa8e9e5d0a00206a01f8e797-a5454548fa8e98a00a00206a01a6673d-en-US>`_
                                """
                                _cmd = "C"
                                
                            class DATA(SCPINodeN, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:DATA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bc40013c1fd34de5.htm#ID_792b4296842df3210a00201901d6e9a7-4e187817842df19b0a00201901936165-en-US>`_
                                """
                                _cmd = "DATA"
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c2e016fdee4e41e6.htm#ID_bcec6412aac4474a0a00201900615633-9bb80280aac445370a002019014405dd-en-US>`_
                                """
                                _cmd = "G"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/39cdaea4416a4c45.htm#ID_3c73b93dfa9057760a00206a0177c3c0-94278c7cfa9051a90a00206a01a6673d-en-US>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/60828f5f8b0946d5.htm#ID_06bb1196fa905f070a00206a01dc29e4-44a83d6cfa90595a0a00206a01a6673d-en-US>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ea669d4abf8a4e28.htm#ID_b1752cc1fa906e1a0a00206a01a677d6-a6a35038fa90685e0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9741b5a2d5bc4f7b.htm#ID_8abb2864fa9066890a00206a0099762f-e45993bafa9060dc0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "TNDefinition"
                            
    class CONFigure(SCPINode):
        """
        CONFigure
        """
        _cmd = "CONFigure"
        
        class CHANnel(SCPINodeN, SCPIQuery, SCPISet):
            """
            CONFigure:CHANnel
            """
            _cmd = "CHANnel"
            
            class CATalog(SCPINode, SCPIQuery):
                """
                `CONFigure:CHANnel:CATalog
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e78199.htm#ID_8267d8bffa90756d0a00206a012834d2-871f66dffa906fe00a00206a01a6673d-en-US>`_
                """
                _cmd = "CATalog"
                
            class MEASure(SCPINode, SCPIQuery, SCPISet):
                """
                CONFigure:CHANnel:MEASure
                """
                _cmd = "MEASure"
                
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    CONFigure:CHANnel:MEASure:ALL
                    """
                    _cmd = "ALL"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONFigure:CHANnel:MEASure:ALL:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e78231.htm#ID_958019b491dbf9e30a00206a01973116-3beacfd491dbf1670a00206a00e9ecac-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:CHANnel:MEASure:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2cd5e872062a431e.htm#ID_1cd54e3791dc03680a00206a012bd79a-94a956b691dbfc250a00206a00e9ecac-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:CHANnel:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a31923122bab4e11.htm#ID_c3f9c539fa907cef0a00206a008fc1b5-8cf66519fa9077420a00206a01a6673d-en-US>`_
                """
                _cmd = "NAME"
                
                class ID(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:CHANnel:NAME:ID
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/da0a7bd5700f41f7.htm#ID_abefaec0fa9084b00a00206a000fc09f-f57f33a0fa907ec40a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ID"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:CHANnel:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5e82d96f75e24caa.htm#ID_2b6e28fdfa9093940a00206a00cd97da-23931b64fa908de70a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
            class TRACe(SCPINode):
                """
                CONFigure:CHANnel:TRACe
                """
                _cmd = "TRACe"
                
                class CATalog(SCPINode, SCPIQuery):
                    """
                    `CONFigure:CHANnel:TRACe:CATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/08f2ade572024bd1.htm#ID_516e93ea91dc10e50a00206a01e04d6b-a40a757391dc09640a00206a00e9ecac-en-US>`_
                    """
                    _cmd = "CATalog"
                    
                class REName(SCPINode, SCPISet):
                    """
                    `CONFigure:CHANnel:TRACe:REName
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bbb28f18094c4ae3.htm#ID_21f2bb55fa908c030a00206a0107df1a-9e702520fa9086840a00206a01a6673d-en-US>`_
                    """
                    _cmd = "REName"
                    
        class TRACe(SCPINodeN):
            """
            CONFigure:TRACe
            """
            _cmd = "TRACe"
            
            class CATalog(SCPINode, SCPIQuery):
                """
                `CONFigure:TRACe:CATalog
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e78557.htm#ID_bce7da14fa909b060a00206a01cbd9eb-e44e55bcfa9095780a00206a01a6673d-en-US>`_
                """
                _cmd = "CATalog"
                
            class CHANnel(SCPINode):
                """
                CONFigure:TRACe:CHANnel
                """
                _cmd = "CHANnel"
                
                class NAME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:TRACe:CHANnel:NAME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f94c4fcfb8094e4b.htm#ID_860185e0fa90a2980a00206a0129ec0d-0cfb8c52fa909ceb0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "NAME"
                    
                    class ID(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONFigure:TRACe:CHANnel:NAME:ID
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/67062066b08c4c45.htm#ID_a007ba5bfa90aa0a0a00206a01848bb0-2e75d305fa90a47c0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "ID"
                        
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:TRACe:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7a040ceb2d3a4047.htm#ID_e80abd45fa90b18c0a00206a01f4249c-c4d0154ffa90abee0a00206a01a6673d-en-US>`_
                """
                _cmd = "NAME"
                
                class ID(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:TRACe:NAME:ID
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1f10213a5d6b4a80.htm#ID_295113b4fa90b8fe0a00206a001dfba5-cb7079e8fa90b3700a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ID"
                    
            class REName(SCPINode, SCPISet):
                """
                `CONFigure:TRACe:REName
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d4f06d994adb4ffa.htm#ID_18b7574dfa90c0af0a00206a01c49181-40592207fa90bad30a00206a01a6673d-en-US>`_
                """
                _cmd = "REName"
                
            class WINDow(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:TRACe:WINDow
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/668ea0c870b04c50.htm#ID_5352b2a291dc2c4d0a00206a005b7de7-e194934291dc23a20a00206a00e9ecac-en-US>`_
                """
                _cmd = "WINDow"
                
                class TRACe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:TRACe:WINDow:TRACe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/46d9e1a8f3dd4c7f.htm#ID_148894f091dc38240a00206a01003829-5f3601f391dc2edd0a00206a00e9ecac-en-US>`_
                    """
                    _cmd = "TRACe"
                    
    class CONTrol(SCPINodeN):
        """
        CONTrol
        """
        _cmd = "CONTrol"
        
        class AUXiliary(SCPINode):
            """
            CONTrol:AUXiliary
            """
            _cmd = "AUXiliary"
            
            class C(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:AUXiliary:C
                """
                _cmd = "C"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:AUXiliary:C:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e78969.htm#ID_a8a179f7fa90c8400a00206a0033f6f5-e626ca43fa90c2840a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DATA"
                    
        class GPIO(SCPINodeN, SCPIQuery, SCPISet):
            """
            CONTrol:GPIO
            """
            _cmd = "GPIO"
            
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CONTrol:GPIO:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/33808ac223674735.htm#ID_d3192ded066b0d0c0a001ae756c50460-6c688743066b0a5c0a001ae733608be0-en-US>`_
                """
                _cmd = "STATe"
                
            class VOLTage(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:GPIO:VOLTage
                """
                _cmd = "VOLTage"
                
                class DEFault(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:GPIO:VOLTage:DEFault
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6d98569ee4824333.htm#ID_8470b084066b0ffa0a001ae758e7691b-a4394381066b0dd70a001ae733608be0-en-US>`_
                    """
                    _cmd = "DEFault"
                    
                class OUTPut(SCPINode, SCPISet):
                    """
                    `CONTrol:GPIO:VOLTage:OUTPut
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/17e1726b8d244456.htm#ID_a95593b7066b13260a001ae702394225-a4f6f8d5066b10e40a001ae733608be0-en-US>`_
                    """
                    _cmd = "OUTPut"
                    
        class HANDler(SCPINode):
            """
            CONTrol:HANDler
            """
            _cmd = "HANDler"
            
            class A(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:A
                """
                _cmd = "A"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:A:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0f573cb5afe64caf.htm#ID_384549a9fa90d7630a00206a01da5d48-204d2afafa90d1970a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DATA"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:A:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e9cbd6865a25403a.htm#ID_fd883255fa90cfc20a00206a01b43b71-8197967cfa90ca150a00206a01a6673d-en-US>`_
                    """
                    _cmd = "MODE"
                    
            class B(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:B
                """
                _cmd = "B"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:B:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0f573cb5afe64caf.htm#ID_82e32087fa90e6480a00206a009d90d0-a680df72fa90e0aa0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DATA"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:B:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e9cbd6865a25403a.htm#ID_df1b2421fa90dec60a00206a001fe8f9-a8227d8efa90d9280a00206a01a6673d-en-US>`_
                    """
                    _cmd = "MODE"
                    
            class C(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:C
                """
                _cmd = "C"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:C:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0f573cb5afe64caf.htm#ID_3f9af4e0fa90f57a0a00206a004e2c4f-374a812bfa90efec0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DATA"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:C:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e9cbd6865a25403a.htm#ID_30067fb2fa90ee180a00206a0024945a-45be43defa90e81c0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "MODE"
                    
            class D(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:D
                """
                _cmd = "D"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:D:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0f573cb5afe64caf.htm#ID_d89e93e0fa91044f0a00206a0185bd14-2a93a2aafa90fec10a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DATA"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:D:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e9cbd6865a25403a.htm#ID_f1fbb137fa90fcec0a00206a011639d8-dc1e6f5bfa90f75f0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "MODE"
                    
            class E(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:E
                """
                _cmd = "E"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:E:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0f573cb5afe64caf.htm#ID_03af4eaaaaa71b910a00206a014d37c1-e591bdf3aaa710370a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "DATA"
                    
            class EXTension(SCPINode):
                """
                CONTrol:HANDler:EXTension
                """
                _cmd = "EXTension"
                
                class INDex(SCPINode):
                    """
                    CONTrol:HANDler:EXTension:INDex
                    """
                    _cmd = "INDex"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:HANDler:EXTension:INDex:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e79453.htm#ID_9ab7d58afa9122e30a00206a00a25190-37519af1fa911d260a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class RTRigger(SCPINode):
                    """
                    CONTrol:HANDler:EXTension:RTRigger
                    """
                    _cmd = "RTRigger"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:HANDler:EXTension:RTRigger:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e79504.htm#ID_822beadefa912aa30a00206a00c2e325-f42ab4a7fa9124e70a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
            class F(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:F
                """
                _cmd = "F"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:F:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0f573cb5afe64caf.htm#ID_65360c0daaa728920a00206a01178ad5-9c82b188aaa71e7f0a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "DATA"
                    
            class G(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:G
                """
                _cmd = "G"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:G:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0f573cb5afe64caf.htm#ID_2f4e59f6aaa737090a00206a01d8c5a5-d3dd0524aaa72ae30a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "DATA"
                    
            class H(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:H
                """
                _cmd = "H"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:H:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0f573cb5afe64caf.htm#ID_84a2a7bcaaa7460c0a00206a01237959-7700b423aaa73a350a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "DATA"
                    
            class INPut(SCPINode, SCPIQuery, SCPISet):
                """
                `CONTrol:HANDler:INPut
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/70a4807bdab549b6.htm#ID_817928e6aaa7560a0a00206a010ca1ce-6f60b089aaa749770a00206a00dee6b8-en-US>`_
                """
                _cmd = "INPut"
                
            class LOGic(SCPINode, SCPIQuery, SCPISet):
                """
                `CONTrol:HANDler:LOGic
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e79581.htm#ID_f78b1faaaaa766d30a00206a00cb9c6b-84654118aaa758e80a00206a00dee6b8-en-US>`_
                """
                _cmd = "LOGic"
                
            class OUTPut(SCPINodeN, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:OUTPut
                """
                _cmd = "OUTPut"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:OUTPut:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ef6b44dd6cba4bbd.htm#ID_eec504bdfa9113d00a00206a004e84e5-63c0c051fa910df40a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DATA"
                    
                class USER(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:OUTPut:USER
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d384e87b03b14621.htm#ID_b6012b5ffa910c0f0a00206a00a5d890-7969a7c7fa9106240a00206a01a6673d-en-US>`_
                    """
                    _cmd = "USER"
                    
            class PASSfail(SCPINode):
                """
                CONTrol:HANDler:PASSfail
                """
                _cmd = "PASSfail"
                
                class LOGic(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:PASSfail:LOGic
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e79768.htm#ID_2595b82eaaa775590a00206a007fcf6d-a5b09155aaa769530a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "LOGic"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:PASSfail:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e79818.htm#ID_f9bf98a0aaa783340a00206a00322e82-b914a914aaa777ea0a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "MODE"
                    
                class POLicy(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:PASSfail:POLicy
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e79902.htm#ID_c5cf67d0aaa791ca0a00206a00b576ef-911cc27baaa785c40a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "POLicy"
                    
                class SCOPe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:PASSfail:SCOPe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e79952.htm#ID_8f644a34aaa7a10c0a00206a01c34f32-a532dcccaaa794f70a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "SCOPe"
                    
                class STATus(SCPINode, SCPIQuery):
                    """
                    `CONTrol:HANDler:PASSfail:STATus
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e80012.htm#ID_669da323aaa7adfd0a00206a01e58d7b-4babcd6caaa7a3eb0a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "STATus"
                    
            class RESet(SCPINode, SCPISet):
                """
                `CONTrol:HANDler:RESet
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e80059.htm#ID_feafcc0afa911b520a00206a01d0958a-3c810aa7fa9115c40a00206a01a6673d-en-US>`_
                """
                _cmd = "RESet"
                
            class SWEepend(SCPINode, SCPIQuery, SCPISet):
                """
                `CONTrol:HANDler:SWEepend
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e80078.htm#ID_4b826235aaa7c8f70a00206a001fcebb-4e04fab1aaa7bc740a00206a00dee6b8-en-US>`_
                """
                _cmd = "SWEepend"
                
        class RFFE(SCPINodeN):
            """
            CONTrol:RFFE
            """
            _cmd = "RFFE"
            
            class COMMand(SCPINode):
                """
                CONTrol:RFFE:COMMand
                """
                _cmd = "COMMand"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:RFFE:COMMand:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/aede8dcd348f4fab.htm#ID_3502760a066b1f8a0a001ae70c239c0e-3f81058e066b1d770a001ae733608be0-en-US>`_
                    """
                    _cmd = "DATA"
                    
                class SEND(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:RFFE:COMMand:SEND
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/79a9cbb958e04a7e.htm#ID_7aebff11066b22b70a001ae7728c5d1d-199a3e2481dfee9f0a001ae738278eca-en-US>`_
                    """
                    _cmd = "SEND"
                    
            class SETTings(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:RFFE:SETTings
                """
                _cmd = "SETTings"
                
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:RFFE:SETTings:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/86e7d9e9c64a4b80.htm#ID_e0afbdf3066b25c40a001ae7374f4675-88aae4cd066b23820a001ae733608be0-en-US>`_
                    """
                    _cmd = "FREQuency"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:RFFE:SETTings:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ad56e7c2cd4c4c48.htm#ID_6e7676fa066b28440a001ae71c2aa9ef-7614426b066b26ae0a001ae733608be0-en-US>`_
                    """
                    _cmd = "STATe"
                    
                class VOLTage(SCPINode):
                    """
                    CONTrol:RFFE:SETTings:VOLTage
                    """
                    _cmd = "VOLTage"
                    
                    class HIGH(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:RFFE:SETTings:VOLTage:HIGH
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/40122cc0e02b4df5.htm#ID_b7836816066b2b330a001ae7691148d3-90a164dd966b72ac0a001ae70f280944-en-US>`_
                        """
                        _cmd = "HIGH"
                        
                    class IO(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:RFFE:SETTings:VOLTage:IO
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/40122cc0e02b4df5.htm#ID_911e89b3066b2da40a001ae73936a740-8055592b066b2bee0a001ae733608be0-en-US>`_
                        """
                        _cmd = "IO"
                        
                    class LOW(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:RFFE:SETTings:VOLTage:LOW
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/40122cc0e02b4df5.htm#ID_d872d092066b30630a001ae75ad2e77f-1722156d066b2e8e0a001ae733608be0-en-US>`_
                        """
                        _cmd = "LOW"
                        
        class SEGMent(SCPINodeN):
            """
            CONTrol:SEGMent
            """
            _cmd = "SEGMent"
            
            class SEQuence(SCPINodeN):
                """
                CONTrol:SEGMent:SEQuence
                """
                _cmd = "SEQuence"
                
                class CLEar(SCPINode):
                    """
                    CONTrol:SEGMent:SEQuence:CLEar
                    """
                    _cmd = "CLEar"
                    
                    class ALL(SCPINode, SCPISet):
                        """
                        `CONTrol:SEGMent:SEQuence:CLEar:ALL
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dce45392f23d4cd1.htm#ID_ba1740ff066b32e30a001ae7038cc690-e385c4e6066b312e0a001ae733608be0-en-US>`_
                        """
                        _cmd = "ALL"
                        
                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CONTrol:SEGMent:SEQuence:COUNt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/863ad1f221e34a86.htm#ID_d8be4e36066b35060a001ae76687ab53-7eee6fdf066b33be0a001ae733608be0-en-US>`_
                    """
                    _cmd = "COUNt"
                    
                class DELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:SEGMent:SEQuence:DELay
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cad27b08f5cd4a59.htm#ID_ff5337c49a5a3eae0a001ae7055abd97-52198a0c066b36ac0a001ae733608be0-en-US>`_
                    """
                    _cmd = "DELay"
                    
                class GPIO(SCPINodeN):
                    """
                    CONTrol:SEGMent:SEQuence:GPIO
                    """
                    _cmd = "GPIO"
                    
                    class VOLTage(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:SEGMent:SEQuence:GPIO:VOLTage
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d59396a2d7e04724.htm#ID_b11ac4b4066b3b210a001ae7511309cd-19aa6061066b394c0a001ae733608be0-en-US>`_
                        """
                        _cmd = "VOLTage"
                        
                class RFFE(SCPINodeN):
                    """
                    CONTrol:SEGMent:SEQuence:RFFE
                    """
                    _cmd = "RFFE"
                    
                    class COMMand(SCPINode):
                        """
                        CONTrol:SEGMent:SEQuence:RFFE:COMMand
                        """
                        _cmd = "COMMand"
                        
                        class DATA(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CONTrol:SEGMent:SEQuence:RFFE:COMMand:DATA
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/391f2dd3ce594a86.htm#ID_06ace371066b3e5d0a001ae77224664e-1fcbae3c066b3c0b0a001ae733608be0-en-US>`_
                            """
                            _cmd = "DATA"
                            
        class SEQuence(SCPINodeN):
            """
            CONTrol:SEQuence
            """
            _cmd = "SEQuence"
            
            class CLEar(SCPINode):
                """
                CONTrol:SEQuence:CLEar
                """
                _cmd = "CLEar"
                
                class ALL(SCPINode, SCPISet):
                    """
                    `CONTrol:SEQuence:CLEar:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ae61df9a65994430.htm#ID_333f4491066b40ce0a001ae721c73f52-88df1fd0066b3f090a001ae733608be0-en-US>`_
                    """
                    _cmd = "ALL"
                    
            class COUNt(SCPINode, SCPIQuery):
                """
                `CONTrol:SEQuence:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/17252f9e8804497b.htm#ID_f18ea6b6066b42f10a001ae70911d2e1-27e2fa22066b416a0a001ae733608be0-en-US>`_
                """
                _cmd = "COUNt"
                
            class DELay(SCPINode, SCPIQuery, SCPISet):
                """
                `CONTrol:SEQuence:DELay
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0bb940016a74464e.htm#ID_d484ffa7066b45230a001ae716a8581a-0dce9372066b43ac0a001ae733608be0-en-US>`_
                """
                _cmd = "DELay"
                
            class GPIO(SCPINodeN):
                """
                CONTrol:SEQuence:GPIO
                """
                _cmd = "GPIO"
                
                class VOLTage(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:SEQuence:GPIO:VOLTage
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3fb7df3527744c2b.htm#ID_61c443f1066b47850a001ae76731bb7b-8bcc6627066b460e0a001ae733608be0-en-US>`_
                    """
                    _cmd = "VOLTage"
                    
            class RFFE(SCPINodeN):
                """
                CONTrol:SEQuence:RFFE
                """
                _cmd = "RFFE"
                
                class COMMand(SCPINode):
                    """
                    CONTrol:SEQuence:RFFE:COMMand
                    """
                    _cmd = "COMMand"
                    
                    class DATA(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:SEQuence:RFFE:COMMand:DATA
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b78d712928e44350.htm#ID_fca5b214066b4a240a001ae74dd3450e-e2ac204e066b48500a001ae733608be0-en-US>`_
                        """
                        _cmd = "DATA"
                        
    class DIAGnostic(SCPINode):
        """
        DIAGnostic
        """
        _cmd = "DIAGnostic"
        
        class ALC(SCPINode):
            """
            DIAGnostic:ALC
            """
            _cmd = "ALC"
            
            class SETTings(SCPINode, SCPIQuery, SCPISet):
                """
                DIAGnostic:ALC:SETTings
                """
                _cmd = "SETTings"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:ALC:SETTings:STATe
                    """
                    _cmd = "STATe"
                    
        class DEFault(SCPINode, SCPIQuery, SCPISet):
            """
            DIAGnostic:DEFault
            """
            _cmd = "DEFault"
            
        class DEVice(SCPINode):
            """
            DIAGnostic:DEVice
            """
            _cmd = "DEVice"
            
            class STATe(SCPINode, SCPISet):
                """
                `DIAGnostic:DEVice:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e82077.htm#ID_4ccbc72a134d7a160a00206a00fc7723-c47502c8134d740b0a00206a0182dc26-en-US>`_
                """
                _cmd = "STATe"
                
        class DUMP(SCPINode):
            """
            DIAGnostic:DUMP
            """
            _cmd = "DUMP"
            
            class SIZE(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:DUMP:SIZE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ff494033e9a843aa.htm#ID_a7bac880066b4d220a001ae71bbc7e0d-90f2c5f2066b4b9b0a001ae733608be0-en-US>`_
                """
                _cmd = "SIZE"
                
        class PRODuct(SCPINode):
            """
            DIAGnostic:PRODuct
            """
            _cmd = "PRODuct"
            
            class CATalog(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:CATalog
                """
                _cmd = "CATalog"
                
            class DESCription(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:DESCription
                """
                _cmd = "DESCription"
                
            class ID(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:ID
                """
                _cmd = "ID"
                
            class MACaddress(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:MACaddress
                """
                _cmd = "MACaddress"
                
            class OPTion(SCPINode):
                """
                DIAGnostic:PRODuct:OPTion
                """
                _cmd = "OPTion"
                
                class FACTory(SCPINode):
                    """
                    DIAGnostic:PRODuct:OPTion:FACTory
                    """
                    _cmd = "FACTory"
                    
                    class CLEar(SCPINode, SCPISet):
                        """
                        DIAGnostic:PRODuct:OPTion:FACTory:CLEar
                        """
                        _cmd = "CLEar"
                        
                class INFO(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DIAGnostic:PRODuct:OPTion:INFO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0bab836e2f604f5e.htm#ID_5b4bc3d2a1e970ab0a001ae735fbde1d-a3143537a1e96f730a001ae70a9caa95-en-US>`_
                    """
                    _cmd = "INFO"
                    
                class LICence(SCPINode):
                    """
                    DIAGnostic:PRODuct:OPTion:LICence
                    """
                    _cmd = "LICence"
                    
                    class CHECk(SCPINode, SCPIQuery, SCPISet):
                        """
                        DIAGnostic:PRODuct:OPTion:LICence:CHECk
                        """
                        _cmd = "CHECk"
                        
                    class UNLock(SCPINode, SCPISet):
                        """
                        DIAGnostic:PRODuct:OPTion:LICence:UNLock
                        """
                        _cmd = "UNLock"
                        
                class LIST(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:PRODuct:OPTion:LIST
                    """
                    _cmd = "LIST"
                    
                class STATus(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:PRODuct:OPTion:STATus
                    """
                    _cmd = "STATus"
                    
            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                DIAGnostic:PRODuct:SELect
                """
                _cmd = "SELect"
                
            class TIME(SCPINode):
                """
                DIAGnostic:PRODuct:TIME
                """
                _cmd = "TIME"
                
                class OPERating(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:PRODuct:TIME:OPERating
                    """
                    _cmd = "OPERating"
                    
        class SERVice(SCPINode):
            """
            DIAGnostic:SERVice
            """
            _cmd = "SERVice"
            
            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:SERVice:FUNCtion
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e117662.htm#ID_351c4edbfa91942b0a00206a019938ad-c622f7b0fa918e7e0a00206a01a6673d-en-US>`_
                """
                _cmd = "FUNCtion"
                
            class RFPower(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:SERVice:RFPower
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e82164.htm#ID_05ffa5f6fa919bcc0a00206a006174c7-16a66f8cfa91960f0a00206a01a6673d-en-US>`_
                """
                _cmd = "RFPower"
                
            class SFUNction(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:SERVice:SFUNction
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f85cfd9d4d74448e.htm#ID_48fd1718fa91a33e0a00206a0034447a-4ce344b0fa919da10a00206a01a6673d-en-US>`_
                """
                _cmd = "SFUNction"
                
        class UPDate(SCPINode):
            """
            DIAGnostic:UPDate
            """
            _cmd = "UPDate"
            
            class BOOT(SCPINode, SCPISet):
                """
                DIAGnostic:UPDate:BOOT
                """
                _cmd = "BOOT"
                
            class CATalog(SCPINode, SCPIQuery):
                """
                DIAGnostic:UPDate:CATalog
                """
                _cmd = "CATalog"
                
            class CHAP(SCPINode):
                """
                DIAGnostic:UPDate:CHAP
                """
                _cmd = "CHAP"
                
                class CHALlenge(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:UPDate:CHAP:CHALlenge
                    """
                    _cmd = "CHALlenge"
                    
                class PRESet(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:CHAP:PRESet
                    """
                    _cmd = "PRESet"
                    
                class RESPonse(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:CHAP:RESPonse
                    """
                    _cmd = "RESPonse"
                    
            class EXECute(SCPINode, SCPISet):
                """
                DIAGnostic:UPDate:EXECute
                """
                _cmd = "EXECute"
                
            class INSTall(SCPINode, SCPISet):
                """
                DIAGnostic:UPDate:INSTall
                """
                _cmd = "INSTall"
                
                class BEGin(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:INSTall:BEGin
                    """
                    _cmd = "BEGin"
                    
                class END(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:INSTall:END
                    """
                    _cmd = "END"
                    
                class STATus(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:UPDate:INSTall:STATus
                    """
                    _cmd = "STATus"
                    
            class PROGress(SCPINode, SCPIQuery, SCPISet):
                """
                DIAGnostic:UPDate:PROGress
                """
                _cmd = "PROGress"
                
            class TRANsfer(SCPINode):
                """
                DIAGnostic:UPDate:TRANsfer
                """
                _cmd = "TRANsfer"
                
                class CLOSe(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:TRANsfer:CLOSe
                    """
                    _cmd = "CLOSe"
                    
                class DATA(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:TRANsfer:DATA
                    """
                    _cmd = "DATA"
                    
                class OPEN(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:TRANsfer:OPEN
                    """
                    _cmd = "OPEN"
                    
                class VERSion(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:UPDate:TRANsfer:VERSion
                    """
                    _cmd = "VERSion"
                    
    class DISPlay(SCPINode, SCPIQuery, SCPISet):
        """
        DISPlay
        """
        _cmd = "DISPlay"
        
        class ANNotation(SCPINode):
            """
            DISPlay:ANNotation
            """
            _cmd = "ANNotation"
            
            class CHANnel(SCPINode, SCPIQuery, SCPISet):
                """
                DISPlay:ANNotation:CHANnel
                """
                _cmd = "CHANnel"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:ANNotation:CHANnel:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/97b83eb36eea4b22.htm#ID_09283553fa921c940a00206a00bfb2e1-8c3c7511fa9216e70a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                """
                DISPlay:ANNotation:FREQuency
                """
                _cmd = "FREQuency"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:ANNotation:FREQuency:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a9752bf5700b4921.htm#ID_a0b6805dfa9224350a00206a01dcf415-e0bc5d8cfa921e880a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class TRACe(SCPINode, SCPIQuery, SCPISet):
                """
                DISPlay:ANNotation:TRACe
                """
                _cmd = "TRACe"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:ANNotation:TRACe:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/97b83eb36eea4b22.htm#ID_69d46e9ebba79eea0a002019006f313f-268f85a2bba79dc10a0020190170f726-en-US>`_
                    """
                    _cmd = "STATe"
                    
        class CMAP(SCPINodeN):
            """
            DISPlay:CMAP
            """
            _cmd = "CMAP"
            
            class LIMit(SCPINode, SCPIQuery, SCPISet):
                """
                DISPlay:CMAP:LIMit
                """
                _cmd = "LIMit"
                
                class FCOLorize(SCPINode, SCPIQuery, SCPISet):
                    """
                    DISPlay:CMAP:LIMit:FCOLorize
                    """
                    _cmd = "FCOLorize"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:CMAP:LIMit:FCOLorize:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e82450.htm#ID_07203f1f996b99230a00206a01fea816-cd8545fd996b91050a00206a0049ced2-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class FSYMbol(SCPINode, SCPIQuery, SCPISet):
                    """
                    DISPlay:CMAP:LIMit:FSYMbol
                    """
                    _cmd = "FSYMbol"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:CMAP:LIMit:FSYMbol:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e82482.htm#ID_a789ec67996ba7b90a00206a01775331-994b212d996b9e720a00206a0049ced2-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:CMAP:LIMit:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e82511.htm#ID_b72519cea06b7a720a00206a006d9d2b-2c0171cca06b736d0a00206a013722ca-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class MARKer(SCPINode, SCPIQuery, SCPISet):
                """
                DISPlay:CMAP:MARKer
                """
                _cmd = "MARKer"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:CMAP:MARKer:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e82561.htm#ID_e76ed6a7fa922c050a00206a00aef132-0ec64a50fa92261a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class RGB(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:CMAP:RGB
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/752a679d99444b26.htm#ID_f96e2125fa9233b60a00206a0101687a-9f550bd8fa922dea0a00206a01a6673d-en-US>`_
                """
                _cmd = "RGB"
                
            class TRACe(SCPINode):
                """
                DISPlay:CMAP:TRACe
                """
                _cmd = "TRACe"
                
                class COLor(SCPINode, SCPIQuery, SCPISet):
                    """
                    DISPlay:CMAP:TRACe:COLor
                    """
                    _cmd = "COLor"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:CMAP:TRACe:COLor:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e82877.htm#ID_96913623fa923b670a00206a01ee5bbf-923eb8ebfa9235aa0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class RGB(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:CMAP:TRACe:RGB
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e82925.htm#ID_71191c2cfa9243080a00206a015c1979-8ce5c12bfa923d4b0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "RGB"
                    
        class LAYout(SCPINode, SCPIQuery, SCPISet):
            """
            `DISPlay:LAYout
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/620d9d36a28c4ad0.htm#ID_42356ef6aaa7d54b0a00206a001cddae-8913c9f4aaa7cafb0a00206a00dee6b8-en-US>`_
            """
            _cmd = "LAYout"
            
            class APPLy(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:LAYout:APPLy
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5ec7955dbc1f4eea.htm#ID_d6f4fe84ced4d31c0a00201901c85cc7-1dabc1deced4d1c40a0020190170f726-en-US>`_
                """
                _cmd = "APPLy"
                
            class DEFine(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:LAYout:DEFine
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f39aa8b61fee48fd.htm#ID_4332cc0dbba7a40b0a0020190055a26c-111967f3bba7a2e20a0020190170f726-en-US>`_
                """
                _cmd = "DEFine"
                
            class EXECute(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:LAYout:EXECute
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ccb35e5e7c3b49fd.htm#ID_bd48f718bba7a5b10a002019009a678c-db3d473fbba7a4780a0020190170f726-en-US>`_
                """
                _cmd = "EXECute"
                
            class GRID(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:LAYout:GRID
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f0abcfab12584f77.htm#ID_70abfb19aaa7e2990a00206a01d81c00-a7770b8aaaa7d7cc0a00206a00dee6b8-en-US>`_
                """
                _cmd = "GRID"
                
            class JOIN(SCPINode, SCPISet):
                """
                `DISPlay:LAYout:JOIN
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/53c5effa46dc4646.htm#ID_000c4953bba7a7760a00201901e721c0-4109ca06bba7a65c0a0020190170f726-en-US>`_
                """
                _cmd = "JOIN"
                
        class MENU(SCPINode):
            """
            DISPlay:MENU
            """
            _cmd = "MENU"
            
            class KEY(SCPINode):
                """
                DISPlay:MENU:KEY
                """
                _cmd = "KEY"
                
                class EXECute(SCPINode, SCPISet):
                    """
                    `DISPlay:MENU:KEY:EXECute
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5f9d9a82fa7a43c5.htm#ID_3cfeb142fa924ac80a00206a01a8df15-3262509dfa9244ec0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "EXECute"
                    
                class SELect(SCPINode, SCPISet):
                    """
                    `DISPlay:MENU:KEY:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f6979f1d623948b8.htm#ID_2fd74a4efa92522b0a00206a00390f14-27eea583fa924c9d0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SELect"
                    
        class RFSize(SCPINode, SCPIQuery, SCPISet):
            """
            `DISPlay:RFSize
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e83626.htm#ID_26a7f2c7fa9259db0a00206a00f26a73-0ebe17bdfa9253ff0a00206a01a6673d-en-US>`_
            """
            _cmd = "RFSize"
            
        class WINDow(SCPINodeN, SCPIQuery, SCPISet):
            """
            DISPlay:WINDow
            """
            _cmd = "WINDow"
            
            class CATalog(SCPINode, SCPIQuery):
                """
                `DISPlay:WINDow:CATalog
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/abdd1db5dc0c48ee.htm#ID_84400b55fa92616d0a00206a006ce5e8-2bbb3a15fa925bb00a00206a01a6673d-en-US>`_
                """
                _cmd = "CATalog"
                
            class MAXimize(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:WINDow:MAXimize
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/99dca8ff187d4000.htm#ID_f3f24319fa9268ef0a00206a01e4b6e2-f727d921fa9263420a00206a01a6673d-en-US>`_
                """
                _cmd = "MAXimize"
                
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:WINDow:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2bf57f884ae84ed2.htm#ID_b9f0fbecfa9270de0a00206a00a45db7-1a416912fa926ad30a00206a01a6673d-en-US>`_
                """
                _cmd = "NAME"
                
            class OVERview(SCPINode, SCPIQuery, SCPISet):
                """
                DISPlay:WINDow:OVERview
                """
                _cmd = "OVERview"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:OVERview:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/33fe4a73a2ab4070.htm#ID_10fbd8f3ced4d87b0a00201901b68cc7-1d9f9891ced4d7230a0020190170f726-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:WINDow:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/065c895d5a2c4230.htm#ID_8e3cb1f5fa9278600a00206a01851f55-928f75e4fa9272b30a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
            class TITLe(SCPINode, SCPIQuery, SCPISet):
                """
                DISPlay:WINDow:TITLe
                """
                _cmd = "TITLe"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TITLe:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ac203fe8a5b647c2.htm#ID_0f9ac45ffa9280010a00206a00e0d734-11ac0202fa927a540a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DATA"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TITLe:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/30e7340225704fd9.htm#ID_c1d70c02fa9287a20a00206a009fab43-d77d2d0bfa9281f50a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class TRACe(SCPINodeN):
                """
                DISPlay:WINDow:TRACe
                """
                _cmd = "TRACe"
                
                class CATalog(SCPINode, SCPIQuery):
                    """
                    `DISPlay:WINDow:TRACe:CATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f6c8345f1d4348ad.htm#ID_906f0858fa928f340a00206a012e7faf-69a2c93cfa9289860a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CATalog"
                    
                class DELete(SCPINode, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:DELete
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/35e75331f5ce4fce.htm#ID_9bdc6b44fa9296c50a00206a00b068cd-6a447b3ffa9291280a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DELete"
                    
                class EFEed(SCPINode, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:EFEed
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a702a260a63d4a10.htm#ID_e3fa49acfa929e470a00206a01a34211-1ed47549fa9298a90a00206a01a6673d-en-US>`_
                    """
                    _cmd = "EFEed"
                    
                class FEED(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:FEED
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/58dad852e7db48a0.htm#ID_d87ac43bfa92a5f80a00206a01214a13-c23d3890fa92a02b0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "FEED"
                    
                class SHOW(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:SHOW
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/666cb4f2f8874259.htm#ID_e087b135fa92ad990a00206a0109416c-3de7dacafa92a7ec0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SHOW"
                    
                class X(SCPINode):
                    """
                    DISPlay:WINDow:TRACe:X
                    """
                    _cmd = "X"
                    
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:X:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1efcc8fa102b4b9b.htm#ID_eb26dfc0fa92b51b0a00206a00214931-20aba55afa92af6d0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "OFFSet"
                        
                class Y(SCPINode):
                    """
                    DISPlay:WINDow:TRACe:Y
                    """
                    _cmd = "Y"
                    
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:Y:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/fba6bb59b840434f.htm#ID_65233ce8fa92bcbc0a00206a0082ad31-db88fa1afa92b6ff0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "OFFSet"
                        
                    class SCALe(SCPINode):
                        """
                        DISPlay:WINDow:TRACe:Y:SCALe
                        """
                        _cmd = "SCALe"
                        
                        class AUTO(SCPINode, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:AUTO
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b1fbc2b484774b76.htm#ID_1feb2da3fa92c42e0a00206a01e047da-37730b41fa92bea00a00206a01a6673d-en-US>`_
                            """
                            _cmd = "AUTO"
                            
                        class BOTTom(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:BOTTom
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6331132d7bf24ded.htm#ID_8b51ec30fa92cbdf0a00206a0123a5f0-4e44393dfa92c6120a00206a01a6673d-en-US>`_
                            """
                            _cmd = "BOTTom"
                            
                        class PDIVision(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:PDIVision
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bdc5467b9ebd4d43.htm#ID_4c11fb55fa92d38f0a00206a000a08ea-2d92c4d5fa92cdd30a00206a01a6673d-en-US>`_
                            """
                            _cmd = "PDIVision"
                            
                        class RLEVel(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:RLEVel
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/65c5b3a27d46498f.htm#ID_21e8c0b9fa92db300a00206a01c11504-3791a074fa92d5740a00206a01a6673d-en-US>`_
                            """
                            _cmd = "RLEVel"
                            
                        class RPOSition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:RPOSition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ea8a750914d84285.htm#ID_1784a4a9fa92e2c20a00206a00192d65-a6fd3b12fa92dd150a00206a01a6673d-en-US>`_
                            """
                            _cmd = "RPOSition"
                            
                        class TOP(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:TOP
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6331132d7bf24ded.htm#ID_2e553fc3fa92ea630a00206a014ba5b8-4b3a4019fa92e4b60a00206a01a6673d-en-US>`_
                            """
                            _cmd = "TOP"
                            
                class ZOOM(SCPINode, SCPIQuery, SCPISet):
                    """
                    DISPlay:WINDow:TRACe:ZOOM
                    """
                    _cmd = "ZOOM"
                    
                    class BOTTom(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:ZOOM:BOTTom
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8f33192c7c374678.htm#ID_4c13e8946c07013b0a00206a005313ce-15625ccf6c06fa750a00206a01eade93-en-US>`_
                        """
                        _cmd = "BOTTom"
                        
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:ZOOM:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b2b9e703a45644b4.htm#ID_f621ce186c070a050a00206a00e386d0-b4028b3f6c0703bc0a00206a01eade93-en-US>`_
                        """
                        _cmd = "STARt"
                        
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:ZOOM:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/45c943218b544691.htm#ID_0801ee0a6c0728e80a00206a018f38c0-c5604fde6c0721180a00206a01eade93-en-US>`_
                        """
                        _cmd = "STATe"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:ZOOM:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b2b9e703a45644b4.htm#ID_3ce8f2656c0713d90a00206a010a19da-9ba5e7346c070cb50a00206a01eade93-en-US>`_
                        """
                        _cmd = "STOP"
                        
                    class TOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:ZOOM:TOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8f33192c7c374678.htm#ID_537535906c071e680a00206a01dff876-ecb2878b6c0716880a00206a01eade93-en-US>`_
                        """
                        _cmd = "TOP"
                        
    class FORMat(SCPINode, SCPIQuery, SCPISet):
        """
        FORMat
        """
        _cmd = "FORMat"
        
        class BORDer(SCPINode, SCPIQuery, SCPISet):
            """
            `FORMat:BORDer
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85486.htm#ID_3675bceefa92f1f40a00206a0080e1b0-61996525fa92ec470a00206a01a6673d-en-US>`_
            """
            _cmd = "BORDer"
            
        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `FORMat:DATA
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85516.htm#ID_42b1c1edfa9301c30a00206a005a835f-27d15adffa92fc260a00206a01a6673d-en-US>`_
            """
            _cmd = "DATA"
            
        class DEXPort(SCPINode):
            """
            FORMat:DEXPort
            """
            _cmd = "DEXPort"
            
            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `FORMat:DEXPort:SOURce
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a4122895a8614cd4.htm#ID_fc4eaae1fa92fa320a00206a008b9cce-81da4c17fa92f3d90a00206a01a6673d-en-US>`_
                """
                _cmd = "SOURce"
                
    class HCOPy(SCPINode, SCPISet):
        """
        HCOPy
        """
        _cmd = "HCOPy"
        
        class DESTination(SCPINode, SCPIQuery, SCPISet):
            """
            `HCOPy:DESTination
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85604.htm#ID_4d99c38afa9309840a00206a01d41aa4-cb1d3d15fa9303a80a00206a01a6673d-en-US>`_
            """
            _cmd = "DESTination"
            
        class DEVice(SCPINode):
            """
            HCOPy:DEVice
            """
            _cmd = "DEVice"
            
            class LANGuage(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:DEVice:LANGuage
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85657.htm#ID_bd2a6c37fa9311150a00206a01b42ce6-ccf29715fa930b680a00206a01a6673d-en-US>`_
                """
                _cmd = "LANGuage"
                
        class IMMediate(SCPINode, SCPISet):
            """
            `HCOPy:IMMediate
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86077.htm#ID_d21a6a5ffa9365110a00206a01870b2a-5d6c01cbfa935f640a00206a01a6673d-en-US>`_
            """
            _cmd = "IMMediate"
            
        class ITEM(SCPINode):
            """
            HCOPy:ITEM
            """
            _cmd = "ITEM"
            
            class ALL(SCPINode, SCPISet):
                """
                `HCOPy:ITEM:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85711.htm#ID_94da1e3bfa9318c60a00206a00ef3e34-3800e316fa9312ea0a00206a01a6673d-en-US>`_
                """
                _cmd = "ALL"
                
            class LOGO(SCPINode, SCPIQuery, SCPISet):
                """
                HCOPy:ITEM:LOGO
                """
                _cmd = "LOGO"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:ITEM:LOGO:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85742.htm#ID_ac9df7a7fa9320860a00206a00ec5c45-4c4a58fcfa931a9b0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class MLISt(SCPINode, SCPIQuery, SCPISet):
                """
                HCOPy:ITEM:MLISt
                """
                _cmd = "MLISt"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:ITEM:MLISt:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85780.htm#ID_854db6e1fa9328370a00206a01529a20-c066e67cfa93227a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                HCOPy:ITEM:TIME
                """
                _cmd = "TIME"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:ITEM:TIME:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85812.htm#ID_83e3f4d2fa932f9a0a00206a010f0f4e-404ea32bfa932a0c0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
        class PAGE(SCPINode):
            """
            HCOPy:PAGE
            """
            _cmd = "PAGE"
            
            class COLor(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:PAGE:COLor
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85844.htm#ID_5105d1a3134de2840a00206a0114a6f3-dca49ae8134ddcc80a00206a0182dc26-en-US>`_
                """
                _cmd = "COLor"
                
            class MARGin(SCPINode):
                """
                HCOPy:PAGE:MARGin
                """
                _cmd = "MARGin"
                
                class BOTTom(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:BOTTom
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85880.htm#ID_3dea753bfa93372b0a00206a01c0ca2d-3f62fe82fa93317e0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "BOTTom"
                    
                class LEFT(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:LEFT
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85911.htm#ID_8992c875fa933ebc0a00206a00922775-5c119a03fa93390f0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "LEFT"
                    
                class RIGHt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:RIGHt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85941.htm#ID_c7f0b442fa93465e0a00206a008d1d63-960d34d5fa9340b00a00206a01a6673d-en-US>`_
                    """
                    _cmd = "RIGHt"
                    
                class TOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:TOP
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e85971.htm#ID_6228e4b0fa934def0a00206a0086d622-cebe271bfa9348520a00206a01a6673d-en-US>`_
                    """
                    _cmd = "TOP"
                    
            class ORIentation(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:PAGE:ORIentation
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86001.htm#ID_f7b8f767fa9355a00a00206a00c03771-29a7b9bafa934fe30a00206a01a6673d-en-US>`_
                """
                _cmd = "ORIentation"
                
            class WINDow(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:PAGE:WINDow
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e7101f963f5c4de3.htm#ID_1c0c843ffa935d7f0a00206a015039a1-42f22e75fa9357840a00206a01a6673d-en-US>`_
                """
                _cmd = "WINDow"
                
    class INITiate(SCPINodeN, SCPISet):
        """
        INITiate
        """
        _cmd = "INITiate"
        
        class CONTinuous(SCPINode, SCPIQuery, SCPISet):
            """
            `INITiate:CONTinuous
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2529407b6dba4f2e.htm#ID_a44b9c33fa936d000a00206a00766e71-d44acbdafa9367050a00206a01a6673d-en-US>`_
            """
            _cmd = "CONTinuous"
            
            class ALL(SCPINode, SCPIQuery, SCPISet):
                """
                `INITiate:CONTinuous:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86196.htm#ID_6387403cd8d5523c0a00206a01023265-128b12f9d8d54b860a00206a0133a7b4-en-US>`_
                """
                _cmd = "ALL"
                
        class IMMediate(SCPINode, SCPISet):
            """
            INITiate:IMMediate
            """
            _cmd = "IMMediate"
            
            class ALL(SCPINode, SCPISet):
                """
                `INITiate:IMMediate:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86237.htm#ID_912c0160d8d55d770a00206a01491fbe-eddf9798d8d555d60a00206a0133a7b4-en-US>`_
                """
                _cmd = "ALL"
                
            class DUMMy(SCPINode, SCPISet):
                """
                `INITiate:IMMediate:DUMMy
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f79d0e51f1b440c9.htm#ID_8a697b81fa937c230a00206a01ed43fb-be0448b2fa9376660a00206a01a6673d-en-US>`_
                """
                _cmd = "DUMMy"
                
            class SCOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `INITiate:IMMediate:SCOPe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d961912528a64003.htm#ID_0b426df9fa9374820a00206a00380abe-581c1051fa936ef40a00206a01a6673d-en-US>`_
                """
                _cmd = "SCOPe"
                
    class INPut(SCPINodeN):
        """
        INPut
        """
        _cmd = "INPut"
        
        class ATTenuation(SCPINode, SCPIQuery, SCPISet):
            """
            `INPut:ATTenuation
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7f41ca301ecf4a76.htm#ID_cec36677fa9383e30a00206a01063b02-23f6f3d6fa937e070a00206a01a6673d-en-US>`_
            """
            _cmd = "ATTenuation"
            
    class INSTrument(SCPINode, SCPIQuery, SCPISet):
        """
        INSTrument
        """
        _cmd = "INSTrument"
        
        class NSELect(SCPINode, SCPIQuery, SCPISet):
            """
            `INSTrument:NSELect
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86400.htm#ID_078f22a7fa938ba40a00206a0072b3e0-af650a43fa9385d70a00206a01a6673d-en-US>`_
            """
            _cmd = "NSELect"
            
        class PORT(SCPINode):
            """
            INSTrument:PORT
            """
            _cmd = "PORT"
            
            class COUNt(SCPINode, SCPIQuery):
                """
                `INSTrument:PORT:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86437.htm#ID_9eb542a9fa9393a30a00206a01fd78a5-0f241535fa938d880a00206a01a6673d-en-US>`_
                """
                _cmd = "COUNt"
                
        class SELect(SCPINode, SCPIQuery, SCPISet):
            """
            `INSTrument:SELect
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e117852.htm#ID_49cfdf62fa939b440a00206a013fc5ae-d0c31584fa9395870a00206a01a6673d-en-US>`_
            """
            _cmd = "SELect"
            
        class SMATrix(SCPINode, SCPIQuery, SCPISet):
            """
            `INSTrument:SMATrix
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6cf81becf1d94292.htm#ID_c20108e4e2b32f990a002019011edfae-c2391792e2b32e510a002019017b841c-en-US>`_
            """
            _cmd = "SMATrix"
            
        class TPORt(SCPINode):
            """
            INSTrument:TPORt
            """
            _cmd = "TPORt"
            
            class COUNt(SCPINode, SCPIQuery):
                """
                `INSTrument:TPORt:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dffa886d18c44be6.htm#ID_a3c1b1d2e2b3316e0a00201901e88744-2e35c5e3e2b330060a002019017b841c-en-US>`_
                """
                _cmd = "COUNt"
                
    class MEMory(SCPINode):
        """
        MEMory
        """
        _cmd = "MEMory"
        
        class CATalog(SCPINode, SCPIQuery):
            """
            `MEMory:CATalog
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86522.htm#ID_952acba6fa93a2a60a00206a00158e32-18081993fa939d180a00206a01a6673d-en-US>`_
            """
            _cmd = "CATalog"
            
            class COUNt(SCPINode, SCPIQuery):
                """
                `MEMory:CATalog:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/24d4e6c36b6941d1.htm#ID_0562f2d34f2f3f8f0a001ae74fc3b6bb-a8d8bf024f2f3dd90a001ae7211c9327-en-US>`_
                """
                _cmd = "COUNt"
                
        class DEFine(SCPINode, SCPISet):
            """
            `MEMory:DEFine
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86562.htm#ID_061ba650fa93aa180a00206a00c6cfff-c04a3e9ffa93a48b0a00206a01a6673d-en-US>`_
            """
            _cmd = "DEFine"
            
        class DELete(SCPINode, SCPISet):
            """
            MEMory:DELete
            """
            _cmd = "DELete"
            
            class ALL(SCPINode, SCPISet):
                """
                `MEMory:DELete:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86592.htm#ID_35efca29fa93b18b0a00206a00349680-421059c6fa93abfd0a00206a01a6673d-en-US>`_
                """
                _cmd = "ALL"
                
            class NAME(SCPINode, SCPISet):
                """
                `MEMory:DELete:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86610.htm#ID_a4188fedfa93b8fd0a00206a007bbe38-13217951fa93b36f0a00206a01a6673d-en-US>`_
                """
                _cmd = "NAME"
                
        class SELect(SCPINode, SCPIQuery, SCPISet):
            """
            `MEMory:SELect
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6b5a13422595410a.htm#ID_346e954ffa93c0600a00206a00f12f17-1813a310fa93bae10a00206a01a6673d-en-US>`_
            """
            _cmd = "SELect"
            
    class MMEMory(SCPINode):
        """
        MMEMory
        """
        _cmd = "MMEMory"
        
        class AKAL(SCPINode):
            """
            MMEMory:AKAL
            """
            _cmd = "AKAL"
            
            class FACTory(SCPINode):
                """
                MMEMory:AKAL:FACTory
                """
                _cmd = "FACTory"
                
                class CONVersion(SCPINode, SCPISet):
                    """
                    `MMEMory:AKAL:FACTory:CONVersion
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86771.htm#ID_00f3bd41fa93c7f10a00206a01f83ace-1386d072fa93c2440a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CONVersion"
                    
            class USER(SCPINode):
                """
                MMEMory:AKAL:USER
                """
                _cmd = "USER"
                
                class CONVersion(SCPINode, SCPISet):
                    """
                    `MMEMory:AKAL:USER:CONVersion
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e86803.htm#ID_0bfad8be134e0c050a00206a0178239a-ada6c16a134e06490a00206a0182dc26-en-US>`_
                    """
                    _cmd = "CONVersion"
                    
        class CATalog(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:CATalog
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7f7650b75a604b3d.htm#ID_d67d6ebffa93cf820a00206a01a6fbab-84db8dd3fa93c9c60a00206a01a6673d-en-US>`_
            """
            _cmd = "CATalog"
            
            class ALL(SCPINode, SCPIQuery, SCPISet):
                """
                `MMEMory:CATalog:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/29a34569412140a3.htm#ID_6bb263ddfa93d6f50a00206a01b648d1-d7bba71dfa93d1670a00206a01a6673d-en-US>`_
                """
                _cmd = "ALL"
                
        class CDIRectory(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:CDIRectory
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e87010.htm#ID_a851e04afa93deb50a00206a01ba773c-866493dbfa93d8f80a00206a01a6673d-en-US>`_
            """
            _cmd = "CDIRectory"
            
        class CKIT(SCPINode):
            """
            MMEMory:CKIT
            """
            _cmd = "CKIT"
            
            class INFO(SCPINode, SCPIQuery, SCPISet):
                """
                `MMEMory:CKIT:INFO
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f05fc8cc8da8453b.htm#ID_977b912c842e29060a00201900b846e9-70e4c8b0842e27320a00201901936165-en-US>`_
                """
                _cmd = "INFO"
                
        class COPY(SCPINode, SCPISet):
            """
            `MMEMory:COPY
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e87048.htm#ID_5982002afa93e6270a00206a00a5825e-91ceacf0fa93e08a0a00206a01a6673d-en-US>`_
            """
            _cmd = "COPY"
            
        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:DATA
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e87156.htm#ID_b272d43dfa93eda90a00206a004c602f-6ae124d7fa93e80c0a00206a01a6673d-en-US>`_
            """
            _cmd = "DATA"
            
        class DELete(SCPINode, SCPISet):
            """
            `MMEMory:DELete
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e87202.htm#ID_4f6d0f68fa93f5690a00206a00977265-306d4498fa93efad0a00206a01a6673d-en-US>`_
            """
            _cmd = "DELete"
            
            class CORRection(SCPINode, SCPISet):
                """
                `MMEMory:DELete:CORRection
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e87249.htm#ID_f4141b0cfa93fceb0a00206a015c2d71-9c1f0333fa93f74e0a00206a01a6673d-en-US>`_
                """
                _cmd = "CORRection"
                
        class LOAD(SCPINode, SCPISet):
            """
            MMEMory:LOAD
            """
            _cmd = "LOAD"
            
            class CKIT(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:CKIT
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e87356.htm#ID_c78e3dc3fa940c6c0a00206a01f47c9b-d1fd8855fa9406a00a00206a01a6673d-en-US>`_
                """
                _cmd = "CKIT"
                
                class SDATa(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CKIT:SDATa
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4fe03fc744814dcd.htm#ID_c1f39b85fa9413de0a00206a01268a9f-3cd2e2d6fa940e410a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SDATa"
                    
                    class WLABel(SCPINode, SCPISet):
                        """
                        `MMEMory:LOAD:CKIT:SDATa:WLABel
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/765abd9f32e14000.htm#ID_05b1f69a066b76e20a001ae73aa0f2d0-7609eb53066b753c0a001ae733608be0-en-US>`_
                        """
                        _cmd = "WLABel"
                        
                class UDIRectory(SCPINode, SCPIQuery, SCPISet):
                    """
                    `MMEMory:LOAD:CKIT:UDIRectory
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e87692.htm#ID_3825c580fa941b7f0a00206a014d2f58-aa68faf7fa9415b30a00206a01a6673d-en-US>`_
                    """
                    _cmd = "UDIRectory"
                    
            class CMAP(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:CMAP
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e87750.htm#ID_351cf3d6fa9422f20a00206a018d97ca-e2d6eb23fa941d540a00206a01a6673d-en-US>`_
                """
                _cmd = "CMAP"
                
            class CORRection(SCPINode, SCPIQuery, SCPISet):
                """
                `MMEMory:LOAD:CORRection
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e87804.htm#ID_25d6c84ffa942a830a00206a0004052a-3d57daf0fa9424c60a00206a01a6673d-en-US>`_
                """
                _cmd = "CORRection"
                
                class MERGe(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:MERGe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4de4620d64e54bea.htm#ID_5fb89cc06c078fbf0a00206a00cc1f27-48b5ed616c0787820a00206a01eade93-en-US>`_
                    """
                    _cmd = "MERGe"
                    
                class RESolve(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:RESolve
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e87971.htm#ID_e782fc7bfa9431f50a00206a01e86316-b5f1ce83fa942c580a00206a01a6673d-en-US>`_
                    """
                    _cmd = "RESolve"
                    
                class TCOefficient(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:TCOefficient
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3391883fd0444077.htm#ID_160bbf146127a73d0a00206a0132199c-5dc6592961279f9c0a00206a01ed2866-en-US>`_
                    """
                    _cmd = "TCOefficient"
                    
            class LIMit(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:LIMit
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8105ab89421143c4.htm#ID_2de53f9cfa9439870a00206a01216055-e1a5d1b6fa9433da0a00206a01a6673d-en-US>`_
                """
                _cmd = "LIMit"
                
            class MDAData(SCPINode, SCPISet):
                """
                MMEMory:LOAD:MDAData
                """
                _cmd = "MDAData"
                
            class MDCData(SCPINode, SCPISet):
                """
                MMEMory:LOAD:MDCData
                """
                _cmd = "MDCData"
                
            class PTRain(SCPINode, SCPISet):
                """
                MMEMory:LOAD:PTRain
                """
                _cmd = "PTRain"
                
            class RIPPle(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:RIPPle
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e88268.htm#ID_53d05c7afa9457fc0a00206a0134102b-a6dd69cffa94523f0a00206a01a6673d-en-US>`_
                """
                _cmd = "RIPPle"
                
            class SEGMent(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:SEGMent
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e88327.htm#ID_1bff4bd6fa94bde90a00206a01c2ce76-065d4235fa94b7fd0a00206a01a6673d-en-US>`_
                """
                _cmd = "SEGMent"
                
            class STATe(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7dda8a2a220446bf.htm#ID_98d61c75fa94c54c0a00206a003ae40a-d3527128fa94bfcd0a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
            class TRACe(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:TRACe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e88437.htm#ID_71cd29a3fa94ccdd0a00206a00176ef8-c8a94a32fa94c7300a00206a01a6673d-en-US>`_
                """
                _cmd = "TRACe"
                
                class AUTO(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:TRACe:AUTO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/19157a43e4c140cf.htm#ID_1129c438581269d50a001ae77ff8a3b6-a64b95bd5812685e0a001ae75f9ff217-en-US>`_
                    """
                    _cmd = "AUTO"
                    
            class VNETworks(SCPINodeN):
                """
                MMEMory:LOAD:VNETworks
                """
                _cmd = "VNETworks"
                
                class BALanced(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:BALanced
                    """
                    _cmd = "BALanced"
                    
                    class DEEMbedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:BALanced:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/68d4179e5b9a4864.htm#ID_60f70d22fa94d4bd0a00206a01d5316a-546be1b0fa94ceb20a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DEEMbedding"
                        
                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:BALanced:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f6b1b692bb9b47c5.htm#ID_1fb5e13dfa94dc2f0a00206a017b5ae4-afca2f18fa94d6a10a00206a01a6673d-en-US>`_
                        """
                        _cmd = "EMBedding"
                        
                class DIFFerential(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:DIFFerential
                    """
                    _cmd = "DIFFerential"
                    
                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        MMEMory:LOAD:VNETworks:DIFFerential:EMBedding
                        """
                        _cmd = "EMBedding"
                        
                class GLOop(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:GLOop
                    """
                    _cmd = "GLOop"
                    
                    class DEEMbedding(SCPINode, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:GLOop:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b4a3d6fa5ec24c48.htm#ID_90df2d0efa94e3c00a00206a00b81c60-551f17abfa94de130a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DEEMbedding"
                        
                    class EMBedding(SCPINode, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:GLOop:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3d2e435406c14d5c.htm#ID_6cf57b55fa94eb520a00206a01f0b35d-3002adcbfa94e5a50a00206a01a6673d-en-US>`_
                        """
                        _cmd = "EMBedding"
                        
                class PPAir(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:PPAir
                    """
                    _cmd = "PPAir"
                    
                    class DEEMbedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:PPAir:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2cc34fe146bb4b3e.htm#ID_0d54645258126fb10a001ae7686ffa62-2155715958126e1a0a001ae75f9ff217-en-US>`_
                        """
                        _cmd = "DEEMbedding"
                        
                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:PPAir:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/806ed1787e384089.htm#ID_e33cac3b581272310a001ae769d4469b-f2244cfe5812709b0a001ae75f9ff217-en-US>`_
                        """
                        _cmd = "EMBedding"
                        
                class SENDed(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:SENDed
                    """
                    _cmd = "SENDed"
                    
                    class DEEMbedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:SENDed:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b4ab11f6c2d1486d.htm#ID_3dd89c63fa94f2d40a00206a00c9b7ad-74a2471cfa94ed360a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DEEMbedding"
                        
                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:SENDed:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/535bed379ed64bb9.htm#ID_b61e5784fa94fa360a00206a01c80b0f-f1e321c8fa94f4a80a00206a01a6673d-en-US>`_
                        """
                        _cmd = "EMBedding"
                        
        class MDIRectory(SCPINode, SCPISet):
            """
            `MMEMory:MDIRectory
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e89416.htm#ID_fd35f1fcfa9501b80a00206a0100c42b-88ece1edfa94fc0b0a00206a01a6673d-en-US>`_
            """
            _cmd = "MDIRectory"
            
        class MOVE(SCPINode, SCPISet):
            """
            `MMEMory:MOVE
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e89460.htm#ID_5a4f49b8fa95092a0a00206a01f9980a-904752d9fa95038d0a00206a01a6673d-en-US>`_
            """
            _cmd = "MOVE"
            
        class MSIS(SCPINode, SCPIQuery, SCPISet):
            """
            MMEMory:MSIS
            """
            _cmd = "MSIS"
            
        class NAME(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:NAME
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e89507.htm#ID_7ed3f8e1fa95183e0a00206a018c947f-39b72916fa9512810a00206a01a6673d-en-US>`_
            """
            _cmd = "NAME"
            
        class RDIRectory(SCPINode, SCPISet):
            """
            `MMEMory:RDIRectory
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e89574.htm#ID_13316b07fa951fdf0a00206a008fc1f6-bf8fd2b9fa951a220a00206a01a6673d-en-US>`_
            """
            _cmd = "RDIRectory"
            
        class STORe(SCPINode):
            """
            MMEMory:STORe
            """
            _cmd = "STORe"
            
            class CKIT(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CKIT
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e89600.htm#ID_539cfe2efa9527410a00206a01d2a4ac-dd207886fa9521b40a00206a01a6673d-en-US>`_
                """
                _cmd = "CKIT"
                
                class WLABel(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:CKIT:WLABel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/efd3c02d66084bdd.htm#ID_888d60aaced4f53a0a00201901d73653-9c37fbc3ced4f3a40a0020190170f726-en-US>`_
                    """
                    _cmd = "WLABel"
                    
            class CMAP(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CMAP
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e89713.htm#ID_cbd50bdafa952f400a00206a00ec799b-eab4a1d4fa9529260a00206a01a6673d-en-US>`_
                """
                _cmd = "CMAP"
                
            class CORRection(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CORRection
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e89750.htm#ID_c353e6ebfa9536b20a00206a01588c09-64171fb4fa9531150a00206a01a6673d-en-US>`_
                """
                _cmd = "CORRection"
                
                class TCOefficient(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:CORRection:TCOefficient
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e89802.htm#ID_9ae3f47f6127dd220a00206a00f0280f-08ed84676127d39c0a00206a01ed2866-en-US>`_
                    """
                    _cmd = "TCOefficient"
                    
            class LIMit(SCPINode, SCPISet):
                """
                `MMEMory:STORe:LIMit
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e89840.htm#ID_782b2ad6fa953e250a00206a019dc625-b89a0a63fa9538870a00206a01a6673d-en-US>`_
                """
                _cmd = "LIMit"
                
            class MARKer(SCPINode, SCPISet):
                """
                `MMEMory:STORe:MARKer
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f70a03bc15d4437f.htm#ID_3fc7f68bfa9545c60a00206a00581ca5-eb6af3e4fa9540090a00206a01a6673d-en-US>`_
                """
                _cmd = "MARKer"
                
            class MDCData(SCPINode, SCPISet):
                """
                MMEMory:STORe:MDCData
                """
                _cmd = "MDCData"
                
            class PTRain(SCPINode, SCPISet):
                """
                MMEMory:STORe:PTRain
                """
                _cmd = "PTRain"
                
            class RIPPle(SCPINode, SCPISet):
                """
                `MMEMory:STORe:RIPPle
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e89937.htm#ID_f13d0426fa955c6b0a00206a0012a7ed-6e6fe2c3fa9556bd0a00206a01a6673d-en-US>`_
                """
                _cmd = "RIPPle"
                
            class SEGMent(SCPINode, SCPISet):
                """
                `MMEMory:STORe:SEGMent
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e89985.htm#ID_de67ac75fa95640c0a00206a0143d61b-7b9796ebfa955e3f0a00206a01a6673d-en-US>`_
                """
                _cmd = "SEGMent"
                
            class STATe(SCPINode, SCPISet):
                """
                `MMEMory:STORe:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5052a11828174526.htm#ID_905ac710fa956bad0a00206a0007bfeb-0c7b3364fa9566000a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
            class TRACe(SCPINode, SCPISet):
                """
                `MMEMory:STORe:TRACe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a65bbed6ba0147dc.htm#ID_4cefccb1fa95732f0a00206a000ff211-d0689586fa956d820a00206a01a6673d-en-US>`_
                """
                _cmd = "TRACe"
                
                class CHANnel(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:TRACe:CHANnel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e90223.htm#ID_5e3f64c9fa957aa10a00206a0151de90-1d6679b9fa9575030a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CHANnel"
                    
                class OPTion(SCPINode):
                    """
                    MMEMory:STORe:TRACe:OPTion
                    """
                    _cmd = "OPTion"
                    
                    class PLUS(SCPINode, SCPIQuery, SCPISet):
                        """
                        `MMEMory:STORe:TRACe:OPTion:PLUS
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ff40aa0133194ed1.htm#ID_b9900453a1e9a3150a001ae76280abec-a8ea7a81a1e9a1be0a001ae70a9caa95-en-US>`_
                        """
                        _cmd = "PLUS"
                        
                    class SSEParator(SCPINode, SCPIQuery, SCPISet):
                        """
                        `MMEMory:STORe:TRACe:OPTion:SSEParator
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a565459101494c2b.htm#ID_5f64ab6ca1e9a4bb0a001ae77a2699fa-13ddc4d6a1e9a3920a001ae70a9caa95-en-US>`_
                        """
                        _cmd = "SSEParator"
                        
                    class TABS(SCPINode, SCPIQuery, SCPISet):
                        """
                        `MMEMory:STORe:TRACe:OPTion:TABS
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cc452c005766424d.htm#ID_fd30ef37a1e9a6710a001ae756b484ff-1daf23f2a1e9a5480a001ae70a9caa95-en-US>`_
                        """
                        _cmd = "TABS"
                        
                    class TRIM(SCPINode, SCPIQuery, SCPISet):
                        """
                        `MMEMory:STORe:TRACe:OPTion:TRIM
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/83a697c6e4ad47f1.htm#ID_6b425a6ba1e9a8170a001ae778e72705-0e2fc535a1e9a6ee0a001ae70a9caa95-en-US>`_
                        """
                        _cmd = "TRIM"
                        
                class PORTs(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:TRACe:PORTs
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bf349758d8b24668.htm#ID_39dd05bffa9582320a00206a01a97190-b9b34189fa957c850a00206a01a6673d-en-US>`_
                    """
                    _cmd = "PORTs"
                    
    class OUTPut(SCPINodeN, SCPIQuery, SCPISet):
        """
        OUTPut
        """
        _cmd = "OUTPut"
        
        class DPORt(SCPINode, SCPIQuery, SCPISet):
            """
            `OUTPut:DPORt
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0c0cec1ef82643e1.htm#ID_917ab5bffa95a7bc0a00206a01b0fd26-0934dcfcfa95a1ff0a00206a01a6673d-en-US>`_
            """
            _cmd = "DPORt"
            
        class STATe(SCPINode, SCPIQuery, SCPISet):
            """
            `OUTPut:STATe
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5bef3747737e49a1.htm#ID_1d3950befa95a01a0a00206a004f6799-85cf6e20fa959a7d0a00206a01a6673d-en-US>`_
            """
            _cmd = "STATe"
            
        class UPORt(SCPINode, SCPIQuery):
            """
            OUTPut:UPORt
            """
            _cmd = "UPORt"
            
            class ECBits(SCPINode, SCPIQuery, SCPISet):
                """
                `OUTPut:UPORt:ECBits
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e90615.htm#ID_954978c2134e5c960a00206a00bd7009-5e1d0c11134e56e90a00206a0182dc26-en-US>`_
                """
                _cmd = "ECBits"
                
            class SEGMent(SCPINodeN, SCPIQuery):
                """
                OUTPut:UPORt:SEGMent
                """
                _cmd = "SEGMent"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    OUTPut:UPORt:SEGMent:STATe
                    """
                    _cmd = "STATe"
                    
                class VALue(SCPINode, SCPIQuery):
                    """
                    OUTPut:UPORt:SEGMent:VALue
                    """
                    _cmd = "VALue"
                    
            class VALue(SCPINode, SCPIQuery):
                """
                `OUTPut:UPORt:VALue
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e1e93d03a7df427c.htm#ID_135223a3fa9598a80a00206a01cafb20-52630dd2fa95931a0a00206a01a6673d-en-US>`_
                """
                _cmd = "VALue"
                
    class PROGram(SCPINode):
        """
        PROGram
        """
        _cmd = "PROGram"
        
        class SELected(SCPINode):
            """
            PROGram:SELected
            """
            _cmd = "SELected"
            
            class EXECute(SCPINode, SCPISet):
                """
                `PROGram:SELected:EXECute
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/392c9cb1d1974b06.htm#ID_189c3c21fa95b6ee0a00206a00783ab2-c1c63606fa95b1310a00206a01a6673d-en-US>`_
                """
                _cmd = "EXECute"
                
            class INIMessage(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:INIMessage
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e90967.htm#ID_40e3620ffa95bfa80a00206a008f8ff5-31d51170fa95ba0b0a00206a01a6673d-en-US>`_
                """
                _cmd = "INIMessage"
                
            class INIParameter(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:INIParameter
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e91083.htm#ID_7a6b9636fa95c73a0a00206a00d1a901-d14937334d3699ed0a00206a01f0cf39-en-US>`_
                """
                _cmd = "INIParameter"
                
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e90777.htm#ID_c54cbe36fa95cebc0a00206a00f8e5b9-e2ad44defa95c91e0a00206a01a6673d-en-US>`_
                """
                _cmd = "NAME"
                
            class RETVal(SCPINode, SCPIQuery):
                """
                `PROGram:SELected:RETVal
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/02fc3f1a6eaf42d6.htm#ID_94731fde6f66e3560a001ae73692d158-f209efbd6f66e1b00a001ae727f5f310-en-US>`_
                """
                _cmd = "RETVal"
                
            class WAIT(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:WAIT
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/82b54e96d1e44f4f.htm#ID_6029b303fa95de0e0a00206a01d08fa1-a92a19e1fa95d8410a00206a01a6673d-en-US>`_
                """
                _cmd = "WAIT"
                
    class SENSe(SCPINodeN):
        """
        SENSe
        """
        _cmd = "SENSe"
        
        class AVERage(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:AVERage
            """
            _cmd = "AVERage"
            
            class CLEar(SCPINode, SCPISet):
                """
                `SENSe:AVERage:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ff10e010f00d4b14.htm#ID_f98b8f87fa95f4f10a00206a01537005-1a87cdf1fa95ef340a00206a01a6673d-en-US>`_
                """
                _cmd = "CLEar"
                
            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:AVERage:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5f171177edec4acc.htm#ID_60175c19fa95fc920a00206a018e0d61-0ec39e5bfa95f6d50a00206a01a6673d-en-US>`_
                """
                _cmd = "COUNt"
                
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:AVERage:MODE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b22adeaf572d4a3a.htm#ID_bb3fe278aaa7f2390a00206a00c5463f-a0adc45baaa7e6240a00206a00dee6b8-en-US>`_
                """
                _cmd = "MODE"
                
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:AVERage:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f2c90c7855f6416e.htm#ID_befa63f5fa9604240a00206a019d1b7a-b4429b00fa95fe760a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
        class BANDwidth(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:BANDwidth
            """
            _cmd = "BANDwidth"
            
            class RESolution(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:BANDwidth:RESolution
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dd1fd694e0ce4dd8.htm#ID_97a679d7fa960b960a00206a00572e56-c5d81c23fa9606080a00206a01a6673d-en-US>`_
                """
                _cmd = "RESolution"
                
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:BANDwidth:RESolution:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5bf234a092e54a5c.htm#ID_ac511438fa9613080a00206a00a13823-54b75391fa960d6a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SELect"
                    
        class BWIDth(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:BWIDth
            """
            _cmd = "BWIDth"
            
            class RESolution(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:BWIDth:RESolution
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dd1fd694e0ce4dd8.htm#ID_3a4684e0fa961ad80a00206a013fb6ed-0a999090fa9614ec0a00206a01a6673d-en-US>`_
                """
                _cmd = "RESolution"
                
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:BWIDth:RESolution:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5bf234a092e54a5c.htm#ID_ba204243fa96223b0a00206a007de2b3-d020815dfa961cad0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SELect"
                    
        class CORRection(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:CORRection
            """
            _cmd = "CORRection"
            
            class CDATa(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:CDATa
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/56c4604324f74fdd.htm#ID_61872ddefa962a0b0a00206a00f647f7-3f3fd3eafa96245d0a00206a01a6673d-en-US>`_
                """
                _cmd = "CDATa"
                
                class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CDATa:CATalog
                    """
                    _cmd = "CATalog"
                    
                class PORT(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CDATa:PORT
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/56c4604324f74fdd.htm#ID_1d57879f3512ffaa0a00206a00fd361c-e90129e83512f8570a00206a01f2dc17-en-US>`_
                    """
                    _cmd = "PORT"
                    
                    class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CDATa:PORT:CATalog
                        """
                        _cmd = "CATalog"
                        
            class CKIT(SCPINode):
                """
                SENSe:CORRection:CKIT
                """
                _cmd = "CKIT"
                
                class CATalog(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:CATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/20ee7245586f47ab.htm#ID_275e8b37fa96319c0a00206a00b96b39-8b99fd8cfa962bef0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CATalog"
                    
                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:DELete
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e92571.htm#ID_d581a0a8fa96390e0a00206a0093c656-0318d330fa9633710a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DELete"
                    
                class DMODe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:DMODe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b0b16acb033e4002.htm#ID_3d0e560697e8eb360a001ae7274e8676-670d0e8997e8e99f0a001ae760f7f904-en-US>`_
                    """
                    _cmd = "DMODe"
                    
                class FFATten(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFATten
                    """
                    _cmd = "FFATten"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFATten:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FFATten:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFLine
                    """
                    _cmd = "FFLine"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFLine:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FFLine:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFSNetwork
                    """
                    _cmd = "FFSNetwork"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFSNetwork:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FFSNetwork:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFTHrough
                    """
                    _cmd = "FFTHrough"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFTHrough:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FFTHrough:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class FMTCh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FMTCh
                    """
                    _cmd = "FMTCh"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FMTCh:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FMTCh:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class FOPen(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FOPen
                    """
                    _cmd = "FOPen"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FOPen:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FOPen:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class FOSHort(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FOSHort
                    """
                    _cmd = "FOSHort"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FOSHort:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FOSHort:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class FREFlect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FREFlect
                    """
                    _cmd = "FREFlect"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FREFlect:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FREFlect:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class FSHort(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FSHort
                    """
                    _cmd = "FSHort"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FSHort:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FSHort:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class FSMatch(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FSMatch
                    """
                    _cmd = "FSMatch"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FSMatch:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FSMatch:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class INSTall(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:INSTall
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e118084.htm#ID_0d28ed7afa968ceb0a00206a00c14d10-2f7f204bfa96872e0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "INSTall"
                    
                class LABel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LABel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/468d3061fddc4522.htm#ID_a949aef5fa96949b0a00206a008cfdb4-08f09b7dfa968ecf0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "LABel"
                    
                class LCATalog(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LCATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6e82c490f7f24b6b.htm#ID_bd9285fcced51a760a0020190106d279-9543f45cced5191e0a0020190170f726-en-US>`_
                    """
                    _cmd = "LCATalog"
                    
                class LDELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LDELete
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e95eefb5eb454112.htm#ID_8cfb4403ced51c5a0a002019000160a1-3112cb6eced51af30a0020190170f726-en-US>`_
                    """
                    _cmd = "LDELete"
                    
                class LLABel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LLABel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/436dc8aef9bf4100.htm#ID_4ee989a8ced51e2f0a00201900885604-edc77a82ced51ce70a0020190170f726-en-US>`_
                    """
                    _cmd = "LLABel"
                    
                class LSELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LSELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/538cff17731d484f.htm#ID_16b73472ced51fe50a002019002e86ba-dbeec92aced51eac0a0020190170f726-en-US>`_
                    """
                    _cmd = "LSELect"
                    
                class MFATten(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFATten
                    """
                    _cmd = "MFATten"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFATten:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MFATten:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFLine
                    """
                    _cmd = "MFLine"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFLine:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MFLine:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFSNetwork
                    """
                    _cmd = "MFSNetwork"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFSNetwork:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MFSNetwork:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFTHrough
                    """
                    _cmd = "MFTHrough"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFTHrough:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MFTHrough:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MMATten(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMATten
                    """
                    _cmd = "MMATten"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMATten:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MMATten:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMLine
                    """
                    _cmd = "MMLine"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMLine:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MMLine:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMSNetwork
                    """
                    _cmd = "MMSNetwork"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMSNetwork:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MMSNetwork:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MMTCh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMTCh
                    """
                    _cmd = "MMTCh"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMTCh:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MMTCh:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMTHrough
                    """
                    _cmd = "MMTHrough"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMTHrough:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MMTHrough:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MOPen(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MOPen
                    """
                    _cmd = "MOPen"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MOPen:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MOPen:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MOSHort(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MOSHort
                    """
                    _cmd = "MOSHort"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MOSHort:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MOSHort:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MREFlect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MREFlect
                    """
                    _cmd = "MREFlect"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MREFlect:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MREFlect:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MSHort(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MSHort
                    """
                    _cmd = "MSHort"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MSHort:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MSHort:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class MSMatch(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MSMatch
                    """
                    _cmd = "MSMatch"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MSMatch:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MSMatch:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class N(SCPINodeN):
                    """
                    SENSe:CORRection:CKIT:N
                    """
                    _cmd = "N"
                    
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFATten
                        """
                        _cmd = "FFATten"
                        
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFLine
                        """
                        _cmd = "FFLine"
                        
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFSNetwork
                        """
                        _cmd = "FFSNetwork"
                        
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFTHrough
                        """
                        _cmd = "FFTHrough"
                        
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FMTCh
                        """
                        _cmd = "FMTCh"
                        
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FOPen
                        """
                        _cmd = "FOPen"
                        
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FREFlect
                        """
                        _cmd = "FREFlect"
                        
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FSHort
                        """
                        _cmd = "FSHort"
                        
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FSMatch
                        """
                        _cmd = "FSMatch"
                        
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:LSELect
                        """
                        _cmd = "LSELect"
                        
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFATten
                        """
                        _cmd = "MFATten"
                        
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFLine
                        """
                        _cmd = "MFLine"
                        
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFSNetwork
                        """
                        _cmd = "MFSNetwork"
                        
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFTHrough
                        """
                        _cmd = "MFTHrough"
                        
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMATten
                        """
                        _cmd = "MMATten"
                        
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMLine
                        """
                        _cmd = "MMLine"
                        
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMSNetwork
                        """
                        _cmd = "MMSNetwork"
                        
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMTCh
                        """
                        _cmd = "MMTCh"
                        
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMTHrough
                        """
                        _cmd = "MMTHrough"
                        
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MOPen
                        """
                        _cmd = "MOPen"
                        
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MREFlect
                        """
                        _cmd = "MREFlect"
                        
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MSHort
                        """
                        _cmd = "MSHort"
                        
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MSMatch
                        """
                        _cmd = "MSMatch"
                        
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:SELect
                        """
                        _cmd = "SELect"
                        
                class OSHort(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:OSHort
                    """
                    _cmd = "OSHort"
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:OSHort:WLABel
                        """
                        _cmd = "WLABel"
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:OSHort:WLABel:SDATa
                            """
                            _cmd = "SDATa"
                            
                class PC(SCPINodeN):
                    """
                    SENSe:CORRection:CKIT:PC
                    """
                    _cmd = "PC"
                    
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFATten
                        """
                        _cmd = "FFATten"
                        
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFLine
                        """
                        _cmd = "FFLine"
                        
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFSNetwork
                        """
                        _cmd = "FFSNetwork"
                        
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFTHrough
                        """
                        _cmd = "FFTHrough"
                        
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FMTCh
                        """
                        _cmd = "FMTCh"
                        
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FOPen
                        """
                        _cmd = "FOPen"
                        
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FREFlect
                        """
                        _cmd = "FREFlect"
                        
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FSHort
                        """
                        _cmd = "FSHort"
                        
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FSMatch
                        """
                        _cmd = "FSMatch"
                        
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:LSELect
                        """
                        _cmd = "LSELect"
                        
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFATten
                        """
                        _cmd = "MFATten"
                        
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFLine
                        """
                        _cmd = "MFLine"
                        
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFSNetwork
                        """
                        _cmd = "MFSNetwork"
                        
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFTHrough
                        """
                        _cmd = "MFTHrough"
                        
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMATten
                        """
                        _cmd = "MMATten"
                        
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMLine
                        """
                        _cmd = "MMLine"
                        
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMSNetwork
                        """
                        _cmd = "MMSNetwork"
                        
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMTCh
                        """
                        _cmd = "MMTCh"
                        
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMTHrough
                        """
                        _cmd = "MMTHrough"
                        
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MOPen
                        """
                        _cmd = "MOPen"
                        
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MREFlect
                        """
                        _cmd = "MREFlect"
                        
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MSHort
                        """
                        _cmd = "MSHort"
                        
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MSMatch
                        """
                        _cmd = "MSMatch"
                        
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:SELect
                        """
                        _cmd = "SELect"
                        
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e92820.htm#ID_b65e4b76fa9a70630a00206a0107a5c6-69af0339fa9a6aa60a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SELect"
                    
                class SMA(SCPINode):
                    """
                    SENSe:CORRection:CKIT:SMA
                    """
                    _cmd = "SMA"
                    
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFATten
                        """
                        _cmd = "FFATten"
                        
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFLine
                        """
                        _cmd = "FFLine"
                        
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFSNetwork
                        """
                        _cmd = "FFSNetwork"
                        
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFTHrough
                        """
                        _cmd = "FFTHrough"
                        
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FMTCh
                        """
                        _cmd = "FMTCh"
                        
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FOPen
                        """
                        _cmd = "FOPen"
                        
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FREFlect
                        """
                        _cmd = "FREFlect"
                        
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FSHort
                        """
                        _cmd = "FSHort"
                        
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FSMatch
                        """
                        _cmd = "FSMatch"
                        
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:LSELect
                        """
                        _cmd = "LSELect"
                        
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFATten
                        """
                        _cmd = "MFATten"
                        
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFLine
                        """
                        _cmd = "MFLine"
                        
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFSNetwork
                        """
                        _cmd = "MFSNetwork"
                        
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFTHrough
                        """
                        _cmd = "MFTHrough"
                        
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMATten
                        """
                        _cmd = "MMATten"
                        
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMLine
                        """
                        _cmd = "MMLine"
                        
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMSNetwork
                        """
                        _cmd = "MMSNetwork"
                        
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMTCh
                        """
                        _cmd = "MMTCh"
                        
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMTHrough
                        """
                        _cmd = "MMTHrough"
                        
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MOPen
                        """
                        _cmd = "MOPen"
                        
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MREFlect
                        """
                        _cmd = "MREFlect"
                        
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MSHort
                        """
                        _cmd = "MSHort"
                        
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MSMatch
                        """
                        _cmd = "MSMatch"
                        
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:SELect
                        """
                        _cmd = "SELect"
                        
                class STANdard(SCPINode):
                    """
                    SENSe:CORRection:CKIT:STANdard
                    """
                    _cmd = "STANdard"
                    
                    class CATalog(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:CKIT:STANdard:CATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/173aa73feb9f4da4.htm#ID_0c560487fa9b35f50a00206a018f09d5-04e887fdfa9b2fab0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "CATalog"
                        
                    class DATA(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:CKIT:STANdard:DATA
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6ed615a6cfde42d5.htm#ID_f9688ab997e995bf0a001ae742db5fd2-d35c0fa897e994970a001ae760f7f904-en-US>`_
                        """
                        _cmd = "DATA"
                        
                    class LCATalog(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:CKIT:STANdard:LCATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3c29f476a1cb4a51.htm#ID_ef4a7ad2ced55c710a0020190114b7a4-6db5736aced55b390a0020190170f726-en-US>`_
                        """
                        _cmd = "LCATalog"
                        
                class USER(SCPINodeN):
                    """
                    SENSe:CORRection:CKIT:USER
                    """
                    _cmd = "USER"
                    
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFATten
                        """
                        _cmd = "FFATten"
                        
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFLine
                        """
                        _cmd = "FFLine"
                        
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFSNetwork
                        """
                        _cmd = "FFSNetwork"
                        
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFTHrough
                        """
                        _cmd = "FFTHrough"
                        
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FMTCh
                        """
                        _cmd = "FMTCh"
                        
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FOPen
                        """
                        _cmd = "FOPen"
                        
                    class FOSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FOSHort
                        """
                        _cmd = "FOSHort"
                        
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FREFlect
                        """
                        _cmd = "FREFlect"
                        
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FSHort
                        """
                        _cmd = "FSHort"
                        
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FSMatch
                        """
                        _cmd = "FSMatch"
                        
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:LSELect
                        """
                        _cmd = "LSELect"
                        
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFATten
                        """
                        _cmd = "MFATten"
                        
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFLine
                        """
                        _cmd = "MFLine"
                        
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFSNetwork
                        """
                        _cmd = "MFSNetwork"
                        
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFTHrough
                        """
                        _cmd = "MFTHrough"
                        
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMATten
                        """
                        _cmd = "MMATten"
                        
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMLine
                        """
                        _cmd = "MMLine"
                        
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMSNetwork
                        """
                        _cmd = "MMSNetwork"
                        
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMTCh
                        """
                        _cmd = "MMTCh"
                        
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMTHrough
                        """
                        _cmd = "MMTHrough"
                        
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MOPen
                        """
                        _cmd = "MOPen"
                        
                    class MOSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MOSHort
                        """
                        _cmd = "MOSHort"
                        
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MREFlect
                        """
                        _cmd = "MREFlect"
                        
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MSHort
                        """
                        _cmd = "MSHort"
                        
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MSMatch
                        """
                        _cmd = "MSMatch"
                        
                    class OSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:OSHort
                        """
                        _cmd = "OSHort"
                        
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:SELect
                        """
                        _cmd = "SELect"
                        
            class COLLect(SCPINode, SCPISet):
                """
                SENSe:CORRection:COLLect
                """
                _cmd = "COLLect"
                
                class ACQuire(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5bae4485a66a4fdb.htm#ID_ef5ce226fa9d34b10a00206a00b1eeba-d8380b43fa9d2ed50a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ACQuire"
                    
                    class RSAVe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:COLLect:ACQuire:RSAVe
                        """
                        _cmd = "RSAVe"
                        
                        class DEFault(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:COLLect:ACQuire:RSAVe:DEFault
                            """
                            _cmd = "DEFault"
                            
                    class SELected(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:ACQuire:SELected
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c6919bbe1b864cae.htm#ID_c00a21defa9d4bc30a00206a0122a8dd-5adea6c9fa9d46260a00206a01a6673d-en-US>`_
                        """
                        _cmd = "SELected"
                        
                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:AUTO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3f0c418e57de4397.htm#ID_cc386375fa9c629c0a00206a00bdf63e-10769a8bfa9c5cd00a00206a01a6673d-en-US>`_
                    """
                    _cmd = "AUTO"
                    
                    class ASSignment(SCPINodeN):
                        """
                        SENSe:CORRection:COLLect:AUTO:ASSignment
                        """
                        _cmd = "ASSignment"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:ASSignment:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c1af194ea15e4e74.htm#ID_5df4176ee2b44c640a002019017f4ab1-12b12dc3e2b44b0c0a002019017b841c-en-US>`_
                            """
                            _cmd = "ACQuire"
                            
                        class ALL(SCPINode):
                            """
                            SENSe:CORRection:COLLect:AUTO:ASSignment:ALL
                            """
                            _cmd = "ALL"
                            
                            class COUNt(SCPINode, SCPIQuery):
                                """
                                `SENSe:CORRection:COLLect:AUTO:ASSignment:ALL:COUNt
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d48b52bc242b4e32.htm#ID_959263675de614120a002019017e262e-dd26319f5de612c90a0020190152315a-en-US>`_
                                """
                                _cmd = "COUNt"
                                
                        class COUNt(SCPINode, SCPIQuery):
                            """
                            `SENSe:CORRection:COLLect:AUTO:ASSignment:COUNt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/18fc2beb38824da2.htm#ID_741269fee2b44e580a0020190035a217-8ce9a3a7e2b44d000a002019017b841c-en-US>`_
                            """
                            _cmd = "COUNt"
                            
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:ASSignment:DEFine
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0b4c577ed7c44274.htm#ID_a4e0bf56e2b4504c0a002019012145a1-ee4aa62fe2b44ee40a002019017b841c-en-US>`_
                            """
                            _cmd = "DEFine"
                            
                            class DEFault(SCPINode, SCPISet):
                                """
                                `SENSe:CORRection:COLLect:AUTO:ASSignment:DEFine:DEFault
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/64618e3b6c8a48f8.htm#ID_1806c3a7e2b452ec0a002019013da53d-5bf3d390e2b450e80a002019017b841c-en-US>`_
                                """
                                _cmd = "DEFault"
                                
                            class TPORt(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:CORRection:COLLect:AUTO:ASSignment:DEFine:TPORt
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5e83b118ba4a4af5.htm#ID_fefffc76ac615e840a00201901f142c0-e2627403ac615d3c0a0020190003471b-en-US>`_
                                """
                                _cmd = "TPORt"
                                
                                class DEFault(SCPINode, SCPISet):
                                    """
                                    `SENSe:CORRection:COLLect:AUTO:ASSignment:DEFine:TPORt:DEFault
                                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ffe7ec78e06d46ea.htm#ID_31e7cb915de618860a002019010fd717-b75dbe175de6175d0a0020190152315a-en-US>`_
                                    """
                                    _cmd = "DEFault"
                                    
                        class DELete(SCPINode):
                            """
                            SENSe:CORRection:COLLect:AUTO:ASSignment:DELete
                            """
                            _cmd = "DELete"
                            
                            class ALL(SCPINode, SCPISet):
                                """
                                `SENSe:CORRection:COLLect:AUTO:ASSignment:DELete:ALL
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/39cbade56c074b32.htm#ID_f5aac7e8e2b4559b0a00201901c4483e-40720b28e2b453970a002019017b841c-en-US>`_
                                """
                                _cmd = "ALL"
                                
                    class CKIT(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:CKIT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9c183d7ea83443b9.htm#ID_53832a46fa9c6a2e0a00206a01a37c63-f7039c7cfa9c64810a00206a01a6673d-en-US>`_
                        """
                        _cmd = "CKIT"
                        
                        class PASSword(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:CKIT:PASSword
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e94514.htm#ID_2a769be13f255d480a00206a00c9e150-22af427d3f2551130a00206a01f2dc17-en-US>`_
                            """
                            _cmd = "PASSword"
                            
                        class PORTs(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:CKIT:PORTs
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/abf506d433e74aa3.htm#ID_f432d1b6e2b458890a00201900df2894-0415557ee2b456f30a002019017b841c-en-US>`_
                            """
                            _cmd = "PORTs"
                            
                            class ADD(SCPINode, SCPISet):
                                """
                                `SENSe:CORRection:COLLect:AUTO:CKIT:PORTs:ADD
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d3fbc9d3f8b54fa6.htm#ID_22e73eec5de61b450a002019006fdae0-c43eb67b5de61a0d0a0020190152315a-en-US>`_
                                """
                                _cmd = "ADD"
                                
                    class CONFigure(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:CONFigure
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/43d940fc71ac4b9e.htm#ID_ec747919e2b45a4e0a00201900e617f8-1282c43ae2b458e70a002019017b841c-en-US>`_
                        """
                        _cmd = "CONFigure"
                        
                    class PORTs(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:PORTs
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/50bac54fa7384143.htm#ID_3691cfa7fa9c71cf0a00206a0106bbfe-1e1e838afa9c6c220a00206a01a6673d-en-US>`_
                        """
                        _cmd = "PORTs"
                        
                        class CONNection(SCPINode, SCPIQuery):
                            """
                            `SENSe:CORRection:COLLect:AUTO:PORTs:CONNection
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e94834.htm#ID_aaa87597fa9c79700a00206a006071b6-b18811a1fa9c73c30a00206a01a6673d-en-US>`_
                            """
                            _cmd = "CONNection"
                            
                        class TYPE(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:PORTs:TYPE
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d551e43da6ab4f79.htm#ID_9ba6f23efa9c81020a00206a012c71ef-cfe00d3cfa9c7b540a00206a01a6673d-en-US>`_
                            """
                            _cmd = "TYPE"
                            
                    class POWer(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:POWer
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ece5a47d15bb4f5a.htm#ID_daecab843f258e990a00206a01d8b36c-57484f7f3f25861d0a00206a01f2dc17-en-US>`_
                        """
                        _cmd = "POWer"
                        
                    class SAVE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:SAVE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/df7c981e3a554bbb.htm#ID_b67aa0efe2b45f300a00201900118a61-f6c4fe37e2b45de80a002019017b841c-en-US>`_
                        """
                        _cmd = "SAVE"
                        
                    class TYPE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:TYPE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7483c5a061284b1f.htm#ID_36396a4bfa9c894f0a00206a01b4efbf-b7c40877fa9c82e60a00206a01a6673d-en-US>`_
                        """
                        _cmd = "TYPE"
                        
                class AVERage(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:AVERage
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/63d5284950ff4da7.htm#ID_08198f833f0376d20a00201900418d9e-7e26d60a3f03756a0a00201901e91f0b-en-US>`_
                    """
                    _cmd = "AVERage"
                    
                class CHANnels(SCPINode):
                    """
                    SENSe:CORRection:COLLect:CHANnels
                    """
                    _cmd = "CHANnels"
                    
                    class ALL(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CHANnels:ALL
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e95181.htm#ID_34af02743512c65b0a00206a00362a14-7b024c7c3512beaa0a00206a01f2dc17-en-US>`_
                        """
                        _cmd = "ALL"
                        
                class CKIT(SCPINode):
                    """
                    SENSe:CORRection:COLLect:CKIT
                    """
                    _cmd = "CKIT"
                    
                    class INSTall(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CKIT:INSTall
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d704124a02f74b82.htm#ID_a4fc6106842e87b10a00201901eee4e7-881b8a8f842e864a0a00201901936165-en-US>`_
                        """
                        _cmd = "INSTall"
                        
                    class LOAD(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CKIT:LOAD
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/19eb6d332bd148fd.htm#ID_91e2e7bb842e89c40a00201901d9aa95-312cf34c842e883e0a00201901936165-en-US>`_
                        """
                        _cmd = "LOAD"
                        
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CKIT:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0383cf4db4d4429e.htm#ID_05b047fd842e8be70a00201901d09b34-d6b0335d842e8a700a00201901936165-en-US>`_
                        """
                        _cmd = "PORT"
                        
                class CONNection(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:CONNection
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/03265a2065d24aa7.htm#ID_51cce608fa9c91bb0a00206a019f3803-81b5f60bfa9c8b910a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CONNection"
                    
                    class GENDers(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CONNection:GENDers
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c63ca1c037e64fb8.htm#ID_b1dca677135238210a00206a00aaa3a0-d8439156135232640a00206a0182dc26-en-US>`_
                        """
                        _cmd = "GENDers"
                        
                    class PORTs(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CONNection:PORTs
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8566df6a31664d76.htm#ID_00065edcfa9c99d90a00206a01564942-32668de0fa9c93af0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "PORTs"
                        
                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:DELete
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2ad00861f5b34278.htm#ID_1eb59eedfa9ca2070a00206a002812f3-1406a431fa9c9bdc0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DELete"
                    
                class ERRor(SCPINode, SCPIQuery):
                    """
                    SENSe:CORRection:COLLect:ERRor
                    """
                    _cmd = "ERRor"
                    
                class FIXTure(SCPINode, SCPISet):
                    """
                    SENSe:CORRection:COLLect:FIXTure
                    """
                    _cmd = "FIXTure"
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/baea708b7c254238.htm#ID_c22640a8fa9ccde90a00206a0017e345-5e45eb40fa9cc7320a00206a01a6673d-en-US>`_
                        """
                        _cmd = "ACQuire"
                        
                    class EXPort(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:EXPort
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cdba7a0f9aab4eee.htm#ID_5b2eb4d5a6eab6940a001ae72c53e02a-418808e9a6eab51d0a001ae729ca0bb3-en-US>`_
                        """
                        _cmd = "EXPort"
                        
                    class IMPort(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:IMPort
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cdba7a0f9aab4eee.htm#ID_c8c75a54a6eab8a80a001ae71f2af99f-b95927ecaae4e1f10a001ae70925c00c-en-US>`_
                        """
                        _cmd = "IMPort"
                        
                    class LMParameter(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:COLLect:FIXTure:LMParameter
                        """
                        _cmd = "LMParameter"
                        
                        class LOSS(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:COLLect:FIXTure:LMParameter:LOSS
                            """
                            _cmd = "LOSS"
                            
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:CORRection:COLLect:FIXTure:LMParameter:LOSS:STATe
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/60ac72a649b24071.htm#ID_61297150fa9caa440a00206a01dd071f-244481e2fa9ca3fb0a00206a01a6673d-en-US>`_
                                """
                                _cmd = "STATe"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:FIXTure:LMParameter:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/594469a5314f4530.htm#ID_de9f2028fa9cb2fe0a00206a01cb5ae0-84440f34fa9cac480a00206a01a6673d-en-US>`_
                            """
                            _cmd = "STATe"
                            
                    class SAVE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:SAVE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f8f30ac030744b53.htm#ID_6eec3f5efa9cbba90a00206a00d4fca3-753af30dfa9cb5210a00206a01a6673d-en-US>`_
                        """
                        _cmd = "SAVE"
                        
                    class STARt(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1ed97663b6774143.htm#ID_91250745fa9cc4e00a00206a01bd2953-4cf1ec84fa9cbdeb0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STARt"
                        
                class LOAD(SCPINode):
                    """
                    SENSe:CORRection:COLLect:LOAD
                    """
                    _cmd = "LOAD"
                    
                    class SELected(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:LOAD:SELected
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9494dd1d711a413b.htm#ID_c10b85456c0c5cad0a00206a002bc4d4-6857c5656c0c51cf0a00206a01eade93-en-US>`_
                        """
                        _cmd = "SELected"
                        
                class METHod(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:METHod
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b70277ab91e94a61.htm#ID_3b1451ddfa9cd6450a00206a0173e35e-f66c5332fa9cd01b0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "METHod"
                    
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:METHod:DEFine
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/24bc511f46a7483a.htm#ID_aaba0ddffa9cde440a00206a019c590e-74fbf89bfa9cd8490a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DEFine"
                        
                class PMETer(SCPINode):
                    """
                    SENSe:CORRection:COLLect:PMETer
                    """
                    _cmd = "PMETer"
                    
                    class ID(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:PMETer:ID
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e96326.htm#ID_5bda58c53512d2ed0a00206a010922a3-3fb7cfcf3512c9a60a00206a01f2dc17-en-US>`_
                        """
                        _cmd = "ID"
                        
                class SAVE(SCPINode, SCPISet):
                    """
                    SENSe:CORRection:COLLect:SAVE
                    """
                    _cmd = "SAVE"
                    
                    class DEFault(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:SAVE:DEFault
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/27cd611c98df422b.htm#ID_29dbd581fa9d097b0a00206a00f2378b-e91b3dc2fa9d03120a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DEFault"
                        
                    class DUMMy(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:SAVE:DUMMy
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9578a3d0f68b43f6.htm#ID_ef2c6f57fa9d24650a00206a00bbe1ad-9e8aac18fa9d1d700a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DUMMy"
                        
                    class SELected(SCPINode, SCPISet):
                        """
                        SENSe:CORRection:COLLect:SAVE:SELected
                        """
                        _cmd = "SELected"
                        
                        class DEFault(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:SAVE:SELected:DEFault
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d6b4af70d4224ab3.htm#ID_de443b96fa9d11e70a00206a014e80a8-932f4fb4fa9d0b9d0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "DEFault"
                            
                        class DUMMy(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:SAVE:SELected:DUMMy
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1d56c9ae6dcd4805.htm#ID_6e9ab6f4fa9d1b1e0a00206a01a07be4-0f07f7f3fa9d14190a00206a01a6673d-en-US>`_
                            """
                            _cmd = "DUMMy"
                            
                class SCONnection(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:SCONnection
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8da8250da50d4831.htm#ID_01899f1efa9d2cc20a00206a00e935a8-c3bdda95fa9d26d60a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SCONnection"
                    
            class CONNection(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:CONNection
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6a95957e0c09448f.htm#ID_8ce9dfd6fa9d53450a00206a0113cb5f-f8a0ef34fa9d4db70a00206a01a6673d-en-US>`_
                """
                _cmd = "CONNection"
                
                class CATalog(SCPINode, SCPIQuery):
                    """
                    `SENSe:CORRection:CONNection:CATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/40aa01430fea4e5e.htm#ID_79a95dcbfa9d5ac70a00206a00e29836-98a422edfa9d55290a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CATalog"
                    
                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CONNection:DELete
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/48ba6caa89804951.htm#ID_395171f4fa9d62490a00206a001360eb-1041e23ffa9d5c9c0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DELete"
                    
            class CSET(SCPINode):
                """
                SENSe:CORRection:CSET
                """
                _cmd = "CSET"
                
                class DESCription(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CSET:DESCription
                    """
                    _cmd = "DESCription"
                    
            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:DATA
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a4c46fde7af640d1.htm#ID_96ff5d0afa9d718b0a00206a01f3d838-01a15260fa9d6bbf0a00206a01a6673d-en-US>`_
                """
                _cmd = "DATA"
                
                class PARameter(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:DATA:PARameter
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/23ded7e07ce64385.htm#ID_f3df74b6fa9d78fd0a00206a01be988b-a95dfeb4fa9d73600a00206a01a6673d-en-US>`_
                    """
                    _cmd = "PARameter"
                    
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SENSe:CORRection:DATA:PARameter:COUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d34a1f2a8f994c22.htm#ID_b4b8c587e2b476620a00201900e87abc-cccf6c58e2b475290a002019017b841c-en-US>`_
                        """
                        _cmd = "COUNt"
                        
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:DATA:PARameter:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/23ded7e07ce64385.htm#ID_59416659351399f60a00206a01efcee1-dcc75689351391a90a00206a01f2dc17-en-US>`_
                        """
                        _cmd = "PORT"
                        
            class DATE(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:DATE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4dd13cde83174c3c.htm#ID_5fc665affa9d806f0a00206a00be0e91-519f73bdfa9d7ae20a00206a01a6673d-en-US>`_
                """
                _cmd = "DATE"
                
            class DSTate(SCPINode, SCPIQuery):
                """
                SENSe:CORRection:DSTate
                """
                _cmd = "DSTate"
                
            class EDELay(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:EDELay
                """
                _cmd = "EDELay"
                
                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:AUTO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c0309a71cecc4d65.htm#ID_086c6faffa9d87e20a00206a009223dc-943616b5fa9d82440a00206a01a6673d-en-US>`_
                    """
                    _cmd = "AUTO"
                    
                class DIELectric(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:DIELectric
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bfd7289a5fd44070.htm#ID_6ae1e633fa9d8f730a00206a01721163-3f04d6d3fa9d89c60a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DIELectric"
                    
                class DISTance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:DISTance
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b7f8cd6052834f53.htm#ID_70b40f05fa9d96f50a00206a004c7fd4-86ce2b88fa9d91570a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DISTance"
                    
                class ELENgth(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:ELENgth
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/157c536c22cf4d9a.htm#ID_640b9ad4fa9d9e670a00206a01bfa35f-8a305bbffa9d98d90a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ELENgth"
                    
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:TIME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e028626ab9d44bf9.htm#ID_ab5a15eefa9da6180a00206a0031b88e-9ce7e9c4fa9da04c0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "TIME"
                    
            class LOSS(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:LOSS
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2902157d598f48ce.htm#ID_e6e77f94fa9db56a0a00206a0193f03d-33f5f50ffa9daf8e0a00206a01a6673d-en-US>`_
                """
                _cmd = "LOSS"
                
                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:AUTO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9c89299de8954e56.htm#ID_a9794b32fa9dbd0b0a00206a00198b3b-88926c88fa9db74e0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "AUTO"
                    
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e17920dcadb14ebe.htm#ID_eaedac34fa9dc48d0a00206a0015b590-244f9ff3fa9dbeef0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "FREQuency"
                    
                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bcbdd9797a884be7.htm#ID_1b00a820fa9dcc3d0a00206a018802f3-f294d833fa9dc6810a00206a01a6673d-en-US>`_
                    """
                    _cmd = "OFFSet"
                    
            class OFFSet(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:OFFSet
                """
                _cmd = "OFFSet"
                
                class COMPensation(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:OFFSet:COMPensation
                    """
                    _cmd = "COMPensation"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:OFFSet:COMPensation:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/238a1fddd13747e0.htm#ID_840216d6a6eac4dd0a001ae756bfb09a-f47f6deea6eac3660a001ae729ca0bb3-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class DFComp(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:OFFSet:DFComp
                    """
                    _cmd = "DFComp"
                    
                    class STATe(SCPINode, SCPIQuery):
                        """
                        `SENSe:CORRection:OFFSet:DFComp:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/586836c972434d7e.htm#ID_df319251fa9ddc3b0a00206a000d80ee-97ada771fa9dd66f0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:OFFSet:MAGNitude
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1e81fc08465043b6.htm#ID_8f8dc01ffa9de5630a00206a006db9af-424d6ac0fa9ddfa60a00206a01a6673d-en-US>`_
                    """
                    _cmd = "MAGNitude"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:OFFSet:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6485389d1a28497a.htm#ID_5b5ee42bfa9ded040a00206a01bba80c-d2212d06fa9de7470a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class PCAL(SCPINode, SCPISet):
                """
                `SENSe:CORRection:PCAL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f951bfb5b8df44ac.htm#ID_f2fa2fc6aaa800620a00206a0094909c-e54697eeaaa7f46c0a00206a00dee6b8-en-US>`_
                """
                _cmd = "PCAL"
                
            class POWer(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:POWer
                """
                _cmd = "POWer"
                
                class ACQuire(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:POWer:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/11090299f2ed4cb0.htm#ID_e41508c7fa9df4950a00206a013d8a2a-c4d9f94dfa9deed90a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ACQuire"
                    
                class AWAVe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:POWer:AWAVe
                    """
                    _cmd = "AWAVe"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:POWer:AWAVe:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1066b6f12da342a8.htm#ID_39a8d55efa9dfc360a00206a016597eb-d55487bdfa9df6890a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:POWer:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6920624db9394985.htm#ID_da5741dffa9e04930a00206a01c80d11-15e9d1bffa9dfe2a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DATA"
                    
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:POWer:DATA:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6920624db9394985.htm#ID_e7e7d1f03513d0d40a00206a019c308c-9a1221113513c9530a00206a01f2dc17-en-US>`_
                        """
                        _cmd = "PORT"
                        
                class HARMonic(SCPINode):
                    """
                    SENSe:CORRection:POWer:HARMonic
                    """
                    _cmd = "HARMonic"
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        SENSe:CORRection:POWer:HARMonic:ACQuire
                        """
                        _cmd = "ACQuire"
                        
                class IMODulation(SCPINode):
                    """
                    SENSe:CORRection:POWer:IMODulation
                    """
                    _cmd = "IMODulation"
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:POWer:IMODulation:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e0a7ba12dfc644c7.htm#ID_8280b6dffa9e13e50a00206a00dfea28-2ca4e2bafa9e0e280a00206a01a6673d-en-US>`_
                        """
                        _cmd = "ACQuire"
                        
                class MIXer(SCPINode):
                    """
                    SENSe:CORRection:POWer:MIXer
                    """
                    _cmd = "MIXer"
                    
                    class IF(SCPINode):
                        """
                        SENSe:CORRection:POWer:MIXer:IF
                        """
                        _cmd = "IF"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            SENSe:CORRection:POWer:MIXer:IF:ACQuire
                            """
                            _cmd = "ACQuire"
                            
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:POWer:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7646142b089747f0.htm#ID_45ae6bc1fa9eeadb0a00206a011182c9-b8091dc0fa9ee4f00a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class PSTate(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:PSTate
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cc435717f8b94267.htm#ID_df533854e2b482770a002019006f0182-17cc5a84e2b4813f0a002019017b841c-en-US>`_
                """
                _cmd = "PSTate"
                
            class SMATrix(SCPINode):
                """
                SENSe:CORRection:SMATrix
                """
                _cmd = "SMATrix"
                
                class CDATa(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:SMATrix:CDATa
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/502fca8391fe467f.htm#ID_f5cc70d5e2b4840e0a002019018689c7-265a6a30e2b482d50a002019017b841c-en-US>`_
                    """
                    _cmd = "CDATa"
                    
                    class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:SMATrix:CDATa:CATalog
                        """
                        _cmd = "CATalog"
                        
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:SMATrix:CDATa:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/502fca8391fe467f.htm#ID_985f5c3ee2b4875a0a00201900ca10d1-4f0b1f65e2b486310a002019017b841c-en-US>`_
                        """
                        _cmd = "PORT"
                        
                        class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:SMATrix:CDATa:PORT:CATalog
                            """
                            _cmd = "CATalog"
                            
            class SSTate(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:SSTate
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/032f6950568d45b0.htm#ID_ef2640f7fa9ef24e0a00206a0113e683-793bfa23fa9eecc00a00206a01a6673d-en-US>`_
                """
                _cmd = "SSTate"
                
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9e4376c2e66f46fb.htm#ID_1251d801fa9ef9c00a00206a00c826db-8d11769cfa9ef4320a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
            class STIMulus(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:STIMulus
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7c130eacff3645f3.htm#ID_3870b1b51353668f0a00206a01286f0b-eaf26caa135360e10a00206a0182dc26-en-US>`_
                """
                _cmd = "STIMulus"
                
                class PORT(SCPINodeN, SCPIQuery):
                    """
                    `SENSe:CORRection:STIMulus:PORT
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7c130eacff3645f3.htm#ID_aca3f0a13513ea960a00206a007adc1d-2c5c50a33513e3330a00206a01f2dc17-en-US>`_
                    """
                    _cmd = "PORT"
                    
        class COUPle(SCPINode, SCPIQuery, SCPISet):
            """
            `SENSe:COUPle
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6bd6847283104056.htm#ID_b39880affa9f01320a00206a01556890-2f7c24edfa9efba40a00206a01a6673d-en-US>`_
            """
            _cmd = "COUPle"
            
        class DC(SCPINodeN):
            """
            SENSe:DC
            """
            _cmd = "DC"
            
            class RANGe(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:DC:RANGe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/59cff42e06dc4f8e.htm#ID_85e3c36e1356b77d0a00206a0011de08-ec487a421356b1d00a00206a0182dc26-en-US>`_
                """
                _cmd = "RANGe"
                
        class FREQuency(SCPINodeN, SCPIQuery, SCPISet):
            """
            SENSe:FREQuency
            """
            _cmd = "FREQuency"
            
            class CENTer(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CENTer
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/42d8825bb9304f5a.htm#ID_e2406746fa9f360d0a00206a00158714-aed43b75fa9f30700a00206a01a6673d-en-US>`_
                """
                _cmd = "CENTer"
                
            class CONVersion(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CONVersion
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c8efca597e3c4cad.htm#ID_a3bb2a00fa9f3d700a00206a01051abd-48ef6c66fa9f37e20a00206a01a6673d-en-US>`_
                """
                _cmd = "CONVersion"
                
                class ARBitrary(SCPINode):
                    """
                    `SENSe:FREQuency:CONVersion:ARBitrary
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e99764.htm#ID_98a8a17bfa9f45010a00206a009ce494-022448048c5dc3830a00206a0022f285-en-US>`_
                    """
                    _cmd = "ARBitrary"
                    
                    class PMETer(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:ARBitrary:PMETer
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/588399e0817144b3.htm#ID_f08d8321fa9f4c640a00206a00cb7453-0eba10acfa9f46e60a00206a01a6673d-en-US>`_
                        """
                        _cmd = "PMETer"
                        
                class DEVice(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:DEVice
                    """
                    _cmd = "DEVice"
                    
                    class PCOefficient(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:DEVice:PCOefficient
                        """
                        _cmd = "PCOefficient"
                        
                class GAIN(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:GAIN
                    """
                    _cmd = "GAIN"
                    
                    class LMCorrection(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:GAIN:LMCorrection
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ddf6ae7f67c14862.htm#ID_19b501f261299b6a0a00206a013f7404-10d65d59612992af0a00206a01ed2866-en-US>`_
                        """
                        _cmd = "LMCorrection"
                        
                class HARMonic(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:HARMonic
                    """
                    _cmd = "HARMonic"
                    
                    class ORDer(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:HARMonic:ORDer
                        """
                        _cmd = "ORDer"
                        
                    class RELative(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:HARMonic:RELative
                        """
                        _cmd = "RELative"
                        
                    class RPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:HARMonic:RPORt
                        """
                        _cmd = "RPORt"
                        
                    class SPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:HARMonic:SPORt
                        """
                        _cmd = "SPORt"
                        
                class MIXer(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:MIXer
                    """
                    _cmd = "MIXer"
                    
                    class FFIXed(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:FFIXed
                        """
                        _cmd = "FFIXed"
                        
                    class FIXed(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:FIXed
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/60891c3d7fd54ed6.htm#ID_4644b954fa9fa0fc0a00206a004be5bf-11ab3bc9fa9f9a740a00206a01a6673d-en-US>`_
                        """
                        _cmd = "FIXed"
                        
                    class FUNDamental(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:FUNDamental
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a1c4edf2d1ac45cf.htm#ID_8a511aeefa9fa9f50a00206a01692dac-c23eb715fa9fa33e0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "FUNDamental"
                        
                    class IFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:IFFixed
                        """
                        _cmd = "IFFixed"
                        
                    class IFPort(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:IFPort
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/61bcffd9773b4ef3.htm#ID_815f1cf4aaa81e3b0a00206a0081c154-9df8ed98aaa812730a00206a00dee6b8-en-US>`_
                        """
                        _cmd = "IFPort"
                        
                    class LOEXternal(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:LOEXternal
                        """
                        _cmd = "LOEXternal"
                        
                    class LOFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:LOFixed
                        """
                        _cmd = "LOFixed"
                        
                    class LOINternal(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:LOINternal
                        """
                        _cmd = "LOINternal"
                        
                    class LOMultiplier(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOMultiplier
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/743380a33eda455c.htm#ID_f3d77c26aaa82d3e0a00206a0170f2da-d163fc66aaa821860a00206a00dee6b8-en-US>`_
                        """
                        _cmd = "LOMultiplier"
                        
                    class LOPort(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOPort
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/74fe7d03764c4a7f.htm#ID_6a4729ceaaa83b090a00206a01c4bfbd-de91c582aaa8301d0a00206a00dee6b8-en-US>`_
                        """
                        _cmd = "LOPort"
                        
                    class MFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:MFFixed
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6b15b2a135cf44f0.htm#ID_be2dd1ceaaa848480a00206a004f1b7e-328d8895aaa83d6b0a00206a00dee6b8-en-US>`_
                        """
                        _cmd = "MFFixed"
                        
                    class RFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:RFFixed
                        """
                        _cmd = "RFFixed"
                        
                    class RFMultiplier(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:RFMultiplier
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f8796452875f445f.htm#ID_d37d6ecbaaa856ee0a00206a01f7adfa-b1ce8fe7aaa84bd20a00206a00dee6b8-en-US>`_
                        """
                        _cmd = "RFMultiplier"
                        
                    class RFPort(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:RFPort
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e433724a23fd4a9e.htm#ID_9356f065aaa863900a00206a004b1cf6-82c43f97aaa859400a00206a00dee6b8-en-US>`_
                        """
                        _cmd = "RFPort"
                        
                    class STAGes(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:STAGes
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c8e19d7d125445db.htm#ID_1ef50da0aaa872460a00206a01ceb9d1-40349cbeaaa8665f0a00206a00dee6b8-en-US>`_
                        """
                        _cmd = "STAGes"
                        
                    class TFRequency(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:TFRequency
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/52f5e8c3a19d41ca.htm#ID_51f82e6cfa9feac60a00206a002e1df4-7cc304a8fa9fe4000a00206a01a6673d-en-US>`_
                        """
                        _cmd = "TFRequency"
                        
            class CW(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CW
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f9c9976fdd0f4f39.htm#ID_2ac09567faa0b2f80a00206a013090e9-fc5e7f70faa0ad4a0a00206a01a6673d-en-US>`_
                """
                _cmd = "CW"
                
            class FIXed(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:FIXed
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f9c9976fdd0f4f39.htm#ID_731505e2fa9ff2480a00206a01158020-7d13c8dafa9fec9b0a00206a01a6673d-en-US>`_
                """
                _cmd = "FIXed"
                
            class IMODulation(SCPINode):
                """
                SENSe:FREQuency:IMODulation
                """
                _cmd = "IMODulation"
                
                class CONVersion(SCPINode, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:CONVersion
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4d584eff06f84733.htm#ID_23fcb342faa0017b0a00206a00b25587-58d97526fa9ffbce0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CONVersion"
                    
                class LTONe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:LTONe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ab3534c8bace41b4.htm#ID_5bf57addfaa0091c0a00206a0142fa1e-01793a61faa0035f0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "LTONe"
                    
                class ORDer(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:FREQuency:IMODulation:ORDer
                    """
                    _cmd = "ORDer"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:IMODulation:ORDer:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8ad47d678f7f436b.htm#ID_06e1352dfaa010ad0a00206a003c0b60-aac10042faa00af00a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class RECeiver(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:RECeiver
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e1eb2d7b18c24a08.htm#ID_b274a1ddfaa0186e0a00206a0161499f-bf9aaa56faa012920a00206a01a6673d-en-US>`_
                    """
                    _cmd = "RECeiver"
                    
                class SPECtrum(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:FREQuency:IMODulation:SPECtrum
                    """
                    _cmd = "SPECtrum"
                    
                    class MORDer(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:IMODulation:SPECtrum:MORDer
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b0c80ebe3fe84751.htm#ID_4245b5cdfaa0207c0a00206a0107003e-ab9dd1fffaa01a520a00206a01a6673d-en-US>`_
                        """
                        _cmd = "MORDer"
                        
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:IMODulation:SPECtrum:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3bf0c8d352974b60.htm#ID_01be2623faa029850a00206a018c40e0-1e47673cfaa0229f0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class TDIStance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:TDIStance
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a7c1836cab484001.htm#ID_aafb6b64faa032bc0a00206a011bedae-83b2e89cfaa02bc70a00206a01a6673d-en-US>`_
                    """
                    _cmd = "TDIStance"
                    
                class TTOutput(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:FREQuency:IMODulation:TTOutput
                    """
                    _cmd = "TTOutput"
                    
                class UTONe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:UTONe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ff61ec52404c4930.htm#ID_63f13342faa046530a00206a012e0ff3-67fe67dbfaa03f5e0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "UTONe"
                    
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:MODE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/208318e5658e49fa.htm#ID_fe506898faa08cd20a00206a01a4bc44-203297cdfaa086e60a00206a01a6673d-en-US>`_
                """
                _cmd = "MODE"
                
            class SBANd(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:SBANd
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/020d819cc9124330.htm#ID_18e53f5efaa094830a00206a0157f1ef-0a15cef1faa08eb60a00206a01a6673d-en-US>`_
                """
                _cmd = "SBANd"
                
            class SEGMent(SCPINode):
                """
                SENSe:FREQuency:SEGMent
                """
                _cmd = "SEGMent"
                
                class AXIS(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:SEGMent:AXIS
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/79ff3cfca02d43db.htm#ID_e107f4ce6129d6200a00206a002cf90e-16bf461d6129cde30a00206a01ed2866-en-US>`_
                    """
                    _cmd = "AXIS"
                    
            class SPAN(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:SPAN
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/880fb7cf42594d10.htm#ID_19d721c4faa09c240a00206a01889fa1-5f6f4612faa096670a00206a01a6673d-en-US>`_
                """
                _cmd = "SPAN"
                
            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:STARt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/62a9e33d543548b1.htm#ID_cb181842faa0a3d50a00206a0130d1a9-3b77cf21faa09df90a00206a01a6673d-en-US>`_
                """
                _cmd = "STARt"
                
            class STOP(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:STOP
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/62a9e33d543548b1.htm#ID_8da94e0ffaa0ab560a00206a001393fe-a4f0d36bfaa0a5b90a00206a01a6673d-en-US>`_
                """
                _cmd = "STOP"
                
        class FUNCtion(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:FUNCtion
            """
            _cmd = "FUNCtion"
            
            class ON(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FUNCtion:ON
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a60c5184e5484818.htm#ID_5611a1c6faaa7b640a00206a00e83a51-a685455efaaa75a70a00206a01a6673d-en-US>`_
                """
                _cmd = "ON"
                
        class LPORt(SCPINodeN):
            """
            SENSe:LPORt
            """
            _cmd = "LPORt"
            
            class ZCOMmon(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:LPORt:ZCOMmon
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ff5f3222ee424c70.htm#ID_94158978faa1977b0a00206a00b62876-b7b2e2a9faa191ce0a00206a01a6673d-en-US>`_
                """
                _cmd = "ZCOMmon"
                
            class ZDEFault(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:LPORt:ZDEFault
                """
                _cmd = "ZDEFault"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:LPORt:ZDEFault:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b5192de6d67e4e20.htm#ID_b2a7efd9a6eae2890a001ae748b54b6c-29d33fd7a6eae0f30a001ae729ca0bb3-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class ZDIFferent(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:LPORt:ZDIFferent
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ff5f3222ee424c70.htm#ID_96565f11faa19f0c0a00206a00efad8e-ed441534faa199500a00206a01a6673d-en-US>`_
                """
                _cmd = "ZDIFferent"
                
        class PAE(SCPINode):
            """
            SENSe:PAE
            """
            _cmd = "PAE"
            
            class DCINput(SCPINode):
                """
                SENSe:PAE:DCINput
                """
                _cmd = "DCINput"
                
                class MAIN(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PAE:DCINput:MAIN
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6fc282982d944daf.htm#ID_356ca9e6612ad1960a00206a008832d6-0a4f4b44612ac12b0a00206a01ed2866-en-US>`_
                    """
                    _cmd = "MAIN"
                    
                class SECondary(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PAE:DCINput:SECondary
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bcee4f6f0bb44595.htm#ID_53a5ef24612ae56c0a00206a01de3061-47c198ac612ad7530a00206a01ed2866-en-US>`_
                    """
                    _cmd = "SECondary"
                    
            class PARameters(SCPINode):
                """
                SENSe:PAE:PARameters
                """
                _cmd = "PARameters"
                
                class I(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PAE:PARameters:I
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/77a78fdc8983460b.htm#ID_70ab057e612a25690a00206a0159a980-61443cbe612a1e830a00206a01ed2866-en-US>`_
                    """
                    _cmd = "I"
                    
                class R(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PAE:PARameters:R
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b8cc1a404aae4a06.htm#ID_cdd9f751612a2f8b0a00206a007085fc-71778e41612a28090a00206a01ed2866-en-US>`_
                    """
                    _cmd = "R"
                    
                class U(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PAE:PARameters:U
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1412c2ce185c4b54.htm#ID_47333546612a392f0a00206a0172f758-80c4866f612a31dc0a00206a01ed2866-en-US>`_
                    """
                    _cmd = "U"
                    
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PAE:TYPE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5425e7f0f7b24f8a.htm#ID_da0fd500612afa6b0a00206a006111f7-dab87b46612aed8a0a00206a01ed2866-en-US>`_
                """
                _cmd = "TYPE"
                
        class PORT(SCPINodeN):
            """
            SENSe:PORT
            """
            _cmd = "PORT"
            
            class ZREFerence(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PORT:ZREFerence
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9e4c4942dcf04a10.htm#ID_307cb740faa1b7b50a00206a0149fb85-20b51d47faa1b2080a00206a01a6673d-en-US>`_
                """
                _cmd = "ZREFerence"
                
        class POWer(SCPINode):
            """
            SENSe:POWer
            """
            _cmd = "POWer"
            
            class AGCMode(SCPINodeN):
                """
                SENSe:POWer:AGCMode
                """
                _cmd = "AGCMode"
                
                class ACQuire(SCPINode, SCPISet):
                    """
                    `SENSe:POWer:AGCMode:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f6d3c2eb53224cd3.htm#ID_287e0e5b5de650020a002019005cd65d-61ceda195de64ec90a0020190152315a-en-US>`_
                    """
                    _cmd = "ACQuire"
                    
                class MEASure(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:POWer:AGCMode:MEASure
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/02847cb715004998.htm#ID_818b778e135527390a00206a0179ba91-f9b489121355216d0a00206a0182dc26-en-US>`_
                    """
                    _cmd = "MEASure"
                    
                class SAVE(SCPINode, SCPISet):
                    """
                    `SENSe:POWer:AGCMode:SAVE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a69c75b84ab946d7.htm#ID_467705d35de651e60a002019015c7244-7af5781c5de650bd0a0020190152315a-en-US>`_
                    """
                    _cmd = "SAVE"
                    
            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:POWer:ATTenuation
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/04a79a1d70d0496d.htm#ID_187ea6a6faa1bf460a00206a008dacb9-7302ebeefaa1b9990a00206a01a6673d-en-US>`_
                """
                _cmd = "ATTenuation"
                
            class GAINcontrol(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:POWer:GAINcontrol
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/02bdb8f60bae4be0.htm#ID_b94cb83baaa880010a00206a0033f802-17c67bf9aaa875340a00206a00dee6b8-en-US>`_
                """
                _cmd = "GAINcontrol"
                
                class GLOBal(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:POWer:GAINcontrol:GLOBal
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6a22d5d655e84479.htm#ID_4c6eef1eaaa88fa10a00206a003fbf40-763d4d64aaa8838b0a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "GLOBal"
                    
            class IFGain(SCPINodeN):
                """
                SENSe:POWer:IFGain
                """
                _cmd = "IFGain"
                
                class MEASure(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:POWer:IFGain:MEASure
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/02847cb715004998.htm#ID_b103b97afaa1c7350a00206a01f123cc-0f4f1ee9faa1c13a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "MEASure"
                    
        class PULSe(SCPINode):
            """
            SENSe:PULSe
            """
            _cmd = "PULSe"
            
            class GENerator(SCPINodeN):
                """
                SENSe:PULSe:GENerator
                """
                _cmd = "GENerator"
                
                class CPPRofile(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:PULSe:GENerator:CPPRofile
                    """
                    _cmd = "CPPRofile"
                    
                class DELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:PULSe:GENerator:DELay
                    """
                    _cmd = "DELay"
                    
                class PERiod(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:PULSe:GENerator:PERiod
                    """
                    _cmd = "PERiod"
                    
                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:PULSe:GENerator:POLarity
                    """
                    _cmd = "POLarity"
                    
                class TRAin(SCPINode):
                    """
                    SENSe:PULSe:GENerator:TRAin
                    """
                    _cmd = "TRAin"
                    
                    class DATA(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:PULSe:GENerator:TRAin:DATA
                        """
                        _cmd = "DATA"
                        
                    class DELete(SCPINode):
                        """
                        SENSe:PULSe:GENerator:TRAin:DELete
                        """
                        _cmd = "DELete"
                        
                        class ALL(SCPINode, SCPISet):
                            """
                            SENSe:PULSe:GENerator:TRAin:DELete:ALL
                            """
                            _cmd = "ALL"
                            
                    class PERiod(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:PULSe:GENerator:TRAin:PERiod
                        """
                        _cmd = "PERiod"
                        
                    class SEGMent(SCPINodeN):
                        """
                        SENSe:PULSe:GENerator:TRAin:SEGMent
                        """
                        _cmd = "SEGMent"
                        
                        class COUNt(SCPINode, SCPIQuery):
                            """
                            SENSe:PULSe:GENerator:TRAin:SEGMent:COUNt
                            """
                            _cmd = "COUNt"
                            
                        class STARt(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:PULSe:GENerator:TRAin:SEGMent:STARt
                            """
                            _cmd = "STARt"
                            
                        class STOP(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:PULSe:GENerator:TRAin:SEGMent:STOP
                            """
                            _cmd = "STOP"
                            
        class ROSCillator(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:ROSCillator
            """
            _cmd = "ROSCillator"
            
            class EXTernal(SCPINode):
                """
                SENSe:ROSCillator:EXTernal
                """
                _cmd = "EXTernal"
                
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:ROSCillator:EXTernal:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8fdadbfdb9f9447f.htm#ID_6c4e79f3faa938c30a00206a013d1159-f5402c6afaa933070a00206a01a6673d-en-US>`_
                    """
                    _cmd = "FREQuency"
                    
            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:ROSCillator:SOURce
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4314a7accd124cd8.htm#ID_c2c6217dfaa940550a00206a018060f9-42609acffaa93aa80a00206a01a6673d-en-US>`_
                """
                _cmd = "SOURce"
                
        class SEGMent(SCPINodeN, SCPIQuery, SCPISet):
            """
            SENSe:SEGMent
            """
            _cmd = "SEGMent"
            
            class ADD(SCPINode, SCPISet):
                """
                `SENSe:SEGMent:ADD
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8b499c72016147ec.htm#ID_42e94b09faa947f60a00206a01e7a868-404ea7abfaa942390a00206a01a6673d-en-US>`_
                """
                _cmd = "ADD"
                
            class BWIDth(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SEGMent:BWIDth
                """
                _cmd = "BWIDth"
                
                class RESolution(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:BWIDth:RESolution
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7f78d4cc550a43b4.htm#ID_a5fd34d6faa94f870a00206a0178a961-ff41de80faa949cb0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "RESolution"
                    
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:BWIDth:RESolution:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/85e00dbdac574895.htm#ID_7c9ad63afaa957280a00206a007d7923-baaeef63faa9516c0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "CONTrol"
                        
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:BWIDth:RESolution:SELect
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8ea6af2b51f94fd7.htm#ID_1347f01dfaa95f080a00206a01678d97-70ffbea1faa9590d0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "SELect"
                        
                        class CONTrol(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:SEGMent:BWIDth:RESolution:SELect:CONTrol
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d4fd2f19549e4c8c.htm#ID_77b69576faa966d80a00206a012e13eb-1431397ffaa960ec0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "CONTrol"
                            
            class CLEar(SCPINode, SCPISet):
                """
                `SENSe:SEGMent:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1e338ccd879849cc.htm#ID_ae21c7cdfaa96ec70a00206a00399727-eec3d465faa968eb0a00206a01a6673d-en-US>`_
                """
                _cmd = "CLEar"
                
            class COUNt(SCPINode, SCPIQuery):
                """
                `SENSe:SEGMent:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cc92badd888e4893.htm#ID_0aedf98efaa976b60a00206a015e9478-74d2e61cfaa970da0a00206a01a6673d-en-US>`_
                """
                _cmd = "COUNt"
                
            class DEFine(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:DEFine
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0fdd5bb7773c4237.htm#ID_68fd9307faa97e670a00206a007b59ed-faf43db76d4c9ff90a00206a00d96734-en-US>`_
                """
                _cmd = "DEFine"
                
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:DEFine:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5d2d463b271f465e.htm#ID_104e6acbfaa985f90a00206a013334f3-d97a540afaa9804c0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SELect"
                    
            class DELete(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:SEGMent:DELete
                """
                _cmd = "DELete"
                
                class ALL(SCPINode, SCPISet):
                    """
                    `SENSe:SEGMent:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ab5e9487d6324d5d.htm#ID_d97d6288faa98db90a00206a0151f78f-1bf10634faa987ed0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ALL"
                    
                class DUMMy(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:DELete:DUMMy
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8b87412b453542e4.htm#ID_e3d18ac5faa9955a0a00206a009f336d-55db9b98faa98f9d0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DUMMy"
                    
            class FREQuency(SCPINode):
                """
                SENSe:SEGMent:FREQuency
                """
                _cmd = "FREQuency"
                
                class CENTer(SCPINode, SCPIQuery):
                    """
                    `SENSe:SEGMent:FREQuency:CENTer
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b20419a51aad471f.htm#ID_94785a74faa99cdc0a00206a01d13180-4e26a2dcfaa9974e0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CENTer"
                    
                class SPAN(SCPINode, SCPIQuery):
                    """
                    `SENSe:SEGMent:FREQuency:SPAN
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b20419a51aad471f.htm#ID_00b1210dfaa9a46d0a00206a00bfcdb7-5367f9bffaa99ed00a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SPAN"
                    
                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:STARt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e6eca9c9cd1b422a.htm#ID_642356f7faa9abff0a00206a010d9e37-ddfabe24faa9a6520a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STARt"
                    
                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:STOP
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e6eca9c9cd1b422a.htm#ID_e9561eb0faa9b3710a00206a002ba8aa-3587e257faa9add40a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STOP"
                    
            class INSert(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:INSert
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a43fbabbfb8548ed.htm#ID_edfe071ffaa9bb510a00206a00232fd5-402184618754dbd40a00206a00048ead-en-US>`_
                """
                _cmd = "INSert"
                
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:INSert:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/53faae429fbd4847.htm#ID_b802bcedfaa9c2f20a00206a00e943e9-dfd68ad3faa9bd640a00206a01a6673d-en-US>`_
                    """
                    _cmd = "SELect"
                    
            class OVERlap(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:OVERlap
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d07bb6d0c6004991.htm#ID_ce5c83b4faa9cac20a00206a01aa0f97-808993ecfaa9c4d60a00206a01a6673d-en-US>`_
                """
                _cmd = "OVERlap"
                
            class POWer(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SEGMent:POWer
                """
                _cmd = "POWer"
                
                class GAINcontrol(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:POWer:GAINcontrol
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3efd8069d3aa445a.htm#ID_506a9a45aaa8a0a80a00206a014de620-c49903a0aaa892ed0a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "GAINcontrol"
                    
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:POWer:GAINcontrol:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9608e4d687cd4b33.htm#ID_55e47952aaa8ae450a00206a01d7002f-41fdea03aaa8a3770a00206a00dee6b8-en-US>`_
                        """
                        _cmd = "CONTrol"
                        
                class LEVel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:POWer:LEVel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/41f669a6f1ca47df.htm#ID_c32c7991faa9d2b10a00206a01709402-1a1b2272faa9cc970a00206a01a6673d-en-US>`_
                    """
                    _cmd = "LEVel"
                    
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:POWer:LEVel:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bd27175de2174b8a.htm#ID_0889af7afaa9da230a00206a01faf0df-69290e76faa9d4950a00206a01a6673d-en-US>`_
                        """
                        _cmd = "CONTrol"
                        
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d3960bdbcfeb49f4.htm#ID_6dc91a91faaa0f4c0a00206a01341c39-ceac6573faaa09900a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
            class SWEep(SCPINode):
                """
                SENSe:SEGMent:SWEep
                """
                _cmd = "SWEep"
                
                class DWELl(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:DWELl
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ce5c1223ab0542ed.htm#ID_011fb27efaa9e1c40a00206a009027ec-1580ec0bfaa9dc170a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DWELl"
                    
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:SWEep:DWELl:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dabe778ff0364c84.htm#ID_8056275efaa9e9750a00206a003922be-67d1b540faa9e3a90a00206a01a6673d-en-US>`_
                        """
                        _cmd = "CONTrol"
                        
                class GENeration(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:GENeration
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6ac02dfba9164182.htm#ID_7dff9430cf938f4d0a001ae76592e970-55859ec9cf938da70a001ae7061b2cf6-en-US>`_
                    """
                    _cmd = "GENeration"
                    
                class POINts(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:POINts
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/52d5a10625e64a82.htm#ID_04a142bffaa9f0e70a00206a01076885-20e0b786faa9eb4a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "POINts"
                    
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:TIME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/37b7c642120149da.htm#ID_f5b6df0ffaa9f8a80a00206a013a9a75-542f6badfaa9f2fb0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "TIME"
                    
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:SWEep:TIME:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ff129a9296e54210.htm#ID_a22e28fffaaa00390a00206a0084a14b-e9c5fc67faa9fa8c0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "CONTrol"
                        
                    class SUM(SCPINode, SCPIQuery):
                        """
                        `SENSe:SEGMent:SWEep:TIME:SUM
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/89fbe395bfe44bc6.htm#ID_b1ba9049faaa07bb0a00206a0168c693-2fa53146faaa020e0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "SUM"
                        
        class SWEep(SCPINode):
            """
            SENSe:SWEep
            """
            _cmd = "SWEep"
            
            class AXIS(SCPINode):
                """
                SENSe:SWEep:AXIS
                """
                _cmd = "AXIS"
                
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:AXIS:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8416b68505d74b1f.htm#ID_5571db31faaa18360a00206a01d696e2-91a48f48faaa12690a00206a01a6673d-en-US>`_
                    """
                    _cmd = "FREQuency"
                    
                class POWer(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:AXIS:POWer
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cfd456caf566495d.htm#ID_a33dcc53faaa1fb80a00206a016ce603-ccb15a96faaa1a2a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "POWer"
                    
            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5cb1268b17f34710.htm#ID_16e99ab0faaa27490a00206a008e95d3-fd50d4b6faaa21ac0a00206a01a6673d-en-US>`_
                """
                _cmd = "COUNt"
                
                class ALL(SCPINode, SCPISet):
                    """
                    `SENSe:SWEep:COUNt:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e104981.htm#ID_b22fd8a02b98b6df0a00206a00b47198-7af948622b98af1e0a00206a0020d3a0-en-US>`_
                    """
                    _cmd = "ALL"
                    
            class DETector(SCPINode):
                """
                SENSe:SWEep:DETector
                """
                _cmd = "DETector"
                
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:DETector:TIME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5e638bbfd9ca4218.htm#ID_6bf27c90faaa2efa0a00206a00bbbd04-fe2114b5faaa294d0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "TIME"
                    
            class DWELl(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:DWELl
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/48bb45e33ab64490.htm#ID_c04c664efaaa36ca0a00206a01e7ac36-1d281f10faaa30de0a00206a01a6673d-en-US>`_
                """
                _cmd = "DWELl"
                
                class IPOint(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:DWELl:IPOint
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8e067eefd1e34640.htm#ID_030aed4fbba8fcb80a00201901c6f0bf-a6d51bb2bba8fb7f0a0020190170f726-en-US>`_
                    """
                    _cmd = "IPOint"
                    
            class GENeration(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:GENeration
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2298b3dd1e844065.htm#ID_7ee8413cfaaa3e5b0a00206a00e2e4dc-8f0aff4cfaaa389e0a00206a01a6673d-en-US>`_
                """
                _cmd = "GENeration"
                
                class ANALog(SCPINode):
                    """
                    SENSe:SWEep:GENeration:ANALog
                    """
                    _cmd = "ANALog"
                    
                    class CONDition(SCPINode, SCPIQuery):
                        """
                        `SENSe:SWEep:GENeration:ANALog:CONDition
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c804742dafba418c.htm#ID_4422091acf9397d90a001ae74b49912d-26ef356bcf9395580a001ae7061b2cf6-en-US>`_
                        """
                        _cmd = "CONDition"
                        
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SWEep:MODE
                """
                _cmd = "MODE"
                
            class POINts(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:POINts
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/68b77d9828354b78.htm#ID_eaf7e123faaa4d8e0a00206a00265a51-df944ab9faaa47d10a00206a01a6673d-en-US>`_
                """
                _cmd = "POINts"
                
            class SPACing(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:SPACing
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f3498d3b009e4326.htm#ID_fcf6483afaaa553e0a00206a0166926c-c3423ddbfaaa4f820a00206a01a6673d-en-US>`_
                """
                _cmd = "SPACing"
                
            class SRCPort(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:SRCPort
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/31cb07b38fbe4454.htm#ID_06884359faaa9a270a00206a01493bc8-eb083f47faaa944b0a00206a01a6673d-en-US>`_
                """
                _cmd = "SRCPort"
                
            class STEP(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:STEP
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6958d4fb3c5642a2.htm#ID_34eced8ffaaa5cef0a00206a0034523e-8bc6b624faaa57520a00206a01a6673d-en-US>`_
                """
                _cmd = "STEP"
                
            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:TIME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8227ae4383e449fe.htm#ID_68a69f3cfaaa64810a00206a010d0e5b-25292a32faaa5ee30a00206a01a6673d-en-US>`_
                """
                _cmd = "TIME"
                
                class AUTO(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:TIME:AUTO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4e1073e7fde645a8.htm#ID_7134b8a5faaa6c310a00206a002ca1b5-cd3732cffaaa66650a00206a01a6673d-en-US>`_
                    """
                    _cmd = "AUTO"
                    
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:TYPE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/3092cc2858af4096.htm#ID_b8dccd81faaa73d30a00206a018614c7-c134571ffaaa6e060a00206a01a6673d-en-US>`_
                """
                _cmd = "TYPE"
                
        class UDSParams(SCPINodeN):
            """
            SENSe:UDSParams
            """
            _cmd = "UDSParams"
            
            class ACTive(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:UDSParams:ACTive
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6648d86a94534c05.htm#ID_98fbfd15842ed63e0a002019008f7696-77db25eb842ed4c70a00201901936165-en-US>`_
                """
                _cmd = "ACTive"
                
            class PARam(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:UDSParams:PARam
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9862134a154b4fea.htm#ID_6e316dbd842ed8610a002019005592c6-0069e2d3842ed6db0a00201901936165-en-US>`_
                """
                _cmd = "PARam"
                
    class SOURce(SCPINodeN):
        """
        SOURce
        """
        _cmd = "SOURce"
        
        class FREQuency(SCPINodeN, SCPIQuery, SCPISet):
            """
            SOURce:FREQuency
            """
            _cmd = "FREQuency"
            
            class CONVersion(SCPINode):
                """
                SOURce:FREQuency:CONVersion
                """
                _cmd = "CONVersion"
                
                class ARBitrary(SCPINode):
                    """
                    SOURce:FREQuency:CONVersion:ARBitrary
                    """
                    _cmd = "ARBitrary"
                    
                    class EFRequency(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:ARBitrary:EFRequency
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/323c75e925bb4524.htm#ID_b7a0eff3faaad3090a00206a0048d9a3-8f628099faaaccb00a00206a01a6673d-en-US>`_
                        """
                        _cmd = "EFRequency"
                        
                    class IFRequency(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:ARBitrary:IFRequency
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/59b39faac9d34290.htm#ID_f158a498faaadb850a00206a016d54a1-dca8927efaaad52c0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "IFRequency"
                        
                class MIXer(SCPINode):
                    """
                    SOURce:FREQuency:CONVersion:MIXer
                    """
                    _cmd = "MIXer"
                    
                    class FUNDamental(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:CONVersion:MIXer:FUNDamental
                        """
                        _cmd = "FUNDamental"
                        
                    class PFIXed(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:CONVersion:MIXer:PFIXed
                        """
                        _cmd = "PFIXed"
                        
                    class PMFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PMFixed
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/90e5b7d03ba1419a.htm#ID_dcd270fcaaa8bb350a00206a006b2206-a481c9f8aaa8b0870a00206a00dee6b8-en-US>`_
                        """
                        _cmd = "PMFixed"
                        
                    class PMODe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PMODe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6abc6f3ee12a4a89.htm#ID_eca305c5aaa8c8740a00206a010fb1c0-7aa0a2dfaaa8be420a00206a00dee6b8-en-US>`_
                        """
                        _cmd = "PMODe"
                        
            class CW(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:CW
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/53b73ef8963647ff.htm#ID_6590a713faaafaa60a00206a01616355-b65bc797faaaf4f90a00206a01a6673d-en-US>`_
                """
                _cmd = "CW"
                
            class FIXed(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:FIXed
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/53b73ef8963647ff.htm#ID_a7452765faaaf3240a00206a011db4aa-5fe941c7faaaed670a00206a01a6673d-en-US>`_
                """
                _cmd = "FIXed"
                
        class GROup(SCPINodeN, SCPIQuery, SCPISet):
            """
            `SOURce:GROup
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/fc145e54206141d3.htm#ID_57d9bdd7faab02280a00206a004a8d5f-d5e97631faaafc8a0a00206a01a6673d-en-US>`_
            """
            _cmd = "GROup"
            
            class CLEar(SCPINode, SCPISet):
                """
                `SOURce:GROup:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/12c2fec8bb4c4781.htm#ID_ef09d686faab099a0a00206a01cdc798-26f736eafaab03fc0a00206a01a6673d-en-US>`_
                """
                _cmd = "CLEar"
                
            class COUNt(SCPINode, SCPIQuery):
                """
                `SOURce:GROup:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/08e95afdda7f45ce.htm#ID_fdf34ed4faab110c0a00206a00d13624-44e4ccb9faab0b6f0a00206a01a6673d-en-US>`_
                """
                _cmd = "COUNt"
                
            class DPORt(SCPINode):
                """
                SOURce:GROup:DPORt
                """
                _cmd = "DPORt"
                
                class COUNt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:GROup:DPORt:COUNt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f23e4eb88b3d40cb.htm#ID_d643aadd4f3002f00a001ae721324d54-2c3bec494f30011b0a001ae7211c9327-en-US>`_
                    """
                    _cmd = "COUNt"
                    
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:GROup:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dc3c54b22c6c4d29.htm#ID_46aebfb54f3005320a001ae7202c9a7a-48b729ec4f3003bb0a001ae7211c9327-en-US>`_
                """
                _cmd = "NAME"
                
            class PORTs(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:GROup:PORTs
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0ce89bb991c34110.htm#ID_7894c65cfaab18ad0a00206a0114eedb-ffa24f1afaab12f00a00206a01a6673d-en-US>`_
                """
                _cmd = "PORTs"
                
            class PPORt(SCPINodeN):
                """
                SOURce:GROup:PPORt
                """
                _cmd = "PPORt"
                
                class DPORt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:GROup:PPORt:DPORt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ca2c99de38a3435c.htm#ID_f929baf84f3008010a001ae7392085da-ccb6ff8f4f30065b0a001ae7211c9327-en-US>`_
                    """
                    _cmd = "DPORt"
                    
            class PPORts(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:GROup:PPORts
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/64383fd17c2f4ab3.htm#ID_103793c84f300aef0a001ae70a6fae59-1dd2cbc84f93c6540a001ae7068aeca9-en-US>`_
                """
                _cmd = "PPORts"
                
            class SIMultaneous(SCPINode):
                """
                SOURce:GROup:SIMultaneous
                """
                _cmd = "SIMultaneous"
                
                class FOFFset(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:GROup:SIMultaneous:FOFFset
                    """
                    _cmd = "FOFFset"
                    
                    class CONDition(SCPINode, SCPIQuery):
                        """
                        `SOURce:GROup:SIMultaneous:FOFFset:CONDition
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1b6cecbf09ac48a2.htm#ID_6677f2c5f72899280a001ae7416d538d-ddecae76f72897730a001ae743c5d16b-en-US>`_
                        """
                        _cmd = "CONDition"
                        
                    class MOFFset(SCPINode):
                        """
                        SOURce:GROup:SIMultaneous:FOFFset:MOFFset
                        """
                        _cmd = "MOFFset"
                        
                        class BWFactor(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:BWFactor
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ce7864aa9d144bfd.htm#ID_5d682b89f7289c160a001ae74facad20-13412b41f7289a130a001ae743c5d16b-en-US>`_
                            """
                            _cmd = "BWFactor"
                            
                        class DVALue(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:DVALue
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c51184c526f44c54.htm#ID_90c896a2f7289ec60a001ae70134d207-eeacc11bf7289cd20a001ae743c5d16b-en-US>`_
                            """
                            _cmd = "DVALue"
                            
                        class MODE(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:MODE
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2645ca2926bf4b9d.htm#ID_e1280075f728a29e0a001ae70b3b58c9-ddf54056f7289ffe0a001ae743c5d16b-en-US>`_
                            """
                            _cmd = "MODE"
                            
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:GROup:SIMultaneous:FOFFset:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2878dd518aae4b66.htm#ID_8e29ec05f728a6a50a001ae76efa6673-4d24d4f7f728a3e60a001ae743c5d16b-en-US>`_
                        """
                        _cmd = "STATe"
                        
        class LPORt(SCPINodeN, SCPIQuery, SCPISet):
            """
            `SOURce:LPORt
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/49f764b18ad748ff.htm#ID_45afb15efaab202f0a00206a00ad1683-d5ab93aafaab1a910a00206a01a6673d-en-US>`_
            """
            _cmd = "LPORt"
            
            class CLEar(SCPINode, SCPISet):
                """
                `SOURce:LPORt:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e2064f162cff4458.htm#ID_f7c17f6bfaab27a10a00206a00d8e015-8f1450e1faab22040a00206a01a6673d-en-US>`_
                """
                _cmd = "CLEar"
                
        class POWer(SCPINodeN, SCPIQuery, SCPISet):
            """
            SOURce:POWer
            """
            _cmd = "POWer"
            
            class ALC(SCPINode):
                """
                SOURce:POWer:ALC
                """
                _cmd = "ALC"
                
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:MODE
                    """
                    _cmd = "MODE"
                    
                class SVARiable(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:SVARiable
                    """
                    _cmd = "SVARiable"
                    
            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:ATTenuation
                """
                _cmd = "ATTenuation"
                
                class AUTO(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ATTenuation:AUTO
                    """
                    _cmd = "AUTO"
                    
            class CORRection(SCPINode, SCPISet):
                """
                SOURce:POWer:CORRection
                """
                _cmd = "CORRection"
                
                class ACQuire(SCPINode, SCPISet):
                    """
                    `SOURce:POWer:CORRection:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d611f3410d13473b.htm#ID_5975972bfaae5f3a0a00206a00433247-c9b39da2faae596e0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ACQuire"
                    
                    class VERification(SCPINode):
                        """
                        SOURce:POWer:CORRection:ACQuire:VERification
                        """
                        _cmd = "VERification"
                        
                        class RESult(SCPINode, SCPIQuery):
                            """
                            `SOURce:POWer:CORRection:ACQuire:VERification:RESult
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0467fd8923a74a33.htm#ID_10e7870afaae66ac0a00206a002942b3-138b97a9faae611f0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "RESult"
                            
                class COLLect(SCPINode, SCPISet):
                    """
                    SOURce:POWer:CORRection:COLLect
                    """
                    _cmd = "COLLect"
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/62891a00782d4b17.htm#ID_e8b93b83faadd71f0a00206a01d443f7-be19ecfffaadd1910a00206a01a6673d-en-US>`_
                        """
                        _cmd = "ACQuire"
                        
                        class VERification(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:CORRection:COLLect:ACQuire:VERification
                            """
                            _cmd = "VERification"
                            
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                """
                                SOURce:POWer:CORRection:COLLect:ACQuire:VERification:STATe
                                """
                                _cmd = "STATe"
                                
                    class AVERage(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CORRection:COLLect:AVERage
                        """
                        _cmd = "AVERage"
                        
                        class COUNt(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:COLLect:AVERage:COUNt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f67677c7002d4509.htm#ID_bf5b43d3faadaa520a00206a01a628d2-72b9973ffaada4b50a00206a01a6673d-en-US>`_
                            """
                            _cmd = "COUNt"
                            
                        class NTOLerance(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:COLLect:AVERage:NTOLerance
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/84fccbafdbda4d27.htm#ID_d92c259efaada2e00a00206a00f34412-cabca395faad9d430a00206a01a6673d-en-US>`_
                            """
                            _cmd = "NTOLerance"
                            
                    class CFACtor(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:CFACtor
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bd429ac245854fce.htm#ID_68824478faadb1d40a00206a00475d07-e8b2b329faadac370a00206a01a6673d-en-US>`_
                        """
                        _cmd = "CFACtor"
                        
                    class FLATness(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CORRection:COLLect:FLATness
                        """
                        _cmd = "FLATness"
                        
                    class METHod(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CORRection:COLLect:METHod
                        """
                        _cmd = "METHod"
                        
                    class PMReadings(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:PMReadings
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b2f7fc620d5b401a.htm#ID_aaa1f504faadc83a0a00206a00d10cf3-900c4040faadc28d0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "PMReadings"
                        
                    class RRECeiver(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CORRection:COLLect:RRECeiver
                        """
                        _cmd = "RRECeiver"
                        
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/25fbcbae02e24593.htm#ID_b9bdd113faade6230a00206a0169b185-c18fca3afaade0660a00206a01a6673d-en-US>`_
                    """
                    _cmd = "DATA"
                    
                    class PARameter(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:DATA:PARameter
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5e0229cc7b574769.htm#ID_8e7c1329e2b4ffc60a002019006b50ba-25446696e2b4fe8d0a002019017b841c-en-US>`_
                        """
                        _cmd = "PARameter"
                        
                        class COUNt(SCPINode, SCPIQuery):
                            """
                            `SOURce:POWer:CORRection:DATA:PARameter:COUNt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0a721461bb424f11.htm#ID_09e9ca8be2b5015c0a00201900f8311e-9e62e375e2b500240a002019017b841c-en-US>`_
                            """
                            _cmd = "COUNt"
                            
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:DATA:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/25fbcbae02e24593.htm#ID_a272ee70351562700a00206a00303ef7-9a74021135155b2c0a00206a01f2dc17-en-US>`_
                        """
                        _cmd = "PORT"
                        
                class DEFault(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:CORRection:DEFault
                    """
                    _cmd = "DEFault"
                    
                class FAST(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:CORRection:FAST
                    """
                    _cmd = "FAST"
                    
                class GENerator(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:CORRection:GENerator
                    """
                    _cmd = "GENerator"
                    
                    class LEVel(SCPINode):
                        """
                        SOURce:POWer:CORRection:GENerator:LEVel
                        """
                        _cmd = "LEVel"
                        
                        class OFFSet(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:GENerator:LEVel:OFFSet
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0eb4b6bdcf0d4e21.htm#ID_abb96447faadfcd70a00206a018d0552-297bb390faadf6eb0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "OFFSet"
                            
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:GENerator:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e9de207841044de6.htm#ID_fa7913e6faae04490a00206a01792c96-0729a476faadfebb0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class HARMonic(SCPINode, SCPISet):
                    """
                    SOURce:POWer:CORRection:HARMonic
                    """
                    _cmd = "HARMonic"
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:HARMonic:ACQuire
                        """
                        _cmd = "ACQuire"
                        
                class IMODulation(SCPINode):
                    """
                    SOURce:POWer:CORRection:IMODulation
                    """
                    _cmd = "IMODulation"
                    
                    class LTONe(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:IMODulation:LTONe
                        """
                        _cmd = "LTONe"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:IMODulation:LTONe:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d3ff622b7a56411d.htm#ID_bb03f965faae136c0a00206a00c59a89-d9aa326efaae0da00a00206a01a6673d-en-US>`_
                            """
                            _cmd = "ACQuire"
                            
                    class PORT(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:IMODulation:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/41a0d5a57dba437b.htm#ID_2248f3c0bba91b3d0a00201900e05938-b5e967b0bba91a140a0020190170f726-en-US>`_
                        """
                        _cmd = "PORT"
                        
                    class UTONe(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:IMODulation:UTONe
                        """
                        _cmd = "UTONe"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:IMODulation:UTONe:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5d8d28cae0ee4ec7.htm#ID_4887b100faae1ade0a00206a01623c15-4f33d57bfaae15410a00206a01a6673d-en-US>`_
                            """
                            _cmd = "ACQuire"
                            
                class LEVel(SCPINode):
                    """
                    SOURce:POWer:CORRection:LEVel
                    """
                    _cmd = "LEVel"
                    
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:LEVel:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/25ace39a40ac49b1.htm#ID_00e3bf8afaae22800a00206a00b4aa09-059f33b0faae1cb30a00206a01a6673d-en-US>`_
                        """
                        _cmd = "OFFSet"
                        
                class MIXer(SCPINode):
                    """
                    SOURce:POWer:CORRection:MIXer
                    """
                    _cmd = "MIXer"
                    
                    class IF(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:MIXer:IF
                        """
                        _cmd = "IF"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            SOURce:POWer:CORRection:MIXer:IF:ACQuire
                            """
                            _cmd = "ACQuire"
                            
                    class LO(SCPINodeN, SCPISet):
                        """
                        SOURce:POWer:CORRection:MIXer:LO
                        """
                        _cmd = "LO"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            SOURce:POWer:CORRection:MIXer:LO:ACQuire
                            """
                            _cmd = "ACQuire"
                            
                    class RF(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:MIXer:RF
                        """
                        _cmd = "RF"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            SOURce:POWer:CORRection:MIXer:RF:ACQuire
                            """
                            _cmd = "ACQuire"
                            
                class NREadings(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:NREadings
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0ca09ffe643247a6.htm#ID_dec18885faae40580a00206a016a7cf9-b9a1534efaae3aca0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "NREadings"
                    
                class OSOurces(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:CORRection:OSOurces
                    """
                    _cmd = "OSOurces"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:OSOurces:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9d8512972ee64ae5.htm#ID_3b3d0ddbfaae47f90a00206a018e9655-fcf684aefaae424c0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class PMETer(SCPINode):
                    """
                    SOURce:POWer:CORRection:PMETer
                    """
                    _cmd = "PMETer"
                    
                    class ID(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:PMETer:ID
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e108877.htm#ID_718458d9faae4fd90a00206a014851d1-3e93700cfaae49ce0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "ID"
                        
                class PPOWer(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:PPOWer
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c5a8849efde0475a.htm#ID_b404743a3515a4a80a00206a014bce76-c8cda1ef351598740a00206a01f2dc17-en-US>`_
                    """
                    _cmd = "PPOWer"
                    
                class PSELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:PSELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/72023c98c65e447f.htm#ID_b7cb46713515b2e10a00206a00ab5074-98441fc73515aad30a00206a01f2dc17-en-US>`_
                    """
                    _cmd = "PSELect"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dec754a87b374b92.htm#ID_aba4178bfaae57890a00206a00e59888-88fe3b6afaae51dc0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
                class TCOefficient(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:CORRection:TCOefficient
                    """
                    _cmd = "TCOefficient"
                    
                    class CALibration(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:CALibration
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/082d754c7e824b9e.htm#ID_ae42fb54612b11db0a00206a0127a802-26ad09a8612b05480a00206a01ed2866-en-US>`_
                        """
                        _cmd = "CALibration"
                        
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:COUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7467446d7bc7431b.htm#ID_173a4efd612b22460a00206a00ef257c-74e014cb612b15360a00206a01ed2866-en-US>`_
                        """
                        _cmd = "COUNt"
                        
                    class DEFine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:DEFine
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/03d957429191480b.htm#ID_bda67605612b2f270a00206a01114ab4-aca50f20612b27470a00206a01ed2866-en-US>`_
                        """
                        _cmd = "DEFine"
                        
                    class DELete(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CORRection:TCOefficient:DELete
                        """
                        _cmd = "DELete"
                        
                        class ALL(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:TCOefficient:DELete:ALL
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cf97363339154f86.htm#ID_9ef00398612b3c850a00206a00866808-d704ff41612b32340a00206a01ed2866-en-US>`_
                            """
                            _cmd = "ALL"
                            
                        class DUMMy(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:TCOefficient:DELete:DUMMy
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2fbf785d99684f5f.htm#ID_f913fc5b612b483d0a00206a01410ab5-a060a1a1612b3ff00a00206a01ed2866-en-US>`_
                            """
                            _cmd = "DUMMy"
                            
                    class FEED(SCPINode, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:FEED
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7d96b4dfe19e4c9b.htm#ID_d8cc63b3612b525e0a00206a01d7a7c3-3305d9e8612b4a9e0a00206a01ed2866-en-US>`_
                        """
                        _cmd = "FEED"
                        
                    class INSert(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:INSert
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a7514edfae9d4a97.htm#ID_237311af612b5dd80a00206a003289ba-eeed4680612b558b0a00206a01ed2866-en-US>`_
                        """
                        _cmd = "INSert"
                        
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2cc602d287784c4e.htm#ID_8bd9cb78612b69510a00206a01eabac8-91600e8e612b60870a00206a01ed2866-en-US>`_
                        """
                        _cmd = "STATe"
                        
            class COUPle(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:COUPle
                """
                _cmd = "COUPle"
                
            class GENerator(SCPINodeN):
                """
                SOURce:POWer:GENerator
                """
                _cmd = "GENerator"
                
                class LLIMit(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:GENerator:LLIMit
                    """
                    _cmd = "LLIMit"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:GENerator:LLIMit:STATe
                        """
                        _cmd = "STATe"
                        
                    class VALue(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:GENerator:LLIMit:VALue
                        """
                        _cmd = "VALue"
                        
                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:GENerator:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bf9688b40fbb4ac9.htm#ID_117aa5bafaae857f0a00206a002f271a-e6a66decfaae7fb30a00206a01a6673d-en-US>`_
                    """
                    _cmd = "OFFSet"
                    
                class PERManent(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:GENerator:PERManent
                    """
                    _cmd = "PERManent"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:GENerator:PERManent:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/29150ecf191b40c9.htm#ID_11c0b55efaae8d9d0a00206a01b64dae-cda894d1faae87730a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:GENerator:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2b2ef3243ae24a58.htm#ID_0269c345faae950f0a00206a011daa70-fee7be52faae8f810a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:LEVel
                """
                _cmd = "LEVel"
                
                class IMMediate(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:LEVel:IMMediate
                    """
                    _cmd = "IMMediate"
                    
                    class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:AMPLitude
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cb0449cb743f4614.htm#ID_d19e984efaaef0ac0a00206a0031e7ac-96acb6e3faaeeb1e0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "AMPLitude"
                        
                    class LLIMit(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:LEVel:IMMediate:LLIMit
                        """
                        _cmd = "LLIMit"
                        
                        class DGRaccess(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:LEVel:IMMediate:LLIMit:DGRaccess
                            """
                            _cmd = "DGRaccess"
                            
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:LEVel:IMMediate:LLIMit:STATe
                            """
                            _cmd = "STATe"
                            
                        class VALue(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:LEVel:IMMediate:LLIMit:VALue
                            """
                            _cmd = "VALue"
                            
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d163782716654728.htm#ID_abfaa0e1faaed2b40a00206a00aa2a79-e7e8f447faaeccd80a00206a01a6673d-en-US>`_
                        """
                        _cmd = "OFFSet"
                        
                    class SLOPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:SLOPe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6a3b406f0df84e3b.htm#ID_d01551b2faaee1b80a00206a0027f573-f0a6fd8cfaaedc2a0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "SLOPe"
                        
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:LEVel:IMMediate:SLOPe:STATe
                            """
                            _cmd = "STATe"
                            
            class PERManent(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:PERManent
                """
                _cmd = "PERManent"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:PERManent:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4a52786e213a4377.htm#ID_33dd3b36faae9cc00a00206a01124b41-a709680bfaae97030a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class REDuce(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:REDuce
                """
                _cmd = "REDuce"
                
                class SDELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:REDuce:SDELay
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/76c24730662a4cc6.htm#ID_ad5bec09b7ffa5770a001ae7253f904c-2ad64f47b7ffa42e0a001ae732f546b3-en-US>`_
                    """
                    _cmd = "SDELay"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:REDuce:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/390210369fef483e.htm#ID_da2ac181b7ffa7990a001ae722723f79-9010cb6db7ffa6420a001ae732f546b3-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:STARt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2facbd33341b4107.htm#ID_4899138ffaaea4800a00206a01efb643-73d350bafaae9ea40a00206a01a6673d-en-US>`_
                """
                _cmd = "STARt"
                
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/64db3d3b774d43db.htm#ID_628e8e9bfaaeac210a00206a00f0e1b9-ac3408ddfaaea6550a00206a01a6673d-en-US>`_
                """
                _cmd = "STATe"
                
            class STOP(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:STOP
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2facbd33341b4107.htm#ID_f96cb7dbfaaeb4110a00206a01447348-2719bf89faaeae150a00206a01a6673d-en-US>`_
                """
                _cmd = "STOP"
                
        class TDIF(SCPINode):
            """
            SOURce:TDIF
            """
            _cmd = "TDIF"
            
            class WAVes(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:TDIF:WAVes
                """
                _cmd = "WAVes"
                
    class STATus(SCPINode):
        """
        STATus
        """
        _cmd = "STATus"
        
        class OPERation(SCPINode, SCPIQuery, SCPISet):
            """
            STATus:OPERation
            """
            _cmd = "OPERation"
            
            class CONDition(SCPINode, SCPIQuery):
                """
                STATus:OPERation:CONDition
                """
                _cmd = "CONDition"
                
            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:ENABle
                """
                _cmd = "ENABle"
                
            class EVENt(SCPINode, SCPIQuery):
                """
                STATus:OPERation:EVENt
                """
                _cmd = "EVENt"
                
            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:NTRansition
                """
                _cmd = "NTRansition"
                
            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:PTRansition
                """
                _cmd = "PTRansition"
                
        class PRESet(SCPINode, SCPISet):
            """
            `STATus:PRESet
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e110863.htm#ID_14990f1cfaaf5cf30a00206a01af2d38-6dc6fe51faaf57740a00206a01a6673d-en-US>`_
            """
            _cmd = "PRESet"
            
        class QUEStionable(SCPINode, SCPIQuery, SCPISet):
            """
            STATus:QUEStionable
            """
            _cmd = "QUEStionable"
            
            class CONDition(SCPINode, SCPIQuery):
                """
                `STATus:QUEStionable:CONDition
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/acf0533fb1e4434e.htm#ID_ec46ac9afaaf64a30a00206a00c8bf13-aaf5fdf0faaf5ef60a00206a01a6673d-en-US>`_
                """
                _cmd = "CONDition"
                
            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:ENABle
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/165d9083d7514744.htm#ID_cb2fe2bcfaaf6c250a00206a002a52d7-12884f3ffaaf66880a00206a01a6673d-en-US>`_
                """
                _cmd = "ENABle"
                
            class EVENt(SCPINode, SCPIQuery):
                """
                `STATus:QUEStionable:EVENt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/edbdffb720be4c72.htm#ID_85f7b6b5faaff47f0a00206a00265edf-50127a48faafeed20a00206a01a6673d-en-US>`_
                """
                _cmd = "EVENt"
                
            class INTegrity(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:INTegrity
                """
                _cmd = "INTegrity"
                
                class CONDition(SCPINode, SCPIQuery):
                    """
                    `STATus:QUEStionable:INTegrity:CONDition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/acf0533fb1e4434e.htm#ID_0333fbe8faaf73a70a00206a013b59a3-26dc522ffaaf6e090a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CONDition"
                    
                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:ENABle
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/165d9083d7514744.htm#ID_3aabbef6faaf7b380a00206a01a6dac4-c217b852faaf757c0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ENABle"
                    
                class EVENt(SCPINode, SCPIQuery):
                    """
                    `STATus:QUEStionable:INTegrity:EVENt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/edbdffb720be4c72.htm#ID_4cda7716faafb7a50a00206a0059dcea-fe65ae3cfaafb1e80a00206a01a6673d-en-US>`_
                    """
                    _cmd = "EVENt"
                    
                class HARDware(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:INTegrity:HARDware
                    """
                    _cmd = "HARDware"
                    
                    class CONDition(SCPINode, SCPIQuery):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:CONDition
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/acf0533fb1e4434e.htm#ID_31ec8179faaf82ab0a00206a01399c5a-48b257acfaaf7d1d0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "CONDition"
                        
                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:ENABle
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/165d9083d7514744.htm#ID_e278e1cafaaf8a4c0a00206a00eea680-6bd338a7faaf847f0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "ENABle"
                        
                    class EVENt(SCPINode, SCPIQuery):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:EVENt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/edbdffb720be4c72.htm#ID_7c9f00d6faafa0d10a00206a017c8e51-d642c8f9faaf9b530a00206a01a6673d-en-US>`_
                        """
                        _cmd = "EVENt"
                        
                    class NTRansition(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:NTRansition
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8b6b137e86d7462f.htm#ID_2a6cb24efaaf91ce0a00206a001b46d6-3974f3f9faaf8c200a00206a01a6673d-en-US>`_
                        """
                        _cmd = "NTRansition"
                        
                    class PTRansition(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:PTRansition
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1bf60bca7cd4485b.htm#ID_00ec2fb7faaf996f0a00206a00babf2b-227ed9b6faaf93a20a00206a01a6673d-en-US>`_
                        """
                        _cmd = "PTRansition"
                        
                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:NTRansition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8b6b137e86d7462f.htm#ID_4838dc31faafa8920a00206a013b68fd-a0b93b62faafa2d50a00206a01a6673d-en-US>`_
                    """
                    _cmd = "NTRansition"
                    
                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:PTRansition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1bf60bca7cd4485b.htm#ID_34bab32dfaafb0040a00206a01d13a50-6dab1c20faafaa760a00206a01a6673d-en-US>`_
                    """
                    _cmd = "PTRansition"
                    
            class LIMit(SCPINodeN, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:LIMit
                """
                _cmd = "LIMit"
                
                class CONDition(SCPINode, SCPIQuery):
                    """
                    `STATus:QUEStionable:LIMit:CONDition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/acf0533fb1e4434e.htm#ID_9ce66863faafbf460a00206a018efcc8-ad923fe4faafb97a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CONDition"
                    
                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:LIMit:ENABle
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/165d9083d7514744.htm#ID_ad66516bfaafc6d80a00206a0177398d-8207f46ffaafc13a0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ENABle"
                    
                class EVENt(SCPINode, SCPIQuery):
                    """
                    `STATus:QUEStionable:LIMit:EVENt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/edbdffb720be4c72.htm#ID_f07789a5faafddda0a00206a0084664d-c2d70464faafd82d0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "EVENt"
                    
                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:LIMit:NTRansition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8b6b137e86d7462f.htm#ID_1f6cf0c8faafce690a00206a00e85b2c-52051c71faafc8bc0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "NTRansition"
                    
                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:LIMit:PTRansition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1bf60bca7cd4485b.htm#ID_5f3a5c1dfaafd60a0a00206a00b66faf-afc7fac9faafd04d0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "PTRansition"
                    
            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:NTRansition
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8b6b137e86d7462f.htm#ID_5f4b6776faafe57b0a00206a008aebef-2ecf6d87faafdfce0a00206a01a6673d-en-US>`_
                """
                _cmd = "NTRansition"
                
            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:PTRansition
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1bf60bca7cd4485b.htm#ID_135540eafaafecfd0a00206a009c969a-29d24063faafe7500a00206a01a6673d-en-US>`_
                """
                _cmd = "PTRansition"
                
        class QUEue(SCPINode, SCPIQuery, SCPISet):
            """
            STATus:QUEue
            """
            _cmd = "QUEue"
            
            class NEXT(SCPINode, SCPIQuery):
                """
                `STATus:QUEue:NEXT
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e111637.htm#ID_3d4f47acfaaffc300a00206a0013451f-0611f439faaff6630a00206a01a6673d-en-US>`_
                """
                _cmd = "NEXT"
                
    class SYSTem(SCPINode):
        """
        SYSTem
        """
        _cmd = "SYSTem"
        
        class COMMunicate(SCPINode):
            """
            SYSTem:COMMunicate
            """
            _cmd = "COMMunicate"
            
            class AKAL(SCPINode):
                """
                SYSTem:COMMunicate:AKAL
                """
                _cmd = "AKAL"
                
                class CONNection(SCPINode, SCPISet):
                    """
                    `SYSTem:COMMunicate:AKAL:CONNection
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e111688.htm#ID_b6e9a9a2fab003a20a00206a016cc0b8-27c8d699faaffe040a00206a01a6673d-en-US>`_
                    """
                    _cmd = "CONNection"
                    
                class MMEMory(SCPINode, SCPISet):
                    """
                    SYSTem:COMMunicate:AKAL:MMEMory
                    """
                    _cmd = "MMEMory"
                    
                    class STATe(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:AKAL:MMEMory:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e111734.htm#ID_34916594fab00b430a00206a0082898c-7dad1344fab005860a00206a01a6673d-en-US>`_
                        """
                        _cmd = "STATe"
                        
            class CODec(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:COMMunicate:CODec
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1052114e59e64095.htm#ID_696257e66f679a250a001ae70ec75580-d27074166f6798ae0a001ae727f5f310-en-US>`_
                """
                _cmd = "CODec"
                
            class GPIB(SCPINode):
                """
                SYSTem:COMMunicate:GPIB
                """
                _cmd = "GPIB"
                
                class SELF(SCPINode):
                    """
                    SYSTem:COMMunicate:GPIB:SELF
                    """
                    _cmd = "SELF"
                    
                    class ADDRess(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:GPIB:SELF:ADDRess
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b3ba68fb72ee42d8.htm#ID_61513521fab012e40a00206a01da716c-2ddf570ffab00d270a00206a01a6673d-en-US>`_
                        """
                        _cmd = "ADDRess"
                        
                    class INIT(SCPINode):
                        """
                        SYSTem:COMMunicate:GPIB:SELF:INIT
                        """
                        _cmd = "INIT"
                        
                        class WAIT(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:GPIB:SELF:INIT:WAIT
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/14a624620e7d44ab.htm#ID_68a7116fbe5215800a001ae738b88c4c-9d13e972be5213fa0a001ae76004eba8-en-US>`_
                            """
                            _cmd = "WAIT"
                            
                    class LPORt(SCPINode):
                        """
                        SYSTem:COMMunicate:GPIB:SELF:LPORt
                        """
                        _cmd = "LPORt"
                        
                        class ALIGn(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:GPIB:SELF:LPORt:ALIGn
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1fec17069a1a42e4.htm#ID_83ec9beebe5217a30a001ae728c4b621-64202eadbe52160d0a001ae76004eba8-en-US>`_
                            """
                            _cmd = "ALIGn"
                            
                    class RTERminator(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:GPIB:SELF:RTERminator
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e111918.htm#ID_ea61ddf3fab01a660a00206a01bf8be0-c5397efffab014c80a00206a01a6673d-en-US>`_
                        """
                        _cmd = "RTERminator"
                        
            class INTernal(SCPINode):
                """
                SYSTem:COMMunicate:INTernal
                """
                _cmd = "INTernal"
                
                class COMMand(SCPINode):
                    """
                    SYSTem:COMMunicate:INTernal:COMMand
                    """
                    _cmd = "COMMand"
                    
                    class TABLes(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:INTernal:COMMand:TABLes
                        """
                        _cmd = "TABLes"
                        
                class REMote(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:INTernal:REMote
                    """
                    _cmd = "REMote"
                    
            class NET(SCPINode):
                """
                SYSTem:COMMunicate:NET
                """
                _cmd = "NET"
                
                class HOSTname(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:NET:HOSTname
                    """
                    _cmd = "HOSTname"
                    
            class RDEVice(SCPINode):
                """
                SYSTem:COMMunicate:RDEVice
                """
                _cmd = "RDEVice"
                
                class AKAL(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:AKAL
                    """
                    _cmd = "AKAL"
                    
                    class ADDRess(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:ADDRess
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/7a0adfab1a314193.htm#ID_38ecc45ffab031490a00206a01f30588-bafade31fab02b9c0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "ADDRess"
                        
                        class ALL(SCPINode, SCPIQuery):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:ADDRess:ALL
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e111996.htm#ID_12b46c80fab038fa0a00206a00cf3f89-d294ec5bfab0332e0a00206a01a6673d-en-US>`_
                            """
                            _cmd = "ALL"
                            
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:CATalog
                        """
                        _cmd = "CATalog"
                        
                    class CKIT(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:CKIT
                        """
                        _cmd = "CKIT"
                        
                        class CATalog(SCPINode, SCPIQuery):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:CKIT:CATalog
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/321d1d0427e343bf.htm#ID_e2b55a2491e0e9db0a00206a00224e9a-50e93f0f91e0dc6d0a00206a00e9ecac-en-US>`_
                            """
                            _cmd = "CATalog"
                            
                        class STANdard(SCPINode):
                            """
                            SYSTem:COMMunicate:RDEVice:AKAL:CKIT:STANdard
                            """
                            _cmd = "STANdard"
                            
                            class CATalog(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SYSTem:COMMunicate:RDEVice:AKAL:CKIT:STANdard:CATalog
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/86aba03e3ec94134.htm#ID_ed1982c535163ef40a00206a01459e8b-5354b0a4351637530a00206a01f2dc17-en-US>`_
                                """
                                _cmd = "CATalog"
                                
                    class CONFigure(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:CONFigure
                        """
                        _cmd = "CONFigure"
                        
                        class AUTO(SCPINode, SCPIQuery, SCPISet):
                            """
                            SYSTem:COMMunicate:RDEVice:AKAL:CONFigure:AUTO
                            """
                            _cmd = "AUTO"
                            
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                """
                                SYSTem:COMMunicate:RDEVice:AKAL:CONFigure:AUTO:STATe
                                """
                                _cmd = "STATe"
                                
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:COUNt
                        """
                        _cmd = "COUNt"
                        
                    class DATE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:DATE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/26a325509010424f.htm#ID_0a954ea791e0f9b90a00206a01b9cb3d-092c4e9f91e0f14d0a00206a00e9ecac-en-US>`_
                        """
                        _cmd = "DATE"
                        
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:DEFine
                        """
                        _cmd = "DEFine"
                        
                    class DELete(SCPINode, SCPISet):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:DELete
                        """
                        _cmd = "DELete"
                        
                    class FRANge(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:FRANge
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2fe4d725e67f40c2.htm#ID_227c868091e1035e0a00206a00808933-f810ee9a91e0fc4a0a00206a00e9ecac-en-US>`_
                        """
                        _cmd = "FRANge"
                        
                    class PORTs(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:PORTs
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5257accae9324f22.htm#ID_9298113091e10ee70a00206a01d92f21-f852f2d391e105b00a00206a00e9ecac-en-US>`_
                        """
                        _cmd = "PORTs"
                        
                    class PREDuction(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:PREDuction
                        """
                        _cmd = "PREDuction"
                        
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:PREDuction:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e112247.htm#ID_79a5e788e15d18260a00206a0144c9a6-aa8db572e15d11020a00206a00796295-en-US>`_
                            """
                            _cmd = "STATe"
                            
                    class SDATa(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:SDATa
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/bedef83f5a58483f.htm#ID_8962fa362b9c026c0a00206a01432b9a-c7df0c252b9bfb280a00206a0020d3a0-en-US>`_
                        """
                        _cmd = "SDATa"
                        
                    class WARMup(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:WARMup
                        """
                        _cmd = "WARMup"
                        
                        class STATe(SCPINode, SCPIQuery):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:WARMup:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e112365.htm#ID_276e3c1791e11bb80a00206a01ac5dc5-a50c9ce891e1132d0a00206a00e9ecac-en-US>`_
                            """
                            _cmd = "STATe"
                            
                class GENerator(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:GENerator
                    """
                    _cmd = "GENerator"
                    
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:CATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0aec52e1cf544e09.htm#ID_632db67afab04fbe0a00206a01429d80-e640b520fab04a200a00206a01a6673d-en-US>`_
                        """
                        _cmd = "CATalog"
                        
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:COUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e112446.htm#ID_3b5eb98efab0578e0a00206a017a57f7-77203d8ffab051d10a00206a01a6673d-en-US>`_
                        """
                        _cmd = "COUNt"
                        
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:DEFine
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8142ad99eab840e8.htm#ID_00159b1efab05f1f0a00206a01cbbccc-ec8148fbfab059820a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DEFine"
                        
                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:DELete
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e112396.htm#ID_96c9fc01fab066ff0a00206a00727635-ee59ffa2fab061620a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DELete"
                        
                    class SEPMode(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:SEPMode
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a02e1397662d4b37.htm#ID_e2afc1d3e15d34390a00206a01d9fc25-db7b4172e15d2c980a00206a00796295-en-US>`_
                        """
                        _cmd = "SEPMode"
                        
                    class SEPower(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:SEPower
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/1fea9e339d68455f.htm#ID_33d0b7dde15d40ad0a00206a017d2253-032c215fe15d37560a00206a00796295-en-US>`_
                        """
                        _cmd = "SEPower"
                        
                class PMETer(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:PMETer
                    """
                    _cmd = "PMETer"
                    
                    class AZERo(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:AZERo
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/b47f04ba45f847b5.htm#ID_96b8e93efab06e710a00206a00ed7fa9-634f7de2fab068e30a00206a01a6673d-en-US>`_
                        """
                        _cmd = "AZERo"
                        
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:CATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4a3fa363c3e44dda.htm#ID_11d8c23afab075f30a00206a007d910e-eda7f0a9fab070560a00206a01a6673d-en-US>`_
                        """
                        _cmd = "CATalog"
                        
                    class CONFigure(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:PMETer:CONFigure
                        """
                        _cmd = "CONFigure"
                        
                        class AUTO(SCPINode, SCPIQuery, SCPISet):
                            """
                            SYSTem:COMMunicate:RDEVice:PMETer:CONFigure:AUTO
                            """
                            _cmd = "AUTO"
                            
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SYSTem:COMMunicate:RDEVice:PMETer:CONFigure:AUTO:STATe
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/5c3b3eaf608c4732.htm#ID_42018499fab07d850a00206a006d6b96-ccc5bc80fab077d70a00206a01a6673d-en-US>`_
                                """
                                _cmd = "STATe"
                                
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:COUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e112810.htm#ID_86a7eabafab085350a00206a00f99a37-d17da2c6fab07f690a00206a01a6673d-en-US>`_
                        """
                        _cmd = "COUNt"
                        
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:DEFine
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/84bc325dc8a24407.htm#ID_f257effbfab08d050a00206a01c0972c-3e7d50f1fab0871a0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DEFine"
                        
                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:DELete
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e112728.htm#ID_163a5ca7fab094870a00206a00ff0043-f41c5122fab08eea0a00206a01a6673d-en-US>`_
                        """
                        _cmd = "DELete"
                        
                    class SPCorrection(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:RDEVice:PMETer:SPCorrection
                        """
                        _cmd = "SPCorrection"
                        
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:PMETer:SPCorrection:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/abc28ee8793c4707.htm#ID_c30269e6e2b52a410a0020190063b2f1-4d844fb7e2b529080a002019017b841c-en-US>`_
                            """
                            _cmd = "STATe"
                            
                class SMATrix(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:SMATrix
                    """
                    _cmd = "SMATrix"
                    
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:SMATrix:CATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/78b19041e1da4d8c.htm#ID_c527b777e2b52c160a002019003c8932-17f21d0de2b52aae0a002019017b841c-en-US>`_
                        """
                        _cmd = "CATalog"
                        
                    class COMMand(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:RDEVice:SMATrix:COMMand
                        """
                        _cmd = "COMMand"
                        
                    class CONFigure(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure
                        """
                        _cmd = "CONFigure"
                        
                        class ABORt(SCPINode, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:ABORt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d864d14525904f3c.htm#ID_5af1ecc5e2b52f810a00201900488d61-917bd8cbe2b52e390a002019017b841c-en-US>`_
                            """
                            _cmd = "ABORt"
                            
                        class END(SCPINode, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:END
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4ef25b4306be4226.htm#ID_2a271d6ee2b531460a002019017a6c38-50ea7940e2b52fee0a002019017b841c-en-US>`_
                            """
                            _cmd = "END"
                            
                        class MLTest(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:MLTest
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/35615f2b64f146bc.htm#ID_bab31821e2b534a10a00201900a1c622-7726b90fe2b533780a002019017b841c-en-US>`_
                            """
                            _cmd = "MLTest"
                            
                        class MLVNa(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:MLVNa
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/424e6d88914a4f4d.htm#ID_9d5ed720e2b536470a002019014fc067-cea1e85ce2b5350f0a002019017b841c-en-US>`_
                            """
                            _cmd = "MLVNa"
                            
                        class MTESt(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:MTESt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e113481.htm#ID_02dd88c3e2b5384b0a00201900a1ec16-5e68904ee2b537120a002019017b841c-en-US>`_
                            """
                            _cmd = "MTESt"
                            
                        class MVNA(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:MVNA
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e113346.htm#ID_2e3b266be2b53a2f0a002019002c349a-fcb7090be2b538c80a002019017b841c-en-US>`_
                            """
                            _cmd = "MVNA"
                            
                        class STARt(SCPINode, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:STARt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/fe47c0c30d1347f2.htm#ID_d606c1c2e2b53c620a002019016d84ea-1085e87be2b53adb0a002019017b841c-en-US>`_
                            """
                            _cmd = "STARt"
                            
                        class TVNA(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:TVNA
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/dba8b46d76e64fa2.htm#ID_2e9f6208e2b53e170a002019008d85be-1778be60e2b53ccf0a002019017b841c-en-US>`_
                            """
                            _cmd = "TVNA"
                            
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:SMATrix:COUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/0a53245cd6704fd1.htm#ID_54a467ace2b53fad0a0020190120e772-95630382e2b53e840a002019017b841c-en-US>`_
                        """
                        _cmd = "COUNt"
                        
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:SMATrix:DEFine
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/01e5d99f805e431f.htm#ID_7496e554e2b541820a00201900a038ef-bbd862bae2b5402a0a002019017b841c-en-US>`_
                        """
                        _cmd = "DEFine"
                        
                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:SMATrix:DELete
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2f34ce5940394635.htm#ID_78fa76a8e2b543380a00201900eaad26-32d0ac12e2b541ef0a002019017b841c-en-US>`_
                        """
                        _cmd = "DELete"
                        
                    class RELays(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:SMATrix:RELays
                        """
                        _cmd = "RELays"
                        
                        class SWITch(SCPINode):
                            """
                            SYSTem:COMMunicate:RDEVice:SMATrix:RELays:SWITch
                            """
                            _cmd = "SWITch"
                            
                            class COUNt(SCPINode, SCPIQuery):
                                """
                                `SYSTem:COMMunicate:RDEVice:SMATrix:RELays:SWITch:COUNt
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/203db75605364802.htm#ID_8464a0fa842f0b490a00201901538ecb-ed9ae3ce842f09c20a00201901936165-en-US>`_
                                """
                                _cmd = "COUNt"
                                
            class TCPip(SCPINode):
                """
                SYSTem:COMMunicate:TCPip
                """
                _cmd = "TCPip"
                
                class CONTrol(SCPINode, SCPIQuery):
                    """
                    SYSTem:COMMunicate:TCPip:CONTrol
                    """
                    _cmd = "CONTrol"
                    
        class CORRection(SCPINode):
            """
            SYSTem:CORRection
            """
            _cmd = "CORRection"
            
            class FMPort(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:CORRection:FMPort
                """
                _cmd = "FMPort"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:CORRection:FMPort:STATe
                    """
                    _cmd = "STATe"
                    
        class DATE(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:DATE
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/06074416ad144635.htm#ID_a847a1ebaaa8d6ac0a00206a006756f9-9b65deafaaa8cad50a00206a00dee6b8-en-US>`_
            """
            _cmd = "DATE"
            
        class DFPRint(SCPINode, SCPIQuery):
            """
            `SYSTem:DFPRint
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/16c0aaa4259448db.htm#ID_cae179f213575a160a00206a0180be6e-87f88bf6135754690a00206a0182dc26-en-US>`_
            """
            _cmd = "DFPRint"
            
        class DISPlay(SCPINode):
            """
            SYSTem:DISPlay
            """
            _cmd = "DISPlay"
            
            class BAR(SCPINode):
                """
                SYSTem:DISPlay:BAR
                """
                _cmd = "BAR"
                
                class HKEY(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:DISPlay:BAR:HKEY
                    """
                    _cmd = "HKEY"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:DISPlay:BAR:HKEY:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/04735c08c458471b.htm#ID_04b780c5a07057500a00206a010feb2c-f9cca7aaa070500c0a00206a013722ca-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class MENU(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:DISPlay:BAR:MENU
                    """
                    _cmd = "MENU"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:DISPlay:BAR:MENU:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/04735c08c458471b.htm#ID_c7815f5ba07065d60a00206a01fcd35f-cee278d3a0705a1e0a00206a013722ca-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class STATus(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:DISPlay:BAR:STATus
                    """
                    _cmd = "STATus"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:DISPlay:BAR:STATus:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/04735c08c458471b.htm#ID_7ceb2976a0706fc90a00206a01a03f62-0474fa26a07068960a00206a013722ca-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class STOols(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:DISPlay:BAR:STOols
                    """
                    _cmd = "STOols"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:DISPlay:BAR:STOols:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/04735c08c458471b.htm#ID_29ae8142a0707a0a0a00206a018e633e-0c0c26d3a070725a0a00206a013722ca-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class TITLe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:DISPlay:BAR:TITLe
                    """
                    _cmd = "TITLe"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:DISPlay:BAR:TITLe:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/04735c08c458471b.htm#ID_8e3e8248a07084c80a00206a014856cb-58386f94a0707ce90a00206a013722ca-en-US>`_
                        """
                        _cmd = "STATe"
                        
                class TOOLs(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:DISPlay:BAR:TOOLs
                    """
                    _cmd = "TOOLs"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:DISPlay:BAR:TOOLs:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/04735c08c458471b.htm#ID_a45a5f24a0708fa60a00206a01841c0e-84805c29a07087780a00206a013722ca-en-US>`_
                        """
                        _cmd = "STATe"
                        
            class COLor(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:DISPlay:COLor
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114012.htm#ID_21c088fffab0b33a0a00206a01c816e7-d31ab677fab0ad9d0a00206a01a6673d-en-US>`_
                """
                _cmd = "COLor"
                
            class CONDuctances(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:DISPlay:CONDuctances
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/47c43a4d53b54002.htm#ID_d2271c9397ea6f290a001ae77f4a7568-33a77b2097ea6de10a001ae760f7f904-en-US>`_
                """
                _cmd = "CONDuctances"
                
            class DIALogs(SCPINode):
                """
                SYSTem:DISPlay:DIALogs
                """
                _cmd = "DIALogs"
                
                class SETup(SCPINode):
                    """
                    SYSTem:DISPlay:DIALogs:SETup
                    """
                    _cmd = "SETup"
                    
                    class MCAL(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:DISPlay:DIALogs:SETup:MCAL
                        """
                        _cmd = "MCAL"
                        
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:DISPlay:DIALogs:SETup:MCAL:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/52e327a6f3ea4d29.htm#ID_617f4b3de2b548580a00201900ff0001-63b39231e2b547100a002019017b841c-en-US>`_
                            """
                            _cmd = "STATe"
                            
            class UPDate(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:DISPlay:UPDate
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114067.htm#ID_4f17f97cfab0badb0a00206a019d73b8-482f9258fab0b53e0a00206a01a6673d-en-US>`_
                """
                _cmd = "UPDate"
                
        class ERRor(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:ERRor
            """
            _cmd = "ERRor"
            
            class ALL(SCPINode, SCPIQuery):
                """
                `SYSTem:ERRor:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114109.htm#ID_3bd07848fab0c23e0a00206a01bf19dc-2c14d208fab0bcb00a00206a01a6673d-en-US>`_
                """
                _cmd = "ALL"
                
            class DISPlay(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:ERRor:DISPlay
                """
                _cmd = "DISPlay"
                
                class ERRor(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:ERRor:DISPlay:ERRor
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/089aa3644bc14e4a.htm#ID_a304d0093535fd6c0a001ae77611c020-d87f519f3535fbd50a001ae72ac1dc63-en-US>`_
                    """
                    _cmd = "ERRor"
                    
                class INFO(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:ERRor:DISPlay:INFO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/089aa3644bc14e4a.htm#ID_eb5520e93535ffdd0a001ae76a65fef0-e504a00a3535fe270a001ae72ac1dc63-en-US>`_
                    """
                    _cmd = "INFO"
                    
                class REMote(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:ERRor:DISPlay:REMote
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/8bb7290d8cb44f14.htm#ID_b06832b2fab0c9c00a00206a00b9f04a-04495e7ffab0c4220a00206a01a6673d-en-US>`_
                    """
                    _cmd = "REMote"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:ERRor:DISPlay:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/4531bcee03ac438e.htm#ID_da0c4734353604800a001ae72d74b408-99f5ef9e353603090a001ae72ac1dc63-en-US>`_
                    """
                    _cmd = "STATe"
                    
                class WARNings(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:ERRor:DISPlay:WARNings
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/089aa3644bc14e4a.htm#ID_d2602e9d353607010a001ae7089ac033-8bb3971d3536055b0a001ae72ac1dc63-en-US>`_
                    """
                    _cmd = "WARNings"
                    
            class NEXT(SCPINode, SCPIQuery):
                """
                `SYSTem:ERRor:NEXT
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114305.htm#ID_7655f04ffab0d1510a00206a00680a86-25be5834fab0cbb40a00206a01a6673d-en-US>`_
                """
                _cmd = "NEXT"
                
        class FIRMware(SCPINode):
            """
            SYSTem:FIRMware
            """
            _cmd = "FIRMware"
            
            class UPDate(SCPINode, SCPISet):
                """
                `SYSTem:FIRMware:UPDate
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114332.htm#ID_0bcb7667fab0d8d30a00206a00b6a20a-9fd656e1fab0d3360a00206a01a6673d-en-US>`_
                """
                _cmd = "UPDate"
                
        class FPReset(SCPINode, SCPISet):
            """
            `SYSTem:FPReset
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114364.htm#ID_f22e24cafab0e0650a00206a00d64c6a-b86b5b25fab0dab80a00206a01a6673d-en-US>`_
            """
            _cmd = "FPReset"
            
        class FREQuency(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:FREQuency
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114386.htm#ID_1a39d97dfab0e7f60a00206a018a7f6e-2fc01ddafab0e2390a00206a01a6673d-en-US>`_
            """
            _cmd = "FREQuency"
            
        class IDENtify(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:IDENtify
            """
            _cmd = "IDENtify"
            
            class FACTory(SCPINode, SCPISet):
                """
                `SYSTem:IDENtify:FACTory
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114437.htm#ID_c1695db591e160a10a00206a00cd77f5-e99d3c9c91e158440a00206a00e9ecac-en-US>`_
                """
                _cmd = "FACTory"
                
            class STRing(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:IDENtify:STRing
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114465.htm#ID_437487be91e16d910a00206a003f7503-85833b1a91e164a80a00206a00e9ecac-en-US>`_
                """
                _cmd = "STRing"
                
        class INFO(SCPINode):
            """
            SYSTem:INFO
            """
            _cmd = "INFO"
            
            class CONTrast(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:INFO:CONTrast
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e4e198e6eab14f2c.htm#ID_961fc2d6842f14130a00201900e72704-c596e387842f12ab0a00201901936165-en-US>`_
                """
                _cmd = "CONTrast"
                
        class KLOCk(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:KLOCk
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114530.htm#ID_9346e83cfab0ef780a00206a01c95e16-25df267cfab0e9cb0a00206a01a6673d-en-US>`_
            """
            _cmd = "KLOCk"
            
        class LANGuage(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:LANGuage
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114559.htm#ID_869a87e0fab0f70a0a00206a0129131e-f2c4c937fab0f15c0a00206a01a6673d-en-US>`_
            """
            _cmd = "LANGuage"
            
        class LOGGing(SCPINode):
            """
            SYSTem:LOGGing
            """
            _cmd = "LOGGing"
            
            class REMote(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:LOGGing:REMote
                """
                _cmd = "REMote"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:LOGGing:REMote:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114608.htm#ID_2859a837fab0feab0a00206a0104b6ad-22b5a74ffab0f8ee0a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
        class NOPeration(SCPINode, SCPISet):
            """
            SYSTem:NOPeration
            """
            _cmd = "NOPeration"
            
        class OPTions(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:OPTions
            """
            _cmd = "OPTions"
            
            class DISable(SCPINode, SCPISet):
                """
                SYSTem:OPTions:DISable
                """
                _cmd = "DISable"
                
            class FACTory(SCPINode, SCPISet):
                """
                `SYSTem:OPTions:FACTory
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114648.htm#ID_efb9e44791e18d2f0a00206a01117c44-73da166c91e183f80a00206a00e9ecac-en-US>`_
                """
                _cmd = "FACTory"
                
            class STRing(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:OPTions:STRing
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114673.htm#ID_fcf476dc91e1979f0a00206a008bad5a-3055959091e18fdf0a00206a00e9ecac-en-US>`_
                """
                _cmd = "STRing"
                
        class PASSword(SCPINode, SCPISet):
            """
            SYSTem:PASSword
            """
            _cmd = "PASSword"
            
            class CENable(SCPINode, SCPISet):
                """
                `SYSTem:PASSword:CENable
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114750.htm#ID_5deccfb4fab1062c0a00206a015e85f5-4817c3fbfab1008f0a00206a01a6673d-en-US>`_
                """
                _cmd = "CENable"
                
        class PRESet(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:PRESet
            """
            _cmd = "PRESet"
            
            class DUMMy(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:PRESet:DUMMy
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114970.htm#ID_0ce589adfab124920a00206a01485f4a-3a5f7062fab11e960a00206a01a6673d-en-US>`_
                """
                _cmd = "DUMMy"
                
            class REMote(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:PRESet:REMote
                """
                _cmd = "REMote"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:PRESet:REMote:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9fcef3bb614f452b.htm#ID_9e274d9e581341e70a001ae771e5dcc6-f3df5f90581340700a001ae75f9ff217-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class SCOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:PRESet:SCOPe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114782.htm#ID_f14f0f4efab10d9f0a00206a00724e94-7cbf2c2dfab108110a00206a01a6673d-en-US>`_
                """
                _cmd = "SCOPe"
                
            class USER(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:PRESet:USER
                """
                _cmd = "USER"
                
                class CAL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:PRESet:USER:CAL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/f0cd6bd78b8a463c.htm#ID_929a0b5bac61eaa90a00201900cbe46b-37784b03ac61e99f0a0020190003471b-en-US>`_
                    """
                    _cmd = "CAL"
                    
                class NAME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:PRESet:USER:NAME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114826.htm#ID_9e06eeaefab115300a00206a00cb4ce5-0538d3bbfab10f830a00206a01a6673d-en-US>`_
                    """
                    _cmd = "NAME"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:PRESet:USER:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e114862.htm#ID_66b8f316fab11cc20a00206a0087213c-35caa738fab117050a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
        class PRIority(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:PRIority
            """
            _cmd = "PRIority"
            
        class SETTings(SCPINode):
            """
            SYSTem:SETTings
            """
            _cmd = "SETTings"
            
            class UPDate(SCPINode, SCPISet):
                """
                `SYSTem:SETTings:UPDate
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e115028.htm#ID_e5afdc76fab134220a00206a00902fa2-2837511dfab12e360a00206a01a6673d-en-US>`_
                """
                _cmd = "UPDate"
                
        class SHUTdown(SCPINode, SCPISet):
            """
            `SYSTem:SHUTdown
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/def2e5e153454147.htm#ID_19d5020713577b1b0a00206a019388f2-1efe305b1357755e0a00206a0182dc26-en-US>`_
            """
            _cmd = "SHUTdown"
            
        class SMATrix(SCPINode):
            """
            SYSTem:SMATrix
            """
            _cmd = "SMATrix"
            
            class OPTimization(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:SMATrix:OPTimization
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/6c0a61c173ee4de7.htm#ID_5e9bd4c9e2b551800a0020190004db0c-b8f06f0be2b550470a002019017b841c-en-US>`_
                """
                _cmd = "OPTimization"
                
        class SOUNd(SCPINode):
            """
            SYSTem:SOUNd
            """
            _cmd = "SOUNd"
            
            class ALARm(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:SOUNd:ALARm
                """
                _cmd = "ALARm"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:SOUNd:ALARm:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2a6409afa1604928.htm#ID_cf6e6360fab13bf20a00206a01a85018-52ea9190fab136060a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
            class STATus(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:SOUNd:STATus
                """
                _cmd = "STATus"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:SOUNd:STATus:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2a6409afa1604928.htm#ID_a23de053fab143740a00206a00e3a371-80e149c4fab13dd60a00206a01a6673d-en-US>`_
                    """
                    _cmd = "STATe"
                    
        class TIME(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:TIME
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/a7965f84d8ac4a09.htm#ID_c96fbd06aaa8f6690a00206a01148777-6b4f287aaaa8ea530a00206a00dee6b8-en-US>`_
            """
            _cmd = "TIME"
            
            class INTermediate(SCPINode, SCPIQuery):
                """
                SYSTem:TIME:INTermediate
                """
                _cmd = "INTermediate"
                
            class STARt(SCPINode, SCPISet):
                """
                SYSTem:TIME:STARt
                """
                _cmd = "STARt"
                
            class STOP(SCPINode, SCPIQuery):
                """
                SYSTem:TIME:STOP
                """
                _cmd = "STOP"
                
            class SYNC(SCPINode, SCPISet):
                """
                SYSTem:TIME:SYNC
                """
                _cmd = "SYNC"
                
        class TSLock(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:TSLock
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e115243.htm#ID_48769b733516bd2c0a00206a005ec64c-a13ed1c43516b4a10a00206a01f2dc17-en-US>`_
            """
            _cmd = "TSLock"
            
        class USER(SCPINode):
            """
            SYSTem:USER
            """
            _cmd = "USER"
            
            class DISPlay(SCPINode):
                """
                SYSTem:USER:DISPlay
                """
                _cmd = "DISPlay"
                
                class TITLe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:USER:DISPlay:TITLe
                    """
                    _cmd = "TITLe"
                    
            class FKEY(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:USER:FKEY
                """
                _cmd = "FKEY"
                
            class KEY(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:USER:KEY
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e115293.htm#ID_5b19f768fab15a190a00206a003ab4cd-5c1d14c8fab1547b0a00206a01a6673d-en-US>`_
                """
                _cmd = "KEY"
                
                class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:USER:KEY:FUNCtion
                    """
                    _cmd = "FUNCtion"
                    
        class VERSion(SCPINode, SCPIQuery):
            """
            `SYSTem:VERSion
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/695c6313296c4a8a.htm#ID_ae289010fab1693c0a00206a008797a2-0d4d3fbffab1637f0a00206a01a6673d-en-US>`_
            """
            _cmd = "VERSion"
            
        class WAIT(SCPINode, SCPISet):
            """
            SYSTem:WAIT
            """
            _cmd = "WAIT"
            
    class TRACe(SCPINode, SCPIQuery, SCPISet):
        """
        TRACe
        """
        _cmd = "TRACe"
        
        class CLEar(SCPINode, SCPISet):
            """
            `TRACe:CLEar
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ac86031e502949ce.htm#ID_64dd94bdfab178ad0a00206a007cb1e5-5b0e530efab1730f0a00206a01a6673d-en-US>`_
            """
            _cmd = "CLEar"
            
        class COPY(SCPINode, SCPISet):
            """
            `TRACe:COPY
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e115607.htm#ID_701570b0fab1805d0a00206a00ce1355-b06fb49ffab17aa10a00206a01a6673d-en-US>`_
            """
            _cmd = "COPY"
            
            class MATH(SCPINode, SCPISet):
                """
                `TRACe:COPY:MATH
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e115702.htm#ID_8db7b1cffab1880e0a00206a015a07f4-f95d19b4fab182510a00206a01a6673d-en-US>`_
                """
                _cmd = "MATH"
                
        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            TRACe:DATA
            """
            _cmd = "DATA"
            
            class RESPonse(SCPINode, SCPIQuery, SCPISet):
                """
                TRACe:DATA:RESPonse
                """
                _cmd = "RESPonse"
                
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRACe:DATA:RESPonse:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e119239.htm#ID_2a0bba9afab1979e0a00206a01b06d03-c178a5b4fab191c20a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ALL"
                    
            class STIMulus(SCPINode, SCPIQuery, SCPISet):
                """
                TRACe:DATA:STIMulus
                """
                _cmd = "STIMulus"
                
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRACe:DATA:STIMulus:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d36e119312.htm#ID_b73c7a35fab18fde0a00206a00c988a1-92a8d8b0fab189f20a00206a01a6673d-en-US>`_
                    """
                    _cmd = "ALL"
                    
    class TRIGger(SCPINodeN):
        """
        TRIGger
        """
        _cmd = "TRIGger"
        
        class CHANnel(SCPINodeN):
            """
            TRIGger:CHANnel
            """
            _cmd = "CHANnel"
            
            class AUXiliary(SCPINodeN, SCPIQuery, SCPISet):
                """
                TRIGger:CHANnel:AUXiliary
                """
                _cmd = "AUXiliary"
                
                class DURation(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:CHANnel:AUXiliary:DURation
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2ec0bc6b13f2415c.htm#ID_862e541aaaa940c00a00206a00c23306-85574235aaa935e20a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "DURation"
                    
                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:CHANnel:AUXiliary:ENABle
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/2f050fb4094d4096.htm#ID_47359972aaa9507f0a00206a00d85789-5734e0b5aaa943dc0a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "ENABle"
                    
                class INTerval(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:CHANnel:AUXiliary:INTerval
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/fb7f8a046d20447a.htm#ID_6e115f17aaa95ddd0a00206a00669cd7-e8362417aaa952b10a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "INTerval"
                    
                class OPOLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:CHANnel:AUXiliary:OPOLarity
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/d4cfc80a1c194fc3.htm#ID_a10e8d4caaa96bc70a00206a01c30908-19056cd3aaa9605d0a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "OPOLarity"
                    
                class POSition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:CHANnel:AUXiliary:POSition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ddbb6ff54bfa4e49.htm#ID_0e644885aaa979540a00206a0189b3a3-f58ab43aaaa96e480a00206a00dee6b8-en-US>`_
                    """
                    _cmd = "POSition"
                    
        class SEQuence(SCPINode):
            """
            TRIGger:SEQuence
            """
            _cmd = "SEQuence"
            
            class HOLDoff(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:HOLDoff
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/c7a1eba08bbc44bb.htm#ID_b0e57a38fab19f200a00206a00cbaf37-80f2d0b6fab199730a00206a01a6673d-en-US>`_
                """
                _cmd = "HOLDoff"
                
            class LINK(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:LINK
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/e09399d307a34f01.htm#ID_a4da22c4fab1a6c10a00206a01179287-42cdd25ffab1a1050a00206a01a6673d-en-US>`_
                """
                _cmd = "LINK"
                
            class MULTiple(SCPINode):
                """
                TRIGger:SEQuence:MULTiple
                """
                _cmd = "MULTiple"
                
                class HOLDoff(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:MULTiple:HOLDoff
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/020b4a1c90f348ff.htm#ID_adddb58013579dc60a00206a0121e541-a514b3ce135797fa0a00206a0182dc26-en-US>`_
                    """
                    _cmd = "HOLDoff"
                    
                class SLOPe(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:MULTiple:SLOPe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/ff1d260400c24bdf.htm#ID_af1475ce1357a5a60a00206a01d52097-fc26c60f13579fca0a00206a0182dc26-en-US>`_
                    """
                    _cmd = "SLOPe"
                    
                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:MULTiple:SOURce
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/12f6a33395644026.htm#ID_f37037d61357ad760a00206a00a7072a-cf0a0a421357a7a90a00206a0182dc26-en-US>`_
                    """
                    _cmd = "SOURce"
                    
            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:SLOPe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/cbc5449b57664ad3.htm#ID_cb1b57a0fab1d4f50a00206a0000a5cb-21b2e7d1fab1cf580a00206a01a6673d-en-US>`_
                """
                _cmd = "SLOPe"
                
            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:SOURce
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_5/Content/9c62999c5a1642f2.htm#ID_3ee3f346fab1dc770a00206a0037b055-0940f367fab1d6da0a00206a01a6673d-en-US>`_
                """
                _cmd = "SOURce"
                
    # END OF ZNB_gen
