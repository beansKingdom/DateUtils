from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="DateUtils",
    version="0.1",
    author="Hly",
    author_email="hlyaction@gmail.com",
    description="A Python library for date compute.",
    long_description=open("README.rst").read(),
    license="MIT",
    url="https://github.com/beansKingdom/DateUtils",
    packages=['DateUtils'],
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Multimedia :: Video',
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=True,
)
