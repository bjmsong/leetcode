"""
讲解：《计算机科学速成课》第13课
递归地分成两半分别排序,然后将结果归并起来
"""
class MergeSort:
    def __init__(self):
        self.aux = list()

    def sort(self, lst):
        self.aux = list(range(len(lst)))   # 辅助列表,O(N)空间
        self.merge_sort(lst, 0, len(lst) - 1)

    def merge_sort(self, lst, lo, hi):
        """
        example:
        merge_sort(lst,0,4)
            merge_sort(lst,0,2)
                merge_sort(lst,0,1)
                    merge_sort(lst,0,0) => return
                    merge_sort(lst,1,1) => return
                    merge(lst,0,1)
                merge_sort(lst,2,2)
                merge(lst,0,2)
            merge_sort(lst,3,4)
            merge(lst,0,4)
        merge_sort(lst,5,8)
            merge_sort(lst,5,6)
            merge_sort(lst,6,8)
                merge_sort(lst,6,7)
                merge_sort(lst,7,8)
                merge(lst,6,8)
            merge(lst,5,8)
        merge(lst,0,8)
        """

        if lo >= hi:    # 基线条件,直到剩下一个元素
            return
        mid = lo + (hi - lo) // 2
        self.merge_sort(lst, lo, mid)      # 排序左半段列表
        self.merge_sort(lst, mid + 1, hi)  # 排序右半段列表
        self.merge(lst, lo, mid, hi)       # 合并左、右半段列表

    def merge(self, lst, lo, mid, hi):

        # 辅助数组拷贝原数组的值
        for k in range(lo, hi + 1):
            self.aux[k] = lst[k]

        # 双指针
        left = lo     # 左半列表开始
        right = mid + 1  # 右半列表开始
        for i in range(lo, hi + 1):    # 按从小到大顺序
            if left > mid:   # 左半列表遍历完成
                lst[i] = self.aux[right]
                right += 1
            elif right > hi:  # 右半列表遍历完成
                lst[i] = self.aux[left]
                left += 1
            elif self.aux[left] < self.aux[right]:
                lst[i] = self.aux[left]
                left += 1
            else:
                lst[i] = self.aux[right]
                right += 1


if __name__ == '__main__':
    with open("../data/sort.txt", "r") as f:
        lst = f.readline().strip().split(" ")

    print(lst)
    ms = MergeSort()
    ms.sort(lst)
    print(lst)




