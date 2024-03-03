from euler import totient, sieve, calc_divisors, gcd
from typing import List


def get_divs(n, divs) -> List[int]:
    res = []
    while n != 1:
        res += [divs[n]]
        n //= divs[n]
    return res


def main():
    N = 10 ** 7
    target = 10 ** 6

    phi = totient(9 * N + 1)
    prime_divisor = calc_divisors(9 * N + 1)

    for n in range(2, N):
        if phi[9 * n] <= target:
            continue
        if gcd(n, 10) != 1:
            continue
        p = phi[9 * n]
        divs = get_divs(p, prime_divisor)
        assert pow(10, p, 9 * n) == 1
        for d in divs:
            while p % d == 0 and pow(10, p//d, 9 * n) == 1:
                p //= d
        if p >= target:
            print(n)
            break



if __name__ == "__main__":
    main()
