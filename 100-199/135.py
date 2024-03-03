from tqdm import tqdm


def main():
    N = 10 ** 6
    res = [0] * (N + 1)
    for a in tqdm(range(1, N)):
        for d in range(a // 4, min(a // 4 + N // (4 * a) + 2, a)):
            if 0 <= a * (4 * d - a) <= N:
                # print(a, d, a * (4 * d - a))
                res[a * (4 * d - a)] += 1
    
    print(res[27])
    print(res[1155])
    print(len([x for x in res if x == 10]))


if __name__ == "__main__":
    main()
