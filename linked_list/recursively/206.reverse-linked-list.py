#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (60.64%)
# Total Accepted:    899K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively(迭代) or recursively(递归). Could you
# implement both?
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        recursively(递归)
        递归函数的功能：将以head为头节点的链表反转，返回反转后链表的表头
        https://zhuanlan.zhihu.com/p/86745433?utm_source=ZHShareTargetIDMore
        """

        if not head or not head.next:
            return head

        tail = head.next
        head.next = None
        new_head = self.reverseList(tail)
        tail.next = head

        return new_head

    # def reverseList(self, head):
    #     """
    #     每次将链表头节点的下一个节点移动到链表的头部，每个节点只移动一次
    #     时间复杂度：O(n)
    #     空间复杂度：O(1)
    #     :param head:
    #     :return:
    #     """
    #     if not head:
    #         return
    #     dummy = ListNode(None)
    #     dummy.next = head
    #     pos = head
    #     while pos.next:
    #         temp = dummy.next  # 保存链表的表头
    #         dummy.next = pos.next  # 把pos的下一个节点置为表头
    #         pos.next = pos.next.next  # pos下一个指针指向再下一个
    #         dummy.next.next = temp  # 指向原表头
    #
    #     return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = None
    for i in reversed(range(1, 6)):
        pos = ListNode(i)
        pos.next = head
        head = pos
    new = s.reverseList(head)
    while new:
        print(new.val)
        new = new.next
