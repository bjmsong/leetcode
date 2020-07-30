"""
寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。
"""


class Solution:

    def getKth(self, A, B, k):
        """
        寻找第k小的值：丢掉k-1个最小的数，剩下的最小的数就是第k小数
        思路：折半删除，递归，双指针
        - 指针1指向nums1数组k/2的位置a，指针2指向nums2数组k/2的位置b,如果a<b，那么a左边的部分一定不包含中位数，可以丢弃
        - 更新k = k - k/2，更新指针，继续上面的步骤
        - 直到k == 1
        """

        lenA = len(A)
        lenB = len(B)
        # 把较短的数组放在前面
        if lenA > lenB:
            return self.getKth(B, A, k)
        if lenA == 0:    # 递归结束的基线条件
            return B[k - 1]
        if k == 1:       # 递归结束的基线条件
            return min(A[0], B[0])
        pa = min(k // 2, lenA)
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        中位数 <=> 第k小数
        时间复杂度：O(log(m+n))
        空间复杂度：O(1)
        """
        lenA = len(nums1)
        lenB = len(nums2)
        k = lenA + lenB
        if k % 2 == 1:
            return self.getKth(nums1, nums2, k // 2 + 1)
        else:
            return (self.getKth(nums1, nums2, k // 2) + self.getKth(nums1, nums2, k // 2 + 1)) * 0.5


if __name__ == '__main__':
    s = Solution()
    assert (s.findMedianSortedArrays([1, 2, 3], []) == 2)
    assert (s.findMedianSortedArrays([], [1, 2, 3, 4]) == 2.5)
    assert (s.findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]) == 6)
    assert (s.findMedianSortedArrays([1, 2, 3], [1, 1, 4, 5]) == 2)
    assert (s.findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13]) == 7)
    assert (s.findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 7)
    assert (s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5)
    assert (s.findMedianSortedArrays([2, 3, 4], [1]) == 2.5)
