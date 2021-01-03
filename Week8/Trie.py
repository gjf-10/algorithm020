"""
1. 对比哈希表和Trie树
哈希表虽然能在O(1)时间内寻找键值， 但却不能做：
    a. 找到具有同一前缀的全部键值
    b. 按词典序枚举字符串的数据集
Trie 可以做到上面两个，
此外：随着哈希表大小增大，会出现大量的冲突，时间复杂度可能增加到O(n)(哈希链表)
Trie树存储多个具有相同前缀的键时可以使用较少的空间此时Trie树只需要O(m)的时间复杂度，m是键长。
在平衡树中查找键值需要O(mlogn)时间复杂度

应用：1. 自动补全（前缀查询） 2.拼写检查 3.IP路由（最长前缀匹配） 4. 单词游戏  5.T9打字预测

Trie结构：
    a. 最多有R个指向子节点的链接，其中每个链接对应数据集中的一个字母
    b. 布尔字段，指定节点是对应键的结尾还是键的前缀

操作：insert 和 search
insert：
    a. 链接存在：沿着链接移动到树的下一个子层，for循环继续搜索下个字符
    b. 链接不存在：创建一个新的节点，并将它与父节点的链接相连
时间空间复杂度都为O(m)
search:
    a. 存在链接，移动到该链接后面路径中的下个节点，继续搜索下个键字符
    b. 没有链接，若已无键字符，且当前节点标记为isEnd，返回true。否则返回False
时间复杂度O(m),空间复杂度O(1)

查找Trie树中的前缀
    和搜索键相似，区别，到达键前缀的末尾时，总返回true，不用考虑isEnd标记。
"""
class Trie:

    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

