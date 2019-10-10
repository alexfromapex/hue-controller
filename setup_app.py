#!/usr/bin/env python3

from setuptools import setup

APP = ['hue-controller/main.py']
DATA_FILES = []
OPTIONS = {}

setup(
    app=APP,
    name="Hue Controller",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
