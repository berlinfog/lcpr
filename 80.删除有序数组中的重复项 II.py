#
# @lc app=leetcode.cn id=80 lang=python3
# @lcpr version=20004
#
# [80] 删除有序数组中的重复项 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0,1
        #[0,slow] is result
        count = 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                count += 1
                if count < 2:
                    slow += 1
                    nums[slow] = nums[fast]
                fast += 1
            else:
                count = 0
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow+1
                
            

# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#

