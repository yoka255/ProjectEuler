cnt = {}
encounter = {}

n = 0

while 1:
	toad = ''.join(sorted(str(n**3)))
	if toad not in encounter:
		encounter[toad] = n**3
		cnt[toad] = 1
	else:
		cnt[toad] += 1
		if cnt[toad] == 5:
			print(encounter[toad])
			quit()
	n += 1