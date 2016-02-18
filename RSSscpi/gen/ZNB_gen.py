# -*- coding: utf-8 -*-
# Generated from ZNB_commands_2_56.inp on 2016-02-18 13:44
from SCPI_gen_support import Instrument, SCPINode, SCPINodeN, SCPIQuery, SCPISet
class ZNB_gen(Instrument):
    class CAL(SCPINode, SCPIQuery):
        _cmd = "*CAL"
    class CLS(SCPINode, SCPISet):
        _cmd = "*CLS"
    class ESE(SCPINode, SCPIQuery, SCPISet):
        _cmd = "*ESE"
    class ESR(SCPINode, SCPIQuery, SCPISet):
        _cmd = "*ESR"
    class IDN(SCPINode, SCPIQuery):
        _cmd = "*IDN"
    class IST(SCPINode, SCPIQuery, SCPISet):
        _cmd = "*IST"
    class OPC(SCPINode, SCPIQuery, SCPISet):
        _cmd = "*OPC"
    class OPT(SCPINode, SCPIQuery):
        _cmd = "*OPT"
    class PCB(SCPINode, SCPISet):
        _cmd = "*PCB"
    class PRE(SCPINode, SCPIQuery, SCPISet):
        _cmd = "*PRE"
    class PSC(SCPINode, SCPIQuery, SCPISet):
        _cmd = "*PSC"
    class RST(SCPINode, SCPISet):
        _cmd = "*RST"
    class SRE(SCPINode, SCPIQuery, SCPISet):
        _cmd = "*SRE"
    class STB(SCPINode, SCPIQuery):
        _cmd = "*STB"
    class TRG(SCPINode, SCPISet):
        _cmd = "*TRG"
    class TST(SCPINode, SCPIQuery):
        _cmd = "*TST"
    class WAI(SCPINode, SCPISet):
        _cmd = "*WAI"
    class DCL(SCPINode, SCPIQuery, SCPISet):
        _cmd = "@DCL"
    class GET(SCPINode, SCPIQuery, SCPISet):
        _cmd = "@GET"
    class LOC(SCPINode, SCPIQuery, SCPISet):
        _cmd = "@LOC"
    class REM(SCPINode, SCPIQuery, SCPISet):
        _cmd = "@REM"
    class ABORt(SCPINode, SCPISet):
        _cmd = "ABORt"
    class CALCulate(SCPINodeN):
        _cmd = "CALCulate"
        class CLIMits(SCPINode):
            _cmd = "CLIMits"
            class FAIL(SCPINode, SCPIQuery):
                _cmd = "FAIL"
        class DATA(SCPINode, SCPIQuery, SCPISet):
            _cmd = "DATA"
            class ALL(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ALL"
            class CALL(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CALL"
                class CATalog(SCPINode, SCPIQuery):
                    _cmd = "CATalog"
            class CHANnel(SCPINode):
                _cmd = "CHANnel"
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ALL"
                class DALL(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DALL"
            class DALL(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DALL"
            class NSWeep(SCPINode, SCPIQuery, SCPISet):
                _cmd = "NSWeep"
                class COUNt(SCPINode, SCPIQuery):
                    _cmd = "COUNt"
                class FIRSt(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FIRSt"
                class LAST(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LAST"
            class SGRoup(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SGRoup"
            class STIMulus(SCPINode, SCPIQuery):
                _cmd = "STIMulus"
            class TRACe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "TRACe"
        class DLINe(SCPINode, SCPIQuery, SCPISet):
            _cmd = "DLINe"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
        class FILTer(SCPINode):
            _cmd = "FILTer"
            class GATE(SCPINode):
                _cmd = "GATE"
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TIME"
                    class AOFFset(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "AOFFset"
                    class CENTer(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "CENTer"
                    class DCHebyshev(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DCHebyshev"
                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SHAPe"
                    class SHOW(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SHOW"
                    class SPAN(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SPAN"
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STARt"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STOP"
                    class TYPE(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "TYPE"
                    class WINDow(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WINDow"
        class FORMat(SCPINode, SCPIQuery, SCPISet):
            _cmd = "FORMat"
            class WQUType(SCPINode, SCPIQuery, SCPISet):
                _cmd = "WQUType"
        class GDAPerture(SCPINode):
            _cmd = "GDAPerture"
            class SCOunt(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SCOunt"
        class LDEViation(SCPINode):
            _cmd = "LDEViation"
            class AUTO(SCPINode, SCPISet):
                _cmd = "AUTO"
            class CONStant(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CONStant"
            class ELENgth(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ELENgth"
            class MODE(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MODE"
            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SLOPe"
        class LIMit(SCPINodeN):
            _cmd = "LIMit"
            class CIRCle(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CIRCle"
                class CLEar(SCPINode, SCPISet):
                    _cmd = "CLEar"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                class DISPlay(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DISPlay"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class FAIL(SCPINode, SCPIQuery):
                    _cmd = "FAIL"
                    class ALL(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "ALL"
                class SOUNd(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SOUNd"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class CLEar(SCPINode, SCPISet):
                _cmd = "CLEar"
            class CONTrol(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CONTrol"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                class DOMain(SCPINode, SCPISet):
                    _cmd = "DOMain"
                class SHIFt(SCPINode, SCPISet):
                    _cmd = "SHIFt"
            class DATA(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DATA"
            class DELete(SCPINode):
                _cmd = "DELete"
                class ALL(SCPINode, SCPISet):
                    _cmd = "ALL"
            class DISPlay(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DISPlay"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class FAIL(SCPINode, SCPIQuery):
                _cmd = "FAIL"
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ALL"
            class LOWer(SCPINode, SCPIQuery, SCPISet):
                _cmd = "LOWer"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                class FEED(SCPINode, SCPISet):
                    _cmd = "FEED"
                class SHIFt(SCPINode, SCPISet):
                    _cmd = "SHIFt"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class RDOMain(SCPINode):
                _cmd = "RDOMain"
                class COMPlex(SCPINode, SCPISet):
                    _cmd = "COMPlex"
                class FORMat(SCPINode, SCPISet):
                    _cmd = "FORMat"
                class SPACing(SCPINode, SCPISet):
                    _cmd = "SPACing"
            class SEGMent(SCPINodeN):
                _cmd = "SEGMent"
                class AMPLitude(SCPINode):
                    _cmd = "AMPLitude"
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STARt"
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STOP"
                class COUNt(SCPINode, SCPIQuery):
                    _cmd = "COUNt"
                class STIMulus(SCPINode):
                    _cmd = "STIMulus"
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STARt"
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STOP"
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TYPE"
            class SOUNd(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SOUNd"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "AREA"
            class TTLout(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "TTLout"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class UPPer(SCPINode, SCPIQuery, SCPISet):
                _cmd = "UPPer"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                class FEED(SCPINode, SCPISet):
                    _cmd = "FEED"
                class SHIFt(SCPINode, SCPISet):
                    _cmd = "SHIFt"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
        class MARKer(SCPINodeN, SCPIQuery, SCPISet):
            _cmd = "MARKer"
            class AOFF(SCPINode, SCPISet):
                _cmd = "AOFF"
            class BWIDth(SCPINode, SCPIQuery, SCPISet):
                _cmd = "BWIDth"
            class COUPled(SCPINode, SCPIQuery, SCPISet):
                _cmd = "COUPled"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class DEFault(SCPINode):
                _cmd = "DEFault"
                class FORMat(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FORMat"
            class DELTa(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DELTa"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class FORMat(SCPINode, SCPIQuery, SCPISet):
                _cmd = "FORMat"
            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                _cmd = "FUNCtion"
                class APEak(SCPINode):
                    _cmd = "APEak"
                    class THReshold(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "THReshold"
                class BWIDth(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "BWIDth"
                    class GMCenter(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "GMCenter"
                    class MODE(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MODE"
                class CENTer(SCPINode, SCPISet):
                    _cmd = "CENTer"
                class DELTa(SCPINode):
                    _cmd = "DELTa"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class DOMain(SCPINode):
                    _cmd = "DOMain"
                    class USER(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "USER"
                        class RANGe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "RANGe"
                        class SHOW(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SHOW"
                        class STARt(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STARt"
                        class STOP(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STOP"
                class EXECute(SCPINode, SCPISet):
                    _cmd = "EXECute"
                class RESult(SCPINode, SCPIQuery):
                    _cmd = "RESult"
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SELect"
                class SPAN(SCPINode, SCPISet):
                    _cmd = "SPAN"
                class STARt(SCPINode, SCPISet):
                    _cmd = "STARt"
                class STOP(SCPINode, SCPISet):
                    _cmd = "STOP"
                class TARGet(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TARGet"
            class MAXimum(SCPINode, SCPISet):
                _cmd = "MAXimum"
            class MINimum(SCPINode, SCPISet):
                _cmd = "MINimum"
            class MODE(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MODE"
            class NAME(SCPINode, SCPIQuery, SCPISet):
                _cmd = "NAME"
            class REFerence(SCPINode, SCPIQuery, SCPISet):
                _cmd = "REFerence"
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MODE"
                class NAME(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "NAME"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TYPE"
                class X(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "X"
                class Y(SCPINode, SCPIQuery):
                    _cmd = "Y"
            class SEARch(SCPINode, SCPISet):
                _cmd = "SEARch"
                class BFILter(SCPINode):
                    _cmd = "BFILter"
                    class RESult(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "RESult"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                            class AREA(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "AREA"
                class FORMat(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FORMat"
                class IMMediate(SCPINode, SCPISet):
                    _cmd = "IMMediate"
                class LEFT(SCPINode, SCPISet):
                    _cmd = "LEFT"
                class NEXT(SCPINode, SCPISet):
                    _cmd = "NEXT"
                class RIGHt(SCPINode, SCPISet):
                    _cmd = "RIGHt"
                class TRACking(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TRACking"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "AREA"
            class TARGet(SCPINode, SCPIQuery, SCPISet):
                _cmd = "TARGet"
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                _cmd = "TYPE"
            class X(SCPINode, SCPIQuery, SCPISet):
                _cmd = "X"
            class Y(SCPINode, SCPIQuery):
                _cmd = "Y"
        class MATH(SCPINode, SCPIQuery, SCPISet):
            _cmd = "MATH"
            class EXPRession(SCPINode, SCPIQuery, SCPISet):
                _cmd = "EXPRession"
                class DEFine(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DEFine"
                class SDEFine(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SDEFine"
            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                _cmd = "FUNCtion"
            class MEMorize(SCPINode, SCPISet):
                _cmd = "MEMorize"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
            class WUNit(SCPINode, SCPIQuery, SCPISet):
                _cmd = "WUNit"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
        class PARameter(SCPINode):
            _cmd = "PARameter"
            class CATalog(SCPINode, SCPIQuery):
                _cmd = "CATalog"
                class SENDed(SCPINode, SCPIQuery):
                    _cmd = "SENDed"
            class DEFine(SCPINode, SCPISet):
                _cmd = "DEFine"
                class SGRoup(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SGRoup"
            class DELete(SCPINode, SCPISet):
                _cmd = "DELete"
                class ALL(SCPINode, SCPISet):
                    _cmd = "ALL"
                class CALL(SCPINode, SCPISet):
                    _cmd = "CALL"
                class CMEMory(SCPINode, SCPISet):
                    _cmd = "CMEMory"
                class MEMory(SCPINode, SCPISet):
                    _cmd = "MEMory"
                class SGRoup(SCPINode, SCPISet):
                    _cmd = "SGRoup"
            class MEASure(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MEASure"
                class SENDed(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SENDed"
            class SDEFine(SCPINode, SCPISet):
                _cmd = "SDEFine"
                class SENDed(SCPINode, SCPISet):
                    _cmd = "SENDed"
            class SELect(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SELect"
        class PHOLd(SCPINode, SCPIQuery, SCPISet):
            _cmd = "PHOLd"
        class RIPPle(SCPINode):
            _cmd = "RIPPle"
            class CLEar(SCPINode, SCPISet):
                _cmd = "CLEar"
            class CONTrol(SCPINode):
                _cmd = "CONTrol"
                class DOMain(SCPINode, SCPISet):
                    _cmd = "DOMain"
            class DATA(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DATA"
            class DELete(SCPINode):
                _cmd = "DELete"
                class ALL(SCPINode, SCPISet):
                    _cmd = "ALL"
            class DISPlay(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DISPlay"
                class RESult(SCPINode):
                    _cmd = "RESult"
                    class ALL(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "ALL"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class FAIL(SCPINode, SCPIQuery):
                _cmd = "FAIL"
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ALL"
            class RDOMain(SCPINode):
                _cmd = "RDOMain"
                class FORMat(SCPINode, SCPISet):
                    _cmd = "FORMat"
            class SEGMent(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "SEGMent"
                class COUNt(SCPINode, SCPIQuery):
                    _cmd = "COUNt"
                class LIMit(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LIMit"
                class RESult(SCPINode, SCPIQuery):
                    _cmd = "RESult"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
                class STIMulus(SCPINode):
                    _cmd = "STIMulus"
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STARt"
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STOP"
            class SOUNd(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SOUNd"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "AREA"
        class SMOothing(SCPINode, SCPIQuery, SCPISet):
            _cmd = "SMOothing"
            class APERture(SCPINode, SCPIQuery, SCPISet):
                _cmd = "APERture"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
        class STATistics(SCPINode, SCPIQuery, SCPISet):
            _cmd = "STATistics"
            class DOMain(SCPINode):
                _cmd = "DOMain"
                class USER(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "USER"
                    class SHOW(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SHOW"
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STARt"
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STOP"
            class EPDelay(SCPINode, SCPIQuery, SCPISet):
                _cmd = "EPDelay"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class FORMat(SCPINode, SCPIQuery, SCPISet):
                _cmd = "FORMat"
            class MMPTpeak(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MMPTpeak"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class MSTDdev(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MSTDdev"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class NLINear(SCPINode):
                _cmd = "NLINear"
                class COMP(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "COMP"
                    class LEVel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LEVel"
                    class RESult(SCPINode, SCPIQuery):
                        _cmd = "RESult"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
            class RESult(SCPINode, SCPIQuery, SCPISet):
                _cmd = "RESult"
            class RMS(SCPINode, SCPIQuery, SCPISet):
                _cmd = "RMS"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class SFLatness(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SFLatness"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "AREA"
        class TRANsform(SCPINode):
            _cmd = "TRANsform"
            class COMPlex(SCPINode, SCPIQuery, SCPISet):
                _cmd = "COMPlex"
            class IMPedance(SCPINode):
                _cmd = "IMPedance"
                class RNORmal(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "RNORmal"
            class TIME(SCPINode, SCPIQuery, SCPISet):
                _cmd = "TIME"
                class CENTer(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "CENTer"
                class DCHebyshev(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DCHebyshev"
                class LPASs(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LPASs"
                    class DCSParam(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DCSParam"
                        class CONTinuous(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "CONTinuous"
                        class EXTRapolate(SCPINode, SCPISet):
                            _cmd = "EXTRapolate"
                class LPFRequency(SCPINode, SCPISet):
                    _cmd = "LPFRequency"
                class METHod(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "METHod"
                class RESolution(SCPINode):
                    _cmd = "RESolution"
                    class EFACtor(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "EFACtor"
                class SPAN(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SPAN"
                class STARt(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STARt"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
                class STIMulus(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STIMulus"
                class STOP(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STOP"
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TYPE"
                class WINDow(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "WINDow"
                class XAXis(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "XAXis"
            class VNETworks(SCPINode):
                _cmd = "VNETworks"
                class BALanced(SCPINode):
                    _cmd = "BALanced"
                    class DEEMbedding(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "DEEMbedding"
                        class PARameters(SCPINode):
                            _cmd = "PARameters"
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "C"
                            class DATA(SCPINodeN, SCPISet):
                                _cmd = "DATA"
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "G"
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "L"
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "R"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "TNDefinition"
                    class EMBedding(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "EMBedding"
                        class PARameters(SCPINode):
                            _cmd = "PARameters"
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "C"
                            class DATA(SCPINodeN, SCPISet):
                                _cmd = "DATA"
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "G"
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "L"
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "R"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "TNDefinition"
                class DIFFerential(SCPINode):
                    _cmd = "DIFFerential"
                    class EMBedding(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "EMBedding"
                        class PARameters(SCPINode):
                            _cmd = "PARameters"
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "C"
                            class DATA(SCPINodeN, SCPISet):
                                _cmd = "DATA"
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "G"
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "L"
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "R"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "TNDefinition"
                class FSIMulator(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FSIMulator"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class GLOop(SCPINode):
                    _cmd = "GLOop"
                    class DEEMbedding(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DEEMbedding"
                        class PARameters(SCPINode):
                            _cmd = "PARameters"
                            class C(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "C"
                            class G(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "G"
                            class L(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "L"
                            class R(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "R"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "TNDefinition"
                    class EMBedding(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "EMBedding"
                        class PARameters(SCPINode):
                            _cmd = "PARameters"
                            class C(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "C"
                            class G(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "G"
                            class L(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "L"
                            class R(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "R"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "TNDefinition"
                class PPAir(SCPINode):
                    _cmd = "PPAir"
                    class DEEMbedding(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "DEEMbedding"
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "DEFine"
                        class DELete(SCPINode, SCPISet):
                            _cmd = "DELete"
                        class PARameters(SCPINode):
                            _cmd = "PARameters"
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "C"
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "G"
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "L"
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "R"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "TNDefinition"
                    class EMBedding(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "EMBedding"
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "DEFine"
                        class DELete(SCPINode, SCPISet):
                            _cmd = "DELete"
                        class PARameters(SCPINode):
                            _cmd = "PARameters"
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "C"
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "G"
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "L"
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "R"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "TNDefinition"
                class PSET(SCPINode):
                    _cmd = "PSET"
                    class DEEMbedding(SCPINodeN):
                        _cmd = "DEEMbedding"
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "DEFine"
                    class EMBedding(SCPINodeN):
                        _cmd = "EMBedding"
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "DEFine"
                class SENDed(SCPINode):
                    _cmd = "SENDed"
                    class DEEMbedding(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "DEEMbedding"
                        class PARameters(SCPINode):
                            _cmd = "PARameters"
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "C"
                            class DATA(SCPINodeN, SCPISet):
                                _cmd = "DATA"
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "G"
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "L"
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "R"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "TNDefinition"
                    class EMBedding(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "EMBedding"
                        class PARameters(SCPINode):
                            _cmd = "PARameters"
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "C"
                            class DATA(SCPINodeN, SCPISet):
                                _cmd = "DATA"
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "G"
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "L"
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                _cmd = "R"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "TNDefinition"
    class CONFigure(SCPINode):
        _cmd = "CONFigure"
        class CHANnel(SCPINodeN, SCPIQuery, SCPISet):
            _cmd = "CHANnel"
            class CATalog(SCPINode, SCPIQuery):
                _cmd = "CATalog"
            class MEASure(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MEASure"
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ALL"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class NAME(SCPINode, SCPIQuery, SCPISet):
                _cmd = "NAME"
                class ID(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ID"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
            class TRACe(SCPINode):
                _cmd = "TRACe"
                class CATalog(SCPINode, SCPIQuery):
                    _cmd = "CATalog"
                class REName(SCPINode, SCPISet):
                    _cmd = "REName"
        class TRACe(SCPINodeN):
            _cmd = "TRACe"
            class CATalog(SCPINode, SCPIQuery):
                _cmd = "CATalog"
            class CHANnel(SCPINode):
                _cmd = "CHANnel"
                class NAME(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "NAME"
                    class ID(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "ID"
            class NAME(SCPINode, SCPIQuery, SCPISet):
                _cmd = "NAME"
                class ID(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ID"
            class REName(SCPINode, SCPISet):
                _cmd = "REName"
            class WINDow(SCPINode, SCPIQuery, SCPISet):
                _cmd = "WINDow"
                class TRACe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TRACe"
    class CONTrol(SCPINodeN):
        _cmd = "CONTrol"
        class AUXiliary(SCPINode):
            _cmd = "AUXiliary"
            class C(SCPINode, SCPIQuery, SCPISet):
                _cmd = "C"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
        class GPIO(SCPINodeN, SCPIQuery, SCPISet):
            _cmd = "GPIO"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
            class VOLTage(SCPINode, SCPIQuery, SCPISet):
                _cmd = "VOLTage"
                class DEFault(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DEFault"
                class OUTPut(SCPINode, SCPISet):
                    _cmd = "OUTPut"
        class HANDler(SCPINode):
            _cmd = "HANDler"
            class A(SCPINode, SCPIQuery, SCPISet):
                _cmd = "A"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MODE"
            class B(SCPINode, SCPIQuery, SCPISet):
                _cmd = "B"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MODE"
            class C(SCPINode, SCPIQuery, SCPISet):
                _cmd = "C"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MODE"
            class D(SCPINode, SCPIQuery, SCPISet):
                _cmd = "D"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MODE"
            class E(SCPINode, SCPIQuery, SCPISet):
                _cmd = "E"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
            class EXTension(SCPINode):
                _cmd = "EXTension"
                class INDex(SCPINode):
                    _cmd = "INDex"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class RTRigger(SCPINode):
                    _cmd = "RTRigger"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
            class F(SCPINode, SCPIQuery, SCPISet):
                _cmd = "F"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
            class G(SCPINode, SCPIQuery, SCPISet):
                _cmd = "G"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
            class H(SCPINode, SCPIQuery, SCPISet):
                _cmd = "H"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
            class INPut(SCPINode, SCPIQuery, SCPISet):
                _cmd = "INPut"
            class LOGic(SCPINode, SCPIQuery, SCPISet):
                _cmd = "LOGic"
            class OUTPut(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "OUTPut"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                class USER(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "USER"
            class PASSfail(SCPINode):
                _cmd = "PASSfail"
                class LOGic(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LOGic"
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MODE"
                class POLicy(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "POLicy"
                class SCOPe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SCOPe"
                class STATus(SCPINode, SCPIQuery):
                    _cmd = "STATus"
            class RESet(SCPINode, SCPISet):
                _cmd = "RESet"
            class SWEepend(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SWEepend"
        class RFFE(SCPINodeN):
            _cmd = "RFFE"
            class COMMand(SCPINode):
                _cmd = "COMMand"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                class SEND(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SEND"
            class SETTings(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SETTings"
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FREQuency"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
                class VOLTage(SCPINode):
                    _cmd = "VOLTage"
                    class HIGH(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "HIGH"
                    class IO(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "IO"
                    class LOW(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LOW"
        class SEGMent(SCPINodeN):
            _cmd = "SEGMent"
            class SEQuence(SCPINodeN):
                _cmd = "SEQuence"
                class CLEar(SCPINode):
                    _cmd = "CLEar"
                    class ALL(SCPINode, SCPISet):
                        _cmd = "ALL"
                class COUNt(SCPINode, SCPIQuery):
                    _cmd = "COUNt"
                class DELay(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DELay"
                class GPIO(SCPINodeN):
                    _cmd = "GPIO"
                    class VOLTage(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "VOLTage"
                class RFFE(SCPINodeN):
                    _cmd = "RFFE"
                    class COMMand(SCPINode):
                        _cmd = "COMMand"
                        class DATA(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "DATA"
        class SEQuence(SCPINodeN):
            _cmd = "SEQuence"
            class CLEar(SCPINode):
                _cmd = "CLEar"
                class ALL(SCPINode, SCPISet):
                    _cmd = "ALL"
            class COUNt(SCPINode, SCPIQuery):
                _cmd = "COUNt"
            class DELay(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DELay"
            class GPIO(SCPINodeN):
                _cmd = "GPIO"
                class VOLTage(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "VOLTage"
            class RFFE(SCPINodeN):
                _cmd = "RFFE"
                class COMMand(SCPINode):
                    _cmd = "COMMand"
                    class DATA(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DATA"
    class DIAGnostic(SCPINode):
        _cmd = "DIAGnostic"
        class ALC(SCPINode):
            _cmd = "ALC"
            class SETTings(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SETTings"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
        class DEFault(SCPINode, SCPIQuery, SCPISet):
            _cmd = "DEFault"
        class DEVice(SCPINode):
            _cmd = "DEVice"
            class STATe(SCPINode, SCPISet):
                _cmd = "STATe"
        class DUMP(SCPINode):
            _cmd = "DUMP"
            class SIZE(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SIZE"
        class PRODuct(SCPINode):
            _cmd = "PRODuct"
            class CATalog(SCPINode, SCPIQuery):
                _cmd = "CATalog"
            class DESCription(SCPINode, SCPIQuery):
                _cmd = "DESCription"
            class ID(SCPINode, SCPIQuery):
                _cmd = "ID"
            class MACaddress(SCPINode, SCPIQuery):
                _cmd = "MACaddress"
            class OPTion(SCPINode):
                _cmd = "OPTion"
                class FACTory(SCPINode):
                    _cmd = "FACTory"
                    class CLEar(SCPINode, SCPISet):
                        _cmd = "CLEar"
                class INFO(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "INFO"
                class LICence(SCPINode):
                    _cmd = "LICence"
                    class CHECk(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "CHECk"
                    class UNLock(SCPINode, SCPISet):
                        _cmd = "UNLock"
                class LIST(SCPINode, SCPIQuery):
                    _cmd = "LIST"
                class STATus(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATus"
            class SELect(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SELect"
            class TIME(SCPINode):
                _cmd = "TIME"
                class OPERating(SCPINode, SCPIQuery):
                    _cmd = "OPERating"
        class SERVice(SCPINode):
            _cmd = "SERVice"
            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                _cmd = "FUNCtion"
            class RFPower(SCPINode, SCPIQuery, SCPISet):
                _cmd = "RFPower"
            class SFUNction(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SFUNction"
        class UPDate(SCPINode):
            _cmd = "UPDate"
            class BOOT(SCPINode, SCPISet):
                _cmd = "BOOT"
            class CATalog(SCPINode, SCPIQuery):
                _cmd = "CATalog"
            class CHAP(SCPINode):
                _cmd = "CHAP"
                class CHALlenge(SCPINode, SCPIQuery):
                    _cmd = "CHALlenge"
                class PRESet(SCPINode, SCPISet):
                    _cmd = "PRESet"
                class RESPonse(SCPINode, SCPISet):
                    _cmd = "RESPonse"
            class EXECute(SCPINode, SCPISet):
                _cmd = "EXECute"
            class INSTall(SCPINode, SCPISet):
                _cmd = "INSTall"
                class BEGin(SCPINode, SCPISet):
                    _cmd = "BEGin"
                class END(SCPINode, SCPISet):
                    _cmd = "END"
                class STATus(SCPINode, SCPIQuery):
                    _cmd = "STATus"
            class PROGress(SCPINode, SCPIQuery, SCPISet):
                _cmd = "PROGress"
            class TRANsfer(SCPINode):
                _cmd = "TRANsfer"
                class CLOSe(SCPINode, SCPISet):
                    _cmd = "CLOSe"
                class DATA(SCPINode, SCPISet):
                    _cmd = "DATA"
                class OPEN(SCPINode, SCPISet):
                    _cmd = "OPEN"
                class VERSion(SCPINode, SCPIQuery):
                    _cmd = "VERSion"
    class DISPlay(SCPINode, SCPIQuery, SCPISet):
        _cmd = "DISPlay"
        class ANNotation(SCPINode):
            _cmd = "ANNotation"
            class CHANnel(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CHANnel"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class FREQuency(SCPINode, SCPIQuery, SCPISet):
                _cmd = "FREQuency"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class TRACe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "TRACe"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
        class CMAP(SCPINodeN):
            _cmd = "CMAP"
            class LIMit(SCPINode, SCPIQuery, SCPISet):
                _cmd = "LIMit"
                class FCOLorize(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FCOLorize"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class FSYMbol(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FSYMbol"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class MARKer(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MARKer"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class RGB(SCPINode, SCPIQuery, SCPISet):
                _cmd = "RGB"
            class TRACe(SCPINode):
                _cmd = "TRACe"
                class COLor(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "COLor"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class RGB(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "RGB"
        class LAYout(SCPINode, SCPIQuery, SCPISet):
            _cmd = "LAYout"
            class APPLy(SCPINode, SCPIQuery, SCPISet):
                _cmd = "APPLy"
            class DEFine(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DEFine"
            class EXECute(SCPINode, SCPIQuery, SCPISet):
                _cmd = "EXECute"
            class GRID(SCPINode, SCPIQuery, SCPISet):
                _cmd = "GRID"
            class JOIN(SCPINode, SCPISet):
                _cmd = "JOIN"
        class MENU(SCPINode):
            _cmd = "MENU"
            class KEY(SCPINode):
                _cmd = "KEY"
                class EXECute(SCPINode, SCPISet):
                    _cmd = "EXECute"
                class SELect(SCPINode, SCPISet):
                    _cmd = "SELect"
        class RFSize(SCPINode, SCPIQuery, SCPISet):
            _cmd = "RFSize"
        class WINDow(SCPINodeN, SCPIQuery, SCPISet):
            _cmd = "WINDow"
            class CATalog(SCPINode, SCPIQuery):
                _cmd = "CATalog"
            class MAXimize(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MAXimize"
            class NAME(SCPINode, SCPIQuery, SCPISet):
                _cmd = "NAME"
            class OVERview(SCPINode, SCPIQuery, SCPISet):
                _cmd = "OVERview"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
            class TITLe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "TITLe"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class TRACe(SCPINodeN):
                _cmd = "TRACe"
                class CATalog(SCPINode, SCPIQuery):
                    _cmd = "CATalog"
                class DELete(SCPINode, SCPISet):
                    _cmd = "DELete"
                class EFEed(SCPINode, SCPISet):
                    _cmd = "EFEed"
                class FEED(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FEED"
                class SHOW(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SHOW"
                class X(SCPINode):
                    _cmd = "X"
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "OFFSet"
                class Y(SCPINode):
                    _cmd = "Y"
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "OFFSet"
                    class SCALe(SCPINode):
                        _cmd = "SCALe"
                        class AUTO(SCPINode, SCPISet):
                            _cmd = "AUTO"
                        class BOTTom(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "BOTTom"
                        class PDIVision(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "PDIVision"
                        class RLEVel(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "RLEVel"
                        class RPOSition(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "RPOSition"
                        class TOP(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "TOP"
                class ZOOM(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ZOOM"
                    class BOTTom(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "BOTTom"
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STARt"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STOP"
                    class TOP(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "TOP"
    class FORMat(SCPINode, SCPIQuery, SCPISet):
        _cmd = "FORMat"
        class BORDer(SCPINode, SCPIQuery, SCPISet):
            _cmd = "BORDer"
        class DATA(SCPINode, SCPIQuery, SCPISet):
            _cmd = "DATA"
        class DEXPort(SCPINode):
            _cmd = "DEXPort"
            class SOURce(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SOURce"
    class HCOPy(SCPINode, SCPISet):
        _cmd = "HCOPy"
        class DESTination(SCPINode, SCPIQuery, SCPISet):
            _cmd = "DESTination"
        class DEVice(SCPINode):
            _cmd = "DEVice"
            class LANGuage(SCPINode, SCPIQuery, SCPISet):
                _cmd = "LANGuage"
        class IMMediate(SCPINode, SCPISet):
            _cmd = "IMMediate"
        class ITEM(SCPINode):
            _cmd = "ITEM"
            class ALL(SCPINode, SCPISet):
                _cmd = "ALL"
            class LOGO(SCPINode, SCPIQuery, SCPISet):
                _cmd = "LOGO"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class MLISt(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MLISt"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class TIME(SCPINode, SCPIQuery, SCPISet):
                _cmd = "TIME"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
        class PAGE(SCPINode):
            _cmd = "PAGE"
            class COLor(SCPINode, SCPIQuery, SCPISet):
                _cmd = "COLor"
            class MARGin(SCPINode):
                _cmd = "MARGin"
                class BOTTom(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "BOTTom"
                class LEFT(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LEFT"
                class RIGHt(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "RIGHt"
                class TOP(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TOP"
            class ORIentation(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ORIentation"
            class WINDow(SCPINode, SCPIQuery, SCPISet):
                _cmd = "WINDow"
    class INITiate(SCPINodeN, SCPISet):
        _cmd = "INITiate"
        class CONTinuous(SCPINode, SCPIQuery, SCPISet):
            _cmd = "CONTinuous"
            class ALL(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ALL"
        class IMMediate(SCPINode, SCPISet):
            _cmd = "IMMediate"
            class ALL(SCPINode, SCPISet):
                _cmd = "ALL"
            class DUMMy(SCPINode, SCPISet):
                _cmd = "DUMMy"
            class SCOPe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SCOPe"
    class INPut(SCPINodeN):
        _cmd = "INPut"
        class ATTenuation(SCPINode, SCPIQuery, SCPISet):
            _cmd = "ATTenuation"
    class INSTrument(SCPINode, SCPIQuery, SCPISet):
        _cmd = "INSTrument"
        class NSELect(SCPINode, SCPIQuery, SCPISet):
            _cmd = "NSELect"
        class PORT(SCPINode):
            _cmd = "PORT"
            class COUNt(SCPINode, SCPIQuery):
                _cmd = "COUNt"
        class SELect(SCPINode, SCPIQuery, SCPISet):
            _cmd = "SELect"
        class SMATrix(SCPINode, SCPIQuery, SCPISet):
            _cmd = "SMATrix"
        class TPORt(SCPINode):
            _cmd = "TPORt"
            class COUNt(SCPINode, SCPIQuery):
                _cmd = "COUNt"
    class MEMory(SCPINode):
        _cmd = "MEMory"
        class CATalog(SCPINode, SCPIQuery):
            _cmd = "CATalog"
            class COUNt(SCPINode, SCPIQuery):
                _cmd = "COUNt"
        class DEFine(SCPINode, SCPISet):
            _cmd = "DEFine"
        class DELete(SCPINode, SCPISet):
            _cmd = "DELete"
            class ALL(SCPINode, SCPISet):
                _cmd = "ALL"
            class NAME(SCPINode, SCPISet):
                _cmd = "NAME"
        class SELect(SCPINode, SCPIQuery, SCPISet):
            _cmd = "SELect"
    class MMEMory(SCPINode):
        _cmd = "MMEMory"
        class AKAL(SCPINode):
            _cmd = "AKAL"
            class FACTory(SCPINode):
                _cmd = "FACTory"
                class CONVersion(SCPINode, SCPISet):
                    _cmd = "CONVersion"
            class USER(SCPINode):
                _cmd = "USER"
                class CONVersion(SCPINode, SCPISet):
                    _cmd = "CONVersion"
        class CATalog(SCPINode, SCPIQuery, SCPISet):
            _cmd = "CATalog"
            class ALL(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ALL"
        class CDIRectory(SCPINode, SCPIQuery, SCPISet):
            _cmd = "CDIRectory"
        class CKIT(SCPINode):
            _cmd = "CKIT"
            class INFO(SCPINode, SCPIQuery, SCPISet):
                _cmd = "INFO"
        class COPY(SCPINode, SCPISet):
            _cmd = "COPY"
        class DATA(SCPINode, SCPIQuery, SCPISet):
            _cmd = "DATA"
        class DELete(SCPINode, SCPISet):
            _cmd = "DELete"
            class CORRection(SCPINode, SCPISet):
                _cmd = "CORRection"
        class LOAD(SCPINode, SCPISet):
            _cmd = "LOAD"
            class CKIT(SCPINode, SCPISet):
                _cmd = "CKIT"
                class SDATa(SCPINode, SCPISet):
                    _cmd = "SDATa"
                    class WLABel(SCPINode, SCPISet):
                        _cmd = "WLABel"
                class UDIRectory(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "UDIRectory"
            class CMAP(SCPINode, SCPISet):
                _cmd = "CMAP"
            class CORRection(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CORRection"
                class MERGe(SCPINode, SCPISet):
                    _cmd = "MERGe"
                class RESolve(SCPINode, SCPISet):
                    _cmd = "RESolve"
                class TCOefficient(SCPINode, SCPISet):
                    _cmd = "TCOefficient"
            class LIMit(SCPINode, SCPISet):
                _cmd = "LIMit"
            class MDAData(SCPINode, SCPISet):
                _cmd = "MDAData"
            class MDCData(SCPINode, SCPISet):
                _cmd = "MDCData"
            class PTRain(SCPINode, SCPISet):
                _cmd = "PTRain"
            class RIPPle(SCPINode, SCPISet):
                _cmd = "RIPPle"
            class SEGMent(SCPINode, SCPISet):
                _cmd = "SEGMent"
            class STATe(SCPINode, SCPISet):
                _cmd = "STATe"
            class TRACe(SCPINode, SCPISet):
                _cmd = "TRACe"
                class AUTO(SCPINode, SCPISet):
                    _cmd = "AUTO"
            class VNETworks(SCPINodeN):
                _cmd = "VNETworks"
                class BALanced(SCPINode):
                    _cmd = "BALanced"
                    class DEEMbedding(SCPINodeN, SCPISet):
                        _cmd = "DEEMbedding"
                    class EMBedding(SCPINodeN, SCPISet):
                        _cmd = "EMBedding"
                class DIFFerential(SCPINode):
                    _cmd = "DIFFerential"
                    class EMBedding(SCPINodeN, SCPISet):
                        _cmd = "EMBedding"
                class GLOop(SCPINode):
                    _cmd = "GLOop"
                    class DEEMbedding(SCPINode, SCPISet):
                        _cmd = "DEEMbedding"
                    class EMBedding(SCPINode, SCPISet):
                        _cmd = "EMBedding"
                class PPAir(SCPINode):
                    _cmd = "PPAir"
                    class DEEMbedding(SCPINodeN, SCPISet):
                        _cmd = "DEEMbedding"
                    class EMBedding(SCPINodeN, SCPISet):
                        _cmd = "EMBedding"
                class SENDed(SCPINode):
                    _cmd = "SENDed"
                    class DEEMbedding(SCPINodeN, SCPISet):
                        _cmd = "DEEMbedding"
                    class EMBedding(SCPINodeN, SCPISet):
                        _cmd = "EMBedding"
        class MDIRectory(SCPINode, SCPISet):
            _cmd = "MDIRectory"
        class MOVE(SCPINode, SCPISet):
            _cmd = "MOVE"
        class MSIS(SCPINode, SCPIQuery, SCPISet):
            _cmd = "MSIS"
        class NAME(SCPINode, SCPIQuery, SCPISet):
            _cmd = "NAME"
        class RDIRectory(SCPINode, SCPISet):
            _cmd = "RDIRectory"
        class STORe(SCPINode):
            _cmd = "STORe"
            class CKIT(SCPINode, SCPISet):
                _cmd = "CKIT"
                class WLABel(SCPINode, SCPISet):
                    _cmd = "WLABel"
            class CMAP(SCPINode, SCPISet):
                _cmd = "CMAP"
            class CORRection(SCPINode, SCPISet):
                _cmd = "CORRection"
                class TCOefficient(SCPINode, SCPISet):
                    _cmd = "TCOefficient"
            class LIMit(SCPINode, SCPISet):
                _cmd = "LIMit"
            class MARKer(SCPINode, SCPISet):
                _cmd = "MARKer"
            class MDCData(SCPINode, SCPISet):
                _cmd = "MDCData"
            class PTRain(SCPINode, SCPISet):
                _cmd = "PTRain"
            class RIPPle(SCPINode, SCPISet):
                _cmd = "RIPPle"
            class SEGMent(SCPINode, SCPISet):
                _cmd = "SEGMent"
            class STATe(SCPINode, SCPISet):
                _cmd = "STATe"
            class TRACe(SCPINode, SCPISet):
                _cmd = "TRACe"
                class CHANnel(SCPINode, SCPISet):
                    _cmd = "CHANnel"
                class OPTion(SCPINode):
                    _cmd = "OPTion"
                    class PLUS(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "PLUS"
                    class SSEParator(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SSEParator"
                    class TABS(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "TABS"
                    class TRIM(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "TRIM"
                class PORTs(SCPINode, SCPISet):
                    _cmd = "PORTs"
    class OUTPut(SCPINodeN, SCPIQuery, SCPISet):
        _cmd = "OUTPut"
        class DPORt(SCPINode, SCPIQuery, SCPISet):
            _cmd = "DPORt"
        class STATe(SCPINode, SCPIQuery, SCPISet):
            _cmd = "STATe"
        class UPORt(SCPINode, SCPIQuery):
            _cmd = "UPORt"
            class ECBits(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ECBits"
            class SEGMent(SCPINodeN, SCPIQuery):
                _cmd = "SEGMent"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
                class VALue(SCPINode, SCPIQuery):
                    _cmd = "VALue"
            class VALue(SCPINode, SCPIQuery):
                _cmd = "VALue"
    class PROGram(SCPINode):
        _cmd = "PROGram"
        class SELected(SCPINode):
            _cmd = "SELected"
            class EXECute(SCPINode, SCPISet):
                _cmd = "EXECute"
            class INIMessage(SCPINode, SCPIQuery, SCPISet):
                _cmd = "INIMessage"
            class INIParameter(SCPINode, SCPIQuery, SCPISet):
                _cmd = "INIParameter"
            class NAME(SCPINode, SCPIQuery, SCPISet):
                _cmd = "NAME"
            class RETVal(SCPINode, SCPIQuery):
                _cmd = "RETVal"
            class WAIT(SCPINode, SCPIQuery, SCPISet):
                _cmd = "WAIT"
    class SENSe(SCPINodeN):
        _cmd = "SENSe"
        class AVERage(SCPINode, SCPIQuery, SCPISet):
            _cmd = "AVERage"
            class CLEar(SCPINode, SCPISet):
                _cmd = "CLEar"
            class COUNt(SCPINode, SCPIQuery, SCPISet):
                _cmd = "COUNt"
            class MODE(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MODE"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
        class BANDwidth(SCPINode, SCPIQuery, SCPISet):
            _cmd = "BANDwidth"
            class RESolution(SCPINode, SCPIQuery, SCPISet):
                _cmd = "RESolution"
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SELect"
        class BWIDth(SCPINode, SCPIQuery, SCPISet):
            _cmd = "BWIDth"
            class RESolution(SCPINode, SCPIQuery, SCPISet):
                _cmd = "RESolution"
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SELect"
        class CORRection(SCPINode, SCPIQuery, SCPISet):
            _cmd = "CORRection"
            class CDATa(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CDATa"
                class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "CATalog"
                class PORT(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "PORT"
                    class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "CATalog"
            class CKIT(SCPINode):
                _cmd = "CKIT"
                class CATalog(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "CATalog"
                class DELete(SCPINode, SCPISet):
                    _cmd = "DELete"
                class DMODe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DMODe"
                class FFATten(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FFATten"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "FFLine"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FFSNetwork"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FFTHrough"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class FMTCh(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FMTCh"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class FOPen(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FOPen"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class FOSHort(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "FOSHort"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class FREFlect(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FREFlect"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class FSHort(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FSHort"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class FSMatch(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FSMatch"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class INSTall(SCPINode, SCPISet):
                    _cmd = "INSTall"
                class LABel(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LABel"
                class LCATalog(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LCATalog"
                class LDELete(SCPINode, SCPISet):
                    _cmd = "LDELete"
                class LLABel(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LLABel"
                class LSELect(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LSELect"
                class MFATten(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MFATten"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "MFLine"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MFSNetwork"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MFTHrough"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MMATten(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MMATten"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "MMLine"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MMSNetwork"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MMTCh(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MMTCh"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MMTHrough"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MOPen(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MOPen"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MOSHort(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "MOSHort"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MREFlect(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MREFlect"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MSHort(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MSHort"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class MSMatch(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MSMatch"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class N(SCPINodeN):
                    _cmd = "N"
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFATten"
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "FFLine"
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFSNetwork"
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFTHrough"
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FMTCh"
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FOPen"
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FREFlect"
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FSHort"
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FSMatch"
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LSELect"
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFATten"
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "MFLine"
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFSNetwork"
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFTHrough"
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMATten"
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "MMLine"
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMSNetwork"
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMTCh"
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMTHrough"
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MOPen"
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MREFlect"
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MSHort"
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MSMatch"
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SELect"
                class OSHort(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "OSHort"
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WLABel"
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "SDATa"
                class PC(SCPINodeN):
                    _cmd = "PC"
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFATten"
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "FFLine"
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFSNetwork"
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFTHrough"
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FMTCh"
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FOPen"
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FREFlect"
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FSHort"
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FSMatch"
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LSELect"
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFATten"
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "MFLine"
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFSNetwork"
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFTHrough"
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMATten"
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "MMLine"
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMSNetwork"
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMTCh"
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMTHrough"
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MOPen"
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MREFlect"
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MSHort"
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MSMatch"
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SELect"
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SELect"
                class SMA(SCPINode):
                    _cmd = "SMA"
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFATten"
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "FFLine"
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFSNetwork"
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFTHrough"
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FMTCh"
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FOPen"
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FREFlect"
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FSHort"
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FSMatch"
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LSELect"
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFATten"
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "MFLine"
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFSNetwork"
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFTHrough"
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMATten"
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "MMLine"
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMSNetwork"
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMTCh"
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMTHrough"
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MOPen"
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MREFlect"
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MSHort"
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MSMatch"
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SELect"
                class STANdard(SCPINode):
                    _cmd = "STANdard"
                    class CATalog(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "CATalog"
                    class DATA(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DATA"
                    class LCATalog(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LCATalog"
                class USER(SCPINodeN):
                    _cmd = "USER"
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFATten"
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "FFLine"
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFSNetwork"
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFTHrough"
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FMTCh"
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FOPen"
                    class FOSHort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FOSHort"
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FREFlect"
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FSHort"
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FSMatch"
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LSELect"
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFATten"
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "MFLine"
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFSNetwork"
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFTHrough"
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMATten"
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "MMLine"
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMSNetwork"
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMTCh"
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MMTHrough"
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MOPen"
                    class MOSHort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MOSHort"
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MREFlect"
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MSHort"
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MSMatch"
                    class OSHort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "OSHort"
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SELect"
            class COLLect(SCPINode, SCPISet):
                _cmd = "COLLect"
                class ACQuire(SCPINode, SCPISet):
                    _cmd = "ACQuire"
                    class RSAVe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "RSAVe"
                        class DEFault(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "DEFault"
                    class SELected(SCPINode, SCPISet):
                        _cmd = "SELected"
                class AUTO(SCPINode, SCPISet):
                    _cmd = "AUTO"
                    class ASSignment(SCPINodeN):
                        _cmd = "ASSignment"
                        class ACQuire(SCPINode, SCPISet):
                            _cmd = "ACQuire"
                        class ALL(SCPINode):
                            _cmd = "ALL"
                            class COUNt(SCPINode, SCPIQuery):
                                _cmd = "COUNt"
                        class COUNt(SCPINode, SCPIQuery):
                            _cmd = "COUNt"
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "DEFine"
                            class DEFault(SCPINode, SCPISet):
                                _cmd = "DEFault"
                            class TPORt(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "TPORt"
                                class DEFault(SCPINode, SCPISet):
                                    _cmd = "DEFault"
                        class DELete(SCPINode):
                            _cmd = "DELete"
                            class ALL(SCPINode, SCPISet):
                                _cmd = "ALL"
                    class CKIT(SCPINode, SCPISet):
                        _cmd = "CKIT"
                        class PASSword(SCPINode, SCPISet):
                            _cmd = "PASSword"
                        class PORTs(SCPINode, SCPISet):
                            _cmd = "PORTs"
                            class ADD(SCPINode, SCPISet):
                                _cmd = "ADD"
                    class CONFigure(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "CONFigure"
                    class PORTs(SCPINode, SCPISet):
                        _cmd = "PORTs"
                        class CONNection(SCPINode, SCPIQuery):
                            _cmd = "CONNection"
                        class TYPE(SCPINode, SCPISet):
                            _cmd = "TYPE"
                    class POWer(SCPINode, SCPISet):
                        _cmd = "POWer"
                    class SAVE(SCPINode, SCPISet):
                        _cmd = "SAVE"
                    class TYPE(SCPINode, SCPISet):
                        _cmd = "TYPE"
                class AVERage(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "AVERage"
                class CHANnels(SCPINode):
                    _cmd = "CHANnels"
                    class ALL(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "ALL"
                class CKIT(SCPINode):
                    _cmd = "CKIT"
                    class INSTall(SCPINode, SCPISet):
                        _cmd = "INSTall"
                    class LOAD(SCPINode, SCPISet):
                        _cmd = "LOAD"
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "PORT"
                class CONNection(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "CONNection"
                    class GENDers(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "GENDers"
                    class PORTs(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "PORTs"
                class DELete(SCPINode, SCPISet):
                    _cmd = "DELete"
                class ERRor(SCPINode, SCPIQuery):
                    _cmd = "ERRor"
                class FIXTure(SCPINode, SCPISet):
                    _cmd = "FIXTure"
                    class ACQuire(SCPINode, SCPISet):
                        _cmd = "ACQuire"
                    class EXPort(SCPINode, SCPISet):
                        _cmd = "EXPort"
                    class IMPort(SCPINode, SCPISet):
                        _cmd = "IMPort"
                    class LMParameter(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LMParameter"
                        class LOSS(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "LOSS"
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "STATe"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                    class SAVE(SCPINode, SCPISet):
                        _cmd = "SAVE"
                    class STARt(SCPINode, SCPISet):
                        _cmd = "STARt"
                class LOAD(SCPINode):
                    _cmd = "LOAD"
                    class SELected(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SELected"
                class METHod(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "METHod"
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DEFine"
                class PMETer(SCPINode):
                    _cmd = "PMETer"
                    class ID(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "ID"
                class SAVE(SCPINode, SCPISet):
                    _cmd = "SAVE"
                    class DEFault(SCPINode, SCPISet):
                        _cmd = "DEFault"
                    class DUMMy(SCPINode, SCPISet):
                        _cmd = "DUMMy"
                    class SELected(SCPINode, SCPISet):
                        _cmd = "SELected"
                        class DEFault(SCPINode, SCPISet):
                            _cmd = "DEFault"
                        class DUMMy(SCPINode, SCPISet):
                            _cmd = "DUMMy"
                class SCONnection(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "SCONnection"
            class CONNection(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CONNection"
                class CATalog(SCPINode, SCPIQuery):
                    _cmd = "CATalog"
                class DELete(SCPINode, SCPISet):
                    _cmd = "DELete"
            class CSET(SCPINode):
                _cmd = "CSET"
                class DESCription(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DESCription"
            class DATA(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DATA"
                class PARameter(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "PARameter"
                    class COUNt(SCPINode, SCPIQuery):
                        _cmd = "COUNt"
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "PORT"
            class DATE(SCPINode, SCPIQuery):
                _cmd = "DATE"
            class DSTate(SCPINode, SCPIQuery):
                _cmd = "DSTate"
            class EDELay(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "EDELay"
                class AUTO(SCPINode, SCPISet):
                    _cmd = "AUTO"
                class DIELectric(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DIELectric"
                class DISTance(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DISTance"
                class ELENgth(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ELENgth"
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TIME"
            class LOSS(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "LOSS"
                class AUTO(SCPINode, SCPISet):
                    _cmd = "AUTO"
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FREQuency"
                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "OFFSet"
            class OFFSet(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "OFFSet"
                class COMPensation(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "COMPensation"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class DFComp(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DFComp"
                    class STATe(SCPINode, SCPIQuery):
                        _cmd = "STATe"
                class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MAGNitude"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class PCAL(SCPINode, SCPISet):
                _cmd = "PCAL"
            class POWer(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "POWer"
                class ACQuire(SCPINode, SCPISet):
                    _cmd = "ACQuire"
                class AWAVe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "AWAVe"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "PORT"
                class HARMonic(SCPINode):
                    _cmd = "HARMonic"
                    class ACQuire(SCPINode, SCPISet):
                        _cmd = "ACQuire"
                class IMODulation(SCPINode):
                    _cmd = "IMODulation"
                    class ACQuire(SCPINode, SCPISet):
                        _cmd = "ACQuire"
                class MIXer(SCPINode):
                    _cmd = "MIXer"
                    class IF(SCPINode):
                        _cmd = "IF"
                        class ACQuire(SCPINode, SCPISet):
                            _cmd = "ACQuire"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class PSTate(SCPINode, SCPIQuery):
                _cmd = "PSTate"
            class SMATrix(SCPINode):
                _cmd = "SMATrix"
                class CDATa(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "CDATa"
                    class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "CATalog"
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "PORT"
                        class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                            _cmd = "CATalog"
            class SSTate(SCPINode, SCPIQuery):
                _cmd = "SSTate"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
            class STIMulus(SCPINode, SCPIQuery):
                _cmd = "STIMulus"
                class PORT(SCPINodeN, SCPIQuery):
                    _cmd = "PORT"
        class COUPle(SCPINode, SCPIQuery, SCPISet):
            _cmd = "COUPle"
        class DC(SCPINodeN):
            _cmd = "DC"
            class RANGe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "RANGe"
        class FREQuency(SCPINodeN, SCPIQuery, SCPISet):
            _cmd = "FREQuency"
            class CENTer(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CENTer"
            class CONVersion(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CONVersion"
                class ARBitrary(SCPINode):
                    _cmd = "ARBitrary"
                    class PMETer(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "PMETer"
                class DEVice(SCPINode):
                    _cmd = "DEVice"
                    class PCOefficient(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "PCOefficient"
                class GAIN(SCPINode):
                    _cmd = "GAIN"
                    class LMCorrection(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LMCorrection"
                class HARMonic(SCPINode):
                    _cmd = "HARMonic"
                    class ORDer(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "ORDer"
                    class RELative(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "RELative"
                    class RPORt(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "RPORt"
                    class SPORt(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SPORt"
                class MIXer(SCPINode):
                    _cmd = "MIXer"
                    class FFIXed(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FFIXed"
                    class FIXed(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "FIXed"
                    class FUNDamental(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FUNDamental"
                    class IFFixed(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "IFFixed"
                    class IFPort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "IFPort"
                    class LOEXternal(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LOEXternal"
                    class LOFixed(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LOFixed"
                    class LOINternal(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LOINternal"
                    class LOMultiplier(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "LOMultiplier"
                    class LOPort(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "LOPort"
                    class MFFixed(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MFFixed"
                    class RFFixed(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "RFFixed"
                    class RFMultiplier(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "RFMultiplier"
                    class RFPort(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "RFPort"
                    class STAGes(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STAGes"
                    class TFRequency(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "TFRequency"
            class CW(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CW"
            class FIXed(SCPINode, SCPIQuery, SCPISet):
                _cmd = "FIXed"
            class IMODulation(SCPINode):
                _cmd = "IMODulation"
                class CONVersion(SCPINode, SCPISet):
                    _cmd = "CONVersion"
                class LTONe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LTONe"
                class ORDer(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "ORDer"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class RECeiver(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "RECeiver"
                class SPECtrum(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SPECtrum"
                    class MORDer(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MORDer"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class TDIStance(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TDIStance"
                class TTOutput(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TTOutput"
                class UTONe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "UTONe"
            class MODE(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MODE"
            class SBANd(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SBANd"
            class SEGMent(SCPINode):
                _cmd = "SEGMent"
                class AXIS(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "AXIS"
            class SPAN(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SPAN"
            class STARt(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STARt"
            class STOP(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STOP"
        class FUNCtion(SCPINode, SCPIQuery, SCPISet):
            _cmd = "FUNCtion"
            class ON(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ON"
        class LPORt(SCPINodeN):
            _cmd = "LPORt"
            class ZCOMmon(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ZCOMmon"
            class ZDEFault(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ZDEFault"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class ZDIFferent(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ZDIFferent"
        class PAE(SCPINode):
            _cmd = "PAE"
            class DCINput(SCPINode):
                _cmd = "DCINput"
                class MAIN(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MAIN"
                class SECondary(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SECondary"
            class PARameters(SCPINode):
                _cmd = "PARameters"
                class I(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "I"
                class R(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "R"
                class U(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "U"
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                _cmd = "TYPE"
        class PORT(SCPINodeN):
            _cmd = "PORT"
            class ZREFerence(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ZREFerence"
        class POWer(SCPINode):
            _cmd = "POWer"
            class AGCMode(SCPINodeN):
                _cmd = "AGCMode"
                class ACQuire(SCPINode, SCPISet):
                    _cmd = "ACQuire"
                class MEASure(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MEASure"
                class SAVE(SCPINode, SCPISet):
                    _cmd = "SAVE"
            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ATTenuation"
            class GAINcontrol(SCPINode, SCPIQuery, SCPISet):
                _cmd = "GAINcontrol"
                class GLOBal(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "GLOBal"
            class IFGain(SCPINodeN):
                _cmd = "IFGain"
                class MEASure(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MEASure"
        class PULSe(SCPINode):
            _cmd = "PULSe"
            class GENerator(SCPINodeN):
                _cmd = "GENerator"
                class CPPRofile(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "CPPRofile"
                class DELay(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DELay"
                class PERiod(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "PERiod"
                class POLarity(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "POLarity"
                class TRAin(SCPINode):
                    _cmd = "TRAin"
                    class DATA(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DATA"
                    class DELete(SCPINode):
                        _cmd = "DELete"
                        class ALL(SCPINode, SCPISet):
                            _cmd = "ALL"
                    class PERiod(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "PERiod"
                    class SEGMent(SCPINodeN):
                        _cmd = "SEGMent"
                        class COUNt(SCPINode, SCPIQuery):
                            _cmd = "COUNt"
                        class STARt(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STARt"
                        class STOP(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STOP"
        class ROSCillator(SCPINode, SCPIQuery, SCPISet):
            _cmd = "ROSCillator"
            class EXTernal(SCPINode):
                _cmd = "EXTernal"
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FREQuency"
            class SOURce(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SOURce"
        class SEGMent(SCPINodeN, SCPIQuery, SCPISet):
            _cmd = "SEGMent"
            class ADD(SCPINode, SCPISet):
                _cmd = "ADD"
            class BWIDth(SCPINode, SCPIQuery, SCPISet):
                _cmd = "BWIDth"
                class RESolution(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "RESolution"
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "CONTrol"
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SELect"
                        class CONTrol(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "CONTrol"
            class CLEar(SCPINode, SCPISet):
                _cmd = "CLEar"
            class COUNt(SCPINode, SCPIQuery):
                _cmd = "COUNt"
            class DEFine(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "DEFine"
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SELect"
            class DELete(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "DELete"
                class ALL(SCPINode, SCPISet):
                    _cmd = "ALL"
                class DUMMy(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DUMMy"
            class FREQuency(SCPINode):
                _cmd = "FREQuency"
                class CENTer(SCPINode, SCPIQuery):
                    _cmd = "CENTer"
                class SPAN(SCPINode, SCPIQuery):
                    _cmd = "SPAN"
                class STARt(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STARt"
                class STOP(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STOP"
            class INSert(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "INSert"
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SELect"
            class OVERlap(SCPINode, SCPIQuery, SCPISet):
                _cmd = "OVERlap"
            class POWer(SCPINode, SCPIQuery, SCPISet):
                _cmd = "POWer"
                class GAINcontrol(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "GAINcontrol"
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "CONTrol"
                class LEVel(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LEVel"
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "CONTrol"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
            class SWEep(SCPINode):
                _cmd = "SWEep"
                class DWELl(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DWELl"
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "CONTrol"
                class GENeration(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "GENeration"
                class POINts(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "POINts"
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TIME"
                    class CONTrol(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "CONTrol"
                    class SUM(SCPINode, SCPIQuery):
                        _cmd = "SUM"
        class SWEep(SCPINode):
            _cmd = "SWEep"
            class AXIS(SCPINode):
                _cmd = "AXIS"
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FREQuency"
                class POWer(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "POWer"
            class COUNt(SCPINode, SCPIQuery, SCPISet):
                _cmd = "COUNt"
                class ALL(SCPINode, SCPISet):
                    _cmd = "ALL"
            class DETector(SCPINode):
                _cmd = "DETector"
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TIME"
            class DWELl(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DWELl"
                class IPOint(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "IPOint"
            class GENeration(SCPINode, SCPIQuery, SCPISet):
                _cmd = "GENeration"
                class ANALog(SCPINode):
                    _cmd = "ANALog"
                    class CONDition(SCPINode, SCPIQuery):
                        _cmd = "CONDition"
            class MODE(SCPINode, SCPIQuery, SCPISet):
                _cmd = "MODE"
            class POINts(SCPINode, SCPIQuery, SCPISet):
                _cmd = "POINts"
            class SPACing(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SPACing"
            class SRCPort(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SRCPort"
            class STEP(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STEP"
            class TIME(SCPINode, SCPIQuery, SCPISet):
                _cmd = "TIME"
                class AUTO(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "AUTO"
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                _cmd = "TYPE"
        class UDSParams(SCPINodeN):
            _cmd = "UDSParams"
            class ACTive(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ACTive"
            class PARam(SCPINode, SCPIQuery, SCPISet):
                _cmd = "PARam"
    class SOURce(SCPINodeN):
        _cmd = "SOURce"
        class FREQuency(SCPINodeN, SCPIQuery, SCPISet):
            _cmd = "FREQuency"
            class CONVersion(SCPINode):
                _cmd = "CONVersion"
                class ARBitrary(SCPINode):
                    _cmd = "ARBitrary"
                    class EFRequency(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "EFRequency"
                    class IFRequency(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "IFRequency"
                class MIXer(SCPINode):
                    _cmd = "MIXer"
                    class FUNDamental(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FUNDamental"
                    class PFIXed(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "PFIXed"
                    class PMFixed(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "PMFixed"
                    class PMODe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "PMODe"
            class CW(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CW"
            class FIXed(SCPINode, SCPIQuery, SCPISet):
                _cmd = "FIXed"
        class GROup(SCPINodeN, SCPIQuery, SCPISet):
            _cmd = "GROup"
            class CLEar(SCPINode, SCPISet):
                _cmd = "CLEar"
            class COUNt(SCPINode, SCPIQuery):
                _cmd = "COUNt"
            class DPORt(SCPINode):
                _cmd = "DPORt"
                class COUNt(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "COUNt"
            class NAME(SCPINode, SCPIQuery, SCPISet):
                _cmd = "NAME"
            class PORTs(SCPINode, SCPIQuery, SCPISet):
                _cmd = "PORTs"
            class PPORt(SCPINodeN):
                _cmd = "PPORt"
                class DPORt(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DPORt"
            class PPORts(SCPINode, SCPIQuery, SCPISet):
                _cmd = "PPORts"
            class SIMultaneous(SCPINode):
                _cmd = "SIMultaneous"
                class FOFFset(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FOFFset"
                    class CONDition(SCPINode, SCPIQuery):
                        _cmd = "CONDition"
                    class MOFFset(SCPINode):
                        _cmd = "MOFFset"
                        class BWFactor(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "BWFactor"
                        class DVALue(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "DVALue"
                        class MODE(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "MODE"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
        class LPORt(SCPINodeN, SCPIQuery, SCPISet):
            _cmd = "LPORt"
            class CLEar(SCPINode, SCPISet):
                _cmd = "CLEar"
        class POWer(SCPINodeN, SCPIQuery, SCPISet):
            _cmd = "POWer"
            class ALC(SCPINode):
                _cmd = "ALC"
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MODE"
                class SVARiable(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SVARiable"
            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ATTenuation"
                class AUTO(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "AUTO"
            class CORRection(SCPINode, SCPISet):
                _cmd = "CORRection"
                class ACQuire(SCPINode, SCPISet):
                    _cmd = "ACQuire"
                    class VERification(SCPINode):
                        _cmd = "VERification"
                        class RESult(SCPINode, SCPIQuery):
                            _cmd = "RESult"
                class COLLect(SCPINode, SCPISet):
                    _cmd = "COLLect"
                    class ACQuire(SCPINode, SCPISet):
                        _cmd = "ACQuire"
                        class VERification(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "VERification"
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "STATe"
                    class AVERage(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "AVERage"
                        class COUNt(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "COUNt"
                        class NTOLerance(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "NTOLerance"
                    class CFACtor(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "CFACtor"
                    class FLATness(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FLATness"
                    class METHod(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "METHod"
                    class PMReadings(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "PMReadings"
                    class RRECeiver(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "RRECeiver"
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DATA"
                    class PARameter(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "PARameter"
                        class COUNt(SCPINode, SCPIQuery):
                            _cmd = "COUNt"
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "PORT"
                class DEFault(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DEFault"
                class FAST(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FAST"
                class GENerator(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "GENerator"
                    class LEVel(SCPINode):
                        _cmd = "LEVel"
                        class OFFSet(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "OFFSet"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class HARMonic(SCPINode, SCPISet):
                    _cmd = "HARMonic"
                    class ACQuire(SCPINode, SCPISet):
                        _cmd = "ACQuire"
                class IMODulation(SCPINode):
                    _cmd = "IMODulation"
                    class LTONe(SCPINode, SCPISet):
                        _cmd = "LTONe"
                        class ACQuire(SCPINode, SCPISet):
                            _cmd = "ACQuire"
                    class PORT(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "PORT"
                    class UTONe(SCPINode, SCPISet):
                        _cmd = "UTONe"
                        class ACQuire(SCPINode, SCPISet):
                            _cmd = "ACQuire"
                class LEVel(SCPINode):
                    _cmd = "LEVel"
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "OFFSet"
                class MIXer(SCPINode):
                    _cmd = "MIXer"
                    class IF(SCPINode, SCPISet):
                        _cmd = "IF"
                        class ACQuire(SCPINode, SCPISet):
                            _cmd = "ACQuire"
                    class LO(SCPINodeN, SCPISet):
                        _cmd = "LO"
                        class ACQuire(SCPINode, SCPISet):
                            _cmd = "ACQuire"
                    class RF(SCPINode, SCPISet):
                        _cmd = "RF"
                        class ACQuire(SCPINode, SCPISet):
                            _cmd = "ACQuire"
                class NREadings(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "NREadings"
                class OSOurces(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "OSOurces"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class PMETer(SCPINode):
                    _cmd = "PMETer"
                    class ID(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "ID"
                class PPOWer(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "PPOWer"
                class PSELect(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "PSELect"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
                class TCOefficient(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TCOefficient"
                    class CALibration(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "CALibration"
                    class COUNt(SCPINode, SCPIQuery):
                        _cmd = "COUNt"
                    class DEFine(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "DEFine"
                    class DELete(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "DELete"
                        class ALL(SCPINode, SCPISet):
                            _cmd = "ALL"
                        class DUMMy(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "DUMMy"
                    class FEED(SCPINode, SCPISet):
                        _cmd = "FEED"
                    class INSert(SCPINodeN, SCPIQuery, SCPISet):
                        _cmd = "INSert"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
            class COUPle(SCPINode, SCPIQuery, SCPISet):
                _cmd = "COUPle"
            class GENerator(SCPINodeN):
                _cmd = "GENerator"
                class LLIMit(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "LLIMit"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                    class VALue(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "VALue"
                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "OFFSet"
                class PERManent(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "PERManent"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class LEVel(SCPINode, SCPIQuery, SCPISet):
                _cmd = "LEVel"
                class IMMediate(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "IMMediate"
                    class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "AMPLitude"
                    class LLIMit(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "LLIMit"
                        class DGRaccess(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "DGRaccess"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                        class VALue(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "VALue"
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "OFFSet"
                    class SLOPe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SLOPe"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
            class PERManent(SCPINode, SCPIQuery, SCPISet):
                _cmd = "PERManent"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class REDuce(SCPINode, SCPIQuery, SCPISet):
                _cmd = "REDuce"
                class SDELay(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SDELay"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class STARt(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STARt"
            class STATe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATe"
            class STOP(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STOP"
        class TDIF(SCPINode):
            _cmd = "TDIF"
            class WAVes(SCPINode, SCPIQuery, SCPISet):
                _cmd = "WAVes"
    class STATus(SCPINode):
        _cmd = "STATus"
        class OPERation(SCPINode, SCPIQuery, SCPISet):
            _cmd = "OPERation"
            class CONDition(SCPINode, SCPIQuery):
                _cmd = "CONDition"
            class ENABle(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ENABle"
            class EVENt(SCPINode, SCPIQuery):
                _cmd = "EVENt"
            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                _cmd = "NTRansition"
            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                _cmd = "PTRansition"
        class PRESet(SCPINode, SCPISet):
            _cmd = "PRESet"
        class QUEStionable(SCPINode, SCPIQuery, SCPISet):
            _cmd = "QUEStionable"
            class CONDition(SCPINode, SCPIQuery):
                _cmd = "CONDition"
            class ENABle(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ENABle"
            class EVENt(SCPINode, SCPIQuery):
                _cmd = "EVENt"
            class INTegrity(SCPINode, SCPIQuery, SCPISet):
                _cmd = "INTegrity"
                class CONDition(SCPINode, SCPIQuery):
                    _cmd = "CONDition"
                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ENABle"
                class EVENt(SCPINode, SCPIQuery):
                    _cmd = "EVENt"
                class HARDware(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "HARDware"
                    class CONDition(SCPINode, SCPIQuery):
                        _cmd = "CONDition"
                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "ENABle"
                    class EVENt(SCPINode, SCPIQuery):
                        _cmd = "EVENt"
                    class NTRansition(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "NTRansition"
                    class PTRansition(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "PTRansition"
                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "NTRansition"
                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "PTRansition"
            class LIMit(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "LIMit"
                class CONDition(SCPINode, SCPIQuery):
                    _cmd = "CONDition"
                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ENABle"
                class EVENt(SCPINode, SCPIQuery):
                    _cmd = "EVENt"
                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "NTRansition"
                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "PTRansition"
            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                _cmd = "NTRansition"
            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                _cmd = "PTRansition"
        class QUEue(SCPINode, SCPIQuery, SCPISet):
            _cmd = "QUEue"
            class NEXT(SCPINode, SCPIQuery):
                _cmd = "NEXT"
    class SYSTem(SCPINode):
        _cmd = "SYSTem"
        class COMMunicate(SCPINode):
            _cmd = "COMMunicate"
            class AKAL(SCPINode):
                _cmd = "AKAL"
                class CONNection(SCPINode, SCPISet):
                    _cmd = "CONNection"
                class MMEMory(SCPINode, SCPISet):
                    _cmd = "MMEMory"
                    class STATe(SCPINode, SCPISet):
                        _cmd = "STATe"
            class CODec(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CODec"
            class GPIB(SCPINode):
                _cmd = "GPIB"
                class SELF(SCPINode):
                    _cmd = "SELF"
                    class ADDRess(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "ADDRess"
                    class INIT(SCPINode):
                        _cmd = "INIT"
                        class WAIT(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "WAIT"
                    class LPORt(SCPINode):
                        _cmd = "LPORt"
                        class ALIGn(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "ALIGn"
                    class RTERminator(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "RTERminator"
            class INTernal(SCPINode):
                _cmd = "INTernal"
                class COMMand(SCPINode):
                    _cmd = "COMMand"
                    class TABLes(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "TABLes"
                class REMote(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "REMote"
            class NET(SCPINode):
                _cmd = "NET"
                class HOSTname(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "HOSTname"
            class RDEVice(SCPINode):
                _cmd = "RDEVice"
                class AKAL(SCPINodeN):
                    _cmd = "AKAL"
                    class ADDRess(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "ADDRess"
                        class ALL(SCPINode, SCPIQuery):
                            _cmd = "ALL"
                    class CATalog(SCPINode, SCPIQuery):
                        _cmd = "CATalog"
                    class CKIT(SCPINode):
                        _cmd = "CKIT"
                        class CATalog(SCPINode, SCPIQuery):
                            _cmd = "CATalog"
                        class STANdard(SCPINode):
                            _cmd = "STANdard"
                            class CATalog(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "CATalog"
                    class CONFigure(SCPINode):
                        _cmd = "CONFigure"
                        class AUTO(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "AUTO"
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "STATe"
                    class COUNt(SCPINode, SCPIQuery):
                        _cmd = "COUNt"
                    class DATE(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DATE"
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DEFine"
                    class DELete(SCPINode, SCPISet):
                        _cmd = "DELete"
                    class FRANge(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "FRANge"
                    class PORTs(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "PORTs"
                    class PREDuction(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "PREDuction"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                    class SDATa(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SDATa"
                    class WARMup(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "WARMup"
                        class STATe(SCPINode, SCPIQuery):
                            _cmd = "STATe"
                class GENerator(SCPINodeN):
                    _cmd = "GENerator"
                    class CATalog(SCPINode, SCPIQuery):
                        _cmd = "CATalog"
                    class COUNt(SCPINode, SCPIQuery):
                        _cmd = "COUNt"
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DEFine"
                    class DELete(SCPINode, SCPISet):
                        _cmd = "DELete"
                    class SEPMode(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SEPMode"
                    class SEPower(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SEPower"
                class PMETer(SCPINodeN):
                    _cmd = "PMETer"
                    class AZERo(SCPINode, SCPISet):
                        _cmd = "AZERo"
                    class CATalog(SCPINode, SCPIQuery):
                        _cmd = "CATalog"
                    class CONFigure(SCPINode):
                        _cmd = "CONFigure"
                        class AUTO(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "AUTO"
                            class STATe(SCPINode, SCPIQuery, SCPISet):
                                _cmd = "STATe"
                    class COUNt(SCPINode, SCPIQuery):
                        _cmd = "COUNt"
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DEFine"
                    class DELete(SCPINode, SCPISet):
                        _cmd = "DELete"
                    class SPCorrection(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "SPCorrection"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
                class SMATrix(SCPINodeN):
                    _cmd = "SMATrix"
                    class CATalog(SCPINode, SCPIQuery):
                        _cmd = "CATalog"
                    class COMMand(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "COMMand"
                    class CONFigure(SCPINode):
                        _cmd = "CONFigure"
                        class ABORt(SCPINode, SCPISet):
                            _cmd = "ABORt"
                        class END(SCPINode, SCPISet):
                            _cmd = "END"
                        class MLTest(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "MLTest"
                        class MLVNa(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "MLVNa"
                        class MTESt(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "MTESt"
                        class MVNA(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "MVNA"
                        class STARt(SCPINode, SCPISet):
                            _cmd = "STARt"
                        class TVNA(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "TVNA"
                    class COUNt(SCPINode, SCPIQuery):
                        _cmd = "COUNt"
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "DEFine"
                    class DELete(SCPINode, SCPISet):
                        _cmd = "DELete"
                    class RELays(SCPINode):
                        _cmd = "RELays"
                        class SWITch(SCPINode):
                            _cmd = "SWITch"
                            class COUNt(SCPINode, SCPIQuery):
                                _cmd = "COUNt"
            class TCPip(SCPINode):
                _cmd = "TCPip"
                class CONTrol(SCPINode, SCPIQuery):
                    _cmd = "CONTrol"
        class CORRection(SCPINode):
            _cmd = "CORRection"
            class FMPort(SCPINode, SCPIQuery, SCPISet):
                _cmd = "FMPort"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
        class DATE(SCPINode, SCPIQuery, SCPISet):
            _cmd = "DATE"
        class DFPRint(SCPINode, SCPIQuery):
            _cmd = "DFPRint"
        class DISPlay(SCPINode):
            _cmd = "DISPlay"
            class BAR(SCPINode):
                _cmd = "BAR"
                class HKEY(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "HKEY"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class MENU(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "MENU"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class STATus(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATus"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class STOols(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STOols"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class TITLe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TITLe"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
                class TOOLs(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TOOLs"
                    class STATe(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "STATe"
            class COLor(SCPINode, SCPIQuery, SCPISet):
                _cmd = "COLor"
            class CONDuctances(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CONDuctances"
            class DIALogs(SCPINode):
                _cmd = "DIALogs"
                class SETup(SCPINode):
                    _cmd = "SETup"
                    class MCAL(SCPINode, SCPIQuery, SCPISet):
                        _cmd = "MCAL"
                        class STATe(SCPINode, SCPIQuery, SCPISet):
                            _cmd = "STATe"
            class UPDate(SCPINode, SCPIQuery, SCPISet):
                _cmd = "UPDate"
        class ERRor(SCPINode, SCPIQuery, SCPISet):
            _cmd = "ERRor"
            class ALL(SCPINode, SCPIQuery):
                _cmd = "ALL"
            class DISPlay(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DISPlay"
                class ERRor(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ERRor"
                class INFO(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "INFO"
                class REMote(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "REMote"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
                class WARNings(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "WARNings"
            class NEXT(SCPINode, SCPIQuery):
                _cmd = "NEXT"
        class FIRMware(SCPINode):
            _cmd = "FIRMware"
            class UPDate(SCPINode, SCPISet):
                _cmd = "UPDate"
        class FPReset(SCPINode, SCPISet):
            _cmd = "FPReset"
        class FREQuency(SCPINode, SCPIQuery, SCPISet):
            _cmd = "FREQuency"
        class IDENtify(SCPINode, SCPIQuery, SCPISet):
            _cmd = "IDENtify"
            class FACTory(SCPINode, SCPISet):
                _cmd = "FACTory"
            class STRing(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STRing"
        class INFO(SCPINode):
            _cmd = "INFO"
            class CONTrast(SCPINode, SCPIQuery, SCPISet):
                _cmd = "CONTrast"
        class KLOCk(SCPINode, SCPIQuery, SCPISet):
            _cmd = "KLOCk"
        class LANGuage(SCPINode, SCPIQuery, SCPISet):
            _cmd = "LANGuage"
        class LOGGing(SCPINode):
            _cmd = "LOGGing"
            class REMote(SCPINode, SCPIQuery, SCPISet):
                _cmd = "REMote"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
        class NOPeration(SCPINode, SCPISet):
            _cmd = "NOPeration"
        class OPTions(SCPINode, SCPIQuery, SCPISet):
            _cmd = "OPTions"
            class DISable(SCPINode, SCPISet):
                _cmd = "DISable"
            class FACTory(SCPINode, SCPISet):
                _cmd = "FACTory"
            class STRing(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STRing"
        class PASSword(SCPINode, SCPISet):
            _cmd = "PASSword"
            class CENable(SCPINode, SCPISet):
                _cmd = "CENable"
        class PRESet(SCPINode, SCPIQuery, SCPISet):
            _cmd = "PRESet"
            class DUMMy(SCPINode, SCPIQuery, SCPISet):
                _cmd = "DUMMy"
            class REMote(SCPINode, SCPIQuery, SCPISet):
                _cmd = "REMote"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class SCOPe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SCOPe"
            class USER(SCPINode, SCPIQuery, SCPISet):
                _cmd = "USER"
                class CAL(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "CAL"
                class NAME(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "NAME"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
        class PRIority(SCPINode, SCPIQuery, SCPISet):
            _cmd = "PRIority"
        class SETTings(SCPINode):
            _cmd = "SETTings"
            class UPDate(SCPINode, SCPISet):
                _cmd = "UPDate"
        class SHUTdown(SCPINode, SCPISet):
            _cmd = "SHUTdown"
        class SMATrix(SCPINode):
            _cmd = "SMATrix"
            class OPTimization(SCPINode, SCPIQuery, SCPISet):
                _cmd = "OPTimization"
        class SOUNd(SCPINode):
            _cmd = "SOUNd"
            class ALARm(SCPINode, SCPIQuery, SCPISet):
                _cmd = "ALARm"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
            class STATus(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STATus"
                class STATe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "STATe"
        class TIME(SCPINode, SCPIQuery, SCPISet):
            _cmd = "TIME"
            class INTermediate(SCPINode, SCPIQuery):
                _cmd = "INTermediate"
            class STARt(SCPINode, SCPISet):
                _cmd = "STARt"
            class STOP(SCPINode, SCPIQuery):
                _cmd = "STOP"
            class SYNC(SCPINode, SCPISet):
                _cmd = "SYNC"
        class TSLock(SCPINode, SCPIQuery, SCPISet):
            _cmd = "TSLock"
        class USER(SCPINode):
            _cmd = "USER"
            class DISPlay(SCPINode):
                _cmd = "DISPlay"
                class TITLe(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "TITLe"
            class FKEY(SCPINode, SCPIQuery, SCPISet):
                _cmd = "FKEY"
            class KEY(SCPINode, SCPIQuery, SCPISet):
                _cmd = "KEY"
                class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "FUNCtion"
        class VERSion(SCPINode, SCPIQuery):
            _cmd = "VERSion"
        class WAIT(SCPINode, SCPISet):
            _cmd = "WAIT"
    class TRACe(SCPINode, SCPIQuery, SCPISet):
        _cmd = "TRACe"
        class CLEar(SCPINode, SCPISet):
            _cmd = "CLEar"
        class COPY(SCPINode, SCPISet):
            _cmd = "COPY"
            class MATH(SCPINode, SCPISet):
                _cmd = "MATH"
        class DATA(SCPINode, SCPIQuery, SCPISet):
            _cmd = "DATA"
            class RESPonse(SCPINode, SCPIQuery, SCPISet):
                _cmd = "RESPonse"
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ALL"
            class STIMulus(SCPINode, SCPIQuery, SCPISet):
                _cmd = "STIMulus"
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ALL"
    class TRIGger(SCPINodeN):
        _cmd = "TRIGger"
        class CHANnel(SCPINodeN):
            _cmd = "CHANnel"
            class AUXiliary(SCPINodeN, SCPIQuery, SCPISet):
                _cmd = "AUXiliary"
                class DURation(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "DURation"
                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "ENABle"
                class INTerval(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "INTerval"
                class OPOLarity(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "OPOLarity"
                class POSition(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "POSition"
        class SEQuence(SCPINode):
            _cmd = "SEQuence"
            class HOLDoff(SCPINode, SCPIQuery, SCPISet):
                _cmd = "HOLDoff"
            class LINK(SCPINode, SCPIQuery, SCPISet):
                _cmd = "LINK"
            class MULTiple(SCPINode):
                _cmd = "MULTiple"
                class HOLDoff(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "HOLDoff"
                class SLOPe(SCPINodeN, SCPIQuery, SCPISet):
                    _cmd = "SLOPe"
                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    _cmd = "SOURce"
            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SLOPe"
            class SOURce(SCPINode, SCPIQuery, SCPISet):
                _cmd = "SOURce"
    # END OF FILE
