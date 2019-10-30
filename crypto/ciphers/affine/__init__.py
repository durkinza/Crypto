from crypto import __version__
from .affine import affine

affine = affine()

def load(subparser):
    parser = subparser.add_parser('affine', help='Affine cipher')
    parser.add_argument("-a", help="The a value")
    parser.add_argument("-b", help="The b value")
    #affine.setup()
