"""
旋转图像

给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15, 13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

"""

"""
https://mp.weixin.qq.com/s?__biz=MzI2NjI5MzU2Nw==&mid=2247485331&idx=1&sn=ca09244eaa8de904844fd5e8ca7cd407&chksm=ea911fc3dde696d5077415e9ad97988a895a2354e72b989cfa2772978b07536652020c303aba&mpshare=1&scene=1&srcid=&sharer_sharetime=1591060020590&sharer_shareid=49581f7bdbef8664715f595bc62d7044&key=9e1b28d078f64d03ec392e3fe00a05ada37740851c7c95a0b1c38181ac22320ba0eb90bc39cbb00c57763d08b40dca74a1dd47f63e44cce7886e5126e22e12de5a24f144e2fb869991aae540f063db4a&ascene=1&uin=MjM1OTMwMzkwMA%3D%3D&devicetype=Windows+7+x64&version=62090070&lang=zh_CN&exportkey=AaljcRWvDgu%2FKBc5vwQOsKM%3D&pass_ticket=sZ12j%2F62P%2FGUnjGrqpYcPYwYa%2FNBtv8UP4ZwDRNFOY1m9FbIh%2FZ6UiAeq5UU7gcW
"""


class Solution:
    def rotate(self, matrix) -> None:
        """
        元素交换只发生在同一层边框的4个元素之间,并且这四个元素都分别位于一条边上
        - 交换最外层边框的元素
        - 交换内层边框的元素
        - 直到边框遍历完
        :param matrix:
        :return:
        """
        # 边框边界
        x, y = 0, len(matrix) - 1
        # 每一轮边框缩小一圈
        while x < y:
            # p：上边点/右边点 的索引, q：下边点/左边点 的索引
            p, q = x, y
            while p < y:
                temp = matrix[x][p]
                matrix[x][p] = matrix[q][x]
                matrix[q][x] = matrix[y][q]
                matrix[y][q] = matrix[p][y]
                matrix[p][y] = temp
                p += 1
                q -= 1
            x += 1
            y -= 1


if __name__ == '__main__':
    s = Solution()

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate(matrix)
    print(matrix)
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    s.rotate(matrix)
    print(matrix)
