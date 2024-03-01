def bouncy(n):
	k = str(n)
	cond = True
	for x in range(len(k) - 1):
		if k[x] > k[x+1]:
			cond = False
	if cond:
		return False
	cond = True
	for x in range(len(k) - 1):
		if k[x] < k[x+1]:
			cond = False
	if cond:
		return False
	return True

count = 0
n = 1
while 1:
	n += 1
	if bouncy(n):
		count += 1
	if 100*count == 99 * n:
		print(n)
		break