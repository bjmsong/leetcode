# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。 
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。 
# 
#  
# 
#  示例： 
# 
#  matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
# 
# 返回 13
#
# matrix = [
#  [1, 3, 5],
#  [6, 7, 12],
#  [11, 14, 14]
#  ],
#
# k = 3
#
# 返回 5
#  
# 
#  提示： 
# 你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。 
#  Related Topics 堆 二分查找




class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        排除k-1个最小的数，剩下的最小的数就是第k小数

        """

    matrix = [
     [1, 3, 5],
     [6, 7, 12],
     [11, 14, 14]
     ],

    k = 3












    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     """
    #     第k小数位于（左上角开始的）对角线的第k**0.5个数所在的行和列
    #     """
    #     idx = int(k ** 0.5)  # 第k小数所在行/列的索引
    #     k -= idx ** 2  # 在第idx行+第idx列中寻找第k小数
    #     if k == 0:
    #         return matrix[idx - 1][idx - 1]
    #     i, j = 0, 0  # 第idx列的行索引，第idx行的列索引
    #     for _ in range(k - 1):
    #         if matrix[i][idx] <= matrix[idx][j]:
    #             i += 1
    #         else:
    #             j += 1
    #
    #     if matrix[i][idx] <= matrix[idx][j]:
    #         return matrix[i][idx]
    #     else:
    #         return matrix[idx][j]
