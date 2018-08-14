#!/usr/bin/python


from setuptools import setup


setup(
    name='trampoline',
    version='0.1.0',
    description='Simple and tiny yield-based trampoline implementation.',
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
