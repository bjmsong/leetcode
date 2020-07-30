#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (49.01%)
# Total Accepted:    435.8K
# Total Submissions: 889.2K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        多指针, 梳理好交换后节点之间的关系
        :param head:
        :return:
        """
        dummy = ListNode(None)
        dummy.next = head
        pos = dummy
        while pos.next and pos.next.next:
            n1 = pos.next
            n2 = n1.next
            n1.next = n2.next
            n2.next = n1
            pos.next = n2
            pos = n1

        return dummy.next



if __name__ == '__main__':
    l = ListNode(None)
    p = l
    for i in [1, 2, 3, 4]:
        p.next = ListNode(i)
        p = p.next

    s = Solution()
    l = s.swapPairs(l.next)
    while l:
        print(l.val)
        l = l.next
