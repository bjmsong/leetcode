"""
N叉树的前序遍历(根节点、子节点)
给定一个 N 叉树，返回其节点值的前序遍历。
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.result = []

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return self.result
        self.result.append(root.val)
        for node in root.children:
            self.preorder(node)

        return self.result
