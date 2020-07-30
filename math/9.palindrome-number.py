#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number # 回文
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (43.33%)
# Total Accepted:    581.3K
# Total Submissions: 1.3M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 反转后面一半的数字，跟前面一半的数字比较
        if x < 0:
            return False
        # 最后一位是0的不可能是回文，因为最高位不可能是0
        if x > 0 and x % 10 == 0:
            return False
        # 当前面的元素<=后面的元素，说明已经到一半了
        x2 = 0
        while x > x2:
            x2 = 10 * x2 + x % 10
            x = x // 10
        if x == x2:
            return True
        if x == x2//10:
            return
        return x == x2 or x == x2 // 10

    # def isPalindrome(self, x: int) -> bool:
    #     """
    #     int->string
    #     空间复杂度：O(n)
    #     :param x:
    #     :return:
    #     """
    #     if x < 0:
    #         return False
    #     x = str(x)
    #     left, right = 0, len(x) - 1
    #     while left < right:
    #         if x[left] != x[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True

    # def isPalindrome(self, x: int) -> bool:
    #     # 先把数字reverse，如果reverse后的数字和原数字一致，则表明是回文！
    #     # 反转后的数字会遇到整数溢出的问题
    #     if x < 0:
    #         return False
    #     xc = x
    #     x_rev = 0
    #     while xc != 0:
    #         x_rev = 10 * x_rev + xc % 10
    #         xc = xc // 10
    #     if x_rev == x:
    #         return True
    #     else:
    #         return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(123))
    print(s.isPalindrome(-121))
