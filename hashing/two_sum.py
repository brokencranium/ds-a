# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            difference = target - num

            if num in hashmap:
                return [hashmap[num], index]

            hashmap[difference] = index


if __name__ == '__main__':
    sol = Solution()
    sol.twoSum([2, 7, 11, 15], 9)
