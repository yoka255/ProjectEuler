from math import log, ceil, floor, sqrt
res = 0 
for p in range(1,1006):
	for q in range(p+1, p + 1 + int(2*sqrt(p))+ 1):
		if p + q <= 2011:
			diff = sqrt(q) - sqrt(p)
			if diff < 1:
				n = ceil(ceil(-2011 / log(diff, 10))/2)
				res += n
print(res)