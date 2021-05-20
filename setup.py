#!/usr/bin/env python

from distutils.core import setup
from os.path import abspath, dirname, join

VERSION = None

version_file = join(dirname(abspath(__file__)), 'ArchiveLibrary', 'version.py')
with open(version_file) as file:
      code = compile(file.read(), version_file, 'exec')
      exec(code)


DESCRIPTION = """
Robot Framework keyword library for handling ZIP files.
"""[1:-1]


CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: Public Domain
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(name         = 'robotframework-archivelibrary',
      version      = VERSION,
      description  = 'Robot Framework keyword library for handling ZIP files',
      long_description = DESCRIPTION,
      author       = 'Bulkan Savun Evcimen',
      author_email = 'bulkan@gmail.com',
      maintainer='Luca Giovenzana',
      maintainer_email='luca@giovenzana.org',
      url          = 'http://github.com/bulkan/robotframework-archivelibrary',
      license      = 'Public Domain',
      keywords     = 'robotframework testing test automation zip files compresssed',
      platforms    = 'any',
      install_requires=[
        'robotframework',
      ],
      classifiers  = CLASSIFIERS.splitlines(),
      packages     = ['ArchiveLibrary'],
      package_data = {'ArchiveLibrary': ['tests/*.txt']}
      )
