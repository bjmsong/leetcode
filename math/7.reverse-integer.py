#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.30%)
# Total Accepted:    693K
# Total Submissions: 2.7M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#


class Solution:
    # def reverse(self, x: int) -> int:
    #     if x<0:
    #         negative = -1
    #         ls=list(str(x))[1:]
    #     else:
    #         negative = 1
    #         ls = list(str(x))
    #     length = len(ls)
    #     for i in range(length//2):
    #         ls[i],ls[length-i-1] = ls[length-i-1],ls[i]  # reverse in place
    #     ls_rev = "".join(ls)
    #     x_rev = int(ls_rev)*negative
    #     if x_rev > 2147483647 or x_rev<-2147483648:   # 反转值溢出
    #         return 0
    #     return x_rev
    def reverse(self, x: int) -> int:
        res, pos = 0, 1
        if x < 0:
            pos = -1
            x = -1 * x
        while x != 0:
            res = 10 * res + x % 10  # 每次将最后一位移到前面
            if res > 2147483647:
                return 0
            x //= 10  # python3 1/10 = 0.1 , 1//10 =0

        return res * pos
