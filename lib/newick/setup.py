#!/usr/bin/env python

from setuptools import setup, find_packages
import re
from codecs import open
from os import path
import sys


setup(
    name='newick',
    version="0.0.1",

    description='read and write trees with python',
    long_description="http://www.daimi.au.dk/~mailund/newick.html",
    url='http://www.daimi.au.dk/~mailund/newick.html',
    install_requires=[],
    author='Thomas Mailund',
    author_email='mailund@birc.au.dk',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='bioinformatics',
    packages=["newick"]
)
