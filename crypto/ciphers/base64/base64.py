from crypto import __version__
from crypto.cipher import Cipher
import base64
import sys

class b64 (Cipher):
	"""
	This is the base64 module
	"""
	message = b''

	def run(self, args):
		if not args.message:
			self.message = str.encode(sys.stdin.read().strip())
		else:
			self.message = str.encode(args.message)
		if args.Action == 'encrypt':
			print(self.encrypt().decode())
		elif args.Action == 'decrypt':
			print(self.decrypt().decode())
		else:
			print("unknown action: "+args.Action)

	def encrypt(self):
		return base64.b64encode(self.message)
        

	def decrypt(self):
		return base64.b64decode(self.message)
