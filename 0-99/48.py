MOD = 10**10

res = 0

for n in range(1, 1001):
	res = (res + n ** n) % MOD
print(res)