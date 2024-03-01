import numpy as np

def cyc(n, p):
	rep = str(n)
	k = len(str(n))
	for _ in range(k):
		if not p[int(rep)]:
			return False
		rep = rep[1:] + rep[0]
	return True



N = 10**6
p = np.ones(N)

for i in range(2,N):
	if p[i]:
		for j in range(2*i, N, i):
			p[j] = 0

res = 0

for i in range(2, N):
	if cyc(i, p):
		print(i)
		res += 1

print(res)