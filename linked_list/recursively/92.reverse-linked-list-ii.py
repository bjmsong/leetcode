#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (37.74%)
# Total Accepted:    253.8K
# Total Submissions: 671.8K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
# Definition for singly-linked list.


class ListNode:
    # https://zhuanlan.zhihu.com/p/86745433?utm_source=

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.successor = None

    def reverseN(self, head, n):
        """
        反转链表的前n个节点
        """
        if n == 1:
            self.successor = head.next
            return head

        last = head.next
        new_head = self.reverseN(head.next, n - 1)
        last.next = head
        head.next = self.successor

        return new_head

    def reverseBetween(self, head, m, n):
        """
        递归，代码简洁
        时间复杂度：o(n)
        空间复杂度：o(n)
        """
        if m == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    # def reverseBetween(self, head, m, n):
    #     dummy = ListNode(-1)
    #     dummy.next = head
    #     pre = dummy
    #     # 找到翻转链表部分的前一个节点, 1->2->3->4->5->NULL, m = 2, n = 4 指的是 节点值为1
    #     for _ in range(m - 1):
    #         pre = pre.next
    #     # 用双指针,进行链表翻转(原地翻转)
    #     node = None     # 翻转后链表的表头
    #     cur = pre.next  # 链表前进的指针
    #     for _ in range(n - m + 1):
    #         tmp = cur.next   # 把下一个结点先保存起来
    #         cur.next = node
    #         node = cur
    #         cur = tmp       # cur指针继续前进
    #     # 将翻转部分 和 原链表拼接
    #     pre.next.next = cur
    #     pre.next = node
    #     return dummy.next


if __name__ == '__main__':
    head = ListNode(None)  # head指针指向链表表头
    pos = head
    for i in [1, 2, 3, 4, 5, 6]:
        node = ListNode(i)
        pos.next = node  # 链表插入结点
        pos = pos.next  # pos指针向前移动

    s = Solution()
    result = s.reverseBetween(head.next, 2, 4)
    while result:
        print(result.val)
        result = result.next
