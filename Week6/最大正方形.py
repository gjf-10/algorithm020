from copy import deepcopy


class Solution:
    def maximalSquare(self, matrix) -> int:
        m, n, max_ = len(matrix), len(matrix[0]), 0
        if m < 2 or n < 2:
            for i in matrix:
                if '1' in i:
                    return 1
            return 0
        dp = deepcopy(matrix)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i-1][j-1] == matrix[i-1][j] == matrix[i][j-1] == matrix[i][j] == '1':
                    temp = min(int(dp[i-1][j-1]),int(dp[i-1][j]), int(dp[i][j-1]))
                    dp[i][j] = temp + 1
                    max_ = max(dp[i][j], max_)
                elif matrix[i-1][j-1] == '1' or matrix[i-1][j] == '1' or matrix[i][j-1] == '1':
                    max_ = max(1, max_)
        return max_ * max_