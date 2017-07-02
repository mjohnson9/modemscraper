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

"""Unit test package for modemscraper."""

import os.path

import httmock


# Mock all of the modem's pages that we use
@httmock.urlmatch(netloc='192.168.100.1', path='/indexData.html')
def index_page(url, request):
    """Provide a mock for the modem index page."""
    return open(
        os.path.join(
            os.path.dirname(__file__),
            'example_pages/indexData.html'
        )
    ).read()


@httmock.urlmatch(netloc='192.168.100.1', path='/cmLogsData.html')
def logs_page(url, request):
    """Provide a mock for the modem log page."""
    return open(
        os.path.join(
            os.path.dirname(__file__),
            'example_pages/cmLogsData.html'
        )
    ).read()


@httmock.urlmatch(netloc='192.168.100.1', path='/cmSignalData.html')
def signals_page(url, request):
    """Provide a mock for the modem signal page."""
    return open(
        os.path.join(
            os.path.dirname(__file__),
            'example_pages/cmSignalData.html'
        )
    ).read()
