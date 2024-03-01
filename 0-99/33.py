

for a in range(10, 100):
	for b in range(a, 100):
		if a * (b%10) == b * (a//10) and b // 10 == a % 10:
			print(a, b)
		if a * (b//10) == b * (a%10) and a // 10 == b % 10:
			print(a, b)