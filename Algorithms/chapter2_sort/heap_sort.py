def swim(pq, k):
    """
    上浮操作
    :param pq: 存放二叉堆的数组,根结点在1,子结点在2和3
    :param k: 需要上浮的元素
    :return:
    """
    while (k > 1) & (pq[k // 2] < pq[k]):
        pq[k], pq[k // 2] = pq[k // 2], pq[k]
        k = k // 2


def sink(pq, k, N):
    """
    下沉操作
    :param pq:
    :param k:需要下沉的元素
    :param N:所有元素的个数
    :return:
    """
    while 2 * k <= N:
        j = 2 * k
        # 取出子结点中最大值
        if j < N:
            if pq[j] < pq[j + 1]:
                j += 1
        # 跟子结点中较大的元素进行比较
        if pq[k] >= pq[j]:
            break
        pq[k], pq[j] = pq[j], pq[k]
        k = j


def heap_sort(lst):
    '''
    堆排序：所有值推入堆中然后每次弹出一个最小值
    '''
    N = len(lst) - 1
    k = N // 2
    # 构造二叉堆:从右到左 sink()
    while k >= 1:
        sink(lst, k, N)
        k -= 1
    print(lst)
    # 下沉排序
    while N > 1:
        lst[1], lst[N] = lst[N], lst[1]
        N -= 1
        sink(lst, 1, N)


if __name__ == '__main__':
    with open("../data/sort.txt", "r") as f:
        lst = f.readline().strip().split(" ")

    # 第一个索引位置不用
    lst.insert(0, None)
    print(lst)
    heap_sort(lst)
    print(lst)
