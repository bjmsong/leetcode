"""
Q: 二叉树的下一个节点
给定一棵二叉树和其中一个节点，如何找出中序遍历序列的下一个节点

"""


class BinaryTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None   # 指向父节点


class Solution:
    def GetNext(self, pNode):
        """
        三种情况
        1. 给定的节点为空：返回空；
        2. 给定的节点有右子树：沿着该右子树，返回右子树的第一个左叶子节点；
        3. 给定的节点没有右子树：如果位于某个节点的左子树中，则上溯直至找到该节点；否则就返回空。
        【因为按照中序遍历“左中右”的遍历方式，当该节点没有右子树时，要么遍历完毕，下一个节点为空；要么某个子树的左子树遍历完毕，下一个节点是子树的根节点】
        """
        if not pNode:
            return
        if not pNode.right:
            return self.getHead(pNode)
        return self.getRightNode(pNode.right)

    def getHead(self, pNode):
        while pNode.next:
            if pNode.next.right == pNode:
                pNode = pNode.next
            elif pNode.next.left == pNode:
                return pNode.next
        return None

    def getRightNode(self, pNode):
        while pNode.left:
            pNode = pNode.left
        return pNode


if __name__ == '__main__':
    pass
