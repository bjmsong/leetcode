class QuickUnion():
    """
    动态连通性问题

    不能保证所有情况下都比quick-find快
    """

    def __init__(self, N):
        self.N = N                  # 联通分量的数量
        self.id = list(range(N))    # 该数组记录每个元素的父节点的联通分量的id

    def is_connected(self, p, q):

        return self.find(p) == self.find(q)

    def find(self, p):
        """
        最好时间复杂度：O(1)
        最坏时间复杂度：O(n)
        """
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        '''
        两棵树融合
        最坏时间复杂度：O(n)
        '''
        idp = self.find(p)
        idq = self.find(q)
        self.id[idp] = idq
        self.N -= 1

    def count(self):
        return self.N


if __name__ == '__main__':
    f = open("../data/uf.txt", "r")
    N = int(f.readline())
    uf = QuickUnion(N)

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
