class Solution:
    def delete_continues(self, s):
        s = list(s)
        slow, fast = 0, 1
        while fast < len(s):
            while fast < len(s) and s[fast] == s[fast - 1]:
                fast += 1
            s[slow] = s[fast - 1]
            if slow >= 1 and s[slow] == s[slow - 1]:
                slow -= 2
            slow += 1
            fast += 1
        return "".join(s)
    # def delete_continues(self, s):
    #     stack = []
    #     for i in range(len(s)):
    #         if not stack:
    #             stack.append(s[i])
    #         elif stack[-1] == s[i]:
    #             while


if __name__ == '__main__':
    s = Solution()
    assert (s.delete_continues("abcccbda") == "ada")
