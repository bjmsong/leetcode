#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (44.19%)
# Total Accepted:    276.6K
# Total Submissions: 626K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#
class Solution:
    def longestConsecutive(self, nums):
        """
        思路： 哈希表存储数组，以每个元素为中心，向左右两边扩展，直到断掉为止
        时间复杂度：O(n)
        """
        d = {}
        for n in nums:
            d[n] = 1
        max_length = 0
        for n in nums:
            if d[n]:
                d[n] = None
                lo, hi = n, n
                length = 0
                while d.get(lo - 1):
                    length += 1
                    d[lo - 1] = None
                    lo -= 1
                while d.get(hi + 1):
                    length += 1
                    d[hi + 1] = None
                    hi += 1
                if length + 1 > max_length:
                    max_length = length + 1

        return max_length



if __name__ == '__main__':
    s = Solution()
    assert (s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
    assert (s.longestConsecutive([1, 2, 3]) == 3)
    assert (s.longestConsecutive([1, 2, 3, 5]) == 3)
    assert (s.longestConsecutive([1, 5, 3, 2]) == 3)
    assert (s.longestConsecutive([1, 2, 3, 5, 6, 7, 8, 10]) == 4)
    assert (s.longestConsecutive([]) == 0)
    assert (s.longestConsecutive([1]) == 1)
