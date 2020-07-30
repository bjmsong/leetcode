#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
#
# algorithms
# Medium (42.95%)
# Total Accepted:    248.7K
# Total Submissions: 578.9K
# Testcase Example:  '[1,1,1,2,2,3]'
#
# Given a sorted array nums, remove the duplicates in-place such that
# duplicates appeared at most twice and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# Example 1:
# 
# 
# Given nums = [1,1,1,2,2,3],
# 
# Your function should return length = 5, with the first five elements of nums
# being 1, 1, 2, 2 and 3 respectively.
# 
# It doesn't matter what you leave beyond the returned length.
# 
# Example 2:
# 
# 
# Given nums = [0,0,1,1,1,1,2,3,3],
# 
# Your function should return length = 7, with the first seven elements of nums
# being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
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
#
class Solution:
    def removeDuplicates(self, nums):
        """
        最多允许重复k次问题:
        - 指针index标记符合条件的元素末尾
        - 遍历数组，每个元素和第index-(k-1)个元素比较,如果值相同，则继续遍历，如果值不同，则添加到符合条件的元素末尾
        :param nums:
        :return:
        """
        k = 2
        if len(nums) <= k:
            return len(nums)
        index = k - 1
        for i in range(k, len(nums)):
            if nums[i] > nums[index - k + 1]:
                index += 1
                nums[index] = nums[i]

        return index + 1


if __name__ == '__main__':
    s = Solution()
    length = s.removeDuplicates([1, 1, 1, 2, 2, 3])
    assert (length == 5)
    length = s.removeDuplicates([1, 1, 2, 3])
    assert (length == 4)
    length = s.removeDuplicates([1, 1])
    assert (length == 2)
    length = s.removeDuplicates([])
    assert (length == 0)
    length = s.removeDuplicates([1, 1, 1])
    assert (length == 2)
