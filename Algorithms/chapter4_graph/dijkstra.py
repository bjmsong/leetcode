import time
import sys
from chapter4_graph.graph import init_graph


def Dijkstra(name_list, W, s, MAX):
    '''
    Dijkstra 算法：计算从源点到其他点的最短距离
        BFS，贪心算法，只做当前最好的选择
    W：权重矩阵，存放图中所有边的非负权值，对称矩阵
    name_list：按照顺序存放W中点的名称，从0开始
    s：源点
    return：存放源点到其他点的最短距离

    https://blog.csdn.net/heroacool/article/details/51014824
    '''

    # 将点名称s改为点索引s
    for i, name in enumerate(name_list):
        if name == s:
            s = i
            break
    # 初始化
    dist = [MAX for x in range(len(name_list))]  # s到所有点的距离，初始化为最大值
    dist[s] = 0  # s到s的距离为0
    min_point = s  # 距离s最短的点为s
    T = set()  # 存放已经算出最短距离的点，初始化为空

    # 开始循环
    while len(T) < len(name_list):  # 一直循环直至T包含了所有点
        # step2:更新各个点到源点的距离
        T.add(min_point)  # 将距离最短的点加入到T中
        for i, w in enumerate(W[min_point]):  # 遍历min_point的所有直接相连的点
            if i not in T and w > 0:  # 只需要更新不属于T的、权值大于0的点
                dist[i] = min(dist[i], dist[min_point] + W[min_point][i])  # 取最小值
        # step1:选出T之外的点中距离源点最短的点
        min_dist = MAX
        for i, d in enumerate(dist):
            if i not in T and d > 0 and d < min_dist:
                min_dist = d
                min_point = i
    return dict((name_list[i], d) for i, d in enumerate(dist))  # 将结果集中的点索引换为点名称，放入到词典中


if __name__ == '__main__':
    MAX = sys.maxsize  # 值的上限
    W = [[0, 9, 4, MAX],
         [9, 0, 3, 1],
         [4, 3, 0, 1],
         [MAX, 1, 1, 0]]
    name_list = ['A', 'B', 'C', 'D']
    print(Dijkstra(name_list, W, 'A', MAX))
