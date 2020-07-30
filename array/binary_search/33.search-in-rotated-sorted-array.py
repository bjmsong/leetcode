#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (32.97%)
# Total Accepted:    431.5K
# Total Submissions: 1.3M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#
class Solution:
    """
    思路：
    - 二分搜索：将数组一分为二
    - 判断前后两部分哪个是有序的
    - 判断target是否处于有序的那一半中
        - 如果是：则在有序的一半中继续二分搜索
        - 如果否：则在无序的一半中继续二分搜索
    时间复杂度： O(logn)
    """

    def search(self, nums, target):

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:    # "="不要漏掉
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:  # 前一半数组有序
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] <= nums[hi]:  # 后一半数组有序
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1

if __name__ == '__main__':
    s = Solution()
    assert (s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1)
    assert (s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4)
