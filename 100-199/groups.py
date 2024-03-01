from itertools import product

def mul(a, b):
	c = [[0,0],[0,0]]
	c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
	c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
	c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
	c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
	for i, j in product([0,1], [0,1]):
		c[i][j] = c[i][j] % 3
	return c

def div(A):
	det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
	res = [[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]]
	for i, j in product([0,1], [0,1]):
		res[i][j] = res[i][j] * det
	return res

def conv(A, B):
	return mul(mul(A, B), mul(div(A), div(B)))


res = []

for a,b,c,d,e,f,g,h in product([0,1,2], repeat = 8):
	if a * d - b * c == 1 == e * h - f * g:
		A = [[a,b],[c,d]]
		B = [[e,f],[g,h]]
		res += [conv(A, B)]

for mat in res:
	if res[0][0] == 1 == res[1][1]:
		print(res)