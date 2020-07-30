#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (42.33%)
# Total Accepted:    323.3K
# Total Submissions: 763.7K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# 
#
class Solution:
    """
    思路： 把0运到左边，把2运到右边
    - 双指针，一个记录0的位置（头部），一个记录2的位置（尾部）
    - 遍历数组
    时间复杂度：O(n)
    [2,0,2,1,1,0]
    """

    def sortColors(self, nums):
        left_index = 0  # 记录0的位置
        right_index = len(nums) - 1  # 记录2的位置
        i = 0  # 遍历指针
        while i <= right_index:  # 注意这边是遍历到右指针即可，不要遍历完数组
            if nums[i] == 0:
                nums[left_index], nums[i] = nums[i], nums[left_index]
                left_index += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right_index] = nums[right_index], nums[i]
                right_index -= 1
            else:
                i += 1

        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    assert (s.sortColors(nums) == [0, 0, 1, 1, 2, 2])
    nums = [2, 0, 1]
    assert (s.sortColors(nums) == [0, 1, 2])
