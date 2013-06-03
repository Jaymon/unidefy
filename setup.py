#!/usr/bin/env python
# http://docs.python.org/distutils/setupscript.html
# http://docs.python.org/2/distutils/examples.html

import ast
import sys
from setuptools import setup

name = 'unidefy'
version = '0.2'

setup(
    name=name,
    version=version,
    description='python unicode -> ascii substitutions for known characters',
    author='Jay Marcyes',
    author_email='jay@marcyes.com',
    url='http://github.com/Jaymon/{}'.format(name),
    py_modules=[
        name,
    ],
    license="MIT",
    zip_safe=True,
    classifiers=[
        'Development Status :: {}'.format(version),
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Topic :: Debug',
        ],
    test_suite = "test_{}".format(name),
)
