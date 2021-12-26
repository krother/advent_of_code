#!/usr/bin/env python
#
# Copyright 2021 Kristian Rother
#
# Please see the LICENSE file that should have been included
# as part of this package.

__author__="Kristian Rother"
__email__ ="krother@academis.eu"

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = []

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

package_data ={}

setup(
        name = "aoc",
        version = "20.21",
        description = "solutions to Advent of Code challenges",
        keywords='coding kata',
        long_description=readme,
        license = 'MIT',
        url='https://github.com/krother/advent_of_code',
        classifiers = [
            'Development Status :: 5 - Production',
            'Intended Audience :: Developers',
            'Topic :: Coding',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.8',
        ],
        install_requires=requirements,
        #setup_requires=setup_requirements,
        test_suite='tests',
        tests_require=test_requirements,
        python_requires='>=3.8',
        author="Kristian Rother",
        author_email="krother@academis.eu",
        extras_require={
            'tests': [
                'pytest',
                'pytest-pep8',
                'pytest-flakes',
            ]
        },
        #py_modules=['tilegamelib'],
        packages=find_packages(include=['aoc']),
        package_data=package_data,
        include_package_data=True,
        data_files=['README.md', 'LICENSE'],
        zip_safe=False,

)
