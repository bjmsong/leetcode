"""
数据流中的移动平均值
给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。
示例：
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""


from collections import deque

class MovingAverage():
    def __init__(self, window):
        self.q = deque()
        self.window = window

    def next(self, val):
        self.q.append(val)
        if len(self.q) > self.window:
            self.q.popleft()
        return sum(self.q) / len(self.q)
