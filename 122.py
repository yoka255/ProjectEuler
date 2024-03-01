from math import log2, ceil
from itertools import combinations_with_replacement
from tqdm import tqdm

def pop_count(n: int) -> int:
    if n == 0:
        return 0
    return n % 2 + pop_count(n // 2)


def main():
    N = 200
    dp = [10000] * (N + 1)
    dp[0] = 0
    dp[1] = 0
    for n in range(2, N+1):
        dp[n] = int(log2(n)) + pop_count(n) - 1
        for k in range(1, n):
            if n % k == 0:
                dp[n] = min(dp[n], dp[k] + dp[n//k])
    print("\n".join([f"{x}: {y}" for x, y in zip(range(N+1), dp)]))
    print(sum(dp))


def inefficient():
    N = 200
    inf = 10000
    dp = [inf] * (N + 1)
    dp[0] = 0
    dp[1] = 0
    sol = [tuple()] * (N+1)
    open_sets = {(1,)}
    while max(dp) == inf:
        print(min([i for i in range(N+1) if dp[i] == inf]))
        next_sets = set()
        for t in tqdm(open_sets):
            for a,b in combinations_with_replacement(t, 2):
                if a + b > N:
                    continue
                if dp[a+b] == inf:
                    dp[a+b] = len(t)
                    sol[a+b] = t
                if len(t) <= dp[a+b] + 2:
                    next_sets.add(tuple(list(t) + [a+b]))
        open_sets = next_sets
    
    for i in range(1, N+1):
        print(f"{i}: {dp[i]} : {sol[i]}")
    print(sum(dp))




if __name__ == "__main__":
    inefficient()
