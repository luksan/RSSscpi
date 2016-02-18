# -*- coding: utf-8 -*-

from setuptools import setup
from tools.generate_class_defs import generate_SCPI_class


generate_SCPI_class("ZVA_commands_3_60.inp", "ZVA_gen")
generate_SCPI_class("ZNB_commands_2_56.inp", "ZNB_gen")

setup(name='RSSscpi',
      version='0.1',
      description='A package for controlling SCPI based instruments in a pythonic way.',
      url='http://github.com/luksan/RSSscpi',
      author='Lukas Sandström',
      author_email='lukas.sandstrom@rohde-schwarz.com',
      license='MIT',
      packages=['RSSscpi', 'RSSscpi.gen'])
