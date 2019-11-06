from .. import __version__
from math import gcd as bltin_gcd
from functools import reduce

def find_pq_sets(n, e):
	"""
		returns a set of prime factors for n and e
	"""
	facN = factors(n)[2:]
	pFacN = []
	# get only prime factors
	for i in range(0, len(facN), 2):
		if(isPrime(facN[i]) and isPrime(facN[i+1])):
			pFacN.append([facN[i], facN[i+1]])
    #if(len(pFacN)>1):
    #    print('Multiple factors available')
    #    print(pFacN)
	if(len(pFacN)<=0):
		raise Exception ('No prime factors available for '+str(n)+' and '+str(e))
	return pFacN


def factors(n):
	"""
		returns the factors of n
	"""
	return list(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def isPrime(Number):
	"""
		returns True or False for if a number is prime
	"""
	return 2 in [Number, 2**Number % Number]


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

def xgcd(a,b):
	"""
		Extended Euclidean Algorithum from 
		http://anh.cs.luc.edu/331/notes/xgcd.pdf
		Useful for negative numbers 
	"""
	prevx, x = 1, 0; prevy, y = 0, 1
	while b:
		q = a/b
		x, prevx = prevx - q*x, x
		y, prevy = prevy - q*y, y
		a, b = b, a % b
	return a, prevx, prevy


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
        return bltin_gcd(a, m) == 1

