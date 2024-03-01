from typing import Type

class Vector:
    def __init__(self, a : float, b : float):
        self.val = (a, b)
    
    def scalar_mul(self, a : float) -> "Vector":
        return Vector(self.val[0] * a, self.val[1] * a)
    
    def __mul__(self, other : "Vector") -> float:
        return self.val[0] * other.val[0] + self.val[1] * other.val[1]

    def __add__(self, other : "Vector") -> "Vector":
        return Vector(self.val[0] + other.val[0], self.val[1] + other.val[1])

    def __sub__(self, other : "Vector") -> "Vector":
        return self + other.scalar_mul(-1)
    
    def __str__(self) -> str:
        return f"({self.val[0]},{self.val[1]})"

def main():
    cnt = 0
    v = Vector(1.4, -9.6) - Vector(0, 10.1)
    last = Vector(0, 10.1)
    curr = Vector(1.4, -9.6)
    while True:
        if -0.01 <= curr.val[0] <= 0.01 and curr.val[1] > 0:
            break
#        print(curr)
        cnt += 1
        norm = Vector(-4 * curr.val[0], -curr.val[1])
        hit = curr - last
#        print(hit)
        reflect = hit - norm.scalar_mul((2 * (hit * norm)) / (norm * norm))
#        print(norm, 2 * (hit * norm) / (norm * norm))
#        print(norm.scalar_mul(2 * (hit * norm) / (norm * norm)))
        m = reflect.val[1] / reflect.val[0]
        b = curr.val[1] - m * curr.val[0]
#        print(m, b)
        x = (- m * b + (- 4 * b ** 2 + 400 + 100 * m ** 2) ** 0.5) / (4 + m ** 2)
        if abs(x - curr.val[0]) < 10 ** -6:
            x = (- m * b - (- 4 * b ** 2 + 400 + 100 * m ** 2) ** 0.5) / (4 + m ** 2)
        y = m * x + b
        next = Vector(x, y)
        last, curr = curr, next
    print(cnt)


if __name__ == "__main__":
    main()
