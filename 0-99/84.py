from random import randint, shuffle

vis = [0]*40

for game in range(100):
	doubles = 0
	pos = 0
	CC = [0, 10] + [-1]*14
	CH = [0, 10, 11, 24, 39, 5, 'R', 'R', 'U', -3] + [-1] * 6

	shuffle(CC)
	shuffle(CH)
	# print(len(CC), CC)
	# print(len(CH), CH)
	# input()
	CCpos = [2, 17, 33]
	CHpos = [7, 22, 36]
	for turn in range(10000):
		vis[pos] += 1
		a = randint(1, 4)
		b = randint(1, 4)
		# print(pos, a, b)
		# input()
		if a == b:
			doubles += 1
		if doubles == 3:
			pos = 10
			doubles = 0
		else:
			if a != b:
				doubles = 0
			pos = (pos + a + b) % 40
			if pos == 30:
				pos = 10
			elif pos in CCpos:
				card = CC[0]
				CC = CC[1:] + [card]
				if card != -1:
					pos = card
			elif pos in CHpos:
				card = CH[0]
				CH = CH[1:] + [card]
				if isinstance(card, int) and card >= 0:
					pos = card
				elif card == -3:
					pos -= 3
				elif card == 'R':
					pos = (pos//5) * 5
					if pos % 2:
						pos += 10
					else:
						pos += 5
				elif card == 'U':
					if 12 <= pos < 28:
						pos = 28
					else:
						pos = 12
		pos = (pos + 40) % 40

a = [(vis[x], x) for x in range(40)]
a = sorted(a, reverse = True)
print(a[0], a[1], a[2], a[3], a[4])
print([a[i][0]/10**6 for i in range(5)])