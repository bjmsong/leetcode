"""
Q: 剪绳子

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m]
可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

测试用例：

"""


class Solution:

    def cuttingRope(self, n):
        """
        动态规划: f(n) = max(f(i)*f(n-i))
        自下而上计算
        不要递归，会大量重复计算
        时间复杂度：O(n^2)
        空间复杂度：O(n)
        :param n:
        :return:
        """
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        products = [1] * (n + 1)
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        for i in range(4, n + 1):
            max = 0
            for j in range(1, i // 2 + 1):
                products[i] = products[j] * products[i - j]
                if max < products[i]:
                    max = products[i]
            products[i] = max

        return products[n]

    def cuttingRope(self, n):
        """
        贪心算法
        当n>5,2(n-2)>n,3(n-3)>n,3(n-3)>2(n-2) => 尽量将绳子切成2或者3的段,优先切成3
        当n=4,切成2+2比3+1乘积更大
        时间复杂度：O(n)
        空间复杂度：O(1)
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
        return pow(3, three) * pow(2, two)


if __name__ == '__main__':
    s = Solution()
    assert (s.cuttingRope(10) == 36)
