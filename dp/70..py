"""
爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        fn, fn_1, fn_2 = n, 2, 1
        for i in range(2, n):
            fn = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = fn

        return fn
