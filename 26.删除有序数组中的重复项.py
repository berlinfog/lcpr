#
# @lc app=leetcode.cn id=26 lang=python3
# @lcpr version=20004
#
# [26] 删除有序数组中的重复项
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None:
            return 0
        slow = 0
        fast = 1
        while fast < len (nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1 
# @lc code=end
def removeElement(nums: List[int], val: int) -> int:
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

# https://labuladong.online/algo/essential-technique/array-two-pointers-summary-2/#%E5%9B%9E%E6%96%87%E4%B8%B2%E5%88%A4%E6%96%AD



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#

