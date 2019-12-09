from .. import __version__
from math import gcd as bltin_gcd
from functools import reduce

def find_pq_sets(n):
	"""
		returns a set of prime factors for n
	"""
	facN = factors(n)[2:]
	pFacN = []
	# get only prime factors
	for i in range(0, len(facN), 2):
		if(isPrime(facN[i]) and isPrime(facN[i+1])):
			pFacN.append([facN[i], facN[i+1]])
	if(len(pFacN)<=0):
		raise Exception ('No prime factors available for '+str(n))
	return pFacN


def factors(n):
	"""
		returns the factors of n
	"""
	return list(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def isPrime(Number):
	"""
		returns True or False for if a number is prime
		This uses Fermat's Primailty test for checking if a number is a candidate prime. 
		Note, this algorithum and may result in false positives .
	"""
	return 1 in [Number, 2**(Number-1) % Number]


def phi(n):
	"""
		golden = (1 + 5 ** 0.5) / 2
	"""
	x = 0
	for i in range(n):
		if (gcd(n, i) == 1):
			x = x+1
	return x


def egcd(a, b):
	"""
		Extended Euclidean Algorithum
	"""
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def gcd(x, y):
	"""
		This function implements the Euclidian algorithm
		to find gcd of two numbers
	"""
	while(y):
		x, y = y, x % y
	return x


def coprime(a, m):
	"""
    	Indicates whether two numbers are coprimes (relatively prime)
	"""
	x = egcd(a, m)[0]
	# indicates relatively prime
	if x == 1:
		return True
		
	# indicates not relatively prime
	else:
		return False


