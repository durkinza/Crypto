from crypto import __version__
from .cupid import cupid


def load_args(subparser):
    parser = subparser.add_parser('cupid', help='Cupid cipher')
    sp = parser.add_subparsers(dest="Action", required=True)
    info = sp.add_parser("info", help="Give details about the cipher")

    # Encrypt a message
    enc = sp.add_parser("encrypt", help="Encrypt the message")
    enc.add_argument("--message", "-m",
                     help="The Message (default reads from stdin)")

    # Decrypt a message
    dec = sp.add_parser("decrypt", help="Decrypt the message")
    dec.add_argument("order", type=int, help="The correct order of columns separated by columns.")
    dec.add_argument("--message", "-m",
                     help="The Message (default reads from stdin)")

    # Break a message (by brute force
    # brk = sp.add_parser("break", help="break the message")
    # brk.add_argument("--message", "-m",
    #                 help="The Message (default reads from stdin)")


def load_cipher(parser):
    obj = cupid(parser)
    return obj
