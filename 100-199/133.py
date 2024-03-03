from euler import gcd, sieve


def main():
    N = 10 ** 5
    is_prime = sieve(N + 2)
    res = [2, 3]
    for p in range(5, N, 2):
        if not is_prime[p]:
            continue
        if not pow(10, gcd(p-1, (2 ** 20) * (5 ** 10)), p) == 1:
            res += [p]
            
    print(sum(res))



if __name__ == "__main__":
    main()
