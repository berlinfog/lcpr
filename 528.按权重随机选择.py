#
# @lc app=leetcode.cn id=528 lang=python3
# @lcpr version=20004
#
# [528] 按权重随机选择
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import random
class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        # 构建前缀和数组，偏移一位留给 preSum[0]
        self.preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            self.preSum[i] = self.preSum[i - 1] + w[i - 1] 


    def pickIndex(self) -> int:
        n = len(self.preSum)
        # 生成在闭区间 [1, preSum[n - 1]] 中的随机整数
        target = random.randint(1, self.preSum[n - 1]) 

        # 获取 target 在前缀和数组 preSum 中的索引
        # 别忘了前缀和数组 preSum 和原始数组 w 有一位索引偏移
        return self.left_bound(self.preSum, target) - 1

    def left_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        # 搜索左侧边界的二分搜索
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end



#
# @lcpr case=start
# ["Solution","pickIndex"][[[1]],[]]\n
# @lcpr case=end

# @lcpr case=start
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"][[[1,3]],[],[],[],[],[]]\n
# @lcpr case=end

#

