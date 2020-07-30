class Solution:
    def restoreString(self, s: str, indices) -> str:
        s_list = list(s)
        for i in range(len(s)):
            s_list[indices[i]] = s[i]

        return "".join(s_list)

    # def restoreString(self, s: str, indices) -> str:
    #     # 原地变换，但是由于python string 不可变，还是需要一个辅助数组s_list
    #     visited = [False] * len(s)
    #     s_list = list(s)
    #     for i in range(len(s)):
    #         index, val = i, s_list[i]
    #         while not visited[index]:
    #             visited[index] = True
    #             temp = val
    #             index = indices[index]
    #             val = s_list[index]
    #             s_list[index] = temp
    #
    #     return "".join(s_list)


if __name__ == '__main__':
    s = Solution()
    assert (s.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]) == "leetcode")
    assert (s.restoreString("abc", [0, 1, 2]) == "abc")
    assert (s.restoreString("aiohn", [3, 1, 4, 2, 0]) == "nihao")
