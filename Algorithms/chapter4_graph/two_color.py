"""
双色问题：能够用两种颜色将图的所有顶点着色，任意一条边的两个端点的颜色都不相同
等价问题：这是一个二分图吗
dfs，每个顶点与邻居顶点颜色标记相反，如果遇到已经遍历的顶点和邻居顶点颜色相同，则说明该图非二分图
"""
import time
from chapter4_graph.graph import init_graph


class TwoColor():
    def __init__(self, G):
        self.__marked = [False] * G.v()
        self.color = [False] * G.v()
        self.__isTwoColorable = True
        for s in range(G.v()):
            if not self.__marked[s]:
                self.dfs(G, s)

    def dfs(self, G, v):
        self.__marked[v] = True
        for w in G.adj(v):
            if not self.__marked[w]:
                self.color[w] = not self.color[v]
                self.dfs(G, w)
            elif self.color[w] == self.color[v]:
                self.__isTwoColorable = False

    def isBipartite(self):
        return self.__isTwoColorable


if __name__ == '__main__':
    start = time.time()

    graph = init_graph()
    tc = TwoColor(graph)
    print(tc.isBipartite())

    end = time.time()
    print("run time = {}".format(end - start))
