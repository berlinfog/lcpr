#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=20004
#
# [48] 旋转图像
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #00 01 02 11 12 22
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for i in range(len(matrix)):
            slow = 0 
            fast = len(matrix[0])-1
            while slow < fast:
                matrix[i][slow],matrix[i][fast] = matrix[i][fast],matrix[i][slow]
                slow += 1
                fast -= 1
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

