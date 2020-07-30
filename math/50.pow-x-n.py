#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (27.95%)
# Total Accepted:    319.4K
# Total Submissions: 1.1M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
# 
# 
#
class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     # 暴力解法, 时间复杂度O(n)
    #     if n<0:
    #         x= 1/x
    #         n= -1*n
    #     result = 1
    #     for i in range(n):
    #         result *= x

    #     return result
    def myPow(self, x: float, n: int) -> float:
        """
        快速幂算法（递归）
        时间复杂度 O(log(n))
        """

        def fastPow(x, n):
            # 把x^n 转化为 x^(n/2) * x^(n/2) ！
            if n == 0:
                return 1
            # if n == 1:
            #     return x
            half = fastPow(x, n // 2)
            if n % 2 == 0:  # 偶数
                return half * half
            else:  # 奇数
                return half * half * x

        if n < 0:
            x = 1 / x
            n = -1 * n
        return fastPow(x, n)
