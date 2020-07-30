# 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 
# 的 min(ai, bi) 总和最大。 
# 
#  示例 1: 
# 
#  
# 输入: [1,4,3,2]
# 
# 输出: 4
# 解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
#  
# 
#  提示: 
# 
#  
#  n 是正整数,范围在 [1, 10000]. 
#  数组中的元素范围在 [-10000, 10000]. 
#  
#  Related Topics 数组


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        同一对中两个数差距越小越好
        先排序，相邻两个数成一组
        """
        nums.sort()
        i = 0
        sum = 0
        while i < len(nums):
            sum += nums[i]
            i += 2

        return sum

