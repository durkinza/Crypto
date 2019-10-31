from crypto import __version__
from .affine import affine


def load(subparser):
    parser = subparser.add_parser('affine', help='Affine cipher')
    sp = parser.add_subparsers(dest="Action", required=True)
    enc = sp.add_parser("encrypt", help="Encrypt the message")
    dec = sp.add_parser("decrypt", help="Decrypt the message")
    enc.add_argument("--a", "-a", type=int, help="The size of the sift", required=True)
    enc.add_argument("--b", "-b", type=int, help="The size of the sift", required=True)
    enc.add_argument("--message", "-m", help="The Message", required=True)

    dec.add_argument("--a", "-a", type=int, help="The size of the sift", required=True)
    dec.add_argument("--b", "-b", type=int, help="The size of the sift", required=True)
    dec.add_argument("--message", "-m", help="The Message", required=True)
    obj = affine(parser)
    return obj
