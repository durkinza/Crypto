from crypto import __version__
from .atbash import atbash


def load_args(subparser):
    parser = subparser.add_parser('atbash', help='Atbash cipher')
    sp = parser.add_subparsers(dest="Action", required=True)
    info = sp.add_parser("info", help="Give details about the cipher")

    # Encrypt the message
    enc = sp.add_parser("encrypt", help="Encrypt the message")
    enc.add_argument("--message", "-m", help="The Message")

    # Decrypt the message
    dec = sp.add_parser("decrypt", help="Decrypt the message")
    dec.add_argument("--message", "-m", help="The Message")


def load_cipher(parser):
    obj = atbash(parser)
    return obj
