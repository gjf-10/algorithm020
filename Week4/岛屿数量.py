class Solution:
    def numIslands(self, grid) -> int:
        # 如果1的上下左右都是0那么该1 是一个岛屿

        def mark(n, m):
            nonlocal grid
            if n < 0 or m < 0 or n >= row or m >= col or grid[n][m] != '1':
                return None
            grid[n][m] = '0'

            mark(n + 1, m)
            mark(n - 1, m)
            mark(n, m + 1)
            mark(n, m - 1)

        row = len(grid)
        col = len(grid[0])

        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    mark(i, j)
                    count += 1
        return count