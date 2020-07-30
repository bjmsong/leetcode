#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (33.74%)
# Total Accepted:    312.9K
# Total Submissions: 927.4K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#
class Solution:
    """
    思路： 二分法搜索,找到后向两边扩展
    时间复杂度：O(logn)
    """

    def searchRange(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] == target:
                left, right = mid, mid
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left + 1, right - 1]
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    assert (s.searchRange([1], 1) == [0, 0])
    assert (s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4])
    assert (s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1])
