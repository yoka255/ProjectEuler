def ispan(s):
	if len(s) != 9:
		return False
	for i in range(1, 10):
		if not str(i) in s:
			return False
	return True

best = 0
for i in range(1, 10**6):
	n = 1
	mul = ""
	while len(mul) < 9:
		mul += str(n * i)
		n += 1
	if ispan(mul) and int(mul) > best:
		best = int(mul)
		print(i, n, mul)

print(best)