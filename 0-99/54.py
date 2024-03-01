def win(me, opp):
	me.sort()
	opp.sort()
	if straight(me) and flush(me):
		if straight(opp) and flush(opp):
			return tiebreak(me, opp)
		return True
	if straight(opp) and flush(opp):
		return True
	print("not sf")
	if len(count(me)) > 0 and count(me)[0][0] == 4:
		if len(count(opp)) > 0 and count(opp)[0][0] == 4:
			return count(me)[0][1] > count(opp)[0][1] or (count(me)[0][1] == count(opp)[0][1] and tiebreak(me, opp))
		return True
	if len(count(opp)) and count(opp)[0] == 4:
		return False
	print("not 4")
	mc = count(me)
	oc = count(opp)
	print(oc, mc)
	if len(mc) > 1 and mc[1][0] == 3:
		if len(oc) > 1 and oc[1][0] == 3:
			return mc[1][1] > oc[1][1] or (mc[1][1] == oc[1][1] and mc[0][1] > oc[0][1])
		return True
	if len(oc) > 1 and oc[1][0] == 3:
		return False
	print("not fh")
	if flush(me):
		if flush(opp):
			return tiebreak(me, opp)
		return True
	if flush(opp):
		return False
	print("not flush")
	if straight(me):
		if straight(opp):
			return tiebreak(me, opp)
		return True
	if straight(opp):
		return False
	print("not straight")
	if len(mc) == 0:
		if len(oc) == 0:
			return tiebreak(me, opp)
		return False
	if len(oc) == 0:
		return True
	print("not high card")
	if mc[0][0] == 3:
		if oc[0][0] == 3:
			return mc[0][1] > oc[0][1] or (mc[0][1] == oc[0][1] and tiebreak(me, opp))
		return True
	if oc[0][0] == 3:
		return False

	if len(mc) > len(oc):
		return True
	if len(oc) > len(mc):
		return False
	if len(oc) > 1:
		return mc[1][1] > oc[1][1] or (mc[1][1] == oc[1][1] and mc[0][1] > oc[0][1]) or (mc[1][1] == oc[1][1] and mc[0][1] == oc[0][1] and tiebreak(me, opp))
	if len(oc) > 0:
		return mc[0][1] > oc[0][1] or (mc[0][1] == oc[0][1] and tiebreak(me, opp))
	return tiebreak(me, opp)

def tiebreak(me, opp):
	i = 4
	while 1:
		if me[i][0] > opp[i][0]:
			return True
		if me[i][0] < opp[i][0]:
			return False
		i -= 1
	print("ouch")

def straight(hand):
	for i in range(4):
		if hand[i+1][0] != hand[i][0] + 1:
			return False
	return True

def flush(hand):
	for i in range(4):
		if hand[i+1][1] != hand[i][1]:
			return False
	return True

def count(hand):
	arr = [0]*14
	for card in hand:
		arr[card[0]] += 1
	return sorted([(x, i) for i, x in enumerate(arr) if x > 1])

with open('p054_poker.txt', 'r') as f:
	dic = {'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}
	cnt = 0
	for i in range(1000):
		l = f.readline()
		l = l.split()
		me = []
		for x in l[:5]:
			if x[0].isdigit():
				me += [(int(x[0]) - 1, x[1])]
			else:
				me += [(dic[x[0]], x[1])]
		opp = []
		for x in l[5:]:
			if x[0].isdigit():
				opp += [(int(x[0]) - 1, x[1])]
			else:
				opp += [(dic[x[0]], x[1])]

		if win(me, opp):
			cnt += 1
			print(me, opp)
	print(cnt)