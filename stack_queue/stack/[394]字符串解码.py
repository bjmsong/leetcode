# 给定一个经过编码的字符串，返回它解码后的字符串。 
# 
#  编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。 
# 
#  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。 
# 
#  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#  
# 
#  示例 2： 
# 
#  输入：s = "3[a2[c]]"
# 输出："accaccacc"
#  
# 
#  示例 3： 
# 
#  输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#  
# 
#  示例 4： 
# 
#  输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#  
#  Related Topics 栈 深度优先搜索


class Solution:
    def decodeString(self, s: str) -> str:
        """
        - 把字符串中的字符依次压入栈中
        - 遇到“]”，则弹出栈中的元素，直到遇到“[”
        """
        stack = []
        for c in s:
            if c == "]":
                temp, d = "", 0
                v = stack.pop()
                while v != "[":
                    temp = v + temp
                    v = stack.pop()
                n = 0
                while stack:
                    top = stack[-1]
                    if top <= '9' and top >= '0':
                        v = stack.pop()
                        d = d + int(v) * 10 ** n
                        n += 1
                    else:
                        break
                stack.append(temp * d)
            else:
                stack.append(c)

        return "".join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("10[leet]"))
    assert (s.decodeString("3[a2[c]]") == "accaccacc")
    assert (s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
