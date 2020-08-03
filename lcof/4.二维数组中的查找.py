"""
Q：二维数组中的查找
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的数学排序
判断数组中是否含有该整数

测试用例：
[] -> None
[[1,2],[2,3]],2 -> True
[[1,2],[2,3]],4 -> False
"""

def findNumber(matrix, value):
    """
    每次跟右上角数字（num）比较,如果value>num,则排除num所在的行，如果value<num，则排除num所在的列
    时间复杂度：O(m+n) m,n分别是行号、列号
    空间复杂度：O(1)
    :param matrix:
    :param value:
    :return:
    """
    if len(matrix) == 0:
        return
    # 右上角数字的行号,列号
    row, col = 0, len(matrix[0]) - 1
    while row <= len(matrix) - 1 and col >= 0:
        if value == matrix[row][col]:
            return True
        elif value > matrix[row][col]:
            row += 1
        else:
            col -= 1

    return False


if __name__ == '__main__':
    for matrix, value in zip(
            [[], [[1, 2], [2, 3]], [[1, 2], [2, 3]], [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]],
            (2, 2, 4, 7)):
        result = findNumber(matrix, value)
        print("{},{} -> {}".format(matrix, value, result))
