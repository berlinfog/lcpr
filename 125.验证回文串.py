#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=20004
#
# [125] 验证回文串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sb = []
        for c in s:
            if c.isalnum():
                sb.append(c.lower())

        l,r = 0, len(sb)-1
        while l < r:
            if sb[l] != sb[r]:
                return False
            l += 1
            r -= 1
        return True
# @lc code=end



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

