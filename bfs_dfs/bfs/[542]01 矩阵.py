# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。 
# 
#  两个相邻元素间的距离为 1 。 
# 
#  示例 1: 
# 输入: 
# 
#  
# 0 0 0
# 0 1 0
# 0 0 0
#  
# 
#  输出: 
# 
#  
# 0 0 0
# 0 1 0
# 0 0 0
#  
# 
#  示例 2: 
# 输入: 
# 
#  
# 0 0 0
# 0 1 0
# 1 1 1
#  
# 
#  输出: 
# 
#  
# 0 0 0
# 0 1 0
# 1 2 1
#  
# 
#  注意: 
# 
#  
#  给定矩阵的元素个数不超过 10000。 
#  给定矩阵中至少有一个元素是 0。 
#  矩阵中的元素只在四个方向上相邻: 上、下、左、右。 
#  
#  Related Topics 深度优先搜索 广度优先搜索


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # 在矩阵的每个位置做bfs:直到遇到0
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        from collections import deque

        for i in range(m):
            for j in range(n):
                q = deque()
                q.append([i, j, 0])
                while q:
                    x, y, d = q.popleft()
                    # 判断是否超出矩阵范围
                    if x < 0 or x == m or y < 0 or y == n:
                        continue
                    if matrix[x][y] == 0:
                        dist[i][j] = d
                        break
                    q.append([x - 1, y, d + 1])
                    q.append([x + 1, y, d + 1])
                    q.append([x, y - 1, d + 1])
                    q.append([x, y + 1, d + 1])

        return dist
