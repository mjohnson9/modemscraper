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

"""Contains utilities and classes for representing DOCSIS channels."""


class Channel:
    """Represents a DOCSIS channel.

    Attributes:
        frequency (int): This channel's frequency in Hertz.
        id (int): This channel's DOCSIS channel ID.
        power (float): This channel's power level in dBmV.

    """

    def __init__(self, channel_id, frequency, power):
        """Create a new Channel.

        Args:
            channel_id (int): This channel's DOCSIS channel ID.
            frequency (int): This channel's frequency in Hertz.
            power (float): This channel's power level in dBmV.
        """
        self.id = channel_id
        self.frequency = frequency
        self.power = power

    def __repr__(self):
        """Create a string representation of this channel.

        Returns:
            str: A string representation of this channel.

        """
        return '<Channel(%dHz)>' % self.frequency


class DownstreamChannel(Channel):
    """Represents a DOCSIS downstream channel.

    Attributes:
        modulation (str): This channel's DOCSIS modulation.
        signal_to_noise (float): This channel's signal to noise ratio in dBmV.

    """

    def __init__(self, channel_id, frequency, power, modulation, snr):
        """Create a DOCSIS downstream channel.

        Args:
            channel_id (int): This channel's DOCSIS channel ID.
            frequency (int): This channel's frequency in Hertz.
            power (float): This channel's power level in dBmV.
            modulation (str): This channel's DOCSIS modulation.
            snr (float): This channel's SNR in dBmV.
        """
        super().__init__(channel_id, frequency, power)

        self.modulation = modulation
        self.signal_to_noise = snr

    def __repr__(self):
        """Create a string representation of this channel.

        Returns:
            str: A string representation of this channel.

        """
        return '<DownstreamChannel(%dHz)>' % self.frequency


class UpstreamChannel(Channel):
    """Represents a DOCSIS upstream channel.

    Attributes:
        symbol_rate (float): This channel's symbol rate in symbols per second.

    """

    def __init__(self, channel_id, frequency, power, symbol_rate):
        """Create a DOCSIS upstream channel.

        Args:
            channel_id (int): This channel's DOCSIS channel ID.
            frequency (int): This channel's frequency in Hertz.
            power (float): This channel's power level in dBmV.
            symbol_rate (float): Symbol rate in sym/sec.
        """
        super().__init__(channel_id, frequency, power)

        self.symbol_rate = symbol_rate

    def __repr__(self):
        """Create a string representation of this channel.

        Returns:
            str: A string representation of this channel.

        """
        return '<UpstreamChannel(%dHz)>' % self.frequency
