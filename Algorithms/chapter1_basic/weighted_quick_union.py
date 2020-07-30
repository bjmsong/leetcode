import numpy as np


class WeightedQuickUnion():
    """
    动态连通性问题
    建立平衡树：小数加到大树上
    """

    def __init__(self, N):
        self.N = N                        # 联通分量的数量
        self.id = np.arange(N).tolist()   # 该数组记录每个元素的父节点的联通分量的id
        self.size = [1] * N               # 记录联通分量包含元素的个数

    def is_connected(self, p, q):

        return self.find(p) == self.find(q)

    def find(self, p):
        """
        时间复杂度：O(lgn)
        """
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        '''
        时间复杂度：O(lgn)
        '''

        idp = self.find(p)
        idq = self.find(q)

        if self.size[idp] < self.size[idq]:
            self.id[idp] = idq
            self.size[idq] += self.size[idp]
        else:
            self.id[idq] = idp
            self.size[idp] += self.size[idq]
        self.N -= 1

    def count(self):
        return self.N


if __name__ == '__main__':
    f = open("../data/uf.txt", "r")
    N = int(f.readline())
    uf = WeightedQuickUnion(N)

    while True:
        s = f.readline().strip()
        if not s:
            break
        p, q = s.split(" ")
        p, q = int(p), int(q)
        if not uf.is_connected(p, q):
            uf.union(p, q)
            print(uf.is_connected(p, q))
    f.close()

    print(str(uf.count()) + " components")
    print("is 1 and 2 connected ? " + str(uf.is_connected(1, 2)))
    print("is 2 and 9 connected ? " + str(uf.is_connected(2, 9)))
