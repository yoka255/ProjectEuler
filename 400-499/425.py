from sage.all import *
from tqdm import tqdm

class DSU:
    def __init__(self, n : int):
        self.par = [i for i in range(n)]
        self.rk = [0] * n

    def find(self, u : int) -> int:
        if self.par[u] == u:
            return u
        self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self, u : int, v : int) -> bool:
#        print(u, v)
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        if self.rk[u] < self.rk[v]:
            u, v = v, u
        self.par[v] = u
        if self.rk[u] == self.rk[v]:
            self.rk[u] += 1
        return True
    

if __name__ == "__main__":
    N = 10 ** 7
    rels = DSU(N)
    res = 0
    for k in tqdm(range(3, N)):
        if is_prime(k):
            k_str = str(k)
            if len(k_str) > 1:
                if is_prime(int(k_str[1:])) and k_str[1] != "0":
                    rels.union(k, int(k_str[1:]))
#                if is_prime(int(k_str[:-1])):
#                    rels.union(k, int(k_str[:-1]))
            for i in range(len(k_str)):
                for j in range(int(k_str[i])):
                    x_str = k_str[:i] + str(j) + k_str[i+1:]
                    x = int(x_str)
                    if x_str[0] != "0" and is_prime(x):
#                        print(k_str, x_str, i)
#                        print(k, x)
                        rels.union(k, x)
            if rels.find(k) != rels.find(2):
#                print(k)
                res += k
    print(res)
            
