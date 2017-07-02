=============
Modem Scraper
=============


.. image:: https://img.shields.io/pypi/v/modemscraper.svg
        :target: https://pypi.python.org/pypi/modemscraper

.. image:: https://img.shields.io/travis/nightexcessive/modemscraper.svg
        :target: https://travis-ci.org/nightexcessive/modemscraper

.. image:: https://coveralls.io/repos/github/nightexcessive/modemscraper/badge.svg?branch=develop
        :target: https://coveralls.io/github/nightexcessive/modemscraper?branch=develop


.. image:: https://readthedocs.org/projects/modemscraper/badge/?version=latest
        :target: https://modemscraper.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/nightexcessive/modemscraper/shield.svg
     :target: https://pyup.io/repos/github/nightexcessive/modemscraper/
     :alt: Updates


Modem scraper retrieves important information from Surfboard-like modem status pages. I developed this so that I could write a Zabbix agent to monitor the status of my Charter SB6141 modem.

So far, it has been tested on the SB6141 running Charter Communication's firmware. If you would like to contribute your modem's status pages for addition, please open an issue.


* Free software: GNU General Public License v3
* Documentation: https://modemscraper.readthedocs.io.


Features
--------

Modem scraper can fetch information from a supported modem's status page, including:

* operational status
* channel statistics, both upstream and downstream
* logs

