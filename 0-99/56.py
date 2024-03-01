from euler import *

res = 0

for a in range(1, 100):
	for b in range(1, 100):
		res = max(res, digsum(a**b))

print(res)