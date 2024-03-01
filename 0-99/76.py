import numpy as np

N = 100
dp = np.zeros(101).astype(int)
dp[0] = 1

for x in range(1, N):
	for i in range(x, N+1):
		dp[i] += dp[i-x]

for x in range(N+1):
	print(x, dp[x])