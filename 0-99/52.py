from tqdm import tqdm

def isperm(a, b):
	return sorted([c for c in a]) == sorted([c for c in b])


def ask(n):
	for i in range(2, 7):
		if not isperm(str(n), str(i * n)):
			return False
	return True

N = 10**7

for n in range(1, N):
	if ask(n):
		print(n)
		quit()
