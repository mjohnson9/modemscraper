# -*- coding: utf-8 -*-

"""
The parser module parses raw units from the modem's pages and converts them
into machine-usable values.
"""
import pint


_unit_registry = None  # scope the default unit registry


def parse(to_parse):
    """
    parse parses unit values from Surfboard pages into a tuple.

    Currently, parse supports:

    * plain integers
    * frequencies expressed in Hz
    * power levels expressed in dB
    * power levels expressed in dBmV
    * symbol rates expressed in Sym/sec

    Args:
        to_parse (TYPE): Description

    Returns:
        tuple: A tuple containing ()

    Raises:
        TypeError: if the value given is not a string.
        ValueError: if the value given is not known to the parser.
    """

    if not isinstance(to_parse, str):
        raise TypeError("input must be a string")

    parsed = None

    try:
        parsed = _unit_registry(to_parse)
    except pint.errors.UndefinedUnitError as err:
        raise ValueError(err)

    if isinstance(parsed, int):
        return (parsed, 'integer')

    parsed = parsed.to_base_units()

    return (parsed.magnitude, '%s' % parsed.units)


def _get_unit_registry():
    # create an empty registry
    _unit_registry = pint.UnitRegistry(filename=None)

    # units from Pint's own defaults
    _unit_registry.define("second = [time] = s = sec")
    _unit_registry.define("[frequency] = 1 / [time]")
    _unit_registry.define("hertz = 1 / second = Hz")

    # our own units
    _unit_registry.define("symbol = [] = sym")
    _unit_registry.define("decibel = [] = dB")
    _unit_registry.define("dBmV = []")

    # our prefixes
    _unit_registry.define("M- = 1000000")

    return _unit_registry


_unit_registry = _get_unit_registry()  # setup our default unit registry
