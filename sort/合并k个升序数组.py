"""
将k个排序数组合并为一个大的排序数组

要求：
在 O(Nlogk) 的时间复杂度内完成：
N 是所有数组包含的整数个数
k 是数组的个数

暴力解法： O(NlogN)
- 将所有数组合并成一个大数组:O(N)
- 大数组排序：O(NlogN)
"""


def merge_k_sort(k_list):
    """
    归并排序
    """
    return


def min_heap(k_list):
    """
    最小堆
    """
    return 

if __name__ == '__main__':
    result = merge_k_sort([
        [1, 3, 5, 7],
        [2, 4, 6],
        [0, 8, 9, 10, 11]
    ])
    print(result)
