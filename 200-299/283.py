# (s-a) * (s-b) * (s-c)

# s ^ 3 - (a+b+c)*s^2 + (ab +ac + bc)*s - abc

# (a+b+c) | 2*abc
import math
from tqdm import tqdm

def heron(a, b, c):
	s = (a+b+c)/2
	return s * (s-a) * (s-b) * (s-c)


highest = 0
res = 0
counts = dict()
for a in tqdm(range(1, 1000)):
	for b in range(a, 1000):
		if math.gcd(a, b) == 1:
			for c in range(b, 1000):
				if c < a + b:
					if heron(a, b, c) ** 0.5 == int(heron(a, b, c) ** 0.5) and int(heron(a, b, c)) % (a + b + c)**2 == 0:
						
						# print(a, b, c)
						# print(heron(a, b, c) **0.5, (a+b+c))
						if int(heron(a, b, c) ** 0.5) // (a + b + c) <= 1000:
							res += (a+b+c) 
						highest = max(highest, int(heron(a, b, c)) // (a + b + c)**2)
						if math.gcd(a,b,c) == 1:
							side = a+b+c
							if side in counts:
								counts[side] += 1
							else:
								counts[side] = 1

print(highest)
print(res)