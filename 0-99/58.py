from euler import *

def prime(n):
	if not n % 2:
		return 0
	k = 3
	while k * k <= n:
		if not n % k:
			return 0
		k += 2
	return 1

N = 10**7

a = 0
b = 1
n = 3
while 1:
	for i in range(4):
		a += prime(n * n - (n-1) * i)
	b += 4
	print(n, a/b)
	if a/b <= 0.1:
		print(n)
		break
	n += 2
