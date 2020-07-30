"""
Q: 链表中倒数第k个节点

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。


"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """
        快慢指针，快指针领先慢指针k-1个位置，当快指针达到链表尾节点，慢指针指向倒数第k个节点
        :param head:
        :param k:
        :return:
        """
        if k == 0:
            return ListNode(None)
        if not head:
            return ListNode(None)
        slow = fast = head
        for i in range(k-1):
            if not fast:
                return ListNode(None)
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next

        return slow

if __name__ == '__main__':
    pass
