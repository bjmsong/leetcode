#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (34.79%)
# Total Accepted:    530.8K
# Total Submissions: 1.5M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 只考虑数字和字母，忽略其余字符
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalpha() and not s[left].isdigit():
                left += 1
            while left < right and not s[right].isalpha() and not s[right].isdigit():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    assert (not s.isPalindrome("0P"))
    assert (not s.isPalindrome("race a car"))
    assert (s.isPalindrome("race car"))
    assert (s.isPalindrome(",,"))
    assert (s.isPalindrome("A man, a plan, a canal: Panama"))
