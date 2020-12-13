class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:     # 左边包括mid有序
                if nums[left] <= target < nums[mid]:    # 如果target在左边
                    right = mid - 1
                else:       # 在无序的右边
                    left = mid + 1
            else:    # 右边有序
                if nums[mid] < target <= nums[right]: # target 在右边
                    left = mid + 1
                else:       # 在左边
                    right = mid - 1
        return -1

class solution1:
    def search(self, nums, target):
        try:
            return nums.index(target)
        except:
            return -1