# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from typing import Tuple

from .scpi.gen_support import SCPINode

class InstrumentInfo:
    def __init__(self, idn_node: SCPINode, opt_node: SCPINode):
        self._idn_node = idn_node
        self._opt_node = opt_node
        self._idn = None  # type: str
        self._opt = None  # type: Tuple[str, ...]

    def query_idn(self) -> str:
        self._idn = str(self._idn_node.q())
        return self._idn

    def query_opt(self) -> str:
        opt = self._opt_node.q()
        self._opt = tuple(opt.split_comma(str))
        return str(opt)

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

    @property
    def installed_options(self) -> Tuple[str, ...]:
        if self._opt is None:
            self.query_opt()
        return self._opt

    def has_option(self, option: str) -> bool:
        """
        Check if the instrument has the given option in the *OPT? string.
        Each installed option is compared with .endwith(option)

        :param option: The option string to test for
        :return: True if the option is installed, False otherwise
        """
        for installed in self.installed_options:
            if installed.endswith(option):
                return True
        return False
