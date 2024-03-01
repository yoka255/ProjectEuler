fibo = [100, 100]
for i in range(10000):
    fibo += [fibo[-1] + fibo[-2]]

def D(x, k):
    # print(k)
    A = """1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"""
    B = """8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"""
    # A = "A"
    # B = "B"
    if k == 0:
        return A[x]
    if k == 1:
        return B[x]
    if x >= fibo[k-2]:
        return D(x - fibo[k-2], k-1)
    return D(x, k-2)

def D_wrap(x):
    i = 0
    while fibo[i] <= x:
        i += 1
    return D(x, i)

for n in range(17, -1, -1):
    print(D_wrap((127 + 19 * n) * (7 ** n) - 1), end = "")