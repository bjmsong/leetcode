class Solution:
    def maxDrawdown(self, prices) -> int:
        # 记录截止当前的最大值
        max_price = prices[0]
        max_drawdown_ratio = 0
        for price in prices:
            max_price = max(price, max_price)
            max_drawdown_ratio = max(max_drawdown_ratio, (max_price - price)/max_price)

        return max_drawdown_ratio

    # def maxDrawdown(self, lst):
    #     import numpy as np
    #     i = np.argmax((np.maximum.accumulate(lst) - lst) / lst)
    #     # 极端情况，没有回撤
    #     if i == 0:
    #         return 0
    #     j = np.argmax(lst[:i])
    #     return (lst[j] - lst[i]) / lst[j]

    # def MaxDrawdown(return_list):
    #     '''最大回撤率
    #     复杂度
    #     1. 找到截止当前的最大值：n
    #     2. 计算回撤值：n
    #     3. 计算最大回撤：n
    #     '''
    #     # np.argmax : 返回最大数的索引
    #     # np.maximum.accumulate : 从左到右,记录列表当前的最大值
    #     i = np.argmax((np.maximum.accumulate(return_list) - return_list) / np.maximum.accumulate(return_list))  # 结束位置
    #     if i == 0:
    #         return 0
    #     j = np.argmax(return_list[:i])  # 开始位置
    #     return (return_list[j] - return_list[i]) / (return_list[j])


if __name__ == '__main__':
    s = Solution()
    return_list = [12, 12, 21, 15, 5, 27, 16, 21, 22, 25, 20, 16, 17]
    print(s.maxDrawdown(return_list))
