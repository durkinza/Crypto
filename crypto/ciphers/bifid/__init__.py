from crypto import __version__
from .bifid import bifid



def load(subparser):
	parser = subparser.add_parser('bifid', help='Bifid cipher')
	sp = parser.add_subparsers(dest="Action", required=True)

	# Encrypt 
	enc = sp.add_parser("encrypt", help="Encrypt the message")
	enc.add_argument("--key", "-k", help="The alphabet key to use. Default(ABCDEFGHIKLMNOPQRSTUVWXYZ)")
	enc.add_argument("--message", "-m", help="The Message")
	
	# Decrypt
	dec = sp.add_parser("decrypt", help="Decrypt the message")
	dec.add_argument("--key", "-k", help="The alphabet key to use. Default(ABCDEFGHIKLMNOPQRSTUVWXYZ)")
	dec.add_argument("--message", "-m", help="The Message")

	obj = bifid(parser)
	return obj
