"""
Q:重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，重建二叉树

"""


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self, level=0):
        """
        递归
        魔术方法__str__：https://blog.csdn.net/luckytanggu/article/details/53649156
        :param level: 层级
        :return: list
        """
        # repr：对象转化为供解释器读取的形式，返回一个对象的string格式
        ret = "\t" * level + repr(self.val) + "\n"
        if self.left:  # 左节点是否非None
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret


def rebuildBinaryTree(front, mid):
    """
    前序遍历：根结点-左结点（前序遍历）-右结点（前序遍历）
    中序遍历：左结点（中序遍历）-根结点-右结点（中序遍历）
    :param front: 前序遍历的结果
    :param mid: 中序遍历的结果
    """
    if len(front) == 0:
        return
    root = front[0]
    index = mid.index(root)
    left_mid = mid[:index]
    right_mid = mid[index + 1:]
    left_front = front[1:len(left_mid) + 1]
    right_front = front[len(left_mid) + 1:]

    head = BinaryTreeNode(root)
    head.left = rebuildBinaryTree(left_front, left_mid)
    head.right = rebuildBinaryTree(right_front, right_mid)
    return head


if __name__ == '__main__':
    front = [1, 2, 4, 7, 3, 5, 6, 8]
    mid = [4, 7, 2, 1, 5, 3, 8, 6]
    head = rebuildBinaryTree(front, mid)
    print(head)
