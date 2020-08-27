# 使用栈实现队列的下列操作： 
# 
#  
#  push(x) -- 将一个元素放入队列的尾部。 
#  pop() -- 从队列首部移除元素。 
#  peek() -- 返回队列首部的元素。 
#  empty() -- 返回队列是否为空。 
#  
# 
#  
# 
#  示例: 
# 
#  MyQueue queue = new MyQueue();
# 
# queue.push(1);
# queue.push(2);  
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false 
# 
#  
# 
#  说明: 
# 
#  
#  你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
#  
#  你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。 
#  假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。 
#  
#  Related Topics 栈 设计


class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []  # 存储队列头部的元素

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        if not self.s2:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        for _ in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0 and len(self.s2) == 0



if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.pop()
    print(q.empty())