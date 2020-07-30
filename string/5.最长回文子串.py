"""
最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""


class Solution:

    def palindromeCheck(self, s):
        """
        中心扩散法
        """
        result = ""
        max_length = 0
        for i in range(len(s)):
            # 若回文子串长度为偶数
            step = 0
            while i - step >= 0 and i + 1 + step < len(s) and s[i - step] == s[i + 1 + step]:
                step += 1
            if 2 * step > max_length:
                max_length = 2 * step
                result = s[i - step + 1:i + step + 1]
            # 若回文子串长度为奇数
            step = 1
            while i - step >= 0 and i + step < len(s) and s[i - step] == s[i + step]:
                step += 1
            if 2 * step - 1 > max_length:
                max_length = 2 * step - 1
                result = s[i - step + 1:i + step]

        return result

    # def expand(self, s, i, j):
    #     while i >= 0 and j < len(s) and s[i] == s[j]:
    #         i -= 1
    #         j += 1
    #     return j - i - 1
    #
    # def longestPalindrome(self, s):
    #     """
    #     中心扩散法：从回文字符串中心往两边扩散,直到不能扩展为止
    #     回文字符串中心有两种情况：单个字符（如aba），两个字符（如abba）
    #     因此遍历的情况一共有n+n-1 = 2n-1种
    #     时间复杂度：O(n^2)
    #     空间复杂度：O(1)
    #     :param s:
    #     :return:
    #     """
    #     lentgh = len(s)
    #     if lentgh < 1:
    #         return s
    #     max_length = 1
    #     start = end = 0  # 最长回文子串的首尾指针
    #     for i in range(lentgh):
    #         len1 = self.expand(s, i, i)  # 中心为单个字符
    #         len2 = self.expand(s, i, i + 1)  # 中心为两个字符
    #         if max_length < max(len1, len2):
    #             max_length = max(len1, len2)
    #             if len2 > len1:
    #                 start = i - (len2 - 2) // 2
    #                 end = i + 1 + (len2 - 2) // 2
    #             else:
    #                 start = i - (len1 - 1) // 2
    #                 end = i + (len1 - 1) // 2
    #
    #     return s[start:end + 1]

    # def palindromeCheck(self, s):
    #     length = len(s)
    #     for i in range(length // 2):
    #         if s[i] != s[length - 1 - i]:
    #             return False
    #     return True

    # def longestPalindrome(self, s):
    #     """
    #     暴力解法：遍历所有(长度大于max_length)的子串，判断是不是回文子串
    #     双指针记录子串的首尾元素
    #     时间复杂度：O(n^3)
    #     :param s:
    #     :return:
    #     """
    #     max_length = 1
    #     result = s
    #     length = len(s)
    #     for i in range(length - 1):
    #         for j in range(i, length):
    #             string_length = j - i + 1
    #             if string_length < max_length:
    #                 continue
    #             if self.palindromeCheck(s[i:j + 1]) and string_length > max_length:
    #                 max_length = string_length
    #                 result = s[i:j + 1]
    #
    #     return result


if __name__ == '__main__':
    s = Solution()
    assert (s.longestPalindrome("abcbd") == "bcb")
    assert (s.longestPalindrome("abcbad") == "abcba")
    assert (s.longestPalindrome("abcba") == "abcba")
    assert (s.longestPalindrome("a") == "a")
    assert (s.longestPalindrome("aa") == "aa")
