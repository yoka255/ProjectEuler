from euler import *

def func(n, fac):
	res = 0
	for char in str(n):
		res += int(fac[int(char)])
	return res

fac = calcfactorial(10)

count = 0

for n in tqdm(range(2, 10**6)):
	vis = set()
	x = n
	while x not in vis:
		vis.add(x)
		x = func(x, fac)
	# print(n, x, len(vis))
	if len(vis) == 60:
		count += 1

print(count)

