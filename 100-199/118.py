from euler import is_prime
from itertools import combinations, permutations
from typing import Iterable, Set, List
from functools import lru_cache
from tqdm import tqdm


def to_number(a: Iterable[int]) -> int:
    return sum([2 ** (x-1) for x in a])


def calc(nums: Set[int], prime_count: List[int]) -> int:
    if not len(nums):
        return 1
    res = 0
    nums = nums.copy()
    x = max(nums)
    nums.remove(x)
    for k in range(len(nums) + 1):
        for comb in combinations(nums, k):
            if prime_count[to_number(list(comb) + [x])]:
                next_nums = nums.copy()
                for i in comb:
                    next_nums.remove(i)
                res += prime_count[to_number(list(comb) + [x])] * calc(next_nums, prime_count)
    return res
    

def main():
    nums = list(range(1, 10))
    prime_count = [0] * (2 ** 9)
    for k in range(1, 10):
        for comb in list(combinations(nums, k)):
            ind = to_number(comb)
            for perm in permutations(comb):
                if is_prime(int("".join(map(str, perm)))):
                    prime_count[ind] += 1

    print(calc(set(range(1, 10)), prime_count))

if __name__ == "__main__":
    main()
