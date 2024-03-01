import numpy as np
from tqdm import tqdm

def pent(n):
	return (3 * n ** 2 - n) // 2

p = [1]
n = 1
while p[n-1] % int(10**6) != 0:
	p += [0]
	k = 1
	while pent(k) <= n:
		p[n] = (p[n] + (-1) ** (k - 1) * p[n - pent(k)]) % int(10**6)
		k += 1
	k = -1
	while pent(k) <= n:
		p[n] = (p[n] + (-1) ** (k - 1) * p[n - pent(k)]) % int(10**6)
		k -= 1
	p[n] = int(p[n])
	n += 1

print(n - 1, p[n - 1])