from itertools import permutations, combinations, product

def mul(a, b):
	return a*b
def add(a, b):
	return a+b
def sub(a, b):
	return a-b
def div(a, b):
	if b == 0:
		return 10**10
	return a/b

best = (1, 2, 3, 4)
bestres = 0

for nums in combinations(range(1, 10), 4):
	poss = set()
	for s in permutations(nums):
		a, b, c, d = s
		for f in product([mul, div, add, sub], repeat=3):
			for o in permutations(range(3)):
				tmpres = 0
				if o == (0, 1, 2): #((a + b) + c) + d
					tmpres = f[2](f[1](f[0](a, b), c), d)
				if o == (0, 2, 1): #(a + b) + (c + d)
					tmpres = f[1](f[0](a, b), f[2](c, d))
				if o == (1, 0, 2): #(a + (b + c)) + d
					tmpres = f[2](f[0](a, f[1](b, c)), d)
				if o == (1, 2, 0): #a + ((b + c) + d)
					tmpres = f[0](a, f[2](f[1](b, c), d))
				if o == (2, 1, 0): #a + (b + (c + d))
					tmpres = f[0](a, f[1](b, f[2](c, d)))
				if o == (2, 0, 1): #(a + b) + (c + d)
					tmpres = f[1](f[0](a, b), f[2](c, d))
				poss.add(tmpres)
				if tmpres - int(tmpres) < 10**(-3):
					poss.add(int(tmpres))
	i = 1 
	while 1:
		if i not in poss:
			break
		i += 1
	if i - 1 > bestres:
		bestres = i-1
		best = nums
		print(best, bestres)
