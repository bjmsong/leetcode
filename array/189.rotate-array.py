#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (30.05%)
# Total Accepted:    297.4K
# Total Submissions: 989.2K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# Note:
# 
# 
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
#
class Solution:

    def rotate(self, nums, k: int) -> None:
        """
        反转三次：前半段、后半段、整体
        空间复杂度：O(1)
        """
        length = len(nums)
        K = k % length

        def rotate_inplace(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        if K > 0:
            rotate_inplace(nums, 0, length - K - 1)  # reverse 前半段
            rotate_inplace(nums, length - K, length - 1)  # reverse 后半段
            rotate_inplace(nums, 0, length - 1)  # reverse 整体

        # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     时间复杂度:O(1)
    #     空间复杂度：O(n)
    #     """
    #     length = len(nums)
    #     K = k % length
    #     nums[:K], nums[K:] = nums[length - K:], nums[:length - K]  # 整体交换

    # def rotate(self, nums: List[int], k: int) -> None:
    #     length = len(nums)
    #     K = k%length
    #     origin_nums = nums[:]  # 原数组的拷贝
    #     for i in range(length):
    #         nums[(i+k)%length] = origin_nums[i]
