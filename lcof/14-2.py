"""
Q: 剪绳子II
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。
请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

测试用例：

"""


class Solution:

    def cuttingRope(self, n: int) -> int:
        """

        :param n:
        :return:
        """
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        # 长度为3的绳子数量
        three = n // 3
        # 如果剩下的绳子长度为4，要剪成2*2
        if (n - three * 3) == 1:
            three -= 1
        two = (n - three * 3) // 2

        return (pow(3, three) * pow(2, two)) % 1000000007


if __name__ == '__main__':
    pass
