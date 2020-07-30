"""
给定一个二叉树，返回它的 后序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    left-right-root
    """

    def __init__(self):
        self.result = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.result.append(root.val)

        return self.result
