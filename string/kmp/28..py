"""
实现 strStr()
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。

例如：
输入: haystack = "hello", needle = "ll"
输出: 2
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        KMP
        :param haystack:
        :param needle:
        :return:
        """











    # def strStr(self, haystack: str, needle: str) -> int:
    #     """
    #     暴力匹配
    #     :param haystack:
    #     :param needle:
    #     :return:
    #
    #     """
    #     if needle == "":
    #         return 0
    #     length1 = len(haystack)
    #     length2 = len(needle)
    #     if length1 < length2:
    #         return -1
    #     for i in range(length1 - length2 + 1):
    #         p = 0
    #         while p < length2 and haystack[i+p] == needle[p]:
    #             p += 1
    #         if p == length2:
    #             return i
    #     return -1


if __name__ == '__main__':
    s = Solution()
    assert (s.strStr("hello", "ll") == 2)
    assert (s.strStr("", "") == 0)
