def binom(n, k):
	res = 1
	for r in range(n, n-k, -1):
		res *= r
	for r in range(1,k+1):
		res = res // r
	return res

n = 100
print(binom(10 + n, 10) + binom(9 + n, 9) - 10 * n - 2)