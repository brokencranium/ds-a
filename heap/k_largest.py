from heapq import heappush, heappop
from typing import List
from collections import deque


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val: int):
        heappush(self.heap, val * -1)

    def extract(self):
        return heappop(self.heap)

    def extract_k(self, k) -> List[int]:
        result = []
        for _ in range(k):
            result.append(self.extract() * -1)
        return result


if __name__ == '__main__':
    test = [1, 35, 2, 3, 4, 22, 21, 5, 6, 10, 7, 8, 9]
    heap = MaxHeap()
    [heap.insert(val) for val in test]
    result = heap.extract_k(3)
    print(result)
