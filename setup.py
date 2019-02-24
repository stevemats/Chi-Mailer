#!/usr/bin/env python3
# encoding: utf-8

import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name="chi_mailer",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    author="Stevemats & fkinaro",
    author_email="stevematindi@gmail.com",
    license='BSD License',
    description="python bulk/mass mailer package",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/stevemats/chi_mailer",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
