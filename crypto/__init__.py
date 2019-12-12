__version__ = '0.1.0.dev0'
import sys
import argparse
import os
import importlib
from os.path import dirname, basename, isfile, join
import glob
from .ciphers import ciphers, init_ciphers
from . import utils


def main(passed_args=None):
    parser = argparse.ArgumentParser(description='Perform a cipher')
    sp = parser.add_subparsers(dest="Cipher")
    # load in all sub-modules
    init_ciphers(sp)
    parser.add_argument(
        '--list', '-l', help="list available ciphers", action="store_true")
    try:
        import argcomplete
        argcomplete.autocomplete(parser)
    except Exception as e:
        pass
    args = parser.parse_args()

    # if we want to see available ciphers, print out their help
    if args.list:
        for cipher, obj in ciphers.items():
            c = obj.load_cipher(sp)
            c.print_short_description()
        # exit after printing available ciphers
        exit(0)

    # if we want to do a cipher, run that object
    if args.Cipher:
        c = ciphers[args.Cipher].load_cipher(sp)
        c.run(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopping...")
        exit(2)
