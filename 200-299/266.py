def isPrime(n):
	x = 2
	while x * x <= n:
		if n % x == 0:
			return False
		x += 1
	return True


primes = []

for i in range(2, 190):
	if isPrime(i):
		primes += [i]

n = len(primes)

A = primes[:n//2]
B = primes[n//2:]

pA = []
pB = []

def findmul(i, mul, pX, X):
	if i == len(X):
		pX += [mul]
		return
	findmul(i+1, mul, pX, X)
	findmul(i+1, mul * X[i], pX, X)

findmul(0, 1, pA, A)
findmul(0, 1, pB, B)

print(len(pA))
print(len(pB))
print(len(A), len(B), n)

pA = sorted(pA)
pB = sorted(pB)

i = 0
j = len(pB) - 1
mul = 1
for p in primes:
	mul *= p

res = 0
while i < len(pA) and pA[i] * pA[i] < mul:
	while (pB[j ] * pA[i]) * (pB[j] * pA[i]) > mul:
		j-=1
	if pB[j] * pA[i] > res:
		res = pB[j] * pA[i]
	i += 1

print(res % (10**16))