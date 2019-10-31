from crypto import __version__
from .caesar import caesar



def load(subparser):
    parser = subparser.add_parser('caesar', help='Caesar cipher')
    sp = parser.add_subparsers(dest="Action", required=True)
    enc = sp.add_parser("encrypt", help="Encrypt the message")
    dec = sp.add_parser("decrypt", help="Decrypt the message")
    enc.add_argument("--shift", "-n", type=int, help="The size of the sift", required=True)
    enc.add_argument("--message", "-m", help="The Message", required=True)
    dec.add_argument("--shift", "-n", type=int, help="The size of the sift", required=True)
    dec.add_argument("--message", "-m", help="The Message", required=True)
    obj = caesar(parser)
    return obj
