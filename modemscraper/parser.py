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

"""The parser module parses raw units into machine-usable values.

It is a specialized module for the units found on a modem's status page. As
such, it does not act as a generalized parser.
"""

_SIMPLE_SUFFIXES = [('hz', 'hertz'), ('db', 'decibel'),
                    ('dbmv', 'decibel-millivolt')]

_MULTIPLIER_SUFFIXES = [('msym/sec', 'symbol / second', 1000000)]


def parse(to_parse):
    """Parse unit values from Surfboard pages.

    Currently, parse supports:

    * plain integers
    * frequencies expressed in Hz
    * power levels expressed in dB
    * power levels expressed in dBmV
    * symbol rates expressed in Sym/sec

    Args:
        to_parse (str): A string containing a unit to be parsed.

    Returns:
        tuple: A tuple containing (parsed magnitude, parsed unit type). For
        example:

        (1000000, 'hertz')

    Raises:
        TypeError: if the value given is not a string.
        ValueError: if the value given is not known to the parser.

    """
    if not isinstance(to_parse, str):
        raise TypeError('input must be a string')

    try:
        # if it's a plain integer, go ahead and return it as such
        return (float(to_parse), 'bare')
    except ValueError:
        # isn't a plan integer
        pass

    to_parse_lower = to_parse.lower()

    for simple_suffix, return_type in _SIMPLE_SUFFIXES:
        simple_suffix_spaced = ' ' + simple_suffix
        if to_parse_lower.endswith(simple_suffix_spaced):
            return (
                float(to_parse[:-len(simple_suffix_spaced)]),
                return_type
            )

    for multiplier_suffix, return_type, multiplier in _MULTIPLIER_SUFFIXES:
        multiplier_suffix_spaced = ' ' + multiplier_suffix
        if to_parse_lower.endswith(multiplier_suffix_spaced):
            return (
                float(to_parse[:-len(multiplier_suffix_spaced)]) * multiplier,
                return_type
            )

    raise ValueError('Did not recognize value from "%s"' % to_parse)
