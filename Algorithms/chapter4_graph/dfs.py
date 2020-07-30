"""
实现图搜索API:DFS
"""
import time
from chapter4_graph.graph import init_graph


class DepthFirstSearch():

    def __init__(self, s, G):
        self.s = s  # 起点
        self.__marked = [False] * G.v()  # 标记是否已经遍历，即和s是否连通
        self.__count = 0  # 与s连通的顶点总数
        self.edgeTo = [None] * G.v()  # 从起点到一个顶点的已知路径上的最后一个顶点
        self.__dfs(G, s)

    def __dfs(self, G, v):
        self.__marked[v] = True
        self.__count += 1
        for w in G.adj(v):  # 搜索相邻顶点
            if not self.marked(w):  # 还没有标记过
                self.edgeTo[w] = v
                self.__dfs(G, w)

    def count(self):
        """
        和s连通的顶点总数
        :return:
        """
        return self.__count

    def marked(self, v):
        """
        v和s是否连通
        :param v:
        :return:
        """
        return self.__marked[v]

    def hasPathTo(self, v):
        """
        是否存在v到s的路径
        :param v:
        :return:
        """
        return self.__marked[v]

    def pathTo(self, v):
        """
        s到v的路径，如果不存在则返回null
        :param v:
        :return:
        """
        if not self.hasPathTo(v):
            return
        path = list()  # 这边是一个栈：后进先出
        x = v
        while x != self.s:
            path.insert(0, x)
            x = self.edgeTo[x]
        path.insert(0, self.s)
        return path


if __name__ == '__main__':
    start = time.time()

    graph = init_graph()
    dfSearch = DepthFirstSearch(0, graph)
    print(dfSearch.count())
    print(dfSearch.marked(1))
    print(dfSearch.marked(10))
    print("Path to 3 is:", dfSearch.pathTo(3))

    end = time.time()
    print("run time = {}".format(end - start))
