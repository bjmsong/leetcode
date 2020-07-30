#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (19.95%)
# Total Accepted:    374.1K
# Total Submissions: 1.9M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string, reverse the string word by word.
# 
# 
# 
# Example 1:
# 
# 
# Input: "the sky is blue"
# Output: "blue is sky the"
# 
# 
# Example 2:
# 
# 
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
# 
# 
# Example 3:
# 
# 
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
# 
# 
# 
# 
# Note:
# 
# 
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed
# string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the
# reversed string.
# 
# 
# 
# 
# Follow up:
# 
# For C programmers, try to solve it in-place in O(1) extra space.
#
class Solution:

    def reverseWords(self, s: str) -> str:
        import re
        lst = re.split("\s+", s.strip())
        left, right = 0, len(lst) - 1
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

        return " ".join(lst)

    # def reverseWords(self, s: str) -> str:
    #     """
    #     倒序遍历，记录单词的边界，把单词依次加入列表中
    #     时间复杂度:O(n)
    #     空间复杂度：O(n)
    #     """
    #     s = s.strip()
    #     result = []
    #     i = len(s) - 1
    #     while i >= 0:
    #         if s[i] != " ":
    #             right = i
    #             while i >= 0 and s[i] != " ":
    #                 i -= 1
    #             left = i + 1
    #             result.append(s[left:right + 1])
    #         else:
    #             i -= 1
    #
    #     return " ".join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("hello  world"))
    print(s.reverseWords("  hello world!  "))
    print(s.reverseWords("hello  world"))
    print(s.reverseWords("hello   world"))
    print(s.reverseWords("hello   world hi world"))
