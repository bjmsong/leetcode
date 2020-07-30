#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (41.55%)
# Total Accepted:    220.4K
# Total Submissions: 530.2K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
# https://www.jianshu.com/p/79b05c2bfdbc

class Solution:

    def combinationSum2(self, candidates, target: int):

        def dfs(temp, residuals, index):
            if residuals < 0:
                return
            if residuals == 0:
                temp_copy = temp.copy()
                result.append(temp_copy)
                return
            for i in range(index, len(candidates)):
                val = candidates[i]
                if val > residuals:
                    return
                if i > index and candidates[i - 1] == val:  # 本轮搜索跳过重复元素
                    continue
                temp.append(val)
                dfs(temp, residuals - val, i + 1)  # index+1: 不取重复值
                temp.pop()

        result = []
        candidates.sort()
        dfs([], target, 0)
        return result

    # def combinationSum2(self, candidates, target: int):
    #     """
    #     DFS
    #     :param candidates:
    #     :param target:
    #     :return:
    #     """
    #     candidates.sort()
    #     result = set()
    #
    #     def dfs(residuals, temp, index):
    #         if residuals == 0:
    #             tempc = temp.copy()
    #             result.add(tuple(tempc))
    #         if residuals > 0:
    #             for i in range(index, len(candidates)):
    #                 val = candidates[i]
    #                 if val > residuals:
    #                     return
    #                 temp.append(val)
    #                 dfs(residuals - val, temp, i + 1)
    #                 temp.pop()
    #
    #     dfs(target, [], 0)
    #     result = [list(item) for item in result]
    #     return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(s.combinationSum2([2, 5, 2, 1, 2], 5))
