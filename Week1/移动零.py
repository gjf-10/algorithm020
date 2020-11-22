# [283] 移动零：
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
#  示例:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]

# 第一遍做的
def moveZeroes(self, nums):
    nums = [0, 1, 0, 3, 12]
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            if i != j:
                nums[i] = 0
            j += 1


# 第二遍
# 1.只能在原数组上进行操作，用尽量少的操作。
# 2.for循环将零的个数记下遇到零的数直接删除，最后添加n个0
#   用一个指针，指向零另一个指针i用于指向非零，只要遇到非零的数字，该指针就和指向零的指针j的数字作值交换，
#   用一个for循环，两个指针同时开始走，i遇到非零停（就是做一次判断）和j所指的值作交换，j遇到零停，等待i作交换，
def moveZeroes1(nums):
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:  # 让i先走找一个非零的元素，没找到则不改变数组，找非零元素则让j走
            nums[j] = nums[i]  # 可能指向的是同一个元素，也可能指向的不是同一个元素
            if i != j:  # 说明 两个指针指向的不是同一个数，则需要互换，
                nums[i] = 0
            j += 1  # 让j指向下一个元素


def moveZeroes2(nums):
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0 and i != j:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    # print(nums)


a = [0, 0, 0, 3, 3]
moveZeroes2(a)
print(a)
