from sage.all import *
import tqdm

def que_381(n):
    res = 0
    for p in tqdm.tqdm(range(5, n)):
        if is_prime(p):
            res += (-3 * pow(8, p-2, p)) % p
#            print(p, (-3 * pow(8, p-2, p)) % p)
    return res


if __name__ == "__main__":
    N = 10**8
    print(que_381(N))
