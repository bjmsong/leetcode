"""
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

"""


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        if not str:
            return 0
        symbol, val = 1, 0
        if str[0] in ('+', '-'):
            if str[0] == '-':
                symbol = -1
            index = 1
            while index < len(str) and str[index] >= '0' and str[index] <= '9':
                val = val * 10 + int(str[index])
                index += 1

        elif str[0] >= '0' and str[0] <= '9':
            index = 0
            while index < len(str) and str[index] >= '0' and str[index] <= '9':
                val = val * 10 + int(str[index])
                index += 1
        else:
            return 0

        result = symbol * val
        if result > pow(2, 31) - 1:
            result = pow(2, 31) - 1
        if result < -pow(2, 31):
            result = -pow(2, 31)
        return result


if __name__ == '__main__':
    s = Solution()
    assert (s.myAtoi("") == 0)
    assert (s.myAtoi("42") == 42)
    assert (s.myAtoi("  -42") == -42)
    assert (s.myAtoi("4193 with words") == 4193)
    assert (s.myAtoi("words and 987") == 0)
    assert (s.myAtoi("-91283472332") == -2147483648)
