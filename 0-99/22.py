names = []
with open('names.txt', 'r') as f:
	names = f.read().split(',')

names = sorted(names)

print(len(names))

res = 0
for i, name in enumerate(names):
	score = 0
	name = name[1:-1].lower()
#	print(name)
	for char in name:
		score += ord(char) - ord('a') + 1
	res += score * (i+1)

print(res)