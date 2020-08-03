"""
Q:从尾到头打印链表

测试用例：
1 -> 4 -> 0 -> 3: 3 0 4 1
None -> None
1 -> 1
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printListNodeReverse(l):
    stack = []
    while l:
        stack.append(l.val)
        l = l.next

    while stack:
        print(stack.pop())



if __name__ == '__main__':
    l1 = None
    printListNodeReverse(l1)
    print("\n")

    l2 = ListNode(1)
    l2.next = ListNode(4)
    l2.next.next = ListNode(0)
    l2.next.next.next = ListNode(3)
    printListNodeReverse(l2)
    print("\n")

    l3 = ListNode(1)
    printListNodeReverse(l3)
