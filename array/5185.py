"""
5185.存在连续三个奇数的数组
"""


class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:

        for i in range(len(arr) - 2):
            cnt = 0
            while i < len(arr) and arr[i] % 2 == 1 and cnt < 3:
                cnt += 1
                i += 1
            if cnt == 3:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    assert (not s.threeConsecutiveOdds([2, 6, 4, 1]))
    assert (s.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
    assert (s.threeConsecutiveOdds([1, 1, 1]))
    assert (not s.threeConsecutiveOdds([1, 3, 2]))
