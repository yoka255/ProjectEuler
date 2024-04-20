from functools import lru_cache
from itertools import product
from typing import Iterable


def get_btw(i: int, j: int, l: int) -> Iterable[int]:
    if i == j:
        return [i] * l
    if j - i == l:
        return list(range(i, j))
    if i - j == l:
        return list(range(i, j, -1))
    return []


def is_legal(board: tuple[tuple[bool]], start: tuple[int,int], end: tuple[int, int]) -> bool:
    if start == end:
        return False
    if board[end[0]][end[1]]:
        return False
    if start[1] == 100:
        return True
    l = max(abs(end[0] - start[0]), abs(end[1] - start[1]))

    iter_x, iter_y = get_btw(start[0], end[0], l), get_btw(start[1], end[1], l)

    if not iter_x or not iter_y:
        return True

    for cur_x, cur_y in zip(iter_x, iter_y):
        if not board[cur_x][cur_y]:
            return False
    return True


@lru_cache(maxsize=None)
def dp(cur: tuple[int,int], board: tuple[tuple[bool]]) -> int:
    n = len(board)
    res = 1
    for i, j in product(range(n), repeat=2):
        if is_legal(board, cur, (i, j)):
            new_board = [list(x) for x in board]
            new_board[i][j] = True
            new_board = tuple([tuple(x) for x in new_board])
            res += dp((i, j), new_board)
    # print(cur)
    # print(board)
    # print(res)
    return res


def main():
    n = 4
    board = tuple([tuple([False] * n) for _ in range(n)])
    print(dp((0, 100), board) - n * n - 1)


if __name__ == "__main__":
    main()
