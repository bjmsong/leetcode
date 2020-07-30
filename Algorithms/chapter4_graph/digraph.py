"""
有向图:邻接表实现
"""
import re


class Digraph():

    def __init__(self, V):
        self.V = V  # 顶点数
        self.E = 0  # 边数
        self.__adj = list()  # 邻接表
        for i in range(self.V):
            self.__adj.append([])

    def addEdge(self, v, w):
        self.__adj[v].append(w)  # 添加有向边:v->w
        self.E += 1

    def adj(self, v):
        return self.__adj[v]

    def reverse(self):
        # 返回有向图的一个副本，所有边反转
        r = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj(v):
                r.addEdge(w, v)
        return r

    def v(self):
        return self.V

    def e(self):
        return self.E


def init_graph():
    with open("../data/tinyDG.txt", "r") as f:
        vertex_num = int(f.readline())
        edge_num = int(f.readline())
        edges = f.readlines()

    graph = Digraph(vertex_num)
    for edge in edges:
        edge = re.split("\s+", edge.strip())
        graph.addEdge(int(edge[0]), int(edge[1]))

    return graph


if __name__ == '__main__':
    graph = init_graph()
    print("Edge num: " + str(graph.e()))
    print("Vertex num: " + str(graph.v()))
    print(graph.adj(0))
    print(graph.reverse().adj(0))