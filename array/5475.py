"""
5475. 统计好三元组
"""


class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        cnt = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, len(arr)):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            cnt += 1

        return cnt


if __name__ == '__main__':
    s = Solution()
    assert (s.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3) == 4)
    assert (s.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1) == 0)
