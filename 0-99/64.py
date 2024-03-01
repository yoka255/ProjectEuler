from math import sqrt
from tqdm import tqdm

def gcd(a, b):
	if b > a:
		return gcd(b, a)
	if b == 0:
		return a
	return gcd(b, a%b)

cnt = 0

def calcexp(k):
	n = int(k**2)
	a = [int(k)]
	x = [(1, 0, 1)]
	while 1:
		c, b, y = x[-1]
		x += [(y*c, y * (a[-1] * y - b), c * c * n - (a[-1] * y - b) ** 2)]
		c, b, y = x[-1]
		g = gcd(c, gcd(b, y))
		x[-1] = (c//g, b//g, y//g)
		a += [int((x[-1][0] * k + x[-1][1]) / x[-1][2])]
		if len(x) > 2 and x[-1] == x[1]:
			break
	return a

# for n in range(2, 10**4 + 1):
# 	# print(n)
# 	if int(sqrt(n)) * int(sqrt(n)) != n:
# 		a = calcexp(sqrt(n))
# 		if len(a) % 2:
# 			cnt += 1
# print(cnt)

print(calcexp(41 ** 0.5))