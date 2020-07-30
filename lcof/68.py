"""
Q: 二叉树的最近公共祖先

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode, p: TreeNode, path) -> List[int]:
        """
        前序遍历
        :param root:
        :return:
        """
        if not root:
            return path

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        前序遍历，得到root->p,root->q的路径
        两条路径的第一个公共节点，即为最低公共祖先
        时间复杂度：O(n)
        空间复杂度：O(logn)
        :param root:
        :param p:
        :param q:
        :return:
        """
        p_path = self.preorderTraversal(root, p, [])
        q_path = self.preorderTraversal(root, q, [])
        ancestor = root
        for p, q in zip(p_path, q_path):
            if p == q:
                ancestor = p
            else:
                break
        return ancestor


if __name__ == '__main__':
    pass
