import numpy as np
from tqdm import tqdm

N = 10*10**6
p = np.ones(N)

for i in range(2, N):
	if p[i]:
		for j in range(2*i, N, i):
			p[j] = 0

bestres = 0

for a in range(-999, 1000):
	for b in range(-1000, 1001):
		n = 0
		while 1:
			if not p[n * n + a * n + b]:
				break
			n += 1
		if n > bestres:
			print(a, b, n)
			print(a*b)
			bestres = n