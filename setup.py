#!/usr/bin/env python3

#    maria2csv - Render a MariaDB dump as csv
#    Copyright (C) 2024  Andreas Thalhammer
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='maria2csv',
    version='0.0.1',
    url='https://github.com/athalhammer/maria2csv',
    author='Andreas Thalhammer',
    author_email='andreas@thalhammer.bayern',
    description='Pipe a MariaDB dump to commandline',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['maria2csv'],
    entry_points={ 'console_scripts': [
            'maria2csv = maria2csv.maria2csv:main_wrapper'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Database'
    ],
    python_requires='>=3.8',
    install_requires=[]
)
