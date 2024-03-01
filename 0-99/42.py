tri = set()

for n in range(1, 100):
	tri.add((n * (n + 1))//2)

res = 0

with open('p042_words.txt', 'r') as f:
	text = f.read()
	words = [x[1:-1] for x in text.split(",")]
	for w in words:
		if sum([ord(c) - ord('A') + 1 for c in w]) in tri:
			res += 1

print(res)
