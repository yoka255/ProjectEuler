con = ""

n = 1
while len(con) < 10**6:
	con += str(n)
	n += 1

res = 1
for i in range(7):
	print(int(con[10**i-1]))
	res *= int(con[10**i-1])
print(res)