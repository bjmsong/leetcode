#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (48.44%)
# Total Accepted:    341.3K
# Total Submissions: 704.3K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#
class Solution:
    """
    转换成图的搜索问题：
    - 节点值是距离目标值的残差（residuals）
    - 相邻节点该节点之后的每个元素
    """
    def combinationSum(self, candidates, target):
        """
        DFS:比bfs快
        终止条件是遍历完所有的情况
        """
        def dfs(temp, residuals, index):
            """
            :param index: 记录当前索引，只遍历>=该索引的数
            """
            if residuals < 0:  # 路径错误，结束搜索
                return
            if residuals == 0:  # 找到解，结束搜索
                tempc = temp.copy()  # 如果直接添加，temp的改动会影响result！
                result.append(tempc)
                return
            for i in range(index, len(candidates)):
                if residuals < candidates[i]:
                    return
                temp.append(candidates[i])
                dfs(temp, residuals - candidates[i], i)  # 通过DFS搜索下一个元素
                temp.pop()    # 搜索完毕，将最新值去除，然后尝试下一个元素

        result = []
        candidates.sort()  # 原地排序,提高搜索效率
        dfs([], target, 0)

        return result

    # def combinationSum(self, candidates, target):
    #     """
    #     BFS
    #     """
    #     from collections import deque
    #     q = deque()
    #     q.append([target, [], 0])
    #     result = []
    #     candidates.sort()
    #     while q:
    #         residuals, temp, index = q.popleft()
    #         if residuals == 0:
    #             tempc = temp.copy()
    #             result.append(tempc)
    #         if residuals > 0:
    #             for i in range(index, len(candidates)):
    #                 val = candidates[i]
    #                 if val > residuals:
    #                     break
    #                 temp.append(val)
    #                 tempc = temp.copy()
    #                 q.append([residuals - val, tempc, i])
    #                 temp.pop()
    #
    #     return result

    # def combinationSum(self, candidates, target: int):
    #     """
    #
    #     """
    #     candidates.sort()
    #     dp = [[] for _ in range(target + 1)]  # dp[i]:和为i的组合
    #     dp[0].append([])
    #     for i in range(1, target + 1):  # 解可能的数字个数 (1 到 target)
    #         for j in range(len(candidates)):
    #             if candidates[j] > i:
    #                 break
    #             for k in range(len(dp[i - candidates[j]])):
    #                 temp = dp[i - candidates[j]][k][:]
    #                 if len(temp) > 0 and temp[-1] > candidates[j]:
    #                     continue
    #                 temp.append(candidates[j])
    #                 dp[i].append(temp)
    #     return dp[target]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 5], 8))
    print(s.combinationSum([2, 3, 6, 7], 7))
