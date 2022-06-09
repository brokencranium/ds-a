import heapq
from heapq import heappush, heappop
import heap
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


def find_kth_largest(nums: List[int], k: int) -> int:
    nums = [num * -1 for num in nums]
    heapq.heapify(nums)

    while k > 1:
        heapq.heappop(nums)
        k -= 1

    return heapq.heappop(nums) * -1


if __name__ == '__main__':
    # test = [1, 35, 2, 3, 4, 22, 21, 5, 6, 10, 7, 8, 9]
    # heap = MaxHeap()
    # [heap.insert(val) for val in test]
    # result = heap.extract_k(3)
    # print(result)
    # heapq.heapify()
    test = [3, 2, 1, 5, 6, 4]
    k = 2
    print(find_kth_largest(test, k))
