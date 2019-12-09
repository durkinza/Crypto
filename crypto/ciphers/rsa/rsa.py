from crypto import __version__
import sys
import random
from crypto.cipher import Cipher
from crypto.utils import find_pq_sets, factors, isPrime, gcd, modinv
class rsa (Cipher):
	"""
		This is the RSA module
	"""

	def print_short_description(self):
		print("rsa:\n\tRSA Cryptosystem\n\tAn asymetric cipher that relys on the difficulty of finding the prime factors of a number.\n")

	def print_long_description(self):
		print("Rivest–Shamir–Adleman (RSA):\n\tThis asymetric cipher starts by finding 2 prime numbers p and q.\n\tn will be public. n = p * q\n\tThe phi(n) will be calculated as phi(n) = (p - 1) * (q - 1) This will be used later.\n\tThe public key e will be selected randomly as a number between 1 and phi(n), such that phi(n) and e have no common factors.\n\tThe secret key d will be calculated as the modular inverse of phi(n) and e. e * d = 1 mod phi(n).\n\tFinally the public and private keys are given as Private(n,d) and Public(n,e)\n\n\tEncrypting a message M to ciphertext C is done as \n\tM^e mod n = C\n\n\tDecrypting a ciphertext C to message M is done as\n\tC^d mod n = C")

	def run (self, args):
		if args.Action == 'info':
			return self.print_long_description()

		if args.Action == 'encrypt':
			if not args.message:
				self.m = sys.stdin.read()
			else:
				self.m = args.message
			self.n = args.n
			self.e = args.e 
			try:
				print(self.encrypt())
			except ValueError:
				print("Input must be integers")
			except Exception as e:
				print( "Error: %s" % str(e) )
		
		elif args.Action == 'decrypt':
			if not args.message:
				self.m = sys.stdin.read()
			else:
				self.m = args.message
			self.d = args.d
			self.n = args.n 

			try: 
				print(self.decrypt())
			except ValueError:
				print("Input must be integers")
			except Exception as e:
				print( "Error: %s" % str(e) )
		elif args.Action == 'make':
			self.p = args.p
			self.q = args.q
			self.e = args.e or None
			try:
				print(self.make())
			except Exception as e:
				print( "Error: %s" % str(e) )

		elif args.Action == 'break':
			self.e = args.e
			self.n = args.n
			try:
				print(self.reverse())
			except Exception as e:
				print( "Error: %s" % str(e) )
		else:
			print("unknown action: "+args.Action)

	def encrypt (self):
		res = ""
		for i in self.m:
			c = (ord(i) ** self.e) % self.n
			res += str(int(c))+' '
		return res

	def decrypt (self):
		res = ""
		for j in self.m.strip().split(' '):
			c = (int(j) ** self.d) % self.n
			#print( chr(int(c)))
			res += chr(c)
		return res.strip()

	def reverse (self):
		if not self.e or not self.n:
			print("-n and -e are required")
		sets = find_pq_sets(self.n)
		for i in range(len(sets)):
			p = sets[i][0]
			q = sets[i][1]
			print('Trying: p='+str(p)+' q='+str(q))
			phiN = (p - 1)*(q - 1)
			print('     phiN: '+str(phiN))
			d = modinv(self.e, phiN)
			print('        d: '+str(d))
			print('        e: '+str(self.e))
			print('        n: '+str(self.n))
		return ('Found: p='+str(p)+' q='+str(q))

	def make (self):
		if not isPrime(self.p):
			raise Exception ("p must be prime")
		if not isPrime(self.q):
			raise Exception ("q must be prime")
		d = None
		while d == None:
			n = self.p*self.q
			phiN = (self.p - 1)*(self.q - 1)
			facPhiN = factors(phiN)
			if not self.e:
				self.e = random.randrange(2, phiN)
				while d == None:
					while self.e in facPhiN:
						self.e = random.randrange(2, phiN)
					try:
						d = modinv(self.e, phiN)
					except:
						self.e = random.randrange(2, phiN)
			else:
				d = modinv(self.e, phiN)
		return ("Private d: %s\nPublic  e: %s\nPublic  n: %s" % (d, self.e, n))
