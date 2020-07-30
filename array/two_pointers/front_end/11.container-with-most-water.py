#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (44.50%)
# Total Accepted:    370.9K
# Total Submissions: 833K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        思路： 每次移动短柱子，因为矩阵的面积取决于短柱子
        时间复杂度：O(n)
        :param height:
        :return:
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            if water > max_area:
                max_area = water
            if height[left] < height[right]:  # 短柱子前移，因为如果短柱子不动，长度又缩小一位，面积不可能变大
                left += 1
            else:
                right -= 1
        return max_area
