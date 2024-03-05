from euler import SqrtNumber


def main():
	q = SqrtNumber(2, 1, 5)
	q *= q

	cur = SqrtNumber(2, 1, 5)

	res = []

	for _ in range(12):
		cur *= q
		print(cur)
		res += [cur.b]

	print(sum(res))


if __name__ == "__main__":
	main()
