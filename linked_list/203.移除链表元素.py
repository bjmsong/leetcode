"""
删除链表中等于给定值 val 的所有节点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        pos = dummy
        while pos and pos.next:
            while pos.next and pos.next.val == val:
                pos.next = pos.next.next
            pos = pos.next

        return dummy.next