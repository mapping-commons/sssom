#!/usr/bin/env python
import sys
from setuptools import setup
from warnings import warn

if sys.version_info < (3, 7, 0):
    warn(f"Python version 3.7 or later is required for sssom.  Current version: {sys.version_info}")
    sys.exit(1)

setup(
    setup_requires=['pbr'],
    pbr=True,
)
