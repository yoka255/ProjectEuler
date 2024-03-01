import numpy as np

mat = np.zeros((80, 80)).astype(int)

with open('p081_matrix.txt', 'r') as f:
	for i in range(80):
		for j, num in enumerate(f.readline().split(',')):
			mat[i][j] = int(num)

dp = np.zeros((80, 80)).astype(int)

for i in range(80):
	for j in range(80):
		if i == 0 and j == 0:
			dp[i][j] = mat[i][j]
		elif i == 0:
			dp[i][j] = mat[i][j] + dp[i][j-1]
		elif j == 0:
			dp[i][j] = mat[i][j] + dp[i-1][j] 
		else:
			dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + mat[i][j]

print(dp[79][79])