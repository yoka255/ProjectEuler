res = 0
for num in range(2, 5*(10**5)):
	sp = 0
	for char in str(num):
		sp += int(char) ** 5
	if sp == num:
		res += sp

print(res)
