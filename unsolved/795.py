from euler import gcd

def g(n):
    res = 0
    for i in range(1, n+1):
        res += (-1) ** i * gcd(n, i ** 2)
    return res

for i in range(100):
    print(i, g(i))