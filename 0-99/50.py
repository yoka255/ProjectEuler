from euler import *

N = 10**6

p = sieve(N)

primes = []
for n in range(N):
	if p[n]:
		primes += [n]

best = 41
bestlen = 6

for i in tqdm(range(len(primes))):
	s = primes[i]
	j = i + 1
	while s < N and j < len(primes):
		if p[s] and j - i + 1 > bestlen:
			bestlen = j-i+1
			best = s
			print(bestlen, best)
		s += primes[j]
		j += 1
		

print(best)