from typing import List, Optional


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total_units = 0
        current_val = 0

        for index, val in enumerate(height):
            if not stack and val <= 0:
                continue

            if stack and val >= stack[0]:
                for _ in range(len(stack) - 1):
                    current_val = stack.pop()
                    total_units += max(stack[0] - current_val, 0)
                stack.clear()

            stack.append(val)

        max_left = 0
        for index, val in enumerate(reversed(stack)):
            if index == 0 or index == len(stack) - 1:
                max_left = val
                continue

            if val >= max_left:
                max_left = val
                continue

            total_units += max(max_left - val, 0)

        return total_units

    def trap_pointers(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1

        left_max = height[left_index]
        right_max = height[right_index]

        total = 0

        while left_index < right_index:
            if height[left_index] <= height[right_index]:
                if height[left_index] < left_max:
                    total += left_max - height[left_index]
                else:
                    left_max = height[left_index]

                left_index += 1

            else:
                # height[right_index] < height[left_index]
                if height[right_index] < right_max:
                    total += right_max - height[right_index]
                else:
                    right_max = height[right_index]

                right_index -= 1

        return total


if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap_pointers([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # print(Solution().trap([4,2,3] ))
    result = {(j,k): False for k in range(4) for j in range(4)}