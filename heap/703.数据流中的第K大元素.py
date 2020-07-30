"""
数据流中的第K大元素
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

你可以假设 nums 的长度≥ k-1 且k ≥ 1

"""


class KthLargest:

    def __init__(self, k, nums):
        """
        维持一个大小为k的最小堆,存储数据流top k的数据,堆顶就是第k大元素
        每次add+取top k操作的时间复杂度：O(logk)
        边界情况：len(nums) == k - 1
        """
        # if k <= 0 or k > len(nums):
        #     return
        self.k = k
        import heapq
        self.heap = []
        if len(nums) == k - 1:
            for i in range(k - 1):
                heapq.heappush(self.heap, nums[i])
            return
        for i in range(k):
            heapq.heappush(self.heap, nums[i])
        for val in nums[k:]:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)

    def add(self, val: int) -> int:
        import heapq
        # 最小堆元素还不足k个
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        if val > self.heap[0]:
            heapq.heappushpop(self.heap, val)

        return self.heap[0]


if __name__ == '__main__':
    arr = [4, 5, 8, 2]
    s = KthLargest(3, arr)
    assert (s.add(3) == 4)
    assert (s.add(5) == 5)
    assert (s.add(10) == 5)
    assert (s.add(9) == 8)
    assert (s.add(4) == 8)

    arr = []
    s = KthLargest(1, arr)
    assert (s.add(-3) == -3)
    assert (s.add(-2) == -2)
    assert (s.add(-3) == -2)
    assert (s.add(0) == 0)
    assert (s.add(4) == 4)
