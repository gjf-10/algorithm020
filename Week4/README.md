DFS:

~~~python
# 递归：
visited = set()
def dfs(node, visited):
    # terminator
    if node in visited:
        # already visited
        return
    # not visited
    visited.add(node)
    
    
    # process current node
    ...
    
    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node, visited)
        
# 非递归
def DFS(self, root):
    if root is None:
        return []
    
    visited, stack = set(), [root]
   
	while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
~~~

BFS:

~~~python
def BFS(graph, start, end):
    visited = set()
    queue = collections.deque()
    queue.append([start])
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.append(nodes)
        ....
~~~



贪心算法：

在每一步选择中都采取在当前状态下最好或最优的选择，从而希望导致结果是全局最好或最优的算法

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退，动态规划则会`保存`以前的运算结果，并根据`以前的结果`对当前选择，有回退功能。

贪心：当下做出局部最优判断

回溯：能够回退

动态规划：最优判断 + 回退

贪心：图中的最小生成树、哈夫曼编码，一般做一些辅助算法。

二分查找：

~~~python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if target == nums[mid]:
        # find target 
    elif target < nums[mid]:
        right = mid - 1
    else:
        left = mid + 1      
~~~

