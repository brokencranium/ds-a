"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that 
they add up to a specific target number. 

Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2
The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space. 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

import bisect


def two_num_sorted(numbers: list[int], target: int) -> list[int] | None:
    max_index = len(numbers) - 1
    curr_index = 0

    while True:
        if numbers[curr_index] + numbers[max_index] == target:
            return [curr_index, max_index]
        elif numbers[curr_index] + numbers[max_index] > target:
            max_index -= 1
        else:
            curr_index += 1

        if curr_index > max_index:
            break

    return None
    # print(i, j, numbers[i] + numbers[j])


def two_num_sorted_binary(numbers: list[int], target: int) -> list[int] | None:
    left_index_start = 0
    left_index_end = len(numbers) - 2
    right_index_start = 1
    right_index_end = len(numbers) - 1

    while True:
        if numbers[left_index_start] + numbers[right_index_end] == target:
            return [left_index_start + 1, right_index_end + 1]
        elif numbers[left_index_start] + numbers[right_index_end] > target:

    pass


if __name__ == "__main__":
    print(two_num_sorted([2, 3, 4], 6))
