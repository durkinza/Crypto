from crypto import __version__
from .caesar import caesar

caesar = caesar()

def load(subparser):
    parser = subparser.add_parser('caesar', help='Caesar cipher')
    parser.add_argument("-a", help="The a value")
    parser.add_argument("--message", "-m", help="The Message")
    #caesar.setup()
