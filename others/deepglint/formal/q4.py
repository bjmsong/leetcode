# -*- coding:utf-8 -*-

import sys
# import numpy as np
import math

# pi = math.pi
degree = sys.stdin.readline().split(" ")
theta = [math.radians(int(k)) for k in degree]
pitch, yaw, roll = theta[0], theta[1], theta[2]

# rx = np.array([[1, 0, 0], [0, np.cos(pitch), np.sin(pitch)], [0, -np.sin(pitch), np.cos(pitch)]])
# ry = np.array([[np.cos(yaw), 0, -np.sin(yaw)], [0, 1, 0], [np.sin(yaw), 0, np.cos(yaw)]])
# rz = np.array([[np.cos(roll), np.sin(roll), 0], [-np.sin(roll), np.cos(roll), 0], [0, 0, 1]])
#
# w1 = np.dot(np.dot(np.dot(rx, ry), rz), (0, 0, 1))
# w2 = np.dot(np.dot(np.dot(rx, ry), rz), (0, 1, 0))


rx = [[1, 0, 0], [0, math.cos(pitch), math.sin(pitch)], [0, -math.sin(pitch), math.cos(pitch)]]
ry = [[math.cos(yaw), 0, -math.sin(yaw)], [0, 1, 0], [math.sin(yaw), 0, math.cos(yaw)]]
rz = [[math.cos(roll), math.sin(roll), 0], [-math.sin(roll), math.cos(roll), 0], [0, 0, 1]]


def multiply(a, b):
    # 矩阵乘法
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]


w1 = multiply(multiply(multiply(rx, ry), rz), [[0], [0], [1]])
w2 = multiply(multiply(multiply(rx, ry), rz), [[0], [1], [0]])

w1 = [k[0] for k in w1]
w2 = [k[0] for k in w2]

def formated(k):
    if round(k, 3) == 0:
        val = abs(k)
    else:
        val = k
    return val


w1 = [formated(k) for k in w1]
w2 = [formated(k) for k in w2]

print("{:.3f} {:.3f} {:.3f}".format(w1[0], w1[1], w1[2]))
print("{:.3f} {:.3f} {:.3f}".format(w2[0], w2[1], w2[2]))
