#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=20004
#
# [15] 三数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 对数组进行排序
        res = []  # 用于存储结果
        
        for i in range(len(nums)):
            # 跳过重复的数字
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]  # 目标值为当前数的相反数
            left, right = i + 1, len(nums) - 1  # 双指针初始化
            
            while left < right:
                # 如果找到满足条件的三元组
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 跳过重复的左指针值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳过重复的右指针值
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 移动指针
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:  # 和小于目标值，移动左指针
                    left += 1
                else:  # 和大于目标值，移动右指针
                    right -= 1
        
        return res
# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

