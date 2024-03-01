res = 0

for m in range(2, 16):
	s = sum([k for k in range(1, m+1)])
	x = m/s
	tmpres = 1
	for j in range(1, m+1):
		tmpres *= (x * j) ** j
	res += int(tmpres)
	print(m, tmpres)
print(res)
