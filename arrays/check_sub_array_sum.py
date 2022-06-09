from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # ////// TC O(N) //////
        remainder = {0: -1}  # mapping remainder with last index
        total = 0

        for i, n in enumerate(nums):
            total += n
            rem = total % k
            if rem not in remainder:
                remainder[rem] = i
            elif i - remainder[rem] > 1:  # making sure that the subarray is of at least of len 2
                return True
        return False


if __name__ == '__main__':
    # inp = [23, 2, 4, 6, 7]
    # k = 6
    # sol = Solution()
    # assert sol.checkSubarraySum(inp, k)

    inp = [23, 2, 6, 4, 7]
    k = 6
    sol = Solution()
    assert sol.checkSubarraySum(inp, k)
