from itertools import permutations

array = [x for x in range(1, 11)]

res = ""
for a in permutations(array):
	valid = True
	if 10 in a[:5] and len([x for x in a[:5] if x < a[0]]) == 0:
		s = a[4] + a[9] + a[5]
		for i in range(4):
			if a[i] + a[i+5] + a[i+6] != s:
				valid = False
	else:
		valid = False
	rep = ""
	for i in range(5):
		rep += str(a[i]) + str(a[i+5]) + str(a[(i+6) % 5+5])
	if valid and rep > res:
		res = rep

print(res)

