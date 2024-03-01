N = 10**6

res = 0

for n in range(N):
	b = "{0:b}".format(n)
	d = str(n)
	if b == b[::-1] and d == d[::-1]:
		print(b, d)
		res += n
print(res)