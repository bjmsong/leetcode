"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:

输入：[1, 2, 3, 3, 2, 1]
输出：[1, 2, 3]

示例2:

输入：[1, 1, 1, 1, 2]
输出：[1, 2]

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        # 用字典存储节点值
        node = {}
        pos = ListNode(None)
        pos.next = head
        while pos.next:
            if not node.get(pos.next.val):
                node[pos.next.val] = 1
                pos = pos.next
            else:
                pos.next = pos.next.next

        return head