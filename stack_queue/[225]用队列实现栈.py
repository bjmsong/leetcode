# 使用队列实现栈的下列操作： 
#
#  push(x) -- 元素 x 入栈 
#  pop() -- 移除栈顶元素 
#  top() -- 获取栈顶元素 
#  empty() -- 返回栈是否为空 
#  
# 
#  注意: 
# 
#  
#  你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合
# 法的。 
#  你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。 
#  你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。 
#  


class MyStack:

    def __init__(self):
        from collections import deque
        self.q1 = deque()  # 存储栈的其余元素
        self.q2 = deque()  # 存储栈顶元素

    def push(self, x: int) -> None:
        if self.q2:
            self.q1.append(self.q2.popleft())
        self.q2.append(x)

    def pop(self) -> int:

        top = self.q2.popleft()
        from collections import deque
        temp = deque()
        for _ in range(len(self.q1)-1):
            temp.append(self.q1.popleft())
        self.q2 = self.q1
        self.q1 = temp

        return top

    def top(self) -> int:
        return self.q2[-1]

    def empty(self) -> bool:
        return len(self.q2) == 0


if __name__ == '__main__':
    s = MyStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
    s.pop()
    print(s.empty())
