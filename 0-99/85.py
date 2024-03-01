def search(a, x):
	l, r = 1, len(a) - 1
	while l < r:
		m = (l + r) // 2
		if a[m] > x:
			r = m
		else:
			l = m + 1
	return l


arr = [(n * (n-1)) // 2 for n in range(2, 2000)]

res = 0
N = 2 * 10**6

for i, k in enumerate(arr):
	l = search(arr, N / k)
	if abs(N - k * arr[l]) < abs(N - res):
		print(i+2, l+2, k, arr[l])
		res = k * arr[l]
	if abs(N - k * arr[l-1]) < abs(N - res):
		print(i+2, l+1, k, arr[l-1])
		print((i+2) * (l+1))
		res = k * arr[l-1]

print(res)
