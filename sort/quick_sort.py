from random import shuffle


class QuickSort:
    """
    - 打乱数组：避免出现数据已经排序好，每次分组时数据都集中在其中一组的情况，时间复杂度最高(O(n^2))
    - 随机选取基准值，将数组分成两部分：比基准值小的移到基准值左边，比基准值大的移到基准值右边
    - 递归：再对分好的数组分别排序
    - 时间复杂度：O(nlogn)
    - 空间复杂度：O(logn), logn层递归
    """

    def sort(self, lst):
        shuffle(lst)
        self.quick_sort(lst, 0, len(lst) - 1)

    def quick_sort(self, lst, lo, hi):
        if lo >= hi:
            return
        j = self.partition(lst, lo, hi)
        self.quick_sort(lst, lo, j)
        self.quick_sort(lst, j + 1, hi)

    def partition(self, lst, lo, hi):
        """
        - 选好基准值：v
        - 双指针: 左指针遇到比v大的数，右指针遇到比v小的数，则交换
        - 最后交换基准值和右指针
        """
        v = lst[lo]
        left, right = lo + 1, hi
        while True:
            while lst[left] <= v and left < hi:
                left += 1
            while lst[right] >= v and right > lo:
                right -= 1
            if left >= right:
                break
            else:
                lst[left], lst[right] = lst[right], lst[left]

        lst[right], lst[lo] = lst[lo], lst[right]
        return right


if __name__ == '__main__':
    lst = [5, 1, 2, 6, 3, 8, 7]
    qs = QuickSort()
    qs.sort(lst)
    print(lst)
