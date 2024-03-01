from tqdm import tqdm

def base_7(n):
	if n < 7:
		return [n]
	return [n%7] + base_7(n//7)

# for i in range(n):
# 	p.append([0] * (n+1))
# p[0][0] = 1

# for i in range(1,n):
# 	p[i][0] = 1
# 	p[i][i] = 1
# 	for k in range(1, i):
# 		p[i][k] = p[i-1][k-1] + p[i-1][k]

# tot = 0
# for i in range(n):
# 	count = 0
# 	for j in range(i):
# 		if p[i][j] % 7 == 0:
# 			count += 1
# 	print(i, count)
# 	tot += count
# print(tot)

n = 10**9

tot = 0
for k in tqdm(range(n)):
	count = 0
	b = base_7(k)
	currnum = k
	currmul = 1
	for dig in range(len(b)-1, 0, -1):
		currnum -= b[dig] * (7 ** dig)
		count += currmul * b[dig] * (7 ** dig - 1 - currnum)
		currmul *= (b[dig] + 1)
	tot += count
print((n * (n+1))//2 - tot)
