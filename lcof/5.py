"""
Q：替换空格
实现一个函数，把字符串的每个空格都替换成"%20"

测试用例：
"We are happy"->"We%20are%20happy"
"We" -> "We"
"""


def replaceSpace(str):
    result = []
    for s in str:
        if s == " ":
            result.append("%20")
        else:
            result.append(s)
    return "".join(result)


# def replaceSpace1(str):
#     """
#     时间复杂度：O(n)
#     空间复杂度：O(m),m是空格数量
#     :param str:
#     :return:
#     """
#     length = len(str)
#     count = 0
#     for i in range(length):
#         if str[i] == ' ':
#             count += 1
#     for i in range(count * 2):
#         str += '1'
#     p1, p2 = length - 1, length + 2 * count - 1
#     while p1 >= 0:
#         if str[p1] == ' ':
#             str[p2] = '0'
#             str[p2 - 1] = '2'
#             str[p2 - 2] = '%'
#             p2 = p2 - 3
#         else:
#             str[p2] = str[p1]
#             p2 -= 1
#         p1 -= 1


if __name__ == '__main__':
    for string in ["We are happy", "We"]:
        result = replaceSpace(string)
        print("{} -> {}".format(string, result))
