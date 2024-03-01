res = 0

fac = [1]
for i in range(1, 10):
	fac += [fac[-1] * i]

for i in range(3, 5 * 10**6):
	facdig = 0
	for char in str(i):
		facdig += fac[int(char)]
	if facdig == i:
		print(i)
		res += i

print(res)