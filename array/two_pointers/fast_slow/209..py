"""
长度最小的子数组

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。
如果不存在符合条件的连续子数组，返回 0。

例如：
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

进阶:
如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""


class Solution:
    def minSubArrayLen(self, s: int, nums):
        """
        快慢指针
        - 快指针前进，和大于等于s则停止前进
        - 慢指针前进，直到和小于s
        - 重复上面两步，直到快指针达到数组末尾 and 慢指针追上快指针
        时间复杂度：O(n)
        """
        slow, fast = 0, 0
        sum = 0
        min_length = len(nums)
        length = 0
        while fast < len(nums) or slow < fast:
            if sum < s and fast < len(nums):  # 快指针前进
                sum += nums[fast]
                fast += 1
            elif sum >= s:                    # 和大于s，慢指针前进
                length = fast - slow
                if length < min_length:
                    min_length = length
                sum -= nums[slow]
                slow += 1
            else:   # 快指针已达到数组末尾，慢指针前进
                slow += 1
        if length == 0:
            return 0

        return min_length


if __name__ == '__main__':
    s = Solution()
    assert (s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2)
    assert (s.minSubArrayLen(100, [2, 3, 1, 2, 4, 3]) == 0)
    assert (s.minSubArrayLen(1, []) == 0)
    assert (s.minSubArrayLen(1, [1]) == 1)
