# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='RSSscpi',
      version='0.1',
      description='A package for controlling SCPI based instruments in a pythonic way.',
      url='http://github.com/luksan/RSSscpi',
      author='Lukas Sandström',
      author_email='lukas.sandstrom@rohde-schwarz.com',
      license='MIT',
      packages=['RSSscpi', 'RSSscpi.gen'])