memo = {}

def msb(n):
    k = 1
    while 2 * k <= n:
        k *= 2
    return k

def f(n, i):
    if i < 0:
        return 0
    if (n,i) in memo:
        return memo[(n, i)]
    if n == 0:
        return 1
    
    if n - 2 ** i >= 0:
        memo[(n, i)] = f(n - 2 ** i, i-1) + f(n - 2 ** i, i-2)
    else:
        memo[(n,i)] = f(n, i-1)
    return memo[(n, i)]

print(f(10 ** 25, 100))
"""
for 2 ^ k the answer is k + 1

"""