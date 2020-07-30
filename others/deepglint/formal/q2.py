# -*- coding:utf-8 -*-

import sys

line = sys.stdin.readline().split(" ")
line = [int(k) for k in line]
M, N, A, B = line[0], line[1], line[2], line[3]

matrix = []
for i in range(M):
    line = sys.stdin.readline().split(" ")
    line = [int(k) for k in line]
    matrix.append(line)

result = []
for row in range(M - A + 1):  # 0 ~ M-A
    pooling_area = []
    result_row = []
    for col in range(N):  # 0 ~ N-B
        val = []
        for a in range(A):
            val.append(matrix[row + a][col])
        pooling_area.append(val)
        if len(pooling_area) == B:
            pooling_area_value = [val for lst in pooling_area for val in lst]
            val = max(pooling_area_value)
            result_row.append(val)
            pooling_area.pop(0)
    result.append(result_row)

for i in range(len(result)):
    for item in result[i]:
        print(item, end=" ")
    print()
