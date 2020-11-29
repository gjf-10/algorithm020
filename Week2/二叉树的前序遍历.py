# 1.二叉树天然的可递归的性质，递归
# 2.根左右
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        # 有个问题就是如何保存遍历过程中产生的值，这里用了一个全局变量，
        # 也可以将列表以参数的形式传进去，
        def preOrder(root):
            if root is None:
                return None
            list_t.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
            return list_t
        global list_t
        list_t = []
        preOrder(root)
        return list_t

# 迭代：递归是一次走到底，迭代是一步一步往后走
class Solution1:
    def preorederTraversal(self, root):
        # 利用栈结构存储迭代过程产生的值
        res = []
        if not root:
            return res

        stack = []
        node = root
        # 根左右
        while stack or root:
            # 里面的循环负责遍历左子树
            while node:
                # 根左根左根左
                res.append(node.val)
                stack.append(node)
                node = node.left
            # 外面的循环负责遍历右子树
            # 根右->在遍历左子树
            node = stack.pop()
            node = node.right
        return res
# 总结：迭代和递归都是深度优先遍历。

# 自己写的，
class Solution2:
    def preorderTraversal(self, root):
        # 递归的前序遍历，根左右
        if root is None:
            return []
        stack = [root] # 根节点
        a = []
        # 根左右
        while stack[-1]:    # 根节点是否存在
            p = stack.pop()     # 删除栈中的根节点并找到它的左右节点
            a.append(p.val)
            left = p.left
            right =p.right
            # 有3中情况，左右节点都有，左右节点中只有一个，没有左右节点
            if left and right:
                #  有左右节点，将左右节点按右左压栈，因为出栈要保证根左右这样的前序
                stack.append(right)
                stack.append(left)
                continue
            elif right or left:
                # 如果只有一个节点将其压栈
                t = right if right else left
                stack.append(t)
                continue
            elif len(stack) == 0:
                # 如果栈中没有元素说明遍历了所有节点
                break
        return a

# 想法：迭代的话需要从根开始找到左孩子，将根压栈，为了找完左孩子后找右孩子
# 我的：从根开始，如果它有左右孩子则直接将左右孩子按右左的形式压栈，而不是压根节点
# 每次遍历一个节点
class Solution3:
    def preorderTraversal(self, root):
        # 迭代
        a = []
        if root is None:
            return a
        stack = [root] # 根节点
        while stack:
            node = stack.pop()
            a.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return a