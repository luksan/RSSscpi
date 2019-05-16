# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import pytest
import pathlib

import os

import RSSscpi.znb
from RSSscpi.znb import ZNB


def test_znb_idn(znb):
    assert str(znb.IDN.q()).startswith("Rohde-Schwarz,ZNB")
