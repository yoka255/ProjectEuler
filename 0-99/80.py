from decimal import *

getcontext().prec = 100
getcontext().rounding = ROUND_DOWN
res = 0
for n in range(2, 100):
	if n ** 0.5 != int(n ** 0.5):
		s = str(Decimal(n) ** Decimal('0.5'))
		k = sum([int(c) for c in s[2:]])
		print(n, k + int(n ** 0.5))
		res += k + int(n ** 0.5)
print(res)