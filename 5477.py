"""
5477. 排布二进制网格的最少交换次数
"""


class Solution:
    def minSwaps(self, grid) -> int:
        """
        从右边开始将对角线以上格子置0,如果右边的置0了，左边的排列变动不会影响右边
        """
        cnt = 0
        n = len(grid)
        for col in reversed(range(1, n)):
            col_list = [row[col] for row in grid]
            upper_one_cnt = col_list[:col].count(1)
            lower_zero_cnt = col_list[col:].count(0)
            if upper_one_cnt > lower_zero_cnt:
                return -1
            # 在同一列元素中交换0,1：双指针，upper里面的1和lower里面的0交换
            left, right = col - 1, col
            for _ in range(upper_one_cnt):
                col_list = [row[col] for row in grid]
                while left >= 0 and col_list[left] == 0:
                    left -= 1
                while right < n and col_list[right] == 1:
                    right += 1
                while right - left > 1:
                    if col_list[left + 1] == 0:
                        grid[left], grid[left + 1] = grid[left + 1], grid[left]
                        left += 1
                    else:
                        grid[right], grid[right - 1] = grid[right - 1], grid[right]
                        right -= 1
                    cnt += 1
                grid[left], grid[right] = grid[right], grid[left]
                cnt += 1

        return cnt


if __name__ == '__main__':
    s = Solution()
    assert (s.minSwaps([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]) == -1)
    assert (s.minSwaps([[1, 0, 0], [1, 1, 0], [1, 1, 1]]) == 0)
    assert (s.minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]) == 3)
    assert (s.minSwaps(
        [[1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 1]]) == 4)
    assert (s.minSwaps([[0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0]]) == -1)
