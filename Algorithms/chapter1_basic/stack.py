"""
栈：后进先出
push()
pop()
"""


class Stack():
    """
    数组实现
    """

    def __init__(self):
        self.stack = list()
        self.n = 0

    def push(self, c):
        self.stack.append(c)
        self.n += 1

    def pop(self):

        self.n -= 1
        self.stack.pop()

    def __len__(self):
        return self.n

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self.stack[cursor]
            cursor += 1


if __name__ == '__main__':
    stack = Stack()
    s = input("请输入(如 to be or not to be - be -- that - - - is):")
    s_split = s.split(" ")
    for i in range(len(s_split)):
        c = s_split[i]
        if c == "-":
            stack.pop()
        else:
            stack.push(c)

    print(len(stack))
    for i in stack:
        print(i)
