#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (30.49%)
# Total Accepted:    233K
# Total Submissions: 764.2K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 


class Solution:

    def fourSum(self, nums, target):
        """
        思路：
        时间复杂度： O(n^3+nlogn)
        空间复杂度：
        """
        solution = {}  # 字典的key/集合可以保证解唯一
        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            for j in range(i + 1, length - 2):  # j从i+1开始
                value = target - nums[i] - nums[j]
                lo = j + 1
                hi = length - 1
                while lo < hi:
                    add = nums[lo] + nums[hi]
                    if add == value:
                        key = (nums[i], nums[j], nums[lo], nums[hi])  # 元组
                        solution[key] = None
                        lo += 1  # don't forget to move on
                    elif add < value:
                        lo += 1
                    else:
                        hi -= 1

        return list(solution.keys())


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
    result = s.fourSum([0, 0, 0, 0], 1)
