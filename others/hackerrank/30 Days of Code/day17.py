import math
import sys


def input():
    return sys.stdin.readline()


class NegativeException(Exception):
    pass


class Calculator():
    def __init__(self):
        pass

    def power(self, n, p):
        try:
            if n < 0 or p < 0:
                raise NegativeException()
            return int(math.pow(n, p))
        except NegativeException:
            raise Exception("n and p should be non-negative")


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
