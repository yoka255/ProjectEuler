res = 1

for i in range(3, 1002, 2):
	res += i * i + (i * i - (i - 1)) + (i * i - 2 * (i - 1)) + (i * i - 3 * (i-1))
	print(i, res)
print(res)