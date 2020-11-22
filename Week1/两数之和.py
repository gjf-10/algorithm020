# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 这样的时间复杂度很高，O(n^2)
nums = [2, 7, 11, 15]
res = []
target = 9
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            res.append([i, j])
print(res)


# 优化：字典的方式
# 由于哈希查找的时间复杂度为 O(1)，所以可以利用哈希容器 map 降低时间复杂度
nums = [3, 3, 6]
def two_sum(nums, target):
    hashmap = {}
    # 将num作为键，index作为值放在字典中
    for k, v in enumerate(nums):
        hashmap[v] = k
    print(hashmap)
    for i, v in enumerate(nums):
        j = hashmap.get(target - v)
        if j is not None and i != j:
            return [i, j]

print(two_sum(nums,6))


def two_sum1(nums, target):
    hashmap = {}
    for k, v in enumerate(nums):
        cp = target - v
        if cp in hashmap:
            return [hashmap[cp], k]
        else:
            hashmap[v] = i
print(two_sum1(nums, 6))

# 第二遍
# 数组中的数不能重复使用保证i和j不相等时间复杂度为O(n^2)
def two_sum2(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
print("two_sums2", two_sum2(nums, 6))

def two_sum3(nums, target):
    j = len(nums) - 1
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] + nums[j] == target:
            return [i, j]
        if nums[i] + nums[j] > target:
            j -= 1
print("two_sum3:", two_sum3(nums, 9))

def two_sum4(nums, target):
    hash_map = {}
    for k, v in enumerate(nums):
        hash_map[v] = k
    for k, v in enumerate(nums):
        if hash_map.get(target - v) is not None:
            return [k, hash_map[target - v]]
print("two_sum4:", two_sum4(nums, 6))