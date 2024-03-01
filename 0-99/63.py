cnt = 0

for exp in range(1, 100):
	for i in range(1, 10):
		if len(str(i ** exp)) == exp:
			cnt += 1

print(cnt)