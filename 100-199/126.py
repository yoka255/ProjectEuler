from itertools import combinations_with_replacement


def layer(n: int, a: int, b: int, c: int) -> int:
    return 2 * (a * c + b * c + a * b) + 4 * (n - 1) * (a + b + c) + 4 * (n - 1) * (n - 2)


def C(n: int) -> int:
    res = 0
    for a, b, c in combinations_with_replacement(range(1, n), 3):
        k = 1
        while layer(k, a, b, c) < n:
            k += 1
        if layer(k, a, b, c) == n:
            res += 1
    return res




def main():
    N = 2 * 10 ** 4
    cnt = [0] * (N + 1)

    a = 1
    while 4 * a <= N:
        b = a
        while 2 * a * b + 2 * b + 2 * a <= N:
            c = b
            while 2 * a * b + 2 * b * c + 2 * a * c <= N:
                k = 1
                while layer(k, a, b, c) <= N:
                    cnt[layer(k, a, b, c)] += 1
                    k += 1
                c += 1
            b += 1
        a += 1

    for i in range(1, N+1):
        print(f"{i}: {cnt[i]}")
    print([i for i in range(1, N+1) if cnt[i] == 1000])
    # print(cnt[22])
    # print(cnt[46])
    # print(cnt[78])
    # print(cnt[118])
    # print(cnt[154])



if __name__ == "__main__":
    main()