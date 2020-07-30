def select_sort(lst):
    """
    选择排序:找到列表中最小的元素，跟第一个元素交换位置，然后依次进行
    """
    for i in range(len(lst)):
        min_value = lst[i]
        idx = i
        for j in range(i, len(lst)):
            if lst[j] < min_value:
                min_value = lst[j]
                idx = j
        lst[i], lst[idx] = lst[idx], lst[i]


if __name__ == '__main__':
    with open("../data/sort.txt", "r") as f:
        lst = f.readline().strip().split(" ")

    print(lst)
    select_sort(lst)
    print(lst)
