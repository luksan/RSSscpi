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


def test_stb(caplog):
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


def test_esr():
    esr = EventStatusRegister(255)
    assert len(esr.BITS) == 7
    assert esr.short_status() == "OPC,QERR,DDE,EXE,CMD,USR,PWR"


def test_pprint(capsys):
    stb = StatusByteRegister(252)
    assert stb.pprint_str() == """
STB: 0b11111100, 252
    error_queue_not_empty, ERR  (bit 2) 4
      questionable_status, QUES (bit 3) 8
        message_available, MAV  (bit 4) 16
     event_status_summary, ESB  (bit 5) 32
    master_status_summary, MSS  (bit 6) 64
 operation_status_summary, OPER (bit 7) 128
        """.strip()

    stb.pprint()
    assert capsys.readouterr()[0] == stb.pprint_str() + "\n"

    esr = EventStatusRegister(253)
    assert esr.pprint_str() == """
ESR: 0b11111101, 253
       operation_complete, OPC  (bit 0) 1
              query_error, QERR (bit 2) 4
   device_dependent_error, DDE  (bit 3) 8
          exceution_error, EXE  (bit 4) 16
            command_error, CMD  (bit 5) 32
             user_request, USR  (bit 6) 64
                 power_on, PWR  (bit 7) 128
        """.strip()

    esr.pprint()
    assert capsys.readouterr()[0] == esr.pprint_str() + "\n"
