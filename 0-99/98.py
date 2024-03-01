from euler import *

def work(w, t, k):
	n = len(w)
	if n != len(t) or n != len(k):
		return "2"
	for i in range(n):
		for j in range(n):
			if w[i] != w[j] and k[i] == k[j]:
				return "2"
			if w[i] == w[j] and k[i] != k[j]:
				return "2"
	ret = ""
	for i in range(n):
		for j in range(n):
			if t[i] == w[j]:
				ret += k[j]
				break
	return ret


words = []

with open('p098_words.txt', 'r') as f:
	words = [w[1:-1] for w in f.read().split(',')]

res = 0

for w in words:
	for k in words:
		if w != k and sorted([c for c in w]) == sorted([c for c in k]):
			j = 1
			while len(str(j ** 2)) <= len(w):
				j+=1
				if len(str(j**2)) == len(w):
					tmp = work(w, k, str(j**2))
					if issquare(int(tmp)) and len(str(j ** 2)) == len(str(int(tmp))):
						print(w, k, j ** 2, tmp)
						res = max(res, int(tmp))


print(res)