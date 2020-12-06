# 二叉搜索树的最近公共祖先
class solutions:
    def lowestCommonAncestor(self, root, p, q):
        # 遍历二叉树得到pq节点的level，
        # 用递归查找节点
        return self.findPQ(root, min(p.val, q.val), max(p.val, q.val))

    def findPQ(self, root, Min, Max):
        # terminator
        if not root:
            return None

        # process logic
        if Min <= root.val and Max >= root.val:
            return root
        # drill down

        ancestor = root
        if Min > root.val:
            ancestor = self.findPQ(root.right, Min, Max)
        elif Max < root.val:
            ancestor = self.findPQ(root.left, Min, Max)
        return ancestor

# 优化
class solution1:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root
        return self.findPQ(root, min(p.val, q.val), max(p.val, q.val))

    def findPQ(self, root, Min, Max):
        if Min < root.val < Max or Min == root.val or root.val == Max:
            return root

        return self.findPQ(root.left, Min, Max) if Max < root.val else self.findPQ(root.right, Min, Max)


#二叉树的最近公共祖先
class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        # 所有值是唯一的， 给定的p, q 都存在于二叉树中
        # 只要这一层找到p q中的一个，就在该节点的左右子树中找，若找得到，该节点为公共祖先，若找不到则该节点的父节点为公共节点

        return self.findQP(root, p, q)

    def findQP(self, root, p, q):
        # 找到p或q任意一个
        if not root or root == q or root == p:
            return root

        left = self.findQP(root.left, p, q)
        right = self.findQP(root.right, p, q)

        # p q 存在左右子树中
        if left and right:
            return root
        # p q存在左子树中或右子树中
        return left if not right else right

