from math import log, ceil

fib = [0,1, 1]

i = 3

while 1:
	fib += [fib[i-1] + fib[i-2]]
	if ceil(log(fib[i]) / log(10)) >= 1000:
		print(i)
		break
	i+=1
