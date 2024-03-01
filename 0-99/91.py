cnt = 0
N = 51
for a in range(N):
	for b in range(N):
		for c in range(N):
			for d in range(N):
				if (a, b) > (c, d) and (c, d) > (0, 0):
					x = a ** 2 + b ** 2
					y = c ** 2 + d ** 2
					z = (a - c) ** 2 + (b - d) ** 2
					if x == y+z or z == y+x or y == z+x:
						cnt += 1


print(cnt)
