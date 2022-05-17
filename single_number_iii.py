# Given an integer array nums, in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that
# appear only once. You can return the answer in any order.
#
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
from typing import List


class Solution:
    @staticmethod
    def single_number(nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1)
        #
        # XOR all the numbers together
        # XOR all the numbers together again
        # XOR the result with the first number
        # XOR the result with the second number
        #
        # XORing two numbers will give you the number that is unique to each
        # of the two numbers

        xor = 0
        for num in nums:
            xor ^= num
        # Find the rightmost set bit
        print(bin(xor))
        rightmost_set_bit = xor & ~(xor - 1)
        print(bin(rightmost_set_bit))
        # Split the numbers into two groups
        # One group will have the rightmost set bit
        # The other group will have the rightmost set bit removed
        # XOR the two groups together
        # The result will be the unique number
        group_one = 0
        group_two = 0
        for num in nums:
            if num & rightmost_set_bit:
                group_one ^= num
            else:
                group_two ^= num
        print(group_one, group_two)
        return [group_one, group_two]


if __name__ == "__main__":
    s = Solution()
    print(s.single_number([1, 2, 1, 3, 2, 5]))
    print(s.single_number([1, 2, 1, 3, 2, 5, 5]))
