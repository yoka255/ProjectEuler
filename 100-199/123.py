from euler import *

N = 10 ** 7
p = sieve(N)
n = 1
for k in range(N):
    if p[k]:
        if n % 2 == 1 and (2 * n * k + 2) % (k ** 2) > (10 ** 10):
            print(k, n, 2 * n * k + 2)
            exit(0)
        n += 1