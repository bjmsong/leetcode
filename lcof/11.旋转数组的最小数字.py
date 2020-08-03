"""
Q:旋转数组的最小数字

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

测试用例：
[3,4,5,1,2] -> 1
[5,2,3,4] -> 2
[2,2,2,0,1] -> 0  有重复元素
[1,3,5] -> 1      旋转回到原数组
[1] -> 1
[] - None
"""


class Solution:
    def minArray(self, numbers):
        """
        旋转数组可以看成两个递增排序的子数组，而且前面的数组元组都大于等于后面数组的元素，最小元组刚好是两个数组的分界线
	    双指针: 第一个指针指向前面数组的元素，第二个指针指向后面数组的元组
        二分查找，每次缩小一半的范围，直到两个指针相邻
        时间复杂度：O(logn)
        空间复杂度：O(1)
        """
        if not numbers:
            return
        if len(numbers) == 1:
            return numbers[0]
        lo = 0
        hi = len(numbers) - 1
        if numbers[lo] < numbers[hi]:  # corner case: 旋转数组是数组本身
            return numbers[lo]
        while lo < hi:
            if hi - lo == 1:
                return numbers[hi]
            mid = (lo + hi) // 2
            if numbers[lo] == numbers[mid] == numbers[hi]:  # 无法用二分法缩小范围,只能用顺序查找
                return self.minInOrder(numbers, lo, hi)
            if numbers[mid] >= numbers[lo]:  # 中间元素位于前面的数组中，把搜索范围缩小到后半部分
                lo = mid
            if numbers[hi] >= numbers[mid]:  # 中间元素位于后面的数组中，把搜索范围缩小到前半部分
                hi = mid

    def minInOrder(self, numbers, lo, hi):
        min_value = numbers[lo]
        for i in range(lo + 1, hi + 1):
            if numbers[i] < min_value:
                min_value = numbers[i]
        return min_value


if __name__ == '__main__':
    s = Solution()
    assert (s.minArray([3, 4, 5, 1, 2]) == 1)
    assert (s.minArray([5, 2, 3, 4]) == 2)
    assert (s.minArray([]) == None)
    assert (s.minArray([1]) == 1)
    assert (s.minArray([2, 2, 2, 0, 1]) == 0)
    assert (s.minArray([1, 3, 5]) == 1)
    assert (s.minArray([3, 1, 3]) == 1)
