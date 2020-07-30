"""
零矩阵
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        按行遍历，找到0，则将该行变0，记录列index
        最后将列变0
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        col = []

        for i in range(m):
            contain_zero = False
            for j in range(n):
                if matrix[i][j] == 0:
                    contain_zero = True
                    col.append(j)
            if contain_zero:
                matrix[i][:] = [0]*n
        for c in col:
            for i in range(m):
                matrix[i][c] = 0


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    s.setZeroes(matrix)
    print(matrix)
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(matrix)
    print(matrix)
