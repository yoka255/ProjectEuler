res = 0 

for a in range(3, 1001):
	r = 0
	for n in range(1, 2 * a, 2):
		r = max(r, (2 * n * a) % (a ** 2))
	print(a, r)
	res += r

print(res)