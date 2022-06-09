from typing import List
from collections import Counter, defaultdict
from itertools import accumulate


# Input: nums = [1,2,3], k = 3
# Output: 2

class Solution:

    @staticmethod
    def sub_array_brute(nums: List[int], k: int) -> int:
        count = 0
        for index, inum in enumerate(nums):
            total = 0
            for jnum in nums[index:]:
                total += jnum
                count = count + 1 if total == k else count

        print(count)
        return count

    @staticmethod
    def sub_array(nums: List[int], k: int) -> int:
        # Intuition is, if the accumulated value - k is already in dict, it means
        # the current accumulated value to a point in the previous elements list is equal to k
        c, res = Counter((0,)), 0
        for accum in accumulate(nums):
            res += c[accum - k]
            c[accum] += 1

        print(res)
        return res

    @staticmethod
    def sub_array_vv(nums: List[int], k: int) -> int:
        # Does not work
        acc = defaultdict(int)
        counter = 0
        for prefix_sum in accumulate(nums):
            diff = prefix_sum - k

            counter = counter + 1 if prefix_sum == k else counter
            counter = counter + 1 if diff in acc else counter

            if prefix_sum == k:
                acc[prefix_sum] += 1

            acc[prefix_sum] += 1

        print(counter)
        print(acc)
        return counter


if __name__ == '__main__':
    sol = Solution()
    # assert 2 == sol.sub_array_brute([1, 1, 1], 2)
    # assert 3 == sol.sub_array_brute([1, -1, 0], 0)
    # assert 3 == sol.sub_array([1, -1, 0], 0)
    # assert 2 == sol.sub_array([1, 1, 1], 2)
    assert 4 == sol.sub_array([3, 4, 7, 2, -3, 1, 4, 2], 7)
    # assert 2 == sol.sub_array([1, 2, 3], 3)
    # assert 6 == sol.sub_array([0, 0, 0], 0)
    # assert 55 == sol.sub_array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
