import math

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
best = math.prod(primes)

def calc(ind):
	global best
	k = 6
	if len(ind) == k:
		# print(ind)
		# input()
		res = 1
		num = 1
		for i in range(1, k):
			for j in range(ind[i-1], ind[i]):
				res *= 2*(k - i)+1
				num *= primes[j] ** (k - i)
		
		if (res + 1) // 2 >= 4 * 10 ** 6:
			if num < best:
				print(ind)
				print(num)
				print(res)
				best = num
		return
	for i in range(ind[-1], len(primes) + 1):
		calc(ind + [i])

calc([0])
print(best)