from euler import totient, sieve, calc_divisors, gcd
from typing import List


def get_divs(n, divs) -> List[int]:
    res = []
    while n != 1:
        res += [divs[n]]
        n //= divs[n]
    return res


def main():
    N = 10 ** 6
    target = 25
    res = []
    phi = totient(9 * N + 1)
    prime_divisor = calc_divisors(9 * N + 1)

    for n in range(2, N):
        if gcd(n, 10) != 1 or prime_divisor[n] == n:
            continue
        k = phi[9 * n]
        divs = get_divs(k, prime_divisor)
        assert pow(10, k, 9 * n) == 1
        for d in divs:
            while k % d == 0 and pow(10, k//d, 9 * n) == 1:
                k //= d
        if (n-1) % k == 0:
            res += [n]
        if len(res) == target:
            break
    print(res)
    print(sum(res))




if __name__ == "__main__":
    main()
