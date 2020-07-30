"""
Q: 数值的整数次方
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

测试用例：

"""


class Solution:
    g_isvalidInput = True

    def power(self, x, n):
        val = 1
        while n > 0:
            val = x * val
            n -= 1
        return val

    def power(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        result = self.power(x, n >> 1)  # 正数，右移运算可以代替除2
        result *= result
        if n % 2 == 1:
            result = result * x

        return result

    def myPow(self, x: float, n: int) -> float:
        """
        当n是偶数：pow(x,n) = pow(x,n//2) * pow(x,n//2)
        当n是奇数：pow(x,n) = pow(x,n//2) * pow(x,n//2) * x
        :param x:
        :param n:
        :return:
        """
        if x == 1:
            return 1
        if x == 0 and n <= 0:
            g_isvalidInput = False
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.power(x, abs(n))
        if n > 0:
            return self.power(x, n)


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2, 3))
    print(s.myPow(2, 0))
    print(s.myPow(2, -2))
