# -*- coding: utf-8 -*-

"""Tests for modemscraper.parser package with cases from the signals page."""

import unittest

from modemscraper import parser
import pytest


class TestInvalid(unittest.TestCase):
    """Tests for invalid cases."""

    def test_parse_non_str():
        """Test for an exception when given non-strings."""
        with pytest.raises(TypeError):
            parser.parse(True)

        with pytest.raises(TypeError):
            parser.parse(1)


class TestDownstream(unittest.TestCase):
    """Tests for the downstream portion of the page."""

    def test_parse_bare_int():
        """Test simple integers."""
        assert parser.parse('15') == (15, 'integer')

    def test_parse_frequency():
        """Test frequencies measured in Hertz."""
        assert parser.parse('639000000 Hz') == (639000000, 'hertz')
        assert parser.parse('603000000 Hz') == (603000000, 'hertz')

    def test_parse_snr():
        """Test signal-to-noise ratios measured in decibels (dB)."""
        assert parser.parse('38 dB') == (38, 'decibel')

    def test_parse_modulation():
        """Test for an exception when given modulation values."""
        with pytest.raises(ValueError):
            parser.parse('QAM256')

    def test_parse_power_level():
        """Test downstream power levels measured in dBmV."""
        assert parser.parse('7 dBmV') == (7, 'dBmV')
        assert parser.parse('-7 dBmV') == (-7, 'dBmV')


class TestUpstream(unittest.TestCase):
    """Tests for the upstream portion of the page."""

    def test_parse_symbol_rate():
        """Test symbol rates measured in Msym/sec."""
        assert parser.parse('5.120 Msym/sec') == (5120000, 'symbol / second')
        assert parser.parse('2.560 Msym/sec') == (2560000, 'symbol / second')
