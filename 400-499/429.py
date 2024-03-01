from tqdm import tqdm
from euler import sieve


def main():
    N = 10 ** 8
    nums = sieve(N)
    primes = [p for p in range(N) if nums[p]]
    res = 1
    mod = 10 ** 9 + 9
    for p in tqdm(primes):
        j = 1
        k = 0
        while p ** j <= N:
            k += N // (p ** j)
            j += 1
        res *= (1 + pow(p, 2 * k, mod))
        res %= mod
    print(res)

        



if __name__ == "__main__":
    main()
