#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (40.67%)
# Total Accepted:    590.9K
# Total Submissions: 1.5M
# Testcase Example:  '[1,1,2]'
#
# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# Example 1:
# 
# 
# Given nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively.
# 
# It doesn't matter what you leave beyond the returned length.
# 
# Example 2:
# 
# 
# Given nums = [0,0,1,1,1,2,2,3,3,4],
# 
# Your function should return length = 5, with the first five elements of nums
# being modified to 0, 1, 2, 3, and 4 respectively.
# 
# It doesn't matter what values are set beyond the returned length.
# 
# 
# Clarification:
# 
# Confused why the returned value is an integer but your answer is an array?
# 
# Note that the input array is passed in by reference, which means modification
# to the input array will be known to the caller as well.
# 
# Internally you can think of this:
# 
# 
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
# 
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
# 
#
class Solution:

    # def removeDuplicates(self, nums):
    #     """
    #     in-place
    #     双指针
    #     测试case:
    #     [1,2,3,4]
    #     [1,1,2]
    #     [0,0,1,1,1,2,2,3]
    #     [1,1,1,1]
    #     """
    #     length = len(nums)
    #     if length < 2:
    #         return length
    #     left_index = 0  # record elements without duplicates
    #     for i in range(1, length):
    #         if nums[left_index] != nums[i]:
    #             left_index += 1
    #             nums[left_index] = nums[i]
    #     return left_index + 1

    def removeDuplicates(self, nums):
        """
        重复项计数法：允许保留k次重复，更通用
        """
        k = 1
        i = 0   # 记录满足条件的数组结尾
        for n in nums:
            if i < k or n > nums[i - k]:
                nums[i] = n
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    assert (s.removeDuplicates([1, 1, 2]) == 2)
    assert (s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5)
