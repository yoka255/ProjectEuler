from math import sqrt, floor
from tqdm import tqdm
from euler import gcd

def calcfrac(arr):
	n = len(arr)
	a, b = arr[n-1], 1
	for i in range(n-2, -1, -1):
		a, b = b, a
		a += b * arr[i]
		g = gcd(a, b)
		a, b = a//g, b//g
	return a, b


res = 1
sol = 1
N = 1000

for n in range(2, N+1):
	if int(sqrt(n)) * int(sqrt(n)) != n:
		a = [int(sqrt(n))]
		x = [(1, 0, 1)]
		k = sqrt(n)
		while 1:
			c, b, y = x[-1]
			x += [(y*c, y * (a[-1] * y - b), c * c * n - (a[-1] * y - b) ** 2)]
			c, b, y = x[-1]
			g = gcd(c, gcd(b, y))
			x[-1] = (c//g, b//g, y//g)
			a += [int((x[-1][0] * k + x[-1][1]) / x[-1][2])]
			if len(x) > 2 and x[-1] == x[1]:
				break

		tmp, tmpb = calcfrac(a[:-2])
		if len(a) == 3:
			tmp, tmpb = calcfrac(a[:-1])
		if tmp ** 2 - n * tmpb**2 == -1:
			tmp, tmpb = tmp ** 2 + n * tmpb ** 2, 2 * tmp * tmpb
		print(n, tmp, a)
		if tmp > sol:
			res = n
			sol = tmp

print(res)


