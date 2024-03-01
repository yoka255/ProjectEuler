import sage.all as S
from tqdm import tqdm

digs = {"0":{0,1,2,4,5,6},
        "1":{2,5},
        "2":{0,2,3,4,6},
        "3":{0,2,3,5,6},
        "4":{1,2,3,5},
        "5":{0,1,3,5,6},
        "6":{0,1,3,4,5,6},
        "7":{0,1,2,5},
        "8":{0,1,2,3,4,5,6},
        "9":{0,1,2,3,5,6}
 }

def digital_root_price(n):
    max_price = 0
    sam_price = 0
    while len(str(n)) > 1:
        next = sum([int(x) for x in str(n)])
        x = str(n)[::-1]
        y = str(next)[::-1]
        for i in range(len(x)):
            sam_price += len(digs[x[i]])
            if i >= len(y):
                max_price += len(digs[x[i]])
            else:
                sam_price += len(digs[y[i]])
                max_price += len(digs[x[i]] ^ digs[y[i]])
        n = next
    
#    print(sam_price, max_price)
    return sam_price - max_price

res = 0

#print(digital_root_price(137))

for n in tqdm(range(10 ** 7, 2 * 10 ** 7)):
    if S.is_prime(n):
        res += digital_root_price(n)

print(res)