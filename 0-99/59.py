from tqdm import tqdm

def pos(a, b, c, asc):
	p = [a, b, c]
	ok = [x for x in range(ord('a'), ord('z') + 1)]
	ok += [x for x in range(ord('A'), ord('Z') + 1)]
	ok += [ord(','), ord('\"'), ord(' '), ord('\'')]
	for i, let in enumerate(asc):
		if p[i%3] ^ let not in ok:
			print(chr(p[i%3] ^ let))
			return False
	return True


asc = []
words = set()

with open('p059_cipher.txt', 'r') as f:
	asc = [int(x) for x in f.read().split(',')]
with open('wordlist.txt', 'r') as f:
	for x in f.read().split():
		words.add(x)

best = 0
bestp = []
for a in tqdm(range(ord('a'), ord('z') + 1)):
	for b in range(ord('a'), ord('z') + 1):
		for c in range(ord('a'), ord('z') + 1):
			cnt = 0
			p = [a, b, c]
			# print(chr(a), chr(b), chr(c))
			res = "".join([chr(p[i%3] ^ let) for i, let in enumerate(asc)])
			for i in range(len(res)):
				for j in range(3,10):
					if res[i:i+j] in words:
						# print(p, res[i:i+j])
						# input()
						cnt += 1

			if cnt > best:
				best = cnt
				bestp = p

print(best, bestp)
res = "".join([chr(bestp[i%3] ^ let) for i, let in enumerate(asc)])
num=0
print(res)
for char in res:
	num += ord(char)
print(num)