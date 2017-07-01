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

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'beautifulsoup4',
    'Pint',
    'requests'
]

setup_requirements = [
    'pytest-runner',
    # TODO(nightexcessive): put setup requirements (distutils extensions,
    # etc.) here
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'httmock'
]

setup(
    name='modemscraper',
    version='0.2.0',
    description='Modem scraper retrieves important information from '
                'Surfboard-like modem status pages.',
    long_description=readme + '\n\n' + history,
    author='Michael Johnson',
    author_email='michael@johnson.computer',
    url='https://github.com/nightexcessive/modemscraper',
    packages=find_packages(include=['modemscraper']),
    include_package_data=True,
    install_requires=requirements,
    license='GNU General Public License v3',
    zip_safe=False,
    keywords='modemscraper',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
