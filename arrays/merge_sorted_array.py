# https://leetcode.com/problems/merge-sorted-array/
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be
# merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

from typing import List


class Solution:
    def merge_v1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = 0
        index2 = 0
        total = m + n
        # [1, 2, 3] [2, 5, 6]
        del nums1[m:]
        del nums2[n:]

        if m == 0:
            nums1.extend(nums2)
            return

        if n == 0:
            return

        while len(nums1) < total:
            if index1 < m and index2 < n and nums1[index1] < nums2[index2]:
                index1 += 1
            elif index1 < m and index2 < n and nums1[index1] >= nums2[index2]:
                nums1.insert(index1, nums2[index2])
                index2 += 1
                m += 1
            elif index2 < n and nums1[-1] > nums2[index2]:

                nums1.insert(-1, nums2[index2])
                index1 += 1
                index2 += 1
            elif index2 < n and nums1[-1] <= nums2[index2]:
                nums1.append(nums2[index2])
                index1 += 1
                index2 += 1

    def merge_v2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

    def merge_v3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n == 0:
            return

        if m == 0 and n > 0:
            nums1[0] = nums2[0]
            return

        index1 = index2 = 0 
        for index in range(m):
            if nums2[index2] < nums1[index1]:
                nums1[index1 + 1 :] = nums1[index1:n]
                nums1[index] = nums2[index]
                n -= 1
            else: 
                u += 1


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 5, 8, 0, 0, 0, 0, 0]
    m = 3
    nums2 = [-1, 2, 2, 4, 6]
    n = 5
    sol.merge_v3(nums1, m, nums2, n)
    print(nums1, [-1, 1, 2, 2, 5, 0, 0, 0])
    assert nums1 == [-1, 1, 2, 2, 5, 0, 0, 0]

    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    # sol.merge_v1(nums1, m, nums2, n)
    # print(nums1)
    # # #
    # nums1 = [1]
    # m = 1
    # nums2 = []
    # n = 0
    # sol.merge_v1(nums1, m, nums2, n)
    # print(nums1)
    # # # #
    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1
    # sol.merge_v1(nums1, m, nums2, n)
    # print(nums1)
    # # # #
    # nums1 = [4, 0, 0, 0, 0, 0]
    # m = 1
    # nums2 = [1, 2, 3, 5, 6]
    # n = 5
    # sol.merge_v1(nums1, m, nums2, n)
    # print(nums1)
    # ###
    # nums1 = [2, 0]
    # nums2 = [1]
    # m = 1
    # n = 1
    # sol.merge_v1(nums1, m, nums2, n)
    # print(nums1)
