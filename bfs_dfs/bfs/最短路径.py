"""
Return the length of the shortest path between root and target node.
"""

from collections import deque


def bfs(root, target):
    q = deque()
    visited = set()
    step = 0
    q.append(root)
    visited.add(root)
    while q:
        length = len(q)
        for i in range(length):
            node = q.popleft()
            if node == target:
                return step
            for neighbors in node.adjs:
                if neighbors not in visited:
                    q.append(neighbors)
                    visited.add(neighbors)
        step += 1

    return -1
