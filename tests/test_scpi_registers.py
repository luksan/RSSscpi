# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import pytest

from RSSscpi.scpi.scpi_registers import SCPIRegister, scpi_bit, StatusByteRegister, EventStatusRegister


# noinspection PyUnusedLocal
def test_register_definition():
    with pytest.raises(AssertionError):
        class DuplicateBitDef(SCPIRegister):
            @scpi_bit(2)
            def a(self):
                pass

            @scpi_bit(2)
            def b(self):
                pass


def test_stb(capsys, caplog):
    stb = StatusByteRegister(0)
    assert len(stb.BITS) == 6
    assert stb.short_status() == ""
    stb.questionable_status = True
    assert stb.short_status() == "QUES"
    stb.value = 255
    for record in caplog.records:
        assert record.levelname == "WARNING"  # Check that a warning is emitted when bits are set outside of the definition
    assert stb.short_status() == "ERR,QUES,MAV,ESB,MSS,OPER"
    assert stb.error_queue_not_empty
    stb.error_queue_not_empty = 0
    assert stb.short_status() == "QUES,MAV,ESB,MSS,OPER"

    stb.pprint()
    capsys.readouterr()


def test_esr(capsys):
    esr = EventStatusRegister(255)
    assert len(esr.BITS) == 7
    assert esr.short_status() == "OPC,QERR,DDE,EXE,CMD,USR,PWR"

    esr.pprint()
    capsys.readouterr()
