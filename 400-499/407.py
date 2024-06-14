import sys
from itertools import product
from tqdm import tqdm

N=10**7
divisors = [[] for _ in range (N+1)]

for x in range(2,N+1):
	if not divisors[x]:
		for k in range(x,N+1,x):
			divisors[k].append(x)

print(divisors[:10])
	
res = [1] * (N+1)
res[1]=0
res[0]=0

for a in tqdm(range(1, N+1)):
	p_divs = set(divisors[a]+divisors[a-1])
	x = a*(a-1)
	mul_divs=[]
	for p in p_divs:
		cur_div = [1]
		while x % (cur_div[-1] * p) ==0:
			cur_div.append(cur_div[-1]*p)
		mul_divs.append(cur_div)
	for div_choice in product(*mul_divs):
		prod=1
		for d in div_choice:
			prod*=d

		if a < prod <= N:
			res[prod]=max(res[prod], a)
print(res[:10])
print(sum(res))