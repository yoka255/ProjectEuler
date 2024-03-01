import numpy as np

def is_integer(x : float) -> bool:
    return x - int(x) < 10 ** -9

N = 10 ** 4

f = np.zeros(N + 1)

for a in range(int(N)):
    for b in range(int(N)):
        x = a/2
        y = b/2
        if is_integer((2 * a * a + 2 * b * b) ** 0.5) and (2 * a * a + 2 * b * b) ** 0.5 <= N:
            f[int(((2 * a * a + 2 * b * b) ** 0.5))] += 1
        if is_integer((x * x + y * y) ** 0.5) and (x * x + y * y) ** 0.5 <= N:
            f[int((x * x + y * y) ** 0.5)] += 1

for i in range(N+1):
    if f[i]:
        print(i, f[i])