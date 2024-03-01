import numpy as np

p = np.zeros((101, 101))
q = np.zeros((101, 101))

for i in range(100):
	p[i][100] = 1

for a in range(99, -1, -1):
	for b in range(99, -1, -1):
		for t in range(1, 9):
			if b + 2 ** (t-1) >= 100:
				p[a][b] = max(p[a][b], ((0.5 ** t) +  0.5 * (1 - 0.5 ** t) * p[a+1][b]) / (0.5 + 0.5 ** (t+1)))
			else:
				p[a][b] = max(p[a][b], ((0.5 ** (t+1)) * (p[a+1][b + 2 ** (t-1)] + p[a][b + 2 ** (t-1)]) +  0.5 * (1 - 0.5 ** t) * p[a+1][b]) / (0.5 + 0.5 ** (t+1)))
		# print(a, b, p[a][b])
		# input()

print(p[0][0], p[1][0])
print((p[0][0] + p[1][0]) / 2)