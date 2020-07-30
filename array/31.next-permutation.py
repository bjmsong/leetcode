#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (30.47%)
# Total Accepted:    237.4K
# Total Submissions: 779.1K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution:
    """
    Do not return anything, modify nums in-place instead.
    permutation: 排列方式
    lexicographically：字典序：逐个比较，小的放前面，如： 123,132,213,231,312,321
    """

    def nextPermutation(self, nums):
        """
        思路：
        step1: 从右边往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
        step2: 再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换
        step3: 将partition后的元素（不包括partition指向的元素）反转，按升序排列
        时间复杂度：O(n)
        """
        length = len(nums)
        if length <= 1:
            return
        partition = -1
        for i in reversed(range(1, length)):  # 从右边开始遍历
            if nums[i - 1] < nums[i]:  # 找到相邻升序元素
                partition = i - 1
                for j in reversed(range(i, length)):  # 从右边开始遍历，找到更大的元素
                    if nums[j] > nums[partition]:
                        nums[partition], nums[j] = nums[j], nums[partition]  # 交换
                        break
                break
        left = partition + 1
        right = length - 1
        while left <= right:  # 反转之后的元素：降序->升序
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 5, 4, 3]
    s.nextPermutation(nums)
    assert (nums == [1, 3, 2, 4, 5])
    nums = [1, 3, 2]
    s.nextPermutation(nums)
    assert (nums == [2, 1, 3])
    nums = [1, 2, 3]
    s.nextPermutation(nums)
    assert (nums == [1, 3, 2])
    nums = [3, 2, 1]
    s.nextPermutation(nums)
    assert (nums == [1, 2, 3])
    nums = [1, 1, 5]
    s.nextPermutation(nums)
    assert (nums == [1, 5, 1])
