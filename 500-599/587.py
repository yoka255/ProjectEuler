from math import pi, sqrt, asin

def calc_ratio(n : int) -> float:
    a = 1/n
    r = (1 + a - sqrt(2) * sqrt(a)) / (1 + a ** 2)
#    print(r)
    s = 1/2 * a * r ** 2 
    s += (1-r) + asin(r-1) / 2 
    s += (r-1) * sqrt(1-(r-1) ** 2) / 2
#    print(s)
    return 4 * s / (4 - pi)

n = 1
while 1:
    if calc_ratio(n) < 0.001:
        break
    n += 1

print(n)