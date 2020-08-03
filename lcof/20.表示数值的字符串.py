"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"、"-1E-16"及"12e+5.4"都不是。
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        标记有么有遇到“.”,"e/E",数字
        举例：+100,-1.23,1.23e10,.23,.23e5
        """
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i in range(len(s)):
            char = s[i]
            if char in ('+', '-'):
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E': 
                    return False
            elif char == '.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif char in ('e', 'E'):
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False  # met_digit要重置
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit

    # def isNumber(self, s: str) -> bool:
    #     """
    #     数值模式：A[.B][e|EC] 或者 .B[e|EC]
    #     举例：+100,-1.23,1.23e10,.23,.23e5
    #     思路：先扫描A，如果遇到小数点，则开始扫描B，如果遇到'e'或者'E',则开始扫描C
    #     时间复杂度：O()
    #     :param s:
    #     :return:
    #     """


if __name__ == '__main__':
    pass
