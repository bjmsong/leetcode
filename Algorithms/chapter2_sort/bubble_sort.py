def bubble_sort(lst):
    # 依次比较相邻元素,把最大的元素逐步移动到末尾
    length = len(lst)
    for k in range(1, length):
        for i in range(length - k):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


if __name__ == '__main__':
    with open("../data/sort.txt", "r") as f:
        lst = f.readline().strip().split(" ")

    print(lst)
    bubble_sort(lst)
    print(lst)
