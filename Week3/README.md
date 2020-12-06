递归练习：

```
二叉树的最小深度：
class Solution1:
    def minDepth(self, root):
        return self.minD(root)

    def minD(self, root, level=0, Min=float('inf')):
        if not root:
            if level == 0:
                Min = 0
            return Min

        level += 1
        if not root.left and not root.right:
            if level < Min:
                level = Min
            return Min

        Min = self.minD(root.left, level, Min)
```

```
翻转二叉树
class Solution:
    def invertTree(self, root):
        self.invert(root)
        return root

    def invert(self, root):
        if not root:
            return None
            
        root.left, root.right = root.right, root.left
        
        self.invert(root.left)
        self.invert(root.right)
```

```
验证二叉搜索树
class solution1:
    def isValidBST(self, root):
        return self.isValid(root)

    def isValid(self, root, upper=float('inf'), lower=float("-inf")):
        if not root:
            return True
        if root.val >= upper or root.val <= lower:
            return False

        if not self.isValid(root.left, root.val, lower): return False
        if not self.isValid(root.right, upper, root.val): return False
        
        return True
```

分治、回溯

```
pow(x,y)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        return self._myPow(x, n) if n > 0 else 1 / self._myPow(x, -n)

    def _myPow(self, x, n):
        if n == 1:
            return x
        temp = self._myPow(x, n // 2)
        return temp * temp if n % 2 == 0 else temp * temp * x
```

```
N皇后问题
class Solution1:
    def solveNQueens(self, n: int):
        def DFS1(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None

            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS1(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        DFS1([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in res] for res in result]

# 每一层下去都有一个 for 循环，
# 该for 循环在每一行中的n个位置中找一个合适的位置，
# 找到进入下一层
# 找不到就返回上一层
# 找到最后如果能找到符合结果的答案，就添加一个解，
# 继续所有的可行解
```

