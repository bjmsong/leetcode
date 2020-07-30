"""
完全平方数:
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
"""


class Solution:
    def numSquares(self, n):
        """
        抽象成图的搜索问题： 起点是n，第一层节点是n-1，n-4,n-9....，第二层节点是n-1-1，n-1-4,n-1-9....,n-4-1,n-4-4,n-4-9,....
        问题转换成，从起点开始到节点值是0的节点的最短路径问题 -> bfs
        - 把residuals作为节点值，直到遇到值为0的节点
        - 值为residuals的相邻节点值为residuals-1，residuals-4，residuals-9......
        - 组成完全平方数的个数就是节点间的步数
        """
        from collections import deque
        q = deque()
        q.append([n, 0])
        visited = set([n])   # 不重复计算相同值的节点
        while q:
            residuals, step = q.popleft()
            for i in reversed(range(1, int(residuals ** 0.5) + 1)):
                val = residuals - i ** 2
                if val == 0:
                    return step + 1
                if val not in visited:
                    visited.add(val)
                    q.append([val, step + 1])

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(12))
    print(s.numSquares(14))
    print(s.numSquares(7168))
