def findcyc(n):
	done = []
	curr = 1
	while 1:
		if not curr:
			return 0
		if curr in done:
			for i in range(len(done)):
				if done[i] == curr:
					return len(done) - i
		done += [curr]
		curr = (curr * 10) % n

best = 2
for d in range(3, 1000):
	if findcyc(d) > findcyc(best):
		print(d, findcyc(d))
		best = d