import sys


def input():
    return sys.stdin.readline()


class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = 0
        self.__elements.sort()
        diff = self.__elements[len(self.__elements) - 1] - self.__elements[0]
        if diff > self.maximumDifference:
            self.maximumDifference = diff


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
