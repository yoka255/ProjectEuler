from sage.all import *

def calc_n(p1, p2):
    s = len(str(p1))
    k = (-p1 * pow(10 ** s, -1, p2)) % p2
    n = (10 ** s) * k + p1
    return n

if __name__ == "__main__":
    print(calc_n(19, 23))
    p1 = 5
    res = 0
    while p1 < 1_000_000:
        p2 = int(next_prime(p1))
        res += calc_n(p1, p2)
        p1 = p2
        
    print(res)