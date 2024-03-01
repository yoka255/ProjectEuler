from sage.all import *
from itertools import combinations, product

def not_working():
    N = 1_000_000

    res = 4
    tmp_phi = 1/2
    x = 15499/94744

    for n in range(3, N):
        if is_prime(n):
    #        print(n)
            tmp_phi *= (n-1)/n
            res *= n
        if tmp_phi < x * (1 - 1/res):
            break

    print(res, tmp_phi)

def take2():
    primes = [2,3,5,7,11,13,17,19,23,29,31,37]
    M = len(primes)
    best = 12939386460

#    6469693230
#    1115464350

    x = 15499/94744
#    x = 4/10
    for m in range(2, M+1):
        for ps in combinations(primes, m):
            for powers in product([1,2,3], repeat=m):
                num = 1
                tmp_phi = 1
                for i, p in enumerate(ps):
                    num *= p ** powers[i]
                    tmp_phi *= (p-1) / p
                if tmp_phi * num / (num - 1) < x :
                    best = min(best, num)
                    if num == best:
                        print(tmp_phi)
                        print(tmp_phi / x)
        
    print(best)

if __name__ == "__main__":
    take2()