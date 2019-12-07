from crypto import __version__
from .baconian import baconian

def load_args(subparser):
    parser = subparser.add_parser('baconian', help='Baconian cipher')
    sp = parser.add_subparsers(dest="Action", required=True)
    info = sp.add_parser("info", help="Give details about the cipher")

	# Encrypt the message
    enc = sp.add_parser("encrypt", help="Encrypt the message")
    enc.add_argument("--notDistinct", "-d", action="store_true", help="Combine characters vu and ij")
    enc.add_argument("--message", "-m", help="The Message")

	# Decrypt the message
    dec = sp.add_parser("decrypt", help="Decrypt the message")
    dec.add_argument("--notDistinct", "-d", action="store_true", help="Combine characters vu and ij")
    dec.add_argument("--message", "-m", help="The Message")


	# Swap
    swp = sp.add_parser("swap", help="Swap A and B")
    swp.add_argument("--message", "-m", help="The Message")

def load_cipher(parser):
    obj = baconian(parser)
    return obj
