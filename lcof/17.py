"""
Q: 打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

测试用例：

"""


class Solution:
    def __init__(self):
        self.result = []  # 用来保存结果

    def printNumber(self, number):
        """
        舍弃左边的0
        :param number:
        :return:
        """
        is_begining = True
        length = len(number)
        valid_number = []
        for i in range(length):
            if is_begining and number[i] != '0':
                is_begining = False
            if not is_begining:
                valid_number.append(number[i])
        # val = int("".join(number))
        # if val != 0:
        #     print(val)
        print("".join(valid_number))

    def print1toMax(self, number, length, index):
        if index == length - 1:
            self.printNumber(number)
            self.result.append(int("".join(number)))
            return
        for i in range(10):
            number[index + 1] = str(i)
            # number[index+1] = chr(ord("0") + i)  # 速度稍快：ord 将字符转换成ASCII码，chr 将ASCII码转换成字符
            self.print1toMax(number, length, index + 1)

    def printNumbers(self, n):
        """
        大数问题：n如果很大，会超出int或者long的范围，因此用字符串来表示数字
        n位所有的十进制数就是n个从0到9的全排列 -- 递归实现
        时间复杂度：O(n)
        空间复杂度：O()
        :param n:
        :return:
        """
        if n < 0:
            return
        number = ['0'] * n
        for i in range(10):
            number[0] = str(i)
            self.print1toMax(number, n, 0)
        return self.result[1:]


if __name__ == '__main__':
    s = Solution()
    print(s.printNumbers(1))
    print(s.printNumbers(2))
