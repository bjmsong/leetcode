"""
括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
"""


class Solution:

    def generateParenthesis(self, n: int):
        result = []

        def generate(left, right, n, s):
            """
            先加左括号，左括号的数量大于等于右括号的数量
            :param left: 左括号的数量
            :param right: 右括号的数量
            :param n: 左括号/右括号的最大值
            """
            # 递归终止条件
            if left == n and right == n:
                result.append(s)
                return

            if left < n:
                generate(left + 1, right, n, s + "(")
            if right < left:
                generate(left, right + 1, n, s + ")")

        generate(0, 0, n, "")

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
