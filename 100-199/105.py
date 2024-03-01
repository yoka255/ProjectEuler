from itertools import combinations

sets = []

with open("0105_sets.txt", "r") as f:
    for line in f.readlines():
        sets.append(sorted([int(x) for x in line.split(",")]))

res = 0

for s in sets:
    if len(s) != len(set(s)):
        continue
    if 0 in s:
        continue
    legit = True
    for x in range(2, len(s)):
        if sum(s[:x]) <= sum(s[-x+1:]):
            legit = False
    optsums = set()
    for x in range(1, len(s)):
        for tup in combinations(s, x):
            if sum(tup) in optsums:
                legit = False
                break
            optsums.add(sum(tup))
    if not legit:
        continue
    res += sum(s)

print(res)