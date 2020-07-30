#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (35.76%)
# Total Accepted:    356.2K
# Total Submissions: 995.9K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#
class Solution(object):
    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])
        if not intervals:
            return []
        left_index = 0
        for i in range(1, len(intervals)):
            if intervals[left_index][1] >= intervals[i][0]:
                intervals[left_index][1] = max(intervals[left_index][1], intervals[i][1])
            else:
                left_index += 1
                intervals[left_index] = intervals[i]
        return intervals[:left_index + 1]


if __name__ == '__main__':
    s = Solution()
    assert (s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]])
    assert (s.merge([[1, 4], [4, 5]]) == [[1, 5]])
    assert (s.merge([[1, 4]]) == [[1, 4]])
    assert (s.merge([]) == [])
    assert (s.merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]])