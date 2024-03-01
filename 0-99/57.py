from math import log, ceil

a = 3
b = 2

cnt = 0

for i in range(1000):
	print(a/b)
	if ceil(log(a, 10)) > ceil(log(b, 10)):
		cnt += 1
	a, b = a + 2*b, a + b

print(cnt)