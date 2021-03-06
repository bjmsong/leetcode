# -*- coding:utf-8 -*-

"""
https://www.hackerrank.com/contests/deepglint-ai-coding-practise/challenges

2200年，在X智慧星球上有一种神奇的武器，它有一个高能准直激光发射装置，还会部署等间距的K层结界，通过K层结界来控制杀伤范围。

初始激光是绝对准直的，即不管经过多少距离，它的杀伤范围都可以认为是1x1的方格。

结界有三种类型。

第一种：普通结界, 有多种型号，型号为p的结界的杀伤范围从dxd增加到(d+p)x(d+p)

第二种：倍增结界，有多种型号，型号为p的结界的杀伤范围从dxd增加到(d*p)x(d*p)

第三种：聚集结界，有多种型号，型号为p(p>=1)，杀伤范围从(dxd)缩小到(s,s), s为满足s*p>=d的最小整数

注:经过任何一种结界，激光仍然保持为准直激光，只有杀伤范围发生了变化。

给定部署的K种结界的顺序，求最终的杀伤范围的边长是多少（显然杀伤范围是个正方形）。

[题目背景：卷积神经网络的感受野]

Input Format

第一行是一个正整数K，表示已经部署了K层结界

接下来是K行，按顺序给出K层结界的情况，每行为两个正整数z(表明结界的类型），一个正整数p(对应类型的结界的型号)

Constraints

z属于[1,3], 对应三种不同类型的结界

当z=1时，p属于[1,10]

当z=2时，p属于[2,3]

当z=3时，p属于[2,10]

在100%的测试样例中K<=1000, 且其中z=2的结界出现次数不超过10次。

Output Format

输出杀伤范围的边长

Sample Input 0

6
1 6
2 3
3 3
2 3
2 3
3 7
Sample Output 0

9

"""

import sys
k = sys.stdin.readline()
d = 1
for i in range(int(k)):
    line = sys.stdin.readline().split(" ")
    z, p = int(line[0]), int(line[1])
    if z == 1:
        d += p
    elif z == 2:
        d *= p
    else:
        div = d//p
        remain = d%p
        if remain == 0:
            d = div
        else:
            d = div + 1
print(d)
