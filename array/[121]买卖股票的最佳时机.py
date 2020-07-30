# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。 
# 
#  如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。 
# 
#  注意：你不能在买入股票前卖出股票。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#  
# 
#  示例 2: 
# 
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#  
#  Related Topics 数组 动态规划


class Solution:
    def maxProfit(self, prices) -> int:
        """
        记录截止当天的历史最低价格：在历史最低价买入，在当天卖出
        时间复杂度：O(n)
        """
        if not prices:
            return 0
        max_margin = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            max_margin = max(max_margin, price - min_price)

        return max_margin

    # def maxProfit(self, prices) -> int:
    #     """
    #     找出数组中两个数字之间的最大差值
    #     暴力解法
    #     时间复杂度：O(n^2)
    #     """
    #     if not prices:
    #         return 0
    #     max_margin = 0
    #     min_price = prices[0] + 1
    #     for i in range(len(prices)):
    #         if prices[i] < min_price:
    #             for j in range(i + 1, len(prices)):
    #                 val = prices[j] - prices[i]
    #                 if val > max_margin:
    #                     max_margin = val
    #             min_price = prices[i]
    #
    #     return max_margin


if __name__ == '__main__':
    s = Solution()
    assert (s.maxProfit([7, 1, 5, 3, 6, 4]) == 5)
    assert (s.maxProfit([7, 6, 4, 3, 1]) == 0)
