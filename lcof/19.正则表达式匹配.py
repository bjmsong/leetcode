"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
"""


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        """
        遇到 x* 的情况其实只有2种:
        - 当连x都匹配不上时自然就是整个X*抛弃掉
        - 当x匹配上时，要么抵消掉一个s, x*保留， 要么整个x*抛弃掉
        :param s: 待匹配的字符串
        :param p: 正则表达式
        """
        if not p:
            return not s
        first_match = bool(s) and p[0] in (".", s[0])
        if len(p) >= 2 and p[1] == "*":
            if first_match:
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            return self.isMatch(s, p[2:])
        return first_match and self.isMatch(s[1:], p[1:])


if __name__ == '__main__':
    s = Solution()
    assert (s.isMatch("abc", "a.*c"))
    assert (s.isMatch("abc", "abc*c"))
    assert (s.isMatch("abc", ".bc"))
    assert (~s.isMatch("abc", "b*c"))
