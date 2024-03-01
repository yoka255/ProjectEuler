from typing import List
from itertools import combinations, product
from tqdm import tqdm


def is_good(A: List[int]) -> bool:
    for x in range(2, len(A)):
        if sum(A[:x]) <= sum(A[-x+1:]):
            return False
    optsums = set()
    for x in range(1, len(A)):
        for tup in combinations(A, x):
            if sum(tup) in optsums:
                return False
            optsums.add(sum(tup))
    return True


def main():
    guess = [20, 31, 38, 39, 40, 42, 45]


    # best_res = "".join(map(str, guess))
    best = 1

    for diffs in tqdm(list(product(range(-7, 5), repeat=7))):
        if sum(diffs) >= best:
            continue
        bad = False
        for i in range(6):
            if guess[i] + diffs[i] >= guess[i+1] + diffs[i+1]:
                bad = True
        if bad:
            continue
        attempt = [x + y for x, y in zip(guess, diffs)]
        if is_good(attempt):
            best = sum(diffs)
            print("".join(map(str, attempt)))



if __name__ == "__main__":
    main()
