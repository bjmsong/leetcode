"""
Q: 把数字翻译成字符串

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。


示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 2^31

"""


class Solution:
    def translateNum(self, num: int) -> int:
        """
        递归解法有重复的子问题，自下而上可以避免这个问题
        :param num:
        :return:
        """


    def translateNum(self, num: int) -> int:
        """
        递归
        设函数f(i)表示从第i位数字开始的不同翻译的数目，则f(i) = f(i+1) + g(i,i+1)*f(i+2)
        当第i位和第i+1位数字拼接起来大于25时，g(i,i+1)为1,否则为0
        时间复杂度:O()
        空间复杂度:O()
        :param num:
        :return:
        """
        length = len(str(num))
        if length in (0, 1):
            return 1
        base = 10 ** (length - 2)
        if num // base > 25 or num // base < 10:
            return self.translateNum(num % (10 * base))
        else:
            return self.translateNum(num % (10 * base)) + self.translateNum(num % base)


if __name__ == '__main__':
    s = Solution()
    print(s.translateNum(12258))
    print(s.translateNum(26))
