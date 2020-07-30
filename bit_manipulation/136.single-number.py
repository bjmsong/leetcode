#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (60.81%)
# Total Accepted:    496.8K
# Total Submissions: 816.3K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#
class Solution:
    def singleNumber(self, nums) -> int:
        # 按位异或：结果相异时为1  
        # 性质：x^0=x x^x=0 y^x^x=y
        length = len(nums)
        res = nums[0]
        for i in range(1, length):
            res = res ^ nums[i]

        return res


if __name__ == '__main__':
    s = Solution()
    assert (s.singleNumber([4, 1, 2, 1, 2]) == 4)
