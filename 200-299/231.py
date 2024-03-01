import numpy as np
from tqdm import tqdm

def psum(x, primes):
	res = 0
	for pr in primes:
		mul = pr
		while mul <= x:
			res += (x//mul)*pr
			mul *= pr
	return res

def calc(x, k, primes):
	return psum(x, primes) - psum(k, primes) - psum(x-k, primes)

n = 20 * (10**6)

p = np.ones(n + 1)
p[0] = 0
p[1] = 0
primes = []

for k in tqdm(range(2, n+1)):
	if p[k]:
		for j in range(2*k, n+1, k):
			p[j] = 0
		primes += [k]

print(calc(n, 15 * (10**6), primes))

