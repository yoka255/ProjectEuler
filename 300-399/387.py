from euler import is_prime, digsum
from typing import Set


def iteration(harsh: Set[str]) -> Set[str]:
    next_set = set()
    for i in range(10):
        for num in harsh:
            if i == 0 and num == "":
                continue
            next_val = int(num + str(i))
            next_sum = sum(map(int, num)) + i
            if next_val % next_sum == 0:
                next_set.add(num + str(i))
    return next_set


def strong_right_prime(n: str) -> bool:
    if len(n) < 2:
        return False
    
    k = n[:-1]
    if not is_prime(int(k) // sum(map(int, k))):
        return False
    return is_prime(int(n))


def main():
    harshads = {""}
    res = 0
    for _ in range(13):
        harshads = iteration(harshads)
        # print(sorted(list(harshads)))
        for i in range(10):
            for x in harshads:
                if strong_right_prime(x + str(i)):
                    # print(x + str(i))
                    res += int(x + str(i))
    
    print(res)


if __name__ == "__main__":
    main()
