"""
二进制求和

给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

例如：
”11“ + ”1“ = ”100“
"""


class Solution:
    def addBinary(self, a, b):

        p1 = len(a) - 1
        p2 = len(b) - 1
        add = 0
        result = []
        while p1 >= 0 or p2 >= 0:
            val = 0
            if p1 >= 0:
                val += int(a[p1])
                p1 -= 1
            if p2 >= 0:
                val += int(b[p2])
                p2 -= 1
            val += add
            add = val // 2
            result.append(str(val % 2))

        if add > 0:
            result.append(str(add))
        return "".join(result[::-1])


if __name__ == '__main__':
    s = Solution()
    assert (s.addBinary("11", "1") == "100")
