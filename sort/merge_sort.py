class MergeSort:
    def __init__(self):
        self.aux = []

    def merge_sort(self, lst):
        self.aux = [0] * len(lst)
        self.sort(lst, 0, len(lst) - 1)

    def sort(self, lst, lo, hi):
        """
        递归：先sort，再merge
        """
        if lo >= hi:  # 列表长度<=1
            return
        mid = (lo + hi) // 2
        self.sort(lst, lo, mid)       # sort左半列表
        self.sort(lst, mid + 1, hi)   # sort右半列表
        self.merge(lst, lo, mid, hi)

    def merge(self, lst, lo, mid, hi):
        """
        - 辅助数组存储lo~hi的数据
        - merge: 双指针依次从lo~mid,mid+1~hi的数组中取数
        """

        for k in range(lo, hi + 1):
            self.aux[k] = lst[k]
        left, right = lo, mid + 1  # 双指针,分别指向两个数组：lo~mid,mid+1~hi
        for idx in range(lo, hi + 1):
            if left > mid:         # 左半列表遍历完成
                lst[idx] = self.aux[right]
                right += 1
            elif right > hi:       # 右半列表遍历完成
                lst[idx] = self.aux[left]
                left += 1
            elif self.aux[left] < self.aux[right]:
                lst[idx] = self.aux[left]
                left += 1
            else:
                lst[idx] = self.aux[right]
                right += 1


if __name__ == '__main__':
    lst = [1, 5, 2, 6, 3, 8, 7]
    ms = MergeSort()
    # 列表作为参数传入函数，函数对列表的操作都会保留
    ms.merge_sort(lst)
    print(lst)
