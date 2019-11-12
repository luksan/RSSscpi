# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""


class InstrumentInfo:
    def __init__(self, idn_node):
        self._idn_node = idn_node
        self._idn = None

    def query_idn(self) -> str:
        self._idn = str(self._idn_node.q())
        return self._idn

    @property
    def manufacturer(self):
        if self._idn is None:
            self.query_idn()
        return self._idn.split(",")[0]

    @property
    def model(self):
        if self._idn is None:
            self.query_idn()
        return self._idn.split(",")[1]

    @property
    def serial_number(self):
        if self._idn is None:
            self.query_idn()
        return self._idn.split(",")[2]

    @property
    def firmware(self):
        if self._idn is None:
            self.query_idn()
        return self._idn.split(",")[3]
