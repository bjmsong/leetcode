"""
多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。

"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        """
        递归
        功能：flatten以head为头节点的链表,返回新链表的头指针
        遍历链表，遇到child指针非空的，则先遍历子链表
        :param head:
        :return:
        """
        if not head:
            return head
        flatten_next = self.flatten(head.next)
        if head.child:
            flatten_child = self.flatten(head.child)
            head.next = flatten_child
            flatten_child.prev = head
            # 得到子链表的末尾节点
            while flatten_child.next:
                flatten_child = flatten_child.next
            flatten_child.next = flatten_next
            if flatten_next:
                flatten_next.prev = flatten_child
            head.child = None
        else:
            head.next = flatten_next
            if flatten_next:
                flatten_next.prev = head

        return head
