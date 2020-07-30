#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#
# https://leetcode.com/problems/sliding-window-median/description/
#
# algorithms
# Hard (33.11%)
# Total Accepted:    28K
# Total Submissions: 84.4K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# Examples: 
# [2,3,4] , the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5 
# 
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position. Your
# job is to output the median array for each window in the original array.
# 
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
# 
# 
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
# ⁠1 [3  -1  -3] 5  3  6  7       -1
# ⁠1  3 [-1  -3  5] 3  6  7       -1
# ⁠1  3  -1 [-3  5  3] 6  7       3
# ⁠1  3  -1  -3 [5  3  6] 7       5
# ⁠1  3  -1  -3  5 [3  6  7]      6
# 
# 
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].
# 
# Note: 
# You may assume k is always valid, ie: k is always smaller than input array's
# size for non-empty array.
#
class Solution:
    # def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    #     # 滑动窗口题型
    #     # 暴力解法：效率低
    #     median = []
    #     index = 0
    #     while index <= len(nums)-k:
    #         sliding = nums[index:k+index]
    #         sliding.sort()
    #         if k % 2 ==0:
    #             median.append((sliding[k//2-1]+sliding[k//2])/2)
    #         else:
    #             median.append(sliding[k//2])
    #         index += 1

    #     return median

    # def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    #     # eg : [1,3,-1,-3,5,3,6,7]
    #     # 插入排序
    #     import bisect   
    #     if k == 0: 
    #         return []
    #     ans = []
    #     window = sorted(nums[0:k])
    #     for i in range(k, len(nums) + 1):   # 滑动窗口
    #         ans.append((window[k // 2] + window[(k - 1) // 2]) / 2.0)  # 无论k是奇数还是偶数
    #         if i == len(nums): 
    #             break
    #         index = bisect.bisect_left(window, nums[i - k])    # 返回最左边值的索引，如果有重复值，返回最左边那个
    #         window.pop(index)                                  # 剔除最左边的值
    #         bisect.insort_left(window, nums[i])                # 加入一个新值，按顺序插入
    #     return ans


    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        基于二叉堆(优先队列)
        步骤：
            1. 构造堆
            2. 调整堆大小
            3. 获取中位数
            4. 滑动窗口,移除元素
        https://blog.csdn.net/MebiuW/article/details/54408831
        https://www.coder4.com/archives/3844
        """
        import heapq                        # 提供了堆队列算法的实现,默认是最小堆(heap[0]表示最小的元素)
        from heapq import heappush, heappop

        min_heap = []  # 最小堆(每个父节点的值都小于所有子节点的值),存储较大的数据
        max_heap = []  # 最大堆(每个父节点的值都大于所有子节点的值)，存储较小的数据
        res = []

        def heapdelete(heap, value):
            # 删除堆中指定元素
            # 由于heapq不能删除任意元素，所以需要我们自己实现这个方法
            if value == heap[-1]:
                return heap.pop()
            node_index = heap.index(value)
            heap[node_index] = heap[-1]
            heap.pop()
            heapq._siftup(heap, node_index)  # 不断和子节点比，让子节点上浮
            heapq._siftdown(heap, 0, node_index)  # 注意_siftdown是使父节点往下移动

        for i in range(len(nums)): 
            # 构造堆 : 值较小的一半放到最大堆，较大的一半放到最小堆中
            if not min_heap or nums[i] >= min_heap[0]:  # min_heap[0] 是最小堆的最小值
                heappush(min_heap, nums[i])
            else:
                heappush(max_heap, -nums[i])    # 【trick！】 构造最大堆时存入堆、从堆中取出的时候，都用相反数

            # 调整堆大小： (最小堆-最大堆)>=1
            if len(min_heap) > len(max_heap) + 1:
                heappush(max_heap, -heappop(min_heap))   # 最小堆pop出来的是值最小的
            if len(max_heap) > len(min_heap):
                heappush(min_heap, -heappop(max_heap))   # 最大堆pop出来的是值最大的

            # 滑动窗口,获取中位数
            if i >= k - 1:
                # if len(max_heap) + len(min_heap) & 1:  # & 按位与运算，优先级低于+ ?
                if k % 2 == 1:
                    res.append(min_heap[0])
                else:
                    res.append((min_heap[0] - max_heap[0]) / 2.0)

                # 移除首位元素
                delete_num = nums[i - k + 1]
                if delete_num < min_heap[0]:
                    heapdelete(max_heap, -delete_num)
                else:
                    heapdelete(min_heap, delete_num)

                # 调整堆大小： (最小堆-最大堆)>=1
                if len(min_heap) > len(max_heap) + 1:
                    heappush(max_heap, -heappop(min_heap))
                if len(max_heap) > len(min_heap):
                    heappush(min_heap, -heappop(max_heap))
        return res

