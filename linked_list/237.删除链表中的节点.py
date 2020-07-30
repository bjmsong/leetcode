"""
删除链表中的节点
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteNode(self, node):
        """
        将node的下一个节点的值赋给node，然后将node.next指向下下一个节点
        时间复杂度：O(1)
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
