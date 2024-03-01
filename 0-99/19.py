days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
curr = 3

res = 0

for year in range(1, 101):
	print(year, curr)
	for month in range(12):
		if curr == 1:
			res += 1
		curr += days[month]
		if month == 1 and year % 4 == 0:
			curr += 1
		curr %= 7

print(res)
