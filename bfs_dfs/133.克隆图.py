"""
克隆图
给你无向连通图中一个节点的引用，请你返回该图的深拷贝（克隆）
图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）
"""


class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node):
        """
        DFS
        时间复杂度：O(n)，每个节点只访问一次
        """
        lookup = {}    # 新旧节点间的对应关系

        def dfs(node):
            if not node:
                return
            if lookup.get(node):
                return lookup[node]
            clone = Node(node.val)
            lookup[node] = clone
            for next in node.neighbors:
                clone.neighbors.append(dfs(next))
            return lookup[node]

        return dfs(node)

    # def cloneGraph(self, node):
    #     """
    #     BFS: 把原图的节点加入队列中，遍历直到队列为空
    #     :param node:
    #     :return:
    #     """
    #     if not node:
    #         return
    #
    #     from collections import deque
    #     q = deque()
    #     q.append(node)
    #     visited = {node: Node(node.val, [])}
    #     while q:
    #         n = q.popleft()
    #         clone = visited[n]
    #         for n1 in n.neighbors:
    #             if not n1:
    #                 break
    #             if n1 in visited:
    #                 clone.neighbors.append(visited[n1])
    #             else:
    #                 visited[n1] = Node(n1.val, [])
    #                 clone.neighbors.append(visited[n1])
    #                 q.append(n1)
    #
    #     return visited[node]


if __name__ == '__main__':
    s = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    clone = s.cloneGraph(node1)
    print(clone)
