#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (41.79%)
# Total Accepted:    366.3K
# Total Submissions: 876.5K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#
class Solution:

    def numIslands(self, grid) -> int:
        """
        - 遍历grid，从遇到1开始，搜索相邻的1，直到没有1
            - BFS，把1加入队列中，直到队列为空，标记已经访问过的
        - 继续遍历grid，搜索1
        - 有几组1就是几个岛屿
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        from collections import deque
        q = deque()
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q.append([i, j])
                    grid[i][j] = 0  # 标记为0的就不会再访问了，起到了visited数组的作用
                    cnt += 1
                while q:
                    x, y = q.popleft()
                    if x + 1 < m and grid[x + 1][y] == '1':
                        q.append([x + 1, y])
                        grid[x + 1][y] = 0
                    if x - 1 >= 0 and grid[x - 1][y] == '1':
                        q.append([x - 1, y])
                        grid[x - 1][y] = 0
                    if y + 1 < n and grid[x][y + 1] == '1':
                        q.append([x, y + 1])
                        grid[x][y + 1] = 0
                    if y - 1 >= 0 and grid[x][y - 1] == '1':
                        q.append([x, y - 1])
                        grid[x][y - 1] = 0

        return cnt

    # def numIslands(self, grid) -> int:
    #     """
    #     DFS
    #     """
    #     def dfs(i, j):
    #         if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
    #             return
    #         grid[i][j] = 0  # 不需要visited矩阵
    #         dfs(i - 1, j)
    #         dfs(i + 1, j)
    #         dfs(i, j - 1)
    #         dfs(i, j + 1)
    #
    #     if not grid:
    #         return 0
    #     m = len(grid)
    #     n = len(grid[0])
    #     cnt = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == "1":
    #                 cnt += 1
    #                 dfs(i, j)
    #
    #     return cnt


if __name__ == '__main__':
    s = Solution()
    num = s.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
    print(num)
