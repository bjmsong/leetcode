"""
寻找有向环
"""
import time
from chapter4_graph.digraph import init_graph


class DirectedCycle():
    def __init__(self, G):
        self.__cycle = list()  # 有向环中的所有顶点
        self.__marked = [False] * G.v()  # 标记是否已遍历
        self.__edgeTo = [None] * G.v()  # 从起点到一个顶点的已知路径上的最后一个顶点
        self.__onstack = [False] * G.v()  # 正在遍历的递归调用栈上的所有顶点
        for v in range(G.v()):
            if not self.__marked[v]:
                self.__dfs(G, v)

    def __dfs(self, G, v):
        self.__marked[v] = True
        self.__onstack[v] = True
        for w in G.adj(v):
            if self.hasCycle():
                return
            elif not self.__marked[w]:
                self.__edgeTo[w] = v
                self.__dfs(G, w)
            elif self.__onstack[w]:   # w已经被遍历过，并且w在当前遍历的栈中，即找到了一个环！
                self.__cycle = list()
                x = v
                while x != w:
                    self.__cycle.append(x)
                    x = self.__edgeTo[x]
                self.__cycle.append(w)
                self.__cycle.append(v)

        self.__onstack[v] = False     # 遍历结束，清除栈

    def hasCycle(self):
        return len(self.__cycle) > 0


if __name__ == '__main__':
    start = time.time()

    graph = init_graph()
    dfSearch = DirectedCycle(graph)
    print(dfSearch.hasCycle())

    end = time.time()
    print("run time = {}".format(end - start))
