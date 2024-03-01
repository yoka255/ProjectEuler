def calc(s):
	res = 0
	t = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	i = 0
	while i < len(s):
		if i < len(s)-1 and t[s[i+1]] > t[s[i]]:
			res -= t[s[i]]
		else:
			res += t[s[i]]
		i += 1
	return res

def romanify(n):
	res = ""
	while n >= 1000:
		res += 'M'
		n -= 1000
	if n >= 900:
		res += 'CM'
		n -= 900
	
	if n >= 500:
		res += 'D'
		n -= 500
	if n >= 400:
		res += 'CD'
		n -= 400
	
	while n >= 100:
		res += 'C'
		n -= 100
	if n >= 90:
		res += 'XC'
		n -= 90

	if n >= 50:
		res += 'L'
		n -= 50
	if n >= 40:
		res += 'XL'
		n -= 40

	while n >= 10:
		res += 'X'
		n -= 10
	if n >= 9:
		res += 'IX'
		n -= 9

	if n >= 5:
		res += 'V'
		n -= 5
	if n >= 4:
		res += 'IV'
		n -= 4
	while n >= 1:
		res += 'I'
		n -= 1
	return res


res = 0

with open('p089_roman.txt') as f:
	for num in f.readlines():
		if num[-1] == '\n':
			num = num[:-1]
		newnum = romanify(calc(num))

		res += len(num) - len(newnum)
		# print(num, newnum, len(num) - len(newnum))
		# input()


print(res)