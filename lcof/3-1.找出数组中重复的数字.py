"""
Q: 找出数组中[任意]一个重复的数字,长度为n的数组中所有数字都在0～n-1的范围内
测试用例：
[] -> []
[1,2,2] -> [2]
[1,1,2] -> [1]
[2,2,2] -> [2]
[2,3,1,0,2,5,3] -> 2 或 3
"""


# def findRepeatedNumber(lst):
#     """
#     思路：先排序，然后遍历数组，双指针记录前后两个数
#     时间复杂度：O(nlogn)+O(n)
#     空间复杂度：O(1)
#     :param lst:
#     :return:
#     """
#     if len(lst) <= 1:
#         return
#     lst.sort()
#     dup = lst[0]
#     for index in range(1, len(lst)):
#         if lst[index] == dup:
#             return dup
#         else:
#             dup = lst[index]


# def findRepeatedNumber(lst):
#     """
#     思路：遍历数组，依次存入哈希表，直到遇到重复值
#     时间复杂度：O(n)
#     空间复杂度：O(n)
#     :param lst:
#     :return:
#     """
#     if len(lst) <= 1:
#         return
#     dup = {}
#     for i in range(len(lst)):
#         if dup.get(i):
#             return i
#         else:
#             dup[lst[i]] = 1


def findRepeatedNumber(lst):
    """
    官方解法，best solution
    因为数组中的数字都在0～n-1的范围内，如果没有重复元素，数字i应该在索引i的位置
    如果元素没有在对应位置，则应交换位置，直到遇到重复元素，或者遍历结束
    时间复杂度：O(n)
    空间复杂度：O(1)
    :param lst:
    :return:
    """
    if len(lst) <= 1:
        return
    for i in range(len(lst)):
        while lst[i] != i:
            if lst[i] == lst[lst[i]]:
                return lst[i]
            # 注意这里不要写成lst[i], lst[lst[i]] = lst[lst[i]], lst[i]
            # 这种嵌套的直接交换在python里面得到的不是你想要的,会死循环
            temp = lst[i]
            lst[i], lst[temp] = lst[temp], lst[i]


if __name__ == '__main__':
    for lst in ([], [1, 2, 2], [1, 1, 2], [2, 2, 2], [2, 3, 1, 0, 2, 5, 3]):
        result = findRepeatedNumber(lst)
        print("{} -> {}".format(lst, result))
