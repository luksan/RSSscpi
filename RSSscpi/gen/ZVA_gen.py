# -*- coding: utf-8 -*-
# Generated from ZVA_commands_3_60.inp on 2016-02-22 18:54
from SCPI_gen_support import Instrument, SCPINode, SCPINodeN, SCPIQuery, SCPISet
class ZVA_gen(Instrument):
    class CAL(SCPINode, SCPIQuery):
        """
        `*CAL
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*CAL"
        
    class CLS(SCPINode, SCPISet):
        """
        `*CLS
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*CLS"
        
    class ESE(SCPINode, SCPIQuery, SCPISet):
        """
        `*ESE
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*ESE"
        
    class ESR(SCPINode, SCPIQuery, SCPISet):
        """
        `*ESR
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*ESR"
        
    class IDN(SCPINode, SCPIQuery):
        """
        `*IDN
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*IDN"
        
    class IST(SCPINode, SCPIQuery, SCPISet):
        """
        `*IST
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*IST"
        
    class OPC(SCPINode, SCPIQuery, SCPISet):
        """
        `*OPC
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*OPC"
        
    class OPT(SCPINode, SCPIQuery):
        """
        `*OPT
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*OPT"
        
    class PCB(SCPINode, SCPISet):
        """
        `*PCB
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*PCB"
        
    class PRE(SCPINode, SCPIQuery, SCPISet):
        """
        `*PRE
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*PRE"
        
    class PSC(SCPINode, SCPIQuery, SCPISet):
        """
        `*PSC
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*PSC"
        
    class RST(SCPINode, SCPISet):
        """
        `*RST
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*RST"
        
    class SRE(SCPINode, SCPIQuery, SCPISet):
        """
        `*SRE
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*SRE"
        
    class STB(SCPINode, SCPIQuery):
        """
        `*STB
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*STB"
        
    class TRG(SCPINode, SCPISet):
        """
        `*TRG
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*TRG"
        
    class TST(SCPINode, SCPIQuery):
        """
        `*TST
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*TST"
        
    class WAI(SCPINode, SCPISet):
        """
        `*WAI
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/common_commands.htm>`_
        """
        _cmd = "*WAI"
        
    class DCL(SCPINode, SCPIQuery, SCPISet):
        """
        `@DCL
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_
        """
        _cmd = "@DCL"
        
    class GET(SCPINode, SCPIQuery, SCPISet):
        """
        `@GET
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_
        """
        _cmd = "@GET"
        
    class LOC(SCPINode, SCPIQuery, SCPISet):
        """
        `@LOC
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_
        """
        _cmd = "@LOC"
        
    class REM(SCPINode, SCPIQuery, SCPISet):
        """
        `@REM
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/annexes/hw_interfaces/gpib_bus_interface.htm#Interface_Messages>`_
        """
        _cmd = "@REM"
        
    class ABORt(SCPINode, SCPISet):
        """
        `ABORt
        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/abort/abort.htm#ABORt>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_climits.htm#FAIL>`_
                """
                _cmd = "FAIL"
                
        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:DATA
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_data.htm#DATA>`_
            """
            _cmd = "DATA"
            
            class ALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:ALL
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_data.htm#DATA_ALL>`_
                """
                _cmd = "ALL"
                
            class CALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:CALL
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_data.htm#DATA_CALL>`_
                """
                _cmd = "CALL"
                
                class CATalog(SCPINode, SCPIQuery):
                    """
                    `CALCulate:DATA:CALL:CATalog
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_data.htm#DATA_CALL_CATalog>`_
                    """
                    _cmd = "CATalog"
                    
            class DALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:DALL
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_data.htm#DATA_DALL>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_data.htm#NSWeep_COUNt>`_
                    """
                    _cmd = "COUNt"
                    
                class FIRSt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:NSWeep:FIRSt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_data.htm#NSWeep_FIRSt>`_
                    """
                    _cmd = "FIRSt"
                    
                class LAST(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:NSWeep:LAST
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_data.htm#NSWeep>`_
                    """
                    _cmd = "LAST"
                    
            class SGRoup(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:SGRoup
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_data.htm#DATA_SGRoup>`_
                """
                _cmd = "SGRoup"
                
            class STIMulus(SCPINode, SCPIQuery):
                """
                `CALCulate:DATA:STIMulus
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_data.htm#STIMulus>`_
                """
                _cmd = "STIMulus"
                
        class DLINe(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:DLINe
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_dline.htm#DLINe>`_
            """
            _cmd = "DLINe"
            
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DLINe:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_dline.htm#DLINe_STATe>`_
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
                    
                    class CENTer(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:CENTer
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_filter.htm#CENTer>`_
                        """
                        _cmd = "CENTer"
                        
                    class DCHebyshev(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:DCHebyshev
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_filter.htm#DCHebyshev>`_
                        """
                        _cmd = "DCHebyshev"
                        
                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:SHAPe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_filter.htm#SHAPe>`_
                        """
                        _cmd = "SHAPe"
                        
                    class SHOW(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:SHOW
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_filter.htm#SHOW>`_
                        """
                        _cmd = "SHOW"
                        
                    class SPAN(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:SPAN
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_filter.htm#SPAN>`_
                        """
                        _cmd = "SPAN"
                        
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:STARt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_filter.htm#STARt>`_
                        """
                        _cmd = "STARt"
                        
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_filter.htm#STATe>`_
                        """
                        _cmd = "STATe"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:STOP
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_filter.htm#STOP>`_
                        """
                        _cmd = "STOP"
                        
                    class TYPE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:TYPE
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_filter.htm#TYPE>`_
                        """
                        _cmd = "TYPE"
                        
                    class WINDow(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:WINDow
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_filter.htm#WINDow>`_
                        """
                        _cmd = "WINDow"
                        
        class FORMat(SCPINode, SCPIQuery, SCPISet):
            """
            CALCulate:FORMat
            """
            _cmd = "FORMat"
            
            class WQUType(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:FORMat:WQUType
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_format.htm#FORMat_WQUType>`_
                """
                _cmd = "WQUType"
                
        class FSIMulator(SCPINode):
            """
            CALCulate:FSIMulator
            """
            _cmd = "FSIMulator"
            
            class BALun(SCPINode):
                """
                CALCulate:FSIMulator:BALun
                """
                _cmd = "BALun"
                
                class DEVice(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:FSIMulator:BALun:DEVice
                    """
                    _cmd = "DEVice"
                    
                class DMCircuit(SCPINode):
                    """
                    CALCulate:FSIMulator:BALun:DMCircuit
                    """
                    _cmd = "DMCircuit"
                    
                    class BPORt(SCPINodeN):
                        """
                        CALCulate:FSIMulator:BALun:DMCircuit:BPORt
                        """
                        _cmd = "BPORt"
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINode, SCPIQuery, SCPISet):
                                """
                                CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:C
                                """
                                _cmd = "C"
                                
                            class L(SCPINode, SCPIQuery, SCPISet):
                                """
                                CALCulate:FSIMulator:BALun:DMCircuit:BPORt:PARameters:L
                                """
                                _cmd = "L"
                                
                class DZConversion(SCPINode):
                    """
                    CALCulate:FSIMulator:BALun:DZConversion
                    """
                    _cmd = "DZConversion"
                    
                    class BPORt(SCPINodeN):
                        """
                        CALCulate:FSIMulator:BALun:DZConversion:BPORt
                        """
                        _cmd = "BPORt"
                        
                        class ZCOMmon(SCPINode, SCPIQuery, SCPISet):
                            """
                            CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZCOMmon
                            """
                            _cmd = "ZCOMmon"
                            
                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZCOMmon:R
                                """
                                _cmd = "R"
                                
                        class ZDIFferent(SCPINode, SCPIQuery, SCPISet):
                            """
                            CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZDIFferent
                            """
                            _cmd = "ZDIFferent"
                            
                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                CALCulate:FSIMulator:BALun:DZConversion:BPORt:ZDIFferent:R
                                """
                                _cmd = "R"
                                
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:FSIMulator:STATe
                """
                _cmd = "STATe"
                
        class GDAPerture(SCPINode):
            """
            CALCulate:GDAPerture
            """
            _cmd = "GDAPerture"
            
            class SCOunt(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:GDAPerture:SCOunt
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_gdaperture.htm#SCOunt>`_
                """
                _cmd = "SCOunt"
                
        class LDEViation(SCPINode):
            """
            CALCulate:LDEViation
            """
            _cmd = "LDEViation"
            
            class AUTO(SCPINode, SCPISet):
                """
                `CALCulate:LDEViation:AUTO
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ldeviation.htm#AUTO>`_
                """
                _cmd = "AUTO"
                
            class CONStant(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LDEViation:CONStant
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ldeviation.htm#CONStant>`_
                """
                _cmd = "CONStant"
                
            class ELENgth(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LDEViation:ELENgth
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ldeviation.htm#ELENgth>`_
                """
                _cmd = "ELENgth"
                
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LDEViation:MODE
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ldeviation.htm#MODE>`_
                """
                _cmd = "MODE"
                
            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LDEViation:SLOPe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ldeviation.htm#SLOPe>`_
                """
                _cmd = "SLOPe"
                
        class LIMit(SCPINodeN):
            """
            CALCulate:LIMit
            """
            _cmd = "LIMit"
            
            class CONTrol(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:CONTrol
                """
                _cmd = "CONTrol"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:DATA
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#CONTrol_DATA>`_
                    """
                    _cmd = "DATA"
                    
                class DOMain(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:DOMain
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#CONTrol_Domain>`_
                    """
                    _cmd = "DOMain"
                    
                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:SHIFt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#CONTrol_SHIFt>`_
                    """
                    _cmd = "SHIFt"
                    
            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LIMit:DATA
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#DATA>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#DELete_ALL>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#DISPlay_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class FAIL(SCPINode, SCPIQuery):
                """
                `CALCulate:LIMit:FAIL
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#FAIL>`_
                """
                _cmd = "FAIL"
                
            class LOWer(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:LOWer
                """
                _cmd = "LOWer"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:DATA
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#LOWer_DATA>`_
                    """
                    _cmd = "DATA"
                    
                class FEED(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:FEED
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#LOWer_FEED>`_
                    """
                    _cmd = "FEED"
                    
                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:SHIFt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#LOWer_SHIFt>`_
                    """
                    _cmd = "SHIFt"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#LOWer_STATe>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#RDOMain_COMPlex>`_
                    """
                    _cmd = "COMPlex"
                    
                class FORMat(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:RDOMain:FORMat
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#RDOMain_FORMat>`_
                    """
                    _cmd = "FORMat"
                    
                class SPACing(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:RDOMain:SPACing
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#RDOMain_SPACing>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#SEG_AMPLITUDE_START>`_
                        """
                        _cmd = "STARt"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:AMPLitude:STOP
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#SEG_AMPLitude_STOP>`_
                        """
                        _cmd = "STOP"
                        
                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CALCulate:LIMit:SEGMent:COUNt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#SEG_COUNt>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#SEG_STIMulus_STARt>`_
                        """
                        _cmd = "STARt"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:STIMulus:STOP
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#SEG_STIMulus_STOP>`_
                        """
                        _cmd = "STOP"
                        
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:SEGMent:TYPE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#SEG_TYPE>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#SOUNd_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LIMit:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#STATe>`_
                """
                _cmd = "STATe"
                
            class TTLout(SCPINodeN, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:TTLout
                """
                _cmd = "TTLout"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:TTLout:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#TTLout>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#UPPer_DATA>`_
                    """
                    _cmd = "DATA"
                    
                class FEED(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:FEED
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#UPPer_FEED>`_
                    """
                    _cmd = "FEED"
                    
                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:SHIFt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#UPPer_SHIFt>`_
                    """
                    _cmd = "SHIFt"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_limit.htm#UPPer_STATe>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#AOFF>`_
                """
                _cmd = "AOFF"
                
            class BWIDth(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MARKer:BWIDth
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#COUPled_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class DELTa(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MARKer:DELTa
                """
                _cmd = "DELTa"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:DELTa:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#DELTa_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class FORMat(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:FORMat
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#FORMat>`_
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
                    
                    class EXCursion(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:APEak:EXCursion
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#EXCursion>`_
                        """
                        _cmd = "EXCursion"
                        
                    class THReshold(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:APEak:THReshold
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#THReshold>`_
                        """
                        _cmd = "THReshold"
                        
                class BWIDth(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:BWIDth
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#BFILter_BWIDth>`_
                    """
                    _cmd = "BWIDth"
                    
                    class GMCenter(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:BWIDth:GMCenter
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#BFILTer_GMCenter>`_
                        """
                        _cmd = "GMCenter"
                        
                    class MODE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:BWIDth:MODE
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#BFILTer_MODE>`_
                        """
                        _cmd = "MODE"
                        
                class CENTer(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:CENTer
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#FUNCtion_CENTer>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#DELTa_STATe_ZVR>`_
                        """
                        _cmd = "STATe"
                        
                class DOMain(SCPINode):
                    """
                    CALCulate:MARKer:FUNCtion:DOMain
                    """
                    _cmd = "DOMain"
                    
                    class USER(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:DOMain:USER
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#DOMain_USER>`_
                        """
                        _cmd = "USER"
                        
                        class SHOW(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:SHOW
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#DOMain_USER_SHOW>`_
                            """
                            _cmd = "SHOW"
                            
                        class STARt(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:STARt
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#DOMain_USER_STARt>`_
                            """
                            _cmd = "STARt"
                            
                        class STOP(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:STOP
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#DOMain_USER_STOP>`_
                            """
                            _cmd = "STOP"
                            
                class EXECute(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:EXECute
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#EXECute>`_
                    """
                    _cmd = "EXECute"
                    
                class RESult(SCPINode, SCPIQuery):
                    """
                    `CALCulate:MARKer:FUNCtion:RESult
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#RESult>`_
                    """
                    _cmd = "RESult"
                    
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:SELect
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#SELect>`_
                    """
                    _cmd = "SELect"
                    
                class STARt(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:STARt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#FUNCTion_STARt>`_
                    """
                    _cmd = "STARt"
                    
                class STOP(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:STOP
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#FUNCtion_STOP>`_
                    """
                    _cmd = "STOP"
                    
                class TARGet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:TARGet
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#TARGet_ZVR>`_
                    """
                    _cmd = "TARGet"
                    
            class MAXimum(SCPINode, SCPISet):
                """
                `CALCulate:MARKer:MAXimum
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#MAXimum>`_
                """
                _cmd = "MAXimum"
                
            class MINimum(SCPINode, SCPISet):
                """
                `CALCulate:MARKer:MINimum
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#MINimum>`_
                """
                _cmd = "MINimum"
                
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:MODE
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#MODE>`_
                """
                _cmd = "MODE"
                
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:NAME
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#NAME>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#REFerence_MODE>`_
                    """
                    _cmd = "MODE"
                    
                class NAME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:NAME
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#REFerence_NAME>`_
                    """
                    _cmd = "NAME"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#REFerence>`_
                    """
                    _cmd = "STATe"
                    
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:TYPE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#REFerence_TYPE>`_
                    """
                    _cmd = "TYPE"
                    
                class X(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:X
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#REFerence_X>`_
                    """
                    _cmd = "X"
                    
                class Y(SCPINode, SCPIQuery):
                    """
                    `CALCulate:MARKer:REFerence:Y
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#REFerence_Y>`_
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
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#SEARch_BFILter_RESult_STATe>`_
                            """
                            _cmd = "STATe"
                            
                class IMMediate(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:IMMediate
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#SEARch_IMMediate>`_
                    """
                    _cmd = "IMMediate"
                    
                class LEFT(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:LEFT
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#SEARch_LEFT>`_
                    """
                    _cmd = "LEFT"
                    
                class NEXT(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:NEXT
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#SEARch_NEXT>`_
                    """
                    _cmd = "NEXT"
                    
                class RIGHt(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:RIGHt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#SEARch_RIGHt>`_
                    """
                    _cmd = "RIGHt"
                    
                class TRACking(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:TRACking
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#SEARch_TRACking>`_
                    """
                    _cmd = "TRACking"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#STATe>`_
                """
                _cmd = "STATe"
                
            class TARGet(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MARKer:TARGet
                """
                _cmd = "TARGet"
                
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:TYPE
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#TYPE>`_
                """
                _cmd = "TYPE"
                
            class X(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:X
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#X>`_
                """
                _cmd = "X"
                
            class Y(SCPINode, SCPIQuery):
                """
                `CALCulate:MARKer:Y
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#Y>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_math.htm#EXPRession_DEFine>`_
                    """
                    _cmd = "DEFine"
                    
                class SDEFine(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MATH:EXPRession:SDEFine
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_math.htm#EXPRession_SDEFine>`_
                    """
                    _cmd = "SDEFine"
                    
            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MATH:FUNCtion
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_math.htm#FUNCtion>`_
                """
                _cmd = "FUNCtion"
                
            class MEMorize(SCPINode, SCPISet):
                """
                `CALCulate:MATH:MEMorize
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_math.htm#MEMorize>`_
                """
                _cmd = "MEMorize"
                
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MATH:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_math.htm#STATe>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_math.htm#WUNit_STATe>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_parameter.htm#CATalog>`_
                """
                _cmd = "CATalog"
                
            class DEFine(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:DEFine
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_parameter.htm#DEFine>`_
                """
                _cmd = "DEFine"
                
                class SGRoup(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:PARameter:DEFine:SGRoup
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_parameter.htm#DEFine_SGRoup>`_
                    """
                    _cmd = "SGRoup"
                    
            class DELete(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:DELete
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_parameter.htm#DELete>`_
                """
                _cmd = "DELete"
                
                class ALL(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:ALL
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_parameter.htm#DELete_ALL>`_
                    """
                    _cmd = "ALL"
                    
                class CALL(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:CALL
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_parameter.htm#DELete_CALL>`_
                    """
                    _cmd = "CALL"
                    
                class SGRoup(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:SGRoup
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_parameter.htm#DELete_SGRoup>`_
                    """
                    _cmd = "SGRoup"
                    
            class MEASure(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:PARameter:MEASure
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_parameter.htm#MEASure>`_
                """
                _cmd = "MEASure"
                
            class NFIGure(SCPINode):
                """
                CALCulate:PARameter:NFIGure
                """
                _cmd = "NFIGure"
                
                class CSETtings(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:NFIGure:CSETtings
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_parameter.htm#NFIGure_CSETtings>`_
                    """
                    _cmd = "CSETtings"
                    
            class SDEFine(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:SDEFine
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_parameter.htm#SDEFine>`_
                """
                _cmd = "SDEFine"
                
            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:PARameter:SELect
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_parameter.htm#SELect>`_
                """
                _cmd = "SELect"
                
        class PHOLd(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:PHOLd
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_phold.htm#PHOLd>`_
            """
            _cmd = "PHOLd"
            
        class RIPPle(SCPINode):
            """
            CALCulate:RIPPle
            """
            _cmd = "RIPPle"
            
            class CONTrol(SCPINode):
                """
                CALCulate:RIPPle:CONTrol
                """
                _cmd = "CONTrol"
                
                class DOMain(SCPINode, SCPISet):
                    """
                    `CALCulate:RIPPle:CONTrol:DOMain
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#CONTrol_Domain>`_
                    """
                    _cmd = "DOMain"
                    
            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:RIPPle:DATA
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#DATA>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#DELete_ALL>`_
                    """
                    _cmd = "ALL"
                    
            class DISPlay(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:RIPPle:DISPlay
                """
                _cmd = "DISPlay"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:DISPlay:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#DISPlay_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class FAIL(SCPINode, SCPIQuery):
                """
                `CALCulate:RIPPle:FAIL
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#FAIL>`_
                """
                _cmd = "FAIL"
                
            class RDOMain(SCPINode):
                """
                CALCulate:RIPPle:RDOMain
                """
                _cmd = "RDOMain"
                
                class FORMat(SCPINode, SCPISet):
                    """
                    `CALCulate:RIPPle:RDOMain:FORMat
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#RDOMain_FORMat>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#SEG_COUNt>`_
                    """
                    _cmd = "COUNt"
                    
                class LIMit(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:SEGMent:LIMit
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#SEG_LIMit>`_
                    """
                    _cmd = "LIMit"
                    
                class RESult(SCPINode, SCPIQuery):
                    """
                    `CALCulate:RIPPle:SEGMent:RESult
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#SEG_RESult>`_
                    """
                    _cmd = "RESult"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:SEGMent:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#SEG_STATe>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#SEG_STIMulus_STARt>`_
                        """
                        _cmd = "STARt"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:RIPPle:SEGMent:STIMulus:STOP
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#SEG_STIMulus_STOP>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#SOUNd_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:RIPPle:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_ripple.htm#STATe>`_
                """
                _cmd = "STATe"
                
        class SMOothing(SCPINode, SCPIQuery, SCPISet):
            """
            CALCulate:SMOothing
            """
            _cmd = "SMOothing"
            
            class APERture(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:SMOothing:APERture
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_smoothing.htm#APERture>`_
                """
                _cmd = "APERture"
                
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:SMOothing:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_smoothing.htm#STATe>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#USER>`_
                    """
                    _cmd = "USER"
                    
                    class SHOW(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:DOMain:USER:SHOW
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#USER_SHOW>`_
                        """
                        _cmd = "SHOW"
                        
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:DOMain:USER:STARt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#USER_STARt>`_
                        """
                        _cmd = "STARt"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:DOMain:USER:STOP
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#USER_STOP>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#EPDelay_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class MMPTpeak(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:STATistics:MMPTpeak
                """
                _cmd = "MMPTpeak"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:STATistics:MMPTpeak:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#MMPTpeak_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class MSTDdev(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:STATistics:MSTDdev
                """
                _cmd = "MSTDdev"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:STATistics:MSTDdev:STATe
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#COMP_LEVel>`_
                        """
                        _cmd = "LEVel"
                        
                    class RESult(SCPINode, SCPIQuery):
                        """
                        `CALCulate:STATistics:NLINear:COMP:RESult
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#COMP_RESult>`_
                        """
                        _cmd = "RESult"
                        
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:NLINear:COMP:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#COMP_STATe>`_
                        """
                        _cmd = "STATe"
                        
            class RESult(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:STATistics:RESult
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#RESult>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#RMS_STATe>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#SFLatness_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:STATistics:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_statistics.htm#STATe>`_
                """
                _cmd = "STATe"
                
        class TDIF(SCPINode):
            """
            CALCulate:TDIF
            """
            _cmd = "TDIF"
            
            class IMBalance(SCPINode):
                """
                CALCulate:TDIF:IMBalance
                """
                _cmd = "IMBalance"
                
                class COMPensation(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:TDIF:IMBalance:COMPensation
                    """
                    _cmd = "COMPensation"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:TDIF:IMBalance:COMPensation:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_tdif.htm#IMBalance_COMPensation>`_
                        """
                        _cmd = "STATe"
                        
        class TRANsform(SCPINode):
            """
            CALCulate:TRANsform
            """
            _cmd = "TRANsform"
            
            class COMPlex(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:TRANsform:COMPlex
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#COMPlex>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#IMPedance_RNORMal>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#CENTer>`_
                    """
                    _cmd = "CENTer"
                    
                class DCHebyshev(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:DCHebyshev
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#DCHebyshev>`_
                    """
                    _cmd = "DCHebyshev"
                    
                class LPASs(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:LPASs
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#LPASs>`_
                    """
                    _cmd = "LPASs"
                    
                    class DCSParam(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:TRANsform:TIME:LPASs:DCSParam
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#LPASs_DCSParam>`_
                        """
                        _cmd = "DCSParam"
                        
                        class CONTinuous(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:TIME:LPASs:DCSParam:CONTinuous
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#LPASs_DCSParam_CONTinuous>`_
                            """
                            _cmd = "CONTinuous"
                            
                        class EXTRapolate(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:TIME:LPASs:DCSParam:EXTRapolate
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#LPASs_DSCParam_EXTRapolate>`_
                            """
                            _cmd = "EXTRapolate"
                            
                class LPFRequency(SCPINode, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:LPFRequency
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#LPFRequency>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#RESolution_EFACtor>`_
                        """
                        _cmd = "EFACtor"
                        
                class SPAN(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:SPAN
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#SPAN>`_
                    """
                    _cmd = "SPAN"
                    
                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STARt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#STARt>`_
                    """
                    _cmd = "STARt"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#STATe>`_
                    """
                    _cmd = "STATe"
                    
                class STIMulus(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STIMulus
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#STIMulus>`_
                    """
                    _cmd = "STIMulus"
                    
                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STOP
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#STOP>`_
                    """
                    _cmd = "STOP"
                    
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:TYPE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#TYPE>`_
                    """
                    _cmd = "TYPE"
                    
                class WINDow(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:WINDow
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#WINDow>`_
                    """
                    _cmd = "WINDow"
                    
                class XAXis(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:XAXis
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform.htm#XAXis>`_
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
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_PARameters_C>`_
                                """
                                _cmd = "C"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:L
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_PARameters_L>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:R
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_PARameters_R>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_STATe>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:TNDefinition
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_DEEMbedding_TNDefinition>`_
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
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_PARameters_C>`_
                                """
                                _cmd = "C"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:L
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_PARameters_L>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:R
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_PARameters_R>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_STATe>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:TNDefinition
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#BALanced_EMBedding_TNDefinition>`_
                            """
                            _cmd = "TNDefinition"
                            
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
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_PARameters_C>`_
                                """
                                _cmd = "C"
                                
                            class L(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:L
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_PARameters_L>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:R
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_PARameters_R>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_STATe>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:TNDefinition
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_DEEMbedding_TNDefinition>`_
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
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_PARameters_C>`_
                                """
                                _cmd = "C"
                                
                            class L(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:L
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_PARameters_L>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:R
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_PARameters_R>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#GLOop_EMBedding_STATe>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            CALCulate:TRANsform:VNETworks:GLOop:EMBedding:TNDefinition
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
                        
                        class DEFine(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:DEFine
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_DEFine>`_
                            """
                            _cmd = "DEFine"
                            
                        class DELete(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:DELete
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_DELete>`_
                            """
                            _cmd = "DELete"
                            
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:C
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_PARameters_C>`_
                                """
                                _cmd = "C"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:L
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_PARameters_L>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:R
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_PARameters_R>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_STATe>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:TNDefinition
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_DEEMbedding_TNDefinition>`_
                            """
                            _cmd = "TNDefinition"
                            
                    class EMBedding(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        CALCulate:TRANsform:VNETworks:PPAir:EMBedding
                        """
                        _cmd = "EMBedding"
                        
                        class DEFine(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:DEFine
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_DEFine>`_
                            """
                            _cmd = "DEFine"
                            
                        class DELete(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:DELete
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_DELete>`_
                            """
                            _cmd = "DELete"
                            
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters
                            """
                            _cmd = "PARameters"
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:C
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_PARameters_C>`_
                                """
                                _cmd = "C"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:L
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_PARameters_L>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:R
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_PARameters_R>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_STATe>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:TNDefinition
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#PPAir_EMBedding_TNDefinition>`_
                            """
                            _cmd = "TNDefinition"
                            
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
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_PARameters_C>`_
                                """
                                _cmd = "C"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:L
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_PARameters_L>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:R
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_PARameters_R>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_STATe>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:TNDefinition
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_DEEMbedding_TNDefinition>`_
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
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_PARameters_C>`_
                                """
                                _cmd = "C"
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:L
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_PARameters_L>`_
                                """
                                _cmd = "L"
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:R
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_PARameters_R>`_
                                """
                                _cmd = "R"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_STATe>`_
                            """
                            _cmd = "STATe"
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:TNDefinition
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_transform_vnetworks.htm#SENDed_EMBedding_TNDefinition>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/configure/configure.htm#CATalog>`_
                """
                _cmd = "CATalog"
                
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:CHANnel:NAME
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/configure/configure.htm#NAME>`_
                """
                _cmd = "NAME"
                
                class ID(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:CHANnel:NAME:ID
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/configure/configure.htm#NAME_ID>`_
                    """
                    _cmd = "ID"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:CHANnel:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/configure/configure.htm#STATe>`_
                """
                _cmd = "STATe"
                
            class TRACe(SCPINode):
                """
                CONFigure:CHANnel:TRACe
                """
                _cmd = "TRACe"
                
                class REName(SCPINode, SCPISet):
                    """
                    `CONFigure:CHANnel:TRACe:REName
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/configure/configure.htm#Channel_Trace_Rename>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/configure/configure.htm#TRACe_CATalog_>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/configure/configure.htm#TRACe_CHANnel_NAME>`_
                    """
                    _cmd = "NAME"
                    
                    class ID(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONFigure:TRACe:CHANnel:NAME:ID
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/configure/configure.htm#TRACe_CHANnel_ID>`_
                        """
                        _cmd = "ID"
                        
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:TRACe:NAME
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/configure/configure.htm#TRACe_NAME>`_
                """
                _cmd = "NAME"
                
                class ID(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:TRACe:NAME:ID
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/configure/configure.htm#TRACe_NAME_ID>`_
                    """
                    _cmd = "ID"
                    
            class REName(SCPINode, SCPISet):
                """
                `CONFigure:TRACe:REName
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/configure/configure.htm#TRACe_REName>`_
                """
                _cmd = "REName"
                
    class CONTrol(SCPINode):
        """
        CONTrol
        """
        _cmd = "CONTrol"
        
        class AUXiliary(SCPINode):
            """
            CONTrol:AUXiliary
            """
            _cmd = "AUXiliary"
            
            class A(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:AUXiliary:A
                """
                _cmd = "A"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:AUXiliary:A:DATA
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control.htm#A_B_DATA>`_
                    """
                    _cmd = "DATA"
                    
            class B(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:AUXiliary:B
                """
                _cmd = "B"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:AUXiliary:B:DATA
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control.htm#A_B_DATA>`_
                    """
                    _cmd = "DATA"
                    
            class C(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:AUXiliary:C
                """
                _cmd = "C"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:AUXiliary:C:DATA
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control.htm#DATA>`_
                    """
                    _cmd = "DATA"
                    
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#A_DATA>`_
                    """
                    _cmd = "DATA"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:A:MODE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#A_MODE>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#A_DATA>`_
                    """
                    _cmd = "DATA"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:B:MODE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#A_MODE>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#A_DATA>`_
                    """
                    _cmd = "DATA"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:C:MODE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#A_MODE>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#A_DATA>`_
                    """
                    _cmd = "DATA"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:D:MODE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#A_MODE>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#A_DATA>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#EXTension_INDEX_STATe>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#EXTension_RTRigger_STATe>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#A_DATA>`_
                    """
                    _cmd = "DATA"
                    
            class OUTPut(SCPINodeN, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:OUTPut
                """
                _cmd = "OUTPut"
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:OUTPut:DATA
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#OUTPut_DATA>`_
                    """
                    _cmd = "DATA"
                    
                class USER(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:OUTPut:USER
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#OUTPut_USER>`_
                    """
                    _cmd = "USER"
                    
            class RESet(SCPINode, SCPISet):
                """
                `CONTrol:HANDler:RESet
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/control/control_handler.htm#RESet>`_
                """
                _cmd = "RESet"
                
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
            
            class AUBW(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:AUBW
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#ALC_AUBW>`_
                """
                _cmd = "AUBW"
                
            class BW(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:BW
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#ALC_BW>`_
                """
                _cmd = "BW"
                
            class CLAMp(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:CLAMp
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#ALC_CLAMp>`_
                """
                _cmd = "CLAMp"
                
            class DMODe(SCPINode):
                """
                DIAGnostic:ALC:DMODe
                """
                _cmd = "DMODe"
                
                class MSTimulus(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:ALC:DMODe:MSTimulus
                    """
                    _cmd = "MSTimulus"
                    
                class POINts(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:ALC:DMODe:POINts
                    """
                    _cmd = "POINts"
                    
                class RTIMe(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:ALC:DMODe:RTIMe
                    """
                    _cmd = "RTIMe"
                    
            class PIParameter(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:PIParameter
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#ALC_PIParameter>`_
                """
                _cmd = "PIParameter"
                
                class GAIN(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DIAGnostic:ALC:PIParameter:GAIN
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#ALC_PIParameter_GAIN>`_
                    """
                    _cmd = "GAIN"
                    
                class ITIMe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DIAGnostic:ALC:PIParameter:ITIMe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#ALC_PIParameter_ITIMe>`_
                    """
                    _cmd = "ITIMe"
                    
            class POFFset(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:POFFset
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#ALC_POFFset>`_
                """
                _cmd = "POFFset"
                
            class RANGe(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:RANGe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#ALC_RANGe>`_
                """
                _cmd = "RANGe"
                
            class SETTings(SCPINode, SCPIQuery, SCPISet):
                """
                DIAGnostic:ALC:SETTings
                """
                _cmd = "SETTings"
                
                class CMODe(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:ALC:SETTings:CMODe
                    """
                    _cmd = "CMODe"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DIAGnostic:ALC:SETTings:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#ALC_SETTings>`_
                    """
                    _cmd = "STATe"
                    
            class SOFFset(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:SOFFset
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#ALC_SOFFset>`_
                """
                _cmd = "SOFFset"
                
            class STOLerance(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:ALC:STOLerance
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#ALC_STOLerance>`_
                """
                _cmd = "STOLerance"
                
        class DEVice(SCPINode):
            """
            DIAGnostic:DEVice
            """
            _cmd = "DEVice"
            
            class STATe(SCPINode, SCPISet):
                """
                `DIAGnostic:DEVice:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#DEVice_STATe>`_
                """
                _cmd = "STATe"
                
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#FUNCtion>`_
                """
                _cmd = "FUNCtion"
                
            class RFPower(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:SERVice:RFPower
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#RFPower>`_
                """
                _cmd = "RFPower"
                
            class SFUNction(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:SERVice:SFUNction
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/diagnostic/diagnostic.htm#SFUNction>`_
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
                    
    class DISPlay(SCPINode):
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#ANNotation_CHANnel>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#ANNotation>`_
                    """
                    _cmd = "STATe"
                    
        class CMAP(SCPINodeN):
            """
            DISPlay:CMAP
            """
            _cmd = "CMAP"
            
            class MARKer(SCPINode, SCPIQuery, SCPISet):
                """
                DISPlay:CMAP:MARKer
                """
                _cmd = "MARKer"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:CMAP:MARKer:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm>`_
                    """
                    _cmd = "STATe"
                    
            class RGB(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:CMAP:RGB
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm>`_
                        """
                        _cmd = "STATe"
                        
                class RGB(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:CMAP:TRACe:RGB
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#CMAP_TRACe_RGB>`_
                    """
                    _cmd = "RGB"
                    
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#MENU_KEY_EXECute>`_
                    """
                    _cmd = "EXECute"
                    
                class SELect(SCPINode, SCPISet):
                    """
                    `DISPlay:MENU:KEY:SELect
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#MENU_KEY_SELect>`_
                    """
                    _cmd = "SELect"
                    
        class RFSize(SCPINode, SCPIQuery, SCPISet):
            """
            `DISPlay:RFSize
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#RFSize>`_
            """
            _cmd = "RFSize"
            
        class WINDow(SCPINodeN):
            """
            DISPlay:WINDow
            """
            _cmd = "WINDow"
            
            class CATalog(SCPINode, SCPIQuery):
                """
                `DISPlay:WINDow:CATalog
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#WINDow_CATalog>`_
                """
                _cmd = "CATalog"
                
            class MAXimize(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:WINDow:MAXimize
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#MAXimize>`_
                """
                _cmd = "MAXimize"
                
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:WINDow:NAME
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#Diagram_NAME>`_
                """
                _cmd = "NAME"
                
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:WINDow:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#STATe>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#TITLe_DATA>`_
                    """
                    _cmd = "DATA"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TITLe:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#TITLe_STATe>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#WINDow_TRACe_CATalog>`_
                    """
                    _cmd = "CATalog"
                    
                class DELete(SCPINode, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:DELete
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#DELete>`_
                    """
                    _cmd = "DELete"
                    
                class EFEed(SCPINode, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:EFEed
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#EFEed>`_
                    """
                    _cmd = "EFEed"
                    
                class FEED(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:FEED
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#FEED>`_
                    """
                    _cmd = "FEED"
                    
                class SHOW(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:SHOW
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#SHOW>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#X_OFFSet>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#Y_OFFSet>`_
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
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#AUTO>`_
                            """
                            _cmd = "AUTO"
                            
                        class BOTTom(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:BOTTom
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#BOTTom>`_
                            """
                            _cmd = "BOTTom"
                            
                        class PDIVision(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:PDIVision
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#PDIVision>`_
                            """
                            _cmd = "PDIVision"
                            
                        class RLEVel(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:RLEVel
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#RLEVel>`_
                            """
                            _cmd = "RLEVel"
                            
                        class RPOSition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:RPOSition
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#RPOSition>`_
                            """
                            _cmd = "RPOSition"
                            
                        class TOP(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:TOP
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/display/display.htm#TOP>`_
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
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/format/format.htm#BORDer>`_
            """
            _cmd = "BORDer"
            
        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `FORMat:DATA
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/format/format.htm#DATA>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/format/format.htm#DEXPort_SOURce>`_
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
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#DESTination>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#DEVice_LANGuage>`_
                """
                _cmd = "LANGuage"
                
        class IMMediate(SCPINode, SCPISet):
            """
            `HCOPy:IMMediate
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#IMMediate>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#ITEM_ALL>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#LOGO>`_
                    """
                    _cmd = "STATe"
                    
            class MLISt(SCPINode, SCPIQuery, SCPISet):
                """
                HCOPy:ITEM:MLISt
                """
                _cmd = "MLISt"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    HCOPy:ITEM:MLISt:STATe
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#TIME>`_
                    """
                    _cmd = "STATe"
                    
        class MITem(SCPINode):
            """
            HCOPy:MITem
            """
            _cmd = "MITem"
            
            class LOGO(SCPINode, SCPIQuery, SCPISet):
                """
                HCOPy:MITem:LOGO
                """
                _cmd = "LOGO"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:MITem:LOGO:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#MITEM_LOGO>`_
                    """
                    _cmd = "STATe"
                    
            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                HCOPy:MITem:TIME
                """
                _cmd = "TIME"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:MITem:TIME:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#MITEM_TIME>`_
                    """
                    _cmd = "STATe"
                    
        class MPAGe(SCPINode):
            """
            HCOPy:MPAGe
            """
            _cmd = "MPAGe"
            
            class WINDow(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:MPAGe:WINDow
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#MPAGe_WINDow>`_
                """
                _cmd = "WINDow"
                
        class PAGE(SCPINode):
            """
            HCOPy:PAGE
            """
            _cmd = "PAGE"
            
            class MARGin(SCPINode):
                """
                HCOPy:PAGE:MARGin
                """
                _cmd = "MARGin"
                
                class BOTTom(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:BOTTom
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#BOTTom>`_
                    """
                    _cmd = "BOTTom"
                    
                class LEFT(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:LEFT
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/calculate/calculate_marker.htm#SEARch_LEFT>`_
                    """
                    _cmd = "LEFT"
                    
                class RIGHt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:RIGHt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#RIGHt>`_
                    """
                    _cmd = "RIGHt"
                    
                class TOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:TOP
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#TOP>`_
                    """
                    _cmd = "TOP"
                    
            class ORIentation(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:PAGE:ORIentation
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#ORIentation>`_
                """
                _cmd = "ORIentation"
                
            class WINDow(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:PAGE:WINDow
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/hcopy/hcopy.htm#WINDow>`_
                """
                _cmd = "WINDow"
                
    class INITiate(SCPINodeN, SCPIQuery, SCPISet):
        """
        INITiate
        """
        _cmd = "INITiate"
        
        class CONTinuous(SCPINode, SCPIQuery, SCPISet):
            """
            `INITiate:CONTinuous
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/initiate/initiate.htm#CONTinuous>`_
            """
            _cmd = "CONTinuous"
            
        class IMMediate(SCPINode, SCPIQuery, SCPISet):
            """
            `INITiate:IMMediate
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/initiate/initiate.htm#IMMediate>`_
            """
            _cmd = "IMMediate"
            
            class DUMMy(SCPINode, SCPIQuery, SCPISet):
                """
                INITiate:IMMediate:DUMMy
                """
                _cmd = "DUMMy"
                
            class SCOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `INITiate:IMMediate:SCOPe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/initiate/initiate.htm#SCOPe>`_
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
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/input/input.htm#ATTenuation>`_
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
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/instrument/instrument.htm#NSELect>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/instrument/instrument.htm#PORT_COUNt>`_
                """
                _cmd = "COUNt"
                
        class SELect(SCPINode, SCPIQuery, SCPISet):
            """
            `INSTrument:SELect
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/instrument/instrument.htm#SELect>`_
            """
            _cmd = "SELect"
            
    class MEMory(SCPINode):
        """
        MEMory
        """
        _cmd = "MEMory"
        
        class CATalog(SCPINode, SCPIQuery):
            """
            `MEMory:CATalog
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/memory/memory.htm#CATalog>`_
            """
            _cmd = "CATalog"
            
        class DEFine(SCPINode, SCPISet):
            """
            `MEMory:DEFine
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/memory/memory.htm#DEFine>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/memory/memory.htm#DELete_ALL>`_
                """
                _cmd = "ALL"
                
            class NAME(SCPINode, SCPISet):
                """
                `MEMory:DELete:NAME
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/memory/memory.htm#DELete_NAME>`_
                """
                _cmd = "NAME"
                
        class SELect(SCPINode, SCPISet):
            """
            `MEMory:SELect
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/memory/memory.htm#SELect>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#AKAL_FACTory_CONVersion>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#AKAL_USER_CONVersion>`_
                    """
                    _cmd = "CONVersion"
                    
        class CATalog(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:CATalog
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#CATalog>`_
            """
            _cmd = "CATalog"
            
            class ALL(SCPINode, SCPIQuery, SCPISet):
                """
                `MMEMory:CATalog:ALL
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#CATalog_All>`_
                """
                _cmd = "ALL"
                
        class CDIRectory(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:CDIRectory
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#CDIRecotry>`_
            """
            _cmd = "CDIRectory"
            
        class COPY(SCPINode, SCPISet):
            """
            `MMEMory:COPY
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#COPY>`_
            """
            _cmd = "COPY"
            
        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:DATA
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#DATA>`_
            """
            _cmd = "DATA"
            
        class DELete(SCPINode, SCPISet):
            """
            `MMEMory:DELete
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#DELete>`_
            """
            _cmd = "DELete"
            
            class CORRection(SCPINode, SCPISet):
                """
                `MMEMory:DELete:CORRection
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#DELete_CORRection>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_CKIT>`_
                """
                _cmd = "CKIT"
                
                class SDATa(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CKIT:SDATa
                    <scpi_reference/mmemory/mmemory.htm#LOAD_CKIT:SDATa>`_
                    """
                    _cmd = "SDATa"
                    
                class UDIRectory(SCPINode, SCPIQuery, SCPISet):
                    """
                    `MMEMory:LOAD:CKIT:UDIRectory
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_CKIT_UDIRectory>`_
                    """
                    _cmd = "UDIRectory"
                    
            class CMAP(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:CMAP
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_CMAP>`_
                """
                _cmd = "CMAP"
                
            class CORRection(SCPINode, SCPIQuery, SCPISet):
                """
                `MMEMory:LOAD:CORRection
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection>`_
                """
                _cmd = "CORRection"
                
                class MERGe(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:MERGe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection_MERGE>`_
                    """
                    _cmd = "MERGe"
                    
                class RESolve(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:RESolve
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection_RESolve>`_
                    """
                    _cmd = "RESolve"
                    
                class TCOefficient(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:TCOefficient
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_CORRection_TCOefficient>`_
                    """
                    _cmd = "TCOefficient"
                    
            class LIMit(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:LIMit
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_LIMit>`_
                """
                _cmd = "LIMit"
                
            class MDAData(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:MDAData
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_MDAData>`_
                """
                _cmd = "MDAData"
                
            class MDCData(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:MDCData
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_MDCData>`_
                """
                _cmd = "MDCData"
                
            class PTRain(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:PTRain
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_PTRain>`_
                """
                _cmd = "PTRain"
                
            class RIPPle(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:RIPPle
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_RIPPle>`_
                """
                _cmd = "RIPPle"
                
            class SEGMent(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:SEGMent
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_SEGMent>`_
                """
                _cmd = "SEGMent"
                
            class STATe(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_STATe>`_
                """
                _cmd = "STATe"
                
            class TRACe(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:TRACe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_TRACE>`_
                """
                _cmd = "TRACe"
                
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_BALanced_DEEMbedding>`_
                        """
                        _cmd = "DEEMbedding"
                        
                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:BALanced:EMBedding
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_BALanced_EMBedding>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_GLOop_DEEMbedding>`_
                        """
                        _cmd = "DEEMbedding"
                        
                    class EMBedding(SCPINode, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:GLOop:EMBedding
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_GLOop_EMBedding>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_PPAir_DEEMbedding>`_
                        """
                        _cmd = "DEEMbedding"
                        
                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:PPAir:EMBedding
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_PPAir_EMBedding>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_SENDed_DEEMbedding>`_
                        """
                        _cmd = "DEEMbedding"
                        
                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:SENDed:EMBedding
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#LOAD_VNETworks_SENDed_EMBedding>`_
                        """
                        _cmd = "EMBedding"
                        
        class MDIRectory(SCPINode, SCPISet):
            """
            `MMEMory:MDIRectory
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#MDIRectory>`_
            """
            _cmd = "MDIRectory"
            
        class MOVE(SCPINode, SCPISet):
            """
            `MMEMory:MOVE
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#MOVE>`_
            """
            _cmd = "MOVE"
            
        class MSIS(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:MSIS
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#MSIS>`_
            """
            _cmd = "MSIS"
            
        class NAME(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:NAME
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#NAME>`_
            """
            _cmd = "NAME"
            
        class RDIRectory(SCPINode, SCPISet):
            """
            `MMEMory:RDIRectory
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#RDIRectory>`_
            """
            _cmd = "RDIRectory"
            
        class SETTings(SCPINode):
            """
            MMEMory:SETTings
            """
            _cmd = "SETTings"
            
            class RENorm(SCPINode):
                """
                MMEMory:SETTings:RENorm
                """
                _cmd = "RENorm"
                
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `MMEMory:SETTings:RENorm:MODE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#SETTings_RENorm_MODE>`_
                    """
                    _cmd = "MODE"
                    
                class RIMPedance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `MMEMory:SETTings:RENorm:RIMPedance
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#SETTings_RENorm_RIMPedance>`_
                    """
                    _cmd = "RIMPedance"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `MMEMory:SETTings:RENorm:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#SETTings_RENorm_STATe>`_
                    """
                    _cmd = "STATe"
                    
        class STORe(SCPINode):
            """
            MMEMory:STORe
            """
            _cmd = "STORe"
            
            class CKIT(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CKIT
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_CKIT>`_
                """
                _cmd = "CKIT"
                
                class WLABel(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:CKIT:WLABel
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_CKIT_WLABel>`_
                    """
                    _cmd = "WLABel"
                    
            class CMAP(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CMAP
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_CMAP>`_
                """
                _cmd = "CMAP"
                
            class CORRection(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CORRection
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_CORRection>`_
                """
                _cmd = "CORRection"
                
                class TCOefficient(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:CORRection:TCOefficient
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_CORRection_TCOefficient>`_
                    """
                    _cmd = "TCOefficient"
                    
            class LIMit(SCPINode, SCPISet):
                """
                `MMEMory:STORe:LIMit
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_LIMit>`_
                """
                _cmd = "LIMit"
                
            class MARKer(SCPINode, SCPISet):
                """
                `MMEMory:STORe:MARKer
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_MARKer>`_
                """
                _cmd = "MARKer"
                
            class MDCData(SCPINode, SCPISet):
                """
                `MMEMory:STORe:MDCData
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_MDCData>`_
                """
                _cmd = "MDCData"
                
            class PTRain(SCPINode, SCPISet):
                """
                `MMEMory:STORe:PTRain
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_PTRain>`_
                """
                _cmd = "PTRain"
                
            class RIPPle(SCPINode, SCPISet):
                """
                `MMEMory:STORe:RIPPle
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_RIPPle>`_
                """
                _cmd = "RIPPle"
                
            class SEGMent(SCPINode, SCPISet):
                """
                `MMEMory:STORe:SEGMent
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_SEGMent>`_
                """
                _cmd = "SEGMent"
                
            class STATe(SCPINode, SCPISet):
                """
                `MMEMory:STORe:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_STATe>`_
                """
                _cmd = "STATe"
                
            class TRACe(SCPINode, SCPISet):
                """
                `MMEMory:STORe:TRACe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_TRACE>`_
                """
                _cmd = "TRACe"
                
                class CHANnel(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:TRACe:CHANnel
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_TRACE_CHANnel>`_
                    """
                    _cmd = "CHANnel"
                    
                class PORTs(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:TRACe:PORTs
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_TRACE_PORTs>`_
                    """
                    _cmd = "PORTs"
                    
                    class INComplete(SCPINode, SCPISet):
                        """
                        `MMEMory:STORe:TRACe:PORTs:INComplete
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/mmemory/mmemory.htm#STORe_TRACE_PORTs_INComplete>`_
                        """
                        _cmd = "INComplete"
                        
    class OUTPut(SCPINodeN, SCPIQuery, SCPISet):
        """
        OUTPut
        """
        _cmd = "OUTPut"
        
        class ATTenuation(SCPINode, SCPIQuery, SCPISet):
            """
            `OUTPut:ATTenuation
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/output/output.htm#Attenuation>`_
            """
            _cmd = "ATTenuation"
            
        class DPORt(SCPINode, SCPIQuery, SCPISet):
            """
            `OUTPut:DPORt
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/output/output.htm#DPORt>`_
            """
            _cmd = "DPORt"
            
        class STATe(SCPINode, SCPIQuery, SCPISet):
            """
            `OUTPut:STATe
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/output/output.htm#DPORt>`_
            """
            _cmd = "STATe"
            
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `OUTPut:STATe:TYPE
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/output/output.htm#STATe_TYPE>`_
                """
                _cmd = "TYPE"
                
        class UPORt(SCPINode, SCPIQuery):
            """
            OUTPut:UPORt
            """
            _cmd = "UPORt"
            
            class BUSY(SCPINode):
                """
                OUTPut:UPORt:BUSY
                """
                _cmd = "BUSY"
                
                class LINK(SCPINode, SCPIQuery, SCPISet):
                    """
                    `OUTPut:UPORt:BUSY:LINK
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/output/output.htm#UPORt_BUSY_LINK>`_
                    """
                    _cmd = "LINK"
                    
            class SEGMent(SCPINodeN, SCPIQuery):
                """
                OUTPut:UPORt:SEGMent
                """
                _cmd = "SEGMent"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `OUTPut:UPORt:SEGMent:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/output/output.htm#UPORt_SEGMent_STATe>`_
                    """
                    _cmd = "STATe"
                    
                class VALue(SCPINode, SCPIQuery):
                    """
                    `OUTPut:UPORt:SEGMent:VALue
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/output/output.htm#UPORt_SEGMent_VALue>`_
                    """
                    _cmd = "VALue"
                    
            class VALue(SCPINode, SCPIQuery):
                """
                `OUTPut:UPORt:VALue
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/output/output.htm#UPORt_VALue>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/program/program.htm#EXECute>`_
                """
                _cmd = "EXECute"
                
            class INIMessage(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:INIMessage
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/program/program.htm#INIMessage>`_
                """
                _cmd = "INIMessage"
                
            class INIParameter(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:INIParameter
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/program/program.htm#INIParameter>`_
                """
                _cmd = "INIParameter"
                
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:NAME
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/program/program.htm#NAME>`_
                """
                _cmd = "NAME"
                
            class RETVal(SCPINode, SCPIQuery):
                """
                `PROGram:SELected:RETVal
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/program/program.htm#RETVal>`_
                """
                _cmd = "RETVal"
                
            class STRing(SCPINode, SCPIQuery, SCPISet):
                """
                PROGram:SELected:STRing
                """
                _cmd = "STRing"
                
            class WAIT(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:WAIT
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/program/program.htm#WAIT>`_
                """
                _cmd = "WAIT"
                
    class ROUTe(SCPINodeN):
        """
        ROUTe
        """
        _cmd = "ROUTe"
        
        class CFILe(SCPINode, SCPIQuery, SCPISet):
            """
            `ROUTe:CFILe
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/route/route.htm#CFILe>`_
            """
            _cmd = "CFILe"
            
        class PORTs(SCPINodeN, SCPIQuery, SCPISet):
            """
            `ROUTe:PORTs
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/route/route.htm#PORTs>`_
            """
            _cmd = "PORTs"
            
    class SENSe(SCPINodeN):
        """
        SENSe
        """
        _cmd = "SENSe"
        
        class AVERage(SCPINode, SCPIQuery, SCPISet):
            """
            `SENSe:AVERage
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___average.htm>`_
            """
            _cmd = "AVERage"
            
            class CLEar(SCPINode, SCPISet):
                """
                `SENSe:AVERage:CLEar
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___average.htm#CLEar>`_
                """
                _cmd = "CLEar"
                
            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:AVERage:COUNt
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___average.htm#Count>`_
                """
                _cmd = "COUNt"
                
                class ACTual(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:AVERage:COUNt:ACTual
                    """
                    _cmd = "ACTual"
                    
                class CURRent(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:AVERage:COUNt:CURRent
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___average.htm#Count_CURRent>`_
                    """
                    _cmd = "CURRent"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:AVERage:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___average.htm#State>`_
                """
                _cmd = "STATe"
                
        class BANDwidth(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:BANDwidth
            """
            _cmd = "BANDwidth"
            
            class RESolution(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:BANDwidth:RESolution
                """
                _cmd = "RESolution"
                
                class DREDuction(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:BANDwidth:RESolution:DREDuction
                    """
                    _cmd = "DREDuction"
                    
                class GENerator(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:BANDwidth:RESolution:GENerator
                    """
                    _cmd = "GENerator"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:BANDwidth:RESolution:MODE
                    """
                    _cmd = "MODE"
                    
                class PORT(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:BANDwidth:RESolution:PORT
                    """
                    _cmd = "PORT"
                    
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:BANDwidth:RESolution:SELect
                    """
                    _cmd = "SELect"
                    
        class BWIDth(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:BWIDth
            """
            _cmd = "BWIDth"
            
            class RESolution(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:BWIDth:RESolution
                """
                _cmd = "RESolution"
                
                class DREDuction(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:BWIDth:RESolution:DREDuction
                    """
                    _cmd = "DREDuction"
                    
                class GENerator(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:BWIDth:RESolution:GENerator
                    """
                    _cmd = "GENerator"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:BWIDth:RESolution:MODE
                    """
                    _cmd = "MODE"
                    
                class PORT(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:BWIDth:RESolution:PORT
                    """
                    _cmd = "PORT"
                    
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:BWIDth:RESolution:SELect
                    """
                    _cmd = "SELect"
                    
        class CONVerter(SCPINode):
            """
            SENSe:CONVerter
            """
            _cmd = "CONVerter"
            
            class AMODel(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CONVerter:AMODel
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_converter.htm#AMODel>`_
                """
                _cmd = "AMODel"
                
            class ASSign(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:CONVerter:ASSign
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_converter.htm#ASSign>`_
                """
                _cmd = "ASSign"
                
            class DESCription(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CONVerter:DESCription
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_converter.htm#DESCription>`_
                """
                _cmd = "DESCription"
                
            class PATH(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CONVerter:PATH
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_converter.htm#PATH>`_
                """
                _cmd = "PATH"
                
        class CORRection(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:CORRection
            """
            _cmd = "CORRection"
            
            class CBFReq(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:CBFReq
                """
                _cmd = "CBFReq"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CBFReq:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction.htm#CBFReq>`_
                    """
                    _cmd = "STATe"
                    
            class CDATa(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:CDATa
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction.htm#CDATa>`_
                """
                _cmd = "CDATa"
                
            class CKIT(SCPINode):
                """
                SENSe:CORRection:CKIT
                """
                _cmd = "CKIT"
                
                class CATalog(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:CATalog
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit.htm#CATalog>`_
                    """
                    _cmd = "CATalog"
                    
                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:DELete
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit.htm#DELete>`_
                    """
                    _cmd = "DELete"
                    
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
                        
                class INSTall(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:INSTall
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit.htm#INSTall>`_
                    """
                    _cmd = "INSTall"
                    
                class LABel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LABel
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit.htm#LABel>`_
                    """
                    _cmd = "LABel"
                    
                class LCATalog(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LCATalog
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit_l(abel).htm#CATalog>`_
                    """
                    _cmd = "LCATalog"
                    
                class LDELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LDELete
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit_l(abel).htm#DELete>`_
                    """
                    _cmd = "LDELete"
                    
                class LLABel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LLABel
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit_l(abel).htm#LABel>`_
                    """
                    _cmd = "LLABel"
                    
                class LSELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LSELect
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit_l(abel).htm#SELect_String>`_
                    """
                    _cmd = "LSELect"
                    
                class MDATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:MDATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit.htm#MDATe>`_
                    """
                    _cmd = "MDATe"
                    
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit.htm#SELect_String>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit.htm#STANdard_CATalog>`_
                        """
                        _cmd = "CATalog"
                        
                    class LCATalog(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:CKIT:STANdard:LCATalog
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_ckit_l(abel).htm#STANdard_CATalog>`_
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
                        
            class COLLect(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:COLLect
                """
                _cmd = "COLLect"
                
                class ACQuire(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:COLLect:ACQuire
                    """
                    _cmd = "ACQuire"
                    
                    class RSAVe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:ACQuire:RSAVe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AQUire_SAVE>`_
                        """
                        _cmd = "RSAVe"
                        
                        class DEFault(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:ACQuire:RSAVe:DEFault
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AQUire_SAVE_DEFault>`_
                            """
                            _cmd = "DEFault"
                            
                    class SELected(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:COLLect:ACQuire:SELected
                        """
                        _cmd = "SELected"
                        
                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:AUTO
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO>`_
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
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_ASSignment_ACQuire>`_
                            """
                            _cmd = "ACQuire"
                            
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:ASSignment:DEFine
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_ASSignment_DEFine>`_
                            """
                            _cmd = "DEFine"
                            
                        class DELete(SCPINode):
                            """
                            SENSe:CORRection:COLLect:AUTO:ASSignment:DELete
                            """
                            _cmd = "DELete"
                            
                            class ALL(SCPINode, SCPISet):
                                """
                                `SENSe:CORRection:COLLect:AUTO:ASSignment:DELete:ALL
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_ASSignment_DELete>`_
                                """
                                _cmd = "ALL"
                                
                    class CKIT(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:CKIT
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_CKIT>`_
                        """
                        _cmd = "CKIT"
                        
                        class PORTs(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:CKIT:PORTs
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_CKIT_Ports>`_
                            """
                            _cmd = "PORTs"
                            
                    class CONFigure(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:CONFigure
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_CONFigure>`_
                        """
                        _cmd = "CONFigure"
                        
                    class PORTs(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:PORTs
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_PORTs>`_
                        """
                        _cmd = "PORTs"
                        
                        class CONNection(SCPINode, SCPIQuery):
                            """
                            `SENSe:CORRection:COLLect:AUTO:PORTs:CONNection
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_PORTs_CONNection>`_
                            """
                            _cmd = "CONNection"
                            
                        class TYPE(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:PORTs:TYPE
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_PORTs_TYPE>`_
                            """
                            _cmd = "TYPE"
                            
                    class RPGRoup(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:RPGRoup
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_RPGRoup>`_
                        """
                        _cmd = "RPGRoup"
                        
                    class SAVE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:SAVE
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_SAVE>`_
                        """
                        _cmd = "SAVE"
                        
                    class TYPE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:TYPE
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_TYPE>`_
                        """
                        _cmd = "TYPE"
                        
                    class VMIXer(SCPINode):
                        """
                        SENSe:CORRection:COLLect:AUTO:VMIXer
                        """
                        _cmd = "VMIXer"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:VMIXer:ACQuire
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#AUTO_VMIXer>`_
                            """
                            _cmd = "ACQuire"
                            
                class CONNection(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:CONNection
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#CONNection>`_
                    """
                    _cmd = "CONNection"
                    
                    class GENDers(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CONNection:GENDers
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#CONNection_GENDers>`_
                        """
                        _cmd = "GENDers"
                        
                    class PORTs(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CONNection:PORTs
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#CONNection_PORTs>`_
                        """
                        _cmd = "PORTs"
                        
                class CSETup(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:CSETup
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#CSETup>`_
                    """
                    _cmd = "CSETup"
                    
                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:DELete
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#DELete>`_
                    """
                    _cmd = "DELete"
                    
                class DETector(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:DETector
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#DETector>`_
                    """
                    _cmd = "DETector"
                    
                class FIXTure(SCPINode, SCPISet):
                    """
                    SENSe:CORRection:COLLect:FIXTure
                    """
                    _cmd = "FIXTure"
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:ACQuire
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#FIXTure_AQUire>`_
                        """
                        _cmd = "ACQuire"
                        
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
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#FIXTure_LMParameter_LOSS>`_
                                """
                                _cmd = "STATe"
                                
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:FIXTure:LMParameter:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#FIXTure_LMParameter>`_
                            """
                            _cmd = "STATe"
                            
                    class SAVE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:SAVE
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#FIXTure_SAVE>`_
                        """
                        _cmd = "SAVE"
                        
                    class STARt(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:STARt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#FIXTure_STARt>`_
                        """
                        _cmd = "STARt"
                        
                class IMODulation(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:COLLect:IMODulation
                    """
                    _cmd = "IMODulation"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:IMODulation:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#IMODulation>`_
                        """
                        _cmd = "STATe"
                        
                class METHod(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:METHod
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#METHod>`_
                    """
                    _cmd = "METHod"
                    
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:METHod:DEFine
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#METHod_DEFine>`_
                        """
                        _cmd = "DEFine"
                        
                class NFIGure(SCPINode, SCPISet):
                    """
                    SENSe:CORRection:COLLect:NFIGure
                    """
                    _cmd = "NFIGure"
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:NFIGure:ACQuire
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#NFIGure_STARt>`_
                        """
                        _cmd = "ACQuire"
                        
                    class END(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:NFIGure:END
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#NFIGure_END>`_
                        """
                        _cmd = "END"
                        
                    class SAVE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:NFIGure:SAVE
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#NFIGure_AQUire>`_
                        """
                        _cmd = "SAVE"
                        
                    class STARt(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:NFIGure:STARt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#NFIGure_SAVE>`_
                        """
                        _cmd = "STARt"
                        
                class RPSHift(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:RPSHift
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#RPSHift>`_
                    """
                    _cmd = "RPSHift"
                    
                class SAVE(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:SAVE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#SAVE>`_
                    """
                    _cmd = "SAVE"
                    
                    class DEFault(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:SAVE:DEFault
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#SAVE_DEFault>`_
                        """
                        _cmd = "DEFault"
                        
                    class DUMMy(SCPINode, SCPISet):
                        """
                        SENSe:CORRection:COLLect:SAVE:DUMMy
                        """
                        _cmd = "DUMMy"
                        
                    class SELected(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:SAVE:SELected
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#SAVE_SELected>`_
                        """
                        _cmd = "SELected"
                        
                        class DEFault(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:SAVE:SELected:DEFault
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#SAVE_SELected_DEFault>`_
                            """
                            _cmd = "DEFault"
                            
                        class DUMMy(SCPINode, SCPISet):
                            """
                            SENSe:CORRection:COLLect:SAVE:SELected:DUMMy
                            """
                            _cmd = "DUMMy"
                            
                class SCONnection(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:SCONnection
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_collect.htm#SCONnection>`_
                    """
                    _cmd = "SCONnection"
                    
            class CONNection(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:CONNection
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#CONNection>`_
                """
                _cmd = "CONNection"
                
                class CATalog(SCPINode, SCPIQuery):
                    """
                    `SENSe:CORRection:CONNection:CATalog
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#CONNection_CATalog>`_
                    """
                    _cmd = "CATalog"
                    
                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CONNection:DELete
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#CONNection_DELete>`_
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
                SENSe:CORRection:DATA
                """
                _cmd = "DATA"
                
                class PARameter(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:DATA:PARameter
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#DATA_PARameter_>`_
                    """
                    _cmd = "PARameter"
                    
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SENSe:CORRection:DATA:PARameter:COUNt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#DATA_PARameter_COUNt>`_
                        """
                        _cmd = "COUNt"
                        
            class DATE(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:DATE
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#DATE>`_
                """
                _cmd = "DATE"
                
            class EDELay(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:EDELay
                """
                _cmd = "EDELay"
                
                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:AUTO
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#EDELay_AUTO>`_
                    """
                    _cmd = "AUTO"
                    
                class DIELectric(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:DIELectric
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#EDELay_DIELectric>`_
                    """
                    _cmd = "DIELectric"
                    
                class DISTance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:DISTance
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#EDELay_DISTance>`_
                    """
                    _cmd = "DISTance"
                    
                class ELENgth(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:ELENgth
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#EDELay_ELENgth>`_
                    """
                    _cmd = "ELENgth"
                    
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:TIME
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#EDELay_TIME>`_
                    """
                    _cmd = "TIME"
                    
            class EWAVe(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:EWAVe
                """
                _cmd = "EWAVe"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EWAVe:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#EWAVe>`_
                    """
                    _cmd = "STATe"
                    
            class FACTory(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:FACTory
                """
                _cmd = "FACTory"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:FACTory:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#FACTory_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class LOSS(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:LOSS
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#LOSS>`_
                """
                _cmd = "LOSS"
                
                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:AUTO
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#LOSS_AUTO>`_
                    """
                    _cmd = "AUTO"
                    
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:FREQuency
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#LOSS_FREQuency>`_
                    """
                    _cmd = "FREQuency"
                    
                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:OFFSet
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#LOSS_OFFSet>`_
                    """
                    _cmd = "OFFSet"
                    
            class NFIGure(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:NFIGure
                """
                _cmd = "NFIGure"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:NFIGure:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#NFIGure_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class NSTate(SCPINode, SCPIQuery):
                """
                SENSe:CORRection:NSTate
                """
                _cmd = "NSTate"
                
            class OFFSet(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:OFFSet
                """
                _cmd = "OFFSet"
                
                class DFComp(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:OFFSet:DFComp
                    """
                    _cmd = "DFComp"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:OFFSet:DFComp:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#OFFset_DFComp_STATe>`_
                        """
                        _cmd = "STATe"
                        
                class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:OFFSet:MAGNitude
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#OFFSet_MAGNitude>`_
                    """
                    _cmd = "MAGNitude"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:OFFSet:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_data.htm#OFFset_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class POWer(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:POWer
                """
                _cmd = "POWer"
                
                class ACQuire(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:POWer:ACQuire
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#POWer_ACQuire>`_
                    """
                    _cmd = "ACQuire"
                    
                class AWAVe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:POWer:AWAVe
                    """
                    _cmd = "AWAVe"
                    
                    class IPMMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:POWer:AWAVe:IPMMatch
                        """
                        _cmd = "IPMMatch"
                        
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:CORRection:POWer:AWAVe:IPMMatch:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#POWer_AWAVe_IPMMatch_STATe>`_
                            """
                            _cmd = "STATe"
                            
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:POWer:AWAVe:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#POWer_AWAVe_STATe>`_
                        """
                        _cmd = "STATe"
                        
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:POWer:DATA
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#POWer_DATA>`_
                    """
                    _cmd = "DATA"
                    
                class HARMonic(SCPINode):
                    """
                    SENSe:CORRection:POWer:HARMonic
                    """
                    _cmd = "HARMonic"
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:POWer:HARMonic:ACQuire
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#HARMonic_ACQuire>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#IMODulation_ACQuire>`_
                        """
                        _cmd = "ACQuire"
                        
                    class RPORt(SCPINode):
                        """
                        SENSe:CORRection:POWer:IMODulation:RPORt
                        """
                        _cmd = "RPORt"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:POWer:IMODulation:RPORt:ACQuire
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#IMODulation_RPORt_ACQuire>`_
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
                            `SENSe:CORRection:POWer:MIXer:IF:ACQuire
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#MIXer_IF_ACQuire>`_
                            """
                            _cmd = "ACQuire"
                            
                        class NFIGure(SCPINode):
                            """
                            SENSe:CORRection:POWer:MIXer:IF:NFIGure
                            """
                            _cmd = "NFIGure"
                            
                            class ACQuire(SCPINode, SCPISet):
                                """
                                `SENSe:CORRection:POWer:MIXer:IF:NFIGure:ACQuire
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#MIXer_IF_NFIGure_ACQuire>`_
                                """
                                _cmd = "ACQuire"
                                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:POWer:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#POWer_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class PSTate(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:PSTate
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#PSTate>`_
                """
                _cmd = "PSTate"
                
            class SSTate(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:SSTate
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#SSTate>`_
                """
                _cmd = "SSTate"
                
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#STATe>`_
                """
                _cmd = "STATe"
                
            class STIMulus(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:STIMulus
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_correction_power.htm#STIMulus>`_
                """
                _cmd = "STIMulus"
                
        class COUPle(SCPINode, SCPIQuery, SCPISet):
            """
            `SENSe:COUPle
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_cmode.htm#COUPle>`_
            """
            _cmd = "COUPle"
            
        class EUNit(SCPINode):
            """
            SENSe:EUNit
            """
            _cmd = "EUNit"
            
            class COMBiner(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:EUNit:COMBiner
                """
                _cmd = "COMBiner"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:EUNit:COMBiner:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_eunit.htm#COMBiner_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class HFILter(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:EUNit:HFILter
                """
                _cmd = "HFILter"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:EUNit:HFILter:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_eunit.htm#HFILter_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class LNAMplifier(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:EUNit:LNAMplifier
                """
                _cmd = "LNAMplifier"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:EUNit:LNAMplifier:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_eunit.htm#LNAMplifier_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class PGENerator(SCPINode):
                """
                SENSe:EUNit:PGENerator
                """
                _cmd = "PGENerator"
                
                class ASSignment(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:EUNit:PGENerator:ASSignment
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_eunit.htm#PGENerator_ASSignment>`_
                    """
                    _cmd = "ASSignment"
                    
                class INPut(SCPINode):
                    """
                    SENSe:EUNit:PGENerator:INPut
                    """
                    _cmd = "INPut"
                    
                    class EXTernal(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:EUNit:PGENerator:INPut:EXTernal
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_eunit.htm#PGENerator_INPut_EXTernal>`_
                        """
                        _cmd = "EXTernal"
                        
                class OUTPut(SCPINode):
                    """
                    SENSe:EUNit:PGENerator:OUTPut
                    """
                    _cmd = "OUTPut"
                    
                    class EXTernal(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:EUNit:PGENerator:OUTPut:EXTernal
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_eunit.htm#PGENerator_OUTPut_EXTernal>`_
                        """
                        _cmd = "EXTernal"
                        
            class PMODulator(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:EUNit:PMODulator
                """
                _cmd = "PMODulator"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:EUNit:PMODulator:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_eunit.htm#PMODulator_STATe>`_
                    """
                    _cmd = "STATe"
                    
        class FREQuency(SCPINodeN, SCPIQuery, SCPISet):
            """
            SENSe:FREQuency
            """
            _cmd = "FREQuency"
            
            class CENTer(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CENTer
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CENTer>`_
                """
                _cmd = "CENTer"
                
            class CONVersion(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CONVersion
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion>`_
                """
                _cmd = "CONVersion"
                
                class ARBitrary(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:CONVersion:ARBitrary
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_ARBitrary>`_
                    """
                    _cmd = "ARBitrary"
                    
                    class PMETer(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:ARBitrary:PMETer
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_ARBitrary_PMETer>`_
                        """
                        _cmd = "PMETer"
                        
                class AWReceiver(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:FREQuency:CONVersion:AWReceiver
                    """
                    _cmd = "AWReceiver"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:AWReceiver:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_AWReceiver__STATe>`_
                        """
                        _cmd = "STATe"
                        
                class DEVice(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:DEVice
                    """
                    _cmd = "DEVice"
                    
                    class MODE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:DEVice:MODE
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_MODE>`_
                        """
                        _cmd = "MODE"
                        
                    class NAME(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:DEVice:NAME
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_NAME>`_
                        """
                        _cmd = "NAME"
                        
                    class PCOefficient(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:DEVice:PCOefficient
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_PCOefficient>`_
                        """
                        _cmd = "PCOefficient"
                        
                        class DEFault(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:FREQuency:CONVersion:DEVice:PCOefficient:DEFault
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_DEVice_PCOefficient_DEFault>`_
                            """
                            _cmd = "DEFault"
                            
                class GAIN(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:GAIN
                    """
                    _cmd = "GAIN"
                    
                    class LMCorrection(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:GAIN:LMCorrection
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_GAIN_LMCorrection>`_
                        """
                        _cmd = "LMCorrection"
                        
                class HARMonic(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:HARMonic
                    """
                    _cmd = "HARMonic"
                    
                    class ORDer(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:HARMonic:ORDer
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_ORDer>`_
                        """
                        _cmd = "ORDer"
                        
                    class RELative(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:HARMonic:RELative
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_RELative>`_
                        """
                        _cmd = "RELative"
                        
                    class RPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:HARMonic:RPORt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_RPORt>`_
                        """
                        _cmd = "RPORt"
                        
                    class SPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:HARMonic:SPORt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency.htm#CONVersion_HARMonic_SPORt>`_
                        """
                        _cmd = "SPORt"
                        
                class MIXer(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:MIXer
                    """
                    _cmd = "MIXer"
                    
                    class AEXTernal(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:AEXTernal
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#AEXTernal>`_
                        """
                        _cmd = "AEXTernal"
                        
                    class AINTernal(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:AINTernal
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#AINTernal>`_
                        """
                        _cmd = "AINTernal"
                        
                    class APORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:APORt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#APORt>`_
                        """
                        _cmd = "APORt"
                        
                    class FFIXed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:FFIXed
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#FFIXed>`_
                        """
                        _cmd = "FFIXed"
                        
                    class FIXed(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:FIXed
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#FIXed>`_
                        """
                        _cmd = "FIXed"
                        
                    class FUNDamental(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:FUNDamental
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#FUNDamental>`_
                        """
                        _cmd = "FUNDamental"
                        
                    class HACCuracy(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:HACCuracy
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#HACCuracy>`_
                        """
                        _cmd = "HACCuracy"
                        
                    class IFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:IFFixed
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#IFFixed>`_
                        """
                        _cmd = "IFFixed"
                        
                    class IFPort(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:IFPort
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#IFSource>`_
                        """
                        _cmd = "IFPort"
                        
                    class LOEXternal(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOEXternal
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOEXternal>`_
                        """
                        _cmd = "LOEXternal"
                        
                    class LOFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOFixed
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOFixed>`_
                        """
                        _cmd = "LOFixed"
                        
                    class LOINternal(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOINternal
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOINternal>`_
                        """
                        _cmd = "LOINternal"
                        
                    class LOMultiplier(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOMultiplier
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOMultiplier>`_
                        """
                        _cmd = "LOMultiplier"
                        
                    class LOPort(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOPort
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#LOPort>`_
                        """
                        _cmd = "LOPort"
                        
                    class MFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:MFFixed
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#MFFixed>`_
                        """
                        _cmd = "MFFixed"
                        
                    class PRFimage(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:PRFimage
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#PRFimage>`_
                        """
                        _cmd = "PRFimage"
                        
                    class RFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:RFFixed
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#RFFixed>`_
                        """
                        _cmd = "RFFixed"
                        
                    class RFMultiplier(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:RFMultiplier
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#RFMultiplier>`_
                        """
                        _cmd = "RFMultiplier"
                        
                    class RFPort(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:RFPort
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#RFSource>`_
                        """
                        _cmd = "RFPort"
                        
                    class STAGes(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:STAGes
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#STAGes>`_
                        """
                        _cmd = "STAGes"
                        
                    class TFRequency(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:TFRequency
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_conversion_mixer.htm#TFRequency>`_
                        """
                        _cmd = "TFRequency"
                        
            class CW(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CW
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_cw.htm#CW>`_
                """
                _cmd = "CW"
                
            class FIXed(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:FIXed
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_cw.htm#CW>`_
                """
                _cmd = "FIXed"
                
            class IMODulation(SCPINode):
                """
                SENSe:FREQuency:IMODulation
                """
                _cmd = "IMODulation"
                
                class COMBiner(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:FREQuency:IMODulation:COMBiner
                    """
                    _cmd = "COMBiner"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:IMODulation:COMBiner:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_imodulation.htm#COMBiner_STATe>`_
                        """
                        _cmd = "STATe"
                        
                class CONVersion(SCPINode, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:CONVersion
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_imodulation.htm#CONVersion>`_
                    """
                    _cmd = "CONVersion"
                    
                class LTONe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:LTONe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_imodulation.htm#LTONe>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_imodulation.htm#ORDer>`_
                        """
                        _cmd = "STATe"
                        
                class PEWCorr(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:FREQuency:IMODulation:PEWCorr
                    """
                    _cmd = "PEWCorr"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:IMODulation:PEWCorr:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_imodulation.htm#PEWCorr>`_
                        """
                        _cmd = "STATe"
                        
                class RECeiver(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:RECeiver
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_imodulation.htm#RECeiver>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_imodulation.htm#SPECtrum_MORDer>`_
                        """
                        _cmd = "MORDer"
                        
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:IMODulation:SPECtrum:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_imodulation.htm#SPECtrum_STATe>`_
                        """
                        _cmd = "STATe"
                        
                class TDIStance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:TDIStance
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_imodulation.htm#TDISTance>`_
                    """
                    _cmd = "TDIStance"
                    
                class TTOutput(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:TTOutput
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_imodulation.htm#TTOutput>`_
                    """
                    _cmd = "TTOutput"
                    
                class UTONe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:UTONe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_imodulation.htm#UTONe>`_
                    """
                    _cmd = "UTONe"
                    
            class LPNoise(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:LPNoise
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_cw.htm#LPNoise>`_
                """
                _cmd = "LPNoise"
                
            class MDELay(SCPINode):
                """
                SENSe:FREQuency:MDELay
                """
                _cmd = "MDELay"
                
                class ACQuire(SCPINode, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:ACQuire
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_mdelay.htm#ACQuire>`_
                    """
                    _cmd = "ACQuire"
                    
                class APERture(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:APERture
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_mdelay.htm#APERture>`_
                    """
                    _cmd = "APERture"
                    
                class CDELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:CDELay
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_mdelay.htm#CDELay>`_
                    """
                    _cmd = "CDELay"
                    
                class CDMode(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:CDMode
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_mdelay.htm#CDMode>`_
                    """
                    _cmd = "CDMode"
                    
                class COMBiner(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:FREQuency:MDELay:COMBiner
                    """
                    _cmd = "COMBiner"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:MDELay:COMBiner:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_mdelay.htm#COMBiner_STATe>`_
                        """
                        _cmd = "STATe"
                        
                class CONVersion(SCPINode, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:CONVersion
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_mdelay.htm#CONVersion>`_
                    """
                    _cmd = "CONVersion"
                    
                class CORRection(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:FREQuency:MDELay:CORRection
                    """
                    _cmd = "CORRection"
                    
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:MDELay:CORRection:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_mdelay.htm#CORRection_STATe>`_
                        """
                        _cmd = "STATe"
                        
                class DIVide(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:DIVide
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_mdelay.htm#DIVide>`_
                    """
                    _cmd = "DIVide"
                    
                class RECeiver(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:RECeiver
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_mdelay.htm#RECeiver>`_
                    """
                    _cmd = "RECeiver"
                    
                    class USE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:MDELay:RECeiver:USE
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_mdelay.htm#RECeiver_USE>`_
                        """
                        _cmd = "USE"
                        
                class UTONe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:MDELay:UTONe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_mdelay.htm#UTONe>`_
                    """
                    _cmd = "UTONe"
                    
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:MODE
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_cw.htm#MODE>`_
                """
                _cmd = "MODE"
                
            class OFFSet(SCPINode):
                """
                SENSe:FREQuency:OFFSet
                """
                _cmd = "OFFSet"
                
                class PWAVes(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:OFFSet:PWAVes
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_cw.htm#OFFSet_PWAVes>`_
                    """
                    _cmd = "PWAVes"
                    
                class WAVes(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:OFFSet:WAVes
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_cw.htm#OFFSet_WAVes>`_
                    """
                    _cmd = "WAVes"
                    
            class SBANd(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:SBANd
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_cw.htm#SBANd>`_
                """
                _cmd = "SBANd"
                
            class SPAN(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:SPAN
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_cw.htm#SPAN>`_
                """
                _cmd = "SPAN"
                
            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:STARt
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_cw.htm#STARt>`_
                """
                _cmd = "STARt"
                
            class STOP(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:STOP
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_frequency_cw.htm#STOP>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_function.htm#FUNCtion>`_
                """
                _cmd = "ON"
                
        class IFRequency(SCPINodeN):
            """
            SENSe:IFRequency
            """
            _cmd = "IFRequency"
            
            class CONVersion(SCPINode):
                """
                SENSe:IFRequency:CONVersion
                """
                _cmd = "CONVersion"
                
                class ARBitrary(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:IFRequency:CONVersion:ARBitrary
                    """
                    _cmd = "ARBitrary"
                    
        class LOMeasure(SCPINodeN, SCPIQuery, SCPISet):
            """
            SENSe:LOMeasure
            """
            _cmd = "LOMeasure"
            
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:LOMeasure:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_lomeasure.htm#LOMeasure>`_
                """
                _cmd = "STATe"
                
        class LOReference(SCPINodeN, SCPIQuery, SCPISet):
            """
            SENSe:LOReference
            """
            _cmd = "LOReference"
            
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:LOReference:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_lomeasure.htm#LOReference>`_
                """
                _cmd = "STATe"
                
        class LPORt(SCPINodeN):
            """
            SENSe:LPORt
            """
            _cmd = "LPORt"
            
            class ZCOMmon(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:LPORt:ZCOMmon
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_lport.htm#ZCOMmon>`_
                """
                _cmd = "ZCOMmon"
                
            class ZDIFferent(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:LPORt:ZDIFferent
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_lport.htm#ZDIFferent>`_
                """
                _cmd = "ZDIFferent"
                
        class NFIGure(SCPINode):
            """
            SENSe:NFIGure
            """
            _cmd = "NFIGure"
            
            class ISNoise(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:NFIGure:ISNoise
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_nfigure.htm#ISNoise>`_
                """
                _cmd = "ISNoise"
                
            class NDUT(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:NFIGure:NDUT
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_nfigure.htm#NDUT>`_
                """
                _cmd = "NDUT"
                
            class RFICorr(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:NFIGure:RFICorr
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_nfigure.htm#RFICorr>`_
                """
                _cmd = "RFICorr"
                
            class SEQuential(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:NFIGure:SEQuential
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_nfigure.htm#SEQuential>`_
                """
                _cmd = "SEQuential"
                
        class PAE(SCPINode):
            """
            SENSe:PAE
            """
            _cmd = "PAE"
            
            class C(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PAE:C
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pae.htm#C>`_
                """
                _cmd = "C"
                
            class EXPRession(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PAE:EXPRession
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pae.htm#EXPRession>`_
                """
                _cmd = "EXPRession"
                
            class K(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PAE:K
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pae.htm#K>`_
                """
                _cmd = "K"
                
        class PMMO(SCPINode, SCPIQuery, SCPISet):
            """
            `SENSe:PMMO
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pmmo.htm#PMMO>`_
            """
            _cmd = "PMMO"
            
        class PORT(SCPINodeN):
            """
            SENSe:PORT
            """
            _cmd = "PORT"
            
            class ZREFerence(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PORT:ZREFerence
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_port.htm#ZREFerence>`_
                """
                _cmd = "ZREFerence"
                
        class POWer(SCPINode):
            """
            SENSe:POWer
            """
            _cmd = "POWer"
            
            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:POWer:ATTenuation
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_power.htm#ATTenuation>`_
                """
                _cmd = "ATTenuation"
                
            class IFGain(SCPINodeN):
                """
                SENSe:POWer:IFGain
                """
                _cmd = "IFGain"
                
                class MEASure(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:POWer:IFGain:MEASure
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_power.htm#IFGain_MEASure>`_
                    """
                    _cmd = "MEASure"
                    
                class REFerence(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:POWer:IFGain:REFerence
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_power.htm#IFGain_REFerence>`_
                    """
                    _cmd = "REFerence"
                    
        class PULSe(SCPINode):
            """
            SENSe:PULSe
            """
            _cmd = "PULSe"
            
            class COUPled(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:PULSe:COUPled
                """
                _cmd = "COUPled"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:COUPled:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#COUPled_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class GENerator(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:PULSe:GENerator
                """
                _cmd = "GENerator"
                
                class CPPRofile(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:CPPRofile
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#CPPRofile>`_
                    """
                    _cmd = "CPPRofile"
                    
                class DELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:DELay
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#DELay>`_
                    """
                    _cmd = "DELay"
                    
                class DINCrement(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:DINCrement
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#DINCrement>`_
                    """
                    _cmd = "DINCrement"
                    
                class MCHannel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:MCHannel
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#MCHannel>`_
                    """
                    _cmd = "MCHannel"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:MODE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#MODE>`_
                    """
                    _cmd = "MODE"
                    
                class PERiod(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:PERiod
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#PERiod>`_
                    """
                    _cmd = "PERiod"
                    
                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:POLarity
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#POLarity>`_
                    """
                    _cmd = "POLarity"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#STATe>`_
                    """
                    _cmd = "STATe"
                    
                class TRAin(SCPINode):
                    """
                    SENSe:PULSe:GENerator:TRAin
                    """
                    _cmd = "TRAin"
                    
                    class DATA(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:PULSe:GENerator:TRAin:DATA
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#TRAin_DATA>`_
                        """
                        _cmd = "DATA"
                        
                    class DELete(SCPINode):
                        """
                        SENSe:PULSe:GENerator:TRAin:DELete
                        """
                        _cmd = "DELete"
                        
                        class ALL(SCPINode, SCPISet):
                            """
                            `SENSe:PULSe:GENerator:TRAin:DELete:ALL
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#TRAin_DELete_ALL>`_
                            """
                            _cmd = "ALL"
                            
                    class PERiod(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:PULSe:GENerator:TRAin:PERiod
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#TRAIn_PERiod>`_
                        """
                        _cmd = "PERiod"
                        
                    class SEGMent(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:PULSe:GENerator:TRAin:SEGMent
                        """
                        _cmd = "SEGMent"
                        
                        class COUNt(SCPINode, SCPIQuery):
                            """
                            `SENSe:PULSe:GENerator:TRAin:SEGMent:COUNt
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGMent_COUNt>`_
                            """
                            _cmd = "COUNt"
                            
                        class STARt(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:PULSe:GENerator:TRAin:SEGMent:STARt
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGment_STATe>`_
                            """
                            _cmd = "STARt"
                            
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:PULSe:GENerator:TRAin:SEGMent:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGment_STIMulus_STOP>`_
                            """
                            _cmd = "STATe"
                            
                        class STOP(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:PULSe:GENerator:TRAin:SEGMent:STOP
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#TRAin_SEGMent_STIMulus_STARt>`_
                            """
                            _cmd = "STOP"
                            
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:TYPE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#TYPE>`_
                    """
                    _cmd = "TYPE"
                    
                class WIDTh(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:GENerator:WIDTh
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse_generator.htm#WIDTh>`_
                    """
                    _cmd = "WIDTh"
                    
            class RECeiver(SCPINode):
                """
                SENSe:PULSe:RECeiver
                """
                _cmd = "RECeiver"
                
                class A(SCPINodeN):
                    """
                    SENSe:PULSe:RECeiver:A
                    """
                    _cmd = "A"
                    
                    class GENerator(SCPINodeN):
                        """
                        SENSe:PULSe:RECeiver:A:GENerator
                        """
                        _cmd = "GENerator"
                        
                        class EVALuation(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:A:GENerator:EVALuation
                            """
                            _cmd = "EVALuation"
                            
                            class MODE(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:GENerator:EVALuation:MODE
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__EVALuation_MODE>`_
                                """
                                _cmd = "MODE"
                                
                            class STARt(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:GENerator:EVALuation:STARt
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__EVALuation_STARt>`_
                                """
                                _cmd = "STARt"
                                
                            class STOP(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:GENerator:EVALuation:STOP
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__EVALuation_STOP>`_
                                """
                                _cmd = "STOP"
                                
                        class LINes(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:PULSe:RECeiver:A:GENerator:LINes
                            """
                            _cmd = "LINes"
                            
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:GENerator:LINes:STATe
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__LINEs_STATe>`_
                                """
                                _cmd = "STATe"
                                
                        class TRIGger(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:A:GENerator:TRIGger
                            """
                            _cmd = "TRIGger"
                            
                            class DELay(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:GENerator:TRIGger:DELay
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__GENerator_gen_no__TRIGger_DELay>`_
                                """
                                _cmd = "DELay"
                                
                    class SRCPort(SCPINodeN):
                        """
                        SENSe:PULSe:RECeiver:A:SRCPort
                        """
                        _cmd = "SRCPort"
                        
                        class EVALuation(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:A:SRCPort:EVALuation
                            """
                            _cmd = "EVALuation"
                            
                            class MODE(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:SRCPort:EVALuation:MODE
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__EVALuation_MODE>`_
                                """
                                _cmd = "MODE"
                                
                            class STARt(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:SRCPort:EVALuation:STARt
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__EVALuation_STARt>`_
                                """
                                _cmd = "STARt"
                                
                            class STOP(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:SRCPort:EVALuation:STOP
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__EVALuation_STOP>`_
                                """
                                _cmd = "STOP"
                                
                        class LINes(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:PULSe:RECeiver:A:SRCPort:LINes
                            """
                            _cmd = "LINes"
                            
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:SRCPort:LINes:STATe
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__LINEs_STATe>`_
                                """
                                _cmd = "STATe"
                                
                        class TRIGger(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:A:SRCPort:TRIGger
                            """
                            _cmd = "TRIGger"
                            
                            class DELay(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:A:SRCPort:TRIGger:DELay
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_A_rec_no__SRCPort_port_no__TRIGger_DELay>`_
                                """
                                _cmd = "DELay"
                                
                class B(SCPINodeN):
                    """
                    SENSe:PULSe:RECeiver:B
                    """
                    _cmd = "B"
                    
                    class GENerator(SCPINodeN):
                        """
                        SENSe:PULSe:RECeiver:B:GENerator
                        """
                        _cmd = "GENerator"
                        
                        class EVALuation(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:B:GENerator:EVALuation
                            """
                            _cmd = "EVALuation"
                            
                            class MODE(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:GENerator:EVALuation:MODE
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__EVALuation_MODE>`_
                                """
                                _cmd = "MODE"
                                
                            class STARt(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:GENerator:EVALuation:STARt
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__EVALuation_STARt>`_
                                """
                                _cmd = "STARt"
                                
                            class STOP(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:GENerator:EVALuation:STOP
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__EVALuation_STOP>`_
                                """
                                _cmd = "STOP"
                                
                        class LINes(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:PULSe:RECeiver:B:GENerator:LINes
                            """
                            _cmd = "LINes"
                            
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:GENerator:LINes:STATe
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__LINEs_STATe>`_
                                """
                                _cmd = "STATe"
                                
                        class TRIGger(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:B:GENerator:TRIGger
                            """
                            _cmd = "TRIGger"
                            
                            class DELay(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:GENerator:TRIGger:DELay
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__GENerator_gen_no__TRIGger_DELay>`_
                                """
                                _cmd = "DELay"
                                
                    class SRCPort(SCPINodeN):
                        """
                        SENSe:PULSe:RECeiver:B:SRCPort
                        """
                        _cmd = "SRCPort"
                        
                        class EVALuation(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:B:SRCPort:EVALuation
                            """
                            _cmd = "EVALuation"
                            
                            class MODE(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:SRCPort:EVALuation:MODE
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__EVALuation_MODE>`_
                                """
                                _cmd = "MODE"
                                
                            class STARt(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:SRCPort:EVALuation:STARt
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__EVALuation_STARt>`_
                                """
                                _cmd = "STARt"
                                
                            class STOP(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:SRCPort:EVALuation:STOP
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__EVALuation_STOP>`_
                                """
                                _cmd = "STOP"
                                
                        class LINes(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:PULSe:RECeiver:B:SRCPort:LINes
                            """
                            _cmd = "LINes"
                            
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:SRCPort:LINes:STATe
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__LINEs_STATe>`_
                                """
                                _cmd = "STATe"
                                
                        class TRIGger(SCPINode):
                            """
                            SENSe:PULSe:RECeiver:B:SRCPort:TRIGger
                            """
                            _cmd = "TRIGger"
                            
                            class DELay(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:PULSe:RECeiver:B:SRCPort:TRIGger:DELay
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#RECeiver_B_rec_no__SRCPort_port_no__TRIGger_DELay>`_
                                """
                                _cmd = "DELay"
                                
            class TIME(SCPINode):
                """
                SENSe:PULSe:TIME
                """
                _cmd = "TIME"
                
                class BWIDth(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:PULSe:TIME:BWIDth
                    """
                    _cmd = "BWIDth"
                    
                    class RESolution(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:PULSe:TIME:BWIDth:RESolution
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#TIME_BWIDth>`_
                        """
                        _cmd = "RESolution"
                        
                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:TIME:STARt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#TIME_STARt>`_
                    """
                    _cmd = "STARt"
                    
                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PULSe:TIME:STOP
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_pulse.htm#TIME_STOP>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_roscillator.htm#EXTernal_FREQuency>`_
                    """
                    _cmd = "FREQuency"
                    
            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:ROSCillator:SOURce
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_roscillator.htm#SOURce>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#ADD>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#BWIDth>`_
                    """
                    _cmd = "RESolution"
                    
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:BWIDth:RESolution:CONTrol
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#BWIDth_CONTrol>`_
                        """
                        _cmd = "CONTrol"
                        
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:BWIDth:RESolution:SELect
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#BWIDth_SELect>`_
                        """
                        _cmd = "SELect"
                        
                        class CONTrol(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:SEGMent:BWIDth:RESolution:SELect:CONTrol
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#BWIDth_SELect_CONTrol>`_
                            """
                            _cmd = "CONTrol"
                            
            class CLEar(SCPINode, SCPISet):
                """
                `SENSe:SEGMent:CLEar
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#CLEAr>`_
                """
                _cmd = "CLEar"
                
            class COUNt(SCPINode, SCPIQuery):
                """
                `SENSe:SEGMent:COUNt
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#COUNt>`_
                """
                _cmd = "COUNt"
                
            class DEFine(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:DEFine
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#DEFine>`_
                """
                _cmd = "DEFine"
                
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:DEFine:SELect
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#DEFine_SELect>`_
                    """
                    _cmd = "SELect"
                    
            class DELete(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:DELete
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#DELete>`_
                """
                _cmd = "DELete"
                
                class ALL(SCPINode, SCPISet):
                    """
                    `SENSe:SEGMent:DELete:ALL
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#DELete_ALL>`_
                    """
                    _cmd = "ALL"
                    
                class DUMMy(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:SEGMent:DELete:DUMMy
                    """
                    _cmd = "DUMMy"
                    
            class FREQuency(SCPINode):
                """
                SENSe:SEGMent:FREQuency
                """
                _cmd = "FREQuency"
                
                class CENTer(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:CENTer
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#CENTer>`_
                    """
                    _cmd = "CENTer"
                    
                class SPAN(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:SPAN
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#SPAN>`_
                    """
                    _cmd = "SPAN"
                    
                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:STARt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#STARt>`_
                    """
                    _cmd = "STARt"
                    
                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:STOP
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#STOP>`_
                    """
                    _cmd = "STOP"
                    
            class INSert(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:INSert
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#INSert>`_
                """
                _cmd = "INSert"
                
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:INSert:SELect
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#OVERlap>`_
                    """
                    _cmd = "SELect"
                    
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:NAME
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#NAME>`_
                """
                _cmd = "NAME"
                
            class OVERlap(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:OVERlap
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#OVERlap>`_
                """
                _cmd = "OVERlap"
                
            class POWer(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SEGMent:POWer
                """
                _cmd = "POWer"
                
                class LEVel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:POWer:LEVel
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#POWer>`_
                    """
                    _cmd = "LEVel"
                    
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:POWer:LEVel:CONTrol
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#POWer_CONTrol>`_
                        """
                        _cmd = "CONTrol"
                        
            class SBANd(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:SBANd
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#SBANd>`_
                """
                _cmd = "SBANd"
                
                class CONTrol(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SBANd:CONTrol
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#SBANd_CONTrol>`_
                    """
                    _cmd = "CONTrol"
                    
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#STATe>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#DWELl>`_
                    """
                    _cmd = "DWELl"
                    
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:SWEep:DWELl:CONTrol
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#DWELl_CONTrol>`_
                        """
                        _cmd = "CONTrol"
                        
                class POINts(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:POINts
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#POINts>`_
                    """
                    _cmd = "POINts"
                    
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:TIME
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#TIME>`_
                    """
                    _cmd = "TIME"
                    
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:SWEep:TIME:CONTrol
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#TIME_CONTrol>`_
                        """
                        _cmd = "CONTrol"
                        
                    class SUM(SCPINode, SCPIQuery):
                        """
                        `SENSe:SEGMent:SWEep:TIME:SUM
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#TIME_SUM>`_
                        """
                        _cmd = "SUM"
                        
            class TRIGger(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SEGMent:TRIGger
                """
                _cmd = "TRIGger"
                
                class CONTrol(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:TRIGger:CONTrol
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#TRIGger_CONTrol>`_
                    """
                    _cmd = "CONTrol"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:TRIGger:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_segment.htm#TRIGger_STATe>`_
                    """
                    _cmd = "STATe"
                    
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___sweep.htm#AXIS_FREQuency>`_
                    """
                    _cmd = "FREQuency"
                    
                class POWer(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:AXIS:POWer
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___sweep.htm#AXIS_POWer>`_
                    """
                    _cmd = "POWer"
                    
            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SWEep:COUNt
                """
                _cmd = "COUNt"
                
            class DETector(SCPINode):
                """
                SENSe:SWEep:DETector
                """
                _cmd = "DETector"
                
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:DETector:TIME
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___sweep.htm#DETector_TIME>`_
                    """
                    _cmd = "TIME"
                    
            class DWELl(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:DWELl
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___sweep.htm#Dwell>`_
                """
                _cmd = "DWELl"
                
            class GENeration(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SWEep:GENeration
                """
                _cmd = "GENeration"
                
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SWEep:MODE
                """
                _cmd = "MODE"
                
            class POINts(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:POINts
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___sweep.htm>`_
                """
                _cmd = "POINts"
                
            class SPACing(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:SPACing
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___sweep.htm#SPACing>`_
                """
                _cmd = "SPACing"
                
            class SRCPort(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:SRCPort
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___sweep.htm#SRCPort>`_
                """
                _cmd = "SRCPort"
                
            class STEP(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:STEP
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___sweep.htm#STEP>`_
                """
                _cmd = "STEP"
                
            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:TIME
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___sweep.htm#Time>`_
                """
                _cmd = "TIME"
                
                class AUTO(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:TIME:AUTO
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___sweep.htm#TIME_Auto>`_
                    """
                    _cmd = "AUTO"
                    
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:TYPE
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_ch___sweep.htm#TYPE>`_
                """
                _cmd = "TYPE"
                
        class TEUNit(SCPINode):
            """
            SENSe:TEUNit
            """
            _cmd = "TEUNit"
            
            class AMONitor(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:TEUNit:AMONitor
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_teunit.htm#AMONitor>`_
                """
                _cmd = "AMONitor"
                
            class COMBiner(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:TEUNit:COMBiner
                """
                _cmd = "COMBiner"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:COMBiner:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_teunit.htm#COMBiner_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class LNAMplifier(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:TEUNit:LNAMplifier
                """
                _cmd = "LNAMplifier"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:LNAMplifier:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_teunit.htm#LNAMplifier_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class PAMPlifier(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:TEUNit:PAMPlifier
                """
                _cmd = "PAMPlifier"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:PAMPlifier:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_teunit.htm#PAMPlifier_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class PMODulator(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:TEUNit:PMODulator
                """
                _cmd = "PMODulator"
                
                class INVert(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:PMODulator:INVert
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_teunit.htm#PMODulator_INVert>`_
                    """
                    _cmd = "INVert"
                    
                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:PMODulator:SOURce
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_teunit.htm#PMODulator_SOURce>`_
                    """
                    _cmd = "SOURce"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:PMODulator:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_teunit.htm#PMODulator_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class REAR(SCPINodeN):
                """
                SENSe:TEUNit:REAR
                """
                _cmd = "REAR"
                
                class INVert(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:REAR:INVert
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_teunit.htm#REAR_INVert>`_
                    """
                    _cmd = "INVert"
                    
                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:REAR:SOURce
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_teunit.htm#REAR_SOURce>`_
                    """
                    _cmd = "SOURce"
                    
            class UMEas(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:TEUNit:UMEas
                """
                _cmd = "UMEas"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:UMEas:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_teunit.htm#UMEas_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class USOurce(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:TEUNit:USOurce
                """
                _cmd = "USOurce"
                
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:TEUNit:USOurce:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_teunit.htm#USOurce_STATe>`_
                    """
                    _cmd = "STATe"
                    
        class UDSParams(SCPINodeN):
            """
            SENSe:UDSParams
            """
            _cmd = "UDSParams"
            
            class ACTive(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:UDSParams:ACTive
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_udsparams.htm#ACTive>`_
                """
                _cmd = "ACTive"
                
            class PARam(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:UDSParams:PARam
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/sense/sense_udsparams.htm#PARam>`_
                """
                _cmd = "PARam"
                
    class SOURce(SCPINodeN):
        """
        SOURce
        """
        _cmd = "SOURce"
        
        class CMODe(SCPINode):
            """
            SOURce:CMODe
            """
            _cmd = "CMODe"
            
            class PORT(SCPINodeN, SCPIQuery, SCPISet):
                """
                SOURce:CMODe:PORT
                """
                _cmd = "PORT"
                
                class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:CMODe:PORT:AMPLitude
                    """
                    _cmd = "AMPLitude"
                    
                class PHASe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:CMODe:PORT:PHASe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_cmode.htm#PORT_PHASe>`_
                    """
                    _cmd = "PHASe"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:CMODe:PORT:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_cmode.htm#PORT_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class RPORt(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:CMODe:RPORt
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_cmode.htm#REFerence_PORT>`_
                """
                _cmd = "RPORt"
                
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
                    
                    class CFRequency(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:ARBitrary:CFRequency
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#CONVersion_ARBitrary_CFRequency>`_
                        """
                        _cmd = "CFRequency"
                        
                    class EFRequency(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:ARBitrary:EFRequency
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#CONVersion_ARBitrary_EFRequency>`_
                        """
                        _cmd = "EFRequency"
                        
                    class IFRequency(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:ARBitrary:IFRequency
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#CONVersion_ARBitrary_IFRequency>`_
                        """
                        _cmd = "IFRequency"
                        
                class MIXer(SCPINode):
                    """
                    SOURce:FREQuency:CONVersion:MIXer
                    """
                    _cmd = "MIXer"
                    
                    class FUNDamental(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:FUNDamental
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#FREQuency_CONVersion_MIXer_FUNDamental>`_
                        """
                        _cmd = "FUNDamental"
                        
                    class PAFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PAFixed
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#FREQuency_CONVersion_MIXer_PAFIXed>`_
                        """
                        _cmd = "PAFixed"
                        
                    class PFIXed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PFIXed
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#FREQuency_CONVersion_MIXer_PFIXed>`_
                        """
                        _cmd = "PFIXed"
                        
                    class PMFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PMFixed
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#PMFixed>`_
                        """
                        _cmd = "PMFixed"
                        
                    class PMODe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PMODe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#PMODe>`_
                        """
                        _cmd = "PMODe"
                        
            class CW(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FREQuency:CW
                """
                _cmd = "CW"
                
            class FIXed(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:FREQuency:FIXed
                """
                _cmd = "FIXed"
                
        class GROup(SCPINodeN, SCPIQuery, SCPISet):
            """
            `SOURce:GROup
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#GROup>`_
            """
            _cmd = "GROup"
            
            class CLEar(SCPINode, SCPISet):
                """
                `SOURce:GROup:CLEar
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#GROup_CLEar>`_
                """
                _cmd = "CLEar"
                
            class COUNt(SCPINode, SCPIQuery):
                """
                `SOURce:GROup:COUNt
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#GROup_COUNt>`_
                """
                _cmd = "COUNt"
                
            class PORTs(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:GROup:PORTs
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#GROup_PORTs>`_
                """
                _cmd = "PORTs"
                
            class SIMultaneous(SCPINode, SCPIQuery, SCPISet):
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_CONDition>`_
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
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_MOFFset_BWFactor>`_
                            """
                            _cmd = "BWFactor"
                            
                        class DVALue(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:DVALue
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_MOFFset_DVALue>`_
                            """
                            _cmd = "DVALue"
                            
                        class MODE(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:MODE
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_MOFFset_MODE>`_
                            """
                            _cmd = "MODE"
                            
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:GROup:SIMultaneous:FOFFset:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_FOFFset_STATe>`_
                        """
                        _cmd = "STATe"
                        
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:GROup:SIMultaneous:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#GROup_SIMultaneous_STATe>`_
                    """
                    _cmd = "STATe"
                    
        class LPORt(SCPINodeN, SCPIQuery, SCPISet):
            """
            `SOURce:LPORt
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch.htm#LPORt>`_
            """
            _cmd = "LPORt"
            
            class CLEar(SCPINode, SCPISet):
                """
                SOURce:LPORt:CLEar
                """
                _cmd = "CLEar"
                
        class POWer(SCPINodeN, SCPIQuery, SCPISet):
            """
            SOURce:POWer
            """
            _cmd = "POWer"
            
            class ALC(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:ALC
                """
                _cmd = "ALC"
                
                class AUBW(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:AUBW
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#AUBW>`_
                    """
                    _cmd = "AUBW"
                    
                class BANDwidth(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:BANDwidth
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#BANDwidth>`_
                    """
                    _cmd = "BANDwidth"
                    
                class CLAMp(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:CLAMp
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#CLAMp>`_
                    """
                    _cmd = "CLAMp"
                    
                class CONTrol(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:CONTrol
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#CONTrol>`_
                    """
                    _cmd = "CONTrol"
                    
                class COUPle(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:COUPle
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#COUPle>`_
                    """
                    _cmd = "COUPle"
                    
                class CSTate(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:CSTate
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#CSTate>`_
                    """
                    _cmd = "CSTate"
                    
                class LPNoise(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:LPNoise
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#LPNoise>`_
                    """
                    _cmd = "LPNoise"
                    
                class PIParameter(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:PIParameter
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#PIParameter>`_
                    """
                    _cmd = "PIParameter"
                    
                    class GAIN(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:ALC:PIParameter:GAIN
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#PIParameter_GAIN>`_
                        """
                        _cmd = "GAIN"
                        
                    class ITIMe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:ALC:PIParameter:ITIMe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#PIParameter_ITIMe>`_
                        """
                        _cmd = "ITIMe"
                        
                class POFFset(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:POFFset
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#POFFset>`_
                    """
                    _cmd = "POFFset"
                    
                class RANGe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:RANGe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#RANGe>`_
                    """
                    _cmd = "RANGe"
                    
                class SOFFset(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:SOFFset
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#SOFFset>`_
                    """
                    _cmd = "SOFFset"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#STATe>`_
                    """
                    _cmd = "STATe"
                    
                class STOLerance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ALC:STOLerance
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_alc.htm#STOLerance>`_
                    """
                    _cmd = "STOLerance"
                    
            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:ATTenuation
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#ATTenuation>`_
                """
                _cmd = "ATTenuation"
                
                class AUTO(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ATTenuation:AUTO
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#ATTenuation_AUTO>`_
                    """
                    _cmd = "AUTO"
                    
                    class VALue(SCPINode, SCPIQuery):
                        """
                        `SOURce:POWer:ATTenuation:AUTO:VALue
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#ATTenuation_AUTO_VALue>`_
                        """
                        _cmd = "VALue"
                        
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:ATTenuation:MODE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#ATTenuation_MODE>`_
                    """
                    _cmd = "MODE"
                    
            class COMBiner(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:COMBiner
                """
                _cmd = "COMBiner"
                
            class CONVerter(SCPINode):
                """
                SOURce:POWer:CONVerter
                """
                _cmd = "CONVerter"
                
                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CONVerter:OFFSet
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#OFFSet>`_
                    """
                    _cmd = "OFFSet"
                    
                class TRANsfer(SCPINode):
                    """
                    SOURce:POWer:CONVerter:TRANsfer
                    """
                    _cmd = "TRANsfer"
                    
                    class AMODel(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:AMODel
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#TRANsfer_AMODel>`_
                        """
                        _cmd = "AMODel"
                        
                    class ATTenuator(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:ATTenuator
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#TRANsfer_ATTenuator>`_
                        """
                        _cmd = "ATTenuator"
                        
                    class DESCription(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:DESCription
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#TRANsfer_DESCription>`_
                        """
                        _cmd = "DESCription"
                        
                    class DSET(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:DSET
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#TRANsfer_DSET>`_
                        """
                        _cmd = "DSET"
                        
                    class ELECtronic(SCPINode):
                        """
                        SOURce:POWer:CONVerter:TRANsfer:ELECtronic
                        """
                        _cmd = "ELECtronic"
                        
                        class LIMit(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CONVerter:TRANsfer:ELECtronic:LIMit
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#TRANsfer_ELECtronic_LIMit>`_
                            """
                            _cmd = "LIMit"
                            
                        class MATTenuation(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CONVerter:TRANsfer:ELECtronic:MATTenuation
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#TRANsfer_ELECtronic_MATTenuation>`_
                            """
                            _cmd = "MATTenuation"
                            
                        class REDuction(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CONVerter:TRANsfer:ELECtronic:REDuction
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#TRANsfer_ELECtronic_REDuction>`_
                            """
                            _cmd = "REDuction"
                            
                    class MECHanical(SCPINode):
                        """
                        SOURce:POWer:CONVerter:TRANsfer:MECHanical
                        """
                        _cmd = "MECHanical"
                        
                        class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CONVerter:TRANsfer:MECHanical:ATTenuation
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#TRANsfer_MECHanical_ATTenuation>`_
                            """
                            _cmd = "ATTenuation"
                            
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:OFFSet
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#TRANsfer_OFFSet>`_
                        """
                        _cmd = "OFFSet"
                        
                    class PATH(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:PATH
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#TRANsfer_PATH>`_
                        """
                        _cmd = "PATH"
                        
                    class SLOPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CONVerter:TRANsfer:SLOPe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_power_converter.htm#TRANsfer_SLOPe>`_
                        """
                        _cmd = "SLOPe"
                        
            class CORRection(SCPINode, SCPISet):
                """
                SOURce:POWer:CORRection
                """
                _cmd = "CORRection"
                
                class ACQuire(SCPINode, SCPISet):
                    """
                    `SOURce:POWer:CORRection:ACQuire
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#ACQuire>`_
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
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#ACQuire_VERification_RESult>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire>`_
                        """
                        _cmd = "ACQuire"
                        
                        class VERification(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:CORRection:COLLect:ACQuire:VERification
                            """
                            _cmd = "VERification"
                            
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SOURce:POWer:CORRection:COLLect:ACQuire:VERification:STATe
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire_VERification_STATe>`_
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
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#COLLect_AVERage_COUNt>`_
                            """
                            _cmd = "COUNt"
                            
                        class NTOLerance(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:COLLect:AVERage:NTOLerance
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#COLLect_AVERage_NTOLerance>`_
                            """
                            _cmd = "NTOLerance"
                            
                    class CFACtor(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:CFACtor
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#COLLect_CFACtor>`_
                        """
                        _cmd = "CFACtor"
                        
                    class FLATness(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:FLATness
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire_VERification_STATe>`_
                        """
                        _cmd = "FLATness"
                        
                    class METHod(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:METHod
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#COLLect_METHod>`_
                        """
                        _cmd = "METHod"
                        
                    class PMReadings(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:PMReadings
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#COLLect_PMReadings>`_
                        """
                        _cmd = "PMReadings"
                        
                    class RRECeiver(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:RRECeiver
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#COLLect_ACQuire_VERification_STATe>`_
                        """
                        _cmd = "RRECeiver"
                        
                class CONVerter(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:CORRection:CONVerter
                    """
                    _cmd = "CONVerter"
                    
                    class LEVel(SCPINode):
                        """
                        SOURce:POWer:CORRection:CONVerter:LEVel
                        """
                        _cmd = "LEVel"
                        
                        class OFFSet(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:CONVerter:LEVel:OFFSet
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#CONVerter_LEVel_OFFset>`_
                            """
                            _cmd = "OFFSet"
                            
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:CONVerter:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#CONVerter_STATe>`_
                        """
                        _cmd = "STATe"
                        
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:DATA
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#DATA>`_
                    """
                    _cmd = "DATA"
                    
                    class PARameter(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:DATA:PARameter
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#DATA_PARameter>`_
                        """
                        _cmd = "PARameter"
                        
                        class COUNt(SCPINode, SCPIQuery):
                            """
                            `SOURce:POWer:CORRection:DATA:PARameter:COUNt
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#DATA_PARameter_COUNt>`_
                            """
                            _cmd = "COUNt"
                            
                class DEFault(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:DEFault
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#CORRection_DEFault>`_
                    """
                    _cmd = "DEFault"
                    
                class FAST(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:FAST
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#FAST>`_
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
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#GENerator_LEVel_OFFset>`_
                            """
                            _cmd = "OFFSet"
                            
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:GENerator:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#GENerator_STATe>`_
                        """
                        _cmd = "STATe"
                        
                class HARMonic(SCPINode, SCPISet):
                    """
                    SOURce:POWer:CORRection:HARMonic
                    """
                    _cmd = "HARMonic"
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SOURce:POWer:CORRection:HARMonic:ACQuire
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#HARMonic_ACQuire>`_
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
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#IMODulation_LOWer_ACQuire>`_
                            """
                            _cmd = "ACQuire"
                            
                    class RPORt(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:IMODulation:RPORt
                        """
                        _cmd = "RPORt"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:IMODulation:RPORt:ACQuire
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#IMODulation_RPORt_ACQuire>`_
                            """
                            _cmd = "ACQuire"
                            
                    class SPORts(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:IMODulation:SPORts
                        """
                        _cmd = "SPORts"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:IMODulation:SPORts:ACQuire
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#IMODulation_SPORts_ACQuire>`_
                            """
                            _cmd = "ACQuire"
                            
                    class UTONe(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:IMODulation:UTONe
                        """
                        _cmd = "UTONe"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:IMODulation:UTONe:ACQuire
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#IMODulation_UPPer_ACQuire>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#LEVel_OFFset>`_
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
                            `SOURce:POWer:CORRection:MIXer:IF:ACQuire
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#MIXer_IF_ACQuire>`_
                            """
                            _cmd = "ACQuire"
                            
                    class LO(SCPINodeN, SCPISet):
                        """
                        SOURce:POWer:CORRection:MIXer:LO
                        """
                        _cmd = "LO"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:MIXer:LO:ACQuire
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#MIXer_LO_ACQuire>`_
                            """
                            _cmd = "ACQuire"
                            
                    class RF(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:MIXer:RF
                        """
                        _cmd = "RF"
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:MIXer:RF:ACQuire
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#MIXer_RF_ACQuire>`_
                            """
                            _cmd = "ACQuire"
                            
                        class NFIGure(SCPINode, SCPISet):
                            """
                            SOURce:POWer:CORRection:MIXer:RF:NFIGure
                            """
                            _cmd = "NFIGure"
                            
                            class ACQuire(SCPINode, SCPISet):
                                """
                                `SOURce:POWer:CORRection:MIXer:RF:NFIGure:ACQuire
                                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#MIXer_RF_NFIGure_ACQuire>`_
                                """
                                _cmd = "ACQuire"
                                
                class NREadings(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:NREadings
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#NREadings>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#OSOurces_STATe>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#PMETer_ID>`_
                        """
                        _cmd = "ID"
                        
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction.htm#STATe>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#CALibration>`_
                        """
                        _cmd = "CALibration"
                        
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:COUNt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#COUNt>`_
                        """
                        _cmd = "COUNt"
                        
                    class DEFine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:DEFine
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#DEFine>`_
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
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#DELete_ALL>`_
                            """
                            _cmd = "ALL"
                            
                        class DUMMy(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:TCOefficient:DELete:DUMMy
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#DELete>`_
                            """
                            _cmd = "DUMMy"
                            
                    class FEED(SCPINode, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:FEED
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#FEED>`_
                        """
                        _cmd = "FEED"
                        
                    class INSert(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:INSert
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#INSert>`_
                        """
                        _cmd = "INSert"
                        
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power_correction_tcoefficient.htm#STATe>`_
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
                        `SOURce:POWer:GENerator:LLIMit:STATe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#GENerator_LLIMit_Enable>`_
                        """
                        _cmd = "STATe"
                        
                    class VALue(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:GENerator:LLIMit:VALue
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#GENerator_LLIMit_VALue>`_
                        """
                        _cmd = "VALue"
                        
                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:GENerator:OFFSet
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_GENerator_OFFSet>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_GENerator_PERManent_STATe>`_
                        """
                        _cmd = "STATe"
                        
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:GENerator:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_GENerator_STATe>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_LEVel>`_
                        """
                        _cmd = "AMPLitude"
                        
                    class LLIMit(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:LEVel:IMMediate:LLIMit
                        """
                        _cmd = "LLIMit"
                        
                        class DGRaccess(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:LEVel:IMMediate:LLIMit:DGRaccess
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_LLIMit_DGRaccess>`_
                            """
                            _cmd = "DGRaccess"
                            
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:LEVel:IMMediate:LLIMit:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_LLIMit_Enable>`_
                            """
                            _cmd = "STATe"
                            
                        class VALue(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:LEVel:IMMediate:LLIMit:VALue
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_LLIMit_VALue>`_
                            """
                            _cmd = "VALue"
                            
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:OFFSet
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_OFFSet>`_
                        """
                        _cmd = "OFFSet"
                        
                    class PHASe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:PHASe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_PHASe>`_
                        """
                        _cmd = "PHASe"
                        
                    class SLOPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:SLOPe
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_SLOPe>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_PERManent_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class REDuce(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:REDuce
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_REDuce>`_
                """
                _cmd = "REDuce"
                
            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:STARt
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_STARt>`_
                """
                _cmd = "STARt"
                
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_STATe>`_
                """
                _cmd = "STATe"
                
            class STOP(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:STOP
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__power__level_.htm#POWer_STOP>`_
                """
                _cmd = "STOP"
                
        class TDIF(SCPINode, SCPIQuery, SCPISet):
            """
            SOURce:TDIF
            """
            _cmd = "TDIF"
            
            class CRFRequency(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:TDIF:CRFRequency
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__tdif.htm#CRFRequency>`_
                """
                _cmd = "CRFRequency"
                
            class IMBalance(SCPINode):
                """
                SOURce:TDIF:IMBalance
                """
                _cmd = "IMBalance"
                
                class AMPLitude(SCPINode):
                    """
                    SOURce:TDIF:IMBalance:AMPLitude
                    """
                    _cmd = "AMPLitude"
                    
                    class LPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:AMPLitude:LPORt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__tdif.htm#IMBalance_AMPlitude_LPORt>`_
                        """
                        _cmd = "LPORt"
                        
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:AMPLitude:STARt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__tdif.htm#IMBalance_AMPlitude_STARt>`_
                        """
                        _cmd = "STARt"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:AMPLitude:STOP
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__tdif.htm#IMBalance_AMPlitude_STOP>`_
                        """
                        _cmd = "STOP"
                        
                class PHASe(SCPINode):
                    """
                    SOURce:TDIF:IMBalance:PHASe
                    """
                    _cmd = "PHASe"
                    
                    class LPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:PHASe:LPORt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__tdif.htm#IMBalance_PHASe_LPORt>`_
                        """
                        _cmd = "LPORt"
                        
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:PHASe:STARt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__tdif.htm#IMBalance_PHASe_STARt>`_
                        """
                        _cmd = "STARt"
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:TDIF:IMBalance:PHASe:STOP
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__tdif.htm#IMBalance_PHASe_STOP>`_
                        """
                        _cmd = "STOP"
                        
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:TDIF:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__tdif.htm#TDIF_STATe>`_
                """
                _cmd = "STATe"
                
            class WAVes(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:TDIF:WAVes
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/source/source_ch__tdif.htm#TDIF_WAVes>`_
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
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#PRESet>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#QUES_CONDition>`_
                """
                _cmd = "CONDition"
                
            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:ENABle
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#QUES_ENABle>`_
                """
                _cmd = "ENABle"
                
            class EVENt(SCPINode, SCPIQuery):
                """
                `STATus:QUEStionable:EVENt
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#LIMit_EVENt>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#INTegrity_CONDition>`_
                    """
                    _cmd = "CONDition"
                    
                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:ENABle
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#INTegrity_ENABle>`_
                    """
                    _cmd = "ENABle"
                    
                class EVENt(SCPINode, SCPIQuery):
                    """
                    `STATus:QUEStionable:INTegrity:EVENt
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#INTegrity_EVENt>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#INTegrity_HARDware_CONDition>`_
                        """
                        _cmd = "CONDition"
                        
                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:ENABle
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#INTegrity_HARDware_ENABle>`_
                        """
                        _cmd = "ENABle"
                        
                    class EVENt(SCPINode, SCPIQuery):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:EVENt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#INTegrity_HARDware_EVENt>`_
                        """
                        _cmd = "EVENt"
                        
                    class NTRansition(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:NTRansition
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#INTegrity_HARDware_NTRansition>`_
                        """
                        _cmd = "NTRansition"
                        
                    class PTRansition(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:PTRansition
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#INTegrity_HARDware_PTRansition>`_
                        """
                        _cmd = "PTRansition"
                        
                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:NTRansition
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#INTegrity_NTRansition>`_
                    """
                    _cmd = "NTRansition"
                    
                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:PTRansition
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#INTegrity_PTRansition>`_
                    """
                    _cmd = "PTRansition"
                    
            class LIMit(SCPINodeN, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:LIMit
                """
                _cmd = "LIMit"
                
                class CONDition(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:LIMit:CONDition
                    """
                    _cmd = "CONDition"
                    
                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:LIMit:ENABle
                    """
                    _cmd = "ENABle"
                    
                class EVENt(SCPINode, SCPIQuery):
                    """
                    STATus:QUEStionable:LIMit:EVENt
                    """
                    _cmd = "EVENt"
                    
                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:LIMit:NTRansition
                    """
                    _cmd = "NTRansition"
                    
                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:LIMit:PTRansition
                    """
                    _cmd = "PTRansition"
                    
            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:NTRansition
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#QUES_NTRansition>`_
                """
                _cmd = "NTRansition"
                
            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:PTRansition
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#QUES_PTRansition>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/status/status.htm#QUEue>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#AKAL_CONNection>`_
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#AKAL_MMEMory__STATe_>`_
                        """
                        _cmd = "STATe"
                        
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
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#ADDRess>`_
                        """
                        _cmd = "ADDRess"
                        
                    class RTERminator(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:GPIB:SELF:RTERminator
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RTERminator>`_
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
                    `SYSTem:COMMunicate:NET:HOSTname
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#NET_HOSTNAME>`_
                    """
                    _cmd = "HOSTname"
                    
            class RDEVice(SCPINode):
                """
                SYSTem:COMMunicate:RDEVice
                """
                _cmd = "RDEVice"
                
                class AKAL(SCPINode):
                    """
                    SYSTem:COMMunicate:RDEVice:AKAL
                    """
                    _cmd = "AKAL"
                    
                    class ADDRess(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:ADDRess
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_AKAL_ADDRess>`_
                        """
                        _cmd = "ADDRess"
                        
                        class ALL(SCPINode, SCPIQuery):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:ADDRess:ALL
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_AKAL_ADDRess_ALL>`_
                            """
                            _cmd = "ALL"
                            
                    class PREDuction(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:PREDuction
                        """
                        _cmd = "PREDuction"
                        
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:PREDuction:STATe
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#AKAL_PREDuction__STATe>`_
                            """
                            _cmd = "STATe"
                            
                class EUNit(SCPINode):
                    """
                    SYSTem:COMMunicate:RDEVice:EUNit
                    """
                    _cmd = "EUNit"
                    
                    class IDN(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:EUNit:IDN
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_EUNit_IDN>`_
                        """
                        _cmd = "IDN"
                        
                    class OPT(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:EUNit:OPT
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_EUNit_OPT>`_
                        """
                        _cmd = "OPT"
                        
                class GENerator(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:GENerator
                    """
                    _cmd = "GENerator"
                    
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:CATalog
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_GENerator_CATalog>`_
                        """
                        _cmd = "CATalog"
                        
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:COUNt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_GENerator_COUNt>`_
                        """
                        _cmd = "COUNt"
                        
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:DEFine
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_GENerator_DEFine>`_
                        """
                        _cmd = "DEFine"
                        
                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:DELete
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_GENerator_DELete>`_
                        """
                        _cmd = "DELete"
                        
                class PMETer(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:PMETer
                    """
                    _cmd = "PMETer"
                    
                    class AZERo(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:AZERo
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_PMETer_AZERo>`_
                        """
                        _cmd = "AZERo"
                        
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:CATalog
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_PMETer_CATalog>`_
                        """
                        _cmd = "CATalog"
                        
                    class CONFigure(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:PMETer:CONFigure
                        """
                        _cmd = "CONFigure"
                        
                        class AUTO(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:PMETer:CONFigure:AUTO
                            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_PMETer_CONFigure_AUTO>`_
                            """
                            _cmd = "AUTO"
                            
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                """
                                SYSTem:COMMunicate:RDEVice:PMETer:CONFigure:AUTO:STATe
                                """
                                _cmd = "STATe"
                                
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:COUNt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_PMETer_COUNt>`_
                        """
                        _cmd = "COUNt"
                        
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:DEFine
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_PMETer_DEFine>`_
                        """
                        _cmd = "DEFine"
                        
                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:DELete
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_PMETer_DELete>`_
                        """
                        _cmd = "DELete"
                        
                class RECeiver(SCPINode):
                    """
                    SYSTem:COMMunicate:RDEVice:RECeiver
                    """
                    _cmd = "RECeiver"
                    
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:RECeiver:DEFine
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_RECeiver_DEFine>`_
                        """
                        _cmd = "DEFine"
                        
                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:RECeiver:DELete
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_RECeiver_DELete>`_
                        """
                        _cmd = "DELete"
                        
                class TEUNit(SCPINode):
                    """
                    SYSTem:COMMunicate:RDEVice:TEUNit
                    """
                    _cmd = "TEUNit"
                    
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:TEUNit:COUNt
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_TEUNit_COUNt>`_
                        """
                        _cmd = "COUNt"
                        
                    class IDN(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:TEUNit:IDN
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_TEUNit_IDN>`_
                        """
                        _cmd = "IDN"
                        
                    class OPT(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:TEUNit:OPT
                        <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#RDEVice_TEUNit_OPT>`_
                        """
                        _cmd = "OPT"
                        
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
                    `SYSTem:CORRection:FMPort:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#CORRection_FMPort_STATe>`_
                    """
                    _cmd = "STATe"
                    
        class DATA(SCPINode):
            """
            SYSTem:DATA
            """
            _cmd = "DATA"
            
            class SIZE(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:DATA:SIZE
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#DATA_SIZE>`_
                """
                _cmd = "SIZE"
                
        class DATE(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:DATE
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#DATE>`_
            """
            _cmd = "DATE"
            
        class DISPlay(SCPINode):
            """
            SYSTem:DISPlay
            """
            _cmd = "DISPlay"
            
            class COLor(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:DISPlay:COLor
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#DISPlay_COLor>`_
                """
                _cmd = "COLor"
                
            class UPDate(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:DISPlay:UPDate
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#DISPlay_UPDate>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#ERRor_ALL>`_
                """
                _cmd = "ALL"
                
            class DISPlay(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:ERRor:DISPlay
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#ERRor_DISPlay>`_
                """
                _cmd = "DISPlay"
                
            class NEXT(SCPINode, SCPIQuery):
                """
                `SYSTem:ERRor:NEXT
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#ERRor_NEXT>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#FIRMware_UPDate>`_
                """
                _cmd = "UPDate"
                
        class FPReset(SCPINode, SCPISet):
            """
            `SYSTem:FPReset
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#FPReset>`_
            """
            _cmd = "FPReset"
            
        class FREQuency(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:FREQuency
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#FREQuency_>`_
            """
            _cmd = "FREQuency"
            
        class IDENtify(SCPINode):
            """
            SYSTem:IDENtify
            """
            _cmd = "IDENtify"
            
            class FACTory(SCPINode, SCPISet):
                """
                `SYSTem:IDENtify:FACTory
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#IDENtify_FACTory>`_
                """
                _cmd = "FACTory"
                
            class STRing(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:IDENtify:STRing
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#IDENtify_STRing>`_
                """
                _cmd = "STRing"
                
        class KLOCk(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:KLOCk
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#KLOCk>`_
            """
            _cmd = "KLOCk"
            
        class LANGuage(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:LANGuage
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#LANGuage>`_
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
                    SYSTem:LOGGing:REMote:STATe
                    """
                    _cmd = "STATe"
                    
        class NOPeration(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:NOPeration
            """
            _cmd = "NOPeration"
            
        class PASSword(SCPINode, SCPISet):
            """
            SYSTem:PASSword
            """
            _cmd = "PASSword"
            
            class CENable(SCPINode, SCPISet):
                """
                `SYSTem:PASSword:CENable
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#PASSword_ENABle>`_
                """
                _cmd = "CENable"
                
        class PRESet(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:PRESet
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#PRESet>`_
            """
            _cmd = "PRESet"
            
            class DUMMy(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:PRESet:DUMMy
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#PRESet_REMote_STATe>`_
                    """
                    _cmd = "STATe"
                    
            class SCOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:PRESet:SCOPe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#PRESet_SCOPe>`_
                """
                _cmd = "SCOPe"
                
            class USER(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:PRESet:USER
                """
                _cmd = "USER"
                
                class NAME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:PRESet:USER:NAME
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#PRESet_USER_NAME>`_
                    """
                    _cmd = "NAME"
                    
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:PRESet:USER:STATe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#PRESet_USER>`_
                    """
                    _cmd = "STATe"
                    
        class PRIority(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:PRIority
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#PRIority>`_
            """
            _cmd = "PRIority"
            
        class SETTings(SCPINode):
            """
            SYSTem:SETTings
            """
            _cmd = "SETTings"
            
            class UPDate(SCPINode, SCPISet):
                """
                SYSTem:SETTings:UPDate
                """
                _cmd = "UPDate"
                
        class SHUTdown(SCPINode, SCPISet):
            """
            `SYSTem:SHUTdown
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#SHUTdown>`_
            """
            _cmd = "SHUTdown"
            
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#SOUNd_ALARm__STATe_>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#SOUNd_STATus__STATe_1>`_
                    """
                    _cmd = "STATe"
                    
        class TIME(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:TIME
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#TIME>`_
            """
            _cmd = "TIME"
            
        class TRESet(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:TRESet
            """
            _cmd = "TRESet"
            
            class STATe(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:TRESet:STATe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#TRESet_STATe>`_
                """
                _cmd = "STATe"
                
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
                    `SYSTem:USER:DISPlay:TITLe
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#USER_DISPlay_TITle>`_
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
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#USER_KEY>`_
                """
                _cmd = "KEY"
                
                class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:USER:KEY:FUNCtion
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#USER_KEY_FUNCtion>`_
                    """
                    _cmd = "FUNCtion"
                    
        class VERSion(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:VERSion
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/system/system.htm#VERSion_>`_
            """
            _cmd = "VERSion"
            
        class WAIT(SCPINode, SCPIQuery, SCPISet):
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
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trace/trace.htm#CLEar>`_
            """
            _cmd = "CLEar"
            
        class COPY(SCPINode, SCPISet):
            """
            `TRACe:COPY
            <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trace/trace.htm#COPY>`_
            """
            _cmd = "COPY"
            
            class MATH(SCPINode, SCPISet):
                """
                `TRACe:COPY:MATH
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trace/trace.htm#COPY_MATH>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trace/trace.htm#RESPonse>`_
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
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trace/trace.htm#STIMulus>`_
                    """
                    _cmd = "ALL"
                    
    class TRIGger(SCPINodeN):
        """
        TRIGger
        """
        _cmd = "TRIGger"
        
        class SEQuence(SCPINode):
            """
            TRIGger:SEQuence
            """
            _cmd = "SEQuence"
            
            class HOLDoff(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:HOLDoff
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trigger/trigger.htm#HOLDoff>`_
                """
                _cmd = "HOLDoff"
                
                class GENerator(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:HOLDoff:GENerator
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trigger/trigger.htm#HOLDoff_GENerator>`_
                    """
                    _cmd = "GENerator"
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:HOLDoff:MODE
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trigger/trigger.htm#HOLDoff_MODE>`_
                    """
                    _cmd = "MODE"
                    
                class PORT(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:HOLDoff:PORT
                    <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trigger/trigger.htm#HOLDoff_PORT>`_
                    """
                    _cmd = "PORT"
                    
            class LINK(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:LINK
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trigger/trigger.htm#LINK>`_
                """
                _cmd = "LINK"
                
            class PULSe(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:PULSe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trigger/trigger.htm#PULSe>`_
                """
                _cmd = "PULSe"
                
            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:SLOPe
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trigger/trigger.htm#SLOPe>`_
                """
                _cmd = "SLOPe"
                
            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:SOURce
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trigger/trigger.htm#SOURce>`_
                """
                _cmd = "SOURce"
                
            class TIMer(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:TIMer
                <https://www.rohde-schwarz.com/webhelp/webhelp_zva_5/scpi_reference/trigger/trigger.htm#TIMer>`_
                """
                _cmd = "TIMer"
                
    # END OF ZVA_gen
