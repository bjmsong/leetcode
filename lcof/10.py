"""
Q: 斐波那契数列
"""


class Solution:

    def fib(self, n):
        """
        从下往上计算
        时间复杂度：O(n)
        空间复杂度：O(1)
        :param n:
        :return:
        """
        if n <= 1:
            return n
        fibn = 0
        fibn_minus_one = 1
        fibn_minus_two = 0
        for i in range(2, n + 1):
            fibn = fibn_minus_one + fibn_minus_two
            fibn_minus_two = fibn_minus_one
            fibn_minus_one = fibn

        # 取模
        if fibn > 1000000007:
            fibn = fibn % 1000000007

        return fibn

    def fib_1(self, n):
        """
        画递归树，可以看到有大量的重复计算
        时间复杂度：O(2^n)
        :param n:
        :return:
        """
        if n <= 1:
            return n
        return self.fib_1(n - 1) + self.fib_1(n - 2)

if __name__ == '__main__':
    s = Solution()
    print(s.fib(100))
