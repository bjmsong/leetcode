#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.16%)
# Total Accepted:    1.8M
# Total Submissions: 4.1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two nums such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
class Solution:

    def twoSum(self, nums, target):
        """
        思路： 先排序，二分法，双指针从头尾开始逼近
        时间复杂度：O(nlogn)
        空间复杂度：O(n)
        """
        nums_sort = [(value, index) for index, value in enumerate(nums)]
        nums_sort.sort(key=lambda x: x[0])  # sort inplace
        begin = 0
        end = len(nums) - 1
        while begin < end:
            add = nums_sort[begin][0] + nums_sort[end][0]
            if add == target:
                return [nums_sort[begin][1], nums_sort[end][1]]  # 注意返回的是index
            elif add < target:
                begin += 1
            else:
                end -= 1

    def twoSum_1(self, nums, target):
        """
        思路： 哈希表(value:index)
        时间复杂度：O(n)
        空间复杂度：O(n)
        :param nums:
        :param target:
        :return:
        """
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
        for i in range(len(nums)):
            v = target - nums[i]
            index = dict.get(v)
            if index and index > i:   # 同一个数不能重复使用
                return [i, index]


if __name__ == '__main__':
    s = Solution()
    result = s.twoSum([2, 5, 5, 11], 10)
    assert (result == [1, 2])
