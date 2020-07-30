"""
有向图的可达性：跟无向图dfs的代码是一样的
"""
import time
from chapter4_graph.digraph import init_graph


class DirectedDFS():
    def __init__(self, sources, G):
        self.sources = sources           # 起点
        self.__marked = [False] * G.v()  # 标记是否已经遍历
        self.__count = 0                 # 与s连通的顶点总数
        self.edgeTo = [None] * G.v()     # 从起点到一个顶点的已知路径上的最后一个顶点
        for s in sources:
            if not self.marked(s):
                self.dfs(G, s)

    def dfs(self, G, v):
        self.__marked[v] = True
        self.__count += 1
        for w in G.adj(v):  # 搜索相邻顶点
            if not self.marked(w):  # 还没有标记过
                self.edgeTo[w] = v
                self.dfs(G, w)

    def count(self):
        return self.__count

    def marked(self, v):
        return self.__marked[v]

    def hasPathTo(self, v):
        # 是否存在v到s的路径
        return self.__marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return
        path = list()  # 栈：后进先出
        x = v
        while x not in self.sources:
            path.insert(0, x)
            x = self.edgeTo[x]
        path.insert(0, x)
        return path


if __name__ == '__main__':
    start = time.time()

    graph = init_graph()
    dfSearch = DirectedDFS([0, 1, 2], graph)
    print(dfSearch.count())
    print(dfSearch.marked(1))
    print(dfSearch.marked(10))
    print("Path to 3 is:", dfSearch.pathTo(3))

    end = time.time()
    print("run time = {}".format(end - start))
