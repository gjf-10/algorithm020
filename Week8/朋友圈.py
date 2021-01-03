class solution1:
    def findCircleNum(self, isConnected):
        if not isConnected: return 0

        n = len(isConnected)
        p = [i for i in range(n)]

        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    self._union(p, i, j)
        return len(set(self._parent(p, i) for i in range(n)))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p2] = p1

    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            i, p[i] = p[i], root
        return root

class solution3:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [0] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                self._dfs(isConnected, visited, i)
                res += 1
        return res

    def _dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and not visited[j]:
                visited[j] = 1
                self._dfs(M, visited, j)