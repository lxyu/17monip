#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

dev_requires = [
    "flake8>=2.2.0",
    "pytest>=2.6.0",
]

setup(
    name="17MonIP",
    version="0.2.3",
    description="IP search based on 17mon.cn, the best IP database for China.",
    author="Lx Yu",
    author_email="github@lxyu.net",
    packages=["IP", ],
    package_data={'IP': ['17monipdb.dat'], },
    entry_points={"console_scripts": ["iploc = IP.cmd:main", ]},
    url="http://lxyu.github.io/17monip/",
    license="MIT",
    long_description=open("README.rst").read(),
    extras_require={
        "dev": dev_requires,
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
