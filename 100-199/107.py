import heapq

n = 40
par = [None]*n

def parent(u):
	if u == par[u]:
		return u
	par[u] = parent(par[u])
	return par[u]

def join(x, y):
	u = par[x]
	v = par[y]
	par[u] = v

for i in range(n):
	par[i] = i

f = open('network.txt', 'r')

heap = []


for i in range(n):
	line = f.readline()
	t = line.split(",")
	for j in range(n):
		if not t[j] in ["-", "-\n"]:
			heapq.heappush(heap, (int(t[j]), i, j))

res = 0

while len(heap):
	d, u, v = heapq.heappop(heap)
	if u > v:
		print(d, u, v, res)
		if parent(u) != parent(v):
			join(u, v)
		else:
			res += d

print(res)
