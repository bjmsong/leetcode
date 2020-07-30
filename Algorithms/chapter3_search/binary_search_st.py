import time


class BinarySearchST():
    """
    基于有序数组:一对平行的数组，一个存储键一个存储值
    键有序
    查询快，插入慢
    """

    def __init__(self):
        self.keys = list()
        self.values = list()
        self.N = 0   # 键-值对的数量

    def rank(self, key):
        """
        是整个实现的核心
        返回表中小于给定键的键的数量(无论key是否包含在列表中)
        二分查找,减少查找所需的比较次数
        :param key:
        :return:
        """
        lo = 0
        hi = self.N - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2  # python3 要地板除
            if key < self.keys[mid]:
                hi = mid - 1
            elif key > self.keys[mid]:
                lo = mid + 1
            else:
                return mid
        return lo

    def put(self, key, value):
        i = self.rank(key)
        # 插入的key大于所有已经存在的key
        if i == self.N:
            self.keys.append(key)  # 不能用self.keys[self.N] , out of index !!!
            self.values.append(value)
            self.N += 1
            return

        # 命中:更新值
        if key == self.keys[i]:
            self.values[i] = value
            return

        # 未命中：添加值
        j = self.N
        self.keys.append(None)
        self.values.append(None)
        while j > i:  # i之后的数往后移一位
            self.keys[j] = self.keys[j - 1]
            self.values[j] = self.values[j - 1]
            j -= 1
        self.keys[i] = key
        self.values[i] = value
        self.N += 1

    def get(self, key):
        if self.isEmpty():
            return

        i = self.rank(key)
        if i < self.N:
            if key == self.keys[i]:
                return self.values[i]

        return

    def delete(self, key):
        if not self.contains(key): return
        i = self.rank(key)
        j = i
        while j < self.N - 1:  # j之后的数往前移一位
            self.keys[j] = self.keys[j + 1]
            self.values[j] = self.values[j + 1]
            j += 1
        self.N -= 1
        self.keys = self.keys[:self.N]
        self.values = self.values[:self.N]

    def min(self):
        # 最小的键
        return self.keys[0]

    def max(self):
        return self.keys[self.N - 1]

    def select(self, k):
        # 排名为k的键
        return self.keys[k]

    def ceiling(self, key):
        # 大于等于key的最小键
        i = self.rank(key)
        return self.keys[i]

    def floor(self, key):
        # 小于等于key的最大键
        i = self.rank(key)
        if (i < self.N) & (key == self.keys[i]):
            return key
        elif i == 0:
            return
        else:
            return self.keys[i - 1]

    def contains(self, key):
        return self.get(key) != None

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N


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

    st = BinarySearchST()
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

    st = BinarySearchST()

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
    # behavior_test()
    performance_test()  # # 20 seconds , the: 7989
