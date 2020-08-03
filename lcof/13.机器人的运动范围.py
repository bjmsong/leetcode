"""
Q: 机器人的运动范围

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？

测试用例：

"""


class Solution:
    def movingCount(self, m, n, k):
        """
        bfs
        """

        def countValue(idx, jdx):
            val = 0
            while idx > 0:
                val += idx % 10
                idx //= 10
            while jdx > 0:
                val += jdx % 10
                jdx //= 10

            return val

        def bfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] == True or countValue(i, j) > k:
                return False
            visited[i][j] = True
            return True

        from collections import deque
        q = deque()
        q.append([0, 0])
        cnt = 0
        visited = [[False] * n for _ in range(m)]
        while q:
            i, j = q.popleft()
            if bfs(i, j):
                cnt += 1
                q.append([i - 1, j])
                q.append([i + 1, j])
                q.append([i, j - 1])
                q.append([i, j + 1])
        return cnt


# class Solution:
#     def countNumber(self, m, n):
#         cnt = 0
#         while m > 0:
#             cnt += m % 10
#             m = m // 10
#         while n > 0:
#             cnt += n % 10
#             n = n // 10
#         return cnt
#
#     def movingCount(self, m, n, k):
#         """
#         BFS:
#         :param m:
#         :param n:
#         :param k:
#         :return:
#         """
#         visited = [[False] * n for _ in range(m)]
#         from collections import deque
#         queue = deque()
#         queue.append([0, 0])
#         cnt = 1
#         visited[0][0] = True
#         while queue:
#             i, j = queue.popleft()
#             if i - 1 >= 0 and self.countNumber(i - 1, j) <= k and not visited[i - 1][j]:
#                 queue.append([i - 1, j])
#                 visited[i - 1][j] = True
#                 cnt += 1
#             if j - 1 >= 0 and self.countNumber(i, j - 1) <= k and not visited[i][j - 1]:
#                 queue.append([i, j - 1])
#                 visited[i][j - 1] = True
#                 cnt += 1
#             if i + 1 < m and self.countNumber(i + 1, j) <= k and not visited[i + 1][j]:
#                 queue.append([i + 1, j])
#                 visited[i + 1][j] = True
#                 cnt += 1
#             if j + 1 < n and self.countNumber(i, j + 1) <= k and not visited[i][j + 1]:
#                 queue.append([i, j + 1])
#                 visited[i][j + 1] = True
#                 cnt += 1
#
#         return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(2, 3, 1))
    print(s.movingCount(3, 1, 0))
