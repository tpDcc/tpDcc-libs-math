#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for tpDcc-libs-math
"""

from tpDcc.libs.math import __version__

import pytest


def test_version():
    assert __version__.get_version()
