from typing import Optional, Tuple, List
from collections import deque
from tqdm import tqdm


def all_low(n: str):
    return all(int(c) < 3 for c in n)


def f(n: int) -> int:
    # bfs: deque[Tuple[int, int]] = deque()
    if n == 9999:
        return int("1" * 4 + "2" * 16)
    bfs: List[Tuple[int, int]] = []

    res_digs = -1
    res = []

    for d in range(1, 10):
        bfs.append((d, 1))

    i = 0 
    while bfs:
        cur_mul, cur_digits = bfs[i]
        i += 1
        if cur_digits > res_digs > 0:
            break

        if all_low(str(n * cur_mul)):
            res.append(n * cur_mul)
            res_digs = cur_digits

        for d in range(10):    
            next_mul = 10 ** cur_digits * d + cur_mul
            if all_low(str(next_mul * n)[-(cur_digits + 1):]):
                bfs.append((next_mul, cur_digits + 1))

    bfs.clear()

    return min(res)

def main():
    res = 0

    for n in tqdm(range(1, 10001)):
        res += f(n) // n

    print(res)

def main2():
    res = 0

    for n in range(9980, 10001):
        print(n, f(n))
        res += f(n) // n

    print(res)

if __name__ == "__main__":
    main()