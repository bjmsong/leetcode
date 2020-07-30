#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (29.22%)
# Total Accepted:    252.2K
# Total Submissions: 863.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        原地变换
        - 遍历一遍，得到链表的长度 l
        - k = k % l
        - 将链表截断，长度分别为l-k,k
        - 将两个链表连接起来
        """
        if not head or not head.next or k == 0:
            return head
        l = 0
        pos = head
        while pos:
            l += 1
            pos = pos.next
        k = k % l
        if k == 0:
            return head
        slow = fast = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        head2 = slow.next
        slow.next = None
        pos = head2
        while pos.next:
            pos = pos.next
        pos.next = head
        return head2


