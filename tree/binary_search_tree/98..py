"""
验证二叉搜索树

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

- 节点的左子树只包含小于当前节点的数。
- 节点的右子树只包含大于当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        """
        递归
        父节点是左子树节点的上界，是右子树节点的下界
        时间复杂度：O(n),每个节点遍历一次
        空间复杂度：O(n)，递归栈的深度最大为n
        """

        def helper(node, lower=float("-inf"), upper=float("inf")):
            """
            验证以node为根节点的树为二叉搜索树
            lower： 左子树节点的下界
            upper： 右子树节点的上界
            """
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not helper(node.left, lower, node.val):
                return False
            if not helper(node.right, node.val, upper):
                return False
            return True

        return helper(root)

    # def isValidBST(self, root: TreeNode) -> bool:
    #     """
    #     中序遍历：左结点、根节点、右节点
    #     中序遍历的结果一定是升序的，如果不是的话，说明不是二叉搜索树
    #     :param root:
    #     :return:
    #     """
    #     stack, inorder = [], float('-inf')
    #
    #     while stack or root:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         root = stack.pop()
    #         # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
    #         if root.val <= inorder:
    #             return False
    #         inorder = root.val
    #         root = root.right
    #
    #     return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    s = Solution()
    print(s.isValidBST(root))

    # [10,5,15,null,null,6,20]
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    print(s.isValidBST(root))
