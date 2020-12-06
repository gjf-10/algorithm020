class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(p_start, p_end, i_start, i_end):
            if p_start == p_end:
                return None

            root = TreeNode(preorder[p_start])

            i_root_index = 0
            for i in range(i_start, i_end):
                if preorder[p_start] == inorder[i]:
                    i_root_index = i
                    break

            left_size = i_root_index - i_start

            root.left = helper(p_start + 1, p_start + left_size + 1, i_start, i_end)
            root.right = helper(p_start + left_size + 1, p_end, i_root_index + 1, i_end)
            return root
        return helper(0,len(preorder), 0, len(inorder))


# 用字典优化查找
class Solution1:
    def buildTree(self, preorder, inorder):
        def helper(p_start, p_end, i_start, i_end):
            if p_start == p_end:
                return None

            i_index_root = index[preorder[p_start]]

            # 先把根节点建立出来
            root = TreeNode(preorder[p_start])
            # 得到左子树中的节点数目
            left_size = i_index_root - i_start

            root.left = helper(p_start + 1, p_start + left_size + 1, i_start, i_end)
            root.right = helper(p_start + left_size + 1, p_end, i_index_root + 1, i_end)

            return root

        n = len(preorder)
        # 构造哈希映射，快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return helper(0, n - 1, 0, n - 1)

"""
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

先找到根节点：3

然后根据根节点把中序遍历分为两部分：左子树和右子树
inorder = [[9], 3, [15, 20, 7]] 左中右

把相应的前序遍历的数组也加进来
左子树
preorder[9]

右子树
preorder[20, 15, 7]

重复构建左右子树
"""