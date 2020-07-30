"""
下一个更大元素 II
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
如果不存在，则输出 -1

示例：
输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

"""


class Solution:
    def nextGreaterElements(self, nums):
        """
        - 将列表复制一倍，转换成“每日温度”（leetcode 739）的题型
        """
        nums = nums + nums
        stack = []
        result = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                small = stack.pop()
                result[small] = nums[i]
            stack.append(i)
        return result[:len(result) // 2]


if __name__ == '__main__':
    s = Solution()
    result = s.nextGreaterElements([1, 2, 1])
    print(result)
