from euler import *

def P(s, N):
    N -= 1
    l = 1
    for i in range(2, s+1):
        l = lcm(l, i)
    res = N // l
    res -= N // lcm(l, s+1)
    return res

print(P(3, 14))
print(P(6, 10**6))

res = 0

for i in range(1, 32):
    res += P(i, 4 ** i)
print(res)
