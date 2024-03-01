N = 100

nums = set()

for a in range(2, N+1):
	for b in range(2, N+1):
		nums.add(a**b)
print(len(nums))