import heapq
from typing import List
from heapq import heapify, heappush, heappop, heappushpop


# Traversal method to achieve array representation is Level Order

class MinHeap:
    def __init__(self):
        self.heap: List[int] = []

    @staticmethod
    def parent(index: int) -> int:
        return (index - 1) // 2

    @staticmethod
    def left(index: int) -> int:
        return (2 * index) + 1

    @staticmethod
    def right(index: int) -> int:
        return (2 * index) + 2

    def insert(self, val: int):
        heapq.heappush(self.heap, val)

    def delete(self, index: int):
        self.decrease(index, float("-inf"))
        self.extract_min()

    def decrease(self, index, new_val):
        self.heap[index] = new_val
        parent_index = self.parent(index)
        while index != 0 and self.heap[parent_index] > self.heap[index]:
            print(self.heap[index], self.heap[self.parent(index)])
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            print(self.heap[index], self.heap[self.parent(index)])
            index = parent_index
            parent_index = self.parent(index)

    def extract_min(self) -> int:
        return heapq.heappop(self.heap)

    def get_min(self) -> int:
        return self.heap[0]


if __name__ == '__main__':
    heap = MinHeap()
    heap.insert(3)
    heap.insert(2)
    # heap.delete(1)
    heap.insert(15)
    heap.insert(5)
    heap.insert(4)
    heap.insert(1)
    heap.insert(45)
    heap.decrease(6, 0)
    print(heap.get_min())
