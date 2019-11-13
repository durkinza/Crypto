from crypto import __version__
from .vigenere import vigenere



def load(subparser):
	parser = subparser.add_parser('vigenere', help='vigenère cipher')
	sp = parser.add_subparsers(dest="Action", required=True)
	
	# Encrypt a message
	enc = sp.add_parser("encrypt", help="Encrypt the message")
	enc.add_argument("--key", "-k", help="The alphabet key to use. Default(ABCDEFGHIKLMNOPQRSTUVWXYZ)")
	enc.add_argument("passphrase", help="The edecrytion passphrase")
	enc.add_argument("--message", "-m", help="The Message (default reads from stdin)")

	# Decrypt a message
	dec = sp.add_parser("decrypt", help="Decrypt the message")
	dec.add_argument("--key", "-k", help="The alphabet key to use. Default(ABCDEFGHIKLMNOPQRSTUVWXYZ)")
	dec.add_argument("passphrase", help="The edecrytion passphrase")
	dec.add_argument("--message", "-m", help="The Message (default reads from stdin)")
	
	obj = vigenere(parser)
	return obj
