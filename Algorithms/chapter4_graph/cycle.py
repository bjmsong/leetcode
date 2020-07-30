"""
检测环：给定的图是无环图吗
dfs过程中，遇到已经mark的点，表明有环
"""

import time
from chapter4_graph.graph import init_graph


class Cycle():
    def __init__(self, G):
        self.__hasCycle = False
        self.__marked = [False] * G.v()  # 标记是否已遍历
        for s in range(G.v()):
            if not self.__marked[s]:
                self.__dfs(G, s, s)

    def __dfs(self, G, v, u):
        # u和v是邻边
        self.__marked[v] = True
        for w in G.adj(v):
            if not self.__marked[w]:
                self.__dfs(G, w, v)
            elif w != u:    # 遇到已经mark的点,并且不是邻边
                self.__hasCycle = True
                return

    def hasCycle(self):
        return self.__hasCycle


if __name__ == '__main__':
    start = time.time()

    graph = init_graph()
    print(graph.adj(0))
    cycle = Cycle(graph)
    print(cycle.hasCycle())

    end = time.time()
    print("run time = {}".format(end - start))
