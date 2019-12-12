from crypto import __version__
from .caesar import caesar


def load_args(subparser):
    parser = subparser.add_parser('caesar', help='Caesar cipher')
    sp = parser.add_subparsers(dest="Action", required=True)
    info = sp.add_parser("info", help="Give details about the cipher")

    # Encrypt a message
    enc = sp.add_parser("encrypt", help="Encrypt the message")
    enc.add_argument("shift", type=int, help="The size of the sift")
    enc.add_argument("--message", "-m",
                     help="The Message (default reads from stdin)")

    # Decrypt a message
    dec = sp.add_parser("decrypt", help="Decrypt the message")
    dec.add_argument("shift", type=int, help="The size of the sift")
    dec.add_argument("--message", "-m",
                     help="The Message (default reads from stdin)")

    # Break a message (by brute force
    brk = sp.add_parser("break", help="break the message")
    brk.add_argument("--message", "-m",
                     help="The Message (default reads from stdin)")


def load_cipher(parser):
    obj = caesar(parser)
    return obj
