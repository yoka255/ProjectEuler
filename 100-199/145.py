cnt = 0

k = 9

for i in range(1, k+1):
	if i % 2 == 0:
		n = i//2
		cnt += 20 * 30 ** (n-1)
	if i % 4 == 3:
		n = i // 4
		cnt += 5 * 20 ** (n + 1) * 25 ** n
print(cnt)