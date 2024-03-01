from euler import *
from math import floor
from tqdm import tqdm

res = (2, 5)

N = 10**6

for d in tqdm(range(8, N+1)):
	n = floor(3 * d / 7)
	# print(n/d, gcd(n, d))
	# input()
	if gcd(d, n) == 1 and abs(3/7 - res[0]/res[1]) > abs(3/7 - n/d):
		res = (n,d)

print(res)