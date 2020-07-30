#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (35.77%)
# Total Accepted:    233.6K
# Total Submissions: 653.1K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Return the linked list sorted as well.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        快慢指针: 快指针负责跳过重复元素，慢指针负责把链表接起来
        """
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and tmp == fast.val:
                    fast = fast.next
            else:
                slow.next = fast  # 结点插入链表
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next


if __name__ == '__main__':
    head = ListNode(None)  # head指针指向链表表头
    pos = head
    for i in [1, 1, 1, 2, 3]:
        node = ListNode(i)
        pos.next = node  # 链表插入结点
        pos = pos.next  # pos指针向前移动

    s = Solution()
    result = s.deleteDuplicates(head.next)
    while result:
        print(result.val)
        result = result.next
