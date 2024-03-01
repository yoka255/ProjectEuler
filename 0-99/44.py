from tqdm import tqdm

pentset = set()
pent = [1]

N = 10**4

for n in range(1, N):
	pentset.add((n * (3 * n - 1)) // 2)
	pent += [(n * (3 * n - 1)) // 2]

for n in range(N, 2 * N):
	pentset.add((n * (3 * n - 1)) // 2)

best = float('inf')

for i in tqdm(range(N)):
	for j in range(i+1, N):
		n = pent[i]
		m = pent[j]
		if n + m in pentset and m - n in pentset and m - n < best:
			print(n, m)
			best = m - n
print(best)