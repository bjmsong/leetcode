"""
Q: 青蛙跳台阶问题
"""


class Solution:
    def numWays(self, n):
        """
        设f(n)是跳上第n阶台阶的跳法数目，则f(n) = f(n-1)+f(n-2)，即斐波那契序列
        区别在于f(0)=1,而不是0
        :param n:
        :return:
        """
        if n <= 1:
            return 1
        fibn = 0
        fibn_minus_one = 1
        fibn_minus_two = 1
        for i in range(2, n + 1):
            fibn = fibn_minus_one + fibn_minus_two
            fibn_minus_two = fibn_minus_one
            fibn_minus_one = fibn

        if fibn > 1000000007:
            fibn %= 1000000007
        return fibn

    def climbStairs(self, n):
        """
        设n级台阶，跳了z次，x次跳两阶，y次跳一阶: z = x + y (1), n = 2x + y (2)
        z次跳跃中x次跳两阶的组合数为Cz(x)
        根据式(2),x的范围为(0,n/2)
        只需要遍历x的范围，把所有的组合数相加即可
        时间复杂度：O()
        空间复杂度：O()
        :param n:
        :return:
        """

        def fact(n):
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

        total = 0
        for x in range(n // 2 + 1):
            y = n - 2 * x
            z = x + y
            total += fact(z) / fact(x) / fact(z - x)
        return total


if __name__ == '__main__':
    s = Solution()
    print(s.numWays(10))
    print(s.climbStairs(10))
