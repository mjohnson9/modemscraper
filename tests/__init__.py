# -*- coding: utf-8 -*-

"""Unit test package for modemscraper."""

import httmock
import os.path


# Mock all of the modem's pages that we use
@httmock.urlmatch(netloc='192.168.100.1', path='/indexData.html')
def index_page(url, request):
    return open(os.path.join(os.path.dirname(__file__), 'example_pages/indexData.html')).read()


@httmock.urlmatch(netloc='192.168.100.1', path='/cmLogsData.html')
def logs_page(url, request):
    return open(os.path.join(os.path.dirname(__file__), 'example_pages/cmLogsData.html')).read()


@httmock.urlmatch(netloc='192.168.100.1', path='/cmSignalData.html')
def signals_page(url, request):
    return open(os.path.join(os.path.dirname(__file__), 'example_pages/cmSignalData.html')).read()
