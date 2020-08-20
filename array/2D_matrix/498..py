"""
对角线遍历

给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

"""


class Solution:

    def findDiagonalOrder(self, matrix):
        """
        每一轮遍历一条对角线,直到碰到边界为止
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        result = []
        up = True   # 标记沿对角线走的方向：向上 or 向下
        i = j = 0
        while i + j < m + n - 1:
            result.append(matrix[i][j])
            if not up:
                while i + 1 < m and j - 1 >= 0:
                    i += 1
                    j -= 1
                    result.append(matrix[i][j])
                if i < m - 1:
                    i += 1
                else:
                    j += 1
            else:
                while i - 1 >= 0 and j + 1 < n:
                    i -= 1
                    j += 1
                    result.append(matrix[i][j])
                if j < n - 1:
                    j += 1
                else:
                    i += 1
            up = not up

        return result


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert (s.findDiagonalOrder(matrix) == [1, 2, 4, 7, 5, 3, 6, 8, 9])
    matrix = ([[1, 2, 3]])
    assert (s.findDiagonalOrder(matrix) == [1, 2, 3])
    assert (s.findDiagonalOrder([]) == [])
    assert (s.findDiagonalOrder([[1]]) == [1])
    assert (s.findDiagonalOrder([[2, 5, 8], [4, 0, -1]]) == [2, 5, 4, 0, 8, -1])
    assert (s.findDiagonalOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [1, 2, 5, 9, 6, 3,
                                                                                                     4, 7, 10, 13, 14,
                                                                                                     11, 8, 12, 15, 16])
