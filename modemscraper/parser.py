# -*- coding: utf-8 -*-
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
