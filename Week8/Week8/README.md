布隆过滤器

判断一个元素是否在一个集合中

运用场景：

​	字处理软件中，检查一个英文单词是否拼写正确

​	在网络爬虫里，一个网址是否被访问过。

​	yahoo， gmail 等邮箱垃圾邮件过滤功能

​	缓存穿透

缓存穿透：

​	为了避免恶意用户频繁请求缓存中不存在DB也不存在的值，会导致缓存失效、DB负载过大，可以使用BloomFilter把所有数据放到bit数组中，当用户请求时存在的值肯定能放行，部分不存在的值也会被放行，绝大部分会被拦截，这些少量漏网之鱼对于DB的影响就会比大量穿透好的多了 

布隆过滤器的核心实现是一个超大的位数组和几个哈希函数。

特点：空间和查询效率高，有一定的误判率。

布隆过滤器添加元素
	将要添加的元素给k个哈希函数，得到对应位数组上的k个位置，将这k个位置设为1

布隆过滤器查询元素

​	将要查询的元素给k个哈希函数，得到对应于维数组上的k个位置，如果k个位置有一个为0，则肯定不在集合中，如果k个位置全部为1，则可能在集合中。

代码

~~~python
from bitarray import bitarray
import mmh3
class BloomFilter:
    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            self.bit_array[result] = 1

    def lookup(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            if self.bit_array[result] == 0:
                return "Nope"
        return "Probably"
~~~

排序

~~~python
# 快速排序
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)
    
def partition(begin, end, nums):
	pivot = nums[begin]
	mark = begin
    for i in range(begin+1, end+1):
		if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
# 归并
def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left + right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
  	while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= right:
        temp.append(nums[j])
        j += 1
    nums[left: right+1] = temp
~~~

