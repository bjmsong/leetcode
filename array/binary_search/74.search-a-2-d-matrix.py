#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (35.07%)
# Total Accepted:    237K
# Total Submissions: 675.6K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Example 1:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
# 
#
class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        二分搜索
        时间复杂度：O(logm+logn)
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        # 确定行： 以每一行的第一个元素组成列表，找到最小的大于target的值
        left, right = 0, m - 1
        while left <= right:  # 等号不要漏
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        if right < 0:
            return False
        else:
            row = right

        # 在确定的行上搜索： 确定值
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    assert (not s.searchMatrix(matrix, 13))
    assert (s.searchMatrix(matrix, 11))
    assert (not s.searchMatrix([[]], 1))
    assert (s.searchMatrix([[1]], 1))
    assert (not s.searchMatrix([[1]], 2))
    assert (not s.searchMatrix([[1, 1]], 2))
