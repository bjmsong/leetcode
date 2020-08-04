"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        """
        双指针，一个记录奇数的位置，一个记录偶数的位置
        """
        length = len(nums)
        if length <= 1:
            return nums
        odd = 0
        even = length - 1
        while odd < even:
            if nums[odd] % 2 == 1:
                odd += 1
            else:
                nums[odd], nums[even] = nums[even], nums[odd]
                even -= 1

        return nums


if __name__ == '__main__':
    pass
