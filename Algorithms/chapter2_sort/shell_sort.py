def shell_sort(items):
    """
    希尔排序
    """
    n = len(items)
    step = n // 3
    while step > 0:
        for cur in range(step, n):
            i = cur
            while i >= step and items[i - step] > items[i]:
                items[i - step], items[i] = items[i], items[i - step]
                i -= step
        step = step // 3


if __name__ == '__main__':
    with open("../data/sort.txt", "r") as f:
        lst = f.readline().strip().split(" ")

    print(lst)
    shell_sort(lst)
    print(lst)
