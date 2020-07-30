#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.99%)
# Total Accepted:    549.3K
# Total Submissions: 2.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     """
    #     - 先排序
    #     - 遍历数组，得到a
    #     - 在剩下的元素里面寻找 b+c = -a : 双指针从首尾逼近
    #     - 跳过重复组合
    #     """
    #     length = len(nums)
    #     if length < 3:
    #         return []
    #     nums.sort()
    #     result = set()
    #     for i in range(length - 2):
    #         left, right = i + 1, length - 1
    #         while left < right:
    #             if nums[left] + nums[right] == -nums[i]:
    #                 result.add((nums[i], nums[left], nums[right]))
    #                 left += 1
    #             elif nums[left] + nums[right] > -nums[i]:
    #                 right -= 1
    #             else:
    #                 left += 1
    #
    #     return list(result)
    #
    # def threeSum_1(self, nums):
    #     """
    #     思路：转换为two sum -- find a+b = -c
    #     双指针从头尾开始逼近
    #     时间复杂度：O(nlogn+n^2)=O(n^2)
    #     空间复杂度：O(n)
    #     """
    #     if len(nums) < 3:
    #         return
    #     nums.sort()
    #     result = dict()  # 三元组不可以重复
    #     for i in range(len(nums) - 2):
    #         target = -nums[i]
    #         begin = i + 1
    #         end = len(nums) - 1
    #         while begin < end:
    #             val = nums[begin] + nums[end]
    #             if val == target:
    #                 key = (nums[i], nums[begin], nums[end])
    #                 result[key] = 1
    #                 begin += 1
    #             elif val > target:
    #                 end -= 1
    #             else:
    #                 begin += 1
    #     return list(result.keys())

    def threeSum(self, nums):
        """
        思路：转换为two sum -- find a+b = -c
        时间复杂度：O(n^2+nlogn)
        空间复杂度：
        """
        if len(nums) < 3:
            return
        nums.sort()
        solution = []
        length = len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # 重复的三元组不要
                continue
            target = -nums[i]
            begin = i + 1
            end = length - 1
            while begin < end:
                add = nums[begin] + nums[end]
                if add == target:
                    solution.append([nums[begin], nums[end], -target])
                    while begin < end and nums[begin] == nums[begin + 1]:  # 重复的三元组不要
                        begin += 1
                    while begin < end and nums[end] == nums[end - 1]:  # 重复的三元组不要
                        end -= 1
                    begin += 1  # index要继续向右移
                    end -= 1  # index要继续向右移
                elif add < target:
                    begin += 1
                else:
                    end -= 1
        return solution


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
