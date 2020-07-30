"""
目标和
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 - 中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
"""


class Solution:
    """
    图搜索问题：
    - 节点值是距离目标的残差(residuals)
    - 相邻节点是(+,-)数组的下一个数
    """

    def findTargetSumWays(self, nums, S: int) -> int:
        """
        DFS
        缓存
        """
        import functools

        @functools.lru_cache(None)  # 缓存函数结果，避免重复计算
        def dfs(idx, residuals):
            if idx == len(nums):
                return [0, 1][residuals == 0]
            return dfs(idx + 1, residuals - nums[idx]) + dfs(idx + 1, residuals + nums[idx])

        return dfs(0, S)

    # def findTargetSumWays(self, nums, S: int) -> int:
    #     """
    #     从第一个元素开始遍历，用字典存储不同目标数对应的组合数
    #     时间复杂度：～O(n^2)
    #     :param nums:
    #     :param S:
    #     :return:
    #     """
    #     import collections
    #     # key:目标数,val:组合的方法数，用字典而不是列表，可以大大减少值的数量 : 2^n -> ~n
    #     c = collections.defaultdict(int)
    #     c[0] = 1
    #     for num in nums:
    #         nxt = collections.defaultdict(int)  # 创建一个字典，因为后面的for循环，不能在原字典上直接改
    #         for k, v in c.items():
    #             nxt[k - num] += v
    #             nxt[k + num] += v
    #         c = nxt
    #     return c[S]

    # def __init__(self):
    #     self.cnt = 0
    #
    # def findTargetSumWays(self, nums, S: int) -> int:
    #     """
    #     暴力解法
    #     时间复杂度：O(2^n)
    #     :param nums:
    #     :param S:
    #     :return:
    #     """
    #
    #     def search(index, val):
    #         if index == len(nums):
    #             for v in val:
    #                 if v == S:
    #                     self.cnt += 1
    #             return self.cnt
    #         temp = []
    #         for v in val:
    #             for new in [nums[index], -nums[index]]:
    #                 temp.append(v + new)
    #         val = temp.copy()
    #         search(index + 1, val)
    #
    #     search(1, [nums[0], -nums[0]])
    #     return self.cnt


if __name__ == '__main__':
    s = Solution()
    assert (s.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5)
