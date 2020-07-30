#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (40.26%)
# Total Accepted:    202.9K
# Total Submissions: 503.5K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        双指针
        把小于x的结点存入一个链表，把大于等于x的结点存入另一个链表，最后拼接
        """
        if not head or not head.next:
            return head
        # small 和 big 之间不能赋值
        small_head = small = ListNode(None)
        big_head = big = ListNode(None)
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        big.next = None
        small.next = big_head.next
        return small_head.next


if __name__ == '__main__':
    head = ListNode(None)  # head指针指向链表表头
    pos = head
    for i in [1, 4, 3, 2, 5, 2]:
        pos.next = ListNode(i)  # 链表插入结点
        pos = pos.next  # pos指针向前移动

    s = Solution()
    result = s.partition(head.next, 3)
    while result:
        print(result.val)
        result = result.next
