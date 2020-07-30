from random import shuffle


class QuickSort:
    """
    《Algorithms》解法，原地排序，递归
    step1： 选取基准值，将一个数组分成两个子数组,左边的数组的元素都小于基准值，右边数组元素都大于基准值
    step2： 将两个子数组排序,整个数组自然就有序了
    时间复杂度：O(nlogn)
    空间复杂度：O(logn)
    """

    def sort(self, lst):
        shuffle(lst)  # 如果碰到已经排序好的列表，这样快排的效率最低（因为每次分割列表不能均匀分割），因此需要先打乱
        self.quick_sort(lst, 0, len(lst) - 1)

    def quick_sort(self, lst, lo, hi):
        if hi <= lo:  # 递归基线条件
            return
        j = self.partiions(lst, lo, hi)
        self.quick_sort(lst, lo, j - 1)
        self.quick_sort(lst, j + 1, hi)

    def partiions(self, lst, lo, hi):
        """
        双指针
        a[lo]到a[j-1] 的所有元素都不大于 a[j]
        a[j+1]到a[hi] 的所有元素都不小于 a[j]
        """
        left = lo  # 左指针
        right = hi  # 右指针
        v = lst[lo]  # 随机选取基准，这边选取第一个值
        while True:
            while (lst[left] <= v) & (left < hi):  # 找到大于v的值
                left += 1
            while (lst[right] >= v) & (right > lo):  # 找到小于v的值
                right -= 1
            if left >= right:
                break
            else:
                lst[left], lst[right] = lst[right], lst[left]  # 交换位置

        lst[right], lst[lo] = lst[lo], lst[right]
        return right


def quick_sort(b):
    """
    非原地排序，代码简单
    时间复杂度：O(nlogn)
    空间复杂度高：O(nlogn)
    """
    shuffle(b)
    if len(b) < 2:
        return b
    # 随机选取基准，这边选取中间
    mid = b[len(b) // 2]
    left, right = [], []
    b.remove(mid)
    for item in b:
        if item >= mid:
            right.append(item)
        else:
            left.append(item)
    return quick_sort(left) + [mid] + quick_sort(right)


if __name__ == '__main__':
    with open("../data/sort.txt", "r") as f:
        lst = f.readline().strip().split(" ")

    lst = [1, 5, 8, 2, 3]
    print(lst)

    print("Quick sort method 1:")
    ms = QuickSort()
    ms.sort(lst)
    print(lst)

    print("Quick sort method 2:")
    result = quick_sort(lst)
    print(result)
