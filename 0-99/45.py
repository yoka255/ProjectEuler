import tqdm

pent = set()
tri = set()

N = 10**6

for n in range(1, N):
	tri.add(n * (n + 1) // 2)
	pent.add(n * (3 * n - 1) // 2)


for n in range(144, N):
	if n * (2 * n - 1) in tri and n * (2 * n - 1) in pent:
		print(n * (2 * n - 1))