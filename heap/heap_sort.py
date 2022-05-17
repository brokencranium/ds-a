from __future__ import annotations
from typing import List


class Heap:
    def __init__(self):
        self.heap: List = []

    def heapify_vv(self, input: List, index, max_len: int):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        left_val = input[left_index] if left_index <= max_len else float("inf")
        right_val = input[right_index] if right_index <= max_len else float("inf")
        parent_val = input[index]

        if left_val < right_val and left_val < parent_val:
            input[index], input[left_index] = input[left_index], input[index]
            self.heapify_vv(input, left_index, max_len)
        elif right_val < left_val and right_val < parent_val:
            input[index], input[right_index] = input[right_index], input[index]
            self.heapify_vv(input, right_index, max_len)

        print(input)

    def heap_sort(self, input):
        max_length = len(input) - 1
        for index in range(max_length // 2, -1, -1):
            self.heapify_vv(input, index, max_length)

        print(input)

        for index in range(max_length, 0, -1):
            input[0], input[index] = input[index], input[0]
            self.heapify_vv(input, 0, index-1)
            print(input[index])


if __name__ == '__main__':
    heap = Heap()

    arr = [9, 8, 5, 7, 3, 1, 4, 6, 2, 0]
    heap.heap_sort(arr)
