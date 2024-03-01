import numpy as np
from tqdm import tqdm
import random
from functools import reduce
import sys

def sieve(N):
	print("Sieving")
	arr = np.ones(N)	
	for i in tqdm(range(2, N)):
		if arr[i]:
			for j in range(2*i, N, i):
				arr[j] = 0
	print("Done sieving")
	arr[0] = 0
	arr[1] = 0
	return arr

arr = sieve(10**4)
primes = [x for x in range(10 ** 4) if arr[x]]

def phi(n):
	res = n
	for p in primes:
		if n % p == 0:
			res //= p
			res *= p-1
			while n % p == 0:
				n /= p
	if n != 1:
		res //= n
		res *= n-1
	return res

done = False
def hype_exp(a, k, mod):
	global done
	if not done:
		print(mod)
	if mod == 1:
		done = True
	if k == 1:
		return a % mod
	return pow(a, hype_exp(a, k-1,phi(mod)) % phi(mod), mod)

if __name__ == "__main__":
	sys.setrecursionlimit(10000)
	print(hype_exp(1777, 1855, 10 ** 8))