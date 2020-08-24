class Solution:

    def delete_continues(self, s):
        """
        将字符串中的字符依次入栈
        如果新入栈元素等于栈顶元素，则不入栈，同时删除栈顶元素
        最终结果为栈中剩下的元素
        """
        stack = []
        i = 0
        while i < len(s):
            if not stack or stack[-1] != s[i]:
                stack.append(s[i])
                i += 1
            elif stack[-1] == s[i]:
                while i < len(s) and stack[-1] == s[i]:
                    i += 1
                stack.pop()


        return "".join(stack)

    # def delete_continues(self, s):
    #     """
    #     - 正则表达式，匹配连续重复字符
    #     - 若匹配完后长度不变，则说明已经没有连续重复字母
    #     """
    #     import re
    #     while True:
    #         # 正则表达式中的小括号"()"代表分组, 其后面出现\1则是代表与第一个小括号中要匹配的内容相同。
    #         new = re.sub(r'([a-z])\1{1,}', "", s)
    #         if len(new) == len(s):
    #             break
    #         s = new
    #
    #     return new

if __name__ == '__main__':
    s = Solution()
    assert (s.delete_continues("abcccbda") == "ada")
    assert (s.delete_continues("abbbbbdddadde") == "e")
