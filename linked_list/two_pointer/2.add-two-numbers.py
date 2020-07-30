#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (31.12%)
# Total Accepted:    876.4K
# Total Submissions: 2.8M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        l = ListNode(None)
        pos = l
        add = 0
        while l1 or l2:
            sum = add
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            pos.next = ListNode(sum % 10)
            pos = pos.next
            add = sum // 10
        if add > 0:
            pos.next = ListNode(add)
        return l.next

    # def addTwoNumbers(self, l1, l2):
    #     """
    #     [1,8],[0]
    #     [2,4,3],[5,6,4]
    #     """
    #     head = ListNode(0)
    #     pos = head  # 链表指针
    #     add = 0  # 进位
    #     while l1 or l2:
    #         val = add
    #         if l1:
    #             val += l1.val
    #             l1 = l1.next
    #         if l2:
    #             val += l2.val
    #             l2 = l2.next
    #         pos.next = ListNode(val % 10)
    #         add = val // 10
    #         pos = pos.next
    #
    #     if add > 0:
    #         pos.next = ListNode(add)
    #     return head.next


if __name__ == '__main__':
    l1 = ListNode(None)
    p1 = l1
    for i in [2, 4, 3]:
        p1.next = ListNode(i)
        p1 = p1.next

    l2 = ListNode(None)
    p2 = l2
    for i in [5, 6, 4]:
        p2.next = ListNode(i)
        p2 = p2.next

    s = Solution()
    l = s.addTwoNumbers(l1.next, l2.next)
    while l:
        print(l.val)
        l = l.next

    l1 = ListNode(None)
    p1 = l1
    for i in [2, 4, 3]:
        p1.next = ListNode(i)
        p1 = p1.next

    l2 = ListNode(None)
    p2 = l2
    for i in [5, 6, 7]:
        p2.next = ListNode(i)
        p2 = p2.next

    s = Solution()
    l = s.addTwoNumbers(l1.next, l2.next)
    while l:
        print(l.val)
        l = l.next
