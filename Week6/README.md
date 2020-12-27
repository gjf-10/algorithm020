学习笔记



~~~python
最大子序列和：

class Solution:
    def maxSubArray(self, nums) -> int:
        """
        1. 分治 f(n) = max(f(n-1), 0) + a[n]
        2. 状态数组 max_
        3. dp 方程
        """
        dp = [nums[0]] + [0]*(len(nums)-1)
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(0, dp[i-1])
        return max(dp)


class Solution1:
    def maxSubArray(self, nums):
        max_so_far = curr_so_far = -float('inf')
        for i in range(len(nums)):
            curr_so_far += nums[i]
            curr_so_far = max(curr_so_far, nums[i])
            max_so_far = max(max_so_far, curr_so_far)
        return max_so_far
    
扩展：乘积最大的子序列
~~~

~~~python
# 三角形最小路径和
"""
1. 递归：n层：left or right: 2^n (记忆化递归)
2. DP
    a. 重复性 (分治) problem(i,j) = min(sub(i+1, j) sub(i+1, j+1)) + a(i,j)
    b. 定义状态数组 f[i,j]
    c. DP 方程 f[i,j] = min(f[i+1,j], f[i+1, j+1]) +a[i,j]

"""
# 递归
class Solution:
    def minimumTotal(self, triangle):
        res = float("inf")
        def divide(level, s, i):
            nonlocal res
            if level == len(triangle)-1:
                res = min(res, s)
                return
            if i <= len(triangle[level]):
                divide(level+1, s + triangle[level+1][i], i)
                divide(level+1, s + triangle[level+1][i+1], i+1)
        divide(0, triangle[0][0], 0)
        return res

# 记忆化递归
class Solution1:
    def minimumTotal(self, triangle):
        res = float('inf')
        memory = [[res]*len(triangle) for _ in range(len(triangle))]
        def divide(level, j):
            if level == len(triangle):
                return 0
            if memory[level][j] != float('inf'):
                return memory[level][j]
            memory[level][j] = min(divide(level + 1, j), divide(level + 1, j + 1)) + triangle[level][j]
            return memory[level][j]
        return divide(0, 0)

# 动态规划
class Solution2:
    def minmumTotal(self, triangle):
        dp = triangle
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]


# dp，优化内存
class Solution3:
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

~~~

~~~python
打家劫舍
class Solution:
    def rob(self, nums) -> int:
        """
        1. 分治（子问题）
        2. 状态数组 dp[i][0/1]
        3 dp 方程： dp[i][0] = max([i-1][0], a[i-1][1])
                   dp[i][1] = dp[i-1][0] + nums[i]
        """
        if not nums:
            return 0
        dp = [[0, 0] for i in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[-1][0], dp[-1][1])

class Solution1:
    def rob(self, nums):
        pre = 0
        now = 0
        for i in nums:
            # dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            pre, now = now, max(pre + i, now)
        return now
~~~

