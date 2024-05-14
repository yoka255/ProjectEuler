import numpy as np
from tqdm import tqdm
import random
from functools import reduce
from typing import Tuple, List, Callable
from math import gcd
import string


class SqrtNumber:

	def __init__(self, a: int, b: int, p: int):
		self.a = a
		self.b = b
		self.p = p

	def __add__(self, other: "SqrtNumber") -> "SqrtNumber":
		assert self.p == other.p
		return SqrtNumber(self.a + other.a, self.b + other.b, self.p)

	def __mul__(self, other: "SqrtNumber") -> "SqrtNumber":
		assert self.p == other.p
		return SqrtNumber(self.a * other.a + self.b * other.b * self.p, self.a * other.b + self.b * other.a, self.p)

	def __sub__(self, other: "SqrtNumber") -> "SqrtNumber":
		assert self.p == other.p
		return SqrtNumber(self.a - other.a, self.b - other.b, self.p)

	def __str__(self) -> str:
		return f"{self.a} + {self.b} * sqrt({self.p})"


class Fraction:

	def __init__(self, a: int, b: int = 1):
		if b == 0:
			raise ZeroDivisionError("Tried to create Fraction object with denominator 0")
		g = gcd(a, b)
		self.a = a // g
		self.b = b // g
		if self.b < 0:
			self.a *= -1
			self.b *= -1

	@staticmethod
	def convert_to_fraction(x: "Fraction | int") -> "Fraction":
		if isinstance(x, Fraction):
			return x
		if isinstance(x, int):
			return Fraction(x)
		raise NotImplementedError("Arithmetic operations between those types are not defined")

	@staticmethod
	def use_conversion(func: Callable[["Fraction", "Fraction"], "Fraction"]):
		def wrapped(a: "Fraction", b: "Fraction | int") -> "Fraction":
			return func(a, Fraction.convert_to_fraction(b))
		return wrapped

	@use_conversion
	def __add__(self: "Fraction", other: "Fraction") -> "Fraction":
		return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)

	@use_conversion
	def __radd__(self: "Fraction", other: "Fraction") -> "Fraction":
		return other + self

	@use_conversion
	def __mul__(self: "Fraction", other: "Fraction") -> "Fraction":
		return Fraction(self.a * other.a, self.b * other.b)
	
	@use_conversion
	def __rmul__(self: "Fraction", other: "Fraction") -> "Fraction":
		return other * self
	
	@use_conversion
	def __sub__(self: "Fraction", other: "Fraction") -> "Fraction":
		return self + other * (-1)

	@use_conversion
	def __rsub__(self: "Fraction", other: "Fraction") -> "Fraction":
		return other - self
	
	@use_conversion
	def __truediv__(self: "Fraction", other: "Fraction") -> "Fraction":
		return self * Fraction(other.b, other.a)

	@use_conversion
	def __rtruediv__(self: "Fraction", other: "Fraction") -> "Fraction":
		return other / self

	def __str__(self) -> str:
		return f"{self.a} / {self.b}"

	def __repr__(self) -> str:
		return f"{self.a} / {self.b}"

	def __eq__(self, other: "Fraction") -> bool:
		return (self.a, self.b) == (other.a, other.b)

	def __hash__(self) -> int:
		return hash((self.a, self.b))


def sieve(N: int) -> List[int]:
	print("Sieving")
	arr = [1] * N
	for i in tqdm(range(2, N)):
		if arr[i]:
			for j in range(2*i, N, i):
				arr[j] = 0
	print("Done sieving")
	arr[0] = 0
	arr[1] = 0
	return arr


def totient(N: int) -> List[int]:
	print("Calculating Euler totient function")
	arr = list(range(N))
	for i in tqdm(range(2, N)):
		if arr[i] == i:
			for j in range(i, N, i):
				arr[j] = (arr[j] // i) * (i - 1)
	print("Done calculating")
	arr[0] = 0
	arr[1] = 0
	return arr


def calc_divisors(N: int) -> List[int]:
	print("Calculating prime divisors")
	arr = list(range(N))
	for i in tqdm(range(2, N)):
		if arr[i] == i:
			for j in range(2*i, N, i):
				arr[j] = i
	print("Done calculating")
	arr[0] = 0
	arr[1] = 0
	return arr


def digsum(n):
	if n < 10:
		return n
	return n % 10 + digsum(n // 10)


def euclid(a : int, b : int) -> Tuple[int, int, int]:
	# returns g, x, y such that ax + by = g
	if b == 0:
		return (a, 1, 0)
	if a < b:
		g, x, y = euclid(b, a)
		return (g, y, x)
	g, x, y = euclid(b, a%b)
	return (g, y, x - y * (a // b))


def lcm(a, b):
	return a * b // gcd(a, b)


def inv_mod(a : int, n : int) -> int:
	return euclid(a, n)[1]


def miller_rabin(n: int, k: int = 100) -> bool:
	if n in [2, 3]:
		return True
	if n in [0, 1]:
		return False
	if n % 2 == 0:
		return False
	r, s = 0, n - 1
	while s % 2 == 0:
		r += 1
		s //= 2
	for _ in range(k):
		a = random.randrange(2, n - 1)
		x = pow(a, s, n)
		if x == 1 or x == n - 1:
			continue
		for _ in range(r-1):
			if x ** 2 == 1:
				break
			x = x ** 2
			x %= n
		if x not in [1, n-1]:
			return False
	return True


def is_prime(n: int) -> bool:
	return miller_rabin(n, 100)


def chinese_remainder(m : list, a : list) -> int:
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * inv_mod(p, n_i) * p
    return sum % prod


def root(n : int, root : int) -> int:
    l,r = (0,n)
    while l < r:
        m = (l + r) // 2
        if pow(m, root) == n:
            return m
        elif pow(m, root) > n:
            r = m - 1
        else:
            l = m + 1
    return -1


def get_all_primes(N: int):
	s = sieve(N)
	return [x for x in range(N) if s[x]]


def to_string_base(n: int, b: int) -> str:
	DIGITS_STRING = string.digits + "abcdef"
	assert(b <= len(DIGITS_STRING))

	def to_string_base_inner(n: int, b: int) -> str:
		return (to_string_base_inner(n // b, b) if n >= b else "") + DIGITS_STRING[n % b]

	return to_string_base_inner(n, b)
