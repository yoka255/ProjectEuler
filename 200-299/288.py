from tqdm import tqdm

if __name__ == "__main__":
    res = 0
    # p = 61
    # q = 10 ** 7
    # res_mod = pow(61,10)
    p=3
    q=10**4
    res_mod = pow(3,20)
    M = 50515093
    S = 290797
    geo_sum = 0

    for n in tqdm(range(q+1)):
        T = S % p
        S = (S * S) % M
        res += T * geo_sum
        res %= res_mod
        geo_sum += pow(p, n, res_mod)
        geo_sum %= res_mod
    print(res)