import time


class ListNode():

    def __init__(self, k, v, next):
        self.key = k
        self.value = v
        self.next = next


class SequentialSearchST():
    """
    基于链表，每个结点存储一个键值对
    插入、查找都慢
    """

    def __init__(self):
        # 链表的首个结点
        self.first = None
        # number of key-value pairs
        self.N = 0

    def put(self, key, value):
        x = self.first
        while x:
            # 命中，更新结点
            if key == x.key:
                x.value = value
                return
            x = x.next
        # 如果没有命中，新结点加到头部
        self.first = ListNode(key, value, self.first)
        self.N += 1

    def get(self, key):
        x = self.first
        while x:
            if key == x.key:
                return x.value
            x = x.next

        return None

    def delete(self, key):

        self.first = self.deleteNode(key, self.first)

    def deleteNode(self, key, node):
        if not node:
            return None
        if key == node.key:
            self.N -= 1
            return node.next
        node.next = self.deleteNode(key, node.next)
        return node

    def contains(self, key):
        return self.get(key) != None

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def keys(self):
        lst = list()
        x = self.first
        while x:
            lst.append(x.key)
            x = x.next
        return lst


def print_key_value(st):
    keys = list()
    values = list()
    for k in st.keys():
        keys.append(k)
        values.append(st.get(k))
    print("keys: ", keys)
    print("values: ", values)


def behavior_test():
    # 行为测试
    with open("../data/st.txt", "r") as f:
        keys = f.readline().strip().split(" ")
        values = f.readline().strip().split(" ")

    print(keys)
    print(values)

    st = SequentialSearchST()
    for k, v in zip(keys, values):
        st.put(k, v)

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

    st = SequentialSearchST()

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
    for word in st.keys():
        if st.get(word) > st.get(max):
            max = word
    print(max + ":", st.get(max))

    end = time.time()
    print("run time = {}".format(end - start))


if __name__ == '__main__':
    behavior_test()
    # performance_test()  # 590 seconds , the: 7989
