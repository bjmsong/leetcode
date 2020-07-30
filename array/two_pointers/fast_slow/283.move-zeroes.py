#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (57.24%)
# Total Accepted:    758.9K
# Total Submissions: 1.3M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#
class Solution:

    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        思路: 双指针,左指针记录非零数字的位置，右指针遍历数组
        时间复杂度： O(n)
        """
        left_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left_index], nums[i] = nums[i], nums[left_index]
                left_index += 1


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    assert (nums == [1, 3, 12, 0, 0])
