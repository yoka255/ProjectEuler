from itertools import combinations
from tqdm import tqdm


def is_square(x: int) -> bool:
    s = int(x ** 0.5)
    return s * s == x


def main():
    for c, b, a in combinations(range(1, 1000), 3):
        if (a + b + c) % 2 == 0 and is_square(a * a - b * b) and is_square(a * a - c * c) and is_square(b * b - c * c):
            print(a, b, c)
            print((a * a +  b * b - c * c) // 2, (a * a - b * b + c * c) // 2, (-a * a +  b * b + c * c) // 2)
            print((a * a + b * b + c * c) / 2)


if __name__ == "__main__":
    main()
