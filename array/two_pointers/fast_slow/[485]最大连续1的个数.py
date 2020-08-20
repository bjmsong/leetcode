# 给定一个二进制数组， 计算其中最大连续1的个数。 
# 
#  示例 1: 
# 
#  
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#  
# 
#  注意： 
# 
#  
#  输入的数组只包含 0 和1。 
#  输入数组的长度是正整数，且不超过 10,000。 
#  
#  Related Topics 数组


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        """
        - 快指针找到1
        - 慢指针指向第一个1
        - 快指针继续前进，直到1的末尾
        - 计算连续1的个数=fast-slow
        """
        fast = 0
        length = 0
        while fast < len(nums):
            while fast < len(nums) and nums[fast] != 1:
                fast += 1
            slow = fast
            while fast < len(nums) and nums[fast] == 1:
                fast += 1
            if fast - slow > length:
                length = fast - slow

        return length


if __name__ == '__main__':
    s = Solution()
    assert (s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3)
