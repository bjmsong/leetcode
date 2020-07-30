#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (46.51%)
# Total Accepted:    173.4K
# Total Submissions: 372.5K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,3,2]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [0,1,0,1,0,1,99]
# Output: 99
# 
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 时间复杂度：nlgn+n

        length = len(nums)
        if length == 0:
            return
        if length == 1:
            return nums[0]

        nums.sort()  # [0 0 0 1 1 1 99]

        # 遍历
        i = 0
        while i <= length - 2:
            if nums[i] == nums[i + 2]:
                i += 3
            else:
                break

        return nums[i]

    # def singleNumber(self, nums: List[int]) -> int:
    # # https://shenjie1993.gitbooks.io/leetcode-python/137%20Single%20Number%20II.html
    # # 一个包含32个元素（因为int型数值为32位）的数组来记录每一个位出现的次数
    #     result = 0
    #     for i in range(32):
    #         count = 0
    #         for num in nums:
    #             count += (num >> i) & 1  # >> 右移动运算符
    #         rem = count % 3
    #         # deal with the negative situation
    #         if i == 31 and rem:
    #             result -= 1 << 31
    #         else:
    #             result |= rem << i
    #     return result

    # def singleNumber(self, nums: List[int]) -> int:
    #     # 存储每个位上出现1，2，3次的情况
    #     one, two, three = 0, 0, 0
    #     for num in nums:
    #         # calculate the count of the each bit
    #         two = two | (one & num)    #  # two为1时，不管num是什么，two都为1
    #         one = one ^ num  # one=0 -> num , one=num -> 0 , one!=num!=0 -> one^num
    #         three = one & two
    #         # clear the count for the bit which has achieved three -- 三进制
    #         one = one & ~three  # three = 0 -> one , three = 1 -> 0
    #         two = two & ~three
    #         print(one, two, three)
    #     return one
