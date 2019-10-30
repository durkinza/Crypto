# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from crypto import __version__

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='crypto-cli',
    version=__version__,
    description='A command line crypto tool',
    long_description=readme,
    author='Zane Durkin, Brandon Foss',
    author_email='zane@neverlanctf.org, foss6583@vandals.uidaho.edu',
    url='https://github.com/durkinza/crypto',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
