"""
请判断一个链表是否为回文链表。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        - 链表在中间截断
            - 快指针速度比慢指针快一倍
        - 将后一半的链表反转
        - 两个一半的链表以此比较
        """
        if not head or not head.next:
            return True

        slow = ListNode(None)
        slow.next = head
        fast = slow
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:  # 链表长度为奇数
            head2 = slow.next.next
        else:
            head2 = slow.next
        slow.next = None

        def reverseLinkedList(head):
            if not head or not head.next:
                return head
            tail = head.next
            new_head = reverseLinkedList(tail)
            tail.next = head
            head.next = None
            return new_head

        head2 = reverseLinkedList(head2)
        while head:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next

        return True


if __name__ == '__main__':
    s = Solution()
    head = None
    for i in [1, 2, 2, 1]:
        pos = ListNode(i)
        pos.next = head
        head = pos
    print(s.isPalindrome(head))

