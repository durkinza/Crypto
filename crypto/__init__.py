__version__ = '0.1.0.dev0'
import sys
import argparse
import os
import importlib
from os.path import dirname, basename, isfile, join
import glob
from .ciphers import init_ciphers
from . import utils

def main(passed_args=None):
    parser = argparse.ArgumentParser(description='Perform a cipher')
    sp = parser.add_subparsers()
    # load in all sub-modules
    init_ciphers(sp)
    #group = parser.add_mutually_exclusive_group()
    #group.add_argument("--affine", action="store_true")
    #group.add_argument("--ceaser", action="store_true")
    #parser.add_argument('cipher', help='The Cipher to run', nargs='?', choices=(
    #        'affine',
    #        'caesar',
    #        'rsa'
    #    ))
    parser.add_argument('--verbose', '-v', help="be verbose", action="store_true")
    args = parser.parse_args()
    args_dict = vars(args)
