N = 51

squares = set()

for m in range(2, N):
	pas = [[0] * N for x in range(N)]
	for row in range(N):
		pas[row][0] = 1
		pas[row][row] = 1
		for col in range(1, row):
			pas[row][col] = (pas[row-1][col-1] + pas[row-1][col]) % (m ** 2)
		for col in range(row+1):
			if pas[row][col] == 0:
				squares.add((row, col))

res = set()

pas = [[0] * N for x in range(N)]
for row in range(N):
	pas[row][0] = 1
	pas[row][row] = 1
	for col in range(1, row):
		pas[row][col] = (pas[row-1][col-1] + pas[row-1][col])
	for col in range(row+1):
		print(pas[row][col], end = " ")
		if (row, col) not in squares:
			res.add(pas[row][col])
	print()

print([pas[t[0]][t[1]] for t in squares])

print(sum(res))