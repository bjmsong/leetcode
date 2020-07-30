#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.50%)
# Total Accepted:    591.7K
# Total Submissions: 1.6M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        """
        - 遇到左括号，压入栈中
        - 遇到右括号，则弹出栈中元素，跟右括号比较是否匹配
        """
        if not s:
            return True
        pair = {"[": "]", "(": ")", "{": "}"}  # key：左括号，value;右括号
        stack = []  # 存储左边的括号
        for i in s:
            if i in ["[", "(", "{"]:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == pair[stack.pop()]:
                    continue
                else:
                    return False
        if not stack:
            return True
        return False
