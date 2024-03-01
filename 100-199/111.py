from euler import is_prime
from itertools import combinations, product


def M(n: int, d: int) -> int:
    possible_digs = [i for i in range(10) if i != d]
    for m in range(n, 0, -1):
        for digs in combinations(range(n), m):
            for extra_digs in product(possible_digs, repeat=n-m):
                j = 0
                num_list = []
                for i in range(n):
                    if i in digs:
                        num_list.append(d)
                    else:
                        num_list.append(extra_digs[j])
                        j += 1
                if num_list[0] == 0:
                    continue
                num = int("".join(map(str, num_list)))
                if is_prime(num):
                    return m  
    return 0     


def S(n: int, d: int, m: int):
    possible_digs = [i for i in range(10) if i != d]
    res = 0
    for digs in combinations(range(n), m):
        for extra_digs in product(possible_digs, repeat=n-m):
            j = 0
            num_list = []
            for i in range(n):
                if i in digs:
                    num_list.append(d)
                else:
                    num_list.append(extra_digs[j])
                    j += 1
            if num_list[0] == 0:
                continue
            num = int("".join(map(str, num_list)))
            if is_prime(num):
                res += num
    return res


def main():
    n = 10
    res = 0
    for d in range(10):
        print(M(n, d))
        print(S(n, d, M(n, d)))
        res += S(n, d, M(n, d))
    print(res)


if __name__ == "__main__":
    main()
