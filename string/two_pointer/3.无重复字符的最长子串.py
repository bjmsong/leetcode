"""
无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串的长度。

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        滑动窗口
        - 使用两个指针代表子串的左右边界
        - 每一步操作，将左指针右移,作为下一个字符串的起始位置，然后不断右移右指针,直到遇到重复元素为止
        优点在于减少了大量重复对比
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        length = len(s)
        if length <= 1:
            return length
        max_length = 1
        # 左右指针
        left, right = 0, 1
        # 记录窗口内的元素
        d = set()
        d.add(s[0])
        while left < length - 1 and right < length:
            # 移动右指针
            while right < length:
                if s[right] in d:
                    break
                else:
                    d.add(s[right])
                    right += 1
            if max_length < len(d):
                max_length = len(d)
            d.remove(s[left])
            left += 1

        return max_length

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     """
    #     双指针:一个记录初始位置，一个记录移动的位置
    #     用集合记录子串的元素(非重复)
    #     时间复杂度：O(n^2)
    #     空间复杂度：O(n)
    #     :param s:
    #     :return:
    #     """
    #     length = len(s)
    #     if length <= 1:
    #         return length
    #     max_length = 1
    #     for i in range(length - 1):
    #         d = set()
    #         d.add(s[i])
    #         for j in range(i + 1, length):
    #             if s[j] in d:
    #                 break
    #             else:
    #                 d.add(s[j])
    #         if len(d) > max_length:
    #             max_length = len(d)
    #
    #     return max_length


if __name__ == '__main__':
    s = Solution()
    assert (s.lengthOfLongestSubstring("abcabcbb") == 3)
    assert (s.lengthOfLongestSubstring("bbbbb") == 1)
    assert (s.lengthOfLongestSubstring("pwwkew") == 3)
    assert (s.lengthOfLongestSubstring("au") == 2)
