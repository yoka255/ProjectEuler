arr = [2, 1, 2]
for i in range(2, 50):
	arr += [1, 1, 2*i]

print(arr[:20])

def calcfrac(arr):
	n = len(arr)
	a, b = arr[n-1], 1
	for i in range(n-2, -1, -1):
		a, b = b, a
		a += b * arr[i]
	return a, b

n = 100
a, b = arr[n-1], 1
for i in range(n-2, -1, -1):
	a, b = b, a
	a += b * arr[i]

a, b = calcfrac(arr[:100])

print(a, b)
print(sum([int(c) for c in str(a)]))