from itertools import combinations_with_replacement

doubles = [2 * x for x in range(1, 21)] + [50]
all_darts = [x for x in range(1, 21)] + [2 * x for x in range(1, 21)] + [3 * x for x in range(1, 21)] + [25, 50]

res = 0
N = 100

for final in doubles:
    res += 1
    for x in all_darts:
        if x + final < N:
            res += 1
    for (x, y) in combinations_with_replacement(all_darts, 2):
        if x + y + final < N:
            res += 1

print(res)