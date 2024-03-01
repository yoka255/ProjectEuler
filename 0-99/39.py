import numpy as np

N = 1000
p = np.zeros(N+1)

for a in range(1, 1000):
	for b in range(a, 1000):
		c = (a**2 + b**2)**0.5
		if int(c) == c and a+b+c <= N:
			p[a+b+int(c)]+=1

best = 0
for i in range(N+1):
	if p[i] > p[best]:
		print(i, p[i])
		best = i

print(best)