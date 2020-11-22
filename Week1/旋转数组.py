# 1. 反转思想，暴力时间复杂度很高，环状替换
# 反转
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    # 1. 能不能暴力，用冒泡的方式，将后面的k个元素从最后一个冒泡到第一个倒数第二个冒泡到第一个, 超出了时间限制
    # 2. 改进：找到不必要的操作
    n = len(nums)
    k = k % n
    nums[:] = nums[n - k:] + nums[:n - k]


arr = [1, 2, 3, 4, 5, 6, 7]


def rotate1(nums, k):
    n = len(nums)
    tempL = nums.copy()
    for i in range(n):
        nums[(i + k) % n] = tempL[i]


# 时间复杂度是O(n), 不过这个赋值很妙
# 另外利用对数组的浅拷贝 空间复杂度应该是O(1)，看另一个官方题解合并两个有序数组中使用切片，并不算新开的空间，结果的时间复杂度仍算O(1)
# rotate(arr, 3)
# print(arr)


# python 中这种浅拷贝的空间复杂度能算O(n)吗
# 我记得有这样说过：python中的这类空间是虚拟空间，而列表中的值指向的正真的物理空间


def rotate2(arr, k):
    def reverse1(arr, start, end):
        # start 和 end是代表数组的下标
        n = (end-start) // 2 if (end-start) % 2 == 0 else (end - start) // 2 + 1
        # 两个指针，一个指向end，一个指向start；如果start < end, 交换连个位置的元素一个++，一个--
        for i in range(n):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    k = k % len(arr)
    reverse1(arr, 0, len(arr) - 1)
    reverse1(arr, 0, k - 1)
    reverse1(arr, k, len(arr) - 1)
rotate2(arr, 3)