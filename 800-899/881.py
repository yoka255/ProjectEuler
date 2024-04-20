from functools import lru_cache
from typing import Tuple
from itertools import product


@lru_cache(maxsize=None)
def dp(tup: Tuple, k: int) -> int:
    if sum(tup) < k:
        return 0
    if k == 0:
        return 1
    if len(tup) == 0:
        return 0

    res = 0
    group_sizes = list(tup)
    while group_sizes[-1] == 0:
        group_sizes = group_sizes[:-1]
    tup = tuple(group_sizes)
    for n in range(min(len(tup) + 1, k + 1)):
        if group_sizes[-1] == 1:
            res += dp(tuple(group_sizes[:-1]), k - n)
        else:
            res += dp(tuple(group_sizes[:-1] + [group_sizes[-1] - 1]), k-n)
    
    return res
    

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

def calc_val(tup: Tuple) -> int:
    i = 0
    res = 1
    for j, cnt in enumerate(tup[::-1]):
        for _ in range(cnt):
            res *= pow(primes[i], len(tup) - j)
            i += 1
    return res


def main():
    target = 10 ** 4
    res = 10 ** 100
    for tup in product(range(13), repeat=7):
        if sum(tup) > 13:
            continue
        for k in range(sum(tup)):
            if dp(tup, k) >= target:
                res = min(res, calc_val(tup))
    print(res)


if __name__ == "__main__":
    main()
