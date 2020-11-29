# 思路：1. 遍历数组，用遍历一次就记住的方式，防止重复遍历，需要存储
#   1.2. 将遍历的某个词作为键存储，值是找到所有的异位词
# 时间复杂度：O(n), 空间复杂度：O(n)

class Solution:
    def groupAnagrams(self, strs):
        dict_strs = {}
        for i in strs:
            p = "".join(sorted(i))
            if dict_strs.get(p) is None:
                dict_strs[p] = [i]
            else:
                dict_strs[p].append(i)
        c = [v for v in dict_strs.values()]
        return c

# nb人写的代码
class solution1:
    def groupAngrams(self, strs):
        dict_strs = {}
        for i in strs:
            p = tuple(sorted(i)) # 这里不需要再转换会字符串了
            if p in dict_strs:
                dict_strs[p].append(i)
            else:
                dict_strs[p] = [i]
        c = [v for v in dict_strs.keys()]
        return c
