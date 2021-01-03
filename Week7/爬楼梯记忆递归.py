class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归
        if n < 3:
            return n
        memo = [1, 2]
        def dfs(n):
            if n-1 < len(memo):
                return memo[n-1]
            tmp = dfs(n - 1) + dfs(n - 2)
            memo.append(tmp)
            return memo[-1]
        return dfs(n)