#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=20004
#
# [1] 两数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictele = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in dictele:
                return [dictele[need],i]
            dictele[nums[i]] = i
        return []
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

