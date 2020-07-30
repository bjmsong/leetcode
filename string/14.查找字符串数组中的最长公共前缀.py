"""
编写一个函数来查找字符串数组中的最长公共前缀

如果不存在公共前缀，返回空字符串 ""

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        result = []
        # 与 zip 相反，可理解为解压，返回二维矩阵式: zip(*["flower", "flow", "flight"]) => [('f','f','f'),('l','l','l'),(...)]
        s = zip(*strs)
        for i in s:
            if len(set(i)) == 1:
                result += i[0]
            else:
                break

        return "".join(result)

    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     n = len(strs)
    #     if n == 0:
    #         return ""
    #     if n == 1:
    #         return strs[0]
    #     cnt = 0
    #     flag = True
    #     for i in range(len(strs[0])):
    #         val = strs[0][i]
    #         for s in strs[1:]:
    #             if i > len(s) - 1 or s[i] != val:
    #                 flag = False
    #                 break
    #         if not flag:
    #             break
    #         else:
    #             cnt += 1
    #
    #     return strs[0][:cnt]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
