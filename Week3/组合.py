class Solution:
    def combine(self, n, k):
        result = []
        if k <= 0 or n < k:
            return result

        def _dfs(begin, path):
            temp = path.copy()  # 不能直接用path，下面的path会有pop操作，会改变result中的结果
            if k == len(path):
                result.append(temp)
                return None

            for i in range(begin, n + 1):
                path.append(i)
                _dfs(i + 1, path)
                # 回到上一个状态
                path.pop()

        _dfs(1, [])
        return result
a = Solution()
a.combine(3, 2)
