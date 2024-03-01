import numpy as np

def poly(n):
	ret = 0
	for b in range(11):
		ret += (-n) ** b 
	return ret	

def calcpoly(n, a):
	ret = 0
	for b in range(len(a)):
		ret += a[b] * n ** b
	return ret

# a_0 + 1 * a_1 + 1^2 * a_2 = 1
# a_0 + 2 * a_1 + 2^2 * a_2 = 8
# a_0 + 3 * a_1 + 3^2 * a_2 = 27

res = 0

b = np.zeros(10).astype(np.longlong)
for i in range(10):
	b[i] = poly(i+1)

print(b)

for exp in range(1, 11):
	M = np.zeros((exp, exp)).astype(np.longlong)
	for i in range(exp):
		for j in range(exp):
			M[i][j] = (i + 1) ** j

	x = np.linalg.solve(M, b[:exp])
	print(x)
	for n in range(1, 30):
		if abs(calcpoly(n, x) - poly(n)) >= 10**-3:
			print(exp,n)
			print(calcpoly(n, x), poly(n))
			res += calcpoly(n, x)
			break

print(res)

