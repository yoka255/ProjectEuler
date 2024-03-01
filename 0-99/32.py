from itertools import permutations

def do(a):
	if not len(a):
		return 0
	return a[0] + 10 * do(a[1:])

pos = set()
a = [i for i in range(1, 10)]

for perm in permutations(a):
	perm = list(perm)
	# print(perm)
	for i in range(1, 8):
		for j in range(i+1, 8):
			if do(perm[:i]) * do(perm[i:j]) == do(perm[j:]):
				pos.add(do(perm[j:]))
				print(do(perm[:i]),  do(perm[i:j]), do(perm[j:]))

print(sum(pos))
