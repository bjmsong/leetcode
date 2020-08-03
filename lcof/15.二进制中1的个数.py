"""
Q: 二进制中1的个数

请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。
例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。
"""


class Solution:

    def hammingWeight(self, n: int) -> int:
        """
        整数减1  => 会将最右边的1置0
        再和原整数做与运算 => 得到的结果是最右边的1变成0
        原整数有多少个1，就能进行多少次这样的运算
        1001-> 1000 , 1000 & 1001 = 1000
        1000 -> 0111 , 0111 & 1000 = 0000
        时间复杂度：O(M) M是1的个数
        """
        cnt = 0
        while n > 0:
            n = n & (n - 1)
            cnt += 1

        return cnt

    def hammingWeight(self, n: int) -> int:
        """
        - 与1做与运算，判断最右边一位是否是1
        1001 & 0001 = 0001
        - 将1左移，变成2，判断次右边一位是否是1
        1001 & 0010 = 0000
        - 将2左移。。
        时间复杂度：O(M) M是位数
        """
        cnt = 0
        flag = 1
        while flag <= n:
            val = n & flag
            if val == flag:
                cnt += 1
            flag = flag << 1

        return cnt

    def hammingWeight(self, n: int) -> int:
        """
        整数与1做与运算，如果最右边一位是1，则与运算结果为1，反之则为0
        做完一次与运算，向右移一位，直到为0
        存在问题：如果输入是负数，会陷入死循环
        """
        cnt = 0
        while n > 0:
            val = n & 1
            if val == 1:
                cnt += 1
            n = n >> 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    assert (s.hammingWeight(9) == 2)
    assert (s.hammingWeight(128) == 1)
