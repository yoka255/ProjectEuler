# def p(L, n):
# 	num = 1
# 	cnt = 0 
# 	while 1:
# 		num *= 2
# 		cnt += 1
# 		if str(num).startswith(L):
# 			n -= 1
# 		if n == 0:
# 			return cnt

# # print(p("123",678910))
# for n in range(1,20):
# 	print(n, p("123", n) - p("123", n-1))
cnt = 1
exp = 90
N = 678910

curr = 2 ** 90

while cnt < N:
	if str(curr * 2 ** 196)[:3] == "123":
		exp += 196
		curr *= 2 ** 196
	elif str(curr * 2 ** 289)[:3] == "123":
		exp += 289
		curr *= 2 ** 289
	elif str(curr * 2 ** 485)[:3] == "123":
		exp += 485
		curr *= 2 ** 485
	print(exp)
	cnt += 1
print(exp)