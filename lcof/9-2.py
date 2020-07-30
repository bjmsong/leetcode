"""
Q: 两个队列实现一个栈

"""

class StackofQueue(object):
    def __init__(self):
        self.q1 = []  # 队列1
        self.q2 = []  # 队列2
        self.n = 0

    def push(self, val):
        self.q1.append(val)

    def pop(self):
        if not self.q1:
            if not self.q2:
                print("The stack is empty !")
                return
            for i in range(len(self.q2)-1):
                self.q1.append(self.q2[i])
            return self.q2[i]

        return self.q2.pop()


if __name__ == '__main__':
    stack = StackofQueue()
    stack.push(5)
    stack.push(3)
    stack.push(1)
    print(stack.pop())
    stack.push(10)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

