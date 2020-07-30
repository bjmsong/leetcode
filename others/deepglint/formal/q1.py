# -*- coding:utf-8 -*-

"""
https://www.hackerrank.com/contests/deepglint-ai-coding/challenges
"""

import sys

for i in range(5):
    N = sys.stdin.readline()
    red = sys.stdin.readline().split(" ")
    red_x = [red[k] for k in range(len(red)) if k % 2 == 0]
    red_y = [red[k] for k in range(len(red)) if k % 2 == 1]
    blue = sys.stdin.readline().split(" ")
    blue_x = [blue[k] for k in range(len(blue)) if k % 2 == 0]
    blue_y = [blue[k] for k in range(len(blue)) if k % 2 == 1]

    # 是否线性可分 : 范围没有交叉
    red_x_max = max(red_x)
    red_x_min = min(red_x)
    red_y_max = max(red_y)
    red_y_min = min(red_y)

    blue_x_max = max(blue_x)
    blue_x_min = min(blue_x)
    blue_y_max = max(blue_y)
    blue_y_min = min(blue_y)

    if red_x_max < blue_x_min or blue_x_max < red_x_min or red_y_max < blue_y_min or blue_y_max < red_y_min:
        print(True)
    else:
        print(False)
