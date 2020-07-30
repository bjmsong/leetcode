#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (36.35%)
# Total Accepted:    391.4K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution:
    def merge(self, nums1, m, nums2, n):
        # 从列表末端开始，双指针
        p1 = m - 1
        p2 = n - 1
        index = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[index] = nums1[p1]
                p1 -= 1
            else:
                nums1[index] = nums2[p2]
                p2 -= 1
            index -= 1
        if p2 >= 0:
            nums1[:index + 1] = nums2[:p2 + 1]

    # def merge(self, nums1, m, nums2, n):
    #     # 从列表末端开始，双指针
    #     if n == 0:
    #         return
    #     if m == 0:
    #         nums1[:] = nums2[:]     # nums1 = nums2 不可以
    #         return
    #     idx1 = m - 1
    #     idx2 = n - 1
    #     i = m + n - 1
    #     while idx1 >= 0 and idx2 >= 0:
    #         if nums1[idx1] > nums2[idx2]:
    #             nums1[i] = nums1[idx1]
    #             idx1 -= 1
    #         else:
    #             nums1[i] = nums2[idx2]
    #             idx2 -= 1
    #         i -= 1
    #     if idx1 < 0:
    #         nums1[:i + 1] = nums2[:idx2 + 1]


if __name__ == '__main__':
    s = Solution()
    nums1 = [0]
    s.merge(nums1, 0, [1], 1)
    print(nums1)
