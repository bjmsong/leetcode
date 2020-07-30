import numpy as np


class QuickFind():
    """
    动态连通性问题
    """

    def __init__(self, N):
        self.N = N                        # 联通分量的数量
        self.id = np.arange(N).tolist()   # 该数组记录每个元素所属的联通分量的id

    def is_connected(self, p, q):
        '''
        时间复杂度：O(1)
        '''
        return self.find(p) == self.find(q)

    def find(self, p):
        '''
        时间复杂度：O(1)
        '''
        return self.id[p]

    def union(self, p, q):
        '''
        时间复杂度：O(n)
        '''
        idp = self.find(p)
        idq = self.find(q)
        for i in range(len(self.id)):
            if self.id[i] == idp:
                self.id[i] = idq
        self.N -= 1

    def count(self):
        return self.N


if __name__ == '__main__':
    f = open("../data/uf.txt", "r")
    N = int(f.readline())
    uf = QuickFind(N)

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
