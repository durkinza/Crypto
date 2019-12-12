from crypto import __version__
from .aes import aes

def load_args(subparser):
    parser = subparser.add_parser('aes', help='AES cipher')
    sp = parser.add_subparsers(dest="Action", required=True)
    info = sp.add_parser("info", help="Give details about the cipher")
	# Encrypt a message
    enc = sp.add_parser("encrypt", help="Encrypt the message")
    enc.add_argument("key", help="The cipher key")
    enc.add_argument("--message", "-m", help="The Message (default reads from stdin)")

	# Decrypt a message
    dec = sp.add_parser("decrypt", help="Decrypt the message")
    dec.add_argument("key", help="The cipher key")
    dec.add_argument("--message", "-m", help="The Message (default reads from stdin)")

def load_cipher(parser):
    obj = aes(parser)
    return obj
