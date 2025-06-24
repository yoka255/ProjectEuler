import json

p = 1_000_000_007
Fp = GF(p)

with open("matrix.json", "r") as f:
    a = json.load(f)

M = Matrix(Fp, len(a), len(a), sparse=True)
for i in range(len(a)):
    for j in a[i]:
        M[i, j] += 1

with open("vector.json", "r") as f:
    b = json.load(f)

v = Matrix(Fp, len(a), 1, sparse=True)
for i in b:
    v[i] = 1

with open("indexs.json", "r") as f:
    c = json.load(f)

u = Matrix(Fp, len(a), 1)
for i in c:
    u[i] = 1

# def out_vector(vv, filename):
#     with open(filename, "w") as f:
#         f.write("\n".join([str(vv[i,0]) for i in range(vv.dimensions()[0])]))

# how to calculate T(5)
x = (u.T * (M*(M*(M*(M * v)))))[0,0]-1