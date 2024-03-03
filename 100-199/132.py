from euler import sieve


def main():
    N = 10 ** 6
    res = []

    is_prime = sieve(N + 2)
    for p in range(4, N):
        if is_prime[p] and pow(10, 10 ** 9, p) == 1:
            res += [p]

    print(res)
    print(len(res))
    print(sum(res[:40]))


if __name__ == "__main__":
    main()