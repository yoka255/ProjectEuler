import numpy as np
from tqdm import tqdm
import random
from functools import reduce
from typing import Tuple, List

def sieve(N: int):
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


def digsum(n):
	if n < 10:
		return n
	return n % 10 + digsum(n // 10)


def gcd(a, b):
	if b > a:
		return gcd(b, a)
	if b == 0:
		return a
	return gcd(b, a%b)


def euclid(a : int, b : int) -> Tuple[int, int, int]:
	# returns g, x, y such that ax + by = g
	if b == 0:
		return (a, 1, 0)
	if a < b:
		g, x, y = euclid(b, a)
		return (g, y, x)
	g, x, y = euclid(b, a%b)
	return (g, y, x - y * (a // b))


def lcm(a, b):
	return a * b // gcd(a, b)


def inv_mod(a : int, n : int) -> int:
	return euclid(a, n)[1]


def miller_rabin(n: int, k: int = 100) -> bool:
	if n in [2, 3]:
		return True
	if n in [0, 1]:
		return False
	if n % 2 == 0:
		return False
	r, s = 0, n - 1
	while s % 2 == 0:
		r += 1
		s //= 2
	for _ in range(k):
		a = random.randrange(2, n - 1)
		x = pow(a, s, n)
		if x == 1 or x == n - 1:
			continue
		for _ in range(r-1):
			if x ** 2 == 1:
				break
			x = x ** 2
			x %= n
		if x not in [1, n-1]:
			return False
	return True


def is_prime(n: int) -> bool:
	return miller_rabin(n, 100)


def chinese_remainder(m : list, a : list) -> int:
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * inv_mod(p, n_i) * p
    return sum % prod
	
def root(n : int, root : int) -> int:
    l,r = (0,n)
    while l < r:
        m = (l + r) // 2
        if pow(m, root) == n:
            return m
        elif pow(m, root) > n:
            r = m - 1
        else:
            l = m + 1
    return -1