from math import prod
from euler import SqrtNumber
from collections import defaultdict
from itertools import product
from tqdm import tqdm


OPTS = defaultdict(list)
MAX_RES = 120_000
SEARCH_LIMIT = 4 * MAX_RES


def is_int(x: float) -> bool:
    return x == int(x)


def check_solution(p: int, b: int, c:int) -> int | None:
    q: float = (p + (4 * b ** 2 - 3 * p ** 2) ** 0.5) / 2
    r: float = (p + (4 * c ** 2 - 3 * p ** 2) ** 0.5) / 2
    a: float = (q ** 2 + r ** 2 - q * r) ** 0.5

    if sum(map(is_int, [q,r,a])) == 3:
        print(p,q,r,a,b,c)
        return int(p + q + r)
    return None



def main():
    # inv = SqrtNumber(7, 4 ,3)
    # for n in range(1, SEARCH_LIMIT + 1):
    #     x = SqrtNumber(n, 0, 3)
    #     while x.a <= SEARCH_LIMIT:
    #         x *= inv
    #         if x.a % 2 == 0:
    #             OPTS[x.b].append(x.a // 2)

    for b in tqdm(range(1, 2 * MAX_RES)):
        p = 1
        while 4 * b * b - 3 * p * p >= 0:
            if is_int((4 * b * b - 3 * p * p) ** 0.5):
                OPTS[p].append(b)
            p += 1

    for q in range(1000):
        if OPTS[q]:
            print(q, OPTS[q])

    res = set()

    for p in range(SEARCH_LIMIT):
        for b, c in product(OPTS[p], repeat=2):
            sol = check_solution(p, b, c)
            # print(sol)
            # input()
            if sol:
                res.add(sol)
    
    print(sum([x for x in res if x <= MAX_RES]))


if __name__ == "__main__":
    main()
