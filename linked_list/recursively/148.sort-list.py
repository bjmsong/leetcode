#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (35.61%)
# Total Accepted:    187.7K
# Total Submissions: 527K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def merge(self, head1, head2):
        """
        按顺序合并两条链表
        """
        if not head1: return head2
        if not head2: return head1

        head = pos = ListNode(0)  # constant space complexity
        while head1 and head2:
            if head1.val < head2.val:
                pos.next = head1
                head1 = head1.next
            else:
                pos.next = head2
                head2 = head2.next
            pos = pos.next

        if head1:
            pos.next = head1
        else:
            pos.next = head2

        return head.next

    def sortList(self, head: ListNode) -> ListNode:
        """
        merge sort， 递归
        - 将链表减半：快慢指针
        - 分别排序减半后的链表
        - 将排序好的两条链表合并
        时间复杂度：O(nlogn)
        空间复杂度：O(1)
        """
        if not head or not head.next:  # 递归基线条件
            return head

        # fast指针走到链表末尾，slow指针走到链表一半
        slow = fast = head
        while fast.next and fast.next.next:  # 注意第一个判断条件不是 slow.next
            slow = slow.next
            fast = fast.next.next

        # 截断链表: head1,head2是截断后的链表的表头指针
        head1 = head
        head2 = slow.next
        slow.next = None

        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)

        return head
