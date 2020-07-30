import sys
import math


def input():
    return sys.stdin.readline()


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0 :
        return False
    sqrt = int(math.sqrt(n)) + 1
    for i in range(3, sqrt, 2):
        if n % i == 0:
            return False
    return True


T = int(input())
for i in range(T):
    n = int(input())
    print("Prime" if isPrime(n) else "Not prime")
