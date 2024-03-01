from euler import *

N = 10**7

p = sieve(N)

best = 0
for i in tqdm(range(2, N)):
	if p[i] and ispan(i):
		best = i
print(best)
