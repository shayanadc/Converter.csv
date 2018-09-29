#!/usr/bin/env python3
"""Factorial project"""
from setuptools import find_packages, setup

with open("README.rst", "r") as fobj:
    long_description = fobj.read()

setup(name = 'csvConvertor',
    version = '0.1',
    description = "convert csv file to json",
    long_description = long_description,
    platforms = ["Linux"],
    author="shayanadc",
    author_email="shayanadc@gmail.com",
    url="https://github.com/shayanadc",
    license = "MIT",
    packages=find_packages()
)