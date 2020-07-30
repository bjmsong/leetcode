import sys


def input():
    return sys.stdin.readline()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        node = Node(data)
        if head is None:
            head = node
            return head
        pos = head
        while pos.next is not None:
            pos = pos.next
        pos.next = Node(data)
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head);
