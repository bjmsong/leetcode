#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (53.40%)
# Total Accepted:    410.2K
# Total Submissions: 767.3K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#
class Solution:

    # def majorityElement(self, nums: List[int]) -> int:
    #     res = dict()
    #     length = len(nums)
    #     for i in range(length):
    #         num = nums[i]
    #         if num in res.keys():
    #             res[num] += 1
    #         else:
    #             res[num] = 1

    #     for k,v in res.items():
    #         if v > length // 2 : 
    #             return k 

    def majorityElement(self, nums) -> int:
        # 众数数量大于一半，那么排好序后中间的数一定是众数！
        nums.sort()
        return nums[len(nums)//2]

    # def majorityElement(self, nums: List[int]) -> int:
    #     # best solution : 摩尔投票法
    #     res = cnt = 0
    #     for num in nums:
    #         if cnt == 0:
    #             res = num
    #             cnt += 1
    #         elif res == num:
    #             cnt += 1
    #         else:
    #             cnt -= 1
    #     return res
