#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (40.13%)
# Total Accepted:    581K
# Total Submissions: 1.4M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, determine if it has a cycle in it.
# 
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
# 
# 
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
# 
# 
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
# 
# 
# 
# 
# 
# 
# 
# Follow up:
# 
# Can you solve it using O(1) (i.e. constant) memory?
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        快慢指针，快指针比慢指针快一倍
        如果有环，快慢指针一定会相遇 => 就像操场跑步套圈
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    # def hasCycle(self, head: ListNode) -> bool:
    #     """
    #     集合：如果链表有环，则某一个节点会被遍历两次
    #     空间复杂度：O(n)
    #     或者用哈希表
    #     :param head:
    #     :return:
    #     """
    #     if not head:
    #         return False
    #     nodes = {head}
    #     head = head.next
    #     while head:
    #         if head in nodes:
    #             return True
    #         else:
    #             nodes.add(head)
    #             head = head.next
    #     return False
