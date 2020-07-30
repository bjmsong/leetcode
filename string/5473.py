class Solution:
    def minFlips(self, target: str) -> int:
        # 从第一位开始比较，碰到不一样的就翻转
        step = 0
        cur = '0'  # 代表当前位及后续位,初始为全0
        for i in range(len(target)):
            if target[i] != cur:
                step += 1
                cur = str(int(cur == '0'))  # 翻转
        return step

    # def minFlips(self, target: str) -> int:
    #     # BFS,超时
    #     from collections import deque
    #     q = deque()
    #     start = "0" * len(target)
    #     if start == target:
    #         return 0
    #     # 前面已经匹配的就不用翻转了
    #     for match_length in range(len(target)):
    #         if start[:match_length] != target[:match_length]:
    #             break
    #     q.append([0, match_length - 1, start])
    #     visited = set([start])
    #     while q:
    #         step, match_length, state = q.popleft()
    #         for i in range(match_length, len(state)):
    #             new_state = state[:i] + "".join([str(int(val == '0')) for val in state[i:]])
    #             if new_state not in visited:
    #                 if new_state == target:
    #                     return step + 1
    #                 for new_match_length in range(match_length, len(target)):
    #                     if new_state[:new_match_length] != target[:new_match_length]:
    #                         break
    #                 q.append([step + 1, new_match_length - 1, new_state])
    #                 visited.add(new_state)


if __name__ == '__main__':
    s = Solution()
    assert (s.minFlips("101") == 3)
    assert (s.minFlips("10111") == 3)
    assert (s.minFlips("00000") == 0)
    assert (s.minFlips("001011101") == 5)
    print(s.minFlips("010001010001"))
    print(s.minFlips("000101000001010101110010"))
