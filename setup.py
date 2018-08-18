#!/usr/bin/python


import os
from setuptools import setup


def readfile(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), 'r') as f:
        return f.read()


setup(
    name='trampoline',
    version='0.1.2',
    description='Simple and tiny yield-based trampoline implementation.',
    long_description=readfile('README.rst'),
    license='MIT',
    author_email='code.danielk@gmail.com',
    url='https://gitlab.com/ferreum/trampoline',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='trampoline recursion tail call',
    packages=['trampoline'],
)


# vim:set sw=4 ts=8 sts=4 et:
