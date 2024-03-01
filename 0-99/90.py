from itertools import combinations

cnt = 0
for c in combinations(range(10), 6):
	for d in combinations(range(10), 6):
		a = list(c)
		b = list(d)
		if 6 in a and not 9 in a:
			a += [9]
		if 9 in a and not 6 in a:
			a += [6]
		if 6 in b and not 9 in b:
			b += [9]
		if 9 in b and not 6 in b:
			b += [6]
		can = True
		for x in range(1, 10):
			s = str(x*x).zfill(2)
			if not ((int(s[0]) in a and int(s[1]) in b) or (int(s[1]) in a and int(s[0]) in b)):
				can = False
		if can:
			print(a, b)
			cnt += 1

print(cnt)
print(cnt // 2)
