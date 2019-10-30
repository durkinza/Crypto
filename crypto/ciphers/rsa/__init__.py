from crypto import __version__
from .rsa import rsa

rsa = rsa()

def load(subparser):
    parser = subparser.add_parser('rsa', help='RSA cipher')
    parser.add_argument("-a", help="The a value")
    parser.add_argument("--message", "-m", help="The Message")
    #rsa.setup()
