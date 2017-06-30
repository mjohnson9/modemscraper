# -*- coding: utf-8 -*-

"""Tests for modemscraper.parser package with cases from the signals page."""

import pytest

from modemscraper import parser


def test_parse_non_str():
    with pytest.raises(TypeError):
        parser.parse(True)

    with pytest.raises(TypeError):
        parser.parse(1)


def test_parse_bare_int():
    assert parser.parse('15') == (15, 'integer')


def test_parse_frequency():
    assert parser.parse('639000000 Hz') == (639000000, 'hertz')
    assert parser.parse('603000000 Hz') == (603000000, 'hertz')


def test_parse_snr():
    assert parser.parse('38 dB') == (38, 'decibel')


def test_parse_modulation():
    with pytest.raises(ValueError):
        parser.parse('QAM256')


def test_parse_power_level():
    assert parser.parse('7 dBmV') == (7, 'dBmV')
    assert parser.parse('-7 dBmV') == (-7, 'dBmV')


def test_parse_symbol_rate():
    assert parser.parse('5.120 Msym/sec') == (5120000, 'symbol / second')
    assert parser.parse('2.560 Msym/sec') == (2560000, 'symbol / second')


def test_parse_ranging_status():
    with pytest.raises(ValueError):
        parser.parse('Success')
