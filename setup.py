#!/usr/bin/env python3
from distutils.version import LooseVersion
import os
import pip
from setuptools import find_packages
from setuptools import setup
import sys

requirements = {
    'setup': [
        'numpy',
        'configargparse>=1.2.1'
        'beautifulsoup4>=4.9.0'
        'requests>=2.23.0'
    ]}

setup_requires = requirements['setup']