#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import re
import io
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()

setup(name='RSSscpi',
      version='0.1.0.dev1',
      description='A package for controlling SCPI based instruments in a pythonic way.',
      long_description='%s' % (
            re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst'))
        ),
      url='http://github.com/luksan/RSSscpi',
      author='Lukas Sandström',
      author_email='lukas.sandstrom@rohde-schwarz.com',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
      classifiers=[
              # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
              'Development Status :: 3 - Alpha',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: BSD License',
              'Operating System :: Unix',
              'Operating System :: POSIX',
              'Operating System :: Microsoft :: Windows',
              'Programming Language :: Python',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              'Programming Language :: Python :: 3.7',
              'Programming Language :: Python :: Implementation :: CPython',
              'Programming Language :: Python :: Implementation :: PyPy',
              'Topic :: Software Development :: Libraries',
      ],
      keywords='instrument control SCPI VISA VNA',
      install_requires=['PyVISA>=1.8',
                        'enum34;python_version<"3.4"',
                        'memoized-property>=1.0.3',
                        'zeroconf>=0.19.1'],
      # List additional groups of dependencies here (e.g. development
      # dependencies). You can install these using the following syntax,
      # for example:
      # $ pip install -e .[dev,test]
      extras_require={
          'dev': ['beautifulsoup4>=4.5.1', 'pytest>=3.07', 'numpy>=1.11.2']
      }
      )
