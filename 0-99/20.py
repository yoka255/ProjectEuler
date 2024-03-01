def digsum(n):
	if n < 10:
		return n
	return n%10 + digsum(n // 10)

n = 1
for i in range(1, 101):
	n *= i

print(digsum(n)) 