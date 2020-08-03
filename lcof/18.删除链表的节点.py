"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        """
        遍历
        时间复杂度：O(n)
        """
        if not head:
            return head
        if head.val == val:
            return head.next
        fast = head
        slow = ListNode(None)
        slow.next = head
        while fast:
            if fast.val == val:
                slow.next = slow.next.next
                return head
            fast = fast.next
            slow = slow.next
        return head


if __name__ == '__main__':
    s = Solution()
    pos = head = ListNode(None)
    for i in [-1, -3, 5, 99]:
        pos.next = ListNode(i)
        pos = pos.next
    s.deleteNode(head.next, -3)
