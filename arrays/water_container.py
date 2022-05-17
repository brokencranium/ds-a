from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = -1

        while left_pointer < right_pointer:
            area = (min(height[left_pointer], height[right_pointer]) *
                    (right_pointer - left_pointer)
                    )

            max_area = area if area > max_area else max_area

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area


if __name__ == '__main__':
    sol = Solution()
    result = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    assert result == 49
