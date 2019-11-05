from crypto import __version__
from crypto.cipher import Cipher
import sys
import math

class bifid (Cipher):
	"""
	This is the bifid module
	Largely based off of the work by Tyler Akins (http://rumkin.com)
	"""
	key = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
	table = [['a','a','a','a','a'],['a','a','a','a','a'],['a','a','a','a','a'],['a','a','a','a','a'],['a','a','a','a','a']]
	message = ""

	def run(self, args):
		if args.key:
			if len(args.key) != 25:
				raise Exception("Key must be 25 characters long")
			self.key = args.key
		self.key_to_table(self.key)
		
		if not args.message:
			self.m = sys.stdin.read().strip()
		else:
			self.m = args.message
		if args.Action == 'encrypt':
			print(self.encrypt())
		elif args.Action == 'decrypt':
			print(self.decrypt())

		else:
			print("unknown action: "+args.Action)

	def findInList(self, List, item):
		try:
			return List.index(item)
		except ValueError:
			return -1




	def col_row(self, needle):
		"""
			returns the column and row of a needle in the haystack
		"""
		for col_i, column in enumerate(self.table):
			for row_i, row in enumerate(column):
				if self.table[col_i][row_i] == needle:
					return col_i, row_i
		return None, None

	def key_to_table(self, key):
		"""
			Takes a key and builds a table for it
		"""
		row = 0
		col = 0
		for c in key:
			self.table[row][col] = c
			col += 1
			if col % 5 == 0:
				col = 0
				row += 1

	def int_at(self, string, index):
		try:
			return int(string[index])
		except:
			return 0

	def mangle(self, encdec, message):
		line1 = ''
		line2 = ''
		for x in range(len(message)):
			pos = self.findInList(self.key, message[x].upper())
			row = math.floor(pos / 5)
			col = pos % 5

			line1 += str(row)
			if encdec > 0:
				line2 += str(col)
			else:
				line1 += str(col)
		line1 += line2
		if encdec < 0:
			line2 = ''
			for x in range(math.floor(len(line1) / 2)):
				line2 += line1[x]
				line2 += line1[math.floor(len(line1)/2) + x]
			line1 = line2
		chars = ''
		i = 0
		for x in range(len(line1)):
			i += 1
			if i %2 == 0:
				continue
			chars += self.key[ self.int_at(line1, x) * 5 + self.int_at(line1, x+1) * 1]
		return chars

	def encrypt(self):
		return self.mangle(1, self.m)

	def decrypt(self):
		return self.mangle(-1, self.m)
