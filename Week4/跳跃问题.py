class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 回溯
        j = i = 0
        p = len(nums) - 1
        t_0 = {}
        while True:
            j += nums[i]
            print(j)
            if j >= p:
                return True
            if nums[j] == 0:
                if t_0.get(str(j)) is None:
                    t_0[str(j)] = 0
                else:
                    t_0[str(j)] += 1
                if t_0[str(j)] == j:
                    return False
                j -= t_0[str(j)]
            if j < p:
                i = j

# 贪心
class Solution1:
    def canJump(self, nums):
        if not nums:
            return False

        end_reachable = len(nums) - 1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] + i >= end_reachable:
                end_reachable = i

        return end_reachable == 0