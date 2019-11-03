from crypto import __version__
from .baconian import baconian



def load(subparser):
    parser = subparser.add_parser('baconian', help='Baconian cipher')
    sp = parser.add_subparsers(dest="Action", required=True)

	# Encrypt the message
    enc = sp.add_parser("encrypt", help="Encrypt the message")
    enc.add_argument("--distinct", "-d", action="store_true", help="Use a distinct code for each value")
    enc.add_argument("--message", "-m", help="The Message")

	# Decrypt the message
    dec = sp.add_parser("decrypt", help="Decrypt the message")
    dec.add_argument("--distinct", "-d", action="store_true", help="Use a distinct code for each value")
    dec.add_argument("--message", "-m", help="The Message")

    obj = baconian(parser)
    return obj
