"""
相交链表

编写一个程序，找到两个单链表相交的起始节点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        - 双指针分别遍历headA+headB，headB+headA
        - 双指针必定会相遇
            - 若两链表相交，则双指针会相遇在交点node
            - 若两链表不相交，则双指针会同时到达链表末尾（null）
        """
        if not headA or not headB:
            return
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB  # if else的精炼写法
            pb = pb.next if pb else headA
        return pa

if __name__ == '__main__':
    pass
