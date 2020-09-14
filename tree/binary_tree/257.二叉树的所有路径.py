"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def findPath(self, node, path):
        if not node:
            return
        # 将当前节点加入路径
        if not path:
            path = str(node.val)
        else:
            path += "->{}".format(node.val)
        if not node.left and not node.right:  # 找到叶子节点
            self.result.append(path)
            return
        self.findPath(node.left, path)
        self.findPath(node.right, path)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.findPath(root, "")
        return self.result


if __name__ == '__main__':
    s = Solution()
