#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=20004
#
# [54] 螺旋矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        top = 0
        bot = m - 1
        left = 0
        right = n - 1
        res = []

        while len(res) < m * n:
            if top <= bot:
                for j in range(left,right+1):
                    res.append(matrix[top][j])
                top += 1

            if left <= right:
                for j in range(top,bot+1):
                    res.append(matrix[j][right])
                right -= 1

            if top <= bot:
                for j in range(right, left-1,-1):
                    res.append(matrix[bot][j])
                bot -= 1
            
            if left <= right:
                for j in range(bot,top-1,-1):
                    res.append(matrix[j][left])
                left += 1
        
        return res
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

