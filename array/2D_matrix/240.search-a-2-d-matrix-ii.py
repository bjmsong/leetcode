#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (41.13%)
# Total Accepted:    193.3K
# Total Submissions: 469.7K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# Example:
# 
# Consider the following matrix:
# 
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# Given target = 5, return true.
# 
# Given target = 20, return false.
# 
#
class Solution:

    def searchMatrix(self, matrix, target):
        """
        思路: 跟右上角的元素比较
        设右上角值为val，如果val<target,则可以排除val所在的行；如果val>target,则可以排除val所在的列
        直到遍历完矩阵
        时间复杂度：O(m+n)
        :param matrix:
        :param target:
        :return:
        """
        if matrix == [] or matrix[0] == []:
            return False
        i = 0  # 行index
        j = len(matrix[0]) - 1  # 列index
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
