import numpy as np 

N = 30000
p = np.zeros(N)
for i in range(1,N):
	for j in range(2*i, N, i):
		p[j] += i

ab = []
for i in range(N):
	if i < p[i]:
		ab += [i]

pos = set()
for a in ab:
	for b in ab:
		pos.add(a + b)
res = 0
for i in range(N):
	if i not in pos:
		print(i)
		res += i
print(res)