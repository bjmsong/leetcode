"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
"""


class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        # 逐行计算
        # 时间复杂度：O(k^2)
        # 空间复杂度：O(k)
        if rowIndex == 0:
            return [1]
        before = []
        for i in range(1, rowIndex + 1):
            cur = [0] * (i + 1)
            cur[0] = 1
            cur[i] = 1
            for i in range(len(before) - 1):
                cur[i + 1] = before[i] + before[i + 1]
            before = cur

        return cur
