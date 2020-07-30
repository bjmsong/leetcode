"""
Q: 反转链表

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        不使用额外空间
        用三个指针分别表示当前节点，前一个节点、后一个节点
        举例：1->2->4
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        p = head  # 当前节点
        p_before = None  # 当前节点的前一个节点
        while p.next:
            p_after = p.next  # 当前节点的后一个节点, 先存起来
            p.next = p_before
            p_before = p
            p = p_after
        p.next = p_before
        return p


if __name__ == '__main__':
    l1 = ListNode(None)
    pos = l1
    for i in [1, 2, 4, 5]:
        pos.next = ListNode(i)
        pos = pos.next
    s = Solution()
    l = s.reverseList(l1.next)
    while l:
        print(l.val)
        l = l.next
