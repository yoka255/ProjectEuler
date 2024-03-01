from euler import chinese_remainder

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
#primes = [2, 7, 13]
res = 0
modulos = [0] * len(primes)

def guess(ind):
    global res
    global primes
    if ind == len(primes):
        res += chinese_remainder(primes, modulos)
        return
    for i in range(primes[ind]):
        if i ** 3 % primes[ind] == 1:
            modulos[ind] = i
            guess(ind + 1)

guess(0)
print(res - 1)