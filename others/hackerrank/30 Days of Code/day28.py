import sys
import math
import os
import random
import re


def input():
    return sys.stdin.readline()


if __name__ == '__main__':
    N = int(input())
    namelist = []
    for _ in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.search(".+@gmail\.com$", emailID):
            namelist.append(firstName)

    namelist.sort()
    for i in namelist:
        print(i)
