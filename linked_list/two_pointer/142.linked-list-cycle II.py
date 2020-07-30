"""
环形链表 II

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

进阶：
你是否可以不用额外空间解决此题？

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        - 计算出环的节点个数（c），快慢指针
            - 快慢指针不相遇 => 无环
            - 快慢指针相遇 => 有环
                - 再次相遇 => 慢指针走的距离记为环的长度（快指针跑两圈，慢指针跑一圈）
        - 快慢指针
            - 快指针先走c步
            - 快慢指针一起前进
            - 指针相遇的地方即为环的入口
        空间复杂度：O(1)
        """
        slow = fast = head
        has_cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break
        if not has_cycle:
            return

        fast = fast.next.next
        slow = slow.next
        length = 1
        while fast != slow:
            fast = fast.next.next
            slow = slow.next
            length += 1

        slow = fast = head
        for i in range(length):
            fast = fast.next
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast

    # def detectCycle(self, head: ListNode) -> ListNode:
    #     """
    #     哈希表：存储下一个节点
    #     空间复杂度：O(n)
    #     :param head:
    #     :return:
    #     """
