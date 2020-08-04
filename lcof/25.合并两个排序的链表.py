"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        pos = head
        while l1 and l2:
            if l1.val < l2.val:
                pos.next = l1
                l1 = l1.next
            else:
                pos.next = l2
                l2 = l2.next
            pos = pos.next
        if l1:
            pos.next = l1
        if l2:
            pos.next = l2
        return head.next

    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     """
    #     递归： 每次将指针指向较小的头节点，然后将剩余的链表合并
    #     :param l1:
    #     :param l2:
    #     :return:
    #     """
    #     head = ListNode(None)
    #     pos = head
    #     if not l1:
    #         pos.next = l2
    #         return head.next
    #     if not l2:
    #         pos.next = l1
    #         return head.next
    #     if l1.val < l2.val:
    #         pos.next = l1
    #         pos.next.next = self.mergeTwoLists(l1.next,l2)
    #     else:
    #         pos.next = l2
    #         pos.next.next = self.mergeTwoLists(l1, l2.next)
    #     return head.next


if __name__ == '__main__':
    l1 = ListNode(None)
    pos = l1
    for i in [1, 2, 4]:
        pos.next = ListNode(i)
        pos = pos.next
    l2 = ListNode(None)
    pos = l2
    for i in [1, 3, 5]:
        pos.next = ListNode(i)
        pos = pos.next
    s = Solution()
    l = s.mergeTwoLists(l1.next, l2.next)
    while l:
        print(l.val)
        l = l.next
