#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

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
    description="Modem scraper retrieves important information from Surfboard-like modem status pages.",
    long_description=readme + '\n\n' + history,
    author="Michael Johnson",
    author_email='michael@johnson.computer',
    url='https://github.com/nightexcessive/modemscraper',
    packages=find_packages(include=['modemscraper']),
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='modemscraper',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
