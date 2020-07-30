# -*- coding:utf-8 -*-

import sys

line = sys.stdin.readline().split(" ")
line = [int(k) for k in line]
N, M, A, B = line[0], line[1], line[2], line[3]

matrix = []
for i in range(M):
    line = sys.stdin.readline().split(" ")
    line = [int(k) for k in line]
    matrix.append(line)


def create_area(yl, yh, xl, xh):
    area = []
    for i in range(xl, xh):
        for j in range(yl, yh):
            area.append(matrix[j][i])
    return area


matrix_p = []
for row in range(M - A + 1):  # 0 ~ M-A
    row_p = []
    for column in range(N - B + 1):  # 0 ~ N-B
        area = create_area(row, row + A, column, column + B)
        val = max(area)
        row_p.append(val)
    matrix_p.append(row_p)

for i in range(len(matrix_p)):
    for item in matrix_p[i]:
        print(item, end=" ")
    print()
