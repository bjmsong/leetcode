"""
复制带随机指针的链表

给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。

"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    # def __init__(self):
    #     self.lookup = {}
    #
    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     # 递归
    #     if not head:
    #         return
    #
    #     if self.lookup.get(head):
    #         return self.lookup[head]
    #
    #     node = Node(head.val)
    #     self.lookup[head] = node
    #     node.next = self.copyRandomList(head.next)
    #     node.random = self.copyRandomList(head.random)
    #
    #     return self.copyRandomList(head)

    def copyRandomList(self, head: 'Node') -> 'Node':
        lookup = {}  # 存储新老节点的对应关系
        p1 = head
        clone = Node(0)
        p2 = clone
        # 复制next指针
        while p1:
            p2.next = Node(p1.val)
            lookup[p1] = p2.next
            p1 = p1.next
            p2 = p2.next
        # 复制random指针
        p1 = head
        while p1:
            lookup[p1].random = lookup.get(p1.random) if lookup.get(p1.random) else None
            p1 = p1.next

        return clone.next
