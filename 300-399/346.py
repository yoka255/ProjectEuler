nums = set()

N = 10**12

for p in range(2, int(N ** 0.5)+1):
	x = 1 + p + p * p 
	while x < N:
		nums.add(x)
		x = x * p + 1 

nums.add(1)
#print(sorted([x for x in nums]))
print(sum(nums))
