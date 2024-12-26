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
    def twoSumDup(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left,right = 0, len(nums)-1
        res = []
        while left < right:
            sum = nums[left] + nums[right]
            l = nums[left]
            r = nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                res.append([nums[left],nums[right]])
                while left < right and nums[left] == l:
                    left += 1
                while left < right and nums[right] == r:
                    right -= 1
        return res
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

