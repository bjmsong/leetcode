"""
N叉树的层序遍历
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        from collections import deque
        q = deque()
        q.append(root)
        result = []
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                for child in node.children:
                    q.append(child)
            result.append(temp)

        return result
