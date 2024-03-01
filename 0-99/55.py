N = 10**4

def islych(n):
	for i in range(50):
		n = str(int(n) + int(n[::-1]))
		if n == n[::-1]:
			return False
	return True

cnt = 0
for n in range(1, N):
	if islych(str(n)):
		print(n)
		cnt += 1

print(cnt)