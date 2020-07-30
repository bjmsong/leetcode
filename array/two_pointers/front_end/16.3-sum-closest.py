#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.77%)
# Total Accepted:    346.4K
# Total Submissions: 756.7K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
#
class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return
        nums.sort()
        sum = nums[0] + nums[1] + nums[2]
        closet = abs(sum - target)
        for i in range(len(nums) - 2):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                val = nums[i] + nums[lo] + nums[hi]
                if val == target:
                    return val
                elif val < target:
                    lo += 1
                else:
                    hi -= 1
                diff = abs(val - target)
                if diff < closet:
                    closet = diff
                    sum = val
        return sum

    # def threeSumClosest(self, nums, target):
    #     """
    #     思路：先排序，再双指针从收尾逼近
    #     时间复杂度：O(n^2+nlgn)
    #     空间复杂度：O(1)
    #     """
    #     nums.sort()
    #     length = len(nums)
    #     closet = nums[0] + nums[1] + nums[2]
    #     diff = abs(closet - target)
    #     for i in range(length - 2):
    #         begin = i + 1
    #         end = length - 1
    #         while begin < end:
    #             add = nums[i] + nums[begin] + nums[end]
    #             if add == target:
    #                 return add
    #             if diff > abs(add - target):
    #                 closet = add
    #                 diff = abs(add - target)
    #             if add < target:
    #                 begin += 1
    #             else:
    #                 end -= 1
    #
    #     return closet


if __name__ == '__main__':
    s = Solution()
    assert (s.threeSumClosest([-1, 2, 1, -4], 1) == 2)
    assert (s.threeSumClosest([-1, 2, 1, -2], 1) == 1)
