from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node'):
        list_a = []
        if not root:
            return list_a
        queue = deque([root])
        while queue:
            temp = []
            for i in range(len(queue)):
               node = queue.popleft()
               temp.append(node.val)
               queue.extend(node.children)
            list_a.append(temp)
        return list_a

