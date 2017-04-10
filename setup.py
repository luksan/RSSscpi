# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

setup(name='RSSscpi',
      version='0.1.0',
      description='A package for controlling SCPI based instruments in a pythonic way.',
      url='http://github.com/luksan/RSSscpi',
      author='Lukas Sandström',
      author_email='lukas.sandstrom@rohde-schwarz.com',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
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
              #'Programming Language :: Python :: 3',
              #'Programming Language :: Python :: 3.3',
              #'Programming Language :: Python :: 3.4',
              #'Programming Language :: Python :: 3.5',
              #'Programming Language :: Python :: 3.6',
              #'Programming Language :: Python :: Implementation :: CPython',
              #'Programming Language :: Python :: Implementation :: PyPy',
              'Topic :: Software Development :: Libraries',
          ],
)
