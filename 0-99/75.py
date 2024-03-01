from euler import *

L = 15 * 10**5

arr = np.zeros(L+1)
for u in range(1, int(L**0.5)):
	for v in range(1, u):
		if gcd(u, v) == 1 and (v % 2 == 0 or u % 2 == 0):
			a, b, c = u**2 - v ** 2, 2 * u * v, u**2 + v**2
			s = a + b + c 
			for x in range(s, L+1, s):
				arr[x] += 1

print(len([x for x in arr if x == 1]))