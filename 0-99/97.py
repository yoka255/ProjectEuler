def pow(a, b, mod):
	cur = a
	res = 1
	while b:
		if b & 1:
			res = (res * cur) % mod
		cur = (cur * cur) % mod
		b //= 2
	return res

mod = 10**10

print((28433 * pow(2, 7830457, mod) + 1) % mod) 