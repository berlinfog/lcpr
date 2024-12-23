#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=20004
#
# [234] 回文链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    left = None
    res = True
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        self.traverse(head)
        return self.res
    
    def traverse(self,right):
        if right == None :
            return
        self.traverse(right.next)
        if self.left.val != right.val:
            self.res = False
        self.left = self.left.next
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

