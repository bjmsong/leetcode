"""
5488. 使数组中所有元素相等的最小操作数
"""


class Solution:
    def minOperations(self, n: int) -> int:
        # 找出平均数
        if n % 2 == 1:
            avg = 2 * (n // 2) + 1
        else:
            avg = 2 * (n // 2) + 1 - 1
        # 比较前半部分数和avg的差距
        step = 0
        for i in range(n // 2):
            step += avg - (2 * i + 1)

        return step


if __name__ == '__main__':
    s = Solution()
    assert (s.minOperations(3) == 2)
    assert (s.minOperations(6) == 9)
