# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

from typing import List


class Solution:

    def median_arrays(self, num1: List[int], num2: List[int]) -> float:
        """[x1, x2, x3, x4, x5, x6] [y1, y2, y3, y4, y5, y6, y7]
            xa <= yb and ya >= xb
            Gaol is to keep the total left group count to be equal to the median value
             """
        num1, num2 = (num1, num2) if len(num1) <= len(num2) else (num2, num1)

        total_len = len(num1) + len(num2)

        num1_index = len(num1) // 2 - 1
        num2_index = len(num2) // 2 - 1

        num1_left = num1[num1_index]
        num1_right = num1[num1_index]

        num2_left = num2[num2_index]
        num2_right = num2[num2_index]

        while num1_left > num2_right or num2_left > num1_right:
            num1_left = num1[num1_index] if num1_index >= 0 else float("-inf")
            num1_right = num1[num1_index + 1] if num1_index < len(num1) else float("inf")

            num2_left = num2[num2_index] if num2_index >= 0 else float("-inf")
            num2_right = num2[num2_index + 1] if num1_index < len(num1) else float("inf")

            if num1_left > num2_right:
                num1_index -= 1
                num2_index += 1

            if num2_left > num1_right:
                num2_index -= 1
                num1_index += 1

        if total_len % 2 == 0:
            median = (max(num1_left, num2_left) + min(num2_right + num2_right)) / 2
        else:
            median = max(num1_left, num2_left)

        return median


if __name__ == '__main__':
    sol = Solution()
    # print(sol.median_arrays([0, 2, 4, 6, 8], [1, 3, 5, 7, 9, 11]))
    print(sol.median_arrays([0, 1, 1, 1, 1], [1, 3, 5, 7, 9, 11]))
