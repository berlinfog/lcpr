#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=20004
#
# [206] 反转链表
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
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head == None or head.next == None:
    #         return head
    #     pre = None
    #     cur = head
    #     nxt = head.next
    #     while cur != None:
    #         cur.next = pre
    #         pre = cur
    #         cur = nxt
    #         if nxt!= None:
    #             nxt = nxt.next
    #     return pre
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

