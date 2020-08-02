"""
5476. 找出数组游戏的赢家
"""


class Solution:
    def getWinner(self, arr, k: int) -> int:
        k = len(arr) - 1 if k > len(arr) - 1 else k
        winner = arr[0]
        for i in range(len(arr)):
            round = 0  # 获胜轮次
            left = right = 1
            if i - left >= 0 and arr[i] > arr[i - left]:
                round += 1
                left += 1
            while arr[i] > arr[(i + right) % len(arr)]:
                round += 1
                right += 1
            if round >= k:
                winner = arr[i]
                break

        return winner


if __name__ == '__main__':
    s = Solution()
    assert (s.getWinner([2, 1, 3, 5, 4, 6, 7], 2) == 5)
    assert (s.getWinner([3, 2, 1], 10) == 3)
    assert (s.getWinner([1, 9, 8, 2, 3, 7, 6, 4, 5], 7) == 9)
    assert (s.getWinner([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 1000000000) == 99)
