#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='hue-controller',
    author='Alex Watson',
    author_email='alexfromapex at gmail dot com',
    version='0.1dev',
    description='Control Phillips Hue lights with WX GUI',
    packages=['wx','phue'],
    license='MIT',
    long_description=open('README.md').read(),
    url = 'https://github.com/alexfromapex/hue-controller'
)
