class Solution:
    def minPathSum(self, grid) -> int:
        """
        1. 分治（子问题）f(i,j) = min(f(i-1,j), f(i, j-1)) + a[i][j]
        2. 状态数组 dp[i][j]
        3. 状态方程
        """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue
                if i - 1 < 0:
                    grid[i][j] += grid[i][j - 1]
                elif j - 1 < 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


# 一行一行算记录能降一维
class Solution1:
    def minPathSum(self, grid):
        dp = [float('inf')] * (len(grid[0])+1)
        dp[1] = 0
        for row in grid:
            for idx, num in enumerate(row):
                dp[idx + 1] = min(dp[idx], dp[idx + 1]) + num
        return dp[-1]