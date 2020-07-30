"""
Q：不修改数组找出重复的数字
- 长度为n+1的数组中所有数字都在1～n的范围内，所以数组中至少有一个数字是重复的
- 请找出任意一个重复的数字，但是不能修改输入的数组
测试用例：
[] -> Invalid Input
[1,2,3] -> Invalid Input
[1,2,2] -> 2
[1,2,2,2] -> 2
[2,3,5,4,3,2,6,7] -> 2 or 3
"""


def findRepeatedNumber(lst):
    """
    二分法: 统计1～n/2的元素个数，如果元素个数大于n/2则说明重复元素位于1～n/2的区间，反之，则位于n/2+1～n的区间
    不断缩小查找范围，直到只剩一个元素
    时间复杂度：O(nlogn)
    空间复杂度：O(1)
    :param lst:
    :return:
    """
    lo = 1
    hi = len(lst) - 1  # n
    while lo < hi:
        mid = (lo + hi) // 2
        cnt = 0
        for i in range(len(lst)):
            if lst[i] <= mid and lst[i] >= lo:
                cnt += 1
        if cnt > mid - lo + 1:
            hi = mid
        else:
            lo = mid + 1

    return lo


# def findRepeatedNumber1(lst):
#     """
#     哈希表存入数组元素
#     时间复杂度：O(n)
#     空间复杂度：O(n)
#     :return:
#     """
#     if len(lst) <= 1:
#         return "Invalid Input"
#     dup = {}
#     for i in range(len(lst)):
#         tmp = lst[i]
#         if tmp > len(lst) - 1:
#             return "Invalid Input"
#         if dup.get(tmp):
#             return tmp
#         else:
#             dup[tmp] = 1
#
#
# def findRepeatedNumber2(lst):
#     """
#     复制到辅助数组，把元素存入对应的index中
#     时间复杂度：O(n)
#     空间复杂度：O(n)
#     :param lst:
#     :return:
#     """
#     length = len(lst)
#     if length <= 1:
#         return "Invalid Input"
#     aux = [None] * length
#     for i in range(length):
#         index = lst[i]
#         if index > length - 1:
#             return "Invalid Input"
#         if index == aux[index]:
#             return index
#         aux[index] = index
#
#
# def findRepeatedNumber3(lst):
#     """
#     官方解法，空间复杂度最优解
#     二分法：第一步先确定重复元素位于(1,n/2)还是(n/2,n)的区间，再依次减半
#     时间复杂度：O(nlogn)
#     空间复杂度：O(1)
#     :param lst:
#     :return:
#     """
#     length = len(lst)
#     if length <= 1:
#         return "Invalid Input"
#     start = 1  #
#     end = length - 1
#     while end >= start:
#         mid = (start + end) // 2
#         count = countRange(lst, length, start, mid)
#         if end == start:
#             if count > 1:
#                 return start
#             else:
#                 break
#         # 缩小寻找范围
#         if count > mid - start + 1:
#             end = mid
#         else:
#             start = mid + 1
#
#     return -1
#
#
# def countRange(lst, length, start, mid):
#     """
#     计算lst数组中值位于start和mid之间的元素数目
#     :param lst:
#     :param length:
#     :param start:
#     :param mid:
#     :return:
#     """
#     if len(lst) == 0:
#         return
#     count = 0
#     for i in range(length):
#         if lst[i] >= start and lst[i] <= mid:  # &是位运算符，不要混淆了
#             count += 1
#     return count


if __name__ == '__main__':
    for lst in [[1, 2, 2], [1, 2, 2, 2], [2, 3, 5, 4, 3, 2, 6, 7]]:
        result = findRepeatedNumber(lst)
        print("{} -> {}".format(lst, result))
