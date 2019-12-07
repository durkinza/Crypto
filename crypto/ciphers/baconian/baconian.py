from crypto import __version__
from crypto.cipher import Cipher
import sys


class baconian (Cipher):
	"""
	This is the baconian module
	Code is mostly based off of work by Tyler Akins (http://rumkin.com)
	"""
	message = ""
	Ualph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	def print_short_description(self):
		print("baconian:\n\tBaconian Cipher\n\tThis cipher converts each character to a binary representation, often represented in A's and B's.\n")

	def print_long_description(self):
		print("Baconian Cipher:\n\tOriginally desgined by Francis Bacon, this cipher uses two alternating values to encode a messsage.\n\tEach character is give a binary representation (a=00000, b=00001, ..., z=10111)\n\t\tIn the case of this version of the cipher, the 0's are returned as A and 1's are returned as B.\n\tThis cipher is best used when hidden in plain sight. \n\t\tex. A message is encoded into a article using two font types. A's being font 1, B's being font 2.")

	def run(self, args):
		if args.Action == 'info':
			return self.print_long_description()
		if not args.message:
			self.m = sys.stdin.read().strip()
		else:
			self.m = args.message
		if hasattr(args, 'notDistinct') and args.notDistinct:
			self.notDistinct = True
			self.Ualph = 'ABCDEFGHIKLMNOPQRSTUWXYZ'
			self.m = self.m.replace("j", "i").replace("J", "J").replace("v", "u").replace("V", "U")
		else:
			self.notDistinct = False
		if args.Action == 'encrypt':
			print(self.encrypt())
		elif args.Action == 'decrypt':
			print(self.decrypt())
		elif args.Action == 'swap':
			print(self.swapBaconian())
		else:
			print("unknown action: "+args.Action)

	def encrypt(self):	
		return self.encode()

	def decrypt(self):
		return self.decode()

	def swapBaconian(self):
		s = self.m
		o = ''

		for x in s :
			c = x
			if (c == '0'):
				c = '1'
			elif (c == '1'):
				c = '0'
			elif (c == 'a'):
				c = 'b'
			elif (c == 'b'):
				c = 'a'
			elif (c == 'A'):
				c = 'B'
			elif (c == 'B'):
				c = 'A'
			o += c
		return o

	def encode(self):
		spaceAdded = True
		out = ''
		s = self.m.upper()
		for x in s:
			if x not in self.Ualph:
				idx = -1
			else:	
				idx = self.Ualph.index(x)
			if idx >= 0:
				out += 'B' if (idx & 0x10) else 'A'
				out += 'B' if (idx & 0x08) else 'A'
				out += 'B' if (idx & 0x04) else 'A'
				out += 'B' if (idx & 0x02) else 'A'
				out += 'B' if (idx & 0x01) else 'A'
				spaceAdded = False
			else:
				if not spaceAdded:
					out += ' ';
					spaceAdded = True
		return out				

	def decode(self):
		out = '';
		buf = '';
		addSpace = False;

		s = self.m.upper()
		s = s.replace('01', 'AB')

		for c in s:
			if c == 'A' or c == 'B':
				buf += c
			elif (buf == ''):
				addSpace = True
			
			if len(buf) == 5:
				idx = 0

				idx += 0 if (buf[0] == 'A') else 16
				idx += 0 if (buf[1] == 'A') else 8
				idx += 0 if (buf[2] == 'A') else 4
				idx += 0 if (buf[3] == 'A') else 2
				idx += 0 if (buf[4] == 'A') else 1

				buf = ''

				if (addSpace):
					out += ' '
					addSpace = False
				out += self.Ualph[idx]
		return out

