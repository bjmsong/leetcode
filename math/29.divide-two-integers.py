#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (16.16%)
# Total Accepted:    195.6K
# Total Submissions: 1.2M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
# 
# Return the quotient after dividing dividend by divisor.
# 
# The integer division should truncate toward zero.
# 
# Example 1:
# 
# 
# Input: dividend = 10, divisor = 3
# Output: 3
# 
# Example 2:
# 
# 
# Input: dividend = 7, divisor = -3
# Output: -2
# 
# Note:
# 
# 
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 2^31 − 1 when the division
# result overflows.
# 
# 
#
class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        # 除法转换为对数减法
        import math
        if dividend == 0:
            return 0
        isPostive = (dividend > 0) == (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = math.log(dividend) - math.log(divisor)  
        res = int(math.exp(res))      # truncate toward zero.
        if isPostive:
            return min(res, 2147483647)    # 正数不超过 2^31-1
        else:
            return max(0 - res, -2147483648)   # 负数不超过 -2^31
        

