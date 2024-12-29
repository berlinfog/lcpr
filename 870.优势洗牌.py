#
# @lc app=leetcode.cn id=870 lang=python3
# @lcpr version=20004
#
# [870] 优势洗牌
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
         # 给 nums2 降序排序
        sorted_nums2 = sorted(enumerate(nums2), key=lambda x: -x[1])
        # 给 nums1 升序排序
        sorted_nums1 = sorted(nums1)
        # nums1 升序排序数组的首位，指向 nums1 的首部，小
        left = 0
        # nums1 升序排序数组的尾部，指向 nums1 的尾部，大
        right = n - 1
        # nums2 降序排序数组的首位，指向 nums2 的首部
        i = 0
        # 结果数组
        res = [0] * n
        # 开始观察 nums2
        for idx,val in sorted_nums2:
            if sorted_nums1[right] > val:
                # 如果 nums1 的首部，大于 nums2 的首部
                # 则将 nums1 的首部，给 nums2 的首部
                res[idx] = sorted_nums1[right]
                right -= 1
            else:
                res[idx] = sorted_nums1[left]
                left += 1
        return res
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n[1,10,4,11]\n
# @lcpr case=end

# @lcpr case=start
# [12,24,8,32]\n[13,25,32,11]\n
# @lcpr case=end

#

