#!/usr/bin/env python2
from distutils.core import setup

setup(
    name='drone-inspy',
    version='1.0.0',
    author='Jonathan Broche',
    scripts=['bin/drone-inspy'],
    url='https://github.com/lair-framework/drone-inspy',
    license='LICENSE',
    description='Parses and imports InSpy JSON output into a lair project.',
    install_requires=[
        "pylair >= 1.0.2", 
        "requests == 2.7.0"
    ],
)
