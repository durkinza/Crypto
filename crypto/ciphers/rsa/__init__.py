from crypto import __version__
from .rsa import rsa

def load_args(subparser):
    parser = subparser.add_parser('rsa', help='RSA cipher')
    sp = parser.add_subparsers(dest="Action", required=True)
    info = sp.add_parser("info", help="Give details about the cipher")

	# Encrypt a message
    enc = sp.add_parser("encrypt", help="Encrypt the message")
    enc.add_argument("n", type=int, help="The public key n")
    enc.add_argument("e", type=int, help="The public key e")
    enc.add_argument("--message", "-m", help="The Message (default reads from stdin)")

	# Decrypt a message
    dec = sp.add_parser("decrypt", help="Decrypt the message")
    dec.add_argument("n", type=int, help="The public key n")
    dec.add_argument("d", type=int, help="The private key d")
    dec.add_argument("--message", "-m", help="The Message (default reads from stdin)")

    # Make a new RSA key
    mk = sp.add_parser("make", help="Make a new small RSA key")
    mk.add_argument("p", type=int, help="The first of 2 primes" )
    mk.add_argument("q", type=int, help="The second of 2 primes")
    mk.add_argument("-e", type=int, help="And integer between 1 and phi(p*q)")

	# Breaking an RSA key
    brk = sp.add_parser("break", help="Break a small RSA key")
    brk.add_argument("n", type=int, help="The public key n")
    brk.add_argument("e", type=int, help="The public key e")

def load_cipher(parser):
    obj = rsa(parser)
    return obj
