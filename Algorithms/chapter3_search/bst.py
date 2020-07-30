import time


class Node():
    """
    二叉查找树的结点
    """

    def __init__(self, key, value, N):
        self.key = key
        self.value = value
        self.left = None  # 小于该结点的所有键组成的二叉查找树
        self.right = None  # 大于该结点的所有键组成的二叉查找树
        self.N = N  # 以该结点为根的子树的结点总数


class BST():
    """
    基于二叉查找树
    """

    def size(self, node):
        if node is None:
            return 0
        else:
            return node.N

    def put(self, node, key, value):
        """
        递归: 沿着树向下走，重置搜索路径上每个父结点指向子结点的链接，并重新计数
        :param node: 当前结点
        :param key:
        :param value:
        :return:
        """
        if node is None:  # 基线条件
            return Node(key, value, 1)
        if key > node.key:
            node.right = self.put(node.right, key, value)
        elif key < node.key:
            node.left = self.put(node.left, key, value)
        else:
            node.value = value  # 替换原结点值

        node.N = self.size(node.left) + self.size(node.right) + 1
        return node

    def get(self, node, key):
        # 递归：沿着树向下走，然后返回
        if node is None:  # 基线条件
            return None
        if key > node.key:
            return self.get(node.right, key)
        elif key < node.key:
            return self.get(node.left, key)
        else:
            return node.value

    def max(self, node):
        # 递归,直到右链接为空
        if node.right is None:
            return node
        return self.max(node.right)

    def min(self, node):
        # 递归,直到左链接为空
        if node.left is None:
            return node
        return self.min(node.left)

    def floor(self, node, key):
        # 向下取整：小于等于该键的最大键
        # 递归
        if node is None:
            return None
        if key == node.key:
            return key
        if key < node.key:  # 在左子树中继续寻找
            return self.floor(node.left, key)
        # key>root.key 则在右子树中寻找
        t = self.floor(node.right, key)
        if t is not None:
            return t
        else:
            return node.key  # 右子树中没有找到，则返回根结点

    def ceiling(self, node, key):
        # 向上取整：大于等于该键的最小键
        # 递归
        if node is None:
            return None
        if key == node.key:
            return key
        if key > node.key:
            return self.ceiling(node.right, key)
        t = self.ceiling(node.left, key)
        if t is not None:
            return t
        else:
            return node.key

    def select(self, node, k):
        # 查找排名为k的键(即树中有k个小于它的键)
        if node is None: return None
        if k < 0: return None
        t = self.size(node.left)
        if t < k:
            return self.select(node.right, k - t - 1)
        elif t == k:
            return node.key
        else:
            return self.select(node.left, k)

    def rank(self, node, key):
        # select()的逆方法,返回给定键的排名(该键不一定存在二叉树中)
        if node is None: return 0
        if key == node.key:
            return self.size(node.left)
        elif key < node.key:
            return self.rank(node.left, key)
        else:
            return 1 + self.size(node.left) + self.rank(node.right, key)

    def delMax(self, node):
        if node is None:
            return None
        if node.right is None:
            return node.left
        else:
            node.right = self.delMax(node.right)

        node.N = self.size(node.right) + self.size(node.left) + 1
        return node

    def delMin(self, node):
        if node is None:
            return None
        if node.left is None:
            return node.right  # 返回该结点的右链接
        else:
            node.left = self.delMin(node.left)

        node.N = self.size(node.right) + self.size(node.left) + 1  # 每一次递归都会重新计算结点数量
        return node

    def delete(self, node, key):

        if node is None:
            return None
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            t = node  # node有两个结点
            node = self.min(t.right)  # 右子树的最小结点作为后继结点
            node.right = self.delMin(t.right)  # 右链接指向删除最小结点后的右子树
            node.left = t.left  # 左链接不变

        node.N = self.size(node.left) + self.size(node.right) + 1
        return node

    def contains(self, node, key):
        if node is None:
            return False
        if key is None:
            return False
        if key == node.key:
            return True
        elif key > node.key:
            return self.contains(node.right, key)
        else:
            return self.contains(node.left, key)

    def isEmpty(self, root):
        return root is None

    def keys(self, root):
        # 返回keys，遍历二叉树(中序遍历)
        keylist = []
        if root is not None:
            keylist.append(root.key)
            if root.left is not None:
                keylist.extend(self.keys(root.left))   # extend:在列表末尾一次性追加另一个序列
            if root.right is not None:
                keylist.extend(self.keys(root.right))

        return keylist


def print_key_value(root, st):
    keys = list()
    values = list()
    for k in st.keys(root):
        keys.append(k)
        values.append(st.get(root, k))
    print("keys:{}".format(keys))
    print("values:{}".format(values))


def behavior_test():
    # 行为测试
    with open("../data/st.txt", "r") as f:
        keys = f.readline().strip().split(" ")
        values = f.readline().strip().split(" ")

    print(keys)
    print(values)

    st = BST()
    root = None  # 二叉查找树的根结点
    for k, v in zip(keys, values):
        root = st.put(root, k, v)

    print_key_value(root, st)

    print(st.contains(root, "S"))
    print(st.contains(root, "SS"))
    print(st.contains(root, None))

    st.delete(root, "E")
    st.delete(root, "EE")
    st.delete(root, "A")

    print_key_value(root, st)

    print(st.floor(root, "D"))
    print(st.ceiling(root, "D"))

    print(st.select(root, 5))
    print(st.rank(root, "Z"))

    st.delMin(root)
    st.delMax(root)


def performance_test():
    # 性能测试:统计词频
    start = time.time()

    st = BST()
    root = None

    with open("../data/tale.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        tale = line.strip().split(" ")
        for word in tale:
            if not st.contains(root, word):
                root = st.put(root, word, 1)
            else:
                root = st.put(root, word, st.get(root, word) + 1)

    print_key_value(root, st)

    max = " "
    root = st.put(root, max, 0)
    for word in st.keys(root):
        if st.get(root, word) > st.get(root, max):
            max = word
    print(max + ":", st.get(root, max))

    end = time.time()
    print("run time = {}".format(end - start))


if __name__ == '__main__':
    behavior_test()
    # performance_test()  # 3 seconds , the: 7989
