from scipy.optimize import fsolve

N = 5000

def arith_geo_sum(r):

    res = 0
    for k in range(1, N+1):
        res += (900 - 3 * k) * (r ** (k - 1))
    return res + 600_000_000_000

    res = 900 * (r ** N - 1) / (r - 1)
    res -= 3 * r * (1 - N * r ** (N-1) + (N-1) * r ** N) / (1 - r) ** 2
    return res + 600_000_000_000


l = 1.002
r = 1.003
while r - l >= 10 ** (-15):
    m = (l + r) / 2
    if arith_geo_sum(m) > 0:
        l = m
    else:
        r = m

print(l, r, arith_geo_sum(l))