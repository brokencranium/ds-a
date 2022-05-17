import random
from typing import List, Optional
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for num in nums:
            if count := num_map.get(num):
                count += 1
            else:
                count = 1

            num_map[num] = count

        return heapq.nlargest(k, num_map, key=num_map.get)

    def dict_vals_sort(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for num in nums:
            if count := num_map.get(num):
                count += 1
            else:
                count = 1

            num_map[num] = count

        keys = list(num_map.keys())

        def quick_sort(keys: List[int]):
            if len(keys) < 2:
                return keys

            partition = keys[random.randint(0, len(keys) - 1)]

            low = []
            same = []
            high = []

            for key in keys:
                if num_map[key] == num_map[partition]:
                    same.append(key)
                elif num_map[key] < num_map[partition]:
                    low.append(key)
                else:
                    high.append(key)

            return quick_sort(low) + quick_sort(same) + quick_sort(high)

        sorted_keys = quick_sort(keys)

        for key in reversed(sorted_keys):
            print(key, num_map[key])


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    # print(Solution().topKFrequent(nums, 2))
    print(Solution().dict_vals_sort(nums, 2))
