def gcd(x, y):

	while(y):
		x, y = y, x % y

	return x


count = []
for _ in range(1000):
	count += [[]]

for x in range(1000):
	for y in range(1000):
		z = (x*x + 5 * x * y + 3 * y * y) ** 0.5
		if gcd(x,y) == 1 and z - int(z) < 10**-5 and int(z)<1000:
			count[int(z)] += [(x,y)]

for z in range(1000):
	if count[z]:
		print(z, count[z])

for u in range(10):
	for v in range(10):
		if gcd(u,v) == 1:
			x = 6 * u * u + 6 * u * v - 3 * v * v 
			y = - u * u + 2 * u * v + 8 * v * v 
			z = 3 * (u * u + 5 * u * v + 3 * v * v)
			if z > 1 and x > 1 and z > 1:
				print(u, v, ":", x,y,z)

# x=uu-3vv
# y=2uv+5vv 
# z =uu+5uv+3vv