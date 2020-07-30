"""
整数拆分
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        products = [1] * (n + 1)
        for i in range(4):
            products[i] = i
        for i in range(4, n + 1):
            max = 0
            for j in range(1, i // 2 + 1):
                products[i] = products[j] * products[i - j]
                if max < products[i]:
                    max = products[i]
            products[i] = max

        return products[n]
