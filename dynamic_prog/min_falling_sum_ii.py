# Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.
# A falling path with non-zero shifts is a choice of exactly one element from each row of grid such
# that no two elements chosen in adjacent rows are in the same column.
from typing import List


class Solution:
    @staticmethod
    def min_falling_path_sum(self, grid: List[List[int]]) -> int:
        # Time: O(n^2)
        # Space: O(n)
        # DP solution
        # dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + grid[i][j]
        # test_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = len(grid)
        print(n)
        print(grid)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        print(dp)
        for i in range(n):
            dp[i][0] = dp[i][n - 1] = grid[i][0] + grid[i][n - 1]
            print(i, dp[i][0])
            for j in range(1, n - 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + grid[i][j]
                print(j, dp[i][j])
        return min(dp[n - 1])


if __name__ == '__main__':
    test_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution.min_falling_path_sum(Solution, test_grid))
    # test_grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    # print(Solution.min_falling_path_sum(Solution, test_grid))
