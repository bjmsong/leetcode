"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例：
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

"""


class Solution:
    def exist(self, board, word: str) -> bool:
        """
        图搜索 DFS
        - 节点值是匹配剩余的字符串
        """
        if not board:
            return False
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j, res):

            if not res:
                return True

            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != res[0]:
                return False

            visited[i][j] = True
            if dfs(i - 1, j, res[1:]) or dfs(i + 1, j, res[1:]) or dfs(i, j - 1, res[1:]) or dfs(i, j + 1, res[1:]):
                return True
            visited[i][j] = False

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, word):
                    return True

        return False



if __name__ == '__main__':
    s = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert (s.exist(board, "ABCCED"))
    assert (s.exist(board, "SEE"))
    assert (~s.exist(board, "ABCB"))
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"]
    ]
    assert (s.exist(board, "ABCESEEEFS"))
