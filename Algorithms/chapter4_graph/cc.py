"""
寻找连通分量:DFS
"""
import time
from chapter4_graph.graph import init_graph


class CC():
    def __init__(self, G):
        self.__count = 0  # 连通分量数
        self.__marked = [False] * G.v()  # 标记是否已经遍历
        self.__id = [None] * G.v()  # 连通分量索引
        for v in range(G.v()):
            if not self.__marked[v]:
                self.__dfs(G, v)
                self.__count += 1

    def __dfs(self, G, v):
        self.__marked[v] = True
        self.__id[v] = self.__count
        for w in G.adj(v):
            if not self.__marked[w]:
                self.__dfs(G, w)

    def count(self):
        """
        连通分量数
        :return:
        """
        return self.__count

    def connected(self, v, w):
        """
        v和w连通吗
        :param v:
        :param w:
        :return:
        """
        return self.__id[v] == self.__id[w]

    def id(self, v):
        """
        v所在的连通分量的标识符
        :param v:
        :return:
        """
        return self.__id[v]


if __name__ == '__main__':
    start = time.time()

    graph = init_graph()
    cc = CC(graph)
    print(cc.count())
    print(cc.connected(1, 2))
    print(cc.connected(1, 10))
    print(cc.connected(1, 3))
    print(cc.id(1))

    end = time.time()
    print("run time = {}".format(end - start))
