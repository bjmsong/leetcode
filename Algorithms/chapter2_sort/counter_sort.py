import time

"""
计数排序：
在内存中开辟max_num（序列中的最大值）+1的空间当做多个桶。序列中出现一个数字num，那就找到对应的桶，加1。
常见的排序算法中，桶排序可以说是速度最快的一种排序算法了(O(n))，当然内存的占用不可避免(O(n))
"""

def bucket_sort(arry):
    max_num = max(arry)
    bucket = [0] * (max_num + 1)
    for i in arry:
        bucket[i] += 1
    sort_arry = []
    for j in range(len(bucket)):
        if bucket[j] != 0:
            for y in range(bucket[j]):  # 重复元素
                sort_arry.append(j)
    return sort_arry



if __name__ == '__main__':
    dis_arry = [3, 4, 1, 21, 6, 41, 23, 2, 2, 3, 4, 1, 21, 6, 41, 23, 2, 2]
    start = time.clock()
    print(bucket_sort(dis_arry))
    end = time.clock()
    print(end - start)
