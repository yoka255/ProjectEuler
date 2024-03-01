from euler import *

ps = [1, 2, 3, 5, 7, 11, 13, 17]

def buildnum(num):
	if len(num) == 10 and ispan0(num):
		return int(num)
	elif len(num) == 10:
		return 0

	res = 0
	i = 9 - len(num)
	for d in range(10):
		if int(str(d) + num[:2]) % ps[i] == 0:
			res += buildnum(str(d) + num)
	return res

count = 0
for i in tqdm(range(10, 100)):
	count += buildnum(str(i))
print(count)