# 题目：给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 注意：假设字符中只有小写字母

# 1. 利用字典的键的唯一性统计出现字母的个数；字母为键，出现的次数为值；
# 空间复杂度为O(1), 时间复杂度为O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        for i in s:
            if sd.get(i) is None:
                sd[i] = 1
            else:
                sd[i] += 1
        for j in t:
            if td.get(j) is None:
                td[j] = 1
            else:
                td[j] += 1
        max_len = max(sd.keys(), td.keys())
        for k in max_len:
            if td.get(k) is None or sd.get(k) is None or td[k] != sd[k]:
                return False
        return True
# 用collections 中的Counter方法构建字典
from collections import Counter
class Soultion00:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = Counter(s)
        dict_t = Counter(t)
        for key in dict_s.keys():
            if dict_t.get(key) is None or dict_s[key] != dict_t[key]:
                return False
        return True
# 测试样例：
# s = 'anagram', t = "nagaram" true
# s = 'a' t = 'ab' false 和 s = 'ab', t = 'a' false

# 第二种解法
# 思路：将每个字符串排序，然后遍历较长的字符串
# 注意：str没有 sort()，sort()没有返回值，用sorted() 该方法的参数是可迭代对象，返回值是一个列表
# 时间复杂度：O(nlogn) 空间复杂度：O(n)
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        print(s)
        max_len = max(len(s), len(t))
        for i in range(max_len):
            if len(s) != len(t):
                return False
            elif s[i] != t[i]:
                return False
        return True

# nb人写的nb代码
# 用set
# 时间复杂度：O(n), 空间复杂度O(1)，这个最快代码也清晰
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set1 = set(s)
        for i in set1:
            if s.count(i) != t.count(i):
                return False
        return True

# 一种哈希映射
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = [0 for i in range(26)]
        for i in range(len(s)):
            a[ord(s[i]) - 97] += 1
            a[ord(t[i]) - 97] -= 1
        for i in a:
            if i != 0:
                return False
        return True
# 总结：set和字典都是hash实现的，这个问题中set实现逻辑更简单