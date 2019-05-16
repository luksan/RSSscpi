# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import logging

import pytest

import RSSscpi
import RSSscpi.znb


@pytest.fixture(scope="module")
def znb():
    z = RSSscpi.znb.connect_ethernet("localhost")
    yield z
    z._visa_res.close()
