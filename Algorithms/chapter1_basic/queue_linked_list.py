"""
using linked list to implement queue structure
"""


class Node():
    def __init__(self, data, next=None):
        self.val = data
        self.next = next


class Queue():

    def __init__(self):
        self.first = None
        self.n = 0

    def enqueue(self, item):
        # 把新元素压入队尾
        if self.isEmpty():
            self.first = Node(item)
            self.n += 1
            return
        pos = self.first
        while pos.next:
            pos = pos.next
        pos.next = Node(item)
        self.n += 1

    def dequeue(self):
        # 把队首元素弹出
        if self.isEmpty():
            print("The queue is empty!")
            return
        num = self.first.val
        self.first = self.first.next
        self.n -= 1
        return num

    def isEmpty(self):
        # 是否为空
        return self.n == 0

    def __len__(self):
        return self.n

    def __iter__(self):
        cur = self.first
        while cur:
            yield cur.val
            cur = cur.next


if __name__ == '__main__':
    print("Test case 1:")
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(5)
    print(q.dequeue())
    print("Length of queue is {}".format(len(q)))
    for i in q:
        print(i)

    print("Test case 2:")
    q = Queue()
    q.dequeue()
    print("Length of queue is {}".format(len(q)))
