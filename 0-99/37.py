from euler import *
import numpy as np

def trunc(n, p):
	tmp = str(n)
	while len(tmp):
		if not p[int(tmp)]:
			return False
		tmp = tmp[1:]
	tmp = str(n)
	while len(tmp):
		if not p[int(tmp)]:
			return False
		tmp = tmp[:-1]
	return True

N = 10**6
p = sieve(N)

res = 0

for i in range(10, N):
	if trunc(i, p):
		res += i
		print(i)
print(res)