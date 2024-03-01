def mul(a, b):
	c = [[0,0],[0,0]]
	c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
	c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
	c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
	c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
	return c


def fibo(p):
	res = [[1,0],[0,1]]
	a = [[1,1], [1,0]]
	while p > 0:
		if p % 2 == 1:
			res = mul(res, a)
		a = mul(a, a)
		p //= 2
	return res[1][0]

curr = 1
last = 0
n = 1
while 1:
	if n % (10 ** 5) == 0:
		print(n)
	s = str(curr)
	if sorted(s[-9:]) == [str(x) for x in range(1,10)]:
		num = fibo(n)
		s = str(num)
		if sorted(s[:9]) == [str(x) for x in range(1,10)]:
			print(n)
			break

	curr, last = curr + last, curr
	curr, last = curr % (10**9), last % (10 ** 9)
	n += 1
