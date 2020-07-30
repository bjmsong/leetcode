"""
杨辉三角

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
"""


class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(1, numRows):
            before = result[-1]  # 上一行
            temp = []            # 这一行
            temp.append(1)
            for j in range(1, len(before)):
                temp.append(before[j] + before[j - 1])
            temp.append(1)
            result.append(temp)

        return result

    # def generate(self, numRows: int) -> List[List[int]]:
    #     if numRows == 0:
    #         return []
    #     result = [[1]]
    #     for i in range(1, numRows):
    #         temp = [a + b for a, b in zip(result[-1] + [0], [0] + result[-1])]
    #         result.append(temp)
    #
    #     return result
