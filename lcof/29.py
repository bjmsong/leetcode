"""
顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
"""


class Solution:


    def spiralOrder(self, matrix):
        """
        遍历顺序：右->下->左->上
        思路：遍历过的标记为visited，遍历遇到边界/已经访问过的则换方向
        :param matrix:
        :return:
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        traversal = []
        visited = [[False] * n for _ in range(m)]
        i, j = 0, 0
        visited[i][j] = True
        traversal.append(matrix[i][j])
        order = 0  # 0:右,1:下,2:左,0:上
        num = 1  # 遍历的元素个数
        while num < m * n:
            if order % 4 == 0:
                while j < n - 1 and not visited[i][j + 1]:
                    j += 1
                    traversal.append(matrix[i][j])
                    visited[i][j] = True
                    num += 1
            if order % 4 == 1:
                while i < m - 1 and not visited[i + 1][j]:
                    i += 1
                    traversal.append(matrix[i][j])
                    visited[i][j] = True
                    num += 1
            if order % 4 == 2:
                while j > 0 and not visited[i][j - 1]:
                    j -= 1
                    traversal.append(matrix[i][j])
                    visited[i][j] = True
                    num += 1
            if order % 4 == 3:
                while i > 0 and not visited[i - 1][j]:
                    i -= 1
                    traversal.append(matrix[i][j])
                    visited[i][j] = True
                    num += 1
            order += 1

        return traversal

    # def spiralOrder(self, matrix):
    #     """
    #     思路：
    #     - 第一轮：右(n)->下(m-1)->左(n-1)->上(m-2)
    #     - 第二轮：右(n-2)->下(m-3)->左(n-3)->上(m-4)
    #     - 直到为0
    #     :param matrix:
    #     :return:
    #     """
    #     m = len(matrix)
    #     if m == 0:
    #         return []
    #     n = len(matrix[0])
    #     traversal = []
    #     0, n-1
    #
    #
    #     return traversal





if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    traversal = s.spiralOrder(matrix)
    print(traversal)
