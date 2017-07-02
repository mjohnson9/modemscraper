#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2017 Michael Johnson
#
# This file is part of modemscraper.
#
# modemscraper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# modemscraper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with modemscraper.  If not, see <http://www.gnu.org/licenses/>.

"""Tests for modemscraper.parser package with cases from the signals page."""

import pytest

from modemscraper import parser


class TestInvalid:
    """Tests for invalid cases."""

    def test_parse_non_str(self):
        """Test for an exception when given non-strings."""
        with pytest.raises(TypeError):
            parser.parse(True)

        with pytest.raises(TypeError):
            parser.parse(1)


class TestDownstream:
    """Tests for the downstream portion of the page."""

    def test_parse_bare_int(self):
        """Test simple integers."""
        assert parser.parse('15') == (15, 'bare')

    def test_parse_frequency(self):
        """Test frequencies measured in Hertz."""
        assert parser.parse('639000000 Hz') == (639000000, 'hertz')
        assert parser.parse('603000000 Hz') == (603000000, 'hertz')

    def test_parse_snr(self):
        """Test signal-to-noise ratios measured in decibels (dB)."""
        assert parser.parse('38 dB') == (38, 'decibel')

    def test_parse_modulation(self):
        """Test for an exception when given modulation values."""
        with pytest.raises(ValueError):
            parser.parse('QAM256')

    def test_parse_power_level(self):
        """Test downstream power levels measured in dBmV."""
        assert parser.parse('7 dBmV') == (7, 'decibel-millivolt')
        assert parser.parse('-7 dBmV') == (-7, 'decibel-millivolt')


class TestUpstream:
    """Tests for the upstream portion of the page."""

    def test_parse_symbol_rate(self):
        """Test symbol rates measured in Msym/sec."""
        assert parser.parse('5.120 Msym/sec') == (5120000, 'symbol / second')
        assert parser.parse('2.560 Msym/sec') == (2560000, 'symbol / second')
