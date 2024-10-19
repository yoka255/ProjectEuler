from typing import Callable, Generic, List, Tuple, Any, TypeVar
from abc import ABCMeta, abstractmethod
import heapq


class DSU:
    def __init__(self):
        self.size: List[int] = []
        self.parent: List[int] = []

    def get_root(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.get_root(self.parent[x])
        return self.parent[x]

    def join(self, x: int, y: int) -> None:
        x = self.get_root(x)
        y = self.get_root(y)
        if x == y:
            return

        if self.size[x] < self.size[y]:
            x, y = y, x

        self.size[x] += self.size[y]
        self.parent[y] = x


T = TypeVar("T")


class Heap(Generic[T]):
    def __init__(self, initial_list: List[T] = []) -> None:
        self.heap = initial_list
        heapq.heapify(self.heap)

    def pop(self) -> T:
        return heapq.heappop(self.heap)

    def top(self) -> T:
        return self.heap[0]

    def push(self, val: T) -> None:
        heapq.heappush(self.heap, val)

    def __len__(self) -> int:
        return len(self.heap)

    def __str__(self) -> str:
        return str(self.heap)