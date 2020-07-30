class MaxPQ():
    """
    优先队列：基于二叉堆
    """

    def __init__(self):
        self.pq = [' ']  # 二叉堆(最大堆，根节点值最大),即pq[k]>max(pq[2k+1],pq[2k+2]), 第一个位置空出来
        self.N = 0

    def swim(self, pq, k):
        """
        上浮操作：子结点跟父结点比较，如果子节点大于父结点，则交换位置，迭代这个过程
        :param pq: 存放二叉堆的数组,根结点在1,父结点为k,子结点为2k+1和2k+2
        :param k: 需要上浮的元素index
        :return:
        """
        while (k > 1) & (pq[k // 2] < pq[k]):
            pq[k], pq[k // 2] = pq[k // 2], pq[k]
            k = k // 2

    def sink(self, pq, k, N):
        """
        下沉操作：父结点和子节点中较大的元素进行比较，如果父节点小于子节点，则交换位置，迭代这个过程
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

    def insert(self, v):
        # 新元素加到数组末尾，增加堆的大小，新元素上浮到合适的位置
        self.N += 1
        self.pq.append(v)
        self.swim(self.pq, self.N)

    def del_max(self):
        # 从数组顶端删去最大的元素，将数组的最后一个元素放到顶端，减小数组的大小，并让这个元素下沉到合适的位置
        max = self.pq[1]
        self.pq[1], self.pq[self.N] = self.pq[self.N], self.pq[1]
        self.N -= 1
        self.pq.pop(self.N + 1)
        self.sink(self.pq, 1, self.N)
        return max


if __name__ == '__main__':
    with open("../data/sort.txt", "r") as f:
        lst = f.readline().strip().split(" ")
    print(lst)

    max_pq = MaxPQ()
    for i in lst:
        max_pq.insert(i)
    for i in range(4):
        print(max_pq.del_max())
    print(max_pq.pq[1:])
