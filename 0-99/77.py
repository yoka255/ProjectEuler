import numpy as np
from euler import *

N = 200
dp = [0] * (N+1)
dp[0] = 1

primes = [p for p, v in enumerate(sieve(N)) if v == 1]

for x in primes:
	for i in range(x, N+1):
		dp[i] += dp[i-x]

for x in range(N+1):
	print(x, dp[x])