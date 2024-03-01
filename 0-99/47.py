import numpy as np 

N = 10**6

p = [0] * N 

for i in range(2, N):
	if not p[i]:
		for j in range(i, N, i):
			p[j] += 1

for i in range(10, N):
	if p[i-3 : i+1] == [4,4,4,4]:
		print(i-3)
