import numpy

def binsearch(arr, x):
	l, r = 0, len(arr) - 1
	while l < r:
		m = (l + r)//2
		if arr[m] >= x:
			r = m
		else:
			l = m + 1
	if arr[l] < x:
		l += 1
	return l

def find_set(nums, types, poly):
	if sorted(types) == [0, 1, 2, 3, 4, 5] and nums[0] // 100 == nums[-1] % 100:
		print(nums, sum(nums))
		input()
	for i in range(6):
		if not i in types:
			req = (nums[-1] % 100) * 100
			j = binsearch(poly[i], req)
			while poly[i][j] < req + 100:
				find_set(nums + [poly[i][j]], types + [i], poly)
				j+=1


poly = [[], [], [], [], [], []]

for i in range(6):
	for n in range(2, 300):
		num = n * ((i+1) * n - (i - 1)) // 2
		if num >= 1000 and num < 10000:
			poly[i] += [num]

for i in range(6):
	print(i)
	for num in poly[i]:
		find_set([num], [i], poly)