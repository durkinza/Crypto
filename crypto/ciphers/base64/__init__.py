from crypto import __version__
from .base64 import b64

def load(subparser):
    parser = subparser.add_parser('base64', help='Base64 Encoding')
    sp = parser.add_subparsers(dest="Action", required=True)
	
	# Encoding
    enc = sp.add_parser("encrypt", help="Encodethe message")
    enc.add_argument("--message", "-m", help="The Message")

	# Decoding
    dec = sp.add_parser("decrypt", help="Decode the message")
    dec.add_argument("--message", "-m", help="The Message")

    obj = b64(parser)
    return obj
