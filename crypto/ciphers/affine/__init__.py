from crypto import __version__
from .affine import affine


def load_args(subparser):
    parser = subparser.add_parser('affine', help='Affine cipher')
    sp = parser.add_subparsers(dest="Action", required=True)
    info = sp.add_parser("info", help="Give details about the cipher")

        # Encrypt the message
    enc = sp.add_parser("encrypt", help="Encrypt the message")    
    enc.add_argument("--a", "-a", type=int, help="The first half of the key (a,b). a should be relatively prime to 26", required=True)
    enc.add_argument("--b", "-b", type=int, help="The second half of the key (a,b)", required=True)
    enc.add_argument("--message", "-m", help="The Message")

        # Decrypt the message
    dec = sp.add_parser("decrypt", help="Decrypt the message")
    dec.add_argument("--a", "-a", type=int, help="The first half of the key (a,b). a should be relatively prime to 26", required=True)
    dec.add_argument("--b", "-b", type=int, help="The second half of the key (a,b)", required=True)
    dec.add_argument("--message", "-m", help="The Message")

def load_cipher(parser):
    obj = affine(parser)
    return obj
