from math import gcd

M = 100_000_000

res = 0

for m in range(1, 10000):
    for n in range(1, m):
        if gcd(m,n) != 1:
            continue
        if m % 2 and n % 2: 
            continue
        a =(m ** 2 - n ** 2)
        b =2 * m * n
        c =(m ** 2 + n ** 2)
        if c % (b-a) == 0:
            print(a, b, c)
            res += M // (a + b + c)

print(res)