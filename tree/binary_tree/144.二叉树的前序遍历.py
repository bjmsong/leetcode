"""
给定一个二叉树，返回它的前序遍历

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    root-left-right
    """
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root):
        # 递归
        if not root:
            return []
        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.result

    # def preorderTraversal(self, root):
    #     """
    #     迭代
    #     - 从根节点开始，每次迭代弹出当前栈顶元素，并将其子节点压入栈中(先压右子节点再压左子节点)
    #     - 在这个算法中，输出到最终结果的顺序按照 Top->Bottom 和 Left->Right，符合前序遍历的顺序
    #     """
    #     stack = []
    #     result = []
    #     if not root:
    #         return result
    #     stack.append(root)
    #     while stack:
    #         node = stack.pop()
    #         result.append(node.val)
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)
    #
    #     return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    print(s.preorderTraversal(root))
