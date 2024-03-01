from math import log

res = 0
best = 0
with open('p099_base_exp.txt', 'r') as f:
	l = f.read().split()

	for i in range(1000):
		a = l[i].split(',')
		b, e = int(a[0]), int(a[1])
		if log(b) * e > res:
			print(b, e)
			res = e * log(b)
			print(i+1)



