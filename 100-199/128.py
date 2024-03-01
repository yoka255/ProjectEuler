from euler import sieve
from typing import List
import tqdm
import numpy as np


def ring(n):
    if n == 0:
        return [1] * 6
    return [i for i in range(2 + 3 * n * (n-1), 2 + 3 * n * (n-1) + 6 * n, n)]


def count_primes(x: int, others: List[int], is_prime: np.ndarray):
    return sum([is_prime[abs(x-a)] for a in others])


def main():
    N = 10 ** 7
    target = 2000
    is_prime = sieve(N)
    res = [1, 2]
    r = 2
    while len(res) < target:
        print(len(res))
        cur = ring(r)
        inner = ring(r-1)
        outer = ring(r + 1)

        for i in range(6):
            if i == 0:
                others = [inner[0]] + [cur[0] + 6 * r - 1] + [outer[0], outer[0] + 1, outer[0] + 6 * (r + 1) - 1]
            else:
                others = [inner[i]] + [outer[i] - 1, outer[i], outer[i] + 1]
            # print(cur[i], others)
            if count_primes(cur[i], others, is_prime) == 3:
                res += [cur[i]]
            # print(cur[j], others)
        
        x = cur[0] + 6 * r - 1
        x_others = [cur[0]] + [inner[0]] + [inner[0] + 6 * (r - 1) - 1] + [outer[0] + 6 * (r + 1) - 1] + [outer[0] + 6 * (r + 1) - 2]
        # print(x, x_others)
        if count_primes(x, x_others, is_prime) == 3:
                res += [x]

        r += 1

    print(res)


if __name__ == "__main__":
    main()
