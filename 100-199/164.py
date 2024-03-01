import numpy as np
from itertools import product


def main():
    dp = np.zeros((10, 10, 21))
    for i in range(10):
        for j in range(10-i):
            dp[i][j][2] = 1
    
    for k in range(3, 21):
        for i in range(10):
            for j in range(10-i):
                for l in range(10 - i - j):
                    dp[i][j][k] += dp[j][l][k-1]
    res = sum([dp[i][k][20] for i,k in product(range(1, 10), range(10))])
    print(res)


if __name__ == "__main__":
    main()
