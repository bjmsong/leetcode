"""
实现Graph API:邻接表数组
"""


class Graph():
    def __init__(self, vertex_num):
        self.V = vertex_num
        self.E = 0
        self.__adj = list()  # 邻接表
        for i in range(self.V):
            self.__adj.append([])

    def v(self):
        return self.V

    def e(self):
        return self.E

    def addEdge(self, v, w):
        self.__adj[v].append(w)
        self.__adj[w].append(v)
        self.E += 1

    def adj(self, v):
        # 返回相邻顶点
        return self.__adj[v]


def init_graph():
    with open("../data/tinyG.txt", "r") as f:
        vertex_num = int(f.readline())
        edge_num = int(f.readline())
        edges = f.readlines()

    graph = Graph(vertex_num)
    for edge in edges:
        edge = edge.strip().split(" ")
        graph.addEdge(int(edge[0]), int(edge[1]))

    return graph


if __name__ == '__main__':
    graph = init_graph()
    print("Edge num: " + str(graph.e()))
    print("Vertex num: " + str(graph.v()))
    print(graph.adj(0))
