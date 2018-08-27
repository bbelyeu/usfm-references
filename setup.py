#!/usr/bin/env python
"""
USFM References Tools
=====================

Tools for working with USFM references in code.

Setup
-----

.. code:: python

    import usfm_references

    usfm_references.valid('GEN.1.1')  # returns True
    usfm_references.valid('BOO.1.1')  # returns False

Links
=====

* `Documentation <https://pythonhosted.org/usfm-references/>`_
* `Source Code <https://github.com/bbelyeu/usfm-references>`_
* `Issues <https://github.com/bbelyeu/usfm-references/issues>`_
* `USFM Standard Reference <http://paratext.org/about/usfm>`_

"""
import ast
import re
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('usfm_references/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name='USFM References',
    version=version,
    url='https://github.com/bbelyeu/usfm-references',
    download_url='https://github.com/bbelyeu/usfm-references/archive/{}.zip'.format(version),
    license='MIT',
    author='Brad Belyeu',
    author_email='bradleylamar@gmail.com',
    description='Tools to work with USFM references',
    long_description=__doc__,
    packages=find_packages(exclude=('tests',)),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
