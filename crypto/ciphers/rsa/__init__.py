from crypto import __version__
from .rsa import rsa

def load(subparser):
    parser = subparser.add_parser('rsa', help='RSA cipher')
    sp = parser.add_subparsers(dest="Action", required=True)
    enc = sp.add_parser("encrypt", help="Encrypt the message")
    dec = sp.add_parser("decrypt", help="Decrypt the message")
    brk = sp.add_parser("break", help="Find p and q from d and e")

    enc.add_argument("--n", "-e", type=int, help="The size of the sift", required=True)
    enc.add_argument("--d", "-d", type=int, help="The size of the sift", required=True)
    enc.add_argument("--message", "-m", help="The Message", required=True)

    dec.add_argument("--a", "-a", type=int, help="The size of the sift", required=True)
    dec.add_argument("--b", "-b", type=int, help="The size of the sift", required=True)
    dec.add_argument("--message", "-m", help="The Message", required=True)

    obj = rsa(parser)
    return obj
