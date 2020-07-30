def insert_sort(lst):
    """
    插入排序:依次跟左边元素比较，保证左侧始终有序
    """
    for i in range(1, len(lst)):
        right_index = i
        left_index = i - 1
        while (left_index >= 0) & (lst[right_index] < lst[left_index]):
            lst[left_index], lst[right_index] = lst[right_index], lst[left_index]
            right_index -= 1
            left_index -= 1


if __name__ == '__main__':
    with open("../data/sort.txt", "r") as f:
        lst = f.readline().strip().split(" ")

    print(lst)
    insert_sort(lst)
    print(lst)
