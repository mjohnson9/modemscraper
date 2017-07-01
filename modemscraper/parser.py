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

import pint


_unit_registry = None  # scope the default unit registry


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

    parsed = None

    try:
        parsed = _unit_registry(to_parse)
    except pint.errors.UndefinedUnitError as err:
        raise ValueError(err)

    if isinstance(parsed, int):
        return (parsed, 'integer')

    if format(parsed.units) != 'hertz':
        # we check that the unit isn't hertz because our spec calls for hertz
        # being returned as such
        parsed.ito_base_units()  # convert to base units in place

    return (parsed.magnitude, '%s' % parsed.units)


def _get_unit_registry():
    # create an empty registry
    _unit_registry = pint.UnitRegistry(filename=None)

    # units from Pint's own defaults
    _unit_registry.define('second = [time] = s = sec')
    _unit_registry.define('[frequency] = 1 / [time]')
    _unit_registry.define('hertz = 1 / second = Hz')

    # our own units
    _unit_registry.define('symbol = [] = sym')
    _unit_registry.define('decibel = [] = dB')
    _unit_registry.define('dBmV = []')

    # our prefixes
    _unit_registry.define('mega- = 1000000 = M-')

    return _unit_registry


_unit_registry = _get_unit_registry()  # setup our default unit registry
