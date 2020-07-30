import time


class Node():
    """
    红黑树的结点
    """

    def __init__(self, key, value, N, color):
        self.key = key
        self.value = value
        self.left = None  # 小于该结点的所有键组成的二叉查找树
        self.right = None  # 大于该结点的所有键组成的二叉查找树
        self.N = N  # 以该结点为根的子树的结点总数
        self.color = color  # 指向它的链接：红色/黑色


class RedBalckBST():
    """
    基于红黑树
    """

    def rotateRight(self, h):
        # 如果左子结点是红色且它的左子结点也是红色的，进行右旋转
        x = h.left
        h.left = x.right
        x.color = h.color
        h.color = 'R'
        x.right = h
        x.N = h.N
        h.N = 1 + self.size(h.left) + self.size(h.right)
        return x

    def rotateLeft(self, h):
        # 如果右子结点是红色而左子结点是黑色的，进行左旋转
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = 'R'
        x.N = h.N
        h.N = 1 + self.size(h.left) + self.size(h.right)
        return x

    def flipColor(self, h):
        # 如果左右子结点都是红色，进行颜色转换
        assert not self.__isRed(h)
        assert self.__isRed(h.left)
        assert self.__isRed(h.right)

        h.color = 'R'
        h.left.color = 'B'
        h.right.color = 'B'

    def put(self, node, key, value):
        if node is None:
            return Node(key, value, 1, )

    def get(self, node, key):
        if node is None: return None
        if key > node.key:
            return self.get(node.right, key)
        elif key < node.key:
            return self.get(node.left, key)
        else:
            return node.value

    def delete(self, key):
        pass

    def contains(self, key):
        pass

    def isEmpty(self):
        pass

    def size(self, node):
        if node is None:
            return 0
        return node.N

    def keys(self):
        pass

    def __isRed(self, node):
        if node is None:
            return False
        return node.color == 'R'


def print_key_value(st):
    keys = list()
    values = list()
    for k in st.keys:
        keys.append(k)
        values.append(st.get(k))
    print(keys)
    print(values)


def behavior_test():
    # 行为测试
    with open("../data/st.txt", "r") as f:
        keys = f.readline().strip().split(" ")
        values = f.readline().strip().split(" ")

    print(keys)
    print(values)

    st = RedBalckBST()
    root = None
    for k, v in zip(keys, values):
        st.put(root, k, v)

    print_key_value(st)

    print(st.contains("S"))
    print(st.contains("SS"))
    print(st.contains(None))

    st.delete("E")
    st.delete("EE")
    st.delete("A")

    print_key_value(st)


def performance_test():
    # 性能测试:统计词频
    start = time.time()

    st = RedBalckBST()

    with open("../data/tale.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        tale = line.strip().split(" ")
        for word in tale:
            if not st.contains(word):
                st.put(word, 1)
            else:
                st.put(word, st.get(word) + 1)

    print_key_value(st)

    max = " "
    st.put(max, 0)
    for word in st.keys:
        if st.get(word) > st.get(max):
            max = word
    print(max + ":", st.get(max))

    end = time.time()
    print("run time = {}".format(end - start))


if __name__ == '__main__':
    behavior_test()
    # performance_test() # seconds , the: 7989
