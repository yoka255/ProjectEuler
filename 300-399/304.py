from sage.all import *
from tqdm import tqdm

def next_prime(n:int) -> int:
	k: int = n+1
	while True:
		if is_prime(k):
			return k
		k += 1

def mul(a, b, m):
	c = [[0,0],[0,0]]
	c[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % m
	c[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % m
	c[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % m
	c[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % m
	return c


def fibo(p, m):
	res = [[1,0],[0,1]]
	a = [[1,1], [1,0]]
	while p > 0:
		if p % 2 == 1:
			res = mul(res, a, m)
		a = mul(a, a, m)
		p //= 2
	return res[1][0]

if __name__ == "__main__":
	N = 100_000
	mod = 1234567891011
	res = 0
	a = next_prime(10 ** 14)
	for _ in tqdm(range(N)):
		res += fibo(a, mod)
		a = next_prime(a)
		res %= mod
	print(res)