fac = [1]

N = 101

for n in range(1, N):
	fac += [n * fac[-1]]

count = 0
for n in range(101):
	for d in range(n+1):
		if fac[n] / (fac[d] * fac[n-d]) > 10**6:
			count += 1

print(count)