#
# @lc app=leetcode.cn id=543 lang=python3
# @lcpr version=20004
#
# [543] 二叉树的直径
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.caltreedia(root)
        return self.ans
    
    def caltreedia(self,root):
        if not root:
            return 0
        left = self.caltreedia(root.left)
        right = self.caltreedia(root.right)
        self.ans = max(self.ans,left+right)
        return max(left,right)+1

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

