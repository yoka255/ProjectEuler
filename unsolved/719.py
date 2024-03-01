from tqdm import tqdm

def can_reach(s, i, target):
	if target == 0 and i == len(s):
		return True
	if target < 0:
		return False
	for j in range(i+1, len(s) + 1):
		if can_reach(s, j, target - int(s[i:j])):
			return True
	return False


N = 10 ** 12
res = 0
for n in tqdm(range(2, int(N ** 0.5) + 1)):
	if can_reach(str(n ** 2), 0, n):
		res += n ** 2
print(res)
