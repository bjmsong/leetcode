#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (43.19%)
# Total Accepted:    511.9K
# Total Submissions: 1.2M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
# 
# 
# 
# Constraints:
# 
# 
# Methods pop, top and getMin operations will always be called on non-empty
# stacks.
# 
# 
#
class MinStack:
    """
    用一个栈存储栈中的最小值，栈的最后一位表示当前的最小值
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []   # 存储栈中的最小值


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:  # 重复的最小值都会被添加到min_stack
            self.min_stack.append(x)

    def pop(self) -> None:
        if not self.isEmpty():
            if self.stack.pop() == self.min_stack[-1]:
                self.min_stack.pop()


    def top(self) -> int:
        if not self.isEmpty():
            return self.stack[-1]


    def getMin(self) -> int:
        if not self.isEmpty():
            return self.min_stack[-1]


    def isEmpty(self):
        return len(self.stack) == 0



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())
    ms.pop()
    print(ms.top())
    print(ms.getMin())