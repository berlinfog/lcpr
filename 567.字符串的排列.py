#
# @lc app=leetcode.cn id=567 lang=python3
# @lcpr version=20004
#
# [567] 字符串的排列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dic = {}
        need = {}
        for s1c in s1:
            s1dic[s1c] = s1dic.get(s1c,0) + 1
        left,right,valid = 0,0,0

        while right < len(s2):
            c = s2[right]
            right += 1
            if c in s1dic:
                need[c] = need.get(c,0) + 1
                if need[c] == s1dic[c]:
                    valid += 1
            
            while right - left >= len(s1):
                if valid == len(s1dic):
                    return True
                d = s1[left]
                left += 1
                if d in s1dic:
                    if need[d] == s1dic[d]:
                        valid -= 1
                    need[d] -= 1
        return False
                
# @lc code=end



#
# @lcpr case=start
# "eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "eidboaoo"\n
# @lcpr case=end

#

