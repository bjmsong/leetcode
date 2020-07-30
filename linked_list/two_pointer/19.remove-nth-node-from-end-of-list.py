#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (34.63%)
# Total Accepted:    486.6K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
# 
# Example:
# 
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def removeNthFromEnd(self, head, n):
        """
        快慢指针
        """

        dummy = ListNode(None)
        dummy.next = head
        fast, slow = dummy, dummy

        # fast指针领先n个节点
        for _ in range(n):
            fast = fast.next
            # n大于链表的长度
            if not fast:
                return

        # 当fast指针指向链表尾节点，slow指针指向倒数第n+1个节点
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next


if __name__ == '__main__':
    l = ListNode(None)
    p = l
    for i in [1, 2, 3, 4, 5]:
        p.next = ListNode(i)
        p = p.next

    s = Solution()
    l = s.removeNthFromEnd(l.next, 2)
    while l:
        print(l.val)
        l = l.next

    l = ListNode(None)
    p = l
    for i in [1, 2]:
        p.next = ListNode(i)
        p = p.next

    s = Solution()
    l = s.removeNthFromEnd(l.next, 2)
    while l:
        print(l.val)
        l = l.next
