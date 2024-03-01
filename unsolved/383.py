factori = [1]

def calc_fact():
    for n in range(1, 10000):
        factori.append(factori[-1] * n)

def fact(n):
    return factori[n]


def v(n, p):
    res = 0
    while n % p == 0:
        n //= p
        res += 1
    return res


def to_string(n, b):
    if n < b:
        return str(n)
    return to_string(n // b, b) + str(n % b)

def vfact(n, p):
    q = p
    res = 0
    while q <= n:
        res += n // q
        q *= p
    return res

if __name__ == "__main__":    
    res = 0

    for i in range(1,10000000):

    #    print(f"{i} {v(fact(i), 5)} {v(fact(2 * i), 5)}")
        if 2 * vfact(i, 5) > vfact(2 * i - 1, 5):
            # print(f"{to_string(i, 5)}  {v(fact(i), 5)=} {v(fact(2 * i - 1), 5)=}")
            res += 1
        if pow(5, v(i, 5)) == i:
            print(i, res-1)