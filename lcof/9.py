"""
Q: 两个栈构造一个队列
"""


class QueueOfStack(object):
    def __init__(self):
        self.s1 = []  # 栈1
        self.s2 = []  # 栈2

    def enqueue(self, val):
        self.s1.append(val)

    def dequeue(self):
        if not self.s2:
            if not self.s1:
                print("The queue is empty !")
                return
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())

        return self.s2.pop()


if __name__ == '__main__':
    queue = QueueOfStack()
    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(1)
    print(queue.dequeue())
    queue.enqueue(10)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
