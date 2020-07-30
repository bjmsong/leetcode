class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack():

    def __init__(self):
        self.first = None
        self.n = 0

    def push(self, item):
        # 把元素压入队首
        if self.isEmpty():
            self.first = Node(item)
            self.n += 1
            return
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1

    def pop(self):
        # 把队首元素弹出
        if self.isEmpty():
            print("The stack is empty")
            return
        val = self.first.data
        self.first = self.first.next
        self.n -= 1
        return val

    def top(self):
        # 查看队首元素
        return self.first.data

    def isEmpty(self):
        # 是否为空
        return self.n == 0

    def __len__(self):
        return self.n

    def __iter__(self):
        cur = self.first
        while cur:
            yield cur.data
            cur = cur.next


if __name__ == '__main__':
    print("Test case 1:")
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(5)
    print(stack.pop())
    print("Length of stack is {}".format(len(stack)))
    for i in stack:
        print(i)
    print(stack.top())

    print("Test case 2:")
    stack = Stack()
    stack.pop()
    print("Length of stack is {}".format(len(stack)))

    print("Test case 3:")
    stack = Stack()
    stack.push(1)
    stack.pop()
    print("Length of stack is {}".format(len(stack)))
