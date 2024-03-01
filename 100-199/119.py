a = []
for b in range(2, 100000):
	for c in range(1, 20):
		s = str(b ** c)
		if len(s) > 1 and sum([int(x) for x in s]) == b:
			a += [(b ** c, c)]

print(sorted(a)[:31])