#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#
# https://leetcode.com/problems/two-city-scheduling/description/
#
# algorithms
# Easy (54.20%)
# Total Accepted:    11.1K
# Total Submissions: 20.4K
# Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
#
# There are 2N people a company is planning to interview. The cost of flying
# the i-th person to city A is costs[i][0], and the cost of flying the i-th
# person to city B is costs[i][1].
# 
# Return the minimum cost to fly every person to a city such that exactly N
# people arrive in each city.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# 
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
# interviewing in each city.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000
# 
#
class Solution:
    # def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    #     # 将costs按差值大小逆序排序
    #     costs.sort(key=lambda tup: abs(tup[1]-tup[0]), reverse=True)
    #     # 依次分配飞A、B的人
    #     length = len(costs)
    #     a = 0
    #     b = 0
    #     index = 0
    #     sum = 0
    #     while a<length/2 and b<length/2:
    #         if costs[index][0]<costs[index][1]:
    #             a += 1
    #             sum += costs[index][0]
    #         else:
    #             b += 1
    #             sum += costs[index][1]
    #         index += 1
        
    #     # 人数不够，则补齐
    #     while a<length/2 and index<length:
    #         sum += costs[index][0]
    #         index += 1
    #     while b<length/2 and index<length:
    #         sum += costs[index][1]
    #         index += 1

    #     return sum
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 按cost(A)-cost(B)顺序排序
        costs.sort(key=lambda tup: tup[0]-tup[1])
        sum = 0
        n = len(costs)//2  # "/"得到的是float
        # 精炼！
        for i in range(n):
            sum += costs[i][0] + costs[i+n][1]

        return sum



