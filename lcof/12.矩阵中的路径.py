"""
Q: 矩阵中的路径

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

"""


class Solution:

    def exist(self, board, word):
        """
        DFS真香
        """
        if not board:
            return False
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]  # 是否在路径中
        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, rows, cols, i, j, word, visited):
                    return True
        return False

    def dfs(self, matrix, rows, cols, i, j, word, visited):
        """
        从(i,j)开始寻找word
        """

        if not word:  # word遍历结束
            return True
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] != word[0] or visited[i][j] == True:
            return False
        visited[i][j] = True
        if (self.dfs(matrix, rows, cols, i + 1, j, word[1:], visited) or
                self.dfs(matrix, rows, cols, i - 1, j, word[1:], visited) or
                self.dfs(matrix, rows, cols, i, j - 1, word[1:], visited) or
                self.dfs(matrix, rows, cols, i, j + 1, word[1:], visited)):
            return True
        visited[i][j] = False
        return False

    # def exist_1(self, board, word):
    #     """
    #     DFS
    #     :param board:
    #     :param word:
    #     :return:
    #     """
    #
    #     def dfs(i, j, k):
    #         if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
    #             return False
    #         if k == len(word) - 1:
    #             return True
    #         tmp, board[i][j] = board[i][j], '/'
    #         res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
    #         board[i][j] = tmp
    #         return res
    #
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if dfs(i, j, 0):
    #                 return True
    #     return False
    #
    # def exist_2(self, board, word):
    #     """
    #     回溯法
    #     :param board:
    #     :param word:
    #     :return:
    #     """
    #     if not board:
    #         return False
    #     m = len(board)
    #     n = len(board[0])
    #     visit = [[False] * n for _ in range(m)]  # 是否在路径中
    #     # visit = m * [n * [False]] # 不要用这种初始化方式， 修改某一个值时，整个列表都会被改变。
    #     path = []  # 栈，存储路径
    #     length = len(word)
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == word[0]:
    #                 if length == 1:
    #                     return True
    #                 path.append([i, j])
    #                 visit[i][j] = True
    #                 index = 1
    #                 idx = i
    #                 jdx = j
    #                 while path:  # 路径不为空
    #                     exists, idx, jdx = self.find_surround(board, idx, jdx, word[index], visit)
    #                     if exists:
    #                         if index == length - 1:
    #                             return True
    #                         else:
    #                             index += 1
    #                             visit[idx][jdx] = True
    #                             path.append([idx, jdx])
    #                     else:
    #                         path.pop()
    #                         index -= 1
    #                         if path:
    #                             idx, jdx = path[len(path) - 1]
    #
    #     return False
    #
    # def find_surround(self, board, i, j, word, visit):
    #     """
    #     在board数组(i, j)的上、下、左、右寻找word，path表示已经存在的路径
    #     :param board:
    #     :param i:
    #     :param j:
    #     :param word:
    #     :param path:
    #     :return:
    #     """
    #     m = len(board)
    #     n = len(board[0])
    #     if j - 1 >= 0 and not visit[i][j - 1] and board[i][j - 1] == word:
    #         return (True, i, j - 1)
    #     if j + 1 <= n - 1 and not visit[i][j + 1] and board[i][j + 1] == word:
    #         return (True, i, j + 1)
    #     if i - 1 >= 0 and not visit[i - 1][j] and board[i - 1][j] == word:
    #         return (True, i - 1, j)
    #     if i + 1 <= m - 1 and not visit[i + 1][j] and board[i + 1][j] == word:
    #         return (True, i + 1, j)
    #
    #     return (False, None, None)


if __name__ == '__main__':
    s = Solution()
    board = [["a", "b", "c", "e"], ["s", "f", "c", "s"], ["a", "d", "e", "e"]]
    assert (s.exist([], 'bfce') == False)
    assert (s.exist(board, 'bfce') == True)
    assert (s.exist(board, 'abfb') == False)
    assert (s.exist([["a"]], "a") == True)
    assert (s.exist([["b", "a"]], "a") == True)
    assert (s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE") == True)
    assert (s.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB") == True)
    assert (s.exist([["a"]], "ab") == False)
    assert (s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED") == True)
