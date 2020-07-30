"""
实现图搜索API:BFS
"""

import time
from collections import deque
from chapter4_graph.graph import init_graph


class BreadthFirstSearch():

    def __init__(self, G, s):
        self.s = s  # 起点
        self.__marked = [False] * G.v()  # 标记是否已经遍历，即和s是否连通
        self.__count = 0  # 与s连通的顶点总数
        self.edgeTo = [None] * G.v()  # 到达该顶点的已知路径上的最后一个顶点
        self.__bfs(G, s)

    def __bfs(self, G, s):
        self.__marked[s] = True
        queue = deque()
        queue.append(s)
        while queue:
            v = queue.popleft()
            self.__count += 1
            for w in G.adj(v):
                if not self.__marked[w]:
                    queue.append(w)
                    self.__marked[w] = True
                    self.edgeTo[w] = v

    def count(self):
        return self.__count

    def marked(self, v):
        return self.__marked[v]

    def hasPathTo(self, v):
        return self.__marked[v]

    def pathTo(self, v):
        if not self.__marked[v]:
            return
        path = list()
        x = v
        while x != self.s:
            path.insert(0, x)
            x = self.edgeTo[x]
        path.insert(0, self.s)
        return path


if __name__ == '__main__':
    start = time.time()

    graph = init_graph()
    bfs = BreadthFirstSearch(graph, 0)
    print(bfs.count())
    print(bfs.marked(1))
    print(bfs.marked(10))
    print("Path to 3 is:", bfs.pathTo(3))

    end = time.time()
    print("run time = {}".format(end - start))
