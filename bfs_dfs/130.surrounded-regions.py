#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (23.05%)
# Total Accepted:    147.6K
# Total Submissions: 640.5K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
#

# [["O","X","O"],["X","O","X"],["O","X","O"]] => [["O","X","O"],["X","X","X"],["O","X","O"]]
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border(边境) of the board are not flipped（翻转） to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#
class Solution:
    def solve(self, board) -> None:
        """
        DFS
        - 从边界的‘O’出发，寻找有连接的‘O’
        - 没有被遍历过的‘O’都翻转为‘X’
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] == 'X':
                return
            visited[i][j] = True
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # 搜索边界
        # 第一行、最后一行
        for i in range(n):
            if board[0][i] == 'O' and not visited[0][i]:
                dfs(0, i)
            if board[m - 1][i] == 'O' and not visited[m - 1][i]:
                dfs(m - 1, i)
        # 第一列、最后一列
        for i in range(m):
            if board[i][0] == 'O' and not visited[i][0]:
                dfs(i, 0)
            if board[i][n - 1] == 'O' and not visited[i][n - 1]:
                dfs(i, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    visited[i][j] = True
                    board[i][j] = 'X'

    # def solve(self, board) -> None:
    #     """
    #     BFS；
    #     - 先搜索边界,记录visit
    #     - 再搜索内部，遇到'0'，则翻转
    #     :param board:
    #     :return:
    #     """
    #     m = len(board)
    #     if m == 0:
    #         return
    #     n = len(board[0])
    #     visit = [[False] * n for _ in range(m)]
    #     from collections import deque
    #
    #     def bfs(i, j):
    #         q = deque()
    #         q.append([i, j])
    #         while q:
    #             i, j = q.popleft()
    #             if i >= 1 and board[i - 1][j] == 'O' and not visit[i - 1][j]:
    #                 visit[i - 1][j] = True
    #                 q.append([i - 1, j])
    #             if i + 1 < m and board[i + 1][j] == 'O' and not visit[i + 1][j]:
    #                 visit[i + 1][j] = True
    #                 q.append([i + 1, j])
    #             if j >= 1 and board[i][j - 1] == 'O' and not visit[i][j - 1]:
    #                 visit[i][j - 1] = True
    #                 q.append([i, j - 1])
    #             if j + 1 < n and board[i][j + 1] == 'O' and not visit[i][j + 1]:
    #                 visit[i][j + 1] = True
    #                 q.append([i, j + 1])
    #
    #     # 搜索边界
    #     # 第一行,最后一行
    #     for i in range(n):
    #         if board[0][i] == 'O' and visit[0][i] == False:
    #             visit[0][i] = True
    #             bfs(0, i)
    #         if board[m - 1][i] == 'O' and visit[m - 1][i] == False:
    #             visit[m - 1][i] = True
    #             bfs(m - 1, i)
    #     # 第一列,最后一列
    #     for i in range(m):
    #         if board[i][0] == 'O' and visit[i][0] == False:
    #             visit[i][0] = True
    #             bfs(i, 0)
    #         if board[i][n - 1] == 'O' and visit[i][n - 1] == False:
    #             visit[i][n - 1] = True
    #             bfs(i, n - 1)
    #
    #     # 搜索内部，把没有visit过的'O'置为'X'
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == 'O' and visit[i][j] == False:
    #                 board[i][j] = 'X'

    # def solve(self, board) -> None:
    #     """
    #     BFS搜索
    #     - 将'O'加入队列，搜索过的都记为visited
    #     - 搜索完毕，如果没有'O'在边界上，则将所有'O'转换为'X'
    #     要分两步，效率低
    #     :param board:
    #     :return:
    #     """
    #     m = len(board)
    #     if m == 0:
    #         return
    #     n = len(board[0])
    #     visited = [[False] * n for _ in range(m)]
    #     from collections import deque
    #     q1 = deque()
    #     q2 = deque()
    #     for i in range(m):
    #         for j in range(n):
    #             if_flip = True
    #             if not visited[i][j] and board[i][j] == 'O':
    #                 q1.append([i, j])
    #                 q2.append([i, j])
    #                 visited[i][j] = True
    #                 if i == 0 or i == m - 1 or j == 0 or j == n - 1:
    #                     if_flip = False
    #
    #                 while q1:
    #                     x, y = q1.popleft()
    #                     if x - 1 >= 0 and not visited[x - 1][y] and board[x - 1][y] == 'O':
    #                         q1.append([x - 1, y])
    #                         q2.append([x - 1, y])
    #                         visited[x - 1][y] = True
    #                         if if_flip and x - 1 == 0:
    #                             if_flip = False
    #                     if x + 1 < m and not visited[x + 1][y] and board[x + 1][y] == 'O':
    #                         q1.append([x + 1, y])
    #                         q2.append([x + 1, y])
    #                         visited[x + 1][y] = True
    #                         if if_flip and x + 1 == m - 1:
    #                             if_flip = False
    #                     if y - 1 >= 0 and not visited[x][y - 1] and board[x][y - 1] == 'O':
    #                         q1.append([x, y - 1])
    #                         q2.append([x, y - 1])
    #                         visited[x][y - 1] = True
    #                         if if_flip and y - 1 == 0:
    #                             if_flip = False
    #                     if y + 1 < n and not visited[x][y + 1] and board[x][y + 1] == 'O':
    #                         q1.append([x, y + 1])
    #                         q2.append([x, y + 1])
    #                         visited[x][y + 1] = True
    #                         if if_flip and y + 1 == n - 1:
    #                             if_flip = False
    #
    #                 while q2:
    #                     x, y = q2.popleft()
    #                     if if_flip:
    #                         board[x][y] = 'X'


if __name__ == '__main__':
    s = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s.solve(board)
    print(board)
    board = [["O", "X", "O"], ["X", "O", "X"], ["O", "X", "O"]]
    s.solve(board)
    print(board)
